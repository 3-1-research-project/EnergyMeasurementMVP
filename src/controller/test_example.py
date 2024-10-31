import re
from playwright.sync_api import Page, expect
import src.playwright.scenario as scenario

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def testlocalhostexists(page: Page):
    page.goto("http://localhost:5000")
    scenario.Scenario(page).run()
    expect(page).to_have_title(re.compile("Minitwit"))

# def test_docs_has_title(page: Page):
#     page.goto("https://playwright.dev/docs/intro")

#     # Expect a title "to contain" a substring.
#     expect(page).not_to_have_title(re.compile("Playwright"))
