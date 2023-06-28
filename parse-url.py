from unittest import TestCase, main
from pokeapi_parse import get_pokemon_info

class CalcTest(TestCase):
    def test_get_pokemon_info(self):
        self.assertEqual(get_pokemon_info("132"),('ditto', ['limber', 'imposter']))
    def test_get_pokemon_info_positive(self):
        pokemon_info = get_pokemon_info(7)
        self.assertEqual(pokemon_info, ('squirtle', ['torrent', 'rain-dish']))

    def test_get_pokemon_info_invalid_id(self):
        # Негативный тест для некорректного ID покемона
        pokemon_info = get_pokemon_info(10000000)
        self.assertIsNone(pokemon_info)

    def test_get_pokemon_info_string_id(self):
        # Негативный тест для передачи строки вместо числового ID
        pokemon_info = get_pokemon_info("Pikachu")
        self.assertIsNone(pokemon_info)

    def test_get_pokemon_info_zero_id(self):
        # Негативный тест для передачи нулевого ID покемона
        pokemon_info = get_pokemon_info(0)
        self.assertIsNone(pokemon_info)

if __name__ == '__main__':
    main()