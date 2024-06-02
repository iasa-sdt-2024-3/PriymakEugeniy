Feature: Get file metadata from Dropbox

  Scenario: Get file metadata
    Given I have a valid access token
    And I have an uploaded file
    When I request metadata for the file
    Then the metadata should be returned