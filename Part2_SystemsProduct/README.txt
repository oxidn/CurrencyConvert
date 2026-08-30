Currency Converter - Systems Product

This is a command-line currency converter that uses live exchange rates from an external API.

Requirements:

* Python 3.10 or later
* Internet connection

Installation:
pip install -r requirements.txt

Usage:
python main.py --from USD --to INR --amount 150

Example:
python main.py --from INR --to USD --amount 1000

Features:

* Live exchange rates
* Command-line interface
* Error handling for invalid inputs
* Logging to app.log
* Automated unit tests

Run tests:
python -m unittest discover tests

API:
https://open.er-api.com/v6/latest/USD
