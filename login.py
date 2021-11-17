import getpass
import core

def login():
  user = {}
  user['name'] = input('Masukkan nama : ')
  user['password'] = getpass.getpass(prompt='Masukkan password : ')

  result = core.get_user_by_name(user['name'])
  is_exist = result != None and result['password'] == user['password']
  if is_exist:
    core.login_user = result
    print("\nAnda berhasil login!")
    input()
  return is_exist

def logout():
  core.login_user = {}
  print("Terima kasih! Sampai Jumpa!")
  input()
  return True

