import httpx
import time

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"


def fetch_pokemon_data(pokemon_name):
    response = httpx.get(f"{POKEMON_URL}{pokemon_name}")
    if response.status_code == 200:
        pokemon = response.json()
        print(
            f"{pokemon_name.capitalize()} é do tipo {pokemon['types'][0]['type']['name']}"
        )
    else:
        print(f"Erro ao buscar dados do {pokemon_name}")


def main_sync():
    print("Iniciando requisições síncronas à API do Pokémon...")

    start_time = time.time()

    # Fazendo requisições de forma sequencial (sem concorrência)
    fetch_pokemon_data("pikachu")
    fetch_pokemon_data("bulbasaur")
    fetch_pokemon_data("charmander")

    end_time = time.time()
    print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")


if __name__ == "__main__":
    main_sync()
