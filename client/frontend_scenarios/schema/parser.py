from frontend_scenarios.scenario import Scenario
import frontend_scenarios.config
import logging
import asyncio


class ScenarioParser(Scenario):
    logger = logging.getLogger("uvicorn")

    def __init__(self, page: frontend_scenarios.config.PwPage, url: str, schema: dict):
        super().__init__(page, url)
        self.schema = schema

    async def signUp(self, username, email, password):
        async def task():
            await super(ScenarioParser, self).signUp(username, email, password),

        await self.parse(
            "SIGN_UP",
            task,
            username=username,
            email=email,
            password=password,
        )

    async def followUser(self, user):
        async def task():
            await super(ScenarioParser, self).followUser(user),

        await self.parse(
            "FOLLOW_USER",
            task,
            user=user,
        )

    async def getPublicTimeline(self):
        async def task():
            await super(ScenarioParser, self).getPublicTimeline()

        await self.parse("GET_PUBLIC_TIMELINE", task)

    async def signOut(self):
        async def task():
            await super(ScenarioParser, self).signOut()

        await self.parse("SIGN_OUT", task)

    async def signIn(self, username, password):
        async def task():
            await super(ScenarioParser, self).signIn(username, password),

        await self.parse(
            "SIGN_IN",
            task,
            username=username,
            password=password,
        )

    async def goToUsersTimeline(self, user):
        async def task():
            await super(ScenarioParser, self).goToUsersTimeline(user),

        await self.parse(
            "GO_TO_USERS_TIMELINE",
            task,
            user=user,
        )

    async def goToMyTimeline(self):
        async def task():
            await super(ScenarioParser, self).goToMyTimeline()

        await self.parse("GO_TO_MY_TIMELINE", task)

    async def post(self):
        async def task():
            await super(ScenarioParser, self).post()

        await self.parse("POST", task)

    async def unfollowUser(self, user):
        async def task():
            await super(ScenarioParser, self).unfollowUser(user),

        await self.parse(
            "UNFOLLOW_USER",
            task,
            user=user,
        )

    async def parse(self, task: str, alt: callable, **kwargs):
        tasks = self.schema.get("tasks")
        tasks = tasks.get(task)
        if tasks is None:
            self.logger.info(f"Executing default task {task}, arguments: {kwargs}")
            await alt()
        else:
            self.logger.info(f"Executing custom task {task}, arguments: {kwargs}")
            await self.parse_and_execute_subtasks(tasks, **kwargs)

    async def parse_and_execute_subtasks(self, subtasks: dict, **kwargs):
        for subtask in subtasks:
            action, params = next(iter(subtask.items()))

            match action:
                case "PRESS_LINK":
                    value = params.get("value")
                    if value is None:
                        await self.page.press_link(params.get("name"))
                    else:
                        await self.page.press_link(kwargs.get(value))

                case "FILL_INPUT":
                    input_name = params.get("name")
                    value = params.get("value")
                    await self.page.fill_input(input_name, kwargs.get(value))
                case "SUBMIT":
                    await self.page.submit()
                case "PRESS_BUTTON":
                    await self.page.press_button(params.get("name"))
                case "SUBMIT_INPUT":
                    await self.page.submit_input()
                case "NAVIGATE_TO":
                    await self.page.navigate_to(self.base + params.get("url"))
                case _:
                    self.logger.error("%s Unknown action", action)
