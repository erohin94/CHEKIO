def first_word(text):
    """
    function returns the first word in a given text.
    """
    a = text.replace('.', ' ').replace(',', ' ')
    x = a.split()
    return x[0]
    
print(first_word("Hello world"))


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
