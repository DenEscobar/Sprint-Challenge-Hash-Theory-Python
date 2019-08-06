#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    answer = None
    ht = HashTable(16)
    for x in range(len(weights)):
        hash_table_insert(ht, weights[x], x)
    for i in range(len(weights)):
        if hash_table_retrieve(ht, limit-weights[i]) is not None:
            value = hash_table_retrieve(ht, limit-weights[i])
            if i < value:
                answer = (value, i)
            else: 
                answer = (i, value)
            return answer 
    return answer




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
