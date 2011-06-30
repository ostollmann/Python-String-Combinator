class TLiteral:
 def __init__(self,char):
   self.data = [char]

class TList:
 def __init__(self,list):
   self.data = list

class TVowels:
 def __init__(self):
   self.data = "aeiou"

class TConsonants:
 def __init__(self):
   self.data = [chr(c) for c in range(ord('a'),ord('z')+1) if (chr(c) not in "aeiou")]

class TLetter:
 def __init__(self):
   self.data = [chr(c) for c in range(ord('a'),ord('z')+1)]

class TNumber:
 def __init__(self):
   self.data = [chr(c) for c in range(ord('0'),ord('9')+1)]

class TAny:
 def __init__(self):
   self.data = [chr(c) for c in range(ord('a'),ord('z')+1)] + [chr(c) for c in range(ord('0'),ord('9')+1)]

class TRange:
 def __init__(self,start,end):
  self.data = [chr(c) for c in range(ord(start),ord(end)+1)]
 
# ---------------------------------------------------------------------
# -- | recursive
def recGen(objs, acc=[""]):
  if not len(objs): return acc
  return recGen(objs[1:], [c + n for c in acc for n in objs[0].data])

# ---------------------------------------------------------------------
# -- | direct
def dirGen(objs, acc=[""]):
  for obj in objs:
    new = []
    for a in acc:
      for c in obj.data:
        new.append(a+c) 
    acc = new
  return acc

if __name__ == '__main__':
  objs = [TLiteral('x'), TList(['1','2']), TLiteral('a'), TRange('e', 'm'), TVowels()]
  print "Generation results:\n %s" % dirGen(objs)
