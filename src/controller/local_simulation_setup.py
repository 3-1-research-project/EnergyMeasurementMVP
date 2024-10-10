import sys
import requests
import asyncio
import httpx
from src.client.scenario import scenario
import threading
from datetime import datetime
from pathlib import Path

# Currently like Helges. Change these
SERVER_URL = "http://10.0.0.4:5000"
CLIENT_1_URL = "http://10.0.0.3:5001/trigger"
CLIENT_2_URL = "http://10.0.0.2:5001/trigger"
CLIENT_3_URL = "http://10.0.0.5:5001/trigger"

async def get_async(url):
    print(f"Starting scenario on {url}...", flush=True)
    timeout = httpx.Timeout(10.0, read=None)
    async with httpx.AsyncClient() as client:
        return await client.get(url, timeout=timeout)


async def main(scenario_no, device, out_path):
    # start three clients
    print("Starting scenario on three clients...", flush=True)
    start_time = datetime.now()
    client_urls = [CLIENT_1_URL, CLIENT_2_URL, CLIENT_3_URL]

    results = await asyncio.gather(*map(get_async, client_urls))
    print(results, flush=True)

    t_delta = datetime.now() - start_time
    print(f"Scenario took {t_delta}", flush=True)
    print("Done with scenario...", flush=True)


if __name__ == "__main__":
    # Store it to "../data/out/minitwit3x"
    out_path = Path(sys.argv[1])
    t1 = threading.Thread(target=scenario, args=(0, "client1", out_path))
    t2 = threading.Thread(target=scenario, args=(1, "client2", out_path))
    t3 = threading.Thread(target=scenario, args=(2, "client3", out_path))

    for idx in range(10):
        # Run the scenario 10 times
        asyncio.run(main(idx, out_path))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
