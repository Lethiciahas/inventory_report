from itertools import product
from inventory_report.inventory.product import Product


def test_cria_produto():
    inventory = Product(
        "10", "Titanium Dioxide", "Target Corporation", "2020-12-08",
        "2023-12-08", "FR29 5791 5333 58XR G4PR IG28 D08", "instrucao 10")

    assert inventory.id == "10"
    assert inventory.nome_do_produto == "Titanium Dioxide"
    assert inventory.nome_da_empresa == "Target Corporation"
    assert inventory.data_de_fabricacao == "2020-12-08"
    assert inventory.data_de_validade == "2023-12-08"
    assert inventory.numero_de_serie == "FR29 5791 5333 58XR G4PR IG28 D08"
    assert inventory.instrucoes_de_armazenamento == "instrucao 10"
