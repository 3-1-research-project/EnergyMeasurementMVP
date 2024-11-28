import httpx
import asyncio


class ClientService:
    url: str

    def __init__(self, url: str):
        self.url = url

    def temp_print_error(self, exception):
        print("ERROR:")
        print(exception.args)
        print(exception.message)

    def is_response_success(self, response) -> bool:
        if response.status_code > 299:
            print(response.text)
            return False
        else:
            return True

    def upload_schema(self, schema_name, schema_content):
        with httpx.Client() as client:
            try:
                response = client.post(
                    f"{self.url}/schema/{schema_name}",
                    json=schema_content,
                    headers={"Content-Type": "application/json"},
                )

                return self.is_response_success(response=response)
            except Exception as e:
                self.temp_print_error(e)
                return False

    async def start_scenario(self, schema_name, minitwit_url) -> bool:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.url}/schema/{schema_name}/start",
                    content=minitwit_url,
                    timeout=None,
                    headers={"Content-Type": "text/plain"},
                )

                return self.is_response_success(response)
            except Exception as e:
                self.temp_print_error(e)
                return False
