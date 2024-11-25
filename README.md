# EnergyMeasurementMVP
This is work in progress

## Local Execution
To run the setup locally, you need to 

1. Start a postgres database
2. Start a MiniTwit application
3. Start a local test run

### 1. Start the postgres database
To start the postgres database take a look at the the [./database-setups/postgres/README.md](./database-setups/postgres/README.md)

### 2. Start a MiniTwit application
Navigate to the [./minitwit-implementations/](./minitwit-implementations/) folder and start one of the possible implementations

### 3. Init
This is work in progress

## Seeding the database
For some scenarios, the database needs to be pre-seeded, which can be done using the [seed.py](/database-seed/README.md) script. For instructions on running the script, see the corresponding [README.md](/database-seed/README.md).

## Running a test

### Initial Setup

1. Connect the Raspberry Pis as specified in the [connecting-devices.md](./docs/connecting-devices.md) document
2. See [database-setup.md](./docs/database.md) for how to setup the database
3. See [server-setup.md](./docs/server-setup.md) for how to setup the server
4. See [client-setup.md](./docs/client-setup.md) for how to setup the client

### Running the tests
See [how-to-run-tests.md](./docs/how-to-run-tests.md) for how to run the tests

### Collecting and Analyzing the Results
See [collect-and-analyze-results.md](./docs/collect-and-analyze-results.md) for how to collect and analyze results
