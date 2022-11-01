from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def estoque_por_empresa(list):
        list_produtos = ""
        list_empresas = [name["nome_da_empresa"] for name in list]
        counter = Counter(list_empresas)
        for produtos in counter:
            list_produtos += f"- {produtos}: {counter.get(produtos)}\n"
        return list_produtos

    def generate(list):
        return(
            f"{SimpleReport.generate(list)}\n"
            "Produtos estocados por empresa:\n"
            f"{CompleteReport.estoque_por_empresa(list)}"
        )
