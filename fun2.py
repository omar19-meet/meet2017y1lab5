####print('*')
####print('*')
####print('*')
####print('*')
####print('*')
####
####print('****')

##def draw_1d(n): #This function prints '*' n times.
##    c='*'*n
##    return(c)
##
##t=draw_1d(50)
##print(t)
c1="~"
c2="!"
##
##def draw_1d(n, char): #This function prints a certain character, either ! or ~ n times
##    c=n*str(char)
##    return(c)
##
##
##
##t2=draw_1d(35,c1)
##print(t2)

def draw_2d(n,m,char):
    draw=int(n)*str(char)
    for i in range(m):
        print("                                                                          ")
        draw=draw+draw
    return(draw)

test2=draw_2d(3,5,c1)
print(test2)
