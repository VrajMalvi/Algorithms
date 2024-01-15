# def firstNonRepeatingCharacter(string):
#     # Write your code here.
#     for idx in range(len(string)):
#         foundDuplicate = False
#         for idx2 in range(len(string)):
#             if string[idx] == string[idx2] and idx != idx2:
#                 foundDuplicate = True

#         if not foundDuplicate:
#             return idx

#     return -1
# # O(n^2) time | O(1)

# SOLution:

def firstNonRepeatingCharacter(string):
    # O(n) | O(1)
    counts = {}
    for character in string:
        if character not in counts:
            counts[character] = string.count(character)
            # or can be done using:
            # counts[i] = counts.get(character, 0) +1
            # if char exist then add 1 if not then assign 0 to the index character

    for idx in range(len(string)):
        char = string[idx]
        if counts[char] == 1:
            return idx

    return -1
