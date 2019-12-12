import sys, functools
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    text = str(text)
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
        if next in ")]}":
            # Process closing bracket, write your code here
            pop = opening_brackets_stack[-1]
            if next == ")" and pop == "(":
                opening_brackets_stack.pop()
            elif next == "}" and pop == "{":
                opening_brackets_stack.pop()
            elif next == "]" and pop == "[":
                opening_brackets_stack.pop()
            else: 
                return i
    return "Success"

def main():
    text = sys.stdin.read()
    ret = find_mismatch(text)
    # Printing answer, write your code here
    print ret

MAINFUNC = main
###########################################################################################
import traceback

if __name__ == '__main__':
  try:
    ret = MAINFUNC()
  except Exception as e:
    details = traceback.format_exc()
    print "\nRuntime error: %s\n\n %s"%(e, details)
  else:
    pass
