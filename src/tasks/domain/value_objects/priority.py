from enum import Enum


class Priority(Enum):
    """Represents the priority of task

    Attributes:
        LOW: The low priority
        HIGH: The high priority
        NORMAL: The normal priority
    """

    LOW = "LOW"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
