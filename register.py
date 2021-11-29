import getpass
import core

def register():
  user = {}
  user['name'] = input('Masukkan nama : ')
  user['password'] = getpass.getpass(prompt='Masukkan password : ')
  is_exist = False if core.get_user_by_name(user['name']) == None else True

  if is_exist == False:
    core.store_user(user)
    core.printc("Green","Anda sudah terdaftar! Silahkan login!")
    core.tap_enter()
  else:
    core.printc("Red","\nNama pengguna sudah ada!")
    core.tap_enter()

