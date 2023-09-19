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

def remove_compartment(head,n):
  #To DO
  i = head 
  total_node = 0
  while i != None:
    total_node += 1
    i = i.next

  idx = total_node - n-1
  if n > total_node:
    return head
  
  else:
    idx = total_node-n-1
    i = head
    count = 0
    while i.next != None:
      if idx == -1:
        return head.next
        
      elif count == idx:
        i.next = i.next.next
        return head
      i = i.next
      count += 1


head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,2)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->72
print()

head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,7)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
print()

head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,6)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->34-->41-->56-->72
print()
