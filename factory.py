from typing import Type, Protocol
from pydantic import StrictStr


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


class UIFactory:
    def __init__(self):
        self._user_interfaces = {}
        
    def add_ui(self, ui: UI):
        self._user_interfaces[ui.name] = ui
        return self

    def greeting(self, language, user):
        return self._user_interfaces[language].greeting(user)
