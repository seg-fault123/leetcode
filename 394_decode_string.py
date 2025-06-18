class Solution:
    def decodeString(self, s: str) -> str:
        # when a ] is encounterd, then the current_string is repeated int_stack[-1] times and added to string_stack[-1]. So all operations are done to current_string. If *number*[ is encountered, the current_string is stored in the stack and a new current_started is started which will be repeated *number* times.
        current_string = ''
        string_stack = []

        current_int = 0
        int_stack = []

        for char in s:
            if char.isdigit():
                current_int = 10*current_int + int(char)
            elif char=='[':
                int_stack.append(current_int)
                current_int = 0

                string_stack.append(current_string)
                current_string = ''
            elif char==']':
                repeat = int_stack.pop()
                current_string = string_stack.pop() + current_string*repeat
            else:
                current_string += char
        
        return current_string

