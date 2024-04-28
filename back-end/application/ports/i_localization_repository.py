from abc import ABC, abstractmethod


class ILocalizationRespository(ABC):
    @abstractmethod
    def get_message(self, key):
        pass
