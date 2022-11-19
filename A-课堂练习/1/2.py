import math
h,s1,v,l,k,n=map(float,input().split())
print(int(min(int(s1-math.sqrt((h-k)/5)*v+l),n)-max(int(s1-math.sqrt(h/5)*v),0)))
