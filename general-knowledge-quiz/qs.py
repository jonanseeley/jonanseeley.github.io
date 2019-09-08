from bs4 import BeautifulSoup as bs
from unidecode import unidecode
import json

class Question():
    def __init__(self, question_text, answer_text, recall_rate):
        self.question_text = question_text
        self.answer_text = answer_text
        self.recall_rate = recall_rate


with open("jawn.html") as f:
    soup = bs(f, features="html.parser")

table = soup.find_all(id="Tab1")[0]
tds = table.find_all("td")

questions = []
for i in range(2, len(tds), 17):
    text = tds[i].p.contents[0].split(" ")
    question_text = unidecode(" ".join(text[0:-1]))
    answer_text = (text[-1][1:-1])
    recall_rate = float(tds[i+1].p.contents[0])
    #questions.append(Question(question_text, answer_text, recall_rate))
    info_dict = {"question_id": len(questions), "question_text": question_text, "answer_text": answer_text, "recall_rate": recall_rate}
    questions.append(info_dict)

with open("questions.json", "w") as f:
    f.write(json.dumps(questions))

correct = 0
'''
for i, (q, a) in enumerate(zip(questions, answers)):
    print(q)
    x = input()
    if x == a:
        print("Correct!")
        correct += 1
    else:
        print(f'Your answer: {x}\tCorrect answer: {a}')
    print(f"You have gotten {correct} out of {i+1} correct!\n") 
    '''
