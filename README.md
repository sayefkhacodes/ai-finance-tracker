# AI Finance Tracker

A personal finance tracker that uses AI to automatically categorise transactions and visualise spending patterns.

Built with Python, SQLite, Flask, and Google Gemini API.

## Features

- Upload transactions via CSV
- AI-powered automatic categorisation using Google Gemini
- Spending summary broken down by category
- Visual pie chart of expenses
- Clean web interface built with Flask

## Tech Stack

- **Python** — core language
- **SQLite** — local database for storing transactions
- **Flask** — web framework for the browser interface
- **Google Gemini API** — AI categorisation
- **Matplotlib** — chart generation

## How It Works

1. Transactions are loaded from a CSV file into a SQLite database
2. Google Gemini AI analyses each transaction and assigns a category
3. A spending summary and pie chart are generated
4. Results are displayed in a Flask web app

## Setup

bash
# Clone the repo
git clone https://github.com/sayefkhacodes/ai-finance-tracker.git
cd ai-finance-tracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Set up database and import transactions
python3 database.py

# Run AI categorisation
python3 run_categorization.py

# Generate chart
python3 chart.py

# Start the web app
python3 app.py


Then open http://127.0.0.1:5000 in your browser.


## Project Structure
ai-finance-tracker/
├── app.py                  # Flask web application

├── database.py             # SQLite database functions

├── categorize.py           # Gemini AI categorisation

├── run_categorization.py   # Pipeline: DB → AI → save results

├── summary.py              # Spending summary logic

├── chart.py                # Pie chart generation

├── transactions.csv        # Sample transaction data

├── templates/

│   └── index.html          # Web interface template

└── static/

└── spending_chart.png  # Generated chart

## What I Learned

- Building a full data pipeline from CSV to database to AI to web
- Prompt engineering to improve AI categorisation accuracy
- Integrating third-party AI APIs into a Python project
- Flask routing and Jinja2 templating
- SQLite database design and CRUD operations