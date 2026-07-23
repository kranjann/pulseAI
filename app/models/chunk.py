from pydantic import BaseModel, Field


class Chunk(BaseModel):
    """
    Represents one searchable unit in the knowledge base.
    """

    chunk_id: str = Field(..., description="Unique identifier for this chunk")
    incident_id: str = Field(..., description="Source incident identifier")
    text: str = Field(..., description="Text to embed")
    metadata: dict[str, str | list[str]] = Field(
        default_factory=dict,
        description="Additional searchable metadata"
    )