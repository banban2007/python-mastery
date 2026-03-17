d = {"Id":1,"Name":"Thu Ta","Posiition":"Developer","Address":"Yangon",[1,2,3]:"Departemt Ids"}
for x,y in d.items():
    print(x,y)

    # TypeError: unhashable type: 'list'