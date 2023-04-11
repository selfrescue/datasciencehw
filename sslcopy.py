# Node 클래스 정의
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# LinkedList 클래스 정의
class LinkedList:

	# 초기화 메소드
	def __init__(self):
		dummy = Node("dummy")
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0

	# append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
	def append(self, data):
		new_node = Node(data) 
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1
        
	def insert_at(self, position, new_data):
		if position < 1:
			print("Error: position should be 1 or greater.")
			return

		if position > self.num_of_data:
			self.append(new_data)
			return

		new_node = Node(new_data)

		self.current = self.head
		self.before = None
		for _ in range(position):
			self.before = self.current
			self.current = self.current.next

		self.before.next = new_node
		new_node.next = self.current
		self.num_of_data += 1

	# insert_at 메소드
	def insert_at(self, position, new_data):
		if position <= 0:
			print("Error: position은 0 이하가 될 수 없음!")
			return

		if position > self.num_of_data:
			self.append(new_data)
			return

		new_node = Node(new_data)

		self.current = self.head
		self.before = None
		for _ in range(position):
			self.before = self.current
			self.current = self.current.next

		self.before.next = new_node
		new_node.next = self.current

		self.num_of_data += 1

	# delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before

			# 중요 : current가 next가 아닌 before로 변경된다.
			self.before.next = self.current.next
			self.current = self.before 

			self.num_of_data -= 1

			return pop_data
    
	# remove 메소드
	def remove(self, key):
		current = self.head
		prev = None
		found = False
		position = 0
		
		while current is not None:
			if current.data == key:
				found = True
				print(f'{position+1}번째 원소({key})를 삭제합니다.')
				if current == self.head:
					self.head = current.next
					current = self.head
				else:
					prev.next = current.next
					current = current.next
					
			else:
				prev = current
				current = current.next
				position += 1
		
		if not found:
			print(f'해당하는 원소가 없습니다.')

	# first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
	def first(self):
		# 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0: 
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	# next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data

	# size 메소드
	def size(self):
		return self.num_of_data 
	
	# traverse_all 메소드
	def traverse_all(self): # dummy가 출력됨 -> 보완 필요
		current = self.head
		result = 'head'
		while current is not None:
			result += f' -> ({current.data})'
			current = current.next
		result += ' -> null'
		print(result)
                
