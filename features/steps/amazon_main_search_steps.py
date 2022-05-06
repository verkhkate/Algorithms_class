# STEPS FOR AMAZON SEARCH FROM MAIN PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time

# Scenario: Verify that User can search for coffee
@when('Search for coffee')
def search_for_coffee(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    time.sleep(2)

@then('Verify search results for coffee are shown')
def results_for_coffee_shown(context):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
    print('Test case passed')