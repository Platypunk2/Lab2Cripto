import csv

def GuardarInfoES(email, password):
    with open("genES.csv", "a") as f:
        f.write(email+","+password+"\n")

def GuardarInfoCL(email, password):
    with open("genCL.csv", "a") as f:
        f.write(email+","+password+"\n")

def VerCL():
    with open('genCL.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)

def VerES():
    with open('genES.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
