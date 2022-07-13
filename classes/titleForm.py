from pydantic import BaseModel
from typing import Optional

class titleInputForm(BaseModel):
    code : Optional[str]
    dateValo : Optional[str]
    dateCourbe : Optional[str]