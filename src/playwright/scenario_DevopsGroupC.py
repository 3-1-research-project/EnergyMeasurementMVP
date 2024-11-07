
from scenario import Scenario
from config import PwPage, Page

class CustomScenario(Scenario):
    def goToUsersTimeline(self, user):
        print("DC: Going to user's timeline")
        self.getPublicTimeline()
        # Try:
        self.page.press_link(user)
        # If doesn't exist, scroll until it does, if hits bottom throw exeption

    def followUser(self, user):
        print("DC: Following user")
        self.page.navigate_to(self.base + "public")
        print("Navigated to public, try to follow")
        self.page.press_link(user)
        print("Clicked user")
        self.page.press_button("Follow user")
        print("Pressed follow user")

    def unfollowUser(self, user):
        print("DC: Unfollowing user")
        self.page.navigate_to(self.base + "public")
        print("Navigated to public, try to unfollow")
        self.page.press_link(user)
        print("Clicked user")
        self.page.press_button("Unfollow user")
        print("Pressed unfollow user")

    




def test_custom_scenario(page: Page):
    scenario = CustomScenario(PwPage(page))
    scenario.run()