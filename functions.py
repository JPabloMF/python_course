# FUNCTIONS ___________________________________
def calculate_op1():
  print('calculate')

def calculate_op2(n):
  print(n*n)

def calculate_op3(n):
  return n*n

calculate_op1()
calculate_op2(2)
print(calculate_op3(5))

def send_data():
    name = 'jose'
    email = 'jose@jose.com'
    age = 20
    city = 'Medellin'
    return (name,email,age,city)


def get_data(data):
    print(data[0])
    print(data[1])
    print(data[2])

get_data(send_data())

# IMPORTS
import random
print(random.randint(1,10))

from math import sqrt
print(sqrt(10))