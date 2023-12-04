from typing import List, Any

from pydantic import BaseModel, StrictStr, Field


class Computer(BaseModel):
    parts: List[StrictStr] = Field(default_factory=list)

    def add(self, part: StrictStr) -> None:
        self.parts.append(part)


class ComputerBuilder:

    def __init__(self) -> None:
        self._product = None
        self.reset()

    @property
    def product(self) -> Computer:
        return self._product

    def reset(self) -> None:
        self._product = Computer()

    def add_monitor(self) -> None:
        self._product.add('Monitor')

    def add_mother_board(self) -> None:
        self._product.add('Mother board')

    def add_cpu(self) -> None:
        self._product.add('CPU')

    def add_ram(self) -> None:
        self._product.add('RAM')

    def add_keyboard(self) -> None:
        self._product.add('Keyboard')
