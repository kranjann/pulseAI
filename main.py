from pathlib import Path

from app.chunking.chunking_service import ChunkingService
from app.loaders.incident_loader import IncidentLoader


def main():
    # Load incidents from the knowledge base
    loader = IncidentLoader()
    incidents = loader.load(Path("app/knowledge_base/incidents.json"))

    print(f"Loaded {len(incidents)} incidents\n")

    # Convert incidents to chunks
    chunking_service = ChunkingService()
    chunks = chunking_service.create_chunks(incidents)

    print(f"Created {len(chunks)} chunks\n")

    # Print each chunk
    for chunk in chunks:
        print("=" * 80)
        print(f"Chunk ID    : {chunk.chunk_id}")
        print(f"Incident ID : {chunk.incident_id}")
        print("Metadata    :", chunk.metadata)
        print("\nText:")
        print(chunk.text)
        print()


if __name__ == "__main__":
    main()