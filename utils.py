def check_not_empty(dict):
    return False if '' in dict.values() or None in dict.values() else True

def check_email(email):
    end = False
    for s in ['.edu.br', '.com', '.com.br']:
        if email.endswith(s):
            end = True
            break
    return '@' in email and end

