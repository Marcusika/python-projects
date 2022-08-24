
#i made this myself
#⚀⚁⚂⚃⚄⚅
import random

face = random.randint(1, 6)
face = str(face)
 
 #("""-----
#|   |
#|   | 
#|   |
#-----""")

if face == "6":
    print("""-----
|0 0|
|0 0| 
|0 0|
-----""")
elif face == "5":
    print("""-----
|0 0|
| 0 | 
|0 0|
-----""")
elif face == "4":
    print("""-----
|0 0|
|   | 
|0 0|
-----""")
elif face == "3":
    print("""-----
|  0|
| 0 | 
|0  |
-----""")
elif face == "2":
    print("""-----
|  0|
|   | 
|0  |
-----""")
elif face == "1":
    print("""-----
|   |
| 0 | 
|   |
-----""")
