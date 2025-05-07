import hashlib

def mmd5(s):
    result=hashlib.md5(s.encode()).hexdigest()
    print(result)

def ssha(s):
    result=hashlib.sha256(s.encode()).hexdigest()
    print(result)

def ssha2(s):
    result=hashlib.sha384(s.encode()).hexdigest()
    print(result)


string1=input("Enter a string: ")

mmd5(string1)
ssha(string1)
ssha2(string1)