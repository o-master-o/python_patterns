import pytest

from factory import UIFactory, SpanishUI, EnglishUI, GermanUI


@pytest.fixture
def user_interface():
    translator_engine = UIFactory()
    translator_engine.add_ui(SpanishUI()).add_ui(EnglishUI()).add_ui(GermanUI())
    return translator_engine


@pytest.mark.parametrize('language, user, expected_greeting', [
    ('English', 'Tom', 'Good morning Tom\nYou use English user interface'),
    ('German', 'Adele', 'Guten Morgen Adele\nSie verwenden eine Deutsche Benutzeroberfläche'),
    ('Spanish', 'Antonio', 'Buenos días Antonio\nEstás usando una interfaz en Español'),
])
def test_translate_to_languages(user_interface, language, user, expected_greeting):
    assert expected_greeting == user_interface.greeting(language, user)
