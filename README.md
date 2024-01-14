# Phone Recommendation System

This project is a phone recommendation system that utilizes web scraping to gather data from an online marketplace, performs exploratory data analysis, and employs machine learning to suggest phones based on user input.

## Introduction

The Phone Recommendation System is designed to help users find the most suitable phones based on their preferences. It includes web scraping to gather phone data, exploratory data analysis (EDA) to clean and analyze the data, machine learning modeling to predict phone prices, and user interaction features to provide recommendations.

## Features

- Web scraping to collect phone data from an online marketplace (Flipkart in this case).
- Exploratory data analysis (EDA) and data cleaning to prepare the dataset for modeling.
- Machine learning modeling using linear regression to predict phone prices.
- User interaction features allowing users to input preferences for RAM size, ROM size, rating, and brand to get personalized recommendations.
- Displaying the suggested price of a phone based on user input.
- Recommending phones that fit within the suggested price range.

## Requirements

- Python 3
- Libraries: requests, BeautifulSoup, retrying, pandas, numpy, seaborn, matplotlib, scikit-learn

## Installation

1. Clone the repository:

```bash
git clone https://github.com/neerajsde/Mobile-Phone-Price-Predection.git
cd phone-recommendation-system