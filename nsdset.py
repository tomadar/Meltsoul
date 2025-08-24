# Number, Seperation and Differences by
# Tobi Martins; Created Martinga formular
# 21st August, 2025

import os
import time

def nsdset():
	try:
		os.system('clear')
		print("""
			Number, Seperation and Differences
			by Tobi Martins; Martinga Formular
""")
		n = int(input("Number: "))
		d = int(input("Difference: "))
		s = int(input("Seperation: "))
		try:
			f = n/s - ((d/2)+((d*s)/2)-d)
			print(f)
			for i in range(s-1):
				f = f+d
				print(f)
		except ZeroDivisionError:
			print("Sorry Zero is Indenominable!")
			time.sleep(2)
			os.system('clear')
			nsdset()
	except ValueError:
		print("Only numbers Supported!")
		time.sleep(2)
		os.system("clear")
		nsdset()

nsdset()