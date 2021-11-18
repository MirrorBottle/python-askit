import core

def show_start_menu():
  print("""
SELAMAT DATANG DI ASKIT!
========================""")
  core.printc("Cyan","""
1) Login
2) Register
3) Lihat Pertanyaan
4) Keluar
  """)

def show_main_menu():
  print(f"""
SELAMAT DATANG DI ASKIT, {core.login_user['name']}!
========================""")
  core.printc("Cyan","""
1) Lihat Daftar Pertanyaan
2) Lihat Jawaban Pertanyaan
3) Jawab Pertanyaan
4) Daftar Pertanyaanmu
5) Buat Pertanyaan
6) Ubah Pertanyaanmu
7) Hapus Pertanyaanmu
8) Daftar Jawabanmu
9) Keluar
  """)
