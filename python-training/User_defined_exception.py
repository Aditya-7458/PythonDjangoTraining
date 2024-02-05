## User defined exception 

class Vote(Exception):
    def __int__(self):
        super()

a=12

try:
    if a<18:
        raise Vote
except Vote:
    print("Age is less than 18")
finally:
    print("Finally executed")
