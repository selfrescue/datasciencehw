from ssl_test import *

if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)


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

    data = l_list.first()
    if data:
        print(data, end= ' ')
    while True:
        data = l_list.next()
        if data:
            print(data, end= ' ')
        else:
            break 
