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


# ==========================
# MÓDULO 3 - CONSULTAS
# ==========================

def nome_variavel(variavel):
    """Converte o nome técnico do CSV para um nome amigável."""

    if variavel == "numero_indice":
        return "Número índice da atividade turística"

    elif variavel == "variacao_acumulada_ano":
        return "Variação acumulada no ano"

    elif variavel == "variacao_mesmo_mes_ano_anterior":
        return "Variação em relação ao mesmo mês do ano anterior"

    return variavel


def nome_unidade(unidade):
    """Converte o nome técnico da unidade."""

    if unidade == "pontos_de_indice":
        return "pontos"

    elif unidade == "percentual":
        return "%"

    return unidade


def explicar_variavel(variavel):
    """Exibe uma breve descrição do indicador."""

    if variavel == "numero_indice":
        print(
            "\nRepresenta o nível da atividade turística no período analisado."
            "\nQuanto maior o valor, maior foi a atividade turística.\n"
        )

    elif variavel == "variacao_acumulada_ano":
        print(
            "\nMostra o crescimento ou a queda acumulada da atividade"
            "\nturística desde o início do ano em comparação"
            "\ncom o mesmo período do ano anterior.\n"
        )

    elif variavel == "variacao_mesmo_mes_ano_anterior":
        print(
            "\nMostra quanto a atividade turística cresceu ou diminuiu"
            "\nem comparação com o mesmo mês do ano anterior.\n"
        )


def mostrar_registro(registro):
    """Exibe um registro."""

    print(
        f"{registro['mes']:<18}"
        f"{registro['valor']:>8.2f} "
        f"{nome_unidade(registro['unidade'])}"
    )


def consultar_variavel(dados, variavel):
    """Consulta um indicador para um território."""

    territorio = input("\nDigite o território: ").strip().lower()

    encontrou = False

    print("\n==============================================================")
    print("Território:", territorio.title())
    print("Indicador :", nome_variavel(variavel))
    print("==============================================================")

    explicar_variavel(variavel)

    for registro in dados:

        if (registro["territorio"].lower() == territorio and
                registro["variavel"] == variavel):

            mostrar_registro(registro)
            encontrou = True

    if not encontrou:
        print("Nenhum registro encontrado.")


def filtrar_valor_minimo(dados):
    """Filtra registros por território, indicador e valor mínimo."""

    print("\nEscolha o indicador:")
    print("1 - Número índice da atividade turística")
    print("2 - Variação acumulada no ano")
    print("3 - Variação em relação ao mesmo mês do ano anterior")

    opcao = input("\nOpção: ")

    if opcao == "1":
        variavel = "numero_indice"

    elif opcao == "2":
        variavel = "variacao_acumulada_ano"

    elif opcao == "3":
        variavel = "variacao_mesmo_mes_ano_anterior"

    else:
        print("\nOpção inválida.")
        return

    territorio = input("\nDigite o território: ").strip().lower()

    valor = float(input("Digite o valor mínimo: "))

    encontrou = False

    print("\n==============================================================")
    print("Território:", territorio.title())
    print("Indicador :", nome_variavel(variavel))
    print("Valor mínimo:", valor, nome_unidade("pontos_de_indice") if variavel == "numero_indice" else "%")
    print("==============================================================\n")

    for registro in dados:

        if (
            registro["territorio"].lower() == territorio
            and registro["variavel"] == variavel
            and registro["valor"] >= valor
        ):

            print(
                f"{registro['mes']:<18}"
                f"{registro['valor']:>8.2f} "
                f"{nome_unidade(registro['unidade'])}"
            )

            encontrou = True

    if not encontrou:
        print("Nenhum registro encontrado.")


def ordenar_valores(dados, reverso=False):
    """Ordena os registros pelo valor."""

    ordenados = dados.copy()

    ordenados.sort(
        key=lambda registro: registro["valor"],
        reverse=reverso
    )

    print()

    for registro in ordenados:

        print(
            f"{registro['territorio']:<20}"
            f"{registro['mes']:<18}"
            f"{nome_variavel(registro['variavel']):<45}"
            f"{registro['valor']:>8.2f} "
            f"{nome_unidade(registro['unidade'])}"
        )


def menu_consultas(dados):

    while True:

        print("\n===================================")
        print("         MÓDULO 3")
        print("          CONSULTAS")
        print("===================================")
        print("1 - Número índice da atividade turística")
        print("2 - Variação acumulada no ano")
        print("3 - Variação em relação ao mesmo mês do ano anterior")
        print("4 - Filtrar registros por valor mínimo")
        print("5 - Ordenar valores (crescente)")
        print("6 - Ordenar valores (decrescente)")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            consultar_variavel(dados, "numero_indice")

        elif opcao == "2":
            consultar_variavel(dados, "variacao_acumulada_ano")

        elif opcao == "3":
            consultar_variavel(dados, "variacao_mesmo_mes_ano_anterior")

        elif opcao == "4":
            filtrar_valor_minimo(dados)

        elif opcao == "5":
            ordenar_valores(dados)

        elif opcao == "6":
            ordenar_valores(dados, True)

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")

        input("\nPressione ENTER para continuar...")

        
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

menu_consultas(dados_turismo)