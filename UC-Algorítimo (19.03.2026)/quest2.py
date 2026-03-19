def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"

    if saque > 1000:
        saque = saque * 1.02

    restante = saldo - saque
    return restante