import re
from playwright.sync_api import Page, expect

class PwPage:
    def __init__(self, page: Page):
        self.page = page

    def press_button(self, button_name: str):
        button_selector = f"button[name='{button_name}']"
        self.page.click(button_selector)

    def navigate_to(self, url: str):
        self.page.goto(url)

    def fill_input(self, input_name: str, value: str):
        input_selector = f"input[name='{input_name}']"
        self.page.fill(input_selector, value)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)