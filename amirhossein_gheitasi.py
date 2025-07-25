import re

def name_checker(name):
    if re.match(r"^[a-zA-z\s]{3,30}$",name):
        return True
    else:
        return False

def family_checker(family):
    if re.match(r"^[a-zA-z\s]{3,30}$",family):
        return True
    else:
        return False

def address_checker(address):
    if re.match(r"^[a-zA-Z0-9]{5,80}$",address):
        return True
    else:
        return False

def mobile_checker(mobile):
    if re.match(r"^+98/09[0-9]{9}$",mobile):
        return True
    else:
        return False

def email_checker(email):
    if re.match(r"^[a-zA-z0-9]{6,30}@gmail.com$",email):
        return True
    else:
        return False

def code_meli_checker(code_meli):
    if re.match(r"^[0-9]{10}$",code_meli):
        return True
    else:
        return False