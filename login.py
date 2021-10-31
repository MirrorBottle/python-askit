import getpass
import core

def login():
  user = {}
  user['name'] = input('Masukkan nama : ')
  user['password'] = getpass.getpass(prompt='Masukkan password : ')

  user = core.get_user_by_name(user['name'])
  is_exist = False if user == None else True
  if is_exist:
    core.login_user = user
    print("Anda berhasil login!\n")
  return is_exist

def logout():
  core.login_user = {}
  print("Terima kasih! Sampai Jumpa!")
  return True

