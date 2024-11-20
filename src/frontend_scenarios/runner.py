from frontend_scenarios.schema.parser import ScenarioParser
from frontend_scenarios.config import PwPage
from playwright.sync_api import sync_playwright
import argparse
from frontend_scenarios.schema.schema import validate_schema
import logging
from datetime import datetime


def run(url, schema_path, headless=True, log_level=logging.INFO):
    log_filename = datetime.now().strftime("logfile_%Y%m%d_%H%M%S.log")
    logging.basicConfig(filename=log_filename, level=log_level)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        logging.debug("Browser launched")
        page = PwPage(browser.new_page())
        if schema_path != None:
            logging.info("Verifiying schema...")
            validated_schema = validate_schema(schema_path)
            logging.info("Schema validated: " + str(validated_schema["project"]))
            scenario = ScenarioParser(page, url, validated_schema)
            logging.info("Running scenario...")
            scenario.run()
        else:
            raise f"schema_path: {schema_path} does not exist"

        logging.info("Done")
        browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Playwright scenarios")
    parser.add_argument("url", type=str, help="Port to run the server on")
    parser.add_argument("schema", help="Schema to run the scenario on")
    args = parser.parse_args()
    logging.info("Running Playwright scenario")
    logging.info("Url: " + args.url)
    logging.info("Schema: " + args.schema)
    run(args.url, args.schema)
