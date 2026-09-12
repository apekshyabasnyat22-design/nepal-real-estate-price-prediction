# Nepal Real Estate Price Prediction and Property Analysis

## Project Overview

**Nepal Real Estate Price Prediction and Property Analysis** is a machine-learning-based web application developed to help users understand and evaluate real-estate properties in Nepal.

The project combines **data analysis, machine learning, PostgreSQL, and Django** to create a platform where users can browse property listings, search and filter properties, view detailed property information, explore locations on an interactive map, and estimate property prices using a trained machine-learning model.

The main purpose of the project is to make property information more organized and support more informed real-estate decisions. Property prices in Nepal can vary greatly depending on location, land area, road access, number of bedrooms and bathrooms, building characteristics, and other property-related factors. Because property information is often scattered and prices may be inconsistent, buyers and sellers may find it difficult to determine whether a property is reasonably priced.

This application uses historical real-estate data and machine-learning techniques to provide estimated property prices and additional insights that can help users compare properties.

## Problem Statement

The real-estate market in Nepal faces several challenges:

* Property prices are often unclear or inconsistent.
* Buyers may pay more than the estimated market value of a property.
* Sellers may undervalue their properties.
* Property information is scattered across different sources.
* Comparing properties based on location, area, price, and facilities can be difficult.
* Users may not have access to data-driven price estimates.
* It can be difficult to identify properties that may be priced below their estimated value.

These challenges can lead to poor purchasing, selling, and investment decisions.

This project addresses these problems by organizing property data into a web application and using machine learning to estimate property prices based on property characteristics.

## Project Objectives

The main objectives of this project are:

1. To develop a machine-learning model for estimating real-estate property prices in Nepal.
2. To analyze property data and identify important factors related to property prices.
3. To store and manage property information using PostgreSQL.
4. To develop a web application using Django.
5. To allow users to browse available property listings.
6. To provide property search and filtering features.
7. To display detailed information about individual properties.
8. To show property locations using interactive maps.
9. To compare listed property prices with machine-learning-based estimated prices.
10. To identify properties that may be undervalued based on the difference between their listed and estimated prices.

## Target Users

The application is designed to support different types of real-estate users:

### Property Buyers

Buyers can browse properties, compare prices, view property details, and use estimated prices to make more informed purchasing decisions.

### Property Sellers

Sellers can use estimated prices as an additional reference when considering how to price their properties.

### Real-Estate Agents

Agents can organize and explore property information and use price estimates to support communication with clients.

### Property Investors

Investors can compare property prices and explore properties that may have a potential difference between their listed price and estimated price.

### Financial Institutions

Banks and other financial institutions could potentially use similar property-analysis systems as an additional source of information during property evaluation.

## Main Features

### 1. Property Listing

The application displays real-estate properties in an organized listing page. Users can browse available properties and view important information such as:

* Property title
* Location
* Price
* Number of bedrooms
* Number of bathrooms
* Land or building area
* Road information
* Property characteristics

### 2. Property Search and Filtering

Users can search and filter properties based on different criteria, including:

* Location
* Minimum price
* Maximum price
* Number of bedrooms
* Number of bathrooms

The application also supports sorting properties by price, making it easier for users to compare lower-priced and higher-priced listings.

### 3. Property Detail Page

Each property has a dedicated detail page containing more complete information about the listing.

The detail page provides information such as:

* Property title
* Address
* Listed price
* Property area
* Bedrooms and bathrooms
* Floors
* Parking information
* Road details
* Property characteristics
* Estimated price
* Location map

### 4. Machine-Learning-Based Price Prediction

The application includes a prediction form where users can enter property-related information and receive an estimated property price.

The prediction process considers information such as:

* Location or neighborhood
* Property area
* Bedrooms
* Bathrooms
* Floors
* Parking
* Road-related information
* Other available property features

The trained machine-learning model processes these inputs and returns an estimated price.

The prediction is intended to provide a data-driven reference rather than a guaranteed market valuation.

### 5. Neighborhood-Based Price Analysis

Property prices can vary significantly between different neighborhoods and cities. The project therefore includes neighborhood-related analysis and information to improve the relevance of price estimates.

Neighborhood information is used to help the application understand differences in property prices across locations.

### 6. Potentially Undervalued Properties

The application includes a section for identifying properties that may be undervalued.

This feature compares:

* The listed price of a property
* The estimated price generated by the machine-learning model

If the estimated price is higher than the listed price by a meaningful amount, the property may be considered potentially undervalued.

This feature does not guarantee that a property is a good investment. It only highlights properties that may deserve further investigation.

### 7. Interactive Property Maps

The application uses **Leaflet** and **OpenStreetMap** to display property locations on an interactive map.

Users can view the approximate geographical location of a property and understand where it is situated.

The project uses geocoded address information to assign latitude and longitude coordinates to properties. These coordinates allow the application to place property markers on the map.

### 8. Responsive User Interface

The frontend is developed using:

* HTML
* CSS
* Bootstrap 5
* JavaScript

Bootstrap 5 is used to create a clean, responsive, and user-friendly interface that can adapt to different screen sizes.

## Dataset and Data Preparation

The project uses a Nepal real-estate dataset containing property-related information. The dataset includes fields such as:

* Property title
* Address
* City
* Price
* Bedrooms
* Bathrooms
* Floors
* Parking
* Facing direction
* Year
* Area
* Road information
* Road width
* Road type
* Building area
* Amenities

The original dataset required several preparation steps before it could be used for analysis and machine learning.

### Data Cleaning

The data-cleaning process included:

* Checking missing values
* Checking duplicate records
* Examining incorrect or inconsistent values
* Removing invalid records
* Cleaning location information
* Checking data types
* Preparing numerical and categorical features

### Area Conversion

Property areas were provided using different measurement units. These included units such as:

* Aana
* Ropani
* Dhur
* Square feet

To make the data consistent, area values were converted into square feet wherever possible.

This conversion made it easier to compare properties and use area as a numerical feature in the machine-learning model.

### Location Cleaning

Location and address values were cleaned to reduce inconsistencies. The project also used address-based geocoding to obtain latitude and longitude coordinates for displaying properties on maps.

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure and characteristics of the real-estate dataset.

The analysis included:

* Examining the distribution of property prices
* Comparing property prices across cities and neighborhoods
* Studying the relationship between area and price
* Checking the number of properties in different locations
* Analyzing price per square foot
* Identifying missing values
* Checking duplicate records
* Examining property characteristics

The analysis indicated that factors such as **location, area, road access, and property characteristics** can influence real-estate prices.

## Machine Learning Approach

The project uses supervised machine learning for **regression** because the target value—property price—is numerical.

Two regression algorithms were explored:

### Random Forest Regressor

Random Forest is an ensemble machine-learning algorithm that combines multiple decision trees to produce a prediction.

It can identify complex relationships between property features and prices. It is useful for this project because property prices may depend on several interacting factors, such as location, area, bedrooms, road width, and property condition.

### Gradient Boosting Regressor

Gradient Boosting builds models sequentially, with each new model attempting to improve the errors made by previous models.

It was used as a comparison model to evaluate another approach for predicting property prices.

### Selected Model

After comparing the models, the **Random Forest Regressor** was selected as the main prediction model based on the evaluation results.

The trained model was saved and integrated into the Django application so that users can receive predictions through the web interface.

## Application Workflow

The overall workflow of the project is:

```text
Nepal Real-Estate Dataset
          ↓
Data Cleaning and Preparation
          ↓
Area Conversion and Location Cleaning
          ↓
Exploratory Data Analysis
          ↓
Machine Learning Model Training
          ↓
Model Evaluation and Selection
          ↓
Saved Machine-Learning Model
          ↓
PostgreSQL Property Database
          ↓
Django Web Application
          ↓
Property Browsing, Search, Maps, and Prediction
```

## Technology Stack

### Data Analysis and Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

### Backend

* Django
* Python

### Database

* PostgreSQL

### Frontend

* HTML
* CSS
* Bootstrap 5
* JavaScript

### Mapping

* Leaflet
* OpenStreetMap
* OpenStreetMap Nominatim geocoding service

## Role of PostgreSQL

PostgreSQL is used to store and manage the property information used by the Django application.

Instead of depending only on a CSV file for displaying properties, the application stores property records in a structured database.

The database supports:

* Property storage
* Property retrieval
* Search and filtering
* Property detail pages
* Price and prediction information
* Management of property-related records

## Role of Django

Django is used as the main backend framework of the application.

It connects the frontend, machine-learning model, and PostgreSQL database.

Django is responsible for:

* Handling web requests
* Retrieving property data
* Displaying property listings
* Processing search and filter inputs
* Receiving prediction form data
* Sending input features to the machine-learning model
* Displaying estimated prices
* Rendering HTML templates
* Managing application URLs and views

## Project Significance

This project demonstrates how data science and web development can be combined to solve a real-world problem.

It brings together:

* Data cleaning
* Exploratory data analysis
* Feature preparation
* Regression modelling
* Model evaluation
* Database management
* Backend development
* Frontend design
* Geographical visualization

The application can help make real-estate information easier to explore and can provide users with additional information when comparing property prices.

## Limitations

The project has several limitations:

* The prediction quality depends on the available dataset.
* Historical property data may not fully represent current market prices.
* Some property information may be incomplete or inconsistent.
* Property prices can change due to economic conditions and market demand.
* The model may not capture every factor that affects real-estate prices.
* Estimated prices should not be treated as official property valuations.
* The application currently focuses on the available dataset and local development environment.

## Future Scope

Possible future improvements include:

* Collecting more recent real-estate data through ethical web scraping.
* Adding more property features to the dataset.
* Improving the model through feature engineering and hyperparameter tuning.
* Adding user registration and login.
* Allowing users to submit their own property listings.
* Adding property image uploads.
* Improving map-based property search.
* Adding price-trend analysis.
* Generating property descriptions using a large language model.
* Adding more advanced property comparison tools.
* Deploying the application online.
* Exploring additional methods for property valuation.

## Conclusion

Nepal Real Estate Price Prediction and Property Analysis is a web-based machine-learning project designed to provide organized property information and data-driven price estimates.

The application combines a cleaned real-estate dataset, regression-based machine learning, PostgreSQL, Django, Bootstrap 5, and Leaflet maps.

Users can browse properties, search and filter listings, view detailed property information, explore property locations, estimate prices, and identify properties that may have a difference between their listed and estimated prices.

Although the model cannot guarantee the exact market value of a property, it provides an additional analytical reference that may support better property-related decisions.

## Author

**Apekshya Basnyat**

## Project Status

Working capstone project featuring:

* Real-estate data analysis
* Machine-learning-based price prediction
* PostgreSQL property database
* Django web application
* Property search and filtering
* Neighborhood-based analysis
* Potentially undervalued property identification
* Interactive property maps
* Responsive Bootstrap 5 interface
