# Base: Tabela 8694 do IBGE - Atividades turísticas
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


# estatisticas
def calcular_soma(valores):
    return sum(valores)
def calcular_media(valores):
    return calcular_soma(valores) / len(valores)
def calcular_minimo(valores):
    return min(valores)

#aqui vem funcoes que trabalham com dicts

def registro_do_maximo(dados):
    #devolve o dicionario todo do maior indice
    return max(dados, key=lambda registro: registro["valor"])

def registro_do_minimo(dados):
    #mesma coisa so que menor indice
    return min(dados, key=lambda registro: registro["valor"])
def agrupar_por_territorios(dados):
    grupos = {}
    for registro in dados:
        territorio = registro["territorio"]
        valor = registro["valor"]
        if territorio not in grupos:
            grupos[territorio] = []
        grupos[territorio].append(valor)
    return grupos

def media_por_territorios(dados):
    grupos = agrupar_por_territorios(dados)
    medias = {}
    for territorio, valores in grupos.items():
        medias[territorio] = calcular_media(valores)
    return medias 

#top 10 
def ranking_territorios(dados, quantidade=10, decrescente=True):
    media = media_por_territorios(dados)
    lista_ordenada = sorted(media.items(), key=lambda item: item[1], reverse=decrescente)
    return lista_ordenada[:quantidade]

#funcao pro submenu
def escolher_quantidade_ranking():
    print("\nQual ranking voce quer ver?")
    print("  [1] Top 3")
    print("  [2] Top 10")
    escolha = input("Escolha uma opcao: ")

    if escolha == "1":
        return 3
    elif escolha == "2":
        return 10
    else:
        print("Opcao invalida, mostrando Top 10 por padrao.")
        return 10

def evolucao_mensal(dados, territorio="Brasil"):
    #mes a mes, territorio especifico
    evolucao = {}
    for registro in dados:
        if registro["territorio"].lower() == territorio.lower():
            evolucao[registro["mes"]] = registro["valor"]
    return evolucao


# --- variacao percentual (substitui a "soma", que nao tem sentido economico) ---
def calcular_variacao_percentual(valor_inicial, valor_final):
    # mostra quanto o indice cresceu ou caiu, em percentual, entre dois pontos no tempo
    return ((valor_final - valor_inicial) / valor_inicial) * 100


def variacao_periodo(dados, territorio="Brasil"):
    # compara o primeiro e o ultimo mes disponivel para o territorio
    evolucao = evolucao_mensal(dados, territorio)
    valores = list(evolucao.values())

    if not valores:
        return None

    valor_inicial = valores[0]
    valor_final = valores[-1]
    variacao = calcular_variacao_percentual(valor_inicial, valor_final)

    return valor_inicial, valor_final, variacao


def exibir_menu_estatisticas():
    print("-" * 50)
    print("ESTATISTICAS - Índice Atividades Turisticas 2025")
    print("-" * 50)
    print("  [1] Estatisticas gerais")
    print("  [2] Ranking de territorios (maiores medias)")
    print("  [3] Ranking de territorios (menores medias)")
    print("  [4] Evolucao mensal de um territorio")
    print("  [5] Insights")
    print("  [0] Voltar ao menu principal")
    print("-" * 50)
 
 
def mostrar_estatisticas(dados):
    while True:
        exibir_menu_estatisticas()
        opcao = input("Escolha uma opcao: ")
 
        if opcao == "1":
            valores = [registro["valor"] for registro in dados]
            maximo = registro_do_maximo(dados)
            minimo = registro_do_minimo(dados)
            resultado_variacao = variacao_periodo(dados, "Brasil")
 
            print("\n--- ESTATISTICAS GERAIS ---")
            print(f"Quantidade de registros: {len(valores)}")
            print(f"Media geral do indice: {calcular_media(valores):.2f}")
            print(
                f"Maximo: {maximo['valor']:.2f} "
                f"({maximo['territorio']}, {maximo['mes']})"
            )
            print(
                f"Minimo: {minimo['valor']:.2f} "
                f"({minimo['territorio']}, {minimo['mes']})"
            )

            if resultado_variacao:
                valor_inicial, valor_final, variacao = resultado_variacao
                print(
                    f"Variacao do indice no Brasil (primeiro mes: {valor_inicial:.2f} "
                    f"-> ultimo mes: {valor_final:.2f}): {variacao:.2f}%"
                )
 
        elif opcao == "2":
            quantidade = escolher_quantidade_ranking()   # pergunta e guarda a resposta (3 ou 10)
            print(f"\n--- TOP {quantidade} TERRITORIOS (MAIOR MEDIA) ---")
            for territorio, media in ranking_territorios(dados, quantidade, True):
                print(f"{territorio}: {media:.2f}")
        
        elif opcao == "3":
            quantidade = escolher_quantidade_ranking()   # pergunta e guarda a resposta (3 ou 10)
            print(f"\n--- TOP {quantidade} TERRITORIOS (MENOR MEDIA) ---")
            for territorio, media in ranking_territorios(dados, quantidade, False):
                print(f"{territorio}: {media:.2f}")
        elif opcao == "4":
            territorio = input("Digite o nome do territorio (ex: Brasil): ")
            evolucao = evolucao_mensal(dados, territorio)
 
            if not evolucao:
                print(f"\nNenhum dado encontrado para '{territorio}'.")
            else:
                print(f"\n--- EVOLUCAO MENSAL: {territorio} ---")
                for mes, valor in evolucao.items():
                    print(f"{mes}: {valor:.2f}")
 
        elif opcao == "5":
            medias = media_por_territorios(dados)
            maior_territorio = max(medias, key=medias.get)
            menor_territorio = min(medias, key=medias.get)
 
            print("\n--- INSIGHTS ---")
            print(
                f"O territorio com maior indice medio de turismo e "
                f"{maior_territorio}, com media de {medias[maior_territorio]:.2f} pontos."
            )
            print(
                f"O territorio com menor indice medio e "
                f"{menor_territorio}, com media de {medias[menor_territorio]:.2f} pontos."
            )
 
        elif opcao == "0":
            break
        else:
            print("Opcao invalida, tente novamente.")
 
        if opcao != "0":
            input("\nPressione ENTER para continuar...")

# ==========================
# MENU PRINCIPAL
# ==========================

def menu_principal():

    while True:

        print("\n" + "=" * 50)
        print("SISTEMA DE DADOS DE TURISMO - IBGE")
        print("=" * 50)
        print("1 - Consultas")
        print("2 - Estatísticas")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_consultas(dados_turismo)

        elif opcao == "2":
            mostrar_estatisticas(dados_turismo)

        elif opcao == "0":
            print("\nEncerrando sistema...")
            break

        else:
            print("\nOpção inválida.")

menu_principal()