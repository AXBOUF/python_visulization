# Munal Baraili - Projects & Experience Portfolio

**Student ID:** 900006725  
**Portfolio:** A collection of data science and machine learning projects demonstrating skills in big data processing, machine learning, data analysis, and visualization.

---

## Work Experience

### Assistant Manager – Operations & Data Insights
**Hungry Jack's** | Fast-Food Retail Operations

**Operational Data Analysis:**
- Analysed operational metrics including sales trends, labour utilisation, inventory movement, and food waste reports to identify patterns and support informed decision-making within the management team
- Compiled reports and visual charts to track performance and highlight opportunities for waste reduction
- Experimented with spreadsheet automation to streamline waste reporting and make operational insights easier to interpret for the team

**Inventory & Cost Management:**
- Managed food inventory counts and monitored waste thresholds
- Tracked inventory movement and identified patterns to optimize ordering and reduce waste
- Supported cost control initiatives through data-driven insights

**Labour & Team Management:**
- Assisted with staff rostering based on expected demand and operational needs
- Supported crew recruitment and training to maintain service and operational standards
- Contributed to maintaining high team performance in a high-volume fast-food environment

**Process Improvement:**
- Provided input on ordering terminal layout and menu item naming to reduce order-entry conflicts
- Improved transaction efficiency during new product launches through practical operational recommendations

---

## Project 1: NYC Taxi Trip Duration Prediction

**Technologies:** PySpark, Python, Matplotlib, Seaborn

**Description:**
Built a predictive model to estimate taxi trip duration in New York City using PySpark. The project analyzed over 729,322 taxi trip records containing pickup/dropoff locations, timestamps, passenger counts, and vendor information. Identified and handled outliers (trips ranging from 1 second to 538 hours) and performed comprehensive exploratory data analysis to understand trip patterns.

**Key Techniques:**
- PySpark DataFrame operations and schema inference
- Data cleaning and outlier detection
- Feature engineering from datetime columns
- Exploratory data analysis with visualization
- Statistical analysis of trip duration distributions
- Vendor and passenger count distribution analysis

**Data Features:** id, vendor_id, pickup_datetime, dropoff_datetime, passenger_count, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, store_and_fwd_flag, trip_duration

**Outcome:** Developed a regression model to predict trip duration based on pickup/dropoff locations, time of day, passenger count, and vendor information.

---

## Project 2: Big Data Integration - MongoDB & PySpark

**Technologies:** MongoDB, PySpark, Python, JSON

**Description:**
Designed and implemented a NoSQL database system for workout tracking data (FitRec database). Created a database schema separating high-level workout metadata from granular time-series trackpoint data to improve query efficiency. Integrated MongoDB with PySpark for distributed data processing of workout data including GPS coordinates, altitude, heart rate readings, and sport type information.

**Key Techniques:**
- MongoDB database design and implementation
- Schema design for time-series and metadata separation
- JSON data parsing and processing
- PySpark integration with MongoDB
- Data population and query optimization
- Collection management in MongoDB

**Data Structure:**
- Workout metadata: sport, gender, userId, id
- Time-series data: longitude, latitude, altitude, heart_rate, timestamp (500 data points per workout)
- Workout types: cycling, running, mountain bike, walking, hiking, cross-country skiing, orienteering

**Outcome:** Created a scalable big data pipeline for fitness tracking data with efficient lookup and indexing capabilities.

---

## Project 3: Human Activity Recognition (HAR)

**Technologies:** Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Random Forest, MLP

**Description:**
Comprehensive human activity recognition project using accelerometer and gyroscope sensor data from mobile devices. The project covers the complete machine learning pipeline from data inspection to model evaluation. Activities include cycling, running, mountain biking, walking, hiking, and indoor cycling. Each workout session contains 50,000-170,000+ sensor readings.

**Key Techniques:**
- Sensor fusion (accelerometer + gyroscope data)
- Time-domain feature extraction
- Frequency-domain feature extraction
- Unsupervised clustering analysis
- Supervised classification (Random Forest, MLP)
- Data visualization and exploratory analysis
- Leak-free validation methodology
- Cross-validation for generalization

**Data Features:** accelerometer (x, y, z), gyroscope (x, y, z), timestamp, seconds_elapsed

**Outcome:** Built classification models to recognize human activities from raw sensor data with emphasis on proper validation and generalization.

---

## Project 4: Credit Card Customer Segmentation

**Technologies:** PySpark, K-Means Clustering, VectorAssembler

**Description:**
Customer segmentation project using K-Means clustering on credit card customer data. Processed customer credit card features including balance, purchase history, payment patterns, and credit limits. Used PySpark's ML library for scalable clustering analysis.

**Key Techniques:**
- PySpark ML pipeline construction
- Feature vector assembly using VectorAssembler
- K-Means clustering algorithm
- Data preprocessing and normalization
- Customer behavior analysis
- Purchase pattern clustering

**Data Features:** CUST_ID, BALANCE, BALANCE_FREQUENCY, PURCHASES, ONEOFF_PURCHASES, INSTALLMENTS_PURCHASES, CASH_ADVANCE, PURCHASES_FREQUENCY, ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, CASH_ADVANCE_FREQUENCY, CASH_ADVANCE_TRX, PURCHASES_TRX, CREDIT_LIMIT, PAYMENTS, MINIMUM_PAYMENTS, PRC_FULL_PAYMENT, TENURE

**Outcome:** Identified distinct customer segments based on credit card usage patterns for targeted marketing strategies.

---

## Project 5: Credit Card Fraud Detection

**Technologies:** Python, Scikit-learn, Isolation Forest, Local Outlier Factor, One-Class SVM, Pandas, Plotly

**Description:**
Fraud detection system for credit card transactions using unsupervised machine learning techniques. Analyzed 284,807 credit card transactions with 28 anonymized features (V1-V28) and transaction amount. Addressed highly imbalanced dataset (only 0.17% fraud cases).

**Key Techniques:**
- Isolation Forest anomaly detection
- Local Outlier Factor (LOF) for outlier detection
- One-Class SVM classification
- Handling imbalanced datasets
- Feature correlation analysis
- Interactive visualization with Plotly
- Performance evaluation metrics

**Data Features:** Time, V1-V28 (anonymized features), Amount, Class (fraud/normal)

**Outcome:** Developed models to detect fraudulent transactions while minimizing false positives, achieving high accuracy in identifying anomalies.

---

## Project 6: Artist Recommender System

**Technologies:** PySpark, ALS (Alternating Least Squares), Collaborative Filtering

**Description:**
Built a collaborative filtering recommender system for artist recommendations using PySpark's MLlib. Processed user-artist interaction data including play counts to predict user preferences. Handled artist alias mapping for data consistency.

**Key Techniques:**
- ALS (Alternating Least Squares) algorithm
- Collaborative filtering
- Implicit feedback recommendation
- Data schema definition and parsing
- Train/test data splitting (80/20)
- User-item rating prediction
- Cold start strategy implementation

**Data Files:** artist_data.txt, user_artist_data.txt, artist_alias.txt

**Outcome:** Created a recommendation engine to suggest artists to users based on their listening history and similar user preferences.

---

## Project 7: Boston Housing Price Prediction

**Technologies:** PySpark, Linear Regression, SparkSQL

**Description:**
Predictive modeling project for Boston housing prices using linear regression. Used PySpark to process the classic Boston housing dataset with features like crime rate, room count, property tax, and proximity to employment centers.

**Key Techniques:**
- PySpark SQL operations
- Linear regression modeling
- Feature selection and preprocessing
- Data loading from CSV
- Schema inference
- Model training and evaluation

**Data Features:** crim (crime rate), zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, black, lstat, medv (median value - target)

**Outcome:** Developed a regression model to predict median house values based on various neighborhood characteristics.

---

## Project 8: Network Anomaly Detection

**Technologies:** Python, K-Means Clustering, Matplotlib, Seaborn

**Description:**
Network intrusion detection project using K-Means clustering on network traffic data. Classified network connections as normal or attacks based on 41 features including duration, protocol type, service, byte counts, and various network statistics.

**Key Techniques:**
- K-Means clustering for anomaly detection
- Network traffic analysis
- Feature engineering from network logs
- Protocol type analysis
- Attack classification
- Data visualization

**Data Features:** duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment, urgent, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root, num_file_creations, num_shells, num_access_files, count, srv_count, serror_rate, rerror_rate, and more

**Outcome:** Identified network anomalies and potential intrusions using unsupervised clustering techniques.

---

## Project 9: IoT Telemetry Data Analysis

**Technologies:** Python, Pandas, Matplotlib, Seaborn

**Description:**
Analysis of IoT sensor telemetry data from multiple devices. Examined temperature, humidity, CO levels, LPG, smoke, light, and motion sensors across different device IDs to understand environmental patterns.

**Key Techniques:**
- Multi-device sensor data comparison
- Correlation analysis between sensors
- Time-series data visualization
- Environmental pattern detection
- Feature aggregation by device

**Data Features:** ts (timestamp), device (device ID), co, humidity, light, lpg, motion, smoke, temp

**Outcome:** Analyzed IoT sensor data to determine temperature and humidity levels for potential suburb monitoring applications.

---

## Project 10: Foreign Exchange Rate Analysis

**Technologies:** Python, Pandas, Matplotlib, Seaborn, Time Series Analysis

**Description:**
Time series analysis of foreign exchange rates across multiple currencies including USD, AUD, EUR, GBP, CAD, CNY, and CHF. Analyzed exchange rate trends over time from 2000 onwards.

**Key Techniques:**
- Time series data processing
- Currency correlation analysis
- Trend visualization (line plots)
- Yearly average rate calculation
- Multi-currency comparison
- Historical trend analysis

**Currencies Analyzed:** Australia (AUD), Euro Area (EUR), United Kingdom (GBP), Canada (CAD), China (CNY), Switzerland (CHF)

**Outcome:** Identified patterns and correlations between different currency exchange rates over multiple years.

---

## Project 11: Market Basket Analysis (Apriori)

**Technologies:** Python, Apriori Algorithm, Association Rules, Squarify, Seaborn

**Description:**
Market basket analysis using the Apriori algorithm to discover association rules in transaction data. Identified frequently co-occurring items to understand purchasing patterns.

**Key Techniques:**
- Apriori algorithm implementation
- Frequent itemset mining
- Association rule generation
- Support and confidence metrics
- Data visualization (treemaps)
- Market pattern discovery

**Outcome:** Discovered association rules revealing customer purchasing behavior and product relationships.

---

## Project 12: Data Analyst Exploratory Analysis

**Technologies:** Python, Pandas, Matplotlib

**Description:**
Exploratory data analysis on job posting data to analyze company distributions, salary estimates, company sizes, and founding years. Created various visualizations to understand job market trends.

**Key Techniques:**
- Data cleaning and preprocessing
- Company distribution analysis (by city/state)
- Year founded analysis with histogram plots
- Salary analysis by job title
- Company size vs. salary analysis
- Data visualization

**Data Features:** Salary Estimate, Company Name, Location, Size, Founded

**Outcome:** Generated insights about job market trends, salary distributions, and company characteristics.

---

## Project 13: Smile Earn - Face Recognition Loyalty System

**Technologies:** Python, Flask, OpenCV, face_recognition library, HTML/CSS, JSON

**Description:**
Full-stack face recognition application that replaces traditional loyalty cards with facial recognition. When customers scan their face at checkout, the system identifies them and automatically awards loyalty points. Built as a proof-of-concept for retail automation and customer identification.

**Key Techniques:**
- Face detection using dlib/face_recognition library
- Face encoding generation (128-dimensional face embeddings)
- Real-time face recognition from webcam
- Flask REST API development
- Image processing with OpenCV
- User registration with face capture
- Model training pipeline for face encodings
- Loyalty points system integration
- POS (Point of Sale) integration
- JSON-based user database

**System Architecture:**
- Backend: Flask server running on port 5002
- Face Recognition: dlib-based encoding and matching
- Training: Batch processing of face images to generate encodings.pickle
- Frontend: HTML/CSS templates for user registration and shopping
- Database: JSON file storage for user profiles and loyalty points

**API Endpoints:**
- `POST /capture` - Capture frame from camera and identify user
- `POST /upload` - Register new user with face image
- `GET/POST /train` - Retrain face recognition model
- `POST /shopping` - Process purchase and award points

**How It Works:**
1. Users register by uploading face images via `/upload` endpoint
2. System stores images in `data/dataset/{username}/` folder
3. Admin triggers `/train` to generate `encodings.pickle` with face embeddings
4. At checkout, camera captures face via `/capture` endpoint
5. System compares against stored encodings using face_distance
6. User identified → loyalty points from `db.json` awarded automatically

**Outcome:** Created a working face recognition loyalty system demonstrating computer vision skills, full-stack development, and integration of ML models with web applications.

---

## Technical Skills Summary

### Programming Languages
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- PySpark
- SQL

### Big Data & Database
- PySpark (DataFrames, ML, SQL)
- MongoDB
- Database Design

### Machine Learning
- Supervised Learning: Linear Regression, Random Forest, MLP
- Unsupervised Learning: K-Means Clustering, DBSCAN
- Anomaly Detection: Isolation Forest, Local Outlier Factor, One-Class SVM
- Recommendation Systems: Collaborative Filtering (ALS)
- Computer Vision: Face Detection, Face Recognition, Face Embeddings

### Data Analysis
- Exploratory Data Analysis (EDA)
- Time Series Analysis
- Feature Engineering
- Data Visualization

### Tools & Libraries
- Pandas, NumPy, Matplotlib, Seaborn, Plotly
- Scikit-learn, PySpark ML
- MongoDB (PyMongo)
- Jupyter/Colab
- Flask, OpenCV, face_recognition

---

## Academic Context

These projects were completed as part of a data science and big data analytics program, demonstrating proficiency in:
- Data processing and analysis at scale
- Machine learning model development
- Database design and integration
- Data visualization and storytelling
- Big data technologies (Spark, MongoDB)
