# override the __len__() method on vector of problem 5 to display the dimension of the vector.

class vectore:
  def __init__(self, l):
    self.l = l
    
    
    
    def __len__(self):
      return len(self.l)
    
v1 = vectore([1, 2, 3])
print(len(v1))    