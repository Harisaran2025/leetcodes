class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] #taking first string of words in variable

        for word in strs[1:]:
            while not word.startswith(prefix):  #startswith is a built in function
                prefix = prefix[:-1]  #removes the last characters one by one comparing with other words

                if prefix == "":
                    return ""

        return prefix
        
