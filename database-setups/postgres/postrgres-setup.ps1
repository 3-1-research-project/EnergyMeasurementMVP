docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=1234 -e POSTGRES_HOST_AUTH_METHOD=trust -d postgres