from selenium.webdriver.common.by import By


class SearchPageLocators (object):
    Search_Bar = (By.CSS_SELECTOR, 'div.home-arrow__search-wrapper input.input__input.mini-suggest__input')
    Results_Dropdown = (By.CSS_SELECTOR, 'div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_flat')
class SearchResultsPageLocators (object):
    ResultsPage = (By.CSS_SELECTOR, 'div.content__left')
class PicturesResultsPageLocators (object):
    Search_Bar = (By.CSS_SELECTOR, 'div.home-arrow__search-wrapper input.input__input.mini-suggest__input')
    Pictures = (By.CSS_SELECTOR, "#content_inner p")