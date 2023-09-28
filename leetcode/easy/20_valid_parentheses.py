class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "({["
        temp = ""

        # if odd, automatic False
        if len(s) % 2 == 1:
            return False

        # for each character in string
        for c in s:
            # check if c is an open bracket. If it is add to the temp string
            if c in open_brackets:
                temp += c
            # otherwise its a close bracket
            else:
                # if all open brackets have already been matched, then False
                if len(temp) == 0:
                    return False
                # grab the last open bracket found in string to this point
                last_open_bracket = temp[len(temp) -1]
                
                # check if closed bracket matches the last open bracket. If it doesn't then return false
                if c == ")" and last_open_bracket != "(":
                    return False
                elif c == "}" and last_open_bracket != "{":
                    return False
                elif c == "]" and last_open_bracket != "[":
                    return False
                else:
                    # otherwise the closed bracket is a match to the last open bracket, so remove the matching bracket.
                    # Need to add a check here for more closed than open brackets.
                    temp = temp[:-1]

        ## check for remaining open brackets
        if len(temp) > 0:
            return False
        return True