
    
from scenario_DevopsGroupC import CustomScenario
from playwright.sync_api import sync_playwright
from scenario_DevopsGroupC import PwPage


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        scenario = CustomScenario(PwPage(page))
        scenario.run()
        print("Done")
        browser.close()

if __name__ == "__main__":
    main()