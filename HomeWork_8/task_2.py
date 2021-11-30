"""
2.  Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""
from collections import Counter
keys = {}


class MyNode:
    def __init__(self, left, right, value=0):
        self.value = left[1] + right[1]
        self.left = left[0]
        self.right = right[0]

    def __repr__(self):
        return f'{self.value}: {self.left} - {self.right}'


def decode(tree, key=None):
    if type(tree) is MyNode:
        decode(tree.left, key + '0')
        decode(tree.right, key + '1')
    else:
        keys[tree] = key


my_str = "beep boop beer!"

counter = Counter()
for ch in my_str:
    counter[ch] += 1

while len(counter) > 1:
    left_item = counter.most_common()[:-2:-1][0]
    # print(left_item)
    del counter[left_item[0]]
    right_item = counter.most_common()[:-2:-1][0]
    del counter[right_item[0]]

    new_node = MyNode(left_item, right_item)
    counter[new_node] = new_node.value

# print(counter)
decode(list(counter)[0], '')

sorted(keys.items(), key=lambda kv: kv[1])
for k, v in keys.items():
    print(f'{k} : {v}')

for s in my_str:
    print(keys[s], end=' ')
# 0011 1101 1010 0010 1101 0110 1000 1111 1001 1000 - мой результат
# 0011 1110 1011 0001 0010 1010 1100 1111 1000 1001 - из примера
