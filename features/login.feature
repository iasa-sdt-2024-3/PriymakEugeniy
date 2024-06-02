Feature: Login and Manage Jobs in OrangeHRM

  Background:
    Given I open the OrangeHRM website
    And I enter the username "Admin"
    And I enter the password "admin123"
    And I click the login button
    And I close the Google OK button if it appears

  Scenario: Add new job title
    Given I am logged in
    When I navigate to the Job Titles page
    And I click the "Add" button
    And I enter job title "Student"
    And I enter job description "Intern position"
    And I enter note "Temporary position"
    And I save the job
    Then I should see "Student" in the job titles list

  Scenario: Delete a job title
    Given I am logged in
    When I navigate to the Job Titles page
    And I select the job title "Student"
    And I click the "Delete" button
    And I confirm the deletion
    Then I should not see "Student" in the job titles list