class Node:
	def __init__(self,data):
		self.data = data
		self.next = None #when node is getting created

class SinglyLinkedList:
	def __init__(self):
		self.head = None #when node is getting created ,head points to the first node,in case of a newlycreated list its none

	#appending a node to the list
	def append(self,data):
		new_node=Node(data)

		if not self.head:
			self.head=new_node
			return

		curr = self.head #curr pointer intitially points to header

		while curr.next: #iterate until the last node which has next as none
			curr = curr.next

		curr.next = new_node #new node is appended at the end of the list

	#prepend at the beginning of the list
	def prepend(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	#Insert after a given node
	def insert_after(self,prev_data,data):
		curr = self.head

		while curr and curr.data != prev_data:
			curr=curr.next

		if not curr:
			print('Previous node not found')
			return

		new_node = Node(data)
		new_node.next = curr.next
		curr.next = new_node

	def delete(self,key):
		curr = self.head

		#if first element is the key to be deleted
		if curr	and curr.data==key:
			self.head = curr.next
			curr = None
			return

		prev = None

		while curr and curr.data!=key:
			prev = curr
			curr = curr.next

		if not curr:
			print("Node not found.")
			return

		prev.next=curr.next
		curr = None


	def search(self,key):
		curr = self.head

		while curr :
			if curr.data == key:
				return True
			curr = curr.next
		return False


	#print the list
	def display(self):
		curr = self.head

		while curr:
			print(f"{curr.data} -> ",end="")
			curr = curr.next

		print("None")



#demo

if __name__=="__main__":
	ll = SinglyLinkedList()
	ll.append(10)
	ll.append(20)
	ll.append(30)
	ll.append(40)
	ll.prepend(5)
	ll.insert_after(20,25)
	ll.delete(10)

	print("Elements:")
	ll.display()

	print("Search element 5",ll.search(5))
	print("Search element 95",ll.search(95))

