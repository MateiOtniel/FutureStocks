import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ...services.linear_regression_service import train_linear_regression, \
	predict_linear_regression
from ...schemas.stock_request import StockRequestTrain, StockRequestPredict
from ...models.linear_regression.linear_regression_model import LinearRegressionModel
import pickle

router = APIRouter()
logging.basicConfig(level=logging.INFO)
models = {}


@router.post("/train")
async def train(request: StockRequestTrain, db: Session = Depends(get_db)):
	for ticker in request.tickers:
		logging.info(f"Training model for ticker: {ticker}")
		model = train_linear_regression(ticker, db)
		models[ticker] = model
	return {
		"message": f"Linear regression models trained for {', '.join(request.tickers)}"}


@router.post("/predict")
async def predict(request: StockRequestPredict, db: Session = Depends(get_db)):
	ticker = request.ticker
	if ticker not in models:
		# Verifică dacă modelul există în baza de date
		model_record = db.query(LinearRegressionModel).filter(
			LinearRegressionModel.ticker == ticker).first()
		if not model_record:
			raise HTTPException(status_code=404,
			                    detail=f"Model not found for the specified ticker: {ticker}")
		
		# Deserializează modelul
		model = pickle.loads(model_record.model)
		models[ticker] = model
	else:
		model = models[ticker]
	
	predictions = predict_linear_regression(ticker, request.end_date, model, db)
	return {"predictions": predictions}
