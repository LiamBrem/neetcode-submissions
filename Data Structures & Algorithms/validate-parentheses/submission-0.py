class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")": "(", "]": "[", "}": "{"}
        stack = []

        for p in s:
            print(p, stack)
            if stack and p in matches and stack[-1] == matches[p]:
                stack.pop()
            else:
                stack.append(p)

        return len(stack) == 0 



        