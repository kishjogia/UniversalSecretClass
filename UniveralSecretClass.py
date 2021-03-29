
from SecretClass import Secret
import json


def read_secret():
    with open('secret.json') as json_file:
        data = json.load(json_file)
        
        s.username = data['username']
        s.password = data['password']

    return

if __name__ == '__main__':
    s = Secret()
    read_secret()
    
    print ("Username = " + s.username)
    print ("Password = " + s.password)