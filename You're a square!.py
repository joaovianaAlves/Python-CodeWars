# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

def is_square(n):    
    return True if n == 0 or (n > 0 and n**0.5 % 1 == 0) else False
