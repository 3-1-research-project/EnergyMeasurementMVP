from frontend_scenarios.schema.parser import ScenarioParser
from frontend_scenarios.config import PwPage
from playwright.sync_api import sync_playwright
import argparse
from frontend_scenarios.schema.schema import validate_schema
import logging
from datetime import datetime
import os
import asyncio
from playwright.async_api import async_playwright


async def run(url, schema_path, headless=True, log_level=logging.DEBUG):
    logging.basicConfig(
        filename=os.path.join(
            "logs", datetime.now().strftime("logfile_%Y%m%d_%H%M%S.log")
        ),
        level=log_level,
    )
    logging.info("Logging setup done")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        logging.debug("Browser launched")
        page = PwPage(await browser.new_page())
        if schema_path != None:
            logging.info("Verifiying schema...")
            validated_schema = validate_schema(schema_path)
            logging.info("Schema validated: " + str(validated_schema["project"]))
            scenario = ScenarioParser(page, url, validated_schema)
            logging.info("Running scenario...")
            await scenario.run()
        else:
            raise f"schema_path: {schema_path} does not exist"

        logging.info("Done")
        await browser.close()


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Run Playwright scenarios")
#     parser.add_argument("url", type=str, help="Port to run the server on")
#     parser.add_argument("schema", help="Schema to run the scenario on")
#     args = parser.parse_args()
#     logging.info("Running Playwright scenario")
#     logging.info("Url: " + args.url)
#     logging.info("Schema: " + args.schema)
#     run(args.url, args.schema)
