import json
from google import genai
from data_schemas import CompanyExtraction, CohortData

from prompt import PROMPT


def generate_cohort_report(api_key: str, data: CohortData) -> dict:
    """
    Create cohort report based on learner data
    :param api_key: Please provide a Google Gemini API key
    :param data: Cohort data
    :return:
    """
    print("Connecting to Google Gemini...")
    client = genai.Client(api_key=api_key)

    print("Sending cohort data...")
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=PROMPT + data.model_dump_json(),
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": CompanyExtraction.model_json_schema()
        },
    )
    print("Creating Progress Summary...")
    return json.loads(response.output_text)


def select_emoji(severity):
    """
    Slack emoji selection
    :param severity: Severity of learner issue(s)
    :return:
    """
    if severity == "HIGH":
        return "🔴"
    elif severity == "MEDIUM":
        return "🟡"
    return "🟢"


def construct_line_item(item):
    """
    Create line item for Slack notifications
    :param item: Raw data
    :return:
    """
    emoji = select_emoji(item.get("severity"))
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                f"{emoji} *{item['learner_name']}* ({item['severity']} Risk)\n"
                f"*Issue:* {item['reason']}\n"
                f"*Suggested Action:* {item['recommended_action']}"
            ),
        },
    }


def format_slack_alert_payload(
        cohort_name: str,
        employer_name: str,
        escalations: list
) -> dict:
    """
    Formats internal escalation data into a Slack Block Kit JSON payload.
    :return:
    """
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Cohort Escalation Alert: {employer_name}",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Cohort:* {cohort_name}\n*Action Required:* The following learners require delivery team intervention.",
            },
        },
        {"type": "divider"},
    ]

    for item in escalations:
        blocks.append(construct_line_item(item))
    return {"blocks": blocks}
