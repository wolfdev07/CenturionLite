import secrets

def create_costumer_membership():
    new_membership = 'C' + secrets.token_hex(3).upper()[:6]

    return new_membership