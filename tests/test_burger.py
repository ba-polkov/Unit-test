class TestBurger:

    def test_add_bun_in_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_in_burger(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_remove_ingredient_from_burger(self, full_burger):
        full_burger.remove_ingredient(0)
        assert len(full_burger.ingredients) == 1

    def test_move_ingredient_in_burger(self, full_burger, mock_sauce):
        full_burger.move_ingredient(0, 1)
        assert full_burger.ingredients[1] == mock_sauce

    def test_get_full_price_burger(self, full_burger, mock_bun, mock_sauce, mock_filling):
        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price()
        assert full_burger.get_price() == expected_price


    def test_get_receipt_burger(self, full_burger):
        assert full_burger.get_receipt() == ('(==== white bun ====)\n'
                                              '= sauce sour cream =\n'
                                              '= filling dinosaur =\n'
                                              '(==== white bun ====)\n'
                                              '\n'
                                              'Price: 800')