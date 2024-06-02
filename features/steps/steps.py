import requests
from behave import given, when, then

DROPBOX_API_URL = "https://api.dropboxapi.com/2"
DROPBOX_CONTENT_URL = "https://content.dropboxapi.com/2"

@given('I have a valid access token')
def step_impl(context):
    context.token = 'YOUR_ACCESS_TOKEN_HERE'

@given('I have a file to upload')
def step_impl(context):
    context.file_path = 'path/to/your/file.txt'
    context.upload_path = '/uploaded_file.txt'

@when('I upload the file to Dropbox')
def step_impl(context):
    headers = {
        "Authorization": f"Bearer {context.token}",
        "Dropbox-API-Arg": f'{{"path": "{context.upload_path}", "mode": "add", "autorename": true, "mute": false, "strict_conflict": false}}',
        "Content-Type": "application/octet-stream",
    }
    with open(context.file_path, 'rb') as f:
        context.response = requests.post(f"{DROPBOX_CONTENT_URL}/files/upload", headers=headers, data=f)
    assert context.response.status_code == 200

@then('the file should be successfully uploaded')
def step_impl(context):
    assert context.response.status_code == 200

@given('I have an uploaded file')
def step_impl(context):
    context.upload_path = '/uploaded_file.txt'

@when('I request metadata for the file')
def step_impl(context):
    headers = {
        "Authorization": f"Bearer {context.token}",
        "Content-Type": "application/json",
    }
    data = {
        "path": context.upload_path,
    }
    context.response = requests.post(f"{DROPBOX_API_URL}/files/get_metadata", headers=headers, json=data)
    assert context.response.status_code == 200

@then('the metadata should be returned')
def step_impl(context):
    assert context.response.status_code == 200
    context.metadata = context.response.json()
    assert 'name' in context.metadata

@when('I delete the file from Dropbox')
def step_impl(context):
    headers = {
        "Authorization": f"Bearer {context.token}",
        "Content-Type": "application/json",
    }
    data = {
        "path": context.upload_path,
    }
    context.response = requests.post(f"{DROPBOX_API_URL}/files/delete_v2", headers=headers, json=data)
    assert context.response.status_code == 200

@then('the file should be successfully deleted')
def step_impl(context):
    assert context.response.status_code == 200