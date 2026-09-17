import json

from mock_data import MOCK_COHORT_DATA
from generate_reports import generate_cohort_report, format_slack_alert_payload

if __name__ == "__main__":
    print("Enter your Google Gemini API key:")
    api_key = input()
    try:
        ai_output = generate_cohort_report(
            api_key=api_key,
            data=MOCK_COHORT_DATA,
        )

        print("==================================================")
        print("ACCOUNT MANAGER EMPLOYER SUMMARY (EMAIL)")
        print("==================================================")
        print(ai_output.get("employer_summary"))

        slack_payload = format_slack_alert_payload(
            cohort_name=MOCK_COHORT_DATA.get("cohort_name"),
            employer_name=MOCK_COHORT_DATA.get("employer_name"),
            escalations=ai_output.get("escalation_items", []),
        )

        print("\n==================================================")
        print("INTERNAL SLACK ALERT PAYLOAD (JSON)")
        print("==================================================")
        print(json.dumps(slack_payload, indent=2))

    except Exception as e:
        print(f"Error generating report: {e}")
