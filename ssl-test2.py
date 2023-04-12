# 글로벌스포츠산업학부 202002253 유혜연
# 정상 동작
# 테스트 2차

from sslcopy import *

if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(1)
    l_list.append(2)
    l_list.append(3)
    l_list.append(4)
    l_list.append(5)
    l_list.append(6)
    l_list.append(7)
    
    # [1, 2, 3, 4, 5, 6, 7]
    # delete문이 끝까지도 잘 되는 지 확인
    print('first: ', l_list.first())
    print('next: ', l_list.next())
    print('next: ', l_list.next())
    print('size: ', l_list.size())
    print('delete: ', l_list.delete())
    print('delete: ', l_list.delete())
    print('delete: ', l_list.delete())
    print('tail: ', l_list.tail.data)
    print('current: ', l_list.current.data)
    print('delete: ', l_list.delete())
    print('delete: ', l_list.delete())
    print('tail: ', l_list.tail.data)

    l_list.insert_at(1, 0) # 맨 앞에 값 삽입
    l_list.remove(3) # 없는 값 지우려고 시도
    l_list.traverse_all() # 전체 값 확인

