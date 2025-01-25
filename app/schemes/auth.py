from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(
        examples=['JzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'],
    )
