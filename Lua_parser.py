from ply import yacc
from Lua_lex import tokens, lexer

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)

def p_grammar(_):
    '''
    chunk :  command_list

    command_list : command command_list
              | empty

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
          
    
    actual_arg_exp : actual_args
                   | empty
                   
    actual_args : exp ',' actual_args
                | exp
    
    expassign    : empty
                 | '=' exp
                 
    explist    : lexp
               | empty
    
    lexp    : ID
            | ID ',' lexp 
    
    exp_list : exp
             | empty
             
    exp    : NUMBER
           | ID
           | exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp LESSEQUAL exp
           | exp GREATEREQUAL exp
           | exp LESS exp
           | exp GREATER exp
           | exp EQUAL exp
           | exp NOTEQUAL exp
           | MINUS exp %prec UMINUS 
           | '(' exp ')' 
           | ID '(' actual_arg_exp ')'
            
    '''
    pass

def p_empty(p):
    'empty :'
    pass


def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()