# Python code​​​​​​‌‌​‌​‌​‌‌​‌​‌​​‌​​​​‌‌​‌​ below
# Use print("messages...") to debug your solution.

import os

def file_info():
    # Your code goes here.
    print(os.listdir())
    os.chdir("deps")

    totalbytes = 0

    for file in os.listdir():
        if file.endswith(".txt"):
            totalbytes += os.stat(file).st_size  
    print(totalbytes)
    return totalbytes

if __name__ == "__main__":
    file_info()