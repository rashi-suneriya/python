dict1 = {'a':1, 'b': 2}
dict2 = {'b':3, 'c': 4}
merged = dict1 | dict2
print(merged)

# use multiple context managers in a single with statement more clearly using parenthesised comntext manager


with (
  open('file1.txt') as f1,
        open('file2.txt') as f2
  
):
  data1 = f1.read()
  data2 = f2.read()
  print(data1)
  print(data2)