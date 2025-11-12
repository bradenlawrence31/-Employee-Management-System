#EmployeeUpdate.py
import pickle
def updateemployee():
    eno=int(input("Enter Emp Number to Update Salary and Company Name:"))
    # get all the records from file
    records = []
    with open("D:\\Python\\FILES\\empproj.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Tracing for finding the record
    found=False
    for index in range(0,len(records)):
        if(records[index][0]==eno):
            recindex=index
            found=True
            break
    if(found):
        #update Salary and comp name
        newsal=float(input("Enter New Salary:"))
        compname=input("Enter New Comp Name:")
        records[recindex][2]=newsal
        records[recindex][3]=compname
        #Re-Write Updated Records to File
        with open("D:\\Python\\FILES\\empproj.pick", "wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Record Updated--verify")
    else:
        print("\tEmployee Number {} Does not Exist".format(eno))