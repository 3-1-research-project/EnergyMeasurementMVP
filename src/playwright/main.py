
from scenario_DevopsGroupC import CustomScenario
from playwright.sync_api import sync_playwright
from scenario_DevopsGroupC import PwPage
import argparse
from schema.schema import validate_schema
from scenario import Scenario

def main(url, schema):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = PwPage(browser.new_page())
        if (schema):
            print("Schema provided")
            validated = validate_schema(schema)
            scenario = parse_scenario_schema(validated, page, url)
            scenario.run()
        else:
            scenario = CustomScenario(page, url)
            scenario.run()

        print("Done")
        browser.close()


def parse_scenario_schema(schema: dict, page: PwPage, url: str) -> Scenario:
    name = schema["project"]
    print(name)
    raise NotImplementedError("Not implemented yet")
    return CustomScenario(page, url)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Playwright scenarios")
    parser.add_argument("url", type=str, help="Port to run the server on")
    parser.add_argument("schema", help="Schema to run the scenario on")
    args = parser.parse_args()
    print("Url: " + args.url)
    print("Schema: " + args.schema)
    main(args.url, args.schema)


