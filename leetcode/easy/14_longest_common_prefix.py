class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num_of_list_elements = len (strs)

        #if the List contains only one string, then return the single string as the longest common prefix (lcp)
        if num_of_list_elements == 1:
            return strs[0]
        lcp = ""
        
        #if either of the first two string elements are the empty string, then return an empty string as the lcp
        first_element_length = len (strs[0])
        second_element_length = len (strs[1])
        if first_element_length == 0 or second_element_length == 0:
            return ""
        
        # Build a the lcp based on the first two elements
        c = 0
        while c < first_element_length and c < second_element_length:
            # when a character is contained in both strings in the same position add the character to the lcp
            if strs[0][c] == strs[1][c]:
                lcp += strs[0][c]
            else:
                break
            c += 1

        # if there where only 2 strings in the list, then return the current lcp.
        if num_of_list_elements == 2:
            return lcp

        # other wise check the remaining items in the list.
        c = 2
        while c < num_of_list_elements and len(lcp) != 0:
            # if the current element is an empty string then lcp is empty string
            if len(strs[c]) == 0:
                return ""
            
            # to avoid index our of bound errors, make sure that you find the short string length between the lcp and current string
            shortest_string_length = 0
            if len(lcp) < len(strs[c]):
                shortest_string_length = len(lcp)
            else:
                 shortest_string_length = len(strs[c])

            #  when a character is contained in the same position in both the string and lcp, add the character to the the tmplcp
            tmplcp = ""
            for i in range(0,shortest_string_length):
                if strs[c][i] == lcp[i]:
                    tmplcp += lcp[i]
                else:
                    break
            # assign the new lcp to the current lcp
            lcp = tmplcp
            c += 1

        return lcp