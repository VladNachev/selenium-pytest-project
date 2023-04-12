# selenium-pytest-pom-project
## Test automation framework with Python Pytest

The project is made for training purposes against the DEMOQA Book Store app (https://demoqa.com/books):

![alt text](https://demoqa.com/images/Toolsqa.jpg)

The project is based on the design pattern of Page Objet Model and Page Factory. It contains some very basics tests. The goal of the project was to implement the Page Object Model with Pytest.

Used technologies in the project:

- Selenium WebDriver
- pytest
- pytest-html for generating reports
- pytest-xdist for execution of multiple test cases in parallel

## Clone repository

```bash
$ git clone https://github.com/VladNachev/selenium-pytest-pom-project.git
```
## Test cases
- test_login_page.py
- test_logout_page.py
- test_invalid_login.py
- test_profile_page.py
- test_add_remove_books.py