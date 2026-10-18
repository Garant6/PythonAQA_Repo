from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    driver.find_element(By.XPATH, "//a [text()='HTML Form']").click()
    # driver.find_element(By.LINK_TEXT, "HTML Form").click()
    # Открыл подсказку только после выполнения задания. Поэтому так добавил этот способ)

    excepted_url = "https://httpbin.qa-territory.online/forms/post"

    assert driver.current_url == excepted_url

    driver.back()
    orig_url = "https://httpbin.qa-territory.online/"

    assert driver.current_url == orig_url

    driver.quit()
