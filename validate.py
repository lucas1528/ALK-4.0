def limitar_tamanho(p):
    if len(p) > 3:
        return False
    return isNumeric(p)

def isNumeric(p):
    if p.isdigit() or p == '':
        return True
    return False