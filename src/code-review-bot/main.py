from dotenv import load_dotenv, dotenv_values

load_dotenv()

GITHUB_PROJECT_TOKEN_AI_COWORKER = dotenv_values()["GITHUB_PROJECT_TOKEN_AI_COWORKER"]

import json
from langchain_community.chat_models import ChatOllama
from libraries.fetch_pull_request_changed_files import fetch_pull_request_changed_files
from libraries.dto.PullRequestMetaDTO import PullRequestMetaDTO
from libraries.code_review.review_code_with_llm import review_code_with_llm
from libraries.dto.CodeReviewFeedbackDTO import CodeReviewFeedbackDTO
from libraries.create_github_urls import request_add_pull_request_comment
from libraries.post_github_pull_request_comment import post_github_pull_request_comment


def read_python_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


LLM_MODEL = "mistral-nemo"
# LLM_MODEL = "gemma2:2b"
# LLM_MODEL = "gemma2:9b"
# LLM_MODEL= "starcoder2:3b"
llm = ChatOllama(
    model=LLM_MODEL,
)

def create_pull_request_comment(feedback: CodeReviewFeedbackDTO) -> dict:
    filename = feedback.filename
    content = feedback.content
    model = feedback.model
    response_id = feedback.response_id
    prompt_version = feedback.prompt_version

    return {
        "body": f"> filename: '{filename}'\n> model: '{model}\n> response_id: {response_id}\n> prompt_version: {prompt_version}\n\n{content}\n",
    }


if __name__ == "__main__":
    # 1. select target pull request
    targetPR = PullRequestMetaDTO(
        owner="wintersalmon",
        repo="ai-coworker",
        pr_number=1
    )

    # 2. fetch pull request changed files
    changed_files = fetch_pull_request_changed_files(targetPR)

    # 3. review code with llm
    feedback_v1 = [review_code_with_llm(llm, changed_file, 1) for changed_file in changed_files]
    feedback_v2 = [review_code_with_llm(llm, changed_file, 2) for changed_file in changed_files]
    feedbacks = feedback_v1 + feedback_v2

    postPRCommentURL = request_add_pull_request_comment(targetPR)

    # 4. print review results
    for feedback in feedbacks:
        try:
            body = create_pull_request_comment(feedback)
            post_github_pull_request_comment(postPRCommentURL, body, GITHUB_PROJECT_TOKEN_AI_COWORKER)

            # TODO save feedback to database

        except Exception as e:
            print(e)
