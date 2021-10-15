"""
Task:- Print a list of all possible coordinates given by (i,j,k) on a 3d grid where the sum of i+j+k is not equal to n.
Input Format:- Four integers x,y,z and n,each on a separate line.
Output Format:- Print the list in lexicographic increasing order.
"""
"""
    1
    1
    1
    2
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
output = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k == n:
                continue
            else:
                output.append([i, j, k])

print(output)
