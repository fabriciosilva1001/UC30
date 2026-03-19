def rank_jogador(pontos, derrotas):
    final = pontos - derrotas * 10

    if final < 0:
        return "Banido"

    if final >= 600:
        return "Diamante"
    elif final >= 300:
        return "Ouro"
    elif final >= 100:
        return "Prata"
    else:
        return "Bronze"