# NBAGPT

A fun little project to talk to NBA data found on Kaggle

## requirements

`poetry`
`streamlit`
`pandasai`
`pandas`
`dotenv`

## Install

`poetry install`

## Run

### Download data from Kaggle

`kaggle datasets download -d justinas/nba-players-data`

### Run streamlit application

`poetry run streamlit run streamlit_app.py`

## TODO

Use local LLMs
Test with more NBA datasets
Allow the user to upload their own dataset
