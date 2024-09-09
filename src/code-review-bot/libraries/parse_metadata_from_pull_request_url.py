import re
from dto.PullRequestMetaDTO import PullRequestMetaDTO

def parse_metadata_from_pull_request_url(pull_request_url: str) -> PullRequestMetaDTO:
    """
    Parses the owner, repo name, and pull request number from a GitHub pull request URL.

    Args:
        pull_request_url (str): The GitHub pull request URL.

    Returns:
        Tuple[str, str, str]: A tuple containing the owner, repo name, and pull request number.
    """
        # Extract the repo owner, repo name, and pull request number from the URL
    pattern = r"https://github.com/([^/]+)/([^/]+)/pull/(\d+)"
    match = re.match(pattern, pull_request_url)
    if not match:
        raise ValueError("Invalid GitHub pull request URL")

    owner, repo, pull_number = match.groups()

    return PullRequestMetaDTO(owner=owner, repo=repo, pull_number=pull_number)
