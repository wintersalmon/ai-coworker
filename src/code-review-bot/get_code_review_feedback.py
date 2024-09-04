from langchain_core.prompts import PromptTemplate
from langchain_core.language_models.chat_models import BaseChatModel

TEMPLATE_FOR_CODE_REVIEW_EXPERT = """You are a highly skilled software engineer and code review expert. Your goal is to analyze the following code carefully, identify any potential issues, and offer constructive feedback to help improve its quality. Your feedback should cover multiple aspects, including but not limited to:
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

PROMPT_TEMPLATE = PromptTemplate.from_template(TEMPLATE_FOR_CODE_REVIEW_EXPERT)

def get_code_review_feedback(llm: BaseChatModel, language: str, code_snippet: str) -> str:    
    """
    Generates code review feedback for a given code snippet.

    Args:
        llm (BaseChatModel): The language model used for generating feedback.
        language (str): The programming language of the code snippet.
        code_snippet (str): The code snippet to be reviewed.

    Returns:
        str: The generated code review feedback.

    Raises:
        None

    Example:
        llm = BaseChatModel()
        language = "Python"
        code_snippet = "def add(a, b):\n    return a + b"
        feedback = get_code_review_feedback(llm, language, code_snippet)
        print(feedback)
    """

    PROMPT = PROMPT_TEMPLATE.invoke({
        "language": language ,
        "code_snippet": code_snippet
    })

    return llm.invoke(PROMPT)
