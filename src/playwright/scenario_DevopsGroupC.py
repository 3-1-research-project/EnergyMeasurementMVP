
from scenario import Scenario
from config import PwPage, Page

class CustomScenario(Scenario):
    def __init__(self, page, url):
        super().__init__(page, url)

    def goToUsersTimeline(self, user):
        self.getPublicTimeline()
        # Try:
        self.page.press_link(user)

    def followUser(self, user):
        self.page.navigate_to(self.base + "public")
        self.page.press_link(user)
        self.page.press_button("Follow user")

    def unfollowUser(self, user):
        self.page.navigate_to(self.base + "public")
        self.page.press_link(user)
        self.page.press_button("Unfollow user")

    




def test_custom_scenario(page: Page):
    scenario = CustomScenario(PwPage(page))
    scenario.run()