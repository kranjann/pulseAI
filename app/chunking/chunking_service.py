from app.chunking.chunk_formatter import ChunkFormatter
from app.models.chunk import Chunk
from app.models.incident import Incident

class ChunkingService:
    """
    Converts Incident objects into searchable Chunk objects.
    """

    def __init__(self):
        self.formatter = ChunkFormatter()

    def create_chunks(self, incidents: list[Incident]) -> list[Chunk]:
        chunks: list[Chunk] = []

        for incident in incidents:
            text = self.formatter.format(incident)

            metadata = {
                "component": incident.component,
                "severity": incident.severity.value,
                "tags": incident.tags,
            }

            chunk = Chunk(
                chunk_id=incident.id,
                incident_id=incident.id,
                text=text,
                metadata=metadata,
            )

            chunks.append(chunk)

        return chunks
            