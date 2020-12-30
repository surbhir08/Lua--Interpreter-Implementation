#!/usr/bin/env python
# Lua interpreter
import sys
from argparse import ArgumentParser
from Lua_lex import lexer
from Lua_frontend import parser
from Lua_state import state
from Lua_interp_walk import walk
from grammar_stuff import dump_AST

def interp(input_stream):
    sys.tracebacklimit = 0
    # initialize the state object
    state.initialize()

    # build the AST
    parser.parse(input_stream, lexer=lexer)
    #print('AST',state.AST)
    # walk the AST
    #dump_AST(state.AST)
    walk(state.AST)
'''
if __name__ == "__main__":
    # parse command line args
    aparser = ArgumentParser()
    aparser.add_argument('input')

    args = vars(aparser.parse_args()

    f = open(args['input'], 'r')
    input_stream = f.read()
    f.close()

    # execute interpreter
    interp(input_stream=input_stream)
'''

'''
a = 1
while (a <= 5) 
do
 print (a)
 a = a+1
 end
'''
'''
x = 5
y = 1

while (1 <= x) 
do
      y = (y * x);
      x = (x - 1);
end 
print (y)


'''
'''
if (12 < 11) then 
return 9 
else 
return 12 
end
'''
'''
fact = 1
for i = 1, 10
do 
fact = fact * i
i = i+1
end
return fact 

'''
'''
function x_value(n)
    x = 2
    z = n / x
    print(z)
end
a = 4
x_value(a)
'''
'''
a = 1
while a < 5 do
print (a)
a = a+1
end 
'''
'''
input_stream= \

fact = 1
for i = 1, 10
do 
fact = fact * i
i = i+1
end
return fact 


interp(input_stream)
'''
