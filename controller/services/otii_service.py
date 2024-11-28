import csv
import datetime
import json
from otii_tcp_client import otii_connection, otii as otii_application


class OtiiService:
    otii_app: any

    def __init__(self, host: str = "127.0.0.1", port: int = 1905):
        connection = otii_connection.OtiiConnection("127.0.0.1", 1905)
        connect_response = connection.connect_to_server(try_for_seconds=10)
        if connect_response["type"] == "error":
            raise Exception(
                f'Exit! Error code: {connect_response["errorcode"]}, '
                f'Description: {connect_response["payload"]["message"]}'
            )
        self.otii_app = otii_application.Otii(connection)

    def configure_multimeter(self) -> tuple[any, any]:
        # Based on the example from
        # https://github.com/qoitech/otii-tcp-client-python/blob/master/examples/basic_measurement.py
        devices = self.otii_app.get_devices()
        if len(devices) == 0:
            raise Exception("No Arc or Ace connected!")
        device = devices[0]

        # Enable the main current, voltage, and power channels

        # device.enable_channel(Channel.MAIN_CURRENT)
        # device.enable_channel(Channel.MAIN_VOLTAGE)
        # device.enable_channel(Channel.MAIN_POWER)

        # device.set_channel_samplerate(Channel.MAIN_CURRENT, 10000)
        # device.set_channel_samplerate(Channel.MAIN_VOLTAGE, 10000)
        # device.set_channel_samplerate(Channel.MAIN_POWER, 10000)

        device.enable_channel("mc", True)
        device.enable_channel("mv", True)
        device.enable_channel("mp", True)

        device.set_channel_samplerate("mc", 10000)
        device.set_channel_samplerate("mv", 10000)
        device.set_channel_samplerate("mp", 10000)

        # Get the active project
        project = self.otii_app.get_active_project()

        return project, device

    def collect_data(self, otii_project, device, schema_path):
        # Get statistics for the recording
        recording = otii_project.get_last_recording()
        # info = recording.get_channel_info(device.id, "mc")
        # statistics = recording.get_channel_statistics(
        #     device.id, "mc", info["from"], info["to"]
        # )

        current_count = recording.get_channel_data_count(device.id, "mc")
        voltage_count = recording.get_channel_data_count(device.id, "mv")
        power_count = recording.get_channel_data_count(device.id, "mp")

        current_data = recording.get_channel_data(device.id, "mc", 0, current_count)
        voltage_data = recording.get_channel_data(device.id, "mv", 0, voltage_count)
        power_data = recording.get_channel_data(device.id, "mp", 0, power_count)

        print("data count")
        print("current: " + str(current_count))
        print("voltage: " + str(voltage_count))
        print("power: " + str(power_count))

        data = {}
        data["current"] = current_data
        data["voltage"] = voltage_data
        data["power"] = power_data
        data["time"] = [
            i / 10000 for i in range(current_count)
        ]  # 10000 is the sample rate

        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        schema = schema_path.split("/")[-1].split(".")[0]

        # Create the filename with the timestamp
        filename = f"{schema}_{timestamp}.json"

        # Write the nested data to a JSON file
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)  # Use indent for pretty formatting

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
