#main source code branch version 0
import random
maxnumber = 0
minnumber = 0
maxletter = 0
minletter = "A"
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def randomnum():
  rannum = random.randint(minnumber, maxnumber)
  return rannum
def randomlett():
  for i in range(1,26):
    if alpha[i] == maxletter:
      index = alpha.index(maxletter)
  return

print()
  

maxnumber = int(input("what is the highest number on your axis?"))
minnumber = int(input("what is the lowest number on your axis?"))
maxletter = input("What is the last letter in your axis?")
minletter = input("What is the first letter in your axis?")


print("Last =",maxletter)
print("First =", minletter)
print("highest =",maxnumber)
print("minimum =",minnumber)
randomnum()
randomlett()

      

  

