# Client API
This API endpoint allows remote control of clients.

## Documentation
A OpenAPI page is exposed on `{url}/docs`, e.g., `http://localhost:8000/docs`

## How to run
The API is set up to run using VS code. If using another editor, some setup is required to allow debugging, etc.

## Scripts
To setup the clients, run the following script [./scripts/client/client-setup.sh](./scripts/client/client-setup.sh)
To start the clients, run the following script [./scripts/client/client-run.sh](./scripts/client/client-run.sh)

### Using the Command Line
The following command will expose the application on `http://localhost:8000`.

```bash
fastapi dev web.py
```

### Using VS code
The [launch.json](../.vscode/launch.json) contains the configuration, such that the program can be executed by typing `debug client-web-trigger-debugger` into the Command Pallet.
