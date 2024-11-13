import config
# from abc import ABC, abstractmethod

class Scenario():

    # constructor with url
    base: str

    def __init__(self, page: config.PwPage, url: str):
        self.base = url
        self.page = page

    def run(self):
        self.scenario()

    # PuT: Get the public timeline
    def getPublicTimeline(self):
        self.page.navigate_to(self.base + "public")
        

    # SU: Sign up
    def signUp(self, username, email, password):
        
        self.page.press_link("sign up")
        
        self.page.fill_input("Username", username) #Fails Here
        
        self.page.fill_input("Email", email)
        
        self.page.fill_input("Password", password)
        
        self.page.fill_input("Password2", password)
        
        self.page.submit()
        

    # SO: Sign out
    def signOut(self):
        
        self.page.press_link("Sign Out")

    # SI: Sign in
    def signIn(self, username, password):
        
        self.page.navigate_to(self.base)
        
        self.page.press_link("Sign In")
        
        self.page.fill_input("Username", username)
        
        self.page.fill_input("Password", password)
        
        self.page.submit_input()
        

    # UsT: Get user's timeline
    def goToUsersTimeline(self, user):
        
        self.getPublicTimeline()
        
        self.page.press_link(user)

    # MyT: My timeline
    def goToMyTimeline(self):
        
        self.page.navigate_to(self.base)
        self.page.press_link("My Timeline")
        
    # MTW: Make tweet
    def post(self):
        
        self.goToMyTimeline()
        self.page.fill_input("text", "Hello, world!")
        self.page.submit_input()

    # FU: Follow user
    def followUser(self, user):
        
        raise Exception("Not implemented")


    # UFU: Unfollow user
    def unfollowUser(self, user):
        
        raise Exception("Not implemented")


    def scenario(self):
        # --- New User Scenario ---
        self.getPublicTimeline()
        self.goToUsersTimeline("test1")
        self.signUp("test1", "test1@test.com","1234")
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
            self.getPublicTimeline()
            for i in range(3):
                self.followUser("test2")
                self.unfollowUser("test2")
                self.post()
            self.signOut()
            self.signIn("test2", "4321") # With seeded user login, Swap user1 and password1 with login information
            self.goToMyTimeline()
            self.getPublicTimeline()
            for i in range(3):
                self.followUser("test1")
                self.unfollowUser("test1")
                self.post()
            self.signOut()