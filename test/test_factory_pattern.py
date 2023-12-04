import pytest

from creational_patterns.factory import UIFactory, SpanishUI, EnglishUI, GermanUI, NonExistentUIError


@pytest.fixture
def user_interface():
    ui_engine = UIFactory(SpanishUI(), EnglishUI(), GermanUI())
    return ui_engine


@pytest.mark.parametrize('language, user, expected_greeting', [
    ('English', 'Tom', 'Good morning Tom\nYou use English user interface'),
    ('German', 'Adele', 'Guten Morgen Adele\nSie verwenden eine Deutsche Benutzeroberfläche'),
    ('Spanish', 'Antonio', 'Buenos días Antonio\nEstás usando una interfaz en Español'),
])
def test_ui_factory_should_use_proper_language_interface(user_interface, language, user, expected_greeting):
    assert expected_greeting == user_interface(language).greeting(user)


def test_providing_non_existent_language_should_rise_non_existent_ui_error(user_interface):
    with pytest.raises(NonExistentUIError) as exc:
        user_interface('nonexistent')
    assert 'There is no user interface with nonexistent language' == str(exc.value)
