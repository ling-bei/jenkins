import allure


class TestJen:

    @allure.step("测试步骤")
    def test(self):
        allure.attach("名称", "内容")
        assert True
