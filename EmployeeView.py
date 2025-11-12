#EmployeeView.py<---File Name and Module Name
#EmployeeView.py<---File Name and Module Name
import pickle
def viewemployee():
    eno=int(input("Enter Employee Number to View Details:"))
    #get all the records from file
    records=[]
    # EmployeeDelete.py
    import pickle
    def deleteemployee():
        eno = int(input("Enter Emp Number to Delete:"))
        # get all the records from file
        records = []
        with open("D:\\Python\\FILES\\empproj.pick", "rb") as fp:
            while (True):
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
            # Tracing for finding the record
            found = False
            for index in range(0, len(records)):
                if (records[index][0] == eno):
                    recindex = index
                    found = True
                    break
            # Decide the record found or not
            if (found):
                records.remove(records[recindex])  # OR records.pop(recindex)
                # rewrite the remaining records to the file
                with open("D:\\Python\\FILES\\empproj.pick", "rb") as fp:
                    for record in records:
                        pickle.dump(record, fp)
                print("\tEmployee Record Deleted--verify")
            else:
                print("\tEmployee Number {} Does not Exist".format(eno))

        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #To display emp details
    found=False
    for record in records:
        if(record[0]==eno):
            rec=record
            found=True
            break
    print("--------------------------------------------")
    if(found):
       print("\tEmployee Number:{}".format(rec[0]))
       print("\tEmployee Name:{}".format(rec[1]))
       print("\tEmployee Salary:{}".format(rec[2]))
       print("\tEmployee Comp Name:{}".format(rec[3]))
    else:
        print("\tEmployee Number {} Does not Exist".format(eno))
    print("--------------------------------------------")


def viewallemployees():
    with open("D:\\Python\\FILES\\empproj.pick", "rb") as fp:
        print("---------------------------------------------")
        print("\tENO\t\tNAME\t\tSAL\t\tCOMP NAME")
        print("---------------------------------------------")
        while(True):
            try:
               record = pickle.load(fp)
               for val in record:
                   print("\t{}".format(val),end="  ")
               print()
            except EOFError:
                print("------------------------------------------")
                break