#1

def sum(n):
    if(n<1):
        return 0
    return n+sum(n-1)
print(sum(5))

#2
def heleper(num,rev):
 if(num<1):
    return rev
 else:
  rev=(rev*10)+(num%10)
  return heleper(num//10,rev)
def ispalindrom(num):
    revs=heleper(num,0)
    return revs==num
print(ispalindrom(22))

#3
def reverseString(str):
  if len(str)==1:
    return str
  else:
    return reverseString(str[1:]) + str[0]
input="abcde"
print(reverseString(input))


#4

def removeKthNode(self, header,k):
    if header==None:
      return None
    if k<=0:
      print('Wrong Input')
      return header
    if k==1:
      header=header.next
      return header
    else:
      header.next=self.removeKthNode(header.next,k-1)
      return header
def printList(self):
    current=self.head
    while current!=None:
      print(current.data,end="->")
      current=current.next
    print()