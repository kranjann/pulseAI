from pathlib import Path

from app.chunking.chunking_service import ChunkingService
from app.embeddings.embedding_service import EmbeddingService
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

    # Generate embeddings
    embedding_service = EmbeddingService("all-MiniLM-L6-v2")
    embedded_chunks = embedding_service.embed_chunks(chunks)

    # Print each embedded chunk
    for chunk in embedded_chunks:
        print("=" * 80)
        print(f"Chunk ID    : {chunk.chunk_id}")
        print(f"Incident ID : {chunk.incident_id}")
        print("Metadata    :", chunk.metadata)

        print("\nText:")
        print(chunk.text)

        print("\nEmbedding")
        print(f"Dimensions  : {len(chunk.embedding)}")
        print(f"First 10 values : {chunk.embedding[:10]}")
        print()


if __name__ == "__main__":
    main()