from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "YjYxODJjZTAtNjg2ZS00ZmE1LWI4YTQtZjc4MjQwZTU2MGM2"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/airsworld")

    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "OTE2NjlhNzgtYTc1Ni00ZTE5LWJmMTUtY2YwMDBjM2ZhZGM5"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/vefapi")

    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()