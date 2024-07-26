# GRPH
## Advanced Jira Analytics

Here's a Python script to connect to Jira, pull issues from a project, analyze attributes like start date and due date, and generate a Gantt chart. This script uses the requests library for Jira API calls and plotly for creating the Gantt chart. Make sure you have requests and plotly installed:


`pip install requests plotly`

## Important Notes:
Authentication: The script uses Basic Authentication with an API token, which is more secure than using a password. Generate an API token from your Jira account and replace API_TOKEN with it.
Jira API Token: You can generate an API token from Jira API tokens.
Project Key: Replace YOUR_PROJECT_KEY with the actual key of the project you want to analyze.
Field Names: Ensure that your Jira project has startDate and dueDate fields. If these fields have different names or you are using custom fields, you will need to adjust the field names in the script accordingly.
Dependencies: Ensure you have requests, pandas, and plotly installed.
