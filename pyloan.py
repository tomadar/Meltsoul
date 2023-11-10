#!/usr/bin/env python3                                                                      
import time
import sys                                    
from termcolor import colored, cprint
import os

def loan():
        os.system('clear')
        passw = 'Zoom'
        count = 0
        limit = 5
        while count < limit:
                print(colored('''
Login Pylon''', "green"))
                psw = input('Password: ')
                count += 1
                if len(psw) == 0:                                    
	           print(colored('Put Password!', 'magenta'))
                        time.sleep(0.5)
                        os.system('clear')
                        if count == 3:
                                print(colored('Caution!, put a password to avoid temporary account disable.', 'yellow'))
                        elif count == 5:
                                print(colored('pyloan: password failure.', 'red'))
                                print('wait till one minute.')
                                time.sleep(2)
                                os.system('clear')

                                for i in range(60, 0, -1):
                                        print(i)
                                        time.sleep(1)
                                        os.system('clear')
                                loan()
                                break
                elif psw == passw:
                        os.system('clear')
                        print(colored('''
∞∞∞∞∞∞∞$$$∞∞∞∞∞∞∞∞∞∞∞∞$$$∞∞∞∞∞∞∞∞∞∞∞$$$∞∞∞∞∞∞∞
              Welcome to Pyloan.
_____The adobe of python financial distro_____

''', "yellow"))
                        try:
                                name = input("Name: ")
                                if len(name) <= 1:
                                        print(colored('Invalid name', 'red'))
                                try:
                                        amount = int(input("Loan-Amount: $"))
                                except ValueError:
                                        print(colored('Invalid loan amount value.', 'red'))
                                try:
                                        cred = int(input("credit-score(300-850): "))
                                except ValueError:
                                        print(colored('Invalid credit score value.', 'red'))
                                repay = input("repay(months)2/4/8: ")
                                os.system('clear')
                                print('processing data...')
                                time.sleep(1.5)
                                os.system('clear')
                                if len(name) <= 1:
                                        print(colored('Name not properly set!', 'red'))
                                        time.sleep(1)
                                        loan()
                                else:
                                        if cred >= 600:
                                             has_good_credit = True
                                             if has_good_credit and repay == "2":
                                             print(colored(f'''

...........................................
Congrats {name},

You are eligible for ${amount} loan, you are to pay ${int(amount*20/100+amount)}, 20% repay rate in 2 months.

''', "green"))
                                             time.sleep(1)
                                             agree = input('Agree?(yes/no): ')
                                             os.system('clear')
                                             if agree == 'yes':
                                             print(colored('''
______________PAYMENT SLIP STATION____________

''', "yellow"))
                                             acc = input('Account number: ')
                                             os.system('clear')
                                             if len(str(acc)) == 10:
                                             print('processing...')
                                             time.sleep(6)
                                             os.system('clear')
                                             credit = colored(f'''
Your account has been credited with ${amount} and has been converted to N{amount*430} into your naira bank account.

''', "cyan")
                                             print(credit)
                                             save_path = '/home/userland/pyloan'
                                             file_name = 'history'
                                             compname = os.path.join(save_path, file_name)
                                             with open(compname, 'a') as file:
                                             file.write(credit)
                                             break
                                             else:
                                             print(cprint('Invalid account number!', 'red', 'on_white', attrs=['bold'], file=sys.stderr))
                                             time.sleep(2)
                                             loan()
                                             elif agree == 'no':
                                             terminated = colored('''
Loan terminated! $

Sorry for the disagreement, you can always check up on us anytime.

''', "blue", "on_grey")
                                             address = colored('''
Navigate to path/pyloan/share/doc or
visit "pyloan" gui page at https://www.pyloan.org/developer/share/doc
''', "yellow")
                                             print(terminated)
                                             print(address)
                                             break
                                             else:
                                             print(colored('Non usable input!', 'red'))

                                             elif has_good_credit and repay == "4":
                                             print(colored(f'''

...........................................
Congrats {name},

You are eligible for ${amount} loan, you are to pay ${int(amount*40/100+amount)}, 40% repay rate in 4 months.

''', "green"))
                                             time.sleep(1)
                                             agree = input('Agree?(yes/no): ')
                                             os.system('clear')
                                             if agree == 'yes':
                                             print(colored('''
_____________Payment Slip Station____________

''', "yellow"))
                                             acc = input('Account number: ')
                                             os.system('clear')
                                             if len(str(acc)) == 10:
                                             print('Processing...')
                                             time.sleep(6)
                                             os.system('clear')
                                             credit2 = colored(f'''
Your account has been credited with ${amount} and has been converted to N{amount*430} into your naira bank account.

''', "cyan")
                                             print(credit2)
                                             save_path2 = '/home/userland/pyloan'
                                             file_name2 = 'history'
                                             compname2 = os.path.join(save_path2, file_name2)
                                             with open(compname2, 'a') as file:
                                             file.write(credit2)
                                             break
                                             else:
                                             print(cprint('Incorrect account number!', 'red', 'on_white', attrs=['bold'], file=sys.stderr))
                                             time.sleep(2)
                                             loan()
                                             elif agree == 'no':
                                             print(colored('''
Loan terminated! $

Sorry for the disagreement, you can always check up on us anytime.

''', "blue", "on_grey"))
                                             print(colored('''
Navigate to path/pyloan/share/doc or
visit "pyloan" gui page at https://www.pyloan.org/developer/share/doc
''', "yellow"))
                                             break
                                             else:
                                             print(colored('Non usable value!', 'red'))

                                             elif has_good_credit and repay == "8":
                                             print(colored(f'''

...........................................
Congrats {name},

You are eligible for ${amount} loan, you are to pay ${int(amount*80/100+amount)}, 80% repay rate in 8 months.

''', "green"))
                                             time.sleep(1)
                                             agree = input('Agree?(yes/no): ')
                                             os.system('clear')
                                             if agree == 'yes':
                                             print(colored('''
_____________Payment Slip Station____________

''', "yellow"))
                                             acc = input('Account number: ')
                                             os.system('clear')
                                             if len(str(acc)) == 10:
                                             print('Processing...')
                                             time.sleep(6)
                                             os.system('clear')
                                             credit3 = colored(f'''
Your account has been credited with ${amount} and has been converted to N{amount*430} into your naira bank account.
''', "cyan")
                                             print(credit3)
                                             with open('/home/userland/pyloan/history', 'a') as file:
                                             file.write(credit3)
                                             break
                                             else:
                                             print(cprint('Invalid account number!', 'red', 'on_white', attrs=['bold'], file=sys.stderr))
                                             time.sleep(2)
                                             loan()
                                             elif agree == 'no':
                                             print(colored('''
Loan terminated! $

Sorry for the disagreement, you can always check up on us anytime.

''', "blue", "on_grey"))
                                             print(colored('''
Navigate to path/pyloan/share/doc or
visit "pyloan" gui page at https://www.pyloan.org/developer/share/doc
''', "yellow"))
                                             break
                                             else:
                                             print(colored('Non usable value!', 'red'))

                                             elif repay != "2" or "4" or "8":
                                             print(colored('''
make sure you type the repay month correctly! 2/4/8

''', "red"))
                                             time.sleep(2)
                                             loan()
                                        else:
                                             if amount == ValueError:
                                             print('Invalid')
                                             else:
                                             low = colored("""
............................................
Sorry, you are not eligible for loan at this moment, your credit score is low.

""", 'blue','on_grey')
                                             print(low)
                                             with open('/home/userland/pyloan/history', 'a') as file:
                                             file.write(low)
                                             break
                        except NameError:
                                print(cprint("""

............................................
Can't process your data, credit score or loan amount not properly set.

""", 'red', 'on_white', attrs=['bold'], file=sys.stderr))
                                ask = input('Try again?(yes/no): ')
                                if ask == 'yes':
                                        loan()
                                elif ask == 'no':
                                        print('Pyloan exit.')
                                        break
                                else:
                                        print('Try Pyloan again!')
                                        break
                else:
                        print(colored('wrong password!', 'red', 'on_white'))
                        time.sleep(1)
                        os.system('clear')
                        if count == 3:
                                print(colored("Caution!, you've exceeded three trials, your account will be temporarily disabled after the fifth wrong trial.", "yellow"))

        else:
                print(colored('Pyloan temporarily disabled!', 'red'))
                print('wait for one minute.')
                time.sleep(2)
                os.system('clear')
                for i in range(60, 0, -1):
                        print(i)
                        time.sleep(1)
                        os.system('clear')
                loan()

loan()
