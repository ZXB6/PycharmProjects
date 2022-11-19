def js(**d):
    sum=0
    for i in d:
        sum+=d.keys(i)
    avr=sum/len(d)
    a=(avr,)
    for i in d:
        if d.keys()>avr:
            a.append(d.keys(i))
    print(a)
js(1,2,3,4,5,6)