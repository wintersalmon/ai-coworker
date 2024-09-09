from dotenv import load_dotenv, dotenv_values

load_dotenv()

GITHUB_PROJECT_TOKEN_AI_COWORKER = dotenv_values()["GITHUB_PROJECT_TOKEN_AI_COWORKER"]

import requests
import json
import re
from typing import Tuple

# Function A: Generate API request parameters
def generate_github_api_url(pull_request_url: str) -> str:
    """
    Generates the API request URL to post a comment to a GitHub pull request.

    Args:
        pull_request_url (str): The GitHub pull request URL.

    Returns:
        str: The API URL for posting the comment.
    """
    # Extract the repo owner, repo name, and pull request number from the URL
    pattern = r"https://github.com/([^/]+)/([^/]+)/pull/(\d+)"
    match = re.match(pattern, pull_request_url)
    if not match:
        raise ValueError("Invalid GitHub pull request URL")

    owner, repo, pull_number = match.groups()

    # Prepare the API endpoint URL for posting comments
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"

    return api_url


def generate_github_api_params(text_content: str, content_format: str) -> dict:
    """
    Generates the data payload to post a comment to a GitHub pull request.

    Args:
        text_content (str): The content of the comment.
        content_format (str): The format of the content ('plain' or 'markdown').

    Returns:
        dict: The data payload for the comment.
    """
    # Set the content in markdown or plain text based on user input
    if content_format == 'markdown':
        comment_body = text_content
    elif content_format == 'plain':
        comment_body = f"```\n{text_content}\n```"  # Wrap plain text in code block for markdown display
    else:
        raise ValueError("Invalid format. Use 'plain' or 'markdown'")

    # Prepare the comment data
    data = {
        "body": comment_body
    }

    return data

# Function B: Make API request to post the comment
def post_github_pull_request_comment(api_url: str, data: dict, github_token: str) -> str:
    """
    Posts a comment to a GitHub pull request using the pre-generated API URL and data.

    Args:
        api_url (str): The GitHub API endpoint URL for posting the comment.
        data (dict): The comment data to post.
        github_token (str): A GitHub personal access token.

    Returns:
        str: The URL of the created comment.
    """
    # Prepare the request headers with authentication
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send the POST request to the GitHub API to create the comment
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        # Return the URL of the created comment
        comment_url = response.json().get('html_url')
        return comment_url
    else:
        raise Exception(f"Failed to post comment: {response.status_code}, {response.json()}")

text_content = """### **Feedback:**
...
"""

# Example usage
if __name__ == "__main__":
    pull_request_url = "https://github.com/wintersalmon/ai-coworker/pull/1"
    content_format = "markdown"  # or "plain"
    github_token = GITHUB_PROJECT_TOKEN_AI_COWORKER

    

    try:
        # Call function A to generate the API request parameters
        print("Generating API parameters...")
        api_url = generate_github_api_url(pull_request_url)
        data = generate_github_api_params(text_content, content_format)

        print (json.dumps(data, indent=4))

        # Call function B to post the comment
        # print("Posting comment...")
        # comment_url = post_github_pull_request_comment(api_url, data, github_token)
        # print(f"Comment posted: {comment_url}")
    except Exception as e:
        print(f"Error: {e}")
