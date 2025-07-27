from praktikum.praktikum import main

def test_main_function(capsys):
    main()
    captured = capsys.readouterr()
    assert "Price:" in captured.out