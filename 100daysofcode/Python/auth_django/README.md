# Automate login to Django Admin

Small script using Selenium to automate login to a Django app and save the cookie to a txt file.

Information to be written in **auth_dev.py**:
- url
- login
- password
- location for the cookie file

To run this project after cloning it:

- Install pipenv ([more info](https://docs.pipenv.org/install/#installing-pipenv))

```
$ pip3 install --user pipenv
```
 
- Install the project's dependencies:

```
$ pipenv install 
```

- If you get the error *"WebDriverException: Message: 'geckodriver' executable needs to be in PATH"*, download [geckodriver](https://github.com/mozilla/geckodriver/releases), extract it and copy the driver to /usr/local/bin and finally make it executable (chmod +x geckodriver). *([source](https://stackoverflow.com/questions/40188699/webdriverexception-message-geckodriver-executable-needs-to-be-in-path)).*  

- Run:
```
$ pipenv run python login.py 
```