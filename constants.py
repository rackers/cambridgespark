from abc import ABC, abstractmethod


class Flag(ABC):
    @abstractmethod
    def message(self):
        pass


class OverdueFlag(Flag):
    def __init__(self, assessment_id: int, overdue_span: int):
        self._assessment_id = assessment_id
        self._overdue_span = overdue_span

    @property
    def message(self):
        return f"Assessment {self._assessment_id} overdue by {self._overdue_span} days"


class AttendanceFlag(Flag):
    def __init__(self, attendance: float):
        self._attendance = attendance

    @property
    def message(self):
        return f"Attendance below threshold ({self._attendance})"


class InactiveFlag(Flag):
    def __init__(self, inactive_span: float):
        self._inactive_span = inactive_span

    @property
    def message(self):
        return f"No platform activity in past {self._inactive_span} days"
