x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)

def nice(n):
    x = 9
    while x < n:
        print("Not nice.. " +str(x))
        x += 10
    print(str(x) + ".. Nice")
nice(69)

def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)