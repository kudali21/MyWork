data = {
    'vasu':'vasu123',
    'joe':'joe123',
    'sri':'sri123'
    }

def login(username,password):
    if data.get(username)==password:
        print("login successful")
    else:
        print("invalid credentials")

login('vasu','vasu123')
login('joe','joe123')
login('sri','sri123')
