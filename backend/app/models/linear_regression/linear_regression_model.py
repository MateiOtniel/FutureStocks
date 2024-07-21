from sqlalchemy import Column, Integer, String, LargeBinary
from ..base import Base

class LinearRegressionModel(Base):
    __tablename__ = 'linear_regression_models'
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, unique=True)
    model = Column(LargeBinary)
