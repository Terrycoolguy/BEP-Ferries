# BEP-Ferries Repository

## Overview

This repository is part of a comprehensive research project aimed at understanding and analyzing public sentiment regarding ferry services in the Netherlands. Given the critical challenges facing ferry operations, including reduced subsidies and the need for enhanced public engagement, this project utilizes web scraping methodologies to collect, validate, and analyze data from major social media platforms: Facebook, Twitter (X), and Google.

## Repository Structure

The repository contains organized directories for each social media platform, each housing the respective scraping tools:

- **Facebook**: Contains a Python-based scraper that automates data collection from Facebook posts, comments, and discussions related to ferry services, leveraging Selenium and BeautifulSoup. The scraper used is a modified version of AbderrahimAl's Facebook scraper, enabling data retrieval from 2014 to the present. For the original scraper, visit [AbderrahimAl's Facebook Scraper](https://github.com/AbderrahimAl/Facebook-Scraper/tree/main).
  
- **Twitter (X)**: Due to changes in Twitter transitioning to platform X, the scraper here navigates the complexities of data retrieval without direct API access, focusing on real-time public opinions and reactions. This scraper is based on [drowsy-coder's Social-Scraper](https://github.com/drowsy-coder/Social-Scraper).
  
- **Google**: Focuses on extracting reviews and ratings from Google Maps related to ferry services across various locations in the Netherlands, providing both quantitative ratings and qualitative insights. The scraper used is gaspa93's Google scraper, unmodified from the original. Visit the original project at [gaspa93's Google Maps Scraper](https://github.com/gaspa93/googlemaps-scraper).

Additionally, the repository includes two other directories:

- **Data Preprocessing**: This directory contains scripts and tools used to preprocess the raw data collected from social media platforms. Data preprocessing is an essential step to clean, format, and prepare the data for further analysis.

- **Sentiment Analysis**: In this directory, you'll find scripts and notebooks for conducting sentiment analysis on the collected data. Sentiment analysis helps assess the emotional tone and sentiment expressed in the social media posts and comments related to ferry services.

Feel free to explore these directories for more details and tools related to data preprocessing and sentiment analysis.

## Usage

Before running any scripts, install the necessary Python dependencies:

```sh
pip install -r requirements.txt

```
Each platform scraper has its own package requirements. They can be found in their respective directory.
