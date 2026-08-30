# Currency Converter - Systems Product

## Overview

This project is a command-line currency converter developed as a Programming Systems Product. It converts an amount from one currency to another using live exchange rates from an external API.

The application includes command-line arguments, error handling, logging, automated unit tests, and documentation.

## Requirements

* Python 3.10 or later
* Internet connection
* Requests Python library

## Installation

1. Navigate to the Part2_SystemsProduct directory.

2. Install the required dependencies:

   pip install -r requirements.txt

## Usage

Run the application using the following command:

```
python main.py --from USD --to INR --amount 150
```

## Arguments

--from

Specifies the source currency code.

Example:

```
--from USD
```

--to

Specifies the target currency code.

Example:

```
--to INR
```

--amount

Specifies the amount to convert.

Example:

```
--amount 150
```

## Example Commands

Convert USD to INR:

```
python main.py --from USD --to INR --amount 150
```

Convert INR to USD:

```
python main.py --from INR --to USD --amount 1000
```

Convert EUR to GBP:

```
python main.py --from EUR --to GBP --amount 50
```

## Exchange Rate API

This project uses the ExchangeRate API to retrieve live currency exchange rates.

API URL:

```
https://open.er-api.com/v6/latest/USD
```

The application fetches exchange rates dynamically when a conversion is performed.

## Error Handling

The program handles invalid input and displays user-friendly error messages.

Examples of handled errors include:

* Negative amounts
* Zero amounts
* Unsupported currency codes
* Invalid input
* Network connection problems
* API request failures

The application avoids displaying raw Python tracebacks to the user.

## Logging

The application logs successful operations and errors to a file named:

```
app.log
```

The log file includes:

* Date and time
* Log level
* Successful exchange rate fetches
* Successful currency conversions
* Errors

## Testing

Automated unit tests are included in:

```
tests/test_converter.py
```

The tests cover both successful conversions and error cases.

To run the tests, use:

```
python -m unittest discover tests
```

## Test Coverage

The automated tests include:

* Valid currency conversion
* Conversion between different currencies
* Negative amount handling
* Zero amount handling
* Invalid source currency
* Invalid target currency

The exchange rate API is mocked during tests so that the tests do not depend on an internet connection or changing live exchange rates.

## Project Structure

Part2_SystemsProduct/

├── src/
│   ├── converter.py
│   └── logger.py
│
├── tests/
│   └── test_converter.py
│
├── main.py
├── requirements.txt
├── README.txt
└── app.log

## Example Output

Command:

```
python main.py --from USD --to INR --amount 150
```

Example output:

```
150.00 USD = 13000.00 INR
```

Note: The actual converted amount may vary because the application uses live exchange rates.

## Author

Programming Systems Product Assignment
