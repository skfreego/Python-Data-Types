"""
Task:-Consider a list (list = []). You can perform the following commands:
. insert i e: Insert integer e at position i
. print: Print the list.
. remove e: Delete the first occurrence of integer e
. append e: Insert integer e at the end of the list.
. sort: Sort the list.
. pop: Pop the last element from the list.
. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the
7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
Input Format:- The first line contains an integer,n , denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.
Output Format:- For each command of type print, print the list on a new line.

"""

"""
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print
"""

if __name__ == '__main__':
    N = int(input())

    command = []
    for i in range(N):
        command.append(input().split())

    result = []
    for i in range(N):
        if command[i][0] == 'insert':
            result.insert(int(command[i][1]), int(command[i][2]))
        elif command[i][0] == 'print':
            print(result)
        elif command[i][0] == 'remove':
            result.remove(int(command[i][1]))
        elif command[i][0] == 'append':
            result.append(int(command[i][1]))
        elif command[i][0] == 'pop':
            result.pop()
        elif command[i][0] == 'sort':
            result.sort()
        elif command[i][0] == 'reverse':
            result.reverse()
