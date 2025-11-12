#EmployeeDelete.py
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
        #Decide the record found or not
        if(found):
            records.remove(records[recindex]) #OR records.pop(recindex)
            #rewrite the remaining records to the file
            with open("D:\\Python\\FILES\\empproj.pick", "wb") as fp:
                for record in records:
                    pickle.dump(record, fp)
            print("\tEmployee Record Deleted--verify")
        else:
            print("\tEmployee Number {} Does not Exist".format(eno))