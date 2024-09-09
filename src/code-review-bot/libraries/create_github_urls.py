from libraries.dto.PullRequestMetaDTO import PullRequestMetaDTO

def fetch_pull_request_changed_files(pullRequest: PullRequestMetaDTO) -> str:
    owner = pullRequest.owner
    repo = pullRequest.repo
    pr_number = pullRequest.pr_number

    return f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

def request_add_pull_request_comment(pullRequest: PullRequestMetaDTO) -> str:
    owner = pullRequest.owner
    repo = pullRequest.repo
    pr_number = pullRequest.pr_number

    return f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
