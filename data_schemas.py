from constants import OverdueFlag, AttendanceFlag, InactiveFlag
from pydantic import BaseModel, Field

employer_summary_description = "A professional, executive-level summary email crafted for an Account Manager to send directly to the employer. Highlight overall progress, praise top performers, and frame risks constructively."
escalation_items_description = "An array of objects for learners needing immediate intervention. Each item must contain 'learner_name', 'severity' (HIGH|MEDIUM|LOW), 'reason', and 'recommended_action'."


class CompanyExtraction(BaseModel):
    employer_summary: str = Field(description=employer_summary_description)
    escalation_items: list[Escalation] = Field(description=escalation_items_description)


class Escalation(BaseModel):
    learner_name: str = Field(description="Name of the learner")
    severity: str = Field(description="(HIGH|MEDIUM|LOW)")
    reason: str = Field(description="Reason for severity")
    recommended_action: str = Field(description="Recommended action to course correct the issue")

class CohortData(BaseModel):
    employer_name: str = Field(description="Name of the employer")
    cohort_name: str = Field(description="Name of the cohort / course")
    reporting_period: str = Field(description="Date of the course")
    learners: list = Field(description="List of learners")

class UserData(BaseModel):
    user_id: str = Field(description="Unique user ID")
    user_name: str = Field(description="Name of the learner")
    sessions_attended: int = Field(description="Number of sessions attended")
    total_sessions: int = Field(description="Total sessions in the course")
    assessments_submitted: int = Field(description="Number of assessments submitted")
    total_assessments: int = Field(description="Total assessments in the course")
    off_the_job_hours: float = Field(description="Number of off the job hours")
    target_hours: float = Field(description="Target number of hours")
    flags: list = Field(description="Learning progress flags")
