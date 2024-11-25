import httpx
import asyncio


class ClientService:
    url: str

    def __init__(self, url: str):
        self.url = url

    def is_response_success(self, response) -> bool:
        return False if response.status_code > 299 else True

    def upload_schema(self, schema_name, schema_content):
        with httpx.Client() as client:
            try:
                response = client.post(
                    f"{self.url}/schema/{schema_name}",
                    json=schema_content,
                    headers={"Content-Type": "application/json"},
                )
            except:
                return False

            return self.is_response_success(response=response)

    def start_scenario(self, schema_name, minitwit_url) -> bool:
        with httpx.Client() as client:
            response = client.post(
                f"{self.url}/schema/{schema_name}/start",
                content=minitwit_url,
                timeout=None,
                headers={"Content-Type": "text/plain"},
            )

            return self.is_response_success(response)
