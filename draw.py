from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    xt = x1
    yt = y1
    ydist = y1 - y0
    xdist = x1 - x0
    if (ydist == 0):
        while (x0 < x1):
            plot(screen, color, x0, y0)
            x0+=1
    elif (xdist == 0):
        while (y0 < y1):
            plot(screen, color, x0, y0)
            y0+=1
    else:
        if (x1 < x0):
            x1 = x0
            x0 = xt
            y1 = y0
            y0 = yt
        A = y1 - y0
        B = x1 - x0
        if (y1 > y0):
            if (A <= B):
                B*=-1
                A*=2
                d = A + B
                B*=2
                while (x0 <= x1):
                    plot(screen, color, x0, y0)
                    if (d > 0):
                        y0+=1
                        d+=B
                    x0+=1
                    d+=A
            else:
                A*=-1
                d = (2 * B) + A
                B*=2
                A*=2
                while (y0 <= y1):
                    plot(screen, color, x0, y0)
                    if (d > 0):
                        x0+=1
                        d+=(A)
                    y0+=1
                    d+=(B)
        else:
            if (abs(A) <= B):
                A*=2
                d = A + B
                B*=2
                while (x0 <= x1):
                    plot(screen, color, x0, y0)
                    if (d < 0):
                        y0-=1
                        d+=B
                    x0+=1
                    d+=A
            else:
                A*=-1
                B*=-1
                B*=2
                d = B + A
                A*=2
                while (y0 >= y1):
                    plot(screen, color, x0, y0)
                    if (d < 0):
                        x0+=1
                        d+=A
                    y0-=1
                    d+=B
