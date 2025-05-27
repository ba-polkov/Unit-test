import allure

from Diplom_1.bun import Bun

class TestBun:

    @allure.title('Тест на успешное создание новой булки')
    # успешно создать новую булку
    def test_new_bun(self):
        bun = Bun("Булка смерти", 405)
        assert bun.get_name() == "Булка смерти"
        assert bun.get_price() == 405