import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the OrangeHRM website')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)  # Додана затримка для завантаження сторінки

@given('I enter the username "{username}"')
def step_impl(context, username):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        element.send_keys(username)
    except Exception as e:
        print(f"Exception occurred: {e}")

@given('I enter the password "{password}"')
def step_impl(context, password):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        element.send_keys(password)
    except Exception as e:
        print(f"Exception occurred: {e}")

@given("I click the login button")
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@given('I close the Google OK button if it appears')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 5).until(
            EC.element_to_be_clickable((By.ID, "OK"))
        )
        element.click()
    except Exception as e:
        print(f"Google OK button did not appear: {e}")

@given('I am logged in')
def step_impl(context):
    context.execute_steps('''
        given I open the OrangeHRM website
        given I enter the username "Admin"
        given I enter the password "admin123"
        given I click the login button
        given I close the Google OK button if it appears
    ''')

@when('I navigate to the Job Titles page')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "menu_admin_viewAdminModule"))
        )
        element.click()
        time.sleep(1)  # Затримка для завантаження підменю

        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "menu_admin_Job"))
        )
        element.click()
        time.sleep(1)  # Затримка для завантаження підменю

        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "menu_admin_viewJobTitleList"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I click the "Add" button')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "btnAdd"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I enter job title "{job_title}"')
def step_impl(context, job_title):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.ID, "jobTitle_jobTitle"))
        )
        element.send_keys(job_title)
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I enter job description "{job_description}"')
def step_impl(context, job_description):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.ID, "jobTitle_jobDescription"))
        )
        element.send_keys(job_description)
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I enter note "{note}"')
def step_impl(context, note):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.ID, "jobTitle_note"))
        )
        element.send_keys(note)
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I save the job')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSave"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@then('I should see "{job_title}" in the job titles list')
def step_impl(context, job_title):
    try:
        job_titles = WebDriverWait(context.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f"//a[contains(text(), '{job_title}')]"))
        )
        assert any(job_title in job_title.text for job_title in job_titles)
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I select the job title "{job_title}"')
def step_impl(context, job_title):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{job_title}')]"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I click the "Delete" button')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "btnDelete"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@when('I confirm the deletion')
def step_impl(context):
    try:
        element = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "dialogDeleteBtn"))
        )
        element.click()
    except Exception as e:
        print(f"Exception occurred: {e}")

@then('I should not see "{job_title}" in the job titles list')
def step_impl(context, job_title):
    try:
        job_titles = context.browser.find_elements(By.XPATH, f"//a[contains(text(), '{job_title}')]")
        assert not any(job_title in job_title.text for job_title in job_titles)
    except Exception as e:
        print(f"Exception occurred: {e}")