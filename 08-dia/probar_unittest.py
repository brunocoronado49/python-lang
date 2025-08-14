"""Unit tests for archivo_prueba module."""
import unittest
import archivo_prueba


class ProbarUnitText(unittest.TestCase):
    """Tests for the 'todo_mayus' function."""

    def test_mayusculas(self):
        """Check if the word is converted to uppercase."""
        palabra = 'hola'
        resultado = archivo_prueba.all_upper(palabra)
        self.assertEqual(resultado, 'HOLA')


if __name__ == '__main__':
    unittest.main()
