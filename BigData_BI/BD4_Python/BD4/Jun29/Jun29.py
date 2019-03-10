'''
file = open("example.txt")
words =[]
for temps in file:
     for mot in temps.split(" "):
       words[].insert(mot)

print(words)'''

''' z=12

def suma_test (a, b):
     c = a+b
     return c

k=int(input("type"))
v=int(input("type"))

print(z)
print("result:",suma_test(k,v)) '''


def calcul_puissa (x,y=2):
     return x**y

def main():
          result = calcul_puissa (2,2)
          print(result)

print("module",__name__)

if __name__=='__main__':
     #print("module",__name__)
     main()