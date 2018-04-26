import sys


def format_price(price) -> str:
    try:
        float_price = float(price)
    except ValueError:
        return None
    if float_price - int(float_price) == 0:
        return '{:,}'.format(int(float_price)).replace(',', ' ')
    return '{:,.2f}'.format(float_price).replace(',', ' ')


if __name__ == '__main__':
    if sys.argv[1]:
        raw_price = sys.argv[1]
    print(format_price(raw_price))
