def justify_text(text, width):
    # Split the text into words
    words = text.split()
    
    # Initialize a list to store the lines
    lines = []
    current_line = []
    current_length = 0
    
    # Build lines such that they fit within the specified width
    for word in words:
        # Check if adding the current word exceeds the width
        if current_length + len(word) + len(current_line) > width:
            # If it does, we push the current line to the list of lines
            lines.append(current_line)
            # Start a new line with the current word
            current_line = [word]
            current_length = len(word)
        else:
            # If it fits, we add the word to the current line
            current_line.append(word)
            current_length += len(word)
    
    # Add the last line
    lines.append(current_line)
    
    # Now justify each line
    justified_text = ""
    for line in lines:
        # If the line has more than one word, justify it
        if len(line) > 1:
            total_spaces = width - sum(len(word) for word in line)
            space_between_words = total_spaces // (len(line) - 1)
            extra_spaces = total_spaces % (len(line) - 1)
            
            # Add words with the appropriate amount of spaces
            for i in range(len(line) - 1):
                justified_text += line[i] + ' ' * (space_between_words + (1 if i < extra_spaces else 0))
            justified_text += line[-1] + '\n'
        else:
            # If there's only one word, it will be left-aligned
            justified_text += line[0].ljust(width) + '\n'
    
    return justified_text


# Get input from the user
input_text = input("Enter the text: ")
width = int(input("Enter the number of columns for justification: "))

# Justify the text
justified_text = justify_text(input_text, width)

# Print the justified text
print("\nJustified Text:")
print(justified_text)
