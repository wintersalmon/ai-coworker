from langchain_core.messages import BaseMessage
from libraries.dto.LLMResponseDTO import LLMResponseDTO, LLMResponseMetadataDTO

def convert_response_to_dto(response: BaseMessage) -> LLMResponseDTO:
    """
    Converts the given BaseMessage object to a string.

    Args:
        data (BaseMessage): The BaseMessage object to convert.

    Returns:
        str: The converted string representation of the BaseMessage object.
    """
    if not response:
        raise ValueError("Failed to generate code review feedback")
    
    if not response.content:
        raise ValueError("Invalid response content")

    if not response.response_metadata:
        raise ValueError("Invalid response metadata")

    llmResponseMetadataDTO: LLMResponseMetadataDTO = LLMResponseMetadataDTO(
        model=response.response_metadata['model'],
        created_at=response.response_metadata['created_at'],
        message=response.response_metadata['message'],
        done_reason=response.response_metadata['done_reason'],
        done=response.response_metadata['done'],
        total_duration=response.response_metadata['total_duration'],
        load_duration=response.response_metadata['load_duration'],
        prompt_eval_count=response.response_metadata['prompt_eval_count'],
        prompt_eval_duration=response.response_metadata['prompt_eval_duration'],
        eval_count=response.response_metadata['eval_count'],
        eval_duration=response.response_metadata['eval_duration'],
    )

    llmResponseDTO: LLMResponseDTO = LLMResponseDTO(
        content=response.content,
        response_metadata=llmResponseMetadataDTO,
        response_id=response.id,
    )

    return llmResponseDTO
