import requests
from src.logger import logger


API_URL = "https://open.er-api.com/v6/latest/USD"


def get_exchange_rates():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "rates" not in data:
            raise ValueError("Invalid response received from exchange rate API.")

        logger.info("Successfully fetched exchange rates.")
        return data["rates"]

    except requests.RequestException as error:
        logger.error(f"Failed to fetch exchange rates: {error}")
        raise ValueError(
            "Unable to fetch exchange rates. Please check your internet connection."
        )


def convert_currency(amount, from_currency, to_currency):
    if amount <= 0:
        logger.error("Invalid amount: must be greater than zero.")
        raise ValueError("Amount must be greater than zero.")

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    rates = get_exchange_rates()

    if from_currency not in rates:
        logger.error(f"Unsupported source currency: {from_currency}")
        raise ValueError(f"Unsupported currency code: {from_currency}")

    if to_currency not in rates:
        logger.error(f"Unsupported target currency: {to_currency}")
        raise ValueError(f"Unsupported currency code: {to_currency}")

    from_rate = rates[from_currency]
    to_rate = rates[to_currency]

    converted_amount = amount / from_rate * to_rate

    logger.info(
        f"Converted {amount} {from_currency} to "
        f"{converted_amount} {to_currency}"
    )

    return converted_amount