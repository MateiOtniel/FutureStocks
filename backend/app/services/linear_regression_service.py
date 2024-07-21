import datetime
import logging
import os
import pickle
from fastapi import HTTPException

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from sklearn.linear_model import LinearRegression
from sqlalchemy.orm import Session

from app.models.linear_regression.linear_regression_prediction import \
	LinearRegressionPrediction
from ..models.linear_regression.linear_regression_model import LinearRegressionModel
from ..models.stock_data import StockData

logging.basicConfig(level=logging.INFO)


def train_linear_regression(ticker: str, db: Session):
	try:
		# Verifică dacă modelul există deja în baza de date
		logging.info(f"Checking if model for {ticker} exists in the database")
		existing_model_record = db.query(LinearRegressionModel).filter(
			LinearRegressionModel.ticker == ticker).first()
		if existing_model_record:
			# Dacă modelul există, deserializează și returnează-l
			logging.info(f"Model for {ticker} found in database. Loading model.")
			model = pickle.loads(existing_model_record.model)
			return model
		
		# Încarcă datele existente din baza de date
		logging.info(f"Checking if data for {ticker} exists in the database")
		existing_data = db.query(StockData).filter(StockData.ticker == ticker).all()
		if existing_data:
			logging.info(f"Data for {ticker} found in database.")
			data = pd.DataFrame([(d.date, d.open, d.high, d.low, d.close, d.volume)
			                     for d in existing_data], columns=['date', '1. open',
			                                                       '2. high', '3. low',
			                                                       '4. close',
			                                                       '5. volume'])
		else:
			# Dacă nu există date, le descarcă de la Alpha Vantage
			logging.info(
				f"Data for {ticker} not found in database. Downloading from Alpha Vantage.")
			ts = TimeSeries(key=os.getenv("ALPHA_VANTAGE_KEY"), output_format='pandas')
			data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')
			data.reset_index(inplace=True)
			data['date'] = pd.to_datetime(data['date'])
			
			# Salvează datele în baza de date
			for _, row in data.iterrows():
				stock_data = StockData(
					ticker=ticker,
					date=row['date'],
					open=row['1. open'],
					high=row['2. high'],
					low=row['3. low'],
					close=row['4. close'],
					volume=row['5. volume']
				)
				db.add(stock_data)
			db.commit()
		
		data['timestamp'] = data['date'].map(pd.Timestamp.timestamp)
		X = data[['timestamp']].values
		y = data['4. close'].values
		
		# Antrenează modelul
		logging.info(f"Training model for {ticker}")
		model = LinearRegression().fit(X, y)
		
		# Serializează și salvează modelul în baza de date
		logging.info(f"Saving model for {ticker} to database")
		model_binary = pickle.dumps(model)
		model_record = LinearRegressionModel(ticker=ticker, model=model_binary)
		db.add(model_record)
		db.commit()
		
		return model
	except Exception as e:
		logging.error(f"Error training model for {ticker}: {e}")
		raise HTTPException(status_code=500, detail="Internal Server Error")


def predict_linear_regression(ticker: str, end_date: str, model, db: Session):
	future_dates = pd.date_range(start=end_date, periods=30).map(
		pd.Timestamp.timestamp).values.reshape(-1, 1)
	predictions = model.predict(future_dates)
	
	for i, prediction in enumerate(predictions):
		prediction_date = datetime.datetime.fromtimestamp(future_dates[i][0])
		pred = LinearRegressionPrediction(
			ticker=ticker,
			prediction_date=prediction_date,
			predicted_close=prediction
		)
		db.add(pred)
	db.commit()
	
	return predictions.tolist()
