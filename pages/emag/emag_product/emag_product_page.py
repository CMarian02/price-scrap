from playwright.sync_api import Page, expect
from shared.base_page import BasePage
from shared.product_handling import get_products_from_excel, add_product_data

from pages.emag.emag_product.emag_product_page_locators import EmagProductPageLocators

class EmagProductPage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
    
    def load(self) -> None:
        self.page.wait_for_load_state('networkidle')
        self.emag_product_price = self.page.locator(EmagProductPageLocators.EMAG_PRODUCT_PRICE)
