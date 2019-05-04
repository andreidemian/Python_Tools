### String Compress ###
def compress(string="jjjsklakkkkallJSJAAAAkKSC"):
    compressed_string = string[0]
    count = 1
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count += 1
        else:
            if(count > 1):
                compressed_string += str(count)
            compressed_string += string[i+1]
            count = 1
    if(count > 1):
        compressed_string += str(count)
    return compressed_string