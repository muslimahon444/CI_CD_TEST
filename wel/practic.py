def ball(name,prd,ball):
    j ={'name':name,'prd':prd,'ball':ball,}
    return j
print(ball('Sara','cricket',100))
print(ball('Dhoni','cricket',50))
print(ball('Virat','cricket',70))

def code(x):
    for o in x:
        if o == int(x):
            res = x*2
            return res
        else:
            print(x)

print(code(6))

def zero(h):
    return h / 0
print(zero(5))

    

