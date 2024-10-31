
from scenario import Scenario
from config import PwPage, Page
import pytest

class CustomScenario(Scenario):
    def goToUsersTimeline(self):
        print("DC: Going to user's timeline")
        self.getPublicTimeline()
        # Try:
        self.page.press_link("a")
        # If doesn't exist, scroll until it does, if hits bottom throw exeption

    def followUser(self, user):
        print("DC: Following user")
        self.page.navigate_to(self.base + "public")
        self.page.press_link(user)
        self.page.press_button("Follow user")

    




def test_custom_scenario(page: Page):
    scenario = CustomScenario(PwPage(page))
    scenario.run()