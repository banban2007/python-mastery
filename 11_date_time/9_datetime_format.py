from datetime import datetime
now = datetime.now()
print(now.strftime("%d"))
print(now.strftime("%a"))
print(now.strftime("%m"))
print(now.strftime("%B"))
print(now.strftime("%y"))
print(now.strftime("%Y"))

print(now.strftime("%a-%m-%Y"))
print(now.strftime("%d/%B/%Y"))
print(now.strftime("%d/%B/%Y %H:%M:%S"))
print(now.strftime("%d/%B/%Y %I:%M:%S"))