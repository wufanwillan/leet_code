def kmpmatch(m,n,pnext):
    i,j=0,0
    lm,ln=len(m),len(n)
    while i<lm and j<ln:
        if j==-1 or m[i]==n[j]:
            i+=1
            j+=1
        else:
            j=pnext[j]
    if j==ln:
        return i-j
    return -1

def generate_table(n):
    ln=len(n)
    i,k=0,-1
    pnext=[-1]*ln
    while i<ln-1:
        if k==-1 or n[i]==n[k]:
            i+=1
            k+=1
            pnext[i]=k
        else:
            k=pnext[k]
    return pnext
