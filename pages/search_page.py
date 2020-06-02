import time
from .base_page import BasePage
from .locators import SearchPageLocators

class SearchPage(BasePage):
        def user_can_enter_data_to_search_bar(self, data_to_search):
            search_bar = self.browser.find_element(*SearchPageLocators.Search_Bar)
            search_bar.send_keys(data_to_search)

        def results_dropdown_appears(self):
            self.is_element_present(*SearchPageLocators.Results_Dropdown)