import os
from selenium import webdriver


class WikiActions:
    def __init__(self):
        """
        Create a Chrome instance
        """
        self._driver = webdriver.Firefox(executable_path=os.getcwd().split("src")[0] + "/public/geckodriver")

    def open_page(self):
        """
        Open the wiki home page
        """
        return self._driver.get("https://en.wikipedia.org/wiki/Main_Page")

    def click_create_account(self):
        """
        Click on create account
        """
        return self._driver.find_element_by_id("pt-createaccount").click()

    def click_login(self):
        """
        Click on login
        """
        return self._driver.find_element_by_id("pt-login").click()

    def set_query(self, query):
        """
        Set your query
        """
        return self._driver.find_element_by_id("searchInput").send_keys(query)

    def click_search(self):
        """
        Press search button
        """
        return self._driver.find_element_by_id("searchButton").click()

    def set_full_screen(self):
        return self._driver.maximize_window()

    def minimize_screen(self):
        return self._driver.minimize_window()

    def close_browser(self):
        """

        Quit driver
        """
        return self._driver.quit()
