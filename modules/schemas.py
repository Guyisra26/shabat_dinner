from pydantic import BaseModel, Field

class RSVP(BaseModel):
    family: str = Field(..., min_length=1)
    num_people: int = Field(..., ge=0)
