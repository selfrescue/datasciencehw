# 글로벌스포츠산업학부 202002253 유혜연
# 정상 동작
# 테스트 1차 

from sslcopy import *

if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)
    
    # [5, 2, 5, 1, 2, 7, 2, 11]
    print('first: ', l_list.first())
    print('next: ', l_list.next())
    print('size: ', l_list.size())
    print('delete: ', l_list.delete())
    print('size: ', l_list.size())
    print('current: ', l_list.current.data)
    print('tail: ', l_list.tail.data)
    print('first: ', l_list.first())
    print('next: ', l_list.next())
    print('next: ', l_list.next())
    print('next: ', l_list.next())
    l_list.insert_at(3, 5)
    l_list.remove(2)
    l_list.traverse_all()

    data = l_list.first()
    if data:
        print(data, end= ' ')
    while True:
        data = l_list.next()
        if data:
            print(data, end= ' ')
        else:
            break 
