from typing import Optional
from langchain_core.language_models import BaseChatModel
from libraries.code_review.get_code_review_feedback import get_code_review_feedback
from libraries.dto.CodeReviewFeedbackDTO import CodeReviewFeedbackDTO
from libraries.dto.PullRequestChangedFileDTO import PullRequestChangedFileDTO


def review_code_with_llm(
        llm: Optional[BaseChatModel],
        changed_file: PullRequestChangedFileDTO,
        prompt_version: int = 1,
    ) -> CodeReviewFeedbackDTO:
    filename = changed_file.filename
    changed_file_content = changed_file.patch

    feedback = get_code_review_feedback(
        llm,
        filename,
        changed_file_content,
        prompt_version,
    )

    content = feedback.content
    review_llm_model = feedback.response_metadata.model
    created_at = feedback.response_metadata.created_at
    response_id = feedback.response_id

    return CodeReviewFeedbackDTO(
        filename=filename,
        content=content,
        model=review_llm_model,
        created_at=created_at,
        response_id=response_id,
        prompt_version=prompt_version,
    )
