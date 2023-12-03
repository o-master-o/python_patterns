from typing import Protocol


class UI(Protocol):
    name: str
    native_name: str

    def greeting(self, user: str) -> str:
        pass


class EnglishUI:
    name = 'English'
    native_name = 'English'

    def greeting(self, user):
        return (f'Good morning {user}\n'
                f'You use {self.name} user interface')


class SpanishUI:
    name = 'Spanish'
    native_name = 'Español'

    def greeting(self, user):
        return (f'Buenos días {user}\n'
                f'Estás usando una interfaz en {self.native_name}')


class GermanUI:
    name = 'German'
    native_name = 'Deutsche'

    def greeting(self, user):
        return (f'Guten Morgen {user}\n'
                f'Sie verwenden eine {self.native_name} Benutzeroberfläche')


class NonExistentUIError(Exception):
    pass


class UIFactory:
    def __init__(self, *uis: UI):
        self._user_interfaces = {}
        self._register_ues(uis)

    def _register_ues(self, uis):
        for ui in uis:
            self._add_ui(ui)

    def _add_ui(self, ui: UI):
        self._user_interfaces[ui.name] = ui

    def __call__(self, language: str):
        try:
            return self._user_interfaces[language]
        except KeyError as exc:
            print(exc)
            raise NonExistentUIError(f'There is no user interface with {language} language')

