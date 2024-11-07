
from scenario import Scenario
from config import PwPage, Page

class ScenarioParse(Scenario):
    def __init__(self, page, url, schema: dict):
        super().__init__(page, url)
        self.schema = schema

    def signUp(self, user):
        ...
   

    def parse_and_execute_subtasks(self, subtasks: dict):
        for subtask in subtasks:
            action, params = next(iter(subtask.items()))
            
            match action:
                case "PRESS_LINK":
                    self.page.press_link(params.get("name"))
                case "FILL_INPUT":
                    self.page.fill_input(params.get("name"), params.get("value"))
                case "SUBMIT":
                    self.page.submit()
                case _:
                    print(f"Unknown action: {action}")
       

        