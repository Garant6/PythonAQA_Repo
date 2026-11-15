from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "user-name")
    )).send_keys("standard_user")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "password")
    )).send_keys("secret_sauce")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "login-button")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_link")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "first-name")
    )).send_keys("Islam")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "last-name")
    )).send_keys("Garant")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "postal-code")
    )).send_keys("47563")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "continue")
    )).click()

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")

    assert total.text[7:] == "$58.29"

    driver.quit()
