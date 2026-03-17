d = {"Id":1,"Name":"Kyaw Kyaw","Position":"Developer","Address":"Yangon"}

d.update({"Address":"Ygn"})
print(d)
d["Id"]=int(input("Id:"))
d["Name"]=(input("Name:"))
d["Position"]=(input("Position:"))
d["Address"]=(input("Address:"))
print(d)