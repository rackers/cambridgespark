from constants import InactiveFlag, OverdueFlag, AttendanceFlag
from data_schemas import CohortData, UserData

MOCK_COHORT_DATA = CohortData(
    employer_name="Acme Corp",
    cohort_name="Data Engineering Apprenticeship - Cohort 4",
    reporting_period="February 2026",
    learners=[
        UserData(
            user_id="L001",
            user_name="Alice Smith",
            sessions_attended=8,
            total_sessions=8,
            assessments_submitted=3,
            total_assessments=3,
            off_the_job_hours=32,
            target_hours=30,
            flags=[],
        ),
        UserData(
            user_id="L002",
            user_name="Bob Jones",
            sessions_attended=5,
            total_sessions=8,
            assessments_submitted=1,
            total_assessments=3,
            off_the_job_hours=12,
            target_hours=30,
            flags=[
                OverdueFlag(
                    assessment_id=2,
                    overdue_span=6,
                ).message,
                AttendanceFlag(
                    attendance=62
                ).message
            ],
        ),
        UserData(
            user_id="L003",
            user_name="Charlie Brown",
            sessions_attended=7,
            total_sessions=8,
            assessments_submitted=2,
            total_assessments=3,
            off_the_job_hours=26,
            target_hours=30,
            flags=[
                InactiveFlag(
                    inactive_span=7,
                ).message
            ],
        ),
    ],
)