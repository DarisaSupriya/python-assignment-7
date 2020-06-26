#python programe to remove odd index characters in a string
str1="python"
str2=" "
for i in range(len(str1)):
    if(i%2==0):
        str2=str2+str1[i]
print("modified string is:",str2)
