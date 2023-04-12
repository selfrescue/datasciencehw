# 글로벌스포츠산업학부 202002253 유혜연
# 정상 동작
# 테스트 3차

from sslcopy import *

if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(0)
    l_list.append(100)
    l_list.append('hello')

    # [0, 100,'hello']
    print('first: ', l_list.first())
    print('delete: ', l_list.delete()) # 맨 앞 값도 삭제 되는 지 확인
    print('delete: ', l_list.delete()) 
    print('delete: ', l_list.delete()) # string 값 + 모두 삭제 되는 지 확인

    l_list.insert_at(3, 'hi') # string 값 삽입
    l_list.insert_at(1, 3.21) # string 값 삽입
    l_list.remove('hi') # string 값 삭제
    l_list.remove(3.21)
    l_list.traverse_all() # string 값도 나오는 지 확인

