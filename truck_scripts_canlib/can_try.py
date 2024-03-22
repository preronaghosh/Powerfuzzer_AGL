def extract_decimal_from_decimal(input_decimal):
    # Convert the decimal input to binary representation
    binary_string = bin(input_decimal)[2:]

    # Ensure the binary string has at least 29 bits (add leading zeros if needed)
    while len(binary_string) < 29:
        binary_string = '0' + binary_string

    # Extract bits 8 to 25 from the binary string and convert to decimal
    extracted_binary = binary_string[3:21]
    print(extracted_binary)
    extracted_decimal = int(extracted_binary, 2)

    return extracted_decimal

# Example usage
input_decimal = 419291417 # Replace with your decimal input
result = extract_decimal_from_decimal(input_decimal)

print(f"Extracted Decimal Value: {result}")