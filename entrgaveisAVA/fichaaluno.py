def ficha_aluno(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


ficha_aluno(nome="Carlos", idade=18, nota=8.5, turma="A")
