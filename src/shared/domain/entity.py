from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from src.shared.domain.notification import Notification


@dataclass
class Entity(ABC):
    notification: Notification = field(default_factory=Notification, init=False)

    @abstractmethod
    def validate(self):
        pass
