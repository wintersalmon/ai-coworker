from typing import NamedTuple

class PullRequestChangedFileDTO(NamedTuple):
    filename: str
    patch: str
