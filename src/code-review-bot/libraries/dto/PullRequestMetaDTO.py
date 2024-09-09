from typing import NamedTuple

class PullRequestMetaDTO(NamedTuple):
    owner: str
    repo: str
    pr_number: str
