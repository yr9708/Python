# -*- coding:utf-8 -*-

def bubble(sort_data):
    for i in range(len(sort_data)-1):
        for j in range(len(sort_data) -i -1):
            if sort_data[j] > sort_data[j+1]:
                sort_data[j], sort_data[j+1] = sort_data[j+1], sort_data[j]
        print(sort_data)
    print(sort_data)
    
if __name__ == '__main__':
    sort_data = [5, 3, 2, 4, 1]
    bubble(sort_data)