from app.models.incident import Incident


class ChunkFormatter:
    """
    Formats an Incident into text suitable for semantic embedding.
    """

    def format(self, incident: Incident) -> str:
        return f"""
Title:
{incident.title}

Test Name:
{incident.test_name}

Assertion:
{incident.assertion}

Failure Summary:
{incident.failure_summary}

Root Cause:
{incident.root_cause}

Resolution:
{incident.resolution}
""".strip()