import getpass
import core

def register():
  user = {}
  user['name'] = input('Masukkan nama : ')
  user['password'] = getpass.getpass(prompt='Masukkan password : ')
  is_exist = False if core.get_user_by_name(user['name']) == None else True

  if is_exist == False:
    core.store_user(user)
    print("Anda sudah terdaftar! Silahkan login!")
    input()
    core.clear()
  else:
    print("Nama pengguna sudah ada!")

