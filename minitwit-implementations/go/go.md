Most essential requirements with regards to versions:

- Go == 1.22
- Go Module: Gorilla == 1.8.1
- Go Module: PG (lib/pg) == 1.10.9

# Go
The Go project is compiled to two executable, one running the frontend and one running the backend, no other install dependencies.

## How to Build the Executable
The project can be compiled by using the VS Code build-frontend and build-backend task in the [https://github.com/3-1-research-project/Eagles](https://github.com/3-1-research-project/Eagles) repository.

## Transfer the executable
Transfer the build executables to the Raspberry Pi using e.g. the `scp` command.

## Running the project
The Go project can be executed by:

### Update the connection string
Set the following environment variables (Note, this has to be done for both the backend and frontend, as they have to e.g., run in two separate terminals):

```
"DBTYPE": "postgres",
"POSTGRES_USER": "postgres",
"POSTGRES_PW": "1234",
"POSTGRES_HOST": "localhost",
"POSTGRES_PORT": "5432",
"POSTGRES_DB_NAME": "postgres",
"POSTGRES_DISABLE_SSL": "true",
```
### Run the program
If it is the first time running the 
```
chmod +x go-frontend-arm64-raw
chmod +x go-backend-arm64-raw
```

Then the MiniTwit can be started by using the following commands
```bash
./go-frontend-arm64-raw
./go-backend-arm64-raw
```

If everything is setup correctly, you can access the MiniTwit application by navigating to the following URL on the controller computer: `http://<server ip>:15000`

