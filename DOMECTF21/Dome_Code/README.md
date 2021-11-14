# Short WriteUp -- Dome Code

## Description

> A New Type of code is in town time to crack it. And the green is 101 !!!

## Solution

The challenge file given was a picture, and apparantly the clue given gave the idea of solving it using the hex codes of colors.

*i did try hexahue tho, sadly did not work out*

The challenge had the color encodings mapped, like green as 101 considering that in binary, we can produce every other color match with the same concept, we can get the following binary pattern,
```
r = "011"
g = "101"
b = "110"
y = "001"
p = "010"
c = "100"
bl= "111"
w = "000" 
```

Mapping the colors from the image we get,
```
r=y=w=b=bl=g=g=g=r=y=p=b=y=g=b=c=r=y=c=bl=g=g=b=y=p=r=b=c=c=w=b=p=p=w=p=g=w=g=b=bl=r=w=b=c=p=y=c=r=p=w=b=c=y=y=y=w=r=g=p=g=y=y=w=g=p=r=w=c=y=g=p=p=p=r=b=b=b=y=p=c=p=r=w=bl=w=g=y=r=r=y=b=bl=c=g=c=g=p=r=w=c=g=g=bl=w=r=y=c=bl=b=c=bl=bl=bl=bl=bl=bl=bl=bl=bl=bl=bl=bl
```

Convert all those to binary and u get, 
```
011001000110111101101101011001010110001101110100011001100111101101110001010011110100100000110010010000010101000101110111011000110100010001100011010000110100001001001000011101010101001001000101010011000100001101010010010011110110110001010100010011000111000101001011011001110111100101100101010011000100101101111000011001100111110100111111111111111111111111111111111111
```

Convert to ascii, and we get the flag,

Flag: `domectf{qOH2AQwcDcCBHuRELCROlTLqKgyeLKxf}`
