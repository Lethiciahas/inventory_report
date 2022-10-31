from collections import Counter


class SimpleReport():
    def fabricacao_mais_antiga(list):
        list_products = [product["data_de_fabricacao"] for product in list]
        return min(list_products)

    def validade_mais_proxima(list):
        list_products = [product["data_de_validade"]for product in list]
        return min(list_products)

    def empresa_com_mais_produtos(list):
        list_empresa = [empresa["nome_da_empresa"] for empresa in list]
        list_counter = Counter(list_empresa)
        return max(list_counter, key=list_counter.get)

    def generate(list):
        fabricacao_mais_antiga = SimpleReport.fabricacao_mais_antiga(list)
        validade_mais_proxima = SimpleReport.validade_mais_proxima(list)
        maior_estoque = SimpleReport.empresa_com_mais_produtos(list)

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {maior_estoque}"
        )
