# Controller
The controller is responsible for starting an experiment. 
This means that it starts a recording, and then it sends a request to all the clients, telling them to start their scenario. 
Then when every scenario is done, it collects the recording of energy from the power supply, and stores it locally. 

## How to run
To run the controller make sure that the setup is reflective of the experiment (see [README.md](README.md))

Additionally, make sure that the Otii Arc Pro power supply is turned on, and powering the server, while being connected to the device about the experiment. 

When server, clients, database and Otii are all up and running, you can start an experiment by typing

```bash
python controller.py <args.client_urls> <args.schema_path> <args.minitwit_url>
```