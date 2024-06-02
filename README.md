# Selenium tests with Behave

## Description 
This project contains tests for automated scenarios on OrangeHRM 
(https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
### Tests included:
1. Add new job: Student or Intern (Go to Admin -> Job - Job Titles -> Click on the Add button):

           Add job title
           Add Job Description: free text up to 20 chars
           Add note
           Save changes

2. Check that your changes are visible on the Job Title page
3. Select your field, click the Delete Selected button and make sure
your field is removed.
## Installation

1. Clone the repository.

2. Install the required packages:
   
 pip install -r requirements.txt

3. Running Tests:

To run the tests and generate a report, use the following command in the terminal:
behave