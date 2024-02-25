import sys
sys.path.append("..")

# fmt: off
import pytest
from src.tasks.task import Task
# fmt: on


class TestUpdate():
    """Test expected exceptions with Task.update"""

    def test_bad_id(self):
        """A non-int id should raise an exception"""
        with pytest.raises(TypeError):
            Task.update(task_id={'dict instead': 1}, task=Task())
