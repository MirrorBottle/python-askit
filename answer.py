import core


def delete_answer():
  answer_id = input("Masukkan ID jawaban (huruf dalam kurung) : ")
  answer = core.get_answer(answer_id)
  if answer != None:
    question = core.get_question(answer['question_id'])
    print(f"""
Pertanyaan [{question['id']}] : {question['question']}
Jawaban [{answer['id']}] : {answer['answer']}
      """)
    is_delete = input("Apa anda yakin ingin menghapus jawaban? (y/n) ") == "y"
    if is_delete:
      core.destroy_answer(answer['id'])
      print("Jawaban telah dihapus!")
  else:
    print("Jawaban tidak ditemukan!")

def show_answers():
  is_show = True
  while is_show:
    core.show_answers()
    is_deleting =  input("\nApa anda ingin menghapus jawaban? (y/n) ") == "y"
    if is_deleting:
      delete_answer()
    else:
      is_show = False

