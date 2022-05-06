# Created by Kate at 4/23/2022
Feature: TESTS FOR AMAZON SEARCH FROM MAIN PAGE

  Scenario: Verify that User can search for coffee
    Given Open Amazon page
    When Search for coffee
    Then Verify search results for coffee are shown