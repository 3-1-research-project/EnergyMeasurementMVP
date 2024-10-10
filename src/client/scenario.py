import requests
import socket
import json
from flask import Flask

app = Flask(__name__)

# Call this for now during testing
api_endpoint = "https://catfact.ninja/fact"

def scenario():
    for _ in range(10):
        r = requests.get(api_endpoint, allow_redirects=True)
        print(r.json())

@app.route('/trigger')
def start_scenario():
    scenario()
    return f"Done running scenario on {socket.gethostname()}."

# local_simulation_setup.py
import sys
import requests
import asyncio
import httpx
# from src.client.scenario import scenario
import threading
from datetime import datetime
from pathlib import Path

# Currently like Helges. Change these
SERVER_URL = "http://10.0.0.4:5000"
CLIENT_1_URL = "https://catfact.ninja/fact" #"http://10.0.0.3:5001/trigger"
CLIENT_2_URL = "https://catfact.ninja/fact" #"http://10.0.0.2:5001/trigger"
CLIENT_3_URL = "https://catfact.ninja/fact" #"http://10.0.0.5:5001/trigger"

async def get_async(url):
    print(f"Starting scenario on {url}...", flush=True)
    timeout = httpx.Timeout(10.0, read=None)
    async with httpx.AsyncClient() as client:
        c = client.get(url, timeout=timeout)
        print(c.json())
        return await c


async def main(scenario_no, out_path):
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
    out_path = "" #Path(sys.argv[0])
    t1 = threading.Thread(target=scenario)
    t2 = threading.Thread(target=scenario)
    t3 = threading.Thread(target=scenario)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    """ for idx in range(10):
        # Run the scenario 10 times
        asyncio.run(main(idx, out_path)) """
        

# scenario.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)



