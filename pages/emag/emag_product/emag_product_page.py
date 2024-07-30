from playwright.sync_api import Page, expect
from shared.base_page import BasePage
from shared.product_handling import get_products_from_excel, add_product_data
from datetime import datetime

from pages.emag.emag_product.emag_product_page_locators import EmagProductPageLocators

class EmagProductPage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
    
    def load(self) -> None:
        self.page.wait_for_load_state('networkidle')
        self.emag_product_price = self.page.locator(EmagProductPageLocators.EMAG_PRODUCT_PRICE)

    def get_products_from_source(self, file_source: str) -> list:
        return get_products_from_excel(file_source)
    
    def browse_products(self, product_url: str) -> None:
        self.page.goto(product_url)
    
    def get_product_price(self) -> str:
        return self.emag_product_price.text_content()
    
    def add_product_data_in_db(self, product_name: str, product_price: str):
        add_product_data('assets/prices_log.xlsx', product_name, product_price, datetime.now())