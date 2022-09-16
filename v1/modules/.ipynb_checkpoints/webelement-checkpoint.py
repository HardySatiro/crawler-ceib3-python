from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement

from v1.modules.utils import delay_function


class WebElement(WebElement):
    """Represents a DOM element.

    Generally, all interesting operations that interact with a document will be
    performed through this interface.

    All method calls will do a freshness check to ensure that the element
    reference is still valid.  This essentially determines whether or not the
    element is still attached to the DOM.  If this test fails, then an
    ``StaleElementReferenceException`` is thrown, and all future calls to this
    instance will fail."""

    @delay_function
    def click(self) -> None:
        """Clicks the element."""

        self._execute(Command.CLICK_ELEMENT)

    @delay_function
    def send_keys(self, *value) -> None:
        """Simulates typing into the element.

        :Args:
            - value - A string for typing, or setting form fields.  For setting
              file inputs, this could be a local file path.

        Use this to send simple key events or to fill out form fields::

            form_textfield = driver.find_element(By.NAME, 'username')
            form_textfield.send_keys("admin")

        This can also be used to set file inputs.

        ::

            file_input = driver.find_element(By.NAME, 'profilePic')
            file_input.send_keys("path/to/profilepic.gif")
            # Generally it's better to wrap the file path in one of the methods
            # in os.path to return the actual path to support cross OS testing.
            # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))

        """
        # transfer file to another machine only if remote driver is used
        # the same behaviour as for java binding
        if self.parent._is_remote:
            local_files = list(map(lambda keys_to_send: self.parent.file_detector.is_local_file(str(keys_to_send)),
                                   "".join(map(str, value)).split("\n")))
            if None not in local_files:
                remote_files = []
                for file in local_files:
                    remote_files.append(self._upload(file))
                value = "\n".join(remote_files)

        self._execute(Command.SEND_KEYS_TO_ELEMENT,
                      {"text": "".join(keys_to_typing(value)), "value": keys_to_typing(value)})
