#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    answer = ()
    ht = HashTable(16)
    print("length", len(weights))
    for x in range(len(weights)):
        print("index", x)
        print("value", weights[x])
        hash_table_insert(ht, weights[x], x)
    for i in range(len(weights)):
        for j in range(i, len(weights)):
            if hash_table_retrieve(ht, limit-weights[j]) is not None:
                print("in table", hash_table_retrieve(ht, limit-weights[j]))
                if weights[i] < weights[j]:
                    answer = (j, i)
                else: 
                    answer = (i, j)
            print(answer)
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
