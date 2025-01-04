import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


def validate_required_fields(driver):

    # Validates that all required fields that are empty have corresponding error messages.

    # Locate all required fields
    required_fields = driver.find_elements(By.CSS_SELECTOR, "[required]")

    # Locate all error messages
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".hs-error-msg")

    # Filter the required fields that are empty
    empty_required_fields = [
        field for field in required_fields
        if not field.get_attribute("value") and field.tag_name != "select"
           or (field.tag_name == "select" and not field.is_selected())
    ]

    # Assert the number of errors messages matches the number of empty required fields
    assert len(empty_required_fields) == len(error_messages), (
        f"It was expected {len(empty_required_fields)} error messages, "
        f"but there was {len(error_messages)} instead"
    )

class TestNegativeTesting:
    @pytest.mark.negative
    def test_form(self, driver):
        # Navigate to Qubika Website
        driver.get("https://qubika.com/")

        # 5) Click ‘Get in touch’ button without filling any field
        contact_button = driver.find_element(By.CSS_SELECTOR, "a.contact-us-modal-open")
        contact_button.click()

        # Explicit wait due to issues during execution, (not worth it to add a test_exception)
        wait = WebDriverWait(driver,15)
        submit_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @class='hs-button primary large' and @value='Submit']")))
        submit_button.click()

        # 6) Validate that all mandatory fields have an error message
        validate_required_fields(driver)

        # 8) Write ‘Test name’ on the ‘Name’ field
        name_field = driver.find_element(By.ID, "firstname-5e204c31-ede2-4976-a096-6919a081b2df")
        name_field.send_keys("Test Name") #Shouldn't be hardcoded

        # 9) Click ‘Get in touch’ button
        submit_button.click()

        # 10) Validate that all mandatory fields have an error message except ‘Name’ field
        validate_required_fields(driver)
