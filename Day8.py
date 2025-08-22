def reverseWords(s: str) -> str:
    # Split by whitespace (this also removes extra spaces automatically)
    words = s.strip().split()
    # Reverse the list of words
    words.reverse()
    # Join back with a single space
    return " ".join(words)

# Test cases
print(reverseWords("the sky is blue"))       # "blue is sky the"
print(reverseWords("  hello world  "))       # "world hello"
print(reverseWords("a good   example"))      # "example good a"
print(reverseWords("    "))                  # ""
print(reverseWords("word"))                  # "word"
