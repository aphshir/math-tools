def suite(exp,value,n,start=0,lis=False):
    if lis == False:
        for i in range(start+1,n+1):
                expr=exp.replace("un",str(value))
                expr=expr.replace("n",str(i-1))
                value=eval(expr)
        return value
    elif lis == True:
        li = {start:value}
        for i in range(start+1,n+1):
                expr=exp.replace("un",str(value))
                expr=expr.replace("n",str(i-1))
                value=eval(expr)
                li.update({i:value})
        return li
    return value
