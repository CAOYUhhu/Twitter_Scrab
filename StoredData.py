#判断变量有没有在矩阵内，如果有，则返回true，否则返回false,并写入json文件

def is_included(variable, matrix):
    if variable in matrix:
        result = True
    else:
        result = False
    return result