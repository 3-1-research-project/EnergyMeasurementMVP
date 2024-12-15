import argparse
import time
from services.client_service import ClientService
from services.otii_service import OtiiService
import httpx
import asyncio
import os
import json


async def run(urls: str, schema_path: str, minitwit_url: str):

    async def start_scenario_for_client(client_service: ClientService):
        return await client_service.start_scenario(
            schema_name=schema_name, minitwit_url=minitwit_url
        )

    otii_service = OtiiService()

    otii_project, device = otii_service.configure_multimeter()

    client_services = [ClientService(url=url) for url in urls]

    schema_name = os.path.splitext(os.path.basename(schema_path))[0]
    schema_content = get_json_data(schema_path=schema_path)

    is_scenario_uploads_success = [
        client_service.upload_schema(
            schema_name=schema_name, schema_content=schema_content
        )
        for client_service in client_services
    ]

    if False in is_scenario_uploads_success:
        print("One or more schema upload failed, stopping measurement")
        return
    else:
        print(f"Uploads successfull, starting tests")

    print("starting recording")
    otii_project.start_recording()

    time.sleep(5)  # 5 sec delay to get baseline power consumption

    for i in range(5):
        print(f"Starting scenario {i}")

        results = await asyncio.gather(*map(start_scenario_for_client, client_services))

        print(results)
        if False in results:
            print("One or more scenario runs failed, stopping measurement")
            otii_project.stop_recording()
            return

    otii_project.stop_recording()
    print("done recording")

    otii_service.collect_data(otii_project, device, schema_path)


def get_json_data(schema_path: str):
    with open(schema_path, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run an energy measurement test")
    parser.add_argument(
        "client_urls",
        help="Space separated list of urls of the client applications",
        type=lambda arg: arg.split(","),
    )
    parser.add_argument("schema_path", help="Path to the schema used for the scenario")
    parser.add_argument("minitwit_url", help="Url of the MiniTwit application")
    args = parser.parse_args()
    asyncio.run(run(args.client_urls, args.schema_path, args.minitwit_url))
