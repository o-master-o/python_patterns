import pytest

from builder import ComputerBuilder


def test_builder_built_computer_with_all_provided_parts():
    computer_builder = ComputerBuilder()
    computer_builder.add_mother_board()
    computer_builder.add_cpu()
    computer_builder.add_ram()
    computer_builder.add_monitor()
    computer_builder.add_keyboard()
    print(computer_builder.product.parts)
    assert ['Mother board', 'CPU', 'RAM', 'Monitor', 'Keyboard'] == computer_builder.product.parts
