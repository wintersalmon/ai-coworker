import requests

def fetch_pull_requests(owner: str, repo: str) -> list[str]:
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        headers = {"Accept": "application/vnd.github.v3+json"}
        
        response = requests.get(url, headers=headers)

        is_success = response.status_code == 200

        if not is_success:
            print(f"Failed to fetch PRs. Status Code: {response.status_code}")
            return []
        
        prs = response.json()
        if not prs:
            print("No open pull requests.")
            return []
        
        return [pr['html_url'] for pr in prs]

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch PRs. Error: {e}")
        return []

if __name__ == "__main__":
    # Example usage:
    pull_requests = fetch_pull_requests("wintersalmon", "ai-coworker")
    print("Pull Requests:", pull_requests)
