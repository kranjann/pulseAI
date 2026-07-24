from sentence_transformers import SentenceTransformer

from app.embeddings.exceptions import EmbeddingError
from app.models.chunk import Chunk


class EmbeddingService:
    """
    Converts chunk text into semantic embeddings.
    """

    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks: list[Chunk]) -> list[Chunk]:

        if not chunks:
            return  []
        
        try:
            texts = [chunk.text for chunk in chunks]

            embeddings = self.model.encode(texts)

            for chunk, embedding in zip(chunks, embeddings):
                chunk.embedding = embedding.tolist()

            return chunks

        except Exception as exc:
            raise EmbeddingError(
                "Failed to generate embeddings."
            ) from exc