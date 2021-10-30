import menus
import core

import question
import answer
from login import login
from register import register


def main():
  core.init()
  is_running = True
  is_logout = False
  while is_logout == False:
    menus.show_main_menu()
    main_choice = input("Apa yang ingin anda lakukan? ")

    if main_choice != "9":
      # SEE ALL QUESTIONS
      if main_choice == "1":
        core.show_questions()
        show_question_choice = input("Apa anda ingin menjawab pertanyaan? (y/n) ")
        if show_question_choice == "y":
          question.answer_question()

      # SEE QUESTION'S ANSWERS
      elif main_choice == "2":
        question.show_question_answers()

      # ANSWER A QUESTION
      elif main_choice == "3":
        question.answer_question()

      # SHOW LOGIN USER QUESTIONS
      elif main_choice == "4":
        core.show_questions(False)
        show_question_choice = input("Apa anda ingin melihat jawaban pertanyaan? (y/n) ")
        if show_question_choice == "y":
          question.show_question_answers()

      # MAKE QUESTIONS
      elif main_choice == "5":
        question.create_question()
      
      # EDIT QUESTIONS
      elif main_choice == "6":
        question.edit_question()

      # DELETE QUESTIONS
      elif main_choice == "7":
        question.delete_question()

      elif main_choice == "8":
        answer.show_answers()

    else:
       core.do_exit()

  # while is_running:
  #   menus.show_start_menu()
  #   start_choice = input("Apa yang ingin anda lakukan? ")

  #   if start_choice != "4":
  #     if start_choice == "1":
  #       is_login = login()
  #       if is_login:
  #         is_logout = False
  #         while is_logout == False:
  #           menus.show_main_menu()
  #           main_choice = input("Apa yang ingin anda lakukan? ")

  #           # SEE ALL QUESTIONS
  #           if main_choice == "1":
  #             core.show_questions()
  #             show_question_choice = input("Apa anda ingin menjawab pertanyaan? (y/n)")
  #             if show_question_choice == "y":
  #               question.answer_question()

  #           # SEE QUESTION'S ANSWERS
  #           elif main_choice == "2":
  #             question.show_question_answers()
  #           # ANSWER A QUESTION
  #           elif main_choice == "3":
  #             question.answer_question()
  #       else:
  #         print("Akun anda belum terdaftar! Silahkan register")
  #     elif start_choice == "2":
  #       register()
  #     elif start_choice == "3":
  #       core.show_questions()
  #   else:
  #     core.do_exit()


if __name__ == "__main__": 
  main()