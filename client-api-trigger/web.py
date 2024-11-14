import os
from fastapi import FastAPI, HTTPException, Request, Response, status, Path, Body
import json
from functools import wraps
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

NAME_DESCRIPTION = "The name of the schema file"
NAME_EXAMPLE = "my-schema"
SCHEMA_DESCRIPTION = "The schema content"
SCHEMA_EXAMPLE = {}

app = FastAPI()

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return Response(str(e.args), status_code=500)

app.middleware('http')(catch_exceptions_middleware)

def get_schema_file_path_from_name(name: str):
    return os.path.join("..", "src", "schema", f"{name}.json")

@app.get("/schema/{name}/start")
def schema_start():
    # python main minitwit-url
    return {"Hello": "World"}

@app.get("/schema/{name}", status_code=status.HTTP_200_OK) 
def schema_get(name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE)):
    file_path = get_schema_file_path_from_name(name)

    with open(file_path, "r") as file:
        schema = json.load(file)
        return schema

@app.post("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_post(name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE), schema: dict = Body(..., description=SCHEMA_DESCRIPTION, example=SCHEMA_EXAMPLE)):
    file_path = get_schema_file_path_from_name(name)

    with open(file_path, "w") as file:
        file.write(json.dumps(schema))

        return {"schema": json.dump(schema), "name": name}

@app.put("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_post(name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE), schema: dict = Body(..., description=SCHEMA_DESCRIPTION, example=SCHEMA_EXAMPLE)):
    file_path = get_schema_file_path_from_name(name)

    with open(file_path, "w") as file:
        file.write(json.dumps(schema))

        return {"name": name, "schema": schema}

@app.delete("/schema/{name}", status_code=status.HTTP_200_OK)
def schema_delete(name: str = Path(..., description=NAME_DESCRIPTION, example=NAME_EXAMPLE)):
    file_path = get_schema_file_path_from_name(name)
    os.remove(file_path)

    return f"Schema {name} was deleted"
