from typing import NamedTuple

class LLMResponseMetadataDTO(NamedTuple):
    model: str
    created_at: str
    message: dict
    done_reason: str
    done: bool
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int

class LLMResponseDTO(NamedTuple):
    content: str
    response_metadata: LLMResponseMetadataDTO
    response_id: str
