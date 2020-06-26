def calculate_letters(text: str):
    letters = []
    for letter in text:
        sign = ord(letter)
        if sign == 32:
            letters.append(True)
        else:
            col = sign % 16
            row = int((sign - col) / 16)
            letters.append((col, row))

    return letters