from django.test import TestCase

# Create your tests here.


class ModelTest(TestCase):
    def test_countries_by_name(self):
        from .models import NamedCountryList

        code = "FR"

        name = "France"

        france_by_code = NamedCountryList(name="list1", countries=["FR"])
        france_by_code.save()

        france_by_name = NamedCountryList(name="list2", countries=["France"])
        france_by_name.save()
        assert france_by_name.countries[0].code == france_by_code.countries[0].code
