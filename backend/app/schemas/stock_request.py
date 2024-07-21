from typing import List
from pydantic import BaseModel

class StockRequestTrain(BaseModel):
    tickers: List[str]

class StockRequestPredict(BaseModel):
    ticker: str
    end_date: str
