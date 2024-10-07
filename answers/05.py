def vowelCounter(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

random_string = input("Enter a word: ")
print(f"Number of vowels : {vowelCounter(random_string)}")