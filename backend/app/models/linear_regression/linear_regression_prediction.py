from sqlalchemy import Column, Integer, String, Float, DateTime
from ..base import Base

class LinearRegressionPrediction(Base):
    __tablename__ = 'linear_regression_predictions'
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    prediction_date = Column(DateTime, index=True)
    predicted_close = Column(Float)