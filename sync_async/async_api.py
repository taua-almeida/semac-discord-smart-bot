import httpx
import asyncio
import time

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"


async def fetch_pokemon_data_async(pokemon_name):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEMON_URL}{pokemon_name}")
        if response.status_code == 200:
            pokemon = response.json()
            print(
                f"{pokemon_name.capitalize()} é do tipo {pokemon['types'][0]['type']['name']}"
            )
        else:
            print(f"Erro ao buscar dados do {pokemon_name}")


async def main_async():
    print("Iniciando requisições assíncronas à API do Pokémon...")

    start_time = time.time()

    # Fazendo as requisições de forma concorrente
    tasks = [
        fetch_pokemon_data_async("pikachu"),
        fetch_pokemon_data_async("bulbasaur"),
        fetch_pokemon_data_async("charmander"),
    ]

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")


if __name__ == "__main__":
    asyncio.run(main_async())
