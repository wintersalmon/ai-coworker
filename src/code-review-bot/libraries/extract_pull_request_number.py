import re

def extract_pull_request_number(url):
    # 정규표현식 패턴
    pattern = r"https://api\.github\.com/repos/[^/]+/[^/]+/pulls/(\d+)"
    
    # PR 번호 추출
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

if __name__ == "__main__":
    # 예시 URL
    url = "https://api.github.com/repos/wintersalmon/ai-coworker/pulls/1"
    
    # 함수 실행
    pr_number = extract_pull_request_number(url)
    print(pr_number)
