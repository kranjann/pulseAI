from pathlib import Path
import json
from app.models.incident import Incident, Severity


class IncidentLoader:
    """
    Responsible only for loading log files.
    """

    def load(self, file_path: Path) -> list[Incident]:

        with file_path.open("r", encoding="utf-8") as file:

            raw_incidents = json.load(file)

            incidents = []

            for raw_incident in raw_incidents:
                incidents.append(Incident(**raw_incident))
        
        return incidents
        

