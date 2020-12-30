from ply import yacc
from Lua_lex import tokens , lexer, is_ID
from Lua_state import state

# set precedence and associativity
# NOTE: all operators need to have tokens
# so that we can put them into the precedence table

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)
#########################################################################
# grammar rules with embedded actions
#########################################################################

def p_chunk(p):
    
    '''
    chunk :  command_list
    '''
    
    state.AST = p[1]

#########################################################################
def p_command_list(p):
    '''
    command_list : command command_list
              | empty
    '''
    if (len(p) == 3):
        p[0] = ('seq', p[1], p[2])
    elif (len(p) == 2):
        p[0] = p[1]
    
#########################################################################
def p_command(p):
    '''
    command    : ID '=' exp
               | FUNCTION ID '(' explist ')' command_list END
               | FUNCTION ID expassign
               | ID '(' actual_arg_exp ')'
               | WHILE '(' exp ')' command
               | IF '(' exp ')' THEN command_list ELSE command_list END
               | RETURN exp_list
               | DO command_list END
               | FOR command ',' exp command 
               | PRINT '(' exp ')'
               | '{' command_list '}'
    '''
    if is_ID(p[1]) and p[2] == '=':
        p[0] = ('assign', p[1], p[3])
    elif p[1] == 'function' and p[3] == '(':
        p[0] = ('fundecl', p[2], p[4], p[6])
    elif p[1] == 'function':
        p[0] = ('function', p[2], p[3])
    elif is_ID(p[1]) and p[2] == '(':
        p[0] = ('callstmt', p[1], p[3])
    elif p[1] == 'return':
        p[0] = ('return', p[2])
    elif p[1] == 'while':
        p[0] = ('while', p[3], p[5])
    elif p[1] == 'if':
        p[0] = ('if', p[3], p[6], p[8])
    elif p[1] == 'print':
        p[0] = ('print', p[3])
    elif p[1] == 'do':
        p[0] = ('do', p[2])
    elif p[1] == 'for':
        p[0] = ('for', p[2], p[4], p[5])
    elif p[1] == '{':
        p[0] = ('block', p[2])
    else:
        raise ValueError("unexpected symbol {}".format(p[1]))
        
#########################################################################
def p_exp(p):
    
    '''
    exp    : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp LESSEQUAL exp
           | exp GREATEREQUAL exp
           | exp LESS exp
           | exp GREATER exp
           | exp EQUAL exp
           | exp NOTEQUAL exp           
    '''  
           
    p[0] = (p[2], p[1], p[3])
    
#########################################################################
def p_paren_exp(p):
    '''
    exp : '(' exp ')'
    '''
    p[0] = ('paren', p[2]) 
    
#########################################################################
    
def p_unary_exp(p):
    '''
    exp : MINUS exp %prec UMINUS
    '''
    p[0] = ('uminus',p[2])
      
#########################################################################
   
def p_call_exp(p):
    '''
    exp : ID '(' actual_arg_exp ')'
    '''
    p[0] = ('callexp', p[1], p[3])
   

    
#########################################################################    
def p_number_exp(p):
    '''
    exp : NUMBER
    '''
    p[0] = ('number', int(p[1]))

#########################################################################
def p_id_exp(p):
    '''
    exp : ID
    '''
    p[0] = ('id', p[1])
       
#########################################################################
def p_actual_args(p):
    '''
    actual_arg_exp : actual_args
                   | empty
    '''
    p[0] = p[1]
    
#########################################################################                  
def p_actual_passed_args(p):
    '''
    actual_args : exp ',' actual_args
                | exp
    '''
    
    if (len(p) == 4):
        p[0] = ('seq', p[1], p[3])
    else:
        p[0] = ('seq', p[1], ('nil',))
        
#########################################################################

def p_return_exp(p):
    '''
    exp_list : exp
             | empty
    '''
    p[0] = p[1]
    
#########################################################################
def p_expassign(p):
    '''
    expassign    : empty
                 | '=' exp
    '''
    if p[1] == '=':
        p[0] = p[2]
    else:
        p[0] = p[1]
        
#########################################################################
def p_explist(p):
    
    '''
    explist    : empty
               | lexp 
    '''

    p[0] = p[1]
        
#########################################################################
def p_lexp(p):
    '''
    lexp    : ID
            | ID ',' lexp 
    '''
    if (len(p) == 4):
        p[0] = ('seq',('id', p[1]), p[3])
    else :
        p[0] = ('seq',('id', p[1]), ('nil',))
        
#########################################################################
   
def p_empty(p):
    '''
    empty :
    '''
    p[0] = ('nil',)
    
#########################################################################
def p_error(p):
    print("Syntax error in input", p )
    
    
#########################################################################
# Building parser

parser = yacc.yacc(debug=False,tabmodule='lua_parser_tab')