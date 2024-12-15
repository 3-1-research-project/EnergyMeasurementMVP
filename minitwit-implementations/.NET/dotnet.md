Most essential requirements with regards to versions:

- .NET 8
- .NET Nuget Package: Microsoft.EntityFrameworkCore == 8.0.2
- .NET Nuget Package: Npgsql.EntityFrameworkCore.PostgreSQL == 8.0.2
- .NET Nuget Package: Microsoft.EntityFrameworkCore.Design == 8.0.2
- .NET Nuget Package: Microsoft.EntityFrameworkCore.Tools == 8.0.2


# .NET
The .NET (C#) project is compiled to a self contained executable, so no pre-installing of dependencies is needed. 

## Build the executable
The project can be compiled by using the VS Code publish task in the [https://github.com/3-1-research-project/DevopsGroupC](https://github.com/3-1-research-project/DevopsGroupC) repository.

## Transfer the executable
Transfer the build executable folder to the Raspberry Pi using e.g. the `scp` command.

## Running the project
The .NET project can be executed by:

### Update the Connection String
On the server open the `appsettings.json` file and update the host of the connection string with the ip of the database. An example is given below

```bash
nano appsettings.json
```

Change
```json
{
 ...
  "ConnectionStrings": {
    "DefaultConnection": "UserID=postgres;Password=1234;Host=localhost;Port=5432;Database=postgres;Pooling=true;MinPoolSize=0;MaxPoolSize=100;ConnectionLifetime=0;"
  },
  ...
}
```

To
```json
{
 ...
  "ConnectionStrings": {
    "DefaultConnection": "UserID=postgres;Password=1234;Host=<INSERT DATABASE IP HERE>;Port=5432;Database=postgres;Pooling=true;MinPoolSize=0;MaxPoolSize=100;ConnectionLifetime=0;"
  },
  ...
}
```

### Run the program
If it is the first time running the 
```
chmod +x csharp-minitwit
```

Then the MiniTwit can be started by using the following commands
```bash
./csharp-minitwit
```

If everything is setup correctly, you can access the MiniTwit application by navigating to the following URL on the controller computer: `http://<server ip>:5000`
