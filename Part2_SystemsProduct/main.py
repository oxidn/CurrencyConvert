import argparse
from src.converter import convert_currency


def main():
    parser = argparse.ArgumentParser(
        description="Convert currency using live exchange rates."
    )

    parser.add_argument(
        "--from",
        dest="from_currency",
        required=True,
        help="Source currency code (example: USD)"
    )

    parser.add_argument(
        "--to",
        dest="to_currency",
        required=True,
        help="Target currency code (example: INR)"
    )

    parser.add_argument(
        "--amount",
        required=True,
        help="Amount to convert"
    )

    args = parser.parse_args()

    try:
        amount = float(args.amount)

        result = convert_currency(
            amount,
            args.from_currency,
            args.to_currency
        )

        print(
            f"{amount:.2f} {args.from_currency.upper()} = "
            f"{result:.2f} {args.to_currency.upper()}"
        )

    except ValueError as error:
        print(f"Error: {error}")

    except Exception:
        print("An unexpected error occurred. Please try again.")


if __name__ == "__main__":
    main()