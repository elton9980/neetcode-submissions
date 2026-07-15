class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        # Use the first string as our reference point
        first_str = strs[0]
        
        # Iterate through each character index of the first string
        for i in range(len(first_str)):
            char_to_match = first_str[i]
            
            # Compare this character with the character at index i in all other strings
            for other_str in strs[1:]:
                # If we've reached the end of any other string, 
                # or if we find a character mismatch:
                if i >= len(other_str) or other_str[i] != char_to_match:
                    # Return the matched prefix up to this point
                    return first_str[:i]
                    
        # If we successfully loop through the entire first string without any mismatch,
        # then the first string itself is the longest common prefix.
        return first_str

        

        