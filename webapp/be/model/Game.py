from typing import Annotated

# from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, SQLModel
from datetime import date

class Game(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    developers: str = Field(index=True)
    publishers: str = Field(index=True)
    is_released: bool = Field(index=True)
    release_date: date | date.year = Field(index=True)
    total_reviews: int = Field(index=True)
    total_positive: int = Field(index=True)
    total_negative: int = Field(index=True)
    review_score: float = Field(index=True)
    positive_percentual: float = Field(index=True)
    metacritic: int
    is_free: bool = Field(index=True)
    price_initial: float = Field(index=True)