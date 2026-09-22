def caixa(*precos):
    total = sum(precos)
    mais_caro = max(precos)
    media = total / len(precos)

    return total, mais_caro, media


print(caixa(10, 25.5, 7, 40))
