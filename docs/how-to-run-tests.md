# How To Run Tests
Before the tests can be run, you first need to setup the experiment as specifed in the [README.md](../README.md), and add a schema to the `controller/schemas/` folder (see [how-to-make-a-schema.md](./how-to-make-a-schema.md)).

Once the schema has been to the schemas folder, the test can be started from the controller computer . Note that [tasks.json](../.vscode/tasks.json) and [launch.json](../.vscode/launch.json) contains configuration for running these commands in vscode

```bash
cd controller/
```

```bash
python controller <comma seperated list of client urls> <path to schema file> <url of the minitwit application (server)> <output file name>
```

An example could be

```bash
python controller http://10.7.7.167:8000,http://10.7.7.168:8000,http://10.7.7.169:8000 schemas/my_schema.json http://10.7.7.90:5000 descriptive_file_name
```
