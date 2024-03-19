import pytest
from src.tasks.domain.value_objects.priority import Priority


class TestPriority:

    def test_low_priority(self):
        assert Priority.LOW.value == "Low"

    def test_high_priority(self):
        assert Priority.HIGH.value == "High"

    def test_normal_priority(self):
        assert Priority.NORMAL.value == "Normal"

    def test_invalid_priory(self):
        with pytest.raises(ValueError):
            Priority("invalid_priority")
