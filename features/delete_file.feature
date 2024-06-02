Feature: Delete file from Dropbox

  Scenario: Delete a file from Dropbox
    Given I have a valid access token
    And I have an uploaded file
    When I delete the file from Dropbox
    Then the file should be successfully deleted