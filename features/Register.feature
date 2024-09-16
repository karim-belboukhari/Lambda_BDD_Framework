Feature: User Registration

  Scenario: Register a new user successfully
    Given the user launches the site
    When the user selects the register option
    And the user fills in the registration fields
    Then the user register successfully
