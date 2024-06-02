Feature: Upload file to Dropbox

  Scenario: Upload a file to Dropbox
    Given I have a valid access token
    And I have a file to upload
    When I upload the file to Dropbox
    Then the file should be successfully uploaded