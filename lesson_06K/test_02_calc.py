from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = wait.until(EC.element_to_be_clickable(
        (By.ID, "delay")
    ))
    delay.click()
    delay.clear()
    delay.send_keys("45")

    btn_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    btn_7.click()

    btn_sum = driver.find_element(By.XPATH, "//span[text()='+']")
    btn_sum.click()

    btn_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    btn_8.click()

    btn_eq = driver.find_element(By.XPATH, "//span[text()='=']")
    btn_eq.click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result_field = driver.find_element(By.CSS_SELECTOR, ".screen")

    assert result_field.text == "15"

    driver.quit()
