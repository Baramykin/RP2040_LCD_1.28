file_path = 'output.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    for symbol in content:
        print(f"Symbol: {symbol}")
        if symbol.isdigit():
            number = int(symbol)
            print(f"Numeric symbol: {number}")
            break
        else:
            print(f"Not a numeric symbol: {symbol}")

            