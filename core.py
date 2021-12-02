from nanoid import generate

from login import login

from os import system

import time
import getpass

def generate_id():
  return generate(size=5)


def init():
  global login_user
  global users
  global questions
  global answers

  users = [
    {"id": 1, "name": "hiroto", "password": "hiroto"},
    {"id": 2, "name": "shyna", "password": "shyna"},
    {"id": 3, "name": "mira", "password": "mira"},
    {"id": 4, "name": "violet", "password": "violet"},
    {"id": 5, "name": "alice", "password": "alice"},
  ]
  questions = [
    {"id": "xYbce", "question": "What's the best piece of advice you ever received?", "user_id": 1, "user_name": "hiroto"},
    {"id": generate_id(), "question": "What fictional place would you most like to go to?", "user_id": 1,"user_name": "hiroto"},
    {"id": generate_id(), "question": "What's your favorite candy?", "user_id": 2, "user_name": "shyna"},
    {"id": generate_id(), "question": "What languages do you speak?", "user_id": 3, "user_name": "mira"},
    {"id": generate_id(), "question": "If you were a vegetable, what vegetable would you be?", "user_id": 4, "user_name": "violet"},
  ]
  answers = [
    {"id": generate_id(), "question_id": "xYbce", "answer": "Never have one", "user_id": 2, "user_name": "shyna"},
    {"id": generate_id(), "question_id": "xYbce", "answer": "Life", "user_id": 3, "user_name": "mira"},
    {"id": generate_id(), "question_id": "xYbce", "answer": "Just Do It!", "user_id": 4, "user_name": "violet"},
    {"id": generate_id(), "question_id": "xYbce", "answer": "Just Do It!", "user_id": 1, "user_name": "hiroto"},
  ]

  login_user = {}

  _ = system('')


# UTILS

def find(val, items, key = 'id'):
  return next((item for item in items if item[key] == val), None)

def search(val, items, key = 'id'):
  result = []
  for item in items:
    if(item[key] == val):
      result.append(item)
  return result if len(result) > 0 else None

def destroy(val, items, key = 'id'):
  for index in range(len(items)):
    if items[index][key] == val:
        del items[index]
        break

def do_exit():
  login_user = {}
  print("Terima kasih! Sampai Jumpa!")
  input()
  exit()



# USER
def get_user_by_id(id):
  return find(id, users)

def get_user_by_name(name):
  return find(name, users, 'name')
  
def store_user(user):
  latest_user = max(users, key=lambda user:user['id'])
  user['id'] = latest_user['id'] + 1
  users.append(user)
  return user


# QUESTIONS
def show_questions(is_all = True):
  clear()
  curr_questions = questions if is_all else search(login_user['id'], questions, 'user_id')
  title = "DAFTAR PERTANYAAN ASKIT!" if is_all else "DAFTAR PERTANYAANMU!"
  print(f"""
{title}
========================
  """)
  if curr_questions != None:
    for question in curr_questions:
      print(f"[{question['id']}] {question['question']}")
  else:
    print("Anda tidak memiliki pertanyaan apapun...")
  print("\n========================")

def get_question(question_id, need_auth = False):
  question = find(question_id, questions)
  if need_auth and question != None:
    return question if question['user_id'] == login_user['id'] else None
  return question

def get_question_answers(question_id):
  question_answers = search(question_id, answers, 'question_id')
  return question_answers

def store_question(question):
  new_question = {
    "id": generate_id(),
    "question": question,
    "user_id": login_user['id'],
    "user_name": login_user['name']
  }
  questions.append(new_question)
  return new_question

def destroy_question(question_id):
  destroy(question_id, questions, 'id')
  destroy(question_id, answers, 'question_id')

def update_question(question_id, question):
  curr_question = find(question_id, questions)
  curr_question['question'] = question

# ANSWERS
def get_answer(answer_id):
  answer = find(answer_id, answers)
  return answer


def show_answers():
  curr_answers = search(login_user['id'], answers, 'user_id')
  print("\nDAFTAR JAWABANMU")
  print("========================")
  if curr_answers != None:
    for answer in curr_answers:
      question = get_question(answer['question_id'])
      print(f"""
Pertanyaan [{question['id']}] : {question['question']}
Jawaban [{answer['id']}] : {answer['answer']}
      """)
  else:
    print("Anda tidak memiliki jawaban apapun...")
  print("========================")


def store_answer(answer, question):
  new_answer = {
    "id": generate_id(),
    "question_id": question['id'],
    "answer": answer,
    "user_id": login_user['id'],
    "user_name": login_user['name']
  }
  answers.append(new_answer)
  return new_answer

def destroy_answer(answer_id):
  destroy(answer_id, answers, 'id')


# DECORATIONS
def clear():
    _ = system('cls')

def timedclear(sec):
  time.sleep(sec)
  clear()

def TapEnter():
  print("\033[1;33;40m")
  getpass.getpass(prompt='Tekan [Enter] untuk melanjutkan')
  print("\033[0;37;40m")
  clear()

def printc(ColourName,text):
  Colour = ("Black","Red","Green","Yellow","Blue","Purple","Cyan","White")
  SelectedColour = Colour.index(ColourName) + 30
  print(f"\033[0;{SelectedColour};40m{text}\033[0;37;40m")

