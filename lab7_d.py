def run_length_encoding(input_string):
    # Initialize variables
    count = 1
    prev_char = input_string[0]
    output = ""

    # Iterate through input string, starting from the second character
    for char in input_string[1:]:
        # If current char is same as previous one, increment the count
        if char == prev_char:
            count += 1
        else:
            output += str(count) + prev_char
            count = 1
            prev_char = char

    # Add the last character and count to output
    output += str(count) + prev_char

    return output


# Example usage
input_string = "aaabbcccdaa"
encoded_string = run_length_encoding(input_string)
print(encoded_string)
