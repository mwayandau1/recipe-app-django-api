from django.test import SimpleTestCase
from .import calc


class TestCaseNum(SimpleTestCase):
    """Test add"""

    def test_add_num(self):
        res = calc.calculateNum(4, 6)
        self.assertEqual(res, 10)

    """Test subtract"""

    def test_subtract(self):
        res = calc.sub(10, 4)
        self.assertEqual(res, 6)
