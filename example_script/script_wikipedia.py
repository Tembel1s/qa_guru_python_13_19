from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName": "android",
    "platformVersion": "9.0",
    "deviceName": "Google Pixel 3",
    "app": "bs://sample.app",
    'bstack:options': {
        "projectName": "First Python project",  # Название проекта которое будет отображаться в Browserstack
        "buildName": "browserstack-build-1",  # Название сборки которое будет отображаться в Browserstack
        "sessionName": "BStack first_test",  # Название сессии которое будет отображаться в Browserstack
        "userName": "sergeymelnikov_lA3vhB",
        "accessKey": "CyTRG6CrR2BJrpWDzNw7"  #
    }
})

driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()
search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert (len(search_results) > 0)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
