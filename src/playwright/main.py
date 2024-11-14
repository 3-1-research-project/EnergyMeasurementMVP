from schema.parser import ScenarioParser
from scenario_DevopsGroupC import DefaultScenario
from playwright.sync_api import sync_playwright
from scenario_DevopsGroupC import PwPage
import argparse
from schema.schema import validate_schema
import logging


def main(url, schema_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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
            scenario = DefaultScenario(page, url)
            logging.info("Running default scenario...")
            scenario.run()

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
    main(args.url, args.schema)
