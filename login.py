import getpass
import core

def login():
  user = {}
  user['name'] = input('Masukkan nama : ')
  user['password'] = getpass.getpass(prompt='Masukkan password : ')

  if user['name'] != '' and user['password'] != '':
    result = core.get_user_by_name(user['name'])
    is_exist = result != None and result['password'] == user['password']
    if is_exist:
      core.login_user = result
      core.printc("Green","\nAnda berhasil login!")
      core.tap_enter()
    return is_exist
  return False

def logout():
  core.login_user = {}
  core.printc("Cyan","\nTerima kasih! Sampai Jumpa!")
  core.tap_enter()
  return True

