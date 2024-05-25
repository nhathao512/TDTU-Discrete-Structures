# -*- coding: utf-8 -*-
"""Lab05.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OasdiDbYJhNrzkeFr2i14agB6Dp4rJMW
"""

#Exercise 1
#a
print("Propositional form: 'P if Q and P implies Q.'")
#b
print("Propositional form: 'Q but not P.'")
#c
print("Propositional form: 'Q implies P.'")

#Exercise 2
#a
print("Statement in natural language form: 'If you understand how to solve all the exercises in the book, then you will get a good grade in the midterm exam, and if you get a good grade in the midterm exam, it means you understand how to solve all the exercises in the book.'")
#b
print("Statement in natural language form: 'You understand how to solve all the exercises in the book if and only if you did not get a good grade in the midterm exam.'")
#c
print("Statement in natural language form: 'You will get a good grade in the midterm exam if and only if you understand how to solve all the exercises in the book.'")

#Exercise 3
#a
print("Negation (Propositional form): ~(Q -> P)")
print("Negation (Natural language): 'You understand how to solve all the exercises in the book, but you may not get a good grade in the midterm exam.'")

print("Converse (Propositional form): P -> Q")
print("Converse (Natural language): 'If you get a good grade in the midterm exam, then you understand how to solve all the exercises in the book.'")

print("Contrapositive (Propositional form): ~Q -> ~P")
print("Contrapositive (Natural language): 'If you don't understand how to solve all the exercises in the book, then you won't get a good grade in the midterm exam.'")
#b
print()
print("Negation (Propositional form): ~(Q <-> ~P)")
print("Negation (Natural language): 'It is not the case that you understand how to solve all the exercises in the book if and only if you did not get a good grade in the midterm exam.'")

print("Converse (Propositional form): (~P <-> Q)")
print("Converse (Natural language): 'You did not get a good grade in the midterm exam if and only if you understand how to solve all the exercises in the book.'")

print("Contrapositive (Propositional form): (~Q <-> P)")
print("Contrapositive (Natural language): 'You did not understand how to solve all the exercises in the book if and only if you got a good grade in the midterm exam.'")
#c
print()
print("Negation (Propositional form): ~(P <-> Q)")
print("Negation (Natural language): 'It is not the case that you will get a good grade in the midterm exam if and only if you understand how to solve all the exercises in the book.'")

print("Converse (Propositional form): (Q <-> P)")
print("Converse (Natural language): 'You understand how to solve all the exercises in the book if and only if you will get a good grade in the midterm exam.'")

print("Contrapositive (Propositional form): (~Q <-> ~P)")
print("Contrapositive (Natural language): 'You will not get a good grade in the midterm exam if and only if you do not understand how to solve all the exercises in the book.'")

#Exercise 4
#a
P = "p"
S1 = "q -> t"
S2 = "p -> t"
S3 = "r -> t"
C = "t"
print("%s\n%s\n%s\n%s\n.%s"%(P, S1, S2, S3, C))
print()
#b
P = "p"
Q = "q"
S1 = "~q -> r"
S2 = "p -> v"
S3 = "r -> s"
S4 = "~s -> ~v"
C = "v"
print("%s;%s\n%s\n%s\n%s\n%s\n.%s"%(P, Q, S1, S2, S3, S4, C))

#Exercise 5
truth = [[True, True], [True, False], [False, True], [False, False]]
def implies(p, q):
  if (p == 1 and q == 0):
    return False
  else:
    return True
#a
print('a)')
print("p \t implies(p, t)\t t")
for item in truth:
  print(item[0], "\t", implies(item[0], item[1]), "\t \t", item[1])

print()
S1 = "p"
S2 = "p -> t"
C = "S1 + S2 -> C = 't'"
print("S1 = %s"%(S1))
print("S2 = %s"%(S2))
print("%s"%(C))

#b
print()
print('b)')
print("p \t implies(p, v)\t v")
for item in truth:
  print(item[0], "\t", implies(item[0], item[1]), "\t \t", item[1])

print()
S1 = "p"
S2 = "p -> v"
C = "S1 + S2 -> C = 'v'"
print("S1 = %s"%(S1))
print("S2 = %s"%(S2))
print("%s"%(C))

#Exercise 6
import math

A = [
    [2, 0, 5, 0, 3, 0],
    [3, 0, 0, 0, 0, 0],
    [0, 6, 2, 0, 5, 0],
    [3, 0, 9, 0, 25, 0],
    [0, 0, 2, 4, 5, 0],
    [0, 0, 0, 0, 0, 5]
]

def isOdd(a):
    a = a[0]
    return a % 2 != 0

def isEven(a):
    a = a[0]
    return a % 2 == 0

def isPrime(a):
    a = a[0]
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def isSquare(a):
    a = a[0]
    return int(math.sqrt(a)) ** 2 == a

def isGreater(a, b):
    a = a[0]
    b = b[0]
    return a > b

def isEqual(a, b):
    a = a[0]
    b = b[0]
    return a == b

def isAbove(a, b):
    a_row, a_col = get_row_col(a)
    b_row, b_col = get_row_col(b)
    return a_row < b_row

def isLeftOf(a, b):
    a_row, a_col = get_row_col(a)
    b_row, b_col = get_row_col(b)
    return a_col < b_col

def get_row_col(element):
    element = element[0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == element:
                return i, j

def check_statement(statement):
    for i in range(len(A)):
        for j in range(len(A[0])):
            element = A[i][j]
            if element != [0]:
                if not eval(statement):
                    return False
    return True

print("(a)", check_statement("any(not isOdd(a) and isPrime(a) for a in A if a != [0])"))
print("(b)", check_statement("all(not isOdd(a) or isSquare(a) for a in A if a != [0])"))
print("(c)", check_statement("all(not isOdd(a) or isGreater(a, [2]) for a in A if a != [0])"))
print("(d)", check_statement("any(isPrime(a) and not (isGreater(a, [3]) or isEqual(a, [3])) for a in A if a != [0])"))
print("(e)", check_statement("any(all(isLeftOf(a, b) for b in A if b != [0]) for a in A if a != [0])"))
print("(f)", check_statement("any(all(not isAbove(a, b) or not isGreater(a, b) for b in A if b != [0]) for a in A if a != [0])"))
print("(g)", check_statement("all(any(isPrime(a) and not isOdd(a) and isOdd(b) and isAbove(a, b) for b in A if b != [0]) for a in A if a != [0])"))
print("(h)", check_statement("all(all(not isEqual(a, b) or not isSquare(a) or not isEven(a) or not isEven(b) or isLeftOf(b, a) for b in A if b != [0]) for a in A if a != [0])"))