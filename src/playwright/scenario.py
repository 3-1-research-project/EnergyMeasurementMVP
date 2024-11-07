import config
# from abc import ABC, abstractmethod

class Scenario():

    # constructor with url




    base: str

    def __init__(self, page: config.PwPage, url: str):
        self.base = url
        self.page = page

    def run(self):
        # print("Starting Playwright scenarios")
        self.scenario()

    # PuT: Get the public timeline
    def getPublicTimeline(self):
        # print("Getting public timeline")
        self.page.navigate_to(self.base + "public")
        # print("Navigated to public")

    # SU: Sign up
    def signUp(self, username, email, password):
        # print("Signing up")
        self.page.press_link("sign up")
        # print("clicked sign up")
        self.page.fill_input("Username", username) #Fails Here
        # print("filled username")
        self.page.fill_input("Email", email)
        # print("filled email")
        self.page.fill_input("Password", password)
        # print("filled password")
        self.page.fill_input("Password2", password)
        # print("filled password2")
        self.page.submit()
        # print("submitted")

    # SO: Sign out
    def signOut(self):
        # print("Signing out")
        self.page.press_link("Sign Out")

    # SI: Sign in
    def signIn(self, username, password):
        # print("Signing in")
        self.page.navigate_to(self.base)
        # print("Navigated to base")
        self.page.press_link("Sign In")
        # print("Clicked Sign In")
        self.page.fill_input("Username", username)
        # print("Filled username")
        self.page.fill_input("Password", password)
        # print("Filled password")
        self.page.submit_input()
        # print("Submitted")

    # UsT: Get user's timeline
    def goToUsersTimeline(self):
        # print("Going to user's timeline")
        raise Exception("Not implemented")

    # MyT: My timeline
    def goToMyTimeline(self):
        # print("Going to my timeline")
        self.page.navigate_to(self.base)
        self.page.press_link("My Timeline")
        
    # MTW: Make tweet
    def post(self):
        # print("Posting")
        self.goToMyTimeline()
        self.page.fill_input("text", "Hello, world!")
        self.page.submit_input()

    # FU: Follow user
    def followUser(self):
        # print("Following user")
        raise Exception("Not implemented")


    # UFU: Unfollow user
    def unfollowUser(self):
        # print("Unfollowing user")
        raise Exception("Not implemented")


    def scenario(self):
        # --- New User Scenario ---
        self.getPublicTimeline()
        self.goToUsersTimeline("test1")
        self.signUp("test1", "test1@test.com","1234")
        # print("Signed up")
        self.signIn("test1", "1234")
        self.post()
        self.signOut()
        self.signUp("test2", "test2@test.com", "4321")
        self.signIn("test2", "4321")
        self.post()
        self.signOut()
        # -------------------------
        for i in range(10):
            self.signIn("test1", "1234") # With seeded user login, Swap user1 and password1 with login information
            self.goToMyTimeline()
            # print("Going to test1 timeline")
            self.getPublicTimeline()
            for i in range(3):
                self.followUser("test2")
                self.unfollowUser("test2")
                self.post()
            self.signOut()
            self.signIn("test2", "4321") # With seeded user login, Swap user1 and password1 with login information
            self.goToMyTimeline()
            # print("Going to test2 timeline")
            self.getPublicTimeline()
            for i in range(3):
                self.followUser("test1")
                self.unfollowUser("test1")
                self.post()
            self.signOut()
        # self.goToMyTimeline()
        # self.signOut()