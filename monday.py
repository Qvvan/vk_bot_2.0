def schedule(time1, para, k):
    if time1 == '9:25' and para[1] == 1:
        if k == 1:
            return 1, 0
        else: return 0, 0
    elif time1 == '9:26':
        return 0, 1
    elif time1 == '11:15' and para[2] == 1:
        if k == 1:
            return 2, 0
        else: return 0, 0
    elif time1 == '11:16':
        return 0, 1
    elif time1 == '13:5' and para[3] == 1:
        if k == 1:
            return 3, 0
        else: return 0, 0
    elif time1 == '13:6':
        return 0, 1
    elif time1 == '15:20' and para[4] == 1:
        if k == 1:
            return 4, 0
        else: return 0, 0
    elif time1 == '15:21':
        return 0, 1
    elif time1 == '17:10' and para[5] == 1:
        if k == 1:
            return 5, 0
        else: return 0, 0
    elif time1 == '17:11':
        return 0, 1
    else: return 0, 1

