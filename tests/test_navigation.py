import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestPositiveScenarios:
    @pytest.mark.navigation
    def test_navigation(self, driver):
        # Navigate to Qubika Website
        driver.get("https://qubika.com/")

        # Validate that the website is displayed correctly, validating: #URL & qubika logo
        actual_url = driver.current_url
        expected_url = "https://qubika.com/"

        logo_element = driver.find_element(By.CLASS_NAME, "logo")
        assert logo_element.is_displayed()
        assert actual_url == expected_url

        #Click ‘Contact us’ button
        contact_button = driver.find_element(By.CSS_SELECTOR, "a.contact-us-modal-open")
        contact_button.click()


        #Validate contact form is displayed - explicit wait due to errors during execution.
        wait = WebDriverWait(driver,15)
        first_name_field = wait.until(ec.visibility_of_element_located((By.ID, "firstname-5e204c31-ede2-4976-a096-6919a081b2df")))
        assert first_name_field.is_displayed() #ADD EXCEPTION TO THIS


        #Email field is displayed
        email_field = driver.find_element(By.ID, "email-5e204c31-ede2-4976-a096-6919a081b2df")
        assert email_field.is_displayed()


        #‘Get in touch’ button is displayed
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        assert submit_button.is_displayed()

