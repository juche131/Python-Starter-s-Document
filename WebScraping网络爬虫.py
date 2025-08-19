import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
# print(response.text) # get html code
soup = BeautifulSoup(response.text, "html.parser")
print(type(soup))  # <class 'bs4.BeautifulSoup'>

# F12元素审查找出问题对应描述为<div id="question-summary-79740020" class="s-post-summary    js-post-summary" data-post-id="79740020" data-post-type-id="1">…</div>flex
questions = soup.select(".s-post-summary.js-post-summary")  # 审查元素（空格用.代替）

# print(questions[0].get("id", 0)) # question-summary-79740089
print(questions[0].select_one(".s-link"))
# [<a class="s-link" href="/questions/79740101/test-a-child-component-that-calls-an-api-within-the-parent-component-react-tes">Test a child component that calls an API within the parent component - react testing library</a>]
print(questions[0].select_one(".s-link").get_text())
# Test a child component that calls an API within the parent component - react testing library


# <span class="s-post-summary--stats-item-number">0</span>
# <span class="s-post-summary--stats-item-number">5</span>
for question in questions:
    print(question.select_one(".s-link").get_text())
    # get rows of text of problem titles got in stackoverflow
    statsitem = question.select(".s-post-summary--stats-item-number")
    print([item.getText() for item in statsitem])
