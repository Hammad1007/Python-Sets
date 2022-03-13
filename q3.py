# Task 3
def Func(x, y, c):
  if c == '+':
    try:
      res = x + y;
      #print(res);
    except:
      print("Masla");
  elif c == '*':
    try:
      res = x * y;
      #print(res);
    except:
      print("Masla");
  elif c == '/':
    try: 
      res = x / y;
      #print(res)
    except: 
      print("Masla");

  return res;

# Main driver
a = 8;
b = 2;
print(Func(a, b, '/'));
print(Func(a, b, '+'));
print(Func(a, b, '*'));
print(Func(a, 'abs', '+'));
