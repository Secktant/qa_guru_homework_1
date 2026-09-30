import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.mark.chrome
def test_chrome():
    opts = Options()
    url = "https://www.google.com/"
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url

    driver.quit()


@pytest.mark.selenium
def test_selenium_web():
    driver = webdriver.Chrome()
    url = "https://www.selenium.dev/"
    driver.get(url)

    assert driver.title == "Selenium"
    assert driver.current_url == url


@pytest.mark.github
def test_github_web():
    driver = webdriver.Chrome()
    url = "https://github.com/"
    driver.get(url)

    assert driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    assert driver.current_url == url
