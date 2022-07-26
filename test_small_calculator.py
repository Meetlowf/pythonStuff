from small_calculator import SmallCalculator
 
 
class TestCalculator(object):
    def test_increments_by_one(self):
        # arrange
        initial_value = 4
        subject = SmallCalculator(initial_value)
 
        # act
        result = subject.increment_by_one()
 
        # assert
        assert result == initial_value + 1
 
    def test_increments_by_one_from_zero_returns_one(self):
        # arrange
        initial_value = 0
        subject = SmallCalculator(initial_value)
 
        # act
        result = subject.increment_by_one()
 
        # assert
        assert result == 1
 
    def test_increments_by_greater_than_one(self):
        # arrange
        init_value = 4
        subject = SmallCalculator(init_value)
 
        # act
        result = subject.increment_by_amount(20)
 
        # assert
        assert result == init_value + 20
 
    def test_increments_by_negative_value(self):
        # arrange
        init_value = 4
        subject = SmallCalculator(init_value)
 
        # act
        result = subject.increment_by_amount(-123)
 
        # assert
        assert result == init_value - 123
 
    def test_increments_by_zero(self):
        # arrange
        init_value = 4
        subject = SmallCalculator(init_value)
 
        # act
        result = subject.increment_by_amount(0)
 
        # assert
        assert result == init_value
 
 
if __name__ == "__main__":
    calculator = TestCalculator()
 
    calculator.test_increments_by_one()
    calculator.test_increments_by_one_from_zero_returns_one()
    calculator.test_increments_by_greater_than_one()
    calculator.test_increments_by_negative_value()
    calculator.test_increments_by_zero()