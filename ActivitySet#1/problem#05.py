def computepay(h, r):
    if h<=40:
        tot=h*r
        return tot
    else:
        i=h-40
        t1=40*r
        t2=i*r*1.5
        t=t1+t2
        return t

hrs = float(input("Enter Hours:"))
rate = float(input("Enter the rate:"))
p = computepay(hrs, rate)
print("Pay", p)