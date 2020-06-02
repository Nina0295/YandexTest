from .pages.search_page import SearchPage
import pytest

def test_search_gives_relevant_results(browser):
    link = "https://yandex.ru/"
    page = SearchPage(browser, link)
    page.open()
    page.user_can_enter_data_to_search_bar("Тензор")
    page.results_dropdown_appears()