import string , random

ALPHA,NUMBR,SYMBL= string.ascii_letters,string.digits,string.punctuation
pass_len = int(input("Enter Password Length : "))
password = "".join(random.sample(ALPHA+NUMBR+SYMBL, pass_len))
print("Your password is : ", password)