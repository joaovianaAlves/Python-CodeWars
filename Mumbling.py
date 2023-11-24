# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    result = ''
    for i, char in enumerate(s):
        result += char.upper() + char.lower()*i
        if i < len(s)-1:
            result += '-'
    return result
