import random

def generate_login():
    login= random.randint(1, 99)
    return login

def generate_age():
    age = random.randint(18, 70)
    return age

def generate_status():
    statuses = ['ACTIVE', 'BLOCKED', 'INACTIVE']
    return random.choice(statuses)

def generate_user():
    user = {'login': generate_login(), 'age': generate_age(), 'status': generate_status()}
    return user