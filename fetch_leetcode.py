import requests

def fetch_leetcode_problem(slug):
    url = f"https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        title
        content
        codeSnippets {
          lang
          code
        }
      }
    }
    """
    variables = {"titleSlug": slug}
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()['data']['question']
    
    return data

def convert_to_markdown(data):
    markdown = f"# {data['title']}\n\n"
    markdown += f"## Problem Description\n{data['content']}\n\n"
    
    for snippet in data['codeSnippets']:
        markdown += f"## Solution ({snippet['lang']})\n```{snippet['lang']})\n{snippet['code']}\n```\n\n"
    
    return markdown

def save_to_file(slug, markdown):
    with open(f"{slug}.md", "w") as file:
        file.write(markdown)

if __name__ == "__main__":
    problem_slug = input("Enter the LeetCode problem slug: ")
    data = fetch_leetcode_problem(problem_slug)
    markdown = convert_to_markdown(data)
    save_to_file(problem_slug, markdown)
