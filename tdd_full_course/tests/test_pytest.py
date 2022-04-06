from src.example_01 import brincadeira

"""GWT
"""

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1
    esperado = 1
    resultado = brincadeira(1)
    assert resultado == esperado