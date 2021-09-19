def add_dots(st):
    res = '.'.join(st[i:i + 1] for i in range(0, len(st), 1))
    return res

def remove_dots(st):
    st2 = ""
    for let in st:
        if let != ".":
            st2 += let
    
    return st2


def count(st):
    return len(st.split("-"))


def is_anagram(first, sec):
    if ("".join(sorted(first))) == ("".join(sorted(sec))):
        return True
    else:
        return False

def flatten(ls):
    res = []
    for i in ls:
        res.extend(i)
    return res

def largest_difference(ls):
    if max(ls)<=100 and min(ls)>= -100:
        diff = max(ls) - min(ls)
    return diff

def div_3(num):
  return num % 3 == 0
  
def get_row_col(st):
    board = {"A1":(0,0), "A2":(1,0), "A3":(2, 0),
             "B1":(0,1), "B2":(1,1), "B3":(2,1),
             "C1":(0,2), "C2":(1,2), "C3":(2,2)}
    if st in board:
        return board[st]

def palindrome(st):
    return st == st[::-1]

def up_down(n):
    res = (n-1, n+1)
    return res

def consecutive_zeros(st):
    return max(map(len,st.split("1")))

def all_equal(ls):
    return all(i==ls[0] for i in ls)

def triple_and(x, y, z):
    return all([x, y, z])

def convert(ls): return [str(i) for i in ls]

def list_xor(n, list1, list2):
    if n in list1 and n in list2:
        return False
    elif n not in list1 and n not in list2:
        return False
    elif n in list1 or list2:
        return True

def format_number(n):
    return(f"{n:,}")