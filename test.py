"32 16 8 4 2 1"

#AND
a=10 #1010
b=7  #0111
  #&=#0010
print(a&b)
#OR
a=6 #0110
b=9 #1010
#|=#1111
print(a|b)

#XOR
a=7 #0111
b=8 #1000
#^=#1111
print(a^b)

#complement 
a=11 #1011
#~a=-1011
#-(1011+1)
#-(1100)
print(~a) 

#lift shift
A=10 #1010
#A<<2 = 1010<<
#101000
#output=40 
print(A<<2)

#Right shift
a=10 #=>1010 (Binary)
#a>>2 = 1010>>2
# 10
#2(Decimal)
print(a>>2)