Feature:

  Scenario: add user role admin
    Given I Launch the browser
    When Enter username "admin" and password "admin123" and click on login button
    And User must succesfully login to the Dashboard page
    When enter dashborar page click in Admin option
    And click in the button add
    Then fill all fields in the form and save the user