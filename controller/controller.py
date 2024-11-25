import argparse
from services.client_service import ClientService
from services.otii_service import OtiiService
import httpx
import asyncio
import os
import json


def run(urls: str, schema_path: str, minitwit_url: str, output_csv_name: str):
    # otii_service = OtiiService()

    # otii_project, device = otii_service.configure_multimeter()

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
        # TODO stop measurement
        return
    else:
        print(f"Uploads successfull, starting tests")

    # print("starting recording")
    # otii_project.start_recording()

    is_scenario_runs_success = [
        client_service.start_scenario(
            schema_name=schema_name, minitwit_url=minitwit_url
        )
        for client_service in client_services
    ]

    print(f"Is schema run success?: {is_scenario_runs_success}")

    # otii_project.stop_recording()
    # print("done recording")

    # otii_service.collect_data(otii_project, device)

    # TODO: save to csv


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
    parser.add_argument(
        "output_csv_name",
        help="Name of final results in csv format",
        default="results",
    )
    args = parser.parse_args()
    run(args.client_urls, args.schema_path, args.minitwit_url, args.output_csv_name)
