import argparse
import time
from services.client_service import ClientService
from services.otii_service import OtiiService
import httpx
import asyncio
import os
import json
import paramiko
import datetime


async def run(urls: str, minitwit_url: str, num_cores: str):

    async def start_scenario_for_client(client_service: ClientService):
        return await client_service.start_scenario(minitwit_url=minitwit_url)

    otii_service = OtiiService()

    otii_project, device = otii_service.configure_multimeter()

    print("urls", urls)

    #url_list = urls.split(",")
    new_list = []
    for url in urls:
        url = url.strip()
        for i in range(int(num_cores)):

            list_chars = list(url)
            list_chars[-1] = str(int(list_chars[-1]) + i)
            new_url = "".join(list_chars)
            new_list.append(new_url)

    print(new_list)

    client_services = [ClientService(url=url) for url in new_list]

    # schema_name = os.path.splitext(os.path.basename(schema_path))[0]
    # schema_content = get_json_data(schema_path=schema_path)

    # is_scenario_uploads_success = [
    #     client_service.upload_schema(
    #         schema_name=schema_name, schema_content=schema_content
    #     )
    #     for client_service in client_services
    # ]

    # if False in is_scenario_uploads_success:
    #     print("One or more schema upload failed, stopping measurement")
    #     return
    # else:
    #     print(f"Uploads successfull, starting tests")
    

    # Raspberry Pi SSH details
    HOST = "10.7.7.128" # minitwit_url # "10.7.7.128" 
    USERNAME = "admin"
    PASSWORD = "admin"  # Use SSH keys instead of passwords if possible!

    def get_raspberry_pi_temp():
        command = "cat /sys/class/thermal/thermal_zone0/temp"  # Reads temperature in millidegrees Celsius

        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, username=USERNAME, password=PASSWORD)

        # Execute command
        stdin, stdout, stderr = ssh.exec_command(command)
        temp_output = stdout.read().decode().strip()

        # Close SSH connection
        ssh.close()

        # Convert to degrees Celsius
        if temp_output.isdigit():
            cpu_temp = int(temp_output) / 1000.0
            return cpu_temp
        else:
            raise ValueError("Failed to retrieve valid temperature data.")

    data_name = "python-flask-B-true"

    print("collecting temperature data pre experiment")
    temperature_data_pre_experiment = get_raspberry_pi_temp()
    print("Pre experiment temp: " + str(temperature_data_pre_experiment))

    print("starting recording")
    otii_project.start_recording()

    time.sleep(5)  # 5 sec delay to get baseline power consumption

    for i in range(1): # TODO temp set to 1 instead of 5 to test
        print(f"Starting scenario {i}")

        results = await asyncio.gather(*map(start_scenario_for_client, client_services))

        print(results)
        if False in results:
            print("One or more scenario runs failed, stopping measurement")
            otii_project.stop_recording()
            return

    otii_project.stop_recording()
    print("done recording")

    print("collecting temperature data post experiment")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{data_name}_temperature_{timestamp}.csv", "w") as file:
        file.write(f"CPU Temperature Pre experiment: {temperature_data_pre_experiment}°C\n")
        file.write(f"CPU Temperature Post experiment: {get_raspberry_pi_temp()}°C\n")

    
    otii_service.collect_data(otii_project, device, data_name)


def get_json_data(data_name: str):
    with open(data_name, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run an energy measurement test")
    parser.add_argument(
        "client_urls",
        help="Space separated list of urls of the client applications",
        type=lambda arg: arg.split(","),
    )
    # parser.add_argument("schema_path", help="Path to the schema used for the scenario")
    parser.add_argument("minitwit_url", help="Url of the MiniTwit application")
    parser.add_argument(
        "num_cores", help="Number of cores to use for the test in each client"
    )
    args = parser.parse_args()
    asyncio.run(run(args.client_urls, args.minitwit_url, args.num_cores))
