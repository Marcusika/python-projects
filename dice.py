#i made this myself
#⚀⚁⚂⚃⚄⚅
import random

face = random.randint(1, 6)
face = str(face)

if face == "6":
    print("⚅")
elif face == "5":
    print("⚄")
elif face == "4":
    print("⚃")
elif face == "3":
    print("⚂")
elif face == "2":
    print("⚁")
elif face == "1":
    print("⚀")

