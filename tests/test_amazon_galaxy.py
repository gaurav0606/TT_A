def test_add_galaxy_to_cart(driver):
    driver.get("https://www.amazon.com")

    driver.find_element("id", "twotabsearchtextbox").send_keys("Samsung Galaxy")
    driver.find_element("id", "nav-search-submit-button").click()

    # Click on the first product
    products = driver.find_elements("css selector", "div.s-main-slot div[data-component-type='s-search-result']")
    products[0].find_element("css selector", "h2 a").click()

    # Switch to new tab if opened
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    try:
        price = driver.find_element("css selector", "span.a-price span.a-offscreen").text
        print(f"Galaxy Price: {price}")
    except:
        print(" Could not find Galaxy price.")

    try:
        driver.find_element("id", "add-to-cart-button").click()
        print(" Galaxy device added to cart.")
    except:
        print(" Failed to add Galaxy device to cart.")
