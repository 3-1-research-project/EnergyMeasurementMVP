import re
from playwright.sync_api import Page, expect
import asyncio


class PwPage:
    def __init__(self, page: Page):
        self.page = page

    async def press_link(self, link_text: str):
        link_selector = f"a:has-text('{link_text}')"
        await self.page.click(link_selector)

    async def submit(self):
        await self.page.click(f"button[type='submit']")

    async def submit_input(self):
        await self.page.click(f"input[type='submit']")

    async def press_button(self, button_name: str):
        button_selector = f"button[name='{button_name}']"
        if not await self.page.is_visible(button_selector):
            button_selector = f"button:has-text('{button_name}')"

        if not button_selector or not await self.page.is_visible(button_selector):
            raise Exception(f"Button '{button_name}' not found")

        await self.page.click(button_selector)

    async def navigate_to(self, url: str):
        await self.page.goto(url)

    async def fill_input(self, input_name: str, value: str):
        input_selector = f"input[name='{input_name}']"
        await self.page.fill(input_selector, value)

    async def get_text(self, selector: str) -> str:
        return await self.page.text_content(selector)
