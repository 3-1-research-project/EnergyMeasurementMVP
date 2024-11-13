from scenario import Scenario
import config
import logging

class ScenarioParser(Scenario):
    def __init__(self, page: config.PwPage, url: str, schema: dict):
        super().__init__(page, url)
        self.schema = schema

    def signUp(self, username, email, password):
        self.parse("SIGN_UP", lambda: super(ScenarioParser, self).signUp(username, email, password), username=username, email=email, password=password)
    
    def followUser(self, user):
        self.parse("FOLLOW_USER", lambda: super(ScenarioParser, self).followUser(user), user=user)

    def getPublicTimeline(self):
        self.parse("GET_PUBLIC_TIMELINE", lambda: super(ScenarioParser, self).getPublicTimeline())

    def signOut(self):
        self.parse("SIGN_OUT", lambda: super(ScenarioParser, self).signOut())

    def signIn(self, username, password):
        self.parse("SIGN_IN", lambda: super(ScenarioParser, self).signIn(username, password), username=username, password=password)

    def goToUsersTimeline(self, user):
        self.parse("GO_TO_USERS_TIMELINE", lambda: super(ScenarioParser, self).goToUsersTimeline(user), user=user)

    def goToMyTimeline(self):
        self.parse("GO_TO_MY_TIMELINE", lambda: super(ScenarioParser, self).goToMyTimeline())

    def post(self):
        self.parse("POST", lambda: super(ScenarioParser, self).post())

    def unfollowUser(self, user):
        self.parse("UNFOLLOW_USER", lambda: super(ScenarioParser, self).unfollowUser(user), user=user)

    def parse(self, task: str, alt: callable, **kwargs):
        tasks = self.schema.get("tasks")
        tasks = tasks.get(task)
        if tasks is None:
            logging.debug('Executing default task %s', task, ", arguments:", kwargs)
            alt()
        else:
            logging.debug('Executing custom task %s', task, ", arguments:", kwargs)
            self.parse_and_execute_subtasks(tasks, **kwargs)

    def parse_and_execute_subtasks(self, subtasks: dict, **kwargs):
        for subtask in subtasks:
            action, params = next(iter(subtask.items()))
            
            match action:
                case "PRESS_LINK":
                    value = params.get("value")
                    if value is None:
                        self.page.press_link(params.get("name"))
                    else:
                        self.page.press_link(kwargs.get(value))
                    
                case "FILL_INPUT":
                    input_name = params.get("name")
                    self.page.fill_input(input_name, kwargs.get(params.get("value")))
                case "SUBMIT":
                    self.page.submit()
                case "PRESS_BUTTON":
                    self.page.press_button(params.get("name"))
                case "SUBMIT_INPUT":
                    self.page.submit_input()
                case "NAVIGATE_TO":
                    self.page.navigate_to(self.base + params.get("url"))
                case _:
                    logging.error('%s Unknown action', action)
