import itertools
digs = [0,2,3,4,5,6,7,8,9]
def solve_cryptarithmetic():
    for digits in itertools.permutations(digs, 7):
        set_d = set(digits)
        # print(digits)
        
        s, e, n, d, o, r, y = digits        
        m=1
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        
        if send + more == money:
            return f"Solution found: {send} + {more} = {money}"
    
    return "No solution found"

print(solve_cryptarithmetic())
