# Simulador de Carrinho de Compras (Versão Simples)
def exibir_carrinho(carrinho: list[dict]):
    print("\nResumo do carrinho:")
    total_itens = 0
    total_valor = 0.0

    for item in carrinho:
        nome = item["nome"]
        quantidade = item["quantidade"]
        preco = item["preco"]
        total_itens += quantidade
        total_valor += quantidade * preco
        print(f"{nome}: {quantidade} unidade(s) - R$ {preco:.2f} cada")

    print(f"\nTotal de itens: {total_itens}")
    print(f"Valor total da compra: R$ {total_valor:.2f}")


def main():
    # Carrinho de compras predefinido
    carrinho = [
        {"nome": "Maçã", "quantidade": 5, "preco": 1.99},
        {"nome": "Banana", "quantidade": 3, "preco": 2.50},
        {"nome": "Laranja", "quantidade": 4, "preco": 3.00},
    ]

    exibir_carrinho(carrinho)


if __name__ == "__main__":
    main()
