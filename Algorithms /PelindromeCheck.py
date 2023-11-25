# solution 1
def isPalindrome(string):
    # Write your code here.
    return string == string[::-1]

# solution 2 
def isPalindrome(string):
    # Write your code here.
    count = 0 
    for i in reversed(range(len(string))):
        if string[count] != string[i]:
            return False
        count += 1
    return True
