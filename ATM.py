# ATM Management system using python mini project
#topics covered:1.conditional stmts 2.built in function 3.operators
username='navya'
password='python123'
c_name=input("enter your name:")
c_pass=str(input("enter your password:"))
if c_name==username and c_pass==password:
     print('''
     1.deposite
     2.withdraw
     3.ministatment
     4.exit
     ''')
     amount=int(input("enter a amount:"))
     option=int(input("select your option:"))
     if option==1:
          dep=int(input("enter the amount:"))
          amount+=dep
          print("total amount:",amount)
     elif option==2:
          wit=int(input("enter the amount:"))
          amount-=wit
          print("total amount:",amount)
     elif option==3:
          print("=====ATM=====")
          print("username:",username)
          print("final amount:",amount)
          print("thanks for visiting")
          print("============")
     elif option==4:
          exit()
else:
     print(" please enter correct login")
     
          
