#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for x in range(length):
        hash_table_insert(ht, weights[x], x)
    for i in weights:
        for j in weights:
            if hash_table_retrieve(ht, limit-weights[i]) is not None:
                if weights[i] < weights[j]:
                    answer = (j, i)
                else: 
                    answer = (i, j)
            return answer

    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
