# stack_reader tool by Jinjer
# used for ctfs to read the stack, with for example string format bugs etc.
# can also be used as a hex translator
# 
# usage : 
# $ python3 stack_reader.py [stack_string]
# 
# options :
# -s : shuffle mode to get strings with possible shifts in the stack
# -d [char] : delimiter used in the stack
# -h : show this help


# used if there is no stack in args
stack = "804b160.804853d.9.bffffbb6.b7e19679.bffffa84.b7fc1000.b7fc1000.804b160.39617044.28293664.6d617045.bf000a64.804861b.2.bffffa84.bffffa90.6dc8d800.bffff9f0.0.0.b7e01fa1.b7fc1000.b7fc1000.0.b7e01fa1.2.bffffa84.bffffa90.bffffa14.1.0.b7fc1000.b7fe771a.b7fff000.0.b7fc1000.0.0.d73d2532.e8f00322.0.0.0.2.8048410.0.b7fecde0.b7fe7970.804a000.2.8048410.0.8048442.8048526.2.bffffa84.80485d0.8048630.b7fe7970.bffffa7c.b7fff940.2.bffffbb6.bffffbbc.0.bffffd72.bffffd9d.bffffdd3.bffffde0.bffffe02.bffffe48.bffffe5b.bffffe70.bffffe8f.bffffeaf.bffffed1.bffffee4.bfffff03.bfffff17.bfffff27.bfffff32.bfffff3a.bfffff52.bfffff71.bfffffee.0.20.b7fd6e5c.21.b7fd6000.10.1f8bfbff.6.1000.11.64.3.8048034.4.20.5.9.7.b7fd8000.8.0.9.8048410.b.451.c.4b5.d.451.e.451.17.1.19.bffffb9b.1a.0.1f.bffffff6.f.bffffbab.0.0.0.0.0.6a000000.626dc8d8.ee269467.5a5db61e.695ab0f3.363836.0.2f2e0000.356863"


import sys

def shuffle(txt) :
    begin = txt[0]
    return (txt[1:]+ begin)

def exit_with_usage() :
    print("usage : python3 stack_reader.py [options] [stack_string]")
    print("options :")
    print("-s : shuffle mode to get strings with possible shifts in the stack")
    print("-d [char] : delimiter used in the stack")
    print("-h : show this help message")
    exit(0)

# handling options

if "-h" in sys.argv :
    exit_with_usage()

delimitor = '.'
delimitor_flag = False
if "-d" in sys.argv :
    delimitor_flag = True
    i = sys.argv.index("-d") + 1
    if len(sys.argv[i]) == 1 :
        delimitor = sys.argv[i]
    else :
        exit_with_usage()

shuffle_flag = False
if "-s" in sys.argv :
    shuffle_flag = True

nb_args = int(delimitor_flag)*2 + int(shuffle_flag)+ 2

argv_length = len(sys.argv)

if len(sys.argv) == nb_args :
    stack = sys.argv[argv_length-1]
# else default is used



# ------ code ------


stack = stack.split(delimitor)
res = []
# formatting the input
for elt in stack :
    elt = "0"*(8-len(elt)) + elt
    temp = []
    for j in range(0,7,2) :
        char = elt[j]+elt[j+1]
        temp.append(char)
    temp.reverse()
    for ch in temp :
        res.append(ch)

txt = ""
for elt in res :
    txt = txt + elt

final = ""

# nb of hex chars that make the encoding
encoding = 2

for i in range(0,len(txt)-1,encoding) :
    c = ""
    for j in range(0,encoding) :
        if not(i+j >= len(txt)) :
            c = c + txt[i+j]
    final = final + chr(int(c,16)%255)

print(final)


# searching for gaps in the stack if there is option -s

if shuffle_flag :
    for j in range(5) :
        res = ""
        for i in range(0,len(stack)-1,2) :
            res = res + chr(int(stack[i]+stack[i+1], 16))
        print(f'nb {j}:\n\n\n\n"{res}"')
        stack = shuffle(stack)


    res = ""
    for i in range(0,len(stack)-1,2) :
        res = res + chr(int(stack[i]+stack[i+1], 16))

    f = res[0]
    for i in range(1,len(res)-1,2) :
        f = f + res[i+1] + res[i]


    print(f)