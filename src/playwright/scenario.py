import config
# from abc import ABC, abstractmethod

class Scenario():
    base = "https://localhost:5000/"

    def __init__(self, page: config.PwPage):
        self.page = page

    def run(self):
        print("Starting Playwright scenarios")
        self.scenario()

    # PuT: Get the public timeline
    def getPublicTimeline(self):
        print("Getting public timeline")
        self.page.navigate_to(self.base + "public")

    # SU: Sign up
    def signUp(self):
        print("Signing up")
        self.page.press_link("Sign Up")
        self.page.fill_input("username", "test2024")
        self.page.fill_input("email", "test@test.com")
        self.page.fill_input("password", "1234")
        self.page.fill_input("password2", "1234")
        self.page.submit()

    # SO: Sign out
    def signOut(self):
        print("Signing out")
        raise Exception("Not implemented")

    # SI: Sign in
    def signIn(self, username, password):
        print("Signing in")
        self.page.navigate_to(self.base)
        self.page.press_link("Sign In")
        self.page.fill_input("username", username)
        self.page.fill_input("password", password)
        self.page.submit()

    # UsT: Get user's timeline
    def goToUsersTimeline(self):
        print("Going to user's timeline")
        raise Exception("Not implemented")

    # MyT: My timeline
    def goToMyTimeline(self):
        print("Going to my timeline")
        self.page.navigate_to(self.base)
        self.page.press_link("My Timeline")
        
    # MTW: Make tweet
    def post(self):
        print("Posting")
        self.goToMyTimeline()
        self.page.fill_input("text", "Hello, world!")
        self.page.submit()

    # FU: Follow user
    def followUser(self):
        print("Following user")
        raise Exception("Not implemented")


    # UFU: Unfollow user
    def unfollowUser(self):
        print("Unfollowing user")
        raise Exception("Not implemented")


    def scenario(self):
        # --- New User Scenario ---
        self.getPublicTimeline()
        self.goToUsersTimeline()
        self.signUp()
        self.signIn("test2024", "1234")
        self.signOut()
        # -------------------------
        for i in range(10):
            self.signIn("test2024", "1234") # With seeded user login, Swap user1 and password1 with login information
            self.goToMyTimeline()
            self.getPublicTimeline()
            for i in range(7):
                self.followUser("a")
                self.post()
            self.signOut()
        # self.goToMyTimeline()
        # self.signOut()