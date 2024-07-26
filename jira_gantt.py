import requests
import json
import pandas as pd
import plotly.express as px
from datetime import datetime

# Jira credentials and project details
JIRA_URL = 'https://betby.atlassian.net'
USERNAME = 'a.nazarenko@betby.com'
PASSWORD = 'jhC87DJs87Flk73jhD__Jk3'
API_TOKEN = '9tflsKrkY27Can5dEQP5P36lYodHo9Z94UJyMHZQmoN1jKkjn4B8Rb1G5lZE8I0Z6dcrv9wfgFpVWJDOv2RczXBCqVk1LqYYn4hqMyRLWAzqPkxQuw2PIDbTs7reJNltlv5aMf5CqpWRhQqLNEhDS22K54yDOYTzq4nFVIxIByNpVHh8xqE6ecSyyVnqaOfT'
PROJECT_KEY = 'FRONT'

# Function to fetch issues from Jira
def fetch_issues(jira_url, username, api_token, project_key):
    url = f"{jira_url}/rest/api/2/search"
    headers = {
        "Accept": "application/json"
    }
    auth = (username, api_token)
    query = {
        'jql': f'project={project_key}',
        'fields': 'summary,startDate,dueDate'
    }

    response = requests.get(url, headers=headers, params=query, auth=auth)
    
    if response.status_code == 200:
        return response.json()['issues']
    else:
        print(f"Failed to fetch issues: {response.status_code}, {response.text}")
        return []

# Function to process issues into a DataFrame
def process_issues(issues):
    data = []
    for issue in issues:
        summary = issue['fields'].get('summary', 'No summary')
        start_date = issue['fields'].get('startDate')
        due_date = issue['fields'].get('dueDate')
        
        if start_date and due_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            data.append({
                'Task': summary,
                'Start': start_date,
                'Finish': due_date
            })
    
    return pd.DataFrame(data)

# Fetch issues from Jira
issues = fetch_issues(JIRA_URL, USERNAME, API_TOKEN, PROJECT_KEY)

# Process issues into a DataFrame
df = process_issues(issues)

# Generate Gantt chart using Plotly
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Project Gantt Chart")
fig.update_yaxes(categoryorder="total ascending")
fig.update_layout(xaxis_title="Date", yaxis_title="Task")

# Save the Gantt chart as a PNG file
fig.write_image("gantt_chart.png")

print("Gantt chart saved as gantt_chart.png")
