QubikaPytest
This project is a technical challenge implementing automated tests using Selenium and pytest in Python.

************************************************************************
REQUIREMENTS AND HOW TO RUN TCs (Visual Studio Code / Pycharm)

Visual Studio Code:

Download repository or clone it
Install python in your machine

*Make sure you are located on project's root folder for the following steps*

Within IDE terminal execute: 
	pip install python
	pip install pytest
	pip install selenium
	python -m venv venv
	.\venv\Scripts\activate
	pip install requirements.txt

Now you can go to the "Tests" view on the left side to interact with the different Test Cases
or execute the following commands

python -m pytest -m navigation -> Run "Navigation" TC 
python -m pytest -m negative -> Run "Negative" TC
python -m pytest -> Run all TCs

-----------------------------------------------------
Pycharm:


Download or clone repo:

git clone https://github.com/nahuelvalles/QubikaPytest.git

once you are in Pycharm's terminal and located in QubikaPytest folder run these commands:

	python -m venv virtualenv
	.\virtualenv\Scripts\activate
	pip install -r requirements.txt

Now you can run the TCs by using following commands:

pytest -m navigation -> Run "Navigation" TC 
pytest -m negative -> Run "Negative" TC
pytest -> Run all TCs

************************************************************************
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
