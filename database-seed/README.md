# Database seed
This script will seed a database through a Minitwit API.

Note, this script only works if there is both a database and Minitwit application running

## How to run
If you are using VS code, there is a task for running the script. Open the `Command Palet`, type `task seed-run`, and input the values prompted. Once inputted, an integrated terminal will open that shows the progress.

If you are not using VS code, consult the [../.vscode/tasks.json](../.vscode/tasks.json) file or fill out the values and run the following command. (You can find it by looking for `"label": "seed-run"`)

```bash
python seed.py <user register endpoint> <tweet endpoint> <amount of users> <tweet per user>
```

## How to debug
If you want to debug this program and are using VS code, open [../launch.json](../.vscode/launch.json) and fill out the args field with the corresponding fields for your running MiniTwit application. (You can find it by looking for `"name": "seed-debug"`)
