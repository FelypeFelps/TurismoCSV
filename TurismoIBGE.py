# MÓDULO 2 - ARMAZENAMENTO DOS DADOS
# Base: Tabela 8694 do IBGE - Atividades turísticas
# Este código não utiliza bibliotecas.

CAMINHO_ARQUIVO = "CSVTurismoIBGE.csv"


def carregar_dados(caminho):
    # Lista principal que armazenará todos os registros do CSV.
    dados = []

    # Abre o arquivo no modo de leitura.
    with open(caminho, "r", encoding="utf-8-sig") as arquivo:

        # Lê a primeira linha, que contém os nomes das colunas.
        cabecalho = arquivo.readline().strip().split(";")

        # Percorre as demais linhas do arquivo.
        for numero_linha, linha in enumerate(arquivo, start=2):
            linha = linha.strip()

            # Ignora linhas vazias.
            if linha == "":
                continue

            # Divide a linha em cinco campos usando ponto e vírgula.
            campos = linha.split(";")

            # Evita armazenar linhas com formato incorreto.
            if len(campos) != 5:
                print(f"Linha {numero_linha} ignorada: formato inválido.")
                continue

            # Separa os campos em variáveis.
            territorio = campos[0]
            mes = campos[1]
            variavel = campos[2]
            valor = float(campos[3])
            unidade = campos[4]

            # Transforma a linha atual em um dicionário.
            registro = {
                "territorio": territorio,
                "mes": mes,
                "variavel": variavel,
                "valor": valor,
                "unidade": unidade
            }

            # Adiciona o dicionário à lista principal.
            dados.append(registro)

    # Devolve a lista pronta.
    return dados


# Executa a função.
dados_turismo = carregar_dados(CAMINHO_ARQUIVO)


# Testes para verificar se o armazenamento funcionou.
print("Colunas encontradas:")
print("territorio, mes, variavel, valor, unidade")

print("\nQuantidade de registros armazenados:", len(dados_turismo))

print("\nPrimeiros cinco registros:")
for registro in dados_turismo[:5]:
    print(registro)

print("\nExemplo de acesso a um campo:")
print("Território do primeiro registro:", dados_turismo[0]["territorio"])
print("Valor do primeiro registro:", dados_turismo[0]["valor"])