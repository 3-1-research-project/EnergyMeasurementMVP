# Postgres Docker Setup
To setup the posgres databse you need to run the [postgres.sh](./posgres-setup.sh) or the [postgres.setup.ps1](./postrgres-setup.ps1) script

Once the container is created it can be stopped, started, and removed using standard docker commands

```bash
docker start postgres
docker stop postgres
docker rm postgres
```

## Entering the Container
The container can be entered either through bash `docker exec -it postgres` or using psql `docker exec -it 321 psql -U postgres`

## Connection String
The connection string of the container is:

`UserID=postgres;Password=1234;Host=localhost;Port=5432;Database=postgres;Pooling=true;MinPoolSize=0;MaxPoolSize=100;ConnectionLifetime=0;`
