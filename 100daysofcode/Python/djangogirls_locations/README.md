# Get list of cities from Django Girls Events

Small script using Selenium to automate the process of getting all the cities a Django Girls workshop has happened and save it to a txt file.

Information to be written in **data_source.py**:
- url
- location for the file

TODO:
- [ ] Get city AND date info
- [ ] Get only past of future workshops
- [ ] Export to JSON

How to run this project after cloning it:

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
$ pipenv run python get.py 
```