from typing import Optional
from langchain_core.prompts import PromptTemplate
from langchain_core.language_models import BaseChatModel
from libraries.code_review.convert_response_to_dto import convert_response_to_dto
from libraries.dto.LLMResponseDTO import LLMResponseDTO

CODE_REVIEW_PROMPT_TEMPLATE = """
You are a highly skilled software engineer and code review expert. Your goal is to analyze the following code carefully, identify any potential issues, and offer constructive feedback to help improve its quality. Your feedback should cover multiple aspects, including but not limited to:
1. **Code Readability:** Comment on whether the code is clear, easy to follow, and well-organized. Suggest improvements for better readability, such as meaningful variable names, consistent indentation, and proper use of comments.
2. **Code Efficiency:** Analyze the code’s performance. Suggest optimizations where necessary, and point out areas where the code could be refactored to run more efficiently or reduce complexity (e.g., time complexity or memory usage).
3. **Best Practices & Standards:** Ensure the code follows best practices for the relevant programming language or framework. Check for adherence to coding standards, including naming conventions, proper error handling, and design patterns.
4. **Security & Vulnerabilities:** Identify any security concerns or vulnerabilities within the code, such as input validation, handling sensitive data, and potential injection flaws. Suggest security improvements to make the code more robust.
5. **Modularity & Scalability:** Assess how modular and scalable the code is. Provide feedback on whether functions and classes are broken down appropriately and how the code will adapt to future growth or changes.
6. **Edge Cases & Testing:** Identify edge cases that may not be handled by the code and provide suggestions to address them. Recommend areas where additional test cases should be written, and evaluate the existing testing coverage if any.
When reviewing, be specific in your feedback, offering code examples for improvement where possible. If the code is good, acknowledge its strengths. Use a friendly and professional tone to encourage continuous improvement.

---

Here is the code snippet for review:
```{language}
{code_snippet}
```
"""

def generate_code_review_prompt(language: str, code_snippet: str):
    """
    Generates a prompt for reviewing the given code snippet using the provided language model.
    """
    if not isinstance(language, str) or not language:
        raise ValueError("'language' must be a non-empty string")
    if not isinstance(code_snippet, str) or not code_snippet:
        raise ValueError("'code_snippet' must be a non-empty string")
    
    return PromptTemplate.from_template(CODE_REVIEW_PROMPT_TEMPLATE).invoke(
        {"language": language, "code_snippet": code_snippet}
    )

def get_code_review_feedback(
    llm: Optional[BaseChatModel],
    language: str,
    code_snippet: str,
) -> LLMResponseDTO:
    """
    Generates code review feedback for a given code snippet using the provided language model.

    Args:
        llm (Optional[BaseChatModel]): The language model used for generating feedback.
        language (str): The programming language of the code snippet.
        code_snippet (str): The code snippet to be reviewed.

    Returns:
        str: The generated code review feedback.

    Raises:
        ValueError: If `language` or `code_snippet` is invalid.
    """
    if not llm or not isinstance(llm, BaseChatModel):
        raise TypeError("Expected 'llm' to be an instance of BaseChatModel")

    if not isinstance(language, str) or not language:
        raise ValueError("'language' must be a non-empty string")
    if not isinstance(code_snippet, str) or not code_snippet:
        raise ValueError("'code_snippet' must be a non-empty string")

    prompt = generate_code_review_prompt(language, code_snippet)

    response = llm.invoke(prompt)

    return convert_response_to_dto(response)
