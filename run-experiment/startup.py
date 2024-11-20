import asyncio
import httpx
import json
import requests
import sys
from datetime import datetime
from pathlib import Path
from otii_tcp_client import otii_connection, otii as otii_application
#from otii_tcp_client.arc import Channel
import subprocess

SERVER_URL = "http://10.7.7.168" # change if needed
DATABASE_URL = "http://10.7.7.146" # change if needed

JSON_SCHEMA = "test_schema.json" # change if needed

CLIENT_1_URL = "http://10.0.0.3:5001/trigger" # pending change
CLIENT_2_URL = "http://10.0.0.2:5001/trigger" # pending change
CLIENT_3_URL = "http://10.0.0.5:5001/trigger" # pending change


def create_otii_app(host="127.0.0.1", port=1905):
    # Connect to the Otii 3 application
    connection = otii_connection.OtiiConnection(host, port)
    connect_response = connection.connect_to_server(try_for_seconds=10)
    if connect_response["type"] == "error":
        raise Exception(
            f'Exit! Error code: {connect_response["errorcode"]}, '
            f'Description: {connect_response["payload"]["message"]}'
        )
    otii_app = otii_application.Otii(connection)

    return otii_app
def configure_multimeter(otii_app):
    # Based on the example from
    # https://github.com/qoitech/otii-tcp-client-python/blob/master/examples/basic_measurement.py
    devices = otii_app.get_devices()
    if len(devices) == 0:
        raise Exception("No Arc or Ace connected!")
    device = devices[0]

    # Enable the main current, voltage, and power channels

    #device.enable_channel(Channel.MAIN_CURRENT)
    #device.enable_channel(Channel.MAIN_VOLTAGE)
    #device.enable_channel(Channel.MAIN_POWER)

    #device.set_channel_samplerate(Channel.MAIN_CURRENT, 10000)
    #device.set_channel_samplerate(Channel.MAIN_VOLTAGE, 10000)
    #device.set_channel_samplerate(Channel.MAIN_POWER, 10000)

    device.enable_channel("mc", True)
    device.enable_channel("mv", True)
    device.enable_channel("mp", True)

    device.set_channel_samplerate("mc", 10000)
    device.set_channel_samplerate("mv", 10000)
    device.set_channel_samplerate("mp", 10000)

    # Get the active project
    project = otii_app.get_active_project()

    return project, device


def collect_data(otii_project, device):
    # Get statistics for the recording
    recording = otii_project.get_last_recording()
    info = recording.get_channel_info(device.id, 'mc')
    statistics = recording.get_channel_statistics(device.id, 'mc', info['from'], info['to'])

    current_count = recording.get_channel_data_count(device.id, 'mc')
    voltage_count = recording.get_channel_data_count(device.id, 'mv')
    power_count = recording.get_channel_data_count(device.id, 'mp')

    current_data = recording.get_channel_data(device.id, 'mc', 0, current_count)
    voltage_data = recording.get_channel_data(device.id, 'mv', 0, voltage_count)
    power_data = recording.get_channel_data(device.id, 'mp', 0, power_count)

    # Write to csv
    print("current_data", current_data)
    print("voltage_data", voltage_data)
    print("power_data", power_data)

    # Print the statistics
#    print(f'From:        {info["from"]} s')
#    print(f'To:          {info["to"]} s')
#    print(f'Offset:      {info["offset"]} s')
#    print(f'Sample rate: {info["sample_rate"]}')

#     print(f'Min:         {statistics["min"]:.5} A')
#     print(f'Max:         {statistics["max"]:.5} A')
#     print(f'Average:     {statistics["average"]:.5} A')
#     print(f'Energy:      {statistics["energy"] / 3600:.5} Wh')

# def generate_output(otii_project, device):
#     # Get statistics for the recording
#     recording = otii_project.get_last_recording()
#     minimum, maximum, avg, energy = recording.get_complete_channel_statistics(device, Channel.MAIN_CURRENT)
#     print(f"{Channel.MAIN_CURRENT.name}: {minimum}, {maximum}, {avg}, {energy}", flush=True)

#     for channel in (Channel.MAIN_VOLTAGE, Channel.MAIN_POWER):
#         minimum, maximum, avg = recording.get_complete_channel_statistics(device, channel)
#         print(f"{channel.name}: {minimum}, {maximum}, {avg}", flush=True)


# async def get_async(url):
#     print(f"Starting scenario on {url}...", flush=True)
#     timeout = httpx.Timeout(10.0, read=None)
#     async with httpx.AsyncClient() as client:
#         return await client.get(url, timeout=timeout)
    
async def start_client(url):
    print(f"Starting scenario on {url}...", flush=True)
    timeout = httpx.Timeout(10.0, read=None)
    files = {'upload_file': open(JSON_SCHEMA, 'rb')}
    name = "test_schema.json"
    async with httpx.AsyncClient() as client:
        return await client.post(f"{url}/schema/{name}/start", files=files, timeout=timeout)
    
async def send_schema(url):
    print(f"Sending schema to {url}")
    timeout = httpx.Timeout(10.0, read=None)
    files = {'upload_file': open(JSON_SCHEMA, 'rb')}
    async with httpx.AsyncClient() as client:
        return await client.post(f"{url}/schema", files=files, timeout=timeout)


async def main(scenario_no, otii_project, device, out_path):
    # reset server db
    #print("Clearing DB on remote server...", flush=True)
    #r = requests.get(f"{SERVER_URL}/cleardb") # TODO maybe need similar endpoint

    #if r.ok:
    # start three clients
    print("Starting scenario on three clients...", flush=True)
    start_time = datetime.now()
    client_urls = [CLIENT_1_URL, CLIENT_2_URL, CLIENT_3_URL]

    otii_project.start_recording()



    results = await asyncio.gather(*map(start_client, client_urls))
    print(results, flush=True)

    otii_project.stop_recording()

    t_delta = datetime.now() - start_time
    print(f"Scenario took {t_delta}", flush=True)
    print("Done with scenario...", flush=True)


if __name__ == "__main__":
    # Store it to "../data/out/minitwit3x"

    asyncio.run(start_client("https://webhook.site/3cc9b8cd-3799-4d2d-8f7f-f8093a5ca52d"))

    print("done")

    # out_path = Path("")
    # otii_project, device = configure_multimeter(create_otii_app())
    # print(otii_project, device)
    # print("done setup")

    # print("starting recording")
    # otii_project.start_recording()

    # subprocess.run(["python", "..\src\playwright\main.py", "http://10.7.7.168:5000/", "test_schema.json"])

    # otii_project.stop_recording()

    # print("done recording")

    # collect_data(otii_project, device)

    # project, device = None, None
    #for idx in range(1): # TODO 1 for now for testing
        # Run the scenario 10 times
     #   asyncio.run(main(idx, otii_project, device, out_path))