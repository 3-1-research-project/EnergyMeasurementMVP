from fastapi import (
    FastAPI,
    Request,
    status,
    Path,
    Body,
)
from fastapi.responses import JSONResponse
import json
from frontend_scenarios.runner import run
import os
import logging

NAME_DESCRIPTION = "The name of the schema file"
NAME_EXAMPLE = "my-schema"
SCHEMA_DESCRIPTION = "The schema content"
SCHEMA_EXAMPLE = {}
URL_DESCRIPTION = "The url of the MiniTwit application"
URL_EXAMPLE = "https://10.7.7.167:8080/"
LOGGER = logging.getLogger("uvicorn")


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


create_folder_if_not_exists("logs")
create_folder_if_not_exists("schemas")

app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        status_code=500,
        content={"args": str(exception.args), "message": exception.message},
    )


def get_schema_file_path_from_name(name: str):
    return os.path.join("schemas", f"{name}.json")


@app.post("/schema/{name}/start", status_code=status.HTTP_200_OK)
async def schema_start(
    name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE),
    url: str = Body(..., description=URL_DESCRIPTION, example=URL_EXAMPLE),
):
    await run(url, get_schema_file_path_from_name(name))
    return {"status": "Tests done"}


@app.get("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_get(
    name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE)
):
    file_path = get_schema_file_path_from_name(name)

    with open(file_path, "r") as file:
        schema = json.load(file)
        return schema


@app.post("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_post(
    name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE),
    schema: dict = Body(..., description=SCHEMA_DESCRIPTION, example=SCHEMA_EXAMPLE),
):
    file_path = get_schema_file_path_from_name(name)

    with open(file_path, "w") as file:
        file.write(json.dumps(schema))

        return {"schema": json.dumps(schema), "name": name}


@app.put("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_post(
    name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE),
    schema: dict = Body(..., description=SCHEMA_DESCRIPTION, example=SCHEMA_EXAMPLE),
):
    file_path = get_schema_file_path_from_name(name)

    with open(file_path, "w") as file:
        file.write(json.dumps(schema))

        return {"name": name, "schema": schema}


@app.delete("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_delete(
    name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE)
):
    file_path = get_schema_file_path_from_name(name)
    os.remove(file_path)

    return f"Schema {name} was deleted"
