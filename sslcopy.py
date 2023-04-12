# 글로벌스포츠산업학부 202002253 유혜연
# 정상 동작


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
		
    	# remove 메소드

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
	
	################### 여기에서 부터 수정 / 새로 만든 메소드
	# 수정한 delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before
			self.before.next = self.current.next
			self.current = self.before
		else:
			self.current = self.current.next
			self.before.next = self.current
		self.num_of_data -= 1
		return pop_data
	
	# insert_at 메소드
	def insert_at(self, position, new_data):
    # 1. position이 0 이하의 값일 경우,오류 메시지를 출력하고 함수를 종료한다. 
		if position <= 0:
			print("Error: position은 0 이하가 될 수 없음!")
			return
        
        # 2. position이 현재 리스트의 크기(num_of_data)보다 크면 append() 함수를 호출하여 리스트의 맨 마지막에 new_data를 삽입한다. 
		if position > self.num_of_data:
			self.append(new_data)
			return
        
        # 3. new_data를 저장할 새로운 노드를 생성한다.
		new_node = Node(new_data)

        # 4. 위치를 맨 앞으로 세팅하고, position의 횟수만큼 리스트를 순회하며 새로운 노드를 삽입할 위치를 찾는다.
		self.current = self.head
		self.before = None
		for _ in range(position):
			self.before = self.current
			self.current = self.current.next
            
        # 5. before 노드와 새로운 노드를 연결하고, 새로운 노드와 current 노드를 연결해 position의 위치에 new_node를 삽입한다. 
		self.before.next = new_node
		new_node.next = self.current
        
        # 6. new_data가 삽입되었으므로, 리스트의 길이(num_of_data)를 1 증가시킨다.
		self.num_of_data += 1

	# remove 메소드
	def remove(self, key):
        # 1. 현재 위치를 맨 앞으로 세팅한 후, found, position 변수 선언
		current = self.head 
		prev = None
		found = False
		position = 0
		found_num=0
		
		# 2. 리스트를 순회하면서 key값과 같은 값을 가진 노드를 찾아 해당 position+1번째 원소(key)를 삭제한다고 출력
		while current is not None:
			if current.data == key:
				found = True
				found_num += 1
				print(f'{position + found_num -1}번째 원소({key})를 삭제합니다.')
                
                # 3. key값과 같은 값을 가진 노드를 삭제                
				if current == self.head:
					self.head = current.next
					current = self.head
				else:
					prev.next = current.next
					current = current.next
					
			else:
				# 4. 다음 노드로 이동
				prev = current
				current = current.next
				position += 1
                
       # 5. key값을 가지는 노드가 없을 경우 출력
		if not found:
			print(f'해당하는 원소가 없습니다.')

	# traverse_all 메소드
	def traverse_all(self): 
		current = self.head.next
		result = 'head'
		while current is not None:
			result += f' -> ({current.data})'
			current = current.next
		result += ' -> null'
		print(result)
                
