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


# ==========================
# MÓDULO 4 - ESTATÍSTICAS / EDA
# ==========================

def filtrar_por_variavel(dados, variavel):
    registros = []

    for registro in dados:
        if registro["variavel"] == variavel:
            registros.append(registro)

    return registros


def calcular_soma(valores):
    soma = 0

    for valor in valores:
        soma += valor

    return soma


def calcular_media(valores):
    if len(valores) == 0:
        return 0

    return calcular_soma(valores) / len(valores)


def registro_do_maximo(dados, variavel="numero_indice"):
    registros = filtrar_por_variavel(dados, variavel)

    if len(registros) == 0:
        return None

    maior = registros[0]

    for registro in registros:
        if registro["valor"] > maior["valor"]:
            maior = registro

    return maior


def registro_do_minimo(dados, variavel="numero_indice"):
    registros = filtrar_por_variavel(dados, variavel)

    if len(registros) == 0:
        return None

    menor = registros[0]

    for registro in registros:
        if registro["valor"] < menor["valor"]:
            menor = registro

    return menor


def media_da_variavel(dados, variavel="numero_indice"):
    valores = []

    for registro in dados:
        if registro["variavel"] == variavel:
            valores.append(registro["valor"])

    return calcular_media(valores)


def agrupar_por_territorios(dados, variavel="numero_indice"):
    grupos = {}

    for registro in dados:
        if registro["variavel"] == variavel:
            territorio = registro["territorio"]
            valor = registro["valor"]

            if territorio not in grupos:
                grupos[territorio] = []

            grupos[territorio].append(valor)

    return grupos


def media_por_territorios(dados, variavel="numero_indice"):
    grupos = agrupar_por_territorios(dados, variavel)
    medias = {}

    for territorio, valores in grupos.items():
        medias[territorio] = calcular_media(valores)

    return medias


def ranking_territorios(dados, quantidade=10, decrescente=True, variavel="numero_indice"):
    medias = media_por_territorios(dados, variavel)
    lista = list(medias.items())

    lista_ordenada = sorted(
        lista,
        key=lambda item: item[1],
        reverse=decrescente
    )

    return lista_ordenada[:quantidade]


def escolher_quantidade_ranking():
    print("\nQual ranking você quer ver?")
    print("  [1] Top 3")
    print("  [2] Top 10")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        return 3

    elif escolha == "2":
        return 10

    else:
        print("Opção inválida, mostrando Top 10 por padrão.")
        return 10


def evolucao_mensal(dados, territorio="Brasil", variavel="numero_indice"):
    evolucao = {}

    for registro in dados:
        if (
            registro["territorio"].lower() == territorio.lower()
            and registro["variavel"] == variavel
        ):
            evolucao[registro["mes"]] = registro["valor"]

    return evolucao


def calcular_variacao_percentual(valor_inicial, valor_final):
    if valor_inicial == 0:
        return 0

    return ((valor_final - valor_inicial) / valor_inicial) * 100


def variacao_periodo(dados, territorio="Brasil", variavel="numero_indice"):
    evolucao = evolucao_mensal(dados, territorio, variavel)
    valores = list(evolucao.values())

    if len(valores) == 0:
        return None

    valor_inicial = valores[0]
    valor_final = valores[-1]
    variacao = calcular_variacao_percentual(valor_inicial, valor_final)

    return valor_inicial, valor_final, variacao


def variacao_por_territorios(dados, variavel="numero_indice"):
    territorios = []

    for registro in dados:
        territorio = registro["territorio"]

        if territorio not in territorios:
            territorios.append(territorio)

    resultado = []

    for territorio in territorios:
        variacao = variacao_periodo(dados, territorio, variavel)

        if variacao is not None:
            valor_inicial, valor_final, percentual = variacao

            resultado.append({
                "territorio": territorio,
                "valor_inicial": valor_inicial,
                "valor_final": valor_final,
                "variacao": percentual
            })

    return resultado


def ranking_variacao_territorios(dados, quantidade=10, decrescente=True):
    variacoes = variacao_por_territorios(dados, "numero_indice")

    ordenados = sorted(
        variacoes,
        key=lambda item: item["variacao"],
        reverse=decrescente
    )

    return ordenados[:quantidade]


def exibir_menu_estatisticas():
    print("-" * 60)
    print("EDA - ANÁLISE EXPLORATÓRIA DOS DADOS TURÍSTICOS")
    print("-" * 60)
    print("  [1] Estatísticas gerais do número índice")
    print("  [2] Ranking de territórios por média do índice")
    print("  [3] Ranking de crescimento do índice")
    print("  [4] Evolução mensal de um território")
    print("  [5] Destaques do turismo")
    print("  [0] Voltar ao menu principal")
    print("-" * 60)


def mostrar_estatisticas(dados):
    while True:
        exibir_menu_estatisticas()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registros_indice = filtrar_por_variavel(dados, "numero_indice")
            territorios = []

            for registro in registros_indice:
                if registro["territorio"] not in territorios:
                    territorios.append(registro["territorio"])

            media_indice = media_da_variavel(dados, "numero_indice")
            maximo = registro_do_maximo(dados, "numero_indice")
            minimo = registro_do_minimo(dados, "numero_indice")
            resultado_variacao = variacao_periodo(dados, "Brasil", "numero_indice")

            print("\n--- ESTATÍSTICAS GERAIS DO NÚMERO ÍNDICE ---")
            print(f"Quantidade de registros do número índice: {len(registros_indice)}")
            print(f"Quantidade de territórios analisados: {len(territorios)}")
            print(f"Média geral do número índice: {media_indice:.2f} pontos")

            if maximo:
                print(
                    f"Maior número índice: {maximo['valor']:.2f} pontos "
                    f"({maximo['territorio']}, {maximo['mes']})"
                )

            if minimo:
                print(
                    f"Menor número índice: {minimo['valor']:.2f} pontos "
                    f"({minimo['territorio']}, {minimo['mes']})"
                )

            if resultado_variacao:
                valor_inicial, valor_final, variacao = resultado_variacao

                print(
                    f"Variação do número índice no Brasil: "
                    f"{valor_inicial:.2f} -> {valor_final:.2f} "
                    f"({variacao:.2f}%)"
                )

        elif opcao == "2":
            quantidade = escolher_quantidade_ranking()

            print(f"\n--- TOP {quantidade} TERRITÓRIOS POR MÉDIA DO NÚMERO ÍNDICE ---")
            for posicao, item in enumerate(ranking_territorios(dados, quantidade, True), start=1):
                territorio, media = item
                print(f"{posicao}. {territorio}: {media:.2f} pontos")

            print(f"\n--- {quantidade} TERRITÓRIOS COM MENORES MÉDIAS DO NÚMERO ÍNDICE ---")
            for posicao, item in enumerate(ranking_territorios(dados, quantidade, False), start=1):
                territorio, media = item
                print(f"{posicao}. {territorio}: {media:.2f} pontos")

        elif opcao == "3":
            quantidade = escolher_quantidade_ranking()

            print(f"\n--- TOP {quantidade} MAIORES CRESCIMENTOS DO NÚMERO ÍNDICE ---")
            for posicao, item in enumerate(ranking_variacao_territorios(dados, quantidade, True), start=1):
                print(
                    f"{posicao}. {item['territorio']}: "
                    f"{item['valor_inicial']:.2f} -> {item['valor_final']:.2f} "
                    f"({item['variacao']:.2f}%)"
                )

            print(f"\n--- TOP {quantidade} MAIORES QUEDAS DO NÚMERO ÍNDICE ---")
            for posicao, item in enumerate(ranking_variacao_territorios(dados, quantidade, False), start=1):
                print(
                    f"{posicao}. {item['territorio']}: "
                    f"{item['valor_inicial']:.2f} -> {item['valor_final']:.2f} "
                    f"({item['variacao']:.2f}%)"
                )

        elif opcao == "4":
            territorio = input("Digite o nome do território (ex: Brasil): ")

            evolucao = evolucao_mensal(dados, territorio, "numero_indice")

            if not evolucao:
                print(f"\nNenhum dado encontrado para '{territorio}'.")

            else:
                print(f"\n--- EVOLUÇÃO MENSAL DO NÚMERO ÍNDICE: {territorio} ---")

                for mes, valor in evolucao.items():
                    print(f"{mes}: {valor:.2f} pontos")

                resultado_variacao = variacao_periodo(dados, territorio, "numero_indice")

                if resultado_variacao:
                    valor_inicial, valor_final, variacao = resultado_variacao

                    print(
                        f"\nVariação no período: "
                        f"{valor_inicial:.2f} -> {valor_final:.2f} "
                        f"({variacao:.2f}%)"
                    )

        elif opcao == "5":
            medias = media_por_territorios(dados, "numero_indice")
            maior_media = max(medias, key=medias.get)
            menor_media = min(medias, key=medias.get)

            maior_crescimento = ranking_variacao_territorios(dados, 1, True)[0]
            maior_queda = ranking_variacao_territorios(dados, 1, False)[0]

            maximo = registro_do_maximo(dados, "numero_indice")
            minimo = registro_do_minimo(dados, "numero_indice")

            print("\n--- DESTAQUES DO TURISMO ---")

            print(
                f"O território com maior média do número índice foi "
                f"{maior_media}, com média de {medias[maior_media]:.2f} pontos."
            )

            print(
                f"O território com menor média do número índice foi "
                f"{menor_media}, com média de {medias[menor_media]:.2f} pontos."
            )

            print(
                f"O maior crescimento no período foi de "
                f"{maior_crescimento['territorio']}, com variação de "
                f"{maior_crescimento['variacao']:.2f}%."
            )

            print(
                f"A maior queda no período foi de "
                f"{maior_queda['territorio']}, com variação de "
                f"{maior_queda['variacao']:.2f}%."
            )

            print(
                f"O maior valor mensal do número índice foi "
                f"{maximo['valor']:.2f} pontos em {maximo['territorio']} "
                f"no mês de {maximo['mes']}."
            )

            print(
                f"O menor valor mensal do número índice foi "
                f"{minimo['valor']:.2f} pontos em {minimo['territorio']} "
                f"no mês de {minimo['mes']}."
            )

        elif opcao == "0":
            break

        else:
            print("Opção inválida, tente novamente.")

        if opcao != "0":
            input("\nPressione ENTER para continuar...")
def exibir_menu_estatisticas():
    print("-" * 50)
    print("ESTATISTICAS - Índice Atividades Turisticas 2025")
    print("-" * 50)
    print("  [1] Estatisticas gerais")
    print("  [2] Ranking de territorios (maiores medias)")
    print("  [3] Ranking de territorios (menores medias)")
    print("  [4] Evolucao mensal de um territorio")
    print("  [5] Destaques do Turismo")
    print("  [0] Voltar ao menu principal")
    print("-" * 50)
 
 
def mostrar_estatisticas(dados):
    while True:
        exibir_menu_estatisticas()
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            registros_indice = [r for r in dados if r["variavel"] == "numero_indice"]
            valores = [registro["valor"] for registro in registros_indice]
            maximo = registro_do_maximo(dados)
            minimo = registro_do_minimo(dados)
            resultado_variacao = variacao_periodo(dados, "Brasil")

            print("\n--- ESTATISTICAS GERAIS (Numero Indice) ---")
            print(f"Quantidade de registros: {len(valores)}")
            print(f"Media geral do indice: {calcular_media(valores):.2f}")
            print(
                f"Maximo: {maximo['valor']:.2f} "
                f"({maximo['territorio']}, {maximo['mes']})")
            print(
                f"Minimo: {minimo['valor']:.2f} "
                f"({minimo['territorio']}, {minimo['mes']})")

            if resultado_variacao:
                valor_inicial, valor_final, variacao = resultado_variacao
                print(
                    f"Variacao do indice no Brasil (primeiro mes: {valor_inicial:.2f} "
                    f"-> ultimo mes: {valor_final:.2f}): {variacao:.2f}%")
 
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
 
            print("\n--- Destaques do turismo ---")
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
# MÓDULO 5 - RELATÓRIO
# ==========================

from datetime import datetime
def gerar_relatorio(dados, caminho_saida="relatorio_turismo.txt"):
    registros_indice = [r for r in dados if r["variavel"] == "numero_indice"]
    valores = [r["valor"] for r in registros_indice]

    quantidade = len(valores)
    media = calcular_media(valores)

    maximo = registro_do_maximo(dados, "numero_indice")
    minimo = registro_do_minimo(dados, "numero_indice")

    # Frequência e percentual por território.
    freq = {}
    for r in registros_indice:
        freq[r["territorio"]] = freq.get(r["territorio"], 0) + 1

    percentual = {}
    for territorio, contagem in freq.items():
        percentual[territorio] = (contagem / quantidade) * 100

    maiores = ranking_territorios(dados, 10, True, "numero_indice")
    menores = ranking_territorios(dados, 10, False, "numero_indice")

    medias = media_por_territorios(dados, "numero_indice")
    maior_territorio = max(medias, key=medias.get)
    menor_territorio = min(medias, key=medias.get)

    resultado_variacao = variacao_periodo(dados, "Brasil", "numero_indice")

    linhas = []
    linhas.append("=" * 60)
    linhas.append("RELATÓRIO - SISTEMA DE ANÁLISE DE TURISMO")
    linhas.append("Fonte: IBGE - Tabela 8694")
    linhas.append(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    linhas.append("=" * 60)

    linhas.append("\n1. ESTATÍSTICAS GERAIS DO NÚMERO ÍNDICE")
    linhas.append("-" * 60)
    linhas.append(f"Quantidade total de registros no CSV : {len(dados)}")
    linhas.append(f"Quantidade de registros analisados   : {quantidade}")
    linhas.append(f"Média geral do número índice         : {media:.2f} pontos")

    if maximo:
        linhas.append(
            f"Máximo                                : "
            f"{maximo['valor']:.2f} pontos "
            f"({maximo['territorio']}, {maximo['mes']})"
        )

    if minimo:
        linhas.append(
            f"Mínimo                                : "
            f"{minimo['valor']:.2f} pontos "
            f"({minimo['territorio']}, {minimo['mes']})"
        )

    linhas.append("\n2. DISTRIBUIÇÃO DOS REGISTROS POR TERRITÓRIO")
    linhas.append("-" * 60)

    for territorio, contagem in freq.items():
        linhas.append(
            f"{territorio:<20} {contagem:>3} registros "
            f"({percentual[territorio]:.1f}%)"
        )

    linhas.append("\n3. RANKING - TOP 10 TERRITÓRIOS COM MAIOR MÉDIA")
    linhas.append("-" * 60)

    for posicao, item in enumerate(maiores, start=1):
        territorio, media_territorio = item
        linhas.append(f"{posicao:>2}. {territorio:<20} {media_territorio:.2f} pontos")

    linhas.append("\n4. RANKING - 10 TERRITÓRIOS COM MENOR MÉDIA")
    linhas.append("-" * 60)

    for posicao, item in enumerate(menores, start=1):
        territorio, media_territorio = item
        linhas.append(f"{posicao:>2}. {territorio:<20} {media_territorio:.2f} pontos")

    linhas.append("\n5. VARIAÇÃO DO NÚMERO ÍNDICE NO BRASIL")
    linhas.append("-" * 60)

    if resultado_variacao:
        vi, vf, var = resultado_variacao
        tendencia = "cresceu" if var > 0 else "caiu"

        linhas.append(f"Valor inicial do índice : {vi:.2f} pontos")
        linhas.append(f"Valor final do índice   : {vf:.2f} pontos")
        linhas.append(
            f"O índice do Brasil {tendencia} "
            f"{abs(var):.2f}% no período analisado."
        )
    else:
        linhas.append("Não foi possível calcular a variação para o Brasil.")

    linhas.append("\n6. INSIGHTS")
    linhas.append("-" * 60)
    linhas.append(
        f"O território com maior índice médio foi {maior_territorio}, "
        f"com média de {medias[maior_territorio]:.2f} pontos."
    )
    linhas.append(
        f"O território com menor índice médio foi {menor_territorio}, "
        f"com média de {medias[menor_territorio]:.2f} pontos."
    )
    linhas.append(
        "A análise foi concentrada no número índice da atividade turística, "
        "pois esse indicador representa diretamente o nível da atividade "
        "turística nos territórios analisados."
    )
    linhas.append(
        "As variáveis de variação acumulada e variação em relação ao mesmo mês "
        "do ano anterior foram mantidas para consultas, mas não foram misturadas."
    )

    linhas.append("\n" + "=" * 60)
    linhas.append("Fim.")

    conteudo = "\n".join(linhas)

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print(f"\nRelatório gerado com sucesso na mesma pasta deste arquivo python: {caminho_saida}")
    return caminho_saida


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
        print("3 - Gerar relatório TXT")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_consultas(dados_turismo)

        elif opcao == "2":
            mostrar_estatisticas(dados_turismo)

        elif opcao == "3":
            gerar_relatorio(dados_turismo)

        elif opcao == "0":
            print("\nVolte sempre...")
            break

        else:
            print("\nOpção inválida.")
menu_principal()