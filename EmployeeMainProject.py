#EmployeeMainProject.py<---Main Project
from EmpMenu import menu
from EmployeeAdd import addemployee
from EmployeeDelete import deleteemployee
from EmployeeSearch import searchemployee
from EmployeeUpdate import updateemployee
from EmployeeView import viewallemployees,viewemployee
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewemployee()
            case 5:
                viewallemployees()
            case 6:
                searchemployee()
            case 7:
                print("Thx for Using this Project")
                break
            case _:
                print("\tUR SELECTION OF OPERATION IS WRONG-TRY AGAIN")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR UR CHOICE-TRY AGAIN")