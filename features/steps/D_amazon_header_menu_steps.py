# STEPS FOR AMAZON HEADER MENU

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time

# Scenario: 'Verify that User is able to click on Header menu links'
@when('Click the link {my_empty_box}')
def Click_the_link(context, my_empty_box):
    context.driver.find_element_by_xpath(f"//*[contains(@class, 'nav-a') and contains(text() ,'{my_empty_box}')]").click()
    time.sleep(2)


@then('Verify that {my_page} page is opened')
def verify_that_page_opened(context, my_page):
    actual_result = context.driver.title
    print("My Title: ", actual_result)
    # expected_result = context.driver.find_element
    # print("Expected result: ", expected_result)
    # if expected_result == actual_result:
    #     print("Test Passed")
    # else:
    #     print(f"Test Failed: Actual text {actual_result} does not match expected {expected_result}")
    # context.driver.back()