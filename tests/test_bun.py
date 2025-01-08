class TestBun:

    def test_get_name_get_right_name(self, mock_bun):
        assert mock_bun.get_name() == mock_bun.name

    def test_get_name_get_right_price(self, mock_bun):
        assert mock_bun.get_price() == mock_bun.price