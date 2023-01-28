import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        print(":............................Launching Chrome browser........................................")
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)

    elif browser == 'edge':
        print(":.............................Launching Edge browser............................................")
        driver = webdriver.Edge()
        driver.implicitly_wait(5)

    elif browser == 'firefox':
        print(":.............................Launching Firefox browser.............................................")
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

    else:
        print(":............................Launching Default Egde browser........................................")
        driver = webdriver.Edge()
        driver.implicitly_wait(5)

    driver.implicitly_wait(5)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############## pytest htm report##############################
# It is hook for adding Environment Info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commeerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abhilash'


# It is hook for delete/modify Environment Info to HTML report
pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# import pytest
# from selenium import webdriver
#
#
# # @pytest.fixture()
# # def setup():
# #     from selenium.webdriver import ChromeOptions, Chrome
# #     opts = ChromeOptions()
# #     opts.add_experimental_option("detach", True)
# #     driver = Chrome(options=opts)
# #     driver.implicitly_wait(5)
# #     return driver
# @pytest.fixture()
# def setup(browser):
#
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#
#         # from selenium.webdriver import ChromeOptions, Chrome
#         # opts = ChromeOptions()
#         # opts.add_experimental_option("detach", True)
#         # driver = Chrome(options=opts)
#         # driver.implicitly_wait(5)
#
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#         print("launching edge browser.......")
#     return driver
#     # from selenium.webdriver import EdgeOptions, Edge
#     # opts = EdgeOptions()
#     # opts.add_experimental_option("detach", True)
#     # driver = Edge(options=opts)
#     # #driver.implicitly_wait(5)
#
#
# def pytest_addoption(parser):  # this will get the value from command line or CLI/HOOKS
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):  # this will return browser value to setup method
#     return request.config.getoption("--browser")
#
# # elif browser == 'firefox':
# #     from selenium.webdriver import FirefoxOptions, Firefox
# #
# #     opts = FirefoxOptions()
# #     driver = webdriver.Firefox(options=opts)
# #     driver.implicitly_wait(5)
# #     print("launching Firefox browser...............")
