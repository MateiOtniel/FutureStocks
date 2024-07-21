# FutureStocks

## Proiect de Predicție a Prețului Acțiunilor folosind Inteligența Artificială

Acest proiect are ca scop prezicerea prețului unei acțiuni pe baza istoricului său utilizând inteligența artificială. Pașii de mai jos oferă o structură pentru proiect, de la colectarea datelor până la evaluarea modelului de predicție.

### Pasul 1: Definirea Problemei
1. **Stabilirea Obiectivelor**:
   - Predicția prețului unei acțiuni pentru o anumită perioadă în viitor (de ex. o zi, o săptămână).
   - Alegerea unei acțiuni specifice sau a unui set de acțiuni pentru analiză.

### Pasul 2: Colectarea și Preprocesarea Datelor
1. **Colectarea Datelor**:
   - Obținerea datelor istorice ale prețurilor acțiunilor (open, high, low, close) și volumul de tranzacționare utilizând API-uri financiare precum Yahoo Finance, Alpha Vantage sau alte surse.
   - Colectarea datelor suplimentare: indicatori tehnici, știri financiare, factori macroeconomici (opțional).

2. **Preprocesarea Datelor**:
   - Curățarea datelor: gestionarea valorilor lipsă, corectarea anomaliilor.
   - Normalizarea/standardizarea datelor pentru îmbunătățirea performanței modelului.

### Pasul 3: Explorarea și Vizualizarea Datelor
1. **Analiza Exploratorie a Datelor (EDA)**:
   - Utilizarea grafice pentru vizualizarea datelor istorice ale prețurilor (grafice de tip linie, histogramă, etc.).
   - Calcularea și vizualizarea indicatorilor tehnici (de ex. media mobilă, RSI, MACD).

### Pasul 4: Dezvoltarea Modelului de Predicție
1. **Alegerea și Construirea Modelului**:
   - **Modele de Machine Learning**: Regresie liniară, ARIMA, modele de regresie complexă.
   - **Modele de Deep Learning**: RNN (Recurrent Neural Networks), LSTM (Long Short-Term Memory), GRU (Gated Recurrent Units).
   - Utilizarea librăriilor precum Scikit-Learn, TensorFlow, Keras, PyTorch.

2. **Antrenarea Modelului**:
   - Separarea datelor în seturi de antrenament și de testare.
   - Antrenarea modelului pe datele de antrenament.
   - Ajustarea hiperparametrilor pentru optimizarea performanței.

### Pasul 5: Evaluarea și Îmbunătățirea Modelului
1. **Evaluarea Performanței**:
   - Utilizarea metricilor de evaluare precum MSE (Mean Squared Error), RMSE (Root Mean Squared Error), MAE (Mean Absolute Error).
   - Vizualizarea predicțiilor comparativ cu datele reale.

2. **Îmbunătățirea Modelului**:
   - Ajustarea parametrilor, adăugarea de noi funcții sau utilizarea unor modele mai avansate pentru îmbunătățirea modelului.

### Pasul 6: Implementarea și Integrarea Modelului
1. **Implementarea Modelului**:
   - Salvarea modelului antrenat.
   - Crearea unui API (de ex. folosind Flask sau FastAPI) pentru a permite utilizarea modelului în timp real.

2. **Integrarea Modelului în Aplicație**:
   - Integrarea modelului de predicție în aplicația personală (de ex. HealthSync) pentru a oferi utilizatorilor predicții de preț.

### Pasul 7: Monitorizarea și Mentenanța Modelului
1. **Monitorizarea Performanței**:
   - Monitorizarea continuă a performanței modelului în producție.
   - Actualizarea periodică a modelului cu date noi pentru menținerea acurateței predicțiilor.

### Pasul 8: Documentarea Proiectului
1. **Documentarea Procesului**:
   - Documentarea fiecărui pas al proiectului, de la colectarea datelor până la implementarea și evaluarea modelului.
   - Scrierea unui raport final care să includă metodologia, rezultatele și concluziile.

### Resurse Suplimentare:
- Tutoriale și documentații oficiale ale librăriilor de machine learning și deep learning.
- Cursuri online despre predicția prețurilor acțiunilor și analiza seriilor temporale.

Acesta este un ghid general, iar detaliile fiecărui pas pot varia în funcție de specificul proiectului și de datele utilizate. 

## Tehnologii Folosite

### Back-End

1. **Limbaj de Programare**:
   - **Python**: Cel mai utilizat datorită librăriilor sale puternice pentru machine learning și data science.

2. **Librării și Framework-uri pentru Machine Learning/Deep Learning**:
   - **Scikit-Learn**: Pentru modele de machine learning mai simple.
   - **TensorFlow/Keras** sau **PyTorch**: Pentru rețele neuronale și modele mai complexe, cum ar fi RNN sau LSTM.

3. **Framework-uri pentru API-uri**:
   - **Flask**: Un micro-framework simplu și flexibil pentru crearea API-urilor RESTful.
   - **FastAPI**: O alternativă modernă, foarte rapidă și prietenoasă pentru crearea de API-uri, cu suport pentru asincronizare.

4. **Baze de Date**:
   - **PostgreSQL**: Pentru stocarea datelor istorice și a predicțiilor.
   - **SQLite**: O alternativă mai ușoară pentru proiectele mici sau în faza de prototip.

5. **Colectarea Datelor**:
   - **yfinance**: O librărie Python pentru obținerea datelor financiare de pe Yahoo Finance.
   - **Alpha Vantage API**: Oferă date de piață în timp real și istorice.

### Front-End

1. **Framework-uri și Librării JavaScript**:
   - **React**: Foarte popular pentru construirea interfețelor utilizator moderne și dinamice.
   - **Vue.js**: O alternativă prietenoasă și flexibilă pentru dezvoltarea de interfețe utilizator.

2. **Librării pentru Vizualizarea Datelor**:
   - **Chart.js**: Pentru grafice simple și ușor de integrat.
   - **D3.js**: Pentru vizualizări complexe și interactive.
   - **Recharts**: O librărie de vizualizare bazată pe React, foarte ușor de folosit.

3. **Framework-uri CSS pentru Stilizare**:
   - **Bootstrap**: Un framework CSS popular care ajută la crearea rapidă de interfețe responsive și atractive.
   - **Material-UI**: Componente UI pentru React care urmează principiile Material Design de la Google.

### Integrarea Back-End cu Front-End

1. **Crearea API-urilor**:
   - API-urile RESTful sunt create folosind Flask sau FastAPI pentru a expune datele și predicțiile către front-end.

2. **Comunicarea între Front-End și Back-End**:
   - **Axios** sau **Fetch API**: Pentru realizarea cererilor HTTP către API-uri din front-end.

### Exemplu de Arhitectură

1. **Server Back-End**:
   - Python cu Flask/FastAPI pentru API-uri.
   - Modelul de predicție este salvat folosind librăria corespunzătoare (pickle pentru Scikit-Learn sau TensorFlow Model Saving pentru TensorFlow).

2. **Front-End**:
   - React pentru interfața utilizator.
   - Chart.js pentru vizualizarea predicțiilor și a datelor istorice.

### Pas cu Pas

1. **Setare Mediu de Dezvoltare**:
   - Instalează Python, pip, și un IDE (de ex. PyCharm, VS Code).
   - Instalează Node.js și npm pentru dezvoltarea front-end.

2. **Back-End**:
   - Creează un API cu Flask/FastAPI care să furnizeze date istorice și predicții.
   - Scrie scripturi pentru colectarea și preprocesarea datelor.
   - Antrenează un model de predicție și salvează-l.

3. **Front-End**:
   - Creează un proiect React.
   - Conectează front-end-ul cu API-urile back-end folosind Axios/Fetch.
   - Construiește componente pentru afișarea graficelor cu datele istorice și predicțiile folosind Chart.js/Recharts.

4. **Integrarea și Testarea**:
   - Asigură comunicarea corectă între front-end și back-end și afișarea corectă a datelor.
   - Testează aplicația cu date reale și verifică acuratețea predicțiilor.

5. **Deploy**:
   - Back-end: Găzduit pe un serviciu cloud (de ex. Heroku, AWS).
   - Front-end: Găzduit pe un serviciu de hosting static

 (de ex. Netlify, Vercel).
