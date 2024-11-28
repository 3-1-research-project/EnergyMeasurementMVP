import frontend_scenarios.config
import asyncio
import string
import random

# from abc import ABC, abstractmethod


class Scenario:

    # constructor with url
    base: str

    def __init__(self, page: frontend_scenarios.config.PwPage, url: str):
        self.base = url
        self.page = page

    async def run(self):
        await self.scenario()

    # PuT: Get the public timeline
    async def getPublicTimeline(self):
        await self.page.navigate_to(self.base + "public")

    # SU: Sign up
    async def signUp(self, username, email, password):

        await self.page.press_link("sign up")

        await self.page.fill_input("Username", username)  # Fails Here

        await self.page.fill_input("Email", email)

        await self.page.fill_input("Password", password)

        await self.page.fill_input("Password2", password)

        await self.page.submit()

    # SO: Sign out
    async def signOut(self):

        await self.page.press_link("Sign Out")

    # SI: Sign in
    async def signIn(self, username, password):

        await self.page.navigate_to(self.base)

        await self.page.press_link("Sign In")

        await self.page.fill_input("Username", username)

        await self.page.fill_input("Password", password)

        await self.page.submit_input()

    # UsT: Get user's timeline
    async def goToUsersTimeline(self, user):

        await self.getPublicTimeline()
        await self.page.navigate_to(self.base + user)

        # Does not work - creates interleaving
        # await self.page.press_link(user)

    # MyT: My timeline
    async def goToMyTimeline(self):

        await self.page.navigate_to(self.base)

        await self.page.press_link("My Timeline")

    # MTW: Make tweet
    async def post(self):

        await self.goToMyTimeline()

        await self.page.fill_input("text", "Hello, world!")

        await self.page.submit_input()

    # FU: Follow user
    def followUser(self, user):

        raise Exception("Not implemented")

    # UFU: Unfollow user
    def unfollowUser(self, user):

        raise Exception("Not implemented")

    async def scenario(self):
        N = 8
        username1 = "".join(random.choices(string.ascii_uppercase, k=N))
        username2 = username1 + "2"
        password = "1234"

        email1 = username1 + "@test.com"
        email2 = username2 + "@test.com"

        # --- New User Scenario ---
        await self.getPublicTimeline()
        await self.signUp(username1, email1, password)
        await self.signIn(username1, password)
        await self.post()
        await self.signOut()
        await self.signUp(username2, email2, password)
        await self.signIn(username2, password)
        await self.post()
        await self.signOut()
        await self.goToUsersTimeline(username1)
        # -------------------------
        for i in range(10):
            await self.signIn(
                username1, password
            )  # With seeded user login, Swap user1 and password1 with login information
            await self.goToMyTimeline()
            await self.getPublicTimeline()
            for i in range(3):
                await self.goToUsersTimeline(username2)
                await self.followUser(username2)
                await self.unfollowUser(username2)
                await self.post()
            await self.signOut()
            await self.signIn(
                username2, password
            )  # With seeded user login, Swap user1 and password1 with login information
            await self.goToMyTimeline()
            await self.getPublicTimeline()
            for i in range(3):
                await self.goToUsersTimeline(username1)
                await self.followUser(username1)
                await self.unfollowUser(username1)
                await self.post()
            await self.signOut()
