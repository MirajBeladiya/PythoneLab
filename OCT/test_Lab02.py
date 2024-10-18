import pytest
import allure

@pytest.mark.smoke
def test_test_case_01():
    assert 2 * 2 == 4

def test_test_case_02():
    print("Hello TC2")
