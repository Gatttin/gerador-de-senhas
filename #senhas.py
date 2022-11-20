#criador de senhas

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
simbols = '!@#$%¨&*().'

string = lower + upper + numbers + simbols
length = 8
password = ''.join(random.sample(string, length))

print('sua senha é:' + password)

