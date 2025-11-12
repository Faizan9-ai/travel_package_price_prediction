# Travel Triangle Tour Package Price Prediction
## Project Overview

#### The Travel Triangle Price Prediction App is a complete end-to-end machine learning project that predicts the price of India tour packages based on features such as destination, duration, travel type, hotel rating, number of travelers, and more.

#### The project covers data collection, cleaning, EDA, feature engineering, model training, evaluation, and deployment on Streamlit Cloud, providing a clean, interactive web interface for real-time predictions.

## Project Workflow
### 1. Web Scraping (Data Collection)

##### Source: TravelTriangle.com

##### Tool Used: BeautifulSoup, requests,Selenium, Chromedriver

##### Goal: Extract India tour packages including:

1. Package name

2.Destination

3.Duration

4.Hotel type

5.No of Days and Nights

6.Total price

The scraped data was saved into a structured CSV file for analysis.

### 2. Data Cleaning & Preprocessing

##### Performed using Pandas and NumPy:

##### Removed duplicates and missing values (NaN).

##### Converted categorical variables into consistent formats.

##### Cleaned numerical columns (extracted numbers from text using regex).

##### Converted duration and cost into numerical form.

##### Encoded categorical columns for ML model compatibility.

### 3.  Exploratory Data Analysis (EDA)

##### Used Matplotlib and Seaborn to visualize:

##### Most popular destinations and tour durations.

##### Correlation between hotel rating, travelers, and package price.

##### Distribution of prices for different travel types.

##### Outlier detection and price range insights.

### 4️. Feature Engineering

##### Created meaningful features to enhance model accuracy:

##### Extracted numeric duration from text like “5 Nights / 6 Days”.

##### Derived average cost per traveler.

##### Encoded categorical variables using OneHotEncoder and ColumnTransformer.

##### Scaled numerical features using StandardScaler.

### 5. Model Building & Training

##### Trained multiple machine learning algorithms:

##### Linear Regression

##### Random Forest Regressor

##### Gradient Boosting Regressor

##### XGBoost Regressor

Each model was trained and compared using cross-validation.
