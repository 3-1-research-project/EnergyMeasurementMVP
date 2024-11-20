import re
from playwright.sync_api import Page, expect


class PwPage:
    def __init__(self, page: Page):
        self.page = page

    def press_link(self, link_text: str):
        link_selector = f"a:has-text('{link_text}')"
        self.page.click(link_selector)

    def submit(self):
        self.page.click(f"button[type='submit']")

    def submit_input(self):
        self.page.click(f"input[type='submit']")

    def press_button(self, button_name: str):
        button_selector = f"button[name='{button_name}']"
        if not self.page.is_visible(button_selector):
            button_selector = f"button:has-text('{button_name}')"

        if not button_selector or not self.page.is_visible(button_selector):
            raise Exception(f"Button '{button_name}' not found")

        self.page.click(button_selector)

    def navigate_to(self, url: str):
        self.page.goto(url)

    def fill_input(self, input_name: str, value: str):
        input_selector = f"input[name='{input_name}']"
        self.page.fill(input_selector, value)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)
