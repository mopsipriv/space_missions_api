from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class Agency(str, Enum):
    NASA = "NASA"
    ESA = "ESA"
    ROSCOSMOS = "ROSCOSMOS"
    JAXA = "JAXA"
    SPACEX = "SPACEX"
    CNSA = "CNSA"

class Status(str, Enum):
    PLANNED = "PLANNED"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class MissionBase(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
        description="Mission name"
    )
    agency: Agency = Field(
        ...,
        description= "Space Agency"
    )
    launch_year: int = Field(
        ge=1957,
        le=2030,
        description= "Launch year (1957 = Sputnik 1)"
    )
    target: str = Field(
        min_length=1,
        max_length=50,
        description="Where is it flying (Mars, Moon, ISS...)"
    )
    status: Status = Field(
        ...,
        description="Mission status"
    )
    crewed: bool = Field(
        ...,
        description="With the crew"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Mission Description"
    )

class MissionCreate(MissionBase):
    """
    Model for creating a mission.
    Inherits all fields from MissionBase.
    No additional fields.
    """
    pass

class MissionUpdate(BaseModel):
    name: Optional[str] = Field(
        min_length=1,
        max_length=100,
        default=None
    )
    agency: Optional[Agency] = Field(
        default=None
    )
    launch_year: Optional[int] = Field(
        ge=1957,
        le=2030,
        default=None
    )
    target: Optional[str] = Field(
        default=None
    )
    status: Optional[Status] = Field(
        default=None
    )
    crewed: Optional[bool] = Field(
        default=None
    )
    description: Optional[str] = Field(
        default=None
    )

class Mission(MissionBase):
    id: int = Field(
        description="Unique mission identifier"
    )

class Stats(BaseModel):
    total: int = Field(
        description="Total number of missions"
    )
    by_agency: dict[str, int] = Field(
        description="How many missions does each agency have"
    )
    by_status: dict[str, int] = Field(
        description="How many missions with each status"
    )
    crewed_count: int = Field(
        description="How many crewed missions"
    )