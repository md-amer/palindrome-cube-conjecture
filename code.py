import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def is_palindrome(s):
    return s == s[::-1]

def is_natural(n):
    return n == n//1

def cube_root(n):
    delta = 0.000001
    n = int(n)
    cube_root = n ** (1/3)
    if abs(cube_root - round(cube_root)) < delta:
        return round(cube_root)
    else:
        return cube_root

def is_perfect_cube(n):
    return is_natural(cube_root(n))

palindrome_cubes = []
cube_roots = []

index = -1

file = open("solutions.txt","a")

for i in range(666252,(10**6)):
    if is_palindrome(str(i)) and is_perfect_cube(i):
        palindrome_cubes.append(str(i))
        cube_roots.append(cube_root(i))
        index += 1
        file.write(str(cube_roots[index])+' '*(10-len(str(cube_roots[index])))+str(palindrome_cubes[index])+'\n')
        file.flush()
    clear_screen()
    print('Current number:')
    print(i)

file.close()
