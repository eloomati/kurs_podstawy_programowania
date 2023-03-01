from unittest import TestCase #Importujemy odpowiedni moduł do testowania

from ut_mod_data import get_data_2 # Pobieramy sobie nasz moduł z funkcją którą chcemy testować

class DataTest(TestCase): #Tworzymy klase,k tóra dziedziczy po klasie TestCase z wczytanego modułu
    def test_first_last(self):
        data = get_data_2("Gary", "Feedbacker")
        self.assertEqual(data, 'Gary Feedbacker, Programista', ['Dane się nie zgadzają']) # Do argumentów assertEqual() można wpisać rownież komentarz do obsługi błędów
        #Specjalnie popsuty test dla pokazania
        # Opcjonalny komunikat się nie wyświetli ponieważ pierwszy zostanie wywołany TypeError:
        # TypeError: get_data2() missing 1 required positional argument: 'occupation'