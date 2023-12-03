from typing import Protocol

import pydantic
from pydantic import StrictStr, BaseModel


class UI(Protocol):
    name: StrictStr
    native_name: StrictStr

    def greeting(self, user: StrictStr):
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
    def __init__(self):
        self._user_interfaces = {}
        
    def add_ui(self, ui: UI):
        self._user_interfaces[ui.name] = ui
        return self

    def __call__(self, language: StrictStr):
        try:
            return self._user_interfaces[language]
        except KeyError as exc:
            print(exc)
            raise NonExistentUIError(f'There is no user interface with {language} language')

