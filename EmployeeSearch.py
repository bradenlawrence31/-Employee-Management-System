#EmployeeSearch.py
import pickle
def searchemployee():
    eno = int(input("Enter Employee Number to Search:"))
    # get all the records from file
    records = []
    with open("D:\\Python\\FILES\\empproj.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # To display emp details
    found = False
    for record in records:
        if (record[0] == eno):
            found = True
            break
    print("-------------------------------------------------------")
    if (found):
        print("\tEMPLOYEE WORKING IN ORGANIZATION--VALID EMPLOYEE ")
    else:
        print("\tEMPLOYEE IS NOT WORKING IN ORGANIZATION--INVALID EMPLOYEE".format(eno))
    print("-------------------------------------------------------")