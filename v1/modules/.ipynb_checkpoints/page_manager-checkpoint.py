from abc import ABC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command

from v1.modules.utils import delay_function
from v1.modules.webdriver import Driver


class PageManager(Driver, ABC):
    """This class is not unstable."""

    def find(self, attribute, type_attr):
        return self.driver.find_element(*(eval(f"By.{type_attr.upper()}"), attribute))

    def findall(self, attribute, type_attr):

        return self.driver.find_elements(*(eval(f"By.{type_attr.upper()}"), attribute))

    def set_attribute(self, xpath, attribute, value):
        element = self.find(xpath, "xpath")
        self.driver.execute_script(f"arguments[0].setAttribute('{attribute}', '{value}')", element)

    def get_parent_html(self, web_element, xpath):
        """work only xpath"""
        return web_element.find_element_by_xpath(xpath).get_attribute("innerHTML")

    def findall_in_element(self, web_element, attribute, type_attr):

        return eval(f"web_element.find_elements_by_{type_attr.lower()}(attribute)")

    @delay_function
    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(1)
        self.driver.refresh()

    @delay_function
    def open_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank')")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def enter_to_iframe(self, iframe_element):
        self.driver.switch_to.frame(iframe_element)

    def element_is_present(self, attribute, type_attr):
        try:
            self.find(attribute, type_attr)
            return True
        except NoSuchElementException:
            return False

    def has_the_attribute(self, element, attr):
        if not element.get_attribute(attr):
            return False
        else:
            return True

    @delay_function
    @property
    def refresh_this_page(self):
        self.driver.refresh()

    @property
    def close_driver(self):
        self.driver.quit()

    @property
    def current_html(self):
        return self.driver.page_source
