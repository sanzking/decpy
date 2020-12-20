#--------------------------------------#
import os, time, uncompyle6
os.system('clear')
#--------------------------------------#
logo = """
====================
DECRYPT PYTHON FILE
====================
"""
#--------------------------------------#
print(logo)
ini = input("pilih file : ")
yakin = input("Decrypt file? [y/n] : ")
if yakin == 'y':
	print()
	os.system(f'uncompyle6 {ini}')
	time.sleep(1)
	print("\n!!!Berhasil didecrypt!!!")
elif yakin == 'n':
	print(">> MUNGKIN LAIN KALI YA :) <<")
	exit()
else:
	exit(">Input salah<")
#--------------------------------------#