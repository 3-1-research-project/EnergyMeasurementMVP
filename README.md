# EnergyMeasurementMVP
This is work in progress

## Local Execution
To run the setup locally, you need to 

1. Start a postgres database
2. Start a MiniTwit application
3. Start a local test run

# Experiment Run
Before consulting this guide, make sure you have a physical setup that look like the following

To run a single experiment you need to (Note, your computer is the controller computer):

![](/media/ExperimentDesign-1.png)

## 1. Start the postgres database
To start the postgres database take a look at the [./database-setups/postgres/README.md](./database-setups/postgres/README.md)

## 2. Start the clients
To start the clients take a look at the [./minitwit-implementation/](./client/README.md)

## 3. Setup the Otii Arc Pro
To setup the Otii Arc Pro, start by downloading [https://www.qoitech.com/software/], on the device used as the controller:

- To use the software an account is required, and can be created for free
- Make sure to physically connect the Otii device with the controller computer using the USB-C port on the back of the Otii device
- Then simply login on the software using your account
- In the Otii Software, find the "Create new project"
- If connected correctly through the aforementioned USB-C port, then the device should be visable in the software
- In the upper left corner a "Power On/Off"  icon should be found
- Press this once to power on the device
- Now it is ready to start recordings

Recordings can either be started manually in the software, or through the controller script, which will attempt to start an experiment run.
The controller script can be found at [./controller/controller.py](./controller/controller.py)

## 4. Start a MiniTwit application
To start the server take a look at the readmes in [./minitwit-implementations/](./minitwit-implementations/).

(Any package used was the newest version at 30/11/2024)

## 5. Run the test
Start the [./controller/controller.py] script.

See the readme for more info [./controller/README.md](./controller/README.md)

## 6. Collecting the Results
By running the [./controller/controller.py] script, a .csv file with the name of the timestamp of the run will be created. This has each reading.

Afterwards you can run the [./analysis/notebook.ipynb] notebook, generating different graphs.

Finally, to check whether or not the CPU was throttled, you need to collection the kernel logs from the server Raspberry Pi using the following command or similar:

```powershell
scp admin@<ip>:/var/log/kern.log .\kernel.log
```

