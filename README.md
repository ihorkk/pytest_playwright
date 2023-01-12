# Pytest Playwright Allure

Sample tests with Pytest + Playwright

## Requirements

 - [Python](https://www.python.org)
 - [Playwright](https://playwright.dev)
 - [Allure-reporter](https://pypi.org/project/allure-pytest/)
 

## Setup

1. Clone this repository to your local machine
2. Install environment:
      ```bash
         python -m pip install --upgrade pip
      ```
      ```bash
         pip install pipenv
      ```
      ```bash
         pipenv install --system
      ```
      ```bash
         playwright install chromium
      ```

## Execution

- To run all the tests:
    `pytest`
- To run specific test:
    `pytest -k <name of the test>`
- To generate allure report:
    `allure serve reports`