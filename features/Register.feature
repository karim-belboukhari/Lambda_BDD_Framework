Feature: User Registration
  @registration @correct_credentials
  Scenario: Register a new user successfully
    Given the user launches the site
    When the user selects the register option
    And the user fills in the registration fields
    Then the user register successfully

 @registration @empty_fields
 Scenario: Fail to register due to missing required fields
    Given the user launches the site
    When the user selects the register option
    And the user leaves The required fields empty
    Then the user sees an error message for missing required fields



