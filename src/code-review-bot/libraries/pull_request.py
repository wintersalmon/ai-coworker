import requests
import json

def get_github_prs(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        prs = response.json()
        if prs:
            for pr in prs:
                print(json.dumps(pr, indent=2))
                print(f"PR Title: {pr['title']}")
                print(f"PR URL: {pr['html_url']}")
                print(f"User: {pr['user']['login']}")
                print(f"Created At: {pr['created_at']}")
                print("-" * 50)
        else:
            print("No open pull requests.")
    else:
        print(f"Failed to fetch PRs. Status Code: {response.status_code}")

# Example usage:
get_github_prs("wintersalmon", "ai-coworker")

# def get_github_pr_detail(owner, repo, pr_number):
#     url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
#     headers = {"Accept": "application/vnd.github.v3+json"}
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         pr = response.json()
#         print(f"PR Title: {pr['title']}")
#         print(f"PR Number: {pr['number']}")
#         print(f"PR State: {pr['state']}")
#         print(f"User: {pr['user']['login']}")
#         print(f"Created At: {pr['created_at']}")
#         print(f"Updated At: {pr['updated_at']}")
#         print(f"Closed At: {pr['closed_at']}")
#         print(f"Merged At: {pr['merged_at']}")
#         print(f"PR Body: {pr['body']}")
#         print(f"URL: {pr['html_url']}")
        
#         # List of files changed in the PR
#         files_url = pr['url'] + '/files'
#         files_response = requests.get(files_url, headers=headers)
#         if files_response.status_code == 200:
#             files = files_response.json()
#             print("\nFiles Changed in the PR:")
#             for file in files:
#                 print(f" - {file['filename']} (Changes: {file['changes']})")
#         else:
#             print("Failed to fetch files changed in the PR.")
#     else:
#         print(f"Failed to fetch PR details. Status Code: {response.status_code}")

# # Example usage:
# get_github_pr_detail("wintersalmon", "ai-coworker", 1)

# import requests

# def get_pr_files_detail(owner, repo, pr_number):
#     # Pull Request의 변경된 파일 목록을 가져오는 API URL
#     url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
#     headers = {"Accept": "application/vnd.github.v3+json"}
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         files = response.json()
        
#         print(f"Pull Request #{pr_number} - Changed Files:")
#         print("-" * 60)
        
#         for file in files:
#             print(f"File: {file['filename']}")
#             print(f"  Status: {file['status']}")
#             print(f"  Additions: {file['additions']}, Deletions: {file['deletions']}, Changes: {file['changes']}")
#             print(f"  Blob URL: {file['blob_url']}")
#             print(f"  Patch:\n{file['patch']}")
#             print("-" * 60)
#     else:
#         print(f"Failed to fetch files. Status Code: {response.status_code}")

# # Example usage:
# get_pr_files_detail("wintersalmon", "ai-coworker", 1)