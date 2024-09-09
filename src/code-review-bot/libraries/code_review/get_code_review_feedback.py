from typing import Optional
from langchain_core.prompts import PromptTemplate
from langchain_core.language_models import BaseChatModel
from libraries.code_review.convert_response_to_dto import convert_response_to_dto
from libraries.dto.LLMResponseDTO import LLMResponseDTO

DEFAULT_PROMPT_VERSION = 1

CODE_REVIEW_PROMPT_V1 = """
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

filename: `{filename}`
```
{code_snippet}
```
"""

CODE_REVIEW_PROMPT_V2 = """
You are a highly skilled software engineer and code review expert. Analyze the following code carefully and provide specific feedback on its quality.

**1. Code Readability:** Analyze the code’s clarity and suggest improvements:
    * Is the logic well-organized? Could it be broken into smaller components (functions/classes)?
    * Are variable names descriptive enough? Do comments explain complex logic?

    **Code Example:**
    ```python
    # Your code snippet here
    ```

**2. Efficiency & Best Practices:**
    * Is the code efficient in terms of time and memory? Can it be optimized or adhere more closely to best practices (e.g., single responsibility, DRY principles)?

    **Code Example:**
    ```python
    # Your code snippet here
    ```

**3. Security & Vulnerabilities:** Identify potential security concerns:
    * Input Validation: Are there protections against attacks like SQL injection or cross-site scripting?
    * Sensitive Data Handling: How is sensitive data, like passwords, being secured?

**4. Modularity & Scalability:** Evaluate the code’s modularity and scalability:
    * Are functions/classes well-defined, making the code easier to refactor or expand?

    **Code Example:**
    ```python
    # Your code snippet here
    ```

Please provide specific examples for each point to illustrate your feedback.

---

Here is the code snippet for review:
filename: `{filename}`
```
{code_snippet}
```
"""

def generate_code_review_prompt(filename: str, code_snippet: str, prompt_version: int):
    """
    Generates a prompt for reviewing the given code snippet.
    """
    if not isinstance(filename, str) or not filename:
        raise ValueError("'filename' must be a non-empty string")
    if not isinstance(code_snippet, str) or not code_snippet:
        raise ValueError("'code_snippet' must be a non-empty string")
    
    CODE_REVIEW_PROMPT = CODE_REVIEW_PROMPT_V2 if prompt_version == 2 else CODE_REVIEW_PROMPT_V1
    
    return PromptTemplate.from_template(CODE_REVIEW_PROMPT).invoke(
        {"filename": filename, "code_snippet": code_snippet}
    )

def get_code_review_feedback(
    llm: Optional[BaseChatModel],
    filename: str,
    code_snippet: str,
    prompt_version: int = DEFAULT_PROMPT_VERSION,
) -> LLMResponseDTO:
    """
    Generates code review feedback for a given code snippet using the provided language model.

    Args:
        llm (Optional[BaseChatModel]): The language model used for generating feedback.
        filename (str): The name of the file containing the code snippet.
        code_snippet (str): The code snippet to be reviewed.

    Returns:
        str: The generated code review feedback.

    Raises:
        ValueError: If `filename` or `code_snippet` is invalid.
    """
    if not llm or not isinstance(llm, BaseChatModel):
        raise TypeError("Expected 'llm' to be an instance of BaseChatModel")

    if not isinstance(filename, str) or not filename:
        raise ValueError("'filename' must be a non-empty string")
    if not isinstance(code_snippet, str) or not code_snippet:
        raise ValueError("'code_snippet' must be a non-empty string")

    prompt = generate_code_review_prompt(filename, code_snippet, prompt_version)

    response = llm.invoke(prompt)

    return convert_response_to_dto(response)
