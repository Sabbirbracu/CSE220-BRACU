import fhm_unittest as unittest
import numpy as np

class Node:
  def __init__(self, elem, next = None):
    self.elem, self.next = elem, next

def create_linked_list(arr):
  head = Node(arr[0])
  tail = head
  for i in arr[1:]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node
  return head

def count(head):
  count = 0
  while head != None:
    count += 1
    head = head.next
  return count

def print_linked_list(head):
  while head != None:
    print(head.elem, end = '-> ')
    head = head.next
  print('None')
  print()


class Layered_Hashtable:
  def __init__(self, express_array_size):
    self.express_array = [None] * express_array_size

  def print_express_lane(self):
    for i in self.express_array:
      print(i.elem, end = ' '*10)
    print()

  def print_layered_hashtable(self):
    print('Express Lane is:')
    self.print_express_lane()

    for i in range (len(self.express_array)-1):
      node = self.express_array[i]
      next_node = self.express_array[i+1]
      print(f'Normal Lane Nodes between Express Lane Node {node.elem} and Express Lane Node {next_node.elem} are: ')
      while node != next_node:
        print(node.elem, end = '->')
        node = node.next
      print()

    print(f'Normal Lane Nodes ending in the Express Lane Node: {node.elem}')

  #DO IT YOURSELF
  def create_layered_hashtable(self, linked_list_head):
    total_node = count(linked_list_head)
    bucket_size = (total_node//len(self.express_array))+1

    temp = linked_list_head
    idx = 0
    for i in range(total_node):
      if i % bucket_size == 0:
        self.express_array[idx] = temp
        idx += 1
      temp= temp.next


  def search_element(self,k):
    output = False
    for i in range(len(self.express_array)-1):
      if k < self.express_array[i].elem or k > self.express_array[len(self.express_array)-1].elem:
        return "NOT Found"
      elif self.express_array[i].elem == k or self.express_array[i+1].elem ==k :
        return "Found"
      elif k >= self.express_array[i].elem and k < self.express_array[i+1].elem:
        temp = self.express_array[i]
        while temp != self.express_array[i+1]:
          if temp.elem == k:
            output = True
          temp = temp.next
    if output is True:
      return "Found"
    else:
      return "Not found"
    

arr = [4,6,9,18,25,37,62,67,79,84]
head = create_linked_list(arr)
express_array_size = 4

layered_ht = Layered_Hashtable(express_array_size)
layered_ht.create_layered_hashtable(head)
layered_ht.print_layered_hashtable()

print('==========1===========')
result = layered_ht.search_element(67)
unittest.output_test(result, 'Found')
print(f'67 {result}') #67 Found

print('==========2===========')
result = layered_ht.search_element(84)
unittest.output_test(result, 'Found')
print(f'84 {result}') #84 Found

print('==========3===========')
result = layered_ht.search_element(1)
unittest.output_test(result, 'Not Found')
print(f'1 {result}') #1 Not Found

print('==========4===========')
result = layered_ht.search_element(92)
unittest.output_test(result, 'Not Found')
print(f'92 {result}') #92 Not Found

print('==========5===========')
result = layered_ht.search_element(41)
unittest.output_test(result, 'Not Found')
print(f'41 {result}') #41 Not Found