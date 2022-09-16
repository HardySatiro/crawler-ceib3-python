import json
import os
import random
from abc import ABC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from v1.modules.webelement import WebElement


class Driver(ABC):
    """This class is not unstable."""

    def __init__(self):
        with open("./v1/resources/agents.json", "rb") as f:
            agents = json.load(f)

        self.options = Options()
        # Comented line by comment line to see tracker running
        if not os.environ.get("HEADLESS"):
            self.options.add_argument("--headless")
        self.options.add_argument(f"user-agent={random.choice(agents)}")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", True)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.options)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(6000)
        self.driver.set_script_timeout(6000)
        self.driver._web_element_cls = WebElement
