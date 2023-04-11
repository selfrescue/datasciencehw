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

# 2) insert_at(self, position, new_data)
# 리스트의 주어진 위치(position)에 new_data를 삽입한다.
# 이 때, 맨 첫 원소의 위치는 1로 정하며, 0 이하의 position 값이 입력되면 error 문을 출력한다.
# 만일 position이 현재 리스트의 크기(원소 갯수)보다 크면 맨 마지막에 new_data를 삽입한다.

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
    
    def remove(self, key): 
        # 맨 앞부터 차례차례 보기 ( 맨 앞 값에서 시작) 
        self.before = self.head
        self.current = self.head.next 
        
        # 만약 data 값이 key 일 경우 pop 한다
        if self.current.data == key: 
            pop_data = self.current.data

            if self.current is self.tail:
                self.tail = self.before
                self.before.next = self.current.next
                self.current = self.before 
                self.num_of_data -= 1
                
                # 삭제된 값의 인덱스를 리스트로 저장해야 함 
                
        # 어떻게 순서대로 넘어갈지 ? 
        while self.current.next != None: 
            self.before = self.current
            self.current = self.current.next
        
# 3) remove(key)
# # 리스트의 원소 가운데 key값과 일치하는 원소를 모두 삭제하고, 리스트를 수정한다.
# # 이 때, 처리 결과를 다음 예와 같이 출력한다.
# #* 3번째 원소(key)를 삭제합니다.
# # * 해당하는 원소가 없습니다.
        
        
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
    
    # 1) traverse_all 함수 
    # # head부터 tail까지 각 노드를 순차적으로 탐색하며 각 노드의 data를 print한다.
    # # 출력 형식:  head -> (100) -> (72) -> (325) -> null
    def traverse_all(self): 
        data=l_list.first()
        if data:
            print(head, end=' -> ')
        while True: 
            data = l_list.next()
            if data:
                print(data, end=' -> ')
            else: 
                break
                
