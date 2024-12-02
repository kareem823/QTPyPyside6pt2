'''
2. Find the Longest Substring Without Repeating Characters

Question:
Given a string, find the length of the longest substring without repeating characters.

Solution:
I can utilize the sliding window technique with a hash map to keep track 
of characters and their positions. This approach allows
 me to efficiently find the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
    # dict to store the last index of each character
    char_map = {}
    start = maxLength = 0
    
    #iterate over the string from the right boundry of the window
    for end in range(len(s)):
        # if the character is in the map and its index is greater than or equal to the start
        if s[end] in char_map and char_map[s[end]] >= start:
            #move the start to the length of the last occurrence of the character
            start = char_map[s[end]] + 1
        
        #update the last index of the character
        char_map[s[end]] = end
        
        #update the maximum length of the substring if the current length is greater
        maxLength = max(maxLength, end - start + 1)

    return maxLength

# Example usage
s = "abcabcbbzigzigzigzihsdjkjbzig"
result = lengthOfLongestSubstring(s)
print(result)