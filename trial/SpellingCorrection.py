from textblob import TextBlob



def remove_repeated_chars(input_string):
    result = []
    count = 1

    for i in range(len(input_string)):
        # Check if the current character is the same as the next one
        if i < len(input_string) - 1 and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            # If the count is 2 or less, add the characters to the result
            if count <= 2:
                result.extend([input_string[i]] * count)
            count = 1

    return ''.join(result)

# Example usage:
input_str = "aaabbbbccdddeee"
result_str = remove_repeated_chars(input_str)
print(result_str)


#
# incorrect_words = ["cmputr", "yeeees", "haappy", "tunee", "fel", "cute"]  # incorrect spelling
#
# text = " ".join(incorrect_words)  # join them as comma separated list
# print(f"original words: {text}")
#
# b = TextBlob(text)
#
# # prints the corrected spelling
# print(f"corrected words: {b.correct()}")