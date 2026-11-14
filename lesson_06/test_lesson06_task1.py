from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # start_btn = driver.find_element(By.XPATH, "//button[text()='Start']")
    # start_btn.click()
#Уже после выполнения увидел в подсказке, что нужно найти именно через CSS_SELECTOR и сделал. Оставил как основное.
#Но так же оставил и свой вариант, чтобы вы видели ход моих мыслей. Буду признателен за комментарии))
    start_btn_byCSS = driver.find_element(By.CSS_SELECTOR, "#start button") 
    start_btn_byCSS.click()

    hello_text = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h4[text()='Hello World!']")
    ))
    assert hello_text.is_displayed
    assert hello_text.text == "Hello World!"

    driver.save_screenshot("screenshots/page.png")

    assert hello_text.text == "Hello World!"

#Это взято из тренировки и не понимаю зачем усложнять?
    # text_via_js = driver.execute_script("return arguments[0].textContent;", hello_text)
    # assert text_via_js == "Hello World!"

    driver.quit()