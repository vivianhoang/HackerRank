"""Steve has a string, s, consisting of n lowercase English alphabetic letters. In one operation,
he can delete any pair of adjacent letters with same value. For example, string "aabcc" would
become either "aab" or "bcc" after 1 operation.

Steve wants to reduce  as much as possible. To do this, he will repeat the above operation as
many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

Note: If the final string is empty, print Empty String."""

def removeRepeats(s):
    letters = list(s)
    i = 0
    while i < len(letters) - 1:
        if letters[i] == letters[i+1]:
            del letters[i], letters[i]
            i = 0
            if len(letters) == 0:
                return "Empty String"
        else:
            i += 1
            
    return ''.join(letters)
            
print removeRepeats(raw_input())