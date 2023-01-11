# Rtrams
#   R : reverse : smart
# Splkiyoanr
# S : skip : even position -> l i o n 

import hashlib

email = 'ihr@gmail.com'
pwd = 'etaNakiPassword'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd)
print(pwd_hash)

your_email = 'ihr@gmail.com'
# your_password = 'etaNakiPassword'
your_password = '6075ba7b0cc84b175e2c57fdce6ec243'

hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()

if email == your_email and pwd_hash == hashed_your_password : 
    print('right user') 
else :
    print('invalid login') 

hacker_email = 'ihr@gmail.com'
hacker_password = '6075ba7b0cc84b175e2c57fdce6ec243'

