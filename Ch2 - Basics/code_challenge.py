# Python code​​​​​​‌‌​‌​‌​‌‌​​​‌‌‌​‌‌‌‌​​​​‌ below
# Use print("messages...") to debug your solution.
import string
show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Your code goes here.
    # Create translation table
    tab = str.maketrans("", "", string.punctuation)
    cleanedteststr = teststr.translate(tab)
    cleanedteststr = cleanedteststr.replace(" ", "")
    reversedstr = cleanedteststr[::-1]  
    print(cleanedteststr)
    print(reversedstr) 
    
    if cleanedteststr.upper() == reversedstr.upper(): 
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    is_palindrome("Radar!")