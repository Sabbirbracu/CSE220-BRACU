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

def shuffle_on_index(head):

    even_head = head
    odd_head = head.next

    even_current = even_head
    odd_current = odd_head

    while odd_current and odd_current.next:
        even_current.next = odd_current.next
        even_current = even_current.next
        odd_current.next = even_current.next
        odd_current = odd_current.next

    even_current.next = odd_head

    return even_head


head = createList(np.array(['S','E','N','P','A','I']))
print('Original Play List: ', end = ' ')
printLinkedList(head)
newhead =  shuffle_on_index(head)
print('New Play List: ', end = ' ')
printLinkedList(newhead) #This should print S-->N-->A-->E-->P-->I
print()

head = createList(np.array(['N','I','S','H','I','N','O','Y','A']))
print('Original Play List: ', end = ' ')
printLinkedList(head)
newhead =  shuffle_on_index(head)
print('New Play List: ', end = ' ')
printLinkedList(newhead) #This should print N-->S-->I-->O-->A-->I-->H-->N-->Y
print()
