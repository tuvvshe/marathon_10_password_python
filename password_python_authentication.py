import getpass
database = {"Tuvshintur.lkhadorj": "0987654321poiuytrewq", "lkhadorj.Tuvshintur": "qwertyuiop1234567890"}
username = input("ENTER Ur USERNAME : ")
password = getpass.getpass("ENTER Ur PASSWORD : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("ENTER Ur PASSWORD AGAIN!!! : ")
        break
print("VERIFIED")