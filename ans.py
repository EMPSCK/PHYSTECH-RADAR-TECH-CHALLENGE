import pandas as pd
import numpy as np

compatibility_matrix = np.array(pd.read_csv('input_with_weights.csv', header=None))
weights = compatibility_matrix[-1]
compatibility_matrix = np.delete(compatibility_matrix, -1, 0)

n = len(compatibility_matrix)
for i in range(n):
    for j in range(i + 1, n):
        compatibility_matrix[j][i] = compatibility_matrix[i][j]

a = {i: [j for j in range(n) if compatibility_matrix[i][j] == 1 ] for i in range(n)}

def key_sort(index):
    aneibors = a[index]
    count = 0
    for j in aneibors:
        if all(i in a[j] for i in path) and j not in path:
            count += 1
    return count


bestfive = [[0, []] for i in range(5)]


def add_to_best(el):
    i = 4
    if bestfive[i][0] >= el[0]:
        return
    while i != -1 and bestfive[i][0] < el[0]:
         bestfive[i], el =  el, bestfive[i]
         i = i - 1


for i in range(28):
    queue = [i]
    path = [i]
    weight = weights[i]
    while queue:
        v = queue.pop(-1)
        neibors = a[v]
        neibors.sort(key=key_sort)
        for neibor in neibors:
            if all(i in a[neibor] for i in path) and neibor not in path:
                weight += weights[neibor]
                path = path + [neibor]
                queue = queue + [neibor]
    add_to_best([weight, path])

print(bestfive)


