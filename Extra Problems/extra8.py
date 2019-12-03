def greaterInt(int1, int2):
    if int1 > int2:
        return int1
    else:
        return int2

def greater3(int1, int2, int3):
    if greaterInt(int1, int2) < int3:
        return int3
    else:
        return greaterInt(int1, int2)

def greater4(int1, int2, int3, int4):
    if greaterInt(int1, int2) > greaterInt(int3, int4):
        return greaterInt(int1, int2)
    else:
        return greaterInt(int3, int4)
