from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    tags = driver.find_elements(By.TAG_NAME, "a")
    assert len(tags) == 9

    for i, tag in enumerate(tags, 1):
        assert tag.is_displayed()

    text_1 = tags[0]
    assert text_1.text == "1"

    driver.quit()
