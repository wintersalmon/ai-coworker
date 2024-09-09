from typing import NamedTuple

class CodeReviewFeedbackDTO(NamedTuple):
    filename: str
    content: str
    model: str
    response_id: str
    prompt_version: int
    created_at: str
