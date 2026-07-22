from pathlib import Path

from app.loaders.incident_loader import IncidentLoader


def main():
    loader = IncidentLoader()

    incidents = loader.load(
        Path("app/knowledge_base/incidents.json")
    )

    print(f"Loaded {len(incidents)} incidents\n")

    for incident in incidents:
        print("=" * 60)
        print(f"ID         : {incident.id}")
        print(f"Title      : {incident.title}")
        print(f"Component  : {incident.component}")
        print(f"Severity   : {incident.severity}")
        print(f"Tags       : {', '.join(incident.tags)}")
        print(f"Root Cause : {incident.root_cause}")
        print(f"Resolution : {incident.resolution}")


if __name__ == "__main__":
    main()