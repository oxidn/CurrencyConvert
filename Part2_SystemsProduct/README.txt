# Currency Converter - Systems Product

This is a currency converter with a simple graphical user interface (GUI) built using Tkinter. It uses live exchange rates from an external API.

## Requirements

* Python 3.10 or later
* Internet connection

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The GUI allows you to:

* Enter an amount
* Select the source currency
* Select the target currency
* Convert using live exchange rates

## Features

* Simple Tkinter GUI
* Live exchange rates
* Multiple currency options
* Error handling for invalid inputs
* Logging to `app.log`
* Automated unit tests

## Run Tests

```bash
python -m unittest discover tests
```

## API

This project uses the ExchangeRate-API:

https://open.er-api.com/v6/latest/USD
