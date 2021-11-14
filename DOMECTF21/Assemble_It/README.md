# Short WriteUp - Assemble It

## Description
> I just found a USB stick, which contains some secret information and it seems this code contains the key to unlock. Can you figure it out?

## Solution
This challenge was based on python disassembly, the solution would be to manually decompile and understand the program.
Then writing a decrypt function would get the flag.

This was a fun challenge, the challenge had 3 files in total
- python disassmebly of function rotate()
- python disassembly of function encrypt()
- Encrypted flag

Here is the documentation to the python disassembly, 
https://docs.python.org/3/library/dis.html

Try checking into the co_consts, co_varnames, etc, it would be help to understand the disassembly better.

*always read the docs*

The whole operation is based on a stack structure. Any function call or arithmatic operation happens via the stack, push and pop.

## Disassembly 1 - function rotate(message)

This was the given disassembly, 

```python
  7           0 LOAD_CONST               1 ('')
              2 STORE_FAST               1 (rot)

  8           4 LOAD_GLOBAL              0 (len)
              6 LOAD_FAST                0 (message)
              8 CALL_FUNCTION            1
             10 LOAD_CONST               2 (1)
             12 BINARY_SUBTRACT
             14 STORE_FAST               2 (i)

 10     >>   16 LOAD_FAST                2 (i)
             18 LOAD_CONST               3 (0)
             20 COMPARE_OP               5 (>=)
             22 POP_JUMP_IF_FALSE       46

 11          24 LOAD_FAST                1 (rot)
             26 LOAD_FAST                0 (message)
             28 LOAD_FAST                2 (i)
             30 BINARY_SUBSCR
             32 BINARY_ADD
             34 STORE_FAST               1 (rot)

 12          36 LOAD_FAST                2 (i)
             38 LOAD_CONST               2 (1)
             40 BINARY_SUBTRACT
             42 STORE_FAST               2 (i)
             44 JUMP_ABSOLUTE           16

 13     >>   46 LOAD_FAST                1 (rot)
             48 RETURN_VALUE
```

Here is the mapping of every python line and its disassembly

```
  7           0 LOAD_CONST               1 ('')
              2 STORE_FAST               1 (rot)
```
```python
rot = ''
```

The right hand side would be the below python code with `message` being a parameter to the function `rotate()`
```
  8           4 LOAD_GLOBAL              0 (len)
              6 LOAD_FAST                0 (message)
              8 CALL_FUNCTION            1
```
```python
len(message)
```

Since currently in our stack, we have the result of `len(message)`, `BINARY_SUBTRACT` will pop `1` and that result off the stack and subtract both
```
             10 LOAD_CONST               2 (1)
             12 BINARY_SUBTRACT
             14 STORE_FAST               2 (i)
```
```python
len(message) - 1
```

This would store the top of the stack into the variable `i`, so essentially the code would be,
```
             14 STORE_FAST               2 (i)
```
```python
i = len(message) - 1
```

This whole block would be a `while` loop
```
 10     >>   16 LOAD_FAST                2 (i)
             18 LOAD_CONST               3 (0)
             20 COMPARE_OP               5 (>=)
             22 POP_JUMP_IF_FALSE       46

 11          24 LOAD_FAST                1 (rot)
             26 LOAD_FAST                0 (message)
             28 LOAD_FAST                2 (i)
             30 BINARY_SUBSCR
             32 BINARY_ADD
             34 STORE_FAST               1 (rot)

 12          36 LOAD_FAST                2 (i)
             38 LOAD_CONST               2 (1)
             40 BINARY_SUBTRACT
             42 STORE_FAST               2 (i)
             44 JUMP_ABSOLUTE           16
```

This would be the entry check of the loop, essentially being,
```
 10     >>   16 LOAD_FAST                2 (i)
             18 LOAD_CONST               3 (0)
             20 COMPARE_OP               5 (>=)
             22 POP_JUMP_IF_FALSE       46
```
```python
while i >= 0
```

`BINARY_SUBSCR` does indexing on the variable `message` with `i` as the index
```
             26 LOAD_FAST                0 (message)
             28 LOAD_FAST                2 (i)
             30 BINARY_SUBSCR
```
```python
message[i]
```

The following lines can be decompiled similarly to,
```
 11          24 LOAD_FAST                1 (rot)
             26 LOAD_FAST                0 (message)
             28 LOAD_FAST                2 (i)
             30 BINARY_SUBSCR
             32 BINARY_ADD
             34 STORE_FAST               1 (rot)

 12          36 LOAD_FAST                2 (i)
             38 LOAD_CONST               2 (1)
             40 BINARY_SUBTRACT
             42 STORE_FAST               2 (i)
```
```python
rot = rot + message[i]
i -= 1
```

Finally, the whole decompilation would be,
```python
def rotate(message):
    rot = ''
    i = len(message) - 1
    while(i >= 0):
        rot = rot + message[i]
        i -= 1
    return rot
```

## Disassembly 2 - function `encrypt(text)`

Similar to the first disassembly the following can be decompiled as such, 
```python
 20           0 LOAD_CONST               1 ('')
              2 STORE_FAST               1 (flag)

 21           4 LOAD_CONST               2 ('secret')
              6 STORE_FAST               2 (key)

 22           8 BUILD_LIST               0
             10 STORE_FAST               3 (encrypt_text)

 23          12 LOAD_GLOBAL              0 (list)
             14 LOAD_GLOBAL              1 (rotate)
             16 LOAD_FAST                0 (text)
             18 CALL_FUNCTION            1
             20 CALL_FUNCTION            1
             22 GET_ITER
        >>   24 FOR_ITER                24 (to 50)
             26 STORE_FAST               4 (i)

 24          28 LOAD_FAST                1 (flag)
             30 LOAD_GLOBAL              2 (chr)
             32 LOAD_GLOBAL              3 (ord)
             34 LOAD_FAST                4 (i)
             36 CALL_FUNCTION            1
             38 LOAD_CONST               3 (1)
             40 BINARY_LSHIFT
             42 CALL_FUNCTION            1
             44 INPLACE_ADD
             46 STORE_FAST               1 (flag)
             48 JUMP_ABSOLUTE           24

 26     >>   50 LOAD_GLOBAL              4 (len)
             52 LOAD_FAST                1 (flag)
             54 CALL_FUNCTION            1
             56 STORE_FAST               5 (K)

 27          58 LOAD_FAST                2 (key)
             60 LOAD_FAST                5 (K)
             62 LOAD_GLOBAL              4 (len)
             64 LOAD_FAST                2 (key)
             66 CALL_FUNCTION            1
             68 BINARY_FLOOR_DIVIDE
             70 LOAD_CONST               3 (1)
             72 BINARY_ADD
             74 BINARY_MULTIPLY
             76 LOAD_CONST               0 (None)
             78 LOAD_FAST                5 (K)
             80 BUILD_SLICE              2
             82 BINARY_SUBSCR
             84 STORE_FAST               6 (newKey)

 29          86 LOAD_GLOBAL              5 (zip)
             88 LOAD_FAST                1 (flag)
             90 LOAD_FAST                6 (newKey)
             92 CALL_FUNCTION            2
             94 GET_ITER
        >>   96 FOR_ITER                50 (to 148)
             98 STORE_FAST               4 (i)

 30         100 LOAD_GLOBAL              0 (list)
            102 LOAD_FAST                4 (i)
            104 CALL_FUNCTION            1
            106 STORE_FAST               4 (i)

 32         108 LOAD_GLOBAL              2 (chr)
            110 LOAD_GLOBAL              3 (ord)
            112 LOAD_FAST                4 (i)
            114 LOAD_CONST               4 (0)
            116 BINARY_SUBSCR
            118 CALL_FUNCTION            1
            120 LOAD_GLOBAL              3 (ord)
            122 LOAD_FAST                4 (i)
            124 LOAD_CONST               3 (1)
            126 BINARY_SUBSCR
            128 CALL_FUNCTION            1
            130 BINARY_ADD
            132 CALL_FUNCTION            1
            134 STORE_FAST               7 (a)

 33         136 LOAD_FAST                3 (encrypt_text)
            138 LOAD_METHOD              6 (append)
            140 LOAD_FAST                7 (a)
            142 CALL_METHOD              1
            144 POP_TOP
            146 JUMP_ABSOLUTE           96

 34     >>  148 LOAD_CONST               1 ('')
            150 LOAD_METHOD              7 (join)
            152 LOAD_FAST                3 (encrypt_text)
            154 LOAD_CONST               0 (None)
            156 LOAD_CONST               0 (None)
            158 BUILD_SLICE              2
            160 BINARY_SUBSCR
            162 CALL_METHOD              1
            164 STORE_FAST               3 (encrypt_text)

 35         166 LOAD_FAST                3 (encrypt_text)
            168 RETURN_VALUE

```

Decompiled code, 
```python
def encrypt(text):
    flag = ''
    key = 'secret'
    encrypt_text = []

    for i in list(rotate(text)):
        flag += chr(ord(i) << 1) # multiplies by 2

    K = len(flag)
    newKey = (key * ((K // len(key)) + 1))[:K]


    for i in list(zip(newKey, flag)):
        a = chr(ord(i[0]) + ord(i[1]))
        encrypt_text.append(a)

    encrypt_text = ''.join(encrypt_text)
```

## Reversed encryption

Here is the function which can reverse the encryption performed,
```python
def decrypt(text):
    key = 'secret'
    K = len(text)
    newKey = (key * ((K // len(key)) + 1))[:K]
    print(newKey)
    

    a = []
    for i in range(len(text)):
        t1 = ord(text[i]) - ord(newKey[i])
        t1 = t1 // 2
        a.append(t1)

    return a
```

running this will give us the flag,

Flag: `domectf{14131074456096369141775717192087}`
