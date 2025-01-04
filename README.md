QubikaPytest
This project is a technical challenge implementing automated tests using Selenium and pytest in Python.

Requirements
Python: Ensure you have Python version 3.8 or higher installed. 
You can check the version by running python --version in your terminal. 
If it is not installed, you can download it from the official Python website at python.org/downloads.

pip: This is Python's package manager and should be installed with Python by default. 
Verify its installation by running pip --version.

Selenium: This is required for browser automation and will be installed via the requirements.txt file.

*Following step not needed for lastest version of Selenium*
Webdriver: Depending on the browser you want to use, such as Chrome, you will need the appropriate driver. 
For Chrome, download the ChromeDriver from the official website. Ensure the version of the driver matches your browser version.

Installation
Clone this repository by using the GitHub URL provided.
git clone https://github.com/nahuelvalles/QubikaPytest.git

Optionally: create a virtual environment to isolate the project dependencies. This step is recommended to avoid conflicts with other projects.

Install the required dependencies listed in the requirements.txt file by running pip install with the file as input.
pip install requirements.txt

Running the Tests
Verify that the Webdriver is properly configured and the project dependencies are installed.

Run the tests in terminal:

pytest -m navigation 
  It will execute the TC related to navigate to Qubika's web page and verified the URL it is the expected one and the logo is displayed
  
pytest -m negative
  It will execute the TC where it opens the "Contact Us" button and validate different aspects of the form.

pytest
  It will execute all TCs

Project Structure:

Reports Folder
  Contains the HTML reports from the TCs, no matter if you select to run just "navigate". "negative" or all TCs, there will be a report for each situation.
  
Tests Folder
  conftest.py - contains configuration such as opening and closing of the driver
  test_navigation
  test_negative_testing

Enhancements:
*Page Object Model should be applied
*Data driven TCs

For any inquires, don't hesitate on reach out to me
-Nahuel
