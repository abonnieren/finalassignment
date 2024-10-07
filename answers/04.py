def palindromeChecker(s):
    s = s.lower()
    s = s.strip()
    if s == s[::-1]:
        return True
    else:
        return False

random_string = input("Enter a string: ")
print(palindromeChecker(random_string))