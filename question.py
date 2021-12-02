import core


def get_question():
  core.clear()
  core.show_questions()
  question_id = input("Masukkan ID pertanyaan (huruf dalam kurung) : ")
  question = core.get_question(question_id)
  return question

def answer_question():
  is_answering = True
  while is_answering:
    question = get_question()
    if question != None:
      print(f"\nPertanyaan:\n{question['question']}\n")
      answer = input("Masukkan jawaban anda : ")
      core.store_answer(answer, question)
      is_answering = True if input("Apa anda ingin menjawab pertanyaan lain? (y/n) : ") == "y" else False
    else:
      core.printc("Red","Pertanyaan tidak ada!")
      core.tap_enter()

def show_question_answers():
  question = get_question()

  if question != None:
    core.clear()
    print(f"\nPertanyaan:\n{question['question']}\n")
    answers = core.get_question_answers(question['id'])
    if answers != None:
      print("Jawaban:\n")
      for answer in answers:
        print(f"> {answer['user_name']} : {answer['answer']}")
      core.tap_enter()
    else:
      print("Belum ada jawaban")
      core.tap_enter()
  else:
    core.printc("Red","Pertanyaan tidak ada!")
    core.tap_enter()


def create_question():
  question = input("\nMasukkan pertanyaanmu : ")
  new_question = core.store_question(question)
  core.printc("Green","Pertanyaan anda berhasil dibuat!")
  core.tap_enter()


def delete_question():
  question_id = input("Masukkan ID pertanyaan (huruf dalam kurung) : ")
  question = core.get_question(question_id, True)
  if question != None:
    print(f"Pertanyaan [{question['id']}] : {question['question']}\n")
    is_delete = input("Apa anda yakin ingin menghapus pertanyaan? (y/n) ") == "y"
    if is_delete:
      core.destroy_question(question['id'])
      print("Pertanyaan telah dihapus!")
      core.tap_enter()
  else:
    print("Pertanyaan tidak ditemukan!")
    core.tap_enter()


def edit_question():
  question_id = input("Masukkan ID pertanyaan (huruf dalam kurung) : ")
  question = core.get_question(question_id, True)
  if question != None:
    core.printc("Cyan", f"Pertanyaan Sebelumnya: {question['question']}")
    new_question = input("Ubah Pertanyaan : ")
    new_question = new_question or question['question']
    core.update_question(question['id'], new_question)
    core.printc("Green", "Pertanyaan telah diubah!")
    core.tap_enter()
  else:
    core.printc("Red", "Pertanyaan tidak ditemukan!")
    core.tap_enter()

