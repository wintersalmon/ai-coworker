import requests
import json

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
