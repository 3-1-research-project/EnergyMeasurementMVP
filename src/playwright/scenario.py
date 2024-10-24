import config
# from abc import ABC, abstractmethod

class Scenario():
    def __init__(self, page: config.PwPage):
        self.page = page

    def run(self):
        print("Starting Playwright scenarios")

        # Start scenario
        self.page.navigate_to("https://playwright.dev/")
        
        self.signup()

        for i in range(5):
            self.post()

        print("Finished Playwright scenarios")

        
    def signup(self):
        print("Signing up")

        self.page.press_button("Get started")
        self.page.fill_input("name", "John Doe")
        
        
    def post(self):
        print("Posting")

        self.page.navigate_to("https://localhost:3000/")
        self.page.fill_input("post", "Hello, world!")
        self.page.press_button("Post")

    