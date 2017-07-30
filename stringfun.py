def string_test(s):
    if len(s)>2:
        if s[0]==s[-1]:
            return("True")
    else:
        return("False")

def add_x(s):
    s='x'+s+'x'
    return(s)

test1=add_x('asdfj')
print(test1)
