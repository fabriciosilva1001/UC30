def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"

    if usuario == "admin" and senha == "1234":
        return "Acesso total"

    if usuario == "admin":
        return "Senha incorreta"

    return "Usuário inválido"