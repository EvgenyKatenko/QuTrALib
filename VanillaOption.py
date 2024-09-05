from dataclasses import dataclass, field
from datetime import date
from abc import ABC

class IInstrument(ABC):
    pass

@dataclass
class VanillaOption(IInstrument):
    _strike: float = field(repr=False)
    _expiry_date: date = field(repr=False)

    def get_strike(self) -> float:
        return self._strike

    def get_expiry_date(self) -> date:
        return self._expiry_date

@dataclass
class EuropeanCallOption(VanillaOption):
    pass

@dataclass
class EuropeanPutOption(VanillaOption):
    pass
