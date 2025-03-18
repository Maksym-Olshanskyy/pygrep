from datetime import datetime, timedelta

doIf = True
doIf2 = True
doIf3 = True

start1 = datetime.now()
for i in range(100000):
    if doIf and doIf2 and doIf3:
        print("Hello")

end1 = datetime.now()


start = datetime.now()

for i in range(100000):
    print("Hello")

end = datetime.now()




print("No If time: ", (end - start))
print("If time: ", (end1 - start1))
