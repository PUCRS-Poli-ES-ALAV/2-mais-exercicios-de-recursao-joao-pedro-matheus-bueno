
def findSubStr(str, match):
    if(len(str) < len(match)):
        return False
         
    if str[:len(match)] == match:
        return True
    
    return findSubStr(str[1:], match)

# Testando a função com alguns exemplos
print(findSubStr("hello world", "world"))  # True
print(findSubStr("hello world", "hello"))  # True
print(findSubStr("hello world", "abc"))    # False