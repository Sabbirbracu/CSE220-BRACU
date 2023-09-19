# You must run this cell to install dependency
import fhm_unittest as unittest
import numpy as np

#Run this cell
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()


def find_next_clue(head):
  
  flag = True
  i = head
  while i != None:

    j = i
    while j.next != None:
      if j.next.elem > i.elem:
        print(f"{j.next.elem} is Greter than {i.elem}")
        flag = True
        break
      else:
        flag = False  
      j = j.next

    if flag == False:
      print(f"No next element greater than {i.elem}")
      
    i = i.next


head = createList(np.array([7,85,54,16,11,30]))
print('Given Clue List: ', end = ' ')
printLinkedList(head)
find_next_clue(head)
print()



head = createList(np.array([20,13,33,12]))
print('Given Clue List: ', end = ' ')
printLinkedList(head)
find_next_clue(head)
print()