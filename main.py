#open site
from Navigation import Navigation
from productselection import Product
from checkout import Checkout

def test_regression_suit():
    nav = Navigation()
    driver = nav.open_site()
    select = Product(driver)
    select.add_product1()
    checkout = Checkout(driver)
    checkout.place_order()
    select = Product(driver)
    select.add_product2()
    checkout = Checkout(driver)
    checkout.place_order2()

# # Step 1: Open site
# nav=Navigation()
# driver=nav.open_site()
#
# #Step 2: Add first product
# select=Product(driver)
# select.add_product1()
#
# #Step 3: Place first order
# checkout=Checkout(driver)
# checkout.place_order()
#
# #Step 4: Add second product
# select=Product(driver)
# select.add_product2()
#
# #Step 5: Place first order
# checkout=Checkout(driver)
# checkout.place_order2()


