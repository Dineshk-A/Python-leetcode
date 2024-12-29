class Solution:
    def indec(haystack : str,needle : str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i : i + len(needle)] == needle: #we are slicing using [i: i+len] for example [1:3] in hello is "el" e is 1 .
                return i
        return -1
    
haystack = "hello"    
needle = "ll"
result = Solution.indec(haystack,needle)
print(result)

# List: A mutable sequence of items, created using square brackets ([]), e.g., my_list = [1, 2, 3].
# String: An immutable sequence of characters, also accessed using square brackets for indexing or slicing, e.g., haystack = "hello".
# Slicing: A technique used to extract a portion of the string (or list) using the start:end syntax within square brackets.

# haystack[] refers to a string (not a list).
# Slicing is the technique you're using to extract substrings from a string, using the square brackets ([]).
# While strings share some similarities with lists (both are sequences), strings are immutable, whereas lists are mutable.

# haystack = "hello"
# substring = haystack[1:3]

# start = 1: This refers to the second character in the string ('e' at index 1).
# end = 3: This means "stop before index 3". In other words, it stops just before index 3, so it includes the characters at index 1 and 2, but not index 3.