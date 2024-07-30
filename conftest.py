import pytest
from playwright.sync_api import Page
from playwright_stealth import stealth_sync

from pages.emag.emag_product.emag_product_page import EmagProductPage


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }


@pytest.fixture()
def emag_product_page(page: Page):
    stealth_sync(page)
    return EmagProductPage(page)