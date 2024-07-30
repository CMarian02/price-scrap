from pages.emag.emag_product.emag_product_page import EmagProductPage

def test_emag_product_page(emag_product_page: EmagProductPage):
    
    emag_product_page.load()
    products = emag_product_page.get_products_from_source('assets/products.xlsx')
    for product_name, product_url in products.items():
        emag_product_page.browse_products(product_url)
        product_price = emag_product_page.get_product_price()
        emag_product_page.add_product_data_in_db(product_name, product_price)


#TODO - BUG
#TODO: Fix the human verification. 
#TODO: Fix when stock for a product is < 3, and price label is different.
#TODO: Fix write bug, if you delete lines in 'price_logs' and script write in file, this is start from last text line, before deletion.