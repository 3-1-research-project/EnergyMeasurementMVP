
    
from scenario_DevopsGroupC import CustomScenario
from playwright.sync_api import sync_playwright
from scenario_DevopsGroupC import PwPage
import argparse

def main(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        scenario = CustomScenario(PwPage(page), url)
        scenario.run()
        print("Done")
        browser.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Playwright scenarios")
    parser.add_argument("url", type=str, help="Port to run the server on")
    args = parser.parse_args()
    print("Url: " + args.url)
    main(args.url)


