# Created by Kate at 4/24/2022

Feature: TESTS FOR AMAZON HEADER MENU

  Scenario: 'Verify that User is able to click on Header menu links'
    Given Open Amazon page
    When Click the link Best Sellers
    Then Verify that Best Sellers page is opened
    When Click the link Amazon Basics
    Then Verify that Amazon Basics page is opened
    When Click the link Customer Service
    Then Verify that Customer Service page is opened
    When Click the link New Releases
    Then Verify that New Releases page is opened
    When Click the link Today
    Then Verify that Today page is opened
    When Click the link Amazon Home
    Then Verify that Amazon Home page is opened
    When Click the link Books
    Then Verify that Books page is opened
    When Click the link Registry
    Then Verify that Registry page is opened