import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_add_iphone_to_cart(driver):
    driver.get("https://www.amazon.com")

    # Search for iPhone
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iPhone")
    driver.find_element(By.ID, "nav-search-submit-button").click()

    # Wait for results to load
    wait = WebDriverWait(driver, 10)
    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")))

    # Loop through results to find a valid product
    for result in results:
        try:
            link = result.find_element(By.CSS_SELECTOR, "h2 a")
            href = link.get_attribute("href")
            driver.get(href)
            break
        except:
            continue
    else:
        pytest.fail(" No clickable product link found.")

    # Wait for price and print it
    try:
        price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price span.a-offscreen"))).text
        print(f" iPhone Price: {price}")
    except:
        print("️ Price not found.")

    # Add to cart
    try:
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
        add_to_cart_btn.click()
        print(" iPhone added to cart.")
    except:
        print(" Add to cart button not found.")
