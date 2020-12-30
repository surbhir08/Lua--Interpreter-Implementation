from Lua_state import state
from grammar_stuff import assert_match


 # Use the exception mechanism to return values from function calls
#########################################################################
class ReturnValue(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))

#########################################################################
def len_seq(seq_list):

    if seq_list[0] == 'nil':
        return 0

    elif seq_list[0] == 'seq':
        # unpack the seq node
        (SEQ, p1, p2) = seq_list

        return 1 + len_seq(p2)

    else:
            raise ValueError("unknown node type: {}".format(seq_list[0]))

#########################################################################
def eval_actual_args(args):

    if args[0] == 'nil':
        return ('nil',)

    elif args[0] == 'seq':
        # unpack the seq node
        (SEQ, p1, p2) = args

        val = walk(p1)

        return ('seq', val, eval_actual_args(p2))

    else:
        raise ValueError("unknown node type: {}".format(args[0]))

#########################################################################
def declare_formal_args(formal_args, actual_val_args):

    if len_seq(actual_val_args) != len_seq(formal_args):
        raise ValueError("actual and formal argument lists do not match")

    if formal_args[0] == 'nil':
        return

    # unpack the args
    (SEQ, (ID, sym), p1) = formal_args
    (SEQ, val, p2) = actual_val_args

    # declare the variable
    state.symbol_table.declare_scalar(sym, val)

    declare_formal_args(p1, p2)

#########################################################################
def handle_call(name, actual_arglist):

    (type, val) = state.symbol_table.lookup_sym(name)

    if type != 'function':
        raise ValueError("{} is not a function".format(name))

    # unpack the funval tuple
    (FUNVAL, formal_arglist, body, context) = val

    if len_seq(formal_arglist) != len_seq(actual_arglist):
        raise ValueError("function {} expects {} arguments".format(name, len_seq(formal_arglist)))

    # set up the environment for static scoping and then execute the function
    actual_val_args = eval_actual_args(actual_arglist)   # evaluate actuals in current symtab
    save_symtab = state.symbol_table.get_config()        # save current symtab
    state.symbol_table.set_config(context)               # make function context current symtab
    state.symbol_table.push_scope()                      # push new function scope
    declare_formal_args(formal_arglist, actual_val_args) # declare formals in function scope

    return_value = None
    try:
        walk(body)                                       # execute the function
    except ReturnValue as val:
        return_value = val.value

    # NOTE: popping the function scope is not necessary because we
    # are restoring the original symtab configuration
    state.symbol_table.set_config(save_symtab)           # restore original symtab config

    return return_value

#########################################################################
# node functions
#########################################################################

def seq(node):

    (SEQ, command, command_list) = node
    assert_match(SEQ, 'seq')

    walk(command)
    walk(command_list)
    
#########################################################################

def nil(node):
    
    (NIL,) = node
    assert_match(NIL, 'nil')
    
    # do nothing!
    pass

#########################################################################
def fundecl_stmt(node):

    try: # try the fundecl pattern without arglist
        (FUNDECL, name, (NIL,), body) = node
        assert_match(FUNDECL, 'fundecl')
        assert_match(NIL, 'nil')

    except ValueError: # try fundecl with arglist
        (FUNDECL, name, arglist, body) = node
        assert_match(FUNDECL, 'fundecl')

        context = state.symbol_table.get_config()
        funval = ('funval', arglist, body, context)
        state.symbol_table.declare_fun(name, funval)

    else: # fundecl pattern matched
        # no arglist is present
        context = state.symbol_table.get_config()
        funval = ('funval', ('nil',), body, context)
        state.symbol_table.declare_fun(name, funval)


#########################################################################
def declare_stmt(node):

    try: # try the declare pattern without initializer
        (FUNCTION, name, (NIL,)) = node
        assert_match(FUNCTION, 'function')
        assert_match(NIL, 'nil')

    except ValueError: # try declare with initializer
        (FUNCTION, name, init_val) = node
        assert_match(FUNCTION, 'FUNCTION')

        value = walk(init_val)
        state.symbol_table.declare_scalar(name, value)

    else: # declare pattern matched
        # when no initializer is present we init with the value 0
        state.symbol_table.declare_scalar(name, 0)

#########################################################################

def assign_stmt(node):

    (ASSIGN, name, exp) = node
    assert_match(ASSIGN, 'assign')
    value = walk(exp)
    try:
        state.symbol_table.update_sym(name, ('scalar', value))
    except ValueError:
        state.symbol_table.declare_scalar(name,0)
        state.symbol_table.update_sym(name, ('scalar', value))
    #print(state.symbol_table)
    

#########################################################################

def print_stmt(node):
    (PRINT, exp) = node
    assert_match(PRINT, 'print')

    value = walk(exp)
    print("> {}".format(value))
        
#########################################################################
def call_stmt(node):

    (CALLSTMT, name, actual_args) = node
    assert_match(CALLSTMT, 'callstmt')

    handle_call(name, actual_args)

#########################################################################
def return_stmt(node):
    (RETURN, exp) = node
    assert_match(RETURN, 'return')

    value = walk(exp)
    print("> {}".format(value))

#########################################################################
def while_stmt(node):

    (WHILE, cond, body) = node
    assert_match(WHILE, 'while')
    
    value = walk(cond)
    while value != 0:
        walk(body)
        value = walk(cond)
        
#########################################################################
def if_stmt(node):
    
    (IF, cond, then_stmt, else_stmt) = node
    assert_match(IF, 'if')

    value = walk(cond)
    if value != 0:
        walk(then_stmt)
    else:
        walk(else_stmt)
    return

#########################################################################
def block_stmt(node):

    (BLOCK, command_list) = node
    assert_match(BLOCK, 'block')

    state.symbol_table.push_scope()
    walk(command_list)
    state.symbol_table.pop_scope()

#########################################################################  

def do_list(node):
    (DO, command_list) = node
    assert_match(DO, 'do')

    state.symbol_table.push_scope()
    walk(command_list)
    state.symbol_table.pop_scope()

#########################################################################  

def for_stmt(node):
    (FOR, cond, range_exp, body) = node
    assert_match(FOR, 'for')

    int_value = walk(cond)
    range_val = walk(range_exp)
    for int_value in range(range_val):
        walk(body)

    return

#########################################################################  

def then_list(node):
    (THEN, command_list, elsestmt) = node
    assert_match(THEN, 'then')

    state.symbol_table.push_scope()
    walk(command_list)
    walk(elsestmt)
    state.symbol_table.pop_scope()

#########################################################################    
def plus_exp(node):
    
    (PLUS,c1,c2) = node
    assert_match(PLUS, '+')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 + v2

#########################################################################
def minus_exp(node):
    
    (MINUS,c1,c2) = node
    assert_match(MINUS, '-')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 - v2

#########################################################################
def times_exp(node):
    
    (TIMES,c1,c2) = node
    assert_match(TIMES, '*')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 * v2

#########################################################################
def divide_exp(node):
    
    (DIVIDE,c1,c2) = node
    assert_match(DIVIDE, '/')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 // v2

#########################################################################
def eq_exp(node):
    
    (EQUAL,c1,c2) = node
    assert_match(EQUAL, '==')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 == v2 else 0

#########################################################################
def le_exp(node):
    
    (LESSEQUAL,c1,c2) = node
    assert_match(LESSEQUAL, '<=')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 <= v2 else 0

#########################################################################
def gr_exp(node):
    
    (GREATEREQUAL,c1,c2) = node
    assert_match(GREATEREQUAL, '>=')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 >= v2 else 0

#########################################################################
def less_exp(node):
    
    (LESS,c1,c2) = node
    assert_match(LESS, '<')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 < v2 else 0

#########################################################################
def greater_exp(node):
    
    (GREATER,c1,c2) = node
    assert_match(GREATER, '>')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 > v2 else 0

#########################################################################
def not_eq_exp(node):
    
    (NOTEQUAL,c1,c2) = node
    assert_match(NOTEQUAL, '!=')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 != v2 else 0

#########################################################################
def number_exp(node):

    (NUMBER, value) = node
    assert_match(NUMBER, 'number')
    
    return value

#########################################################################
def id_exp(node):
    
    (ID, name) = node
    assert_match(ID, 'id')
    #print(state.symbol_table)
    (type, val) = state.symbol_table.lookup_sym(name)
    #print(state.symbol_table.lookup_sym(name))
    if type != 'scalar':
        raise ValueError("{} is not a scalar".format(name))

    return val

#########################################################################
def call_exp(node):
    # call_exp works just like call_stmt with the exception
    # that we have to pass back a return value

    (CALLEXP, name, args) = node
    assert_match(CALLEXP, 'callexp')

    return_value = handle_call(name, args)

    if return_value is None:
        raise ValueError("No return value from function {}".format(name))

    return return_value

#########################################################################
def uminus_exp(node):
    
    (UMINUS, exp) = node
    assert_match(UMINUS, 'uminus')
    
    val = walk(exp)
    return - val

#########################################################################
def not_exp(node):
    
    (NOT, exp) = node
    assert_match(NOT, 'not')
    
    val = walk(exp)
    return 0 if val != 0 else 1

#########################################################################
def paren_exp(node):
    
    (PAREN, exp) = node
    assert_match(PAREN, 'paren')
    
    # return the value of the parenthesized expression
    return walk(exp)


#########################################################################
# walk
#########################################################################

def walk(node):
    # node format: (TYPE, [child1[, child2[, ...]]])
    type = node[0]

    if type in dispatch_dict:
        node_function = dispatch_dict[type]
        return node_function(node)
    else:
        raise ValueError("walk: unknown tree node type: " + type)


# a dictionary to associate tree nodes with node functions
dispatch_dict = {
    'seq': seq,
    'nil': nil,
    'fundecl' : fundecl_stmt,
    'function' : declare_stmt,
    'assign'  : assign_stmt,
    'callstmt': call_stmt,
    'print' : print_stmt,
    'return' : return_stmt,
    'while': while_stmt,
    'do'   : do_list,
    'for'  : for_stmt,
    'if': if_stmt,
    'number': number_exp,
    'id': id_exp,
    'paren': paren_exp,
    '+': plus_exp,
    '-': minus_exp,
    '*': times_exp,
    '/': divide_exp,
    '==': eq_exp,
    '<=': le_exp,
    '>=' : gr_exp,
    '<' : less_exp,
    '>' : greater_exp,
    '!=' : not_eq_exp,
    'uminus': uminus_exp,
    'not': not_exp,
    'callexp' : call_exp,
    'block' : block_stmt,   
    }