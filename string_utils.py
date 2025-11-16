def split_before_each_uppercases(formula):
    x=""
    y=[]
    for i in formula:
        x+=i
        if i.isupper():
            y.append(x)
            x=""
    return(y)


def split_at_first_digit(formula):
    x=""
    y=""
    for i in formula:
        if i.isdigit(): x+=i
        else: y+=i
    if x=="": x+=1
    return(y,int(x))
            
