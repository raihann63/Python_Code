import datetime

now=datetime.datetime.now()

print("Current date :  ")
print(now.strftime("%Y-%m-%d"))
print("-"*40)
print("Current time:  ")
print(now.strftime("%H:%M:%S"))

