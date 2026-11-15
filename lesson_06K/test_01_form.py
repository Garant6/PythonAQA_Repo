from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form6K():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name= 'address']")
    ))
    address.click()
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.send_keys("test@skypro.com")

    phone_num = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='phone']")
    ))
    phone_num.click()
    phone_num.send_keys("+7985899998787")

    zip_code = wait.until(EC.element_to_be_clickable(
        (By.NAME, "zip-code")
    ))
    zip_code.click()
    zip_code.send_keys("")

    city = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='city']")
    ))
    city.click()
    city.send_keys("Москва")

    country = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='country']")
    ))
    country.click()
    country.send_keys("Россия")

    job_pos = wait.until(EC.element_to_be_clickable(
        (By.NAME, "job-position")
    ))
    job_pos.click()
    job_pos.send_keys("QA")

    company = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='company']")
    ))
    company.click()
    company.send_keys("SkyPro")

    subm_btn = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "btn-outline-primary")
    ))
    subm_btn.click()

    # zip_code = driver.find_element(By.ID, "zip-code")
    # bg_color = zip_code.value_of_css_property("background-color")
    # assert bg_color in ["rgba(255, 0, 0, 1)", "rgb(255, 0, 0)"]

    zip_code_f = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_f.get_attribute("class")

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]

    for g_field_id in green_fields:
        field_elem = driver.find_element(By.ID, g_field_id)

        assert "alert-success" in field_elem.get_attribute("class")

    driver.quit()
