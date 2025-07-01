class Node:
	def __init__(self,data):
		self.data = data
		self.next = None	
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head is None

	def length(self):
		count = 0
		curr = self.head
		while curr:
			count+=1
			curr = curr.next
		return count

	def clear(self):
		self.head = None

	def to_list(self):
		result = []
		curr = self.head
		while curr :
			result.append(curr.data)
			curr = curr.next
		return result

	def display(self):
		curr = self.head
		while curr :
			print(f"{curr.data}<->",end="")
			curr = curr.next
		print("None")

	
	def display_backward(self):
		curr = self.head

		if not curr:
			print("none")
			return

		while curr.next:
			curr = curr.next

		while curr:
			print(f"{curr.data}<->",end="")
			curr = curr.prev
		print("None")


	def append(self,data):
		new_node = Node(data)

		if not self.head:
			self.head = new_node
			return

		curr = self.head

		while curr.next:
			curr = curr.next

		curr.next = new_node
		new_node.prev = curr


	def prepend(self,data):
		new_node = Node(data)

		new_node.next = self.head

		if self.head:
			self.head.prev = new_node

		self.head = new_node



	def insert_after(self,target_data,data):
		new_node = Node(data)

		curr = self.head

		while not curr and curr.data!=target_data:
			curr.next

		if not curr:
			print("target_data not found")
			return

		new_node.next = curr.next
		new_node.prev = curr

		if curr.next:
			curr.next.prev = new_node

		curr.next = new_node


	def insert_before(self,data,target_data):
		new_node = Node(data)

		curr = self.head

		while not curr and curr.data!=target_data:
			curr.next

		if not curr:
			print("target_data not found")
			return

		new_node.next = curr
		new_node.prev = curr.prev

		if curr.prev:
			curr.prev.next = new_node
		else:
			self.head = new_node

		curr.prev = new_node


	def delete(self,key):
		curr = self.head

		while curr and curr.data != key:
			curr = curr.next

		if not curr:
			print("Node not found")
			return

		if curr.prev:
			curr.prev.next = curr.next
		else:
			self.head=curr.next

		if curr.next:
			curr.next.prev = curr.prev

		curr = None

	def delete_head(self):
		if not self.head:
			return

		self.head = self.head.next

		if self.head:
			self.head.prev = None

	def delete_tail(self):
		if not self.head:
			return

		curr = self.head

		while curr.next :
			curr = curr.next

		if curr.prev:
			curr.prev.next = None
		else:
			self.head = None

	def reverse(self):
		curr = self.head
		prev = None

		while curr :
			prev = curr.prev
			curr.prev = curr.next
			curr.next = prev
			curr = curr.prev
		if prev:
			self.head = prev.prev

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    dll.insert_after(10, 15)
    dll.insert_before(5, 2)
    dll.display()

    print("Length:", dll.length())
    print("Is Empty?", dll.is_empty())

    print("List:", dll.to_list())
    print("Reverse:")
    dll.reverse()
    dll.display()

    dll.delete(15)
    dll.delete_head()
    dll.delete_tail()
    print("After deletions:")
    dll.display()

    dll.clear()
    print("After clearing:")
    dll.display()
    print("Is Empty?", dll.is_empty())