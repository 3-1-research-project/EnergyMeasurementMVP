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


async def run(url, schema_path, headless=True, log_level=logging.INFO):
    logger = logging.getLogger("uvicorn")
    logger.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler = logging.FileHandler(
        os.path.join("logs", datetime.now().strftime("logfile_%Y%m%d_%H%M%S.log"))
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info(f"Logging setup done, start scenario test of schema: {schema_path}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        logger.info("Browser launched")
        page = PwPage(await browser.new_page())
        if schema_path != None:
            logger.info("Verifiying schema...")
            validated_schema = validate_schema(schema_path)
            logger.info("Schema validated: " + str(validated_schema["project"]))
            scenario = ScenarioParser(page, url, validated_schema)
            logger.info("Running scenario...")
            await scenario.run(schema_path)
        else:
            raise f"schema_path: {schema_path} does not exist"

        logger.info(f"Done with scenario with schema: {schema_path}")
        await browser.close()
