from django.test import TestCase

from django_countries.data import ALT_CODES
from django_countries import countries

three2two = {v[0]: k for k, v in ALT_CODES.items()}
name2two = {v: k for k, v in dict(countries).items()}


# Create your tests here.


class TestByName(TestCase):
    """
    Use case:  i import files from a csv, countries may be either France or FR ..

    """

    def test_code(self):
        # impor here to avoid failure on test discovery
        from .models import NamedCountryList

        france_by_code = NamedCountryList(name="list1", countries=["FR"])
        france_by_code.save()

        france_by_name = NamedCountryList(name="list2", countries=["France"])
        france_by_name.save()
        assert france_by_name.countries[0].code == france_by_code.countries[0].code

    def test_name(self):
        from .models import NamedCountryList

        france_by_code = NamedCountryList(name="list1", countries=["FR"])
        france_by_code.save()

        france_by_name = NamedCountryList(name="list2", countries=["France"])
        france_by_name.save()

        assert france_by_code.countries[0].name == france_by_name.countries[0].name

    def test_code_workaround(self):
        from .models import NamedCountryList

        france_by_code = NamedCountryList(name="list1", countries=["FR"])
        france_hack_name = NamedCountryList(
            name="hacked", countries=[name2two[name] for name in ["France"]]
        )

        assert france_hack_name.countries[0].code == france_by_code.countries[0].code
        assert france_hack_name.countries[0].name == france_by_code.countries[0].name

        assert france_hack_name.countries[0].flag == france_by_code.countries[0].flag
