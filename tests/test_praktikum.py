import pytest
from unittest.mock import patch, MagicMock
from practicum.praktikum import main


def test_main_function_prints_receipt(capsys):
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "bun_1"

    mock_sauce = MagicMock()
    mock_sauce.get_name.return_value = "sauce_1"

    mock_db = MagicMock()
    mock_db.available_buns.return_value = [mock_bun]
    mock_db.available_ingredients.return_value = [
        MagicMock(), mock_sauce, MagicMock(), mock_sauce, mock_sauce, mock_sauce
    ]

    with patch("Diplom_1.practicum.praktikum.Database", return_value=mock_db):
        try:
            main()
        except Exception as e:
            pytest.fail(f"main() raised an exception: {e}")

    output = capsys.readouterr().out

    assert "bun_1" in output
    assert "sauce_1" in output
    assert "Price:" in output
