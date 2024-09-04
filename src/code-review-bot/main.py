from dotenv import load_dotenv

load_dotenv()

from langchain_community.chat_models import ChatOllama
LLM_MODEL = "mistral-nemo"
llm = ChatOllama(
    model=LLM_MODEL,
)

from get_code_review_feedback import get_code_review_feedback

if __name__ == "__main__":
    code_snippet = "def add(a, b):\n    return a + b"
    feedback = get_code_review_feedback(llm, 'python', code_snippet)
    print(feedback)
