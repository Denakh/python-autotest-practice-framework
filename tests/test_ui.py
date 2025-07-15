from selenium import webdriver

class TestUi:

    def test_something(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        assert True
