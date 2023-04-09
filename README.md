# selenium-pytest-pom-project
## Test automation framework with Python Pytest

The project is made for training purposes against the DEMOQA web-site (https://demoqa.com/):

![alt text](https://demoqa.com/images/Toolsqa.jpg)

The project is based on the design pattern of Page Objet Model and Page Factory.

Used technologies in the project:

- Selenium WebDriver
- pytest
- pytest-html for generating reports
- pytest-xdist for execution of multiple test cases in parallel

## Clone repository

```bash
$ git clone https://github.com/VladNachev/selenium-pytest-pom-project.git
```
## TODO
- Describe the test cases ih the suit
- Add more test cases
- RegistrationTest - Test User Registration. **Note:** Corresponding function generates unique credentials each time so the test can be re-used multiple times.
- Add requirement.txt file so all necessary modules could be installed in bulk