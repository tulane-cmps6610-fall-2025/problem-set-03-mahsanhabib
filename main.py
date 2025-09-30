#problem-set-03

# no other imports needed
from collections import defaultdict
import math
#

### PART 1: SEARCHING UNSORTED LISTS 

def iterate(f, x, a):
    # print(x)
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        # print(f"x = {x}, a[0] = {a[0]}, {f(x, a[0])}")
        return iterate(f, f(x, a[0]), a[1:])

# search an unordered list L for a key x using iterate
def isearch(L, x):
    ###TODO
    def f(found, item):
        return bool(found or item == x) 
    return iterate(f, False, L) 
    ###

def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert isearch([], 2) == (2 in [1, 3, 5])


test_isearch()

# --------------------------------------------------------------------------

# search an unordered list L for a key x using reduce
def rsearch(L, x):
    ###TODO
    # Use reduce with a lambda, always return boolean
    # def f(found, item):
    #     print(f"found={found}, item={item}, item==x={item==x}")
    #     return bool(found is True or item == x)
    # return reduce(f, False, L)
    return (
        reduce(lambda found, item:
                   (found is True)     # left subtree already found it
                   or (item is True)   # right subtree already found it
                   or (found == x)     # left subtree reduced to element x
                   or (item == x),     # right subtree reduced to element x
               False, L)
    )

def reduce(f, id_, a):
    # print(a)
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel 
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        # print(a[:len(a)//2], a[len(a)//2:], res )
        return res 

def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(ureduce(f, id_, a[:len(a)//3]),
                 ureduce(f, id_, a[len(a)//3:]))

def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert rsearch([], 2) == (2 in [1, 3, 5])

test_rsearch()




### PART 3: PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    ### TODO
    # mylist = ['(', 'a', ')']
    return iterate(parens_update, 0, mylist) == 0
    pass
    ###


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    ###TODO
    if current_output < 0:
        return current_output  # Already invalid, keep it negative
    
    if next_input == '(':
        return current_output + 1
    elif next_input == ')':
        return current_output - 1
    else:
        return current_output
    
    ###


def test_parens_match_iterative():
    assert parens_match_iterative(['(', 'a', ')']) == True
    assert parens_match_iterative([')', '(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
    assert parens_match_iterative([]) == True


test_parens_match_iterative()


#### Scan solution

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0
    
    

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    ###TODO
    mapped = list(map(paren_map, mylist))
    scanned, total = scan(lambda x, y: x + y, 0, mapped)
    # print(f"mapped: {mapped}, scanned: {scanned}, total: {total}")
    return total == 0 and all(min_f(x, 0) == 0 for x in scanned)
    

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y


def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False
    assert parens_match_scan([]) == True


test_parens_match_scan()

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###TODO
    # base cases
    if len(mylist) == 0:
        return (0, 0)
    elif len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1)
        elif mylist[0] == ')':
            return (1, 0)
        else:
            return (0, 0)
    
    # recursive case
    # - first solve subproblems
    mid = len(mylist) // 2
    left_R, left_L = parens_match_dc_helper(mylist[:mid])
    right_R, right_L = parens_match_dc_helper(mylist[mid:])


    
    # - then compute the solution (R,L) using these solutions, in constant time.

    matched = min(left_L, right_R)
    total_R = left_R + right_R - matched
    total_L = left_L + right_L - matched
    return (total_R, total_L)


def test_parens_match_dc():
    assert parens_match_dc(['(', 'a', ')']) == True
    assert parens_match_dc([')', '(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 


test_parens_match_dc()








### PART 2: LIST DEDUPLICATION

def dedup_sequential(A):
    """
    Sequential algorithm to remove duplicates while preserving order.
    Work: O(n), Span: O(n)
    """
    seen = set()
    result = []
    for item in A:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def dedup_parallel(A):
    """
    Parallel divide-and-conquer algorithm for deduplication.
    Work: O(n log n), Span: O(n)
    """
    if len(A) <= 1:
        return A[:]
    
    mid = len(A) // 2
    left = dedup_parallel(A[:mid])
    right = dedup_parallel(A[mid:])
    
    # Merge while preserving order and removing duplicates
    seen = set(left)
    result = left[:]
    
    for item in right:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

def test_dedup():
    # Test case 1: Basic duplicates
    assert dedup_sequential([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    assert dedup_parallel([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 2: No duplicates
    assert dedup_sequential([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert dedup_parallel([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 3: All duplicates
    assert dedup_sequential([1, 1, 1, 1]) == [1]
    assert dedup_parallel([1, 1, 1, 1]) == [1]
    
    # Test case 4: Empty list
    assert dedup_sequential([]) == []
    assert dedup_parallel([]) == []
    
    # Test case 5: Single element
    assert dedup_sequential([42]) == [42]
    assert dedup_parallel([42]) == [42]
    
    # Test case 6: Mixed types (strings and numbers)
    assert dedup_sequential(['a', 1, 'b', 1, 'a', 2]) == ['a', 1, 'b', 2]
    assert dedup_parallel(['a', 1, 'b', 1, 'a', 2]) == ['a', 1, 'b', 2]

# Run the tests
test_dedup()
print("All deduplication tests passed!")
