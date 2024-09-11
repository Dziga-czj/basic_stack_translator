# jinjer_ctf_tools
A repository regrouping all my ctf tools I made.


# Index 
- [stack_translator.py](#stack_translatorpy)



## stack_translator.py
stack_translator tool by Jinjer  
used for ctfs to translate the stack, that you retrieve with for example string format bugs etc.  
can also be used as a hex translator  

#### usage : 
```
$ python3 stack_translator.py [options] [stack_string]
```
#### options :
`-s` : shuffle mode to get strings with possible shifts in the stack  
`-d <char>` : delimiter used in the stack  
`-h` : show help message

