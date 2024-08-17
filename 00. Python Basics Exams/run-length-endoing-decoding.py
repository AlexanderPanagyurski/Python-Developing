def encode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    encoded_text = []
    current_index = 0
    counter = 1

    for current_index in range(len(text) - 1):
        if text[current_index] == text[current_index + 1]:
            counter += 1
        else:
            encoded_text.append(text[current_index])
            if counter > 1:
                encoded_text.append(str(counter))
            counter = 1
    encoded_text.append(text[current_index + 1])
    if counter > 1:
        encoded_text.append(str(counter))

    return "".join(encoded_text)


def decode(text):
    """
    Decodes the text using run-length encoding
    """
    decoded_text = []
    for index in range(len(text)):
        number = ""
        current_index = index + 1
        while current_index < len(text) and text[current_index].isnumeric():
            number += text[current_index]
            current_index += 1

        if text[index].isalpha():
            decoded_text.append(text[index])

        if number.isnumeric():
            for i in range(int(number) - 1):
                decoded_text.append(text[index])
        index = current_index

    return "".join(decoded_text)


print(encode("AABCCCDEEEE") == "A2BC3DE4")
print(decode("A2BC3DE4") == "AABCCCDEEEE")
print(encode("ABABAB") == "ABABAB")
print(decode("ABABAB") == "ABABAB")