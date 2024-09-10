# jinjer_ctf_tools
A repository regrouping all my ctf tools I made.


# Index 
- [stack_reader.py](#stack_readerpy)



## stack_reader.py
stack_reader tool by Jinjer  
used for ctfs to read the stack, with for example string format bugs etc.  
can also be used as a hex translator  

#### usage : 
```
$ python3 stack_reader.py [stack_string]
```
#### options :
`-s` : shuffle mode to get strings with possible shifts in the stack  
`-d [char]` : delimiter used in the stack  
`-h` : show help message

