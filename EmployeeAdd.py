#EmployeeAdd.py<--File Name and Module Name
#EmployeeAdd.py<--File Name and Module Name
import pickle
def isunique(lst):
    # get all the records from file
    records = []
    with open("D:\\Python\\FILES\\empproj.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Trace the records for Unique
    res=True
    for record in records:
        if(record[0]==lst[0]):
            res=False
    return res

def addemployee():
    with open("D:\\Python\\FILES\\empproj.pick", "ab") as fp:
        try:
            print("-"*60)
            #accept Employee Values from Key Board
            empno=int(input("Enter Employee Number:"))
            print("-" * 60)
            #create an empty list for Placing values employee values
            lst=list()
            lst.append(empno)
            #save Iterable object -lst into the file
            if(isunique(lst)):
                empname = input("Enter Employee Name:")
                empsal = float(input("Enter Employee Salary:"))
                empcompname = input("Enter Employee Comp Name:")
                lst.append(empname)
                lst.append(empsal)
                lst.append(empcompname)
                pickle.dump(lst,fp)
                print("Employee Record Saved in File Sucessfully")
            else:
                print("\tAlready {} Employee Exist".format(empno))
            print("-" * 60)
        except ValueError:
            print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR EMPNO AND SAL")
