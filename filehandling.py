# f = open('demofile.txt', 'rwt')

# print(f.read())

with open('demofile.txt') as f:
    print(f.read()) 

f = open("demofile.txt")
print(f.readline())
f.close()

with open('demofile.txt', 'a') as f:
    f.write("why are you reading this file?\n")

with open('demofile.txt', 'w') as f:
    f.write("Okay so now i am wirting this file look motherfucker this is how it should be done")

with open('demofile.txt') as f:
    print(f.read())

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
