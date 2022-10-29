from inventory_report.inventory.product import Product


def test_relatorio_produto():
    expected = Product(
        "10", "Titanium Dioxide", "Target Corporation", "2020-12-08",
        "2023-12-08", "FR29 5791 5333 58XR G4PR IG28 D08", "instrucao 10")
    report = str(
        f"O produto {expected.nome_do_produto}"
        f" fabricado em {expected.data_de_fabricacao}"
        f" por {expected.nome_da_empresa} com validade"
        f" até {expected.data_de_validade}"
        f" precisa ser armazenado {expected.instrucoes_de_armazenamento}."
    )

    assert expected.__repr__() == report
