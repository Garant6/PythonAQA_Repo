from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    orig_url = driver.current_url

    driver.find_element(By.CSS_SELECTOR, "[placeholder='Customer name']").send_keys("Islam")
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    assert driver.current_url != orig_url

    driver.quit()
