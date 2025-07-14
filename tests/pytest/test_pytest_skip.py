import pytest


@pytest.mark.skip(reason="In Development")
def test_feature_in_development():
    ...


@pytest.mark.skip(reason="In Development")
class TestSuitSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...
