Feature:

  Scenario: Login with valid parameters
    Given I Launch the browser
    When I open orange HRM LoginPage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must succesfully login to the Dashboard page

  Scenario: Login with invalid parameters
    Given I Launch the browser
    When I open orange HRM LoginPage
    And Enter username "admin" and password "admin"
    And Click on login button
    Then Show message the Invalid credentials

  Scenario Outline: Login with multiples parameters
    Given I Launch the browser
    When I open orange HRM LoginPage
    And Enter username "<ExcelIndex>" and password "<ExcelIndex>"
    And Click on login button
    Then User must succesfully login to the Dashboard page

    Examples:
      | ExcelIndex |
      |          1 |
      |          2 |
      |          3 |
      |          4 |
      |          5 |