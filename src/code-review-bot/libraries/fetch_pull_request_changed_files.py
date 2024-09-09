import requests
from libraries.dto.PullRequestChangedFileDTO import PullRequestChangedFileDTO
from libraries.dto.PullRequestMetaDTO import PullRequestMetaDTO
import libraries.create_github_urls as create_github_urls

def fetch_pull_request_changed_files(pullRequest: PullRequestMetaDTO) -> list[PullRequestChangedFileDTO]:

    url = create_github_urls.fetch_pull_request_changed_files(pullRequest)
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch files. Status Code: {response.status_code}")
        return []

    chaged_files = response.json()

    if not chaged_files:
        print("No files changed in the PR.")
        return []

    return [PullRequestChangedFileDTO(filename=file['filename'], patch=file['patch']) for file in chaged_files]

if __name__ == "__main__":
    # Example usage:
    pr = PullRequestMetaDTO(
        owner="wintersalmon",
        repo="ai-coworker",
        pr_number=1
    )
    changed_files = fetch_pull_request_changed_files(pr)
    for file in changed_files:
        print(f"File: {file.filename}")
        print(f"Patch: len({len(file.patch)})")
        print("-" * 50)

