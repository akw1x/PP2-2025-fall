def is_palindrome(text):
    text = text.lower()  
    text = text.replace(" ", "")
    rtext = text[::-1] 
    if text == rtext:
        return True
    else:
        return False

word = input()

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")