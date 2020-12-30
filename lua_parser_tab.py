
# lua_parser_tab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftPLUSMINUSleftTIMESDIVIDErightUMINUSDIVIDE DO ELSE END EQUAL FOR FUNCTION GREATER GREATEREQUAL ID IF LESS LESSEQUAL MINUS NOTEQUAL NUMBER PLUS PRINT RETURN THEN TIMES WHILE\n    chunk :  command_list\n    \n    command_list : command command_list\n              | empty\n    \n    command    : ID '=' exp\n               | FUNCTION ID '(' explist ')' command_list END\n               | FUNCTION ID expassign\n               | ID '(' actual_arg_exp ')'\n               | WHILE '(' exp ')' command\n               | IF '(' exp ')' THEN command_list ELSE command_list END\n               | RETURN exp_list\n               | DO command_list END\n               | FOR command ',' exp command \n               | PRINT '(' exp ')'\n               | '{' command_list '}'\n    \n    exp    : exp PLUS exp\n           | exp MINUS exp\n           | exp TIMES exp\n           | exp DIVIDE exp\n           | exp LESSEQUAL exp\n           | exp GREATEREQUAL exp\n           | exp LESS exp\n           | exp GREATER exp\n           | exp EQUAL exp\n           | exp NOTEQUAL exp           \n    \n    exp : '(' exp ')'\n    \n    exp : MINUS exp %prec UMINUS\n    \n    exp : ID '(' actual_arg_exp ')'\n    \n    exp : NUMBER\n    \n    exp : ID\n    \n    actual_arg_exp : actual_args\n                   | empty\n    \n    actual_args : exp ',' actual_args\n                | exp\n    \n    exp_list : exp\n             | empty\n    \n    expassign    : empty\n                 | '=' exp\n    \n    explist    : empty\n               | lexp \n    \n    lexp    : ID\n            | ID ',' lexp \n    \n    empty :\n    "
    
_lr_action_items = {'ID':([0,3,6,9,10,11,13,15,16,17,18,19,20,21,22,23,24,25,26,29,31,36,37,38,39,42,43,44,45,46,47,48,49,50,51,52,54,55,56,58,59,60,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,83,84,85,86,87,88,92,93,95,],[5,5,17,25,5,5,5,25,25,-42,25,25,-10,-34,-35,25,25,-29,-28,25,-4,61,-6,-36,25,25,25,25,25,25,25,25,25,25,25,-26,25,-11,25,-14,-7,25,-37,5,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,5,-13,61,5,-8,5,-27,-12,-5,5,-9,]),'FUNCTION':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[6,6,-42,6,6,6,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,6,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,6,-13,6,-8,6,-27,-12,-5,6,-9,]),'WHILE':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[7,7,-42,7,7,7,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,7,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,7,-13,7,-8,7,-27,-12,-5,7,-9,]),'IF':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[8,8,-42,8,8,8,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,8,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,8,-13,8,-8,8,-27,-12,-5,8,-9,]),'RETURN':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[9,9,-42,9,9,9,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,9,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,9,-13,9,-8,9,-27,-12,-5,9,-9,]),'DO':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[10,10,-42,10,10,10,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,10,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,10,-13,10,-8,10,-27,-12,-5,10,-9,]),'FOR':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[11,11,-42,11,11,11,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,11,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,11,-13,11,-8,11,-27,-12,-5,11,-9,]),'PRINT':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[12,12,-42,12,12,12,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,12,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,12,-13,12,-8,12,-27,-12,-5,12,-9,]),'{':([0,3,9,10,11,13,17,20,21,22,25,26,31,37,38,52,55,58,59,65,66,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,87,88,92,93,95,],[13,13,-42,13,13,13,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,13,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,13,-13,13,-8,13,-27,-12,-5,13,-9,]),'$end':([0,1,2,3,4,9,14,17,20,21,22,25,26,31,37,38,52,55,58,59,65,68,69,70,71,72,73,74,75,76,77,78,81,85,87,88,92,95,],[-42,0,-1,-42,-3,-42,-2,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-13,-8,-27,-12,-5,-9,]),'END':([3,4,9,10,14,17,20,21,22,25,26,27,31,37,38,52,55,58,59,65,68,69,70,71,72,73,74,75,76,77,78,81,84,85,87,88,90,92,93,94,95,],[-42,-3,-42,-42,-2,-42,-10,-34,-35,-29,-28,55,-4,-6,-36,-26,-11,-14,-7,-37,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-13,-42,-8,-27,-12,92,-5,-42,95,-9,]),'}':([3,4,9,13,14,17,20,21,22,25,26,30,31,37,38,52,55,58,59,65,68,69,70,71,72,73,74,75,76,77,78,81,85,87,88,92,95,],[-42,-3,-42,-42,-2,-42,-10,-34,-35,-29,-28,58,-4,-6,-36,-26,-11,-14,-7,-37,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-13,-8,-27,-12,-5,-9,]),'ELSE':([3,4,9,14,17,20,21,22,25,26,31,37,38,52,55,58,59,65,68,69,70,71,72,73,74,75,76,77,78,81,85,86,87,88,91,92,95,],[-42,-3,-42,-2,-42,-10,-34,-35,-29,-28,-4,-6,-36,-26,-11,-14,-7,-37,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-13,-8,-42,-27,-12,93,-5,-9,]),'=':([5,17,],[15,39,]),'(':([5,7,8,9,12,15,16,17,18,19,23,24,25,29,39,42,43,44,45,46,47,48,49,50,51,54,56,60,],[16,18,19,24,29,24,24,36,24,24,24,24,54,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'MINUS':([9,15,16,18,19,21,23,24,25,26,29,31,35,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,57,60,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[23,23,23,23,23,43,23,23,-29,-28,23,43,43,23,43,43,23,23,23,23,23,23,23,23,23,23,-26,43,23,23,43,23,43,-15,-16,-17,-18,43,43,43,43,43,43,-25,43,-27,]),'NUMBER':([9,15,16,18,19,23,24,29,39,42,43,44,45,46,47,48,49,50,51,54,56,60,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),',':([9,17,20,21,22,25,26,28,31,35,37,38,52,55,58,59,61,65,68,69,70,71,72,73,74,75,76,77,78,81,85,87,88,92,95,],[-42,-42,-10,-34,-35,-29,-28,56,-4,60,-6,-36,-26,-11,-14,-7,83,-37,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-13,-8,-27,-12,-5,-9,]),')':([16,25,26,32,33,34,35,36,40,41,52,53,54,57,61,62,63,64,68,69,70,71,72,73,74,75,76,77,78,79,82,87,89,],[-42,-29,-28,59,-30,-31,-33,-42,66,67,-26,78,-42,81,-40,84,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,87,-32,-27,-41,]),'PLUS':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[42,-29,-28,42,42,42,42,-26,42,42,42,-15,-16,-17,-18,42,42,42,42,42,42,-25,42,-27,]),'TIMES':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[44,-29,-28,44,44,44,44,-26,44,44,44,44,44,-17,-18,44,44,44,44,44,44,-25,44,-27,]),'DIVIDE':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[45,-29,-28,45,45,45,45,-26,45,45,45,45,45,-17,-18,45,45,45,45,45,45,-25,45,-27,]),'LESSEQUAL':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[46,-29,-28,46,46,46,46,-26,46,46,46,-15,-16,-17,-18,46,46,46,46,46,46,-25,46,-27,]),'GREATEREQUAL':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[47,-29,-28,47,47,47,47,-26,47,47,47,-15,-16,-17,-18,47,47,47,47,47,47,-25,47,-27,]),'LESS':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[48,-29,-28,48,48,48,48,-26,48,48,48,-15,-16,-17,-18,48,48,48,48,48,48,-25,48,-27,]),'GREATER':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[49,-29,-28,49,49,49,49,-26,49,49,49,-15,-16,-17,-18,49,49,49,49,49,49,-25,49,-27,]),'EQUAL':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[50,-29,-28,50,50,50,50,-26,50,50,50,-15,-16,-17,-18,50,50,50,50,50,50,-25,50,-27,]),'NOTEQUAL':([21,25,26,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,78,80,87,],[51,-29,-28,51,51,51,51,-26,51,51,51,-15,-16,-17,-18,51,51,51,51,51,51,-25,51,-27,]),'THEN':([67,],[86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'chunk':([0,],[1,]),'command_list':([0,3,10,13,84,86,93,],[2,14,27,30,90,91,94,]),'command':([0,3,10,11,13,66,80,84,86,93,],[3,3,3,28,3,85,88,3,3,3,]),'empty':([0,3,9,10,13,16,17,36,54,84,86,93,],[4,4,22,4,4,34,38,63,34,4,4,4,]),'exp_list':([9,],[20,]),'exp':([9,15,16,18,19,23,24,29,39,42,43,44,45,46,47,48,49,50,51,54,56,60,],[21,31,35,40,41,52,53,57,65,68,69,70,71,72,73,74,75,76,77,35,80,35,]),'actual_arg_exp':([16,54,],[32,79,]),'actual_args':([16,54,60,],[33,33,82,]),'expassign':([17,],[37,]),'explist':([36,],[62,]),'lexp':([36,83,],[64,89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> chunk","S'",1,None,None,None),
  ('chunk -> command_list','chunk',1,'p_chunk','Lua_frontend.py',20),
  ('command_list -> command command_list','command_list',2,'p_command_list','Lua_frontend.py',29),
  ('command_list -> empty','command_list',1,'p_command_list','Lua_frontend.py',30),
  ('command -> ID = exp','command',3,'p_command','Lua_frontend.py',40),
  ('command -> FUNCTION ID ( explist ) command_list END','command',7,'p_command','Lua_frontend.py',41),
  ('command -> FUNCTION ID expassign','command',3,'p_command','Lua_frontend.py',42),
  ('command -> ID ( actual_arg_exp )','command',4,'p_command','Lua_frontend.py',43),
  ('command -> WHILE ( exp ) command','command',5,'p_command','Lua_frontend.py',44),
  ('command -> IF ( exp ) THEN command_list ELSE command_list END','command',9,'p_command','Lua_frontend.py',45),
  ('command -> RETURN exp_list','command',2,'p_command','Lua_frontend.py',46),
  ('command -> DO command_list END','command',3,'p_command','Lua_frontend.py',47),
  ('command -> FOR command , exp command','command',5,'p_command','Lua_frontend.py',48),
  ('command -> PRINT ( exp )','command',4,'p_command','Lua_frontend.py',49),
  ('command -> { command_list }','command',3,'p_command','Lua_frontend.py',50),
  ('exp -> exp PLUS exp','exp',3,'p_exp','Lua_frontend.py',80),
  ('exp -> exp MINUS exp','exp',3,'p_exp','Lua_frontend.py',81),
  ('exp -> exp TIMES exp','exp',3,'p_exp','Lua_frontend.py',82),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp','Lua_frontend.py',83),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp','Lua_frontend.py',84),
  ('exp -> exp GREATEREQUAL exp','exp',3,'p_exp','Lua_frontend.py',85),
  ('exp -> exp LESS exp','exp',3,'p_exp','Lua_frontend.py',86),
  ('exp -> exp GREATER exp','exp',3,'p_exp','Lua_frontend.py',87),
  ('exp -> exp EQUAL exp','exp',3,'p_exp','Lua_frontend.py',88),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp','Lua_frontend.py',89),
  ('exp -> ( exp )','exp',3,'p_paren_exp','Lua_frontend.py',98),
  ('exp -> MINUS exp','exp',2,'p_unary_exp','Lua_frontend.py',106),
  ('exp -> ID ( actual_arg_exp )','exp',4,'p_call_exp','Lua_frontend.py',114),
  ('exp -> NUMBER','exp',1,'p_number_exp','Lua_frontend.py',123),
  ('exp -> ID','exp',1,'p_id_exp','Lua_frontend.py',130),
  ('actual_arg_exp -> actual_args','actual_arg_exp',1,'p_actual_args','Lua_frontend.py',137),
  ('actual_arg_exp -> empty','actual_arg_exp',1,'p_actual_args','Lua_frontend.py',138),
  ('actual_args -> exp , actual_args','actual_args',3,'p_actual_passed_args','Lua_frontend.py',145),
  ('actual_args -> exp','actual_args',1,'p_actual_passed_args','Lua_frontend.py',146),
  ('exp_list -> exp','exp_list',1,'p_return_exp','Lua_frontend.py',158),
  ('exp_list -> empty','exp_list',1,'p_return_exp','Lua_frontend.py',159),
  ('expassign -> empty','expassign',1,'p_expassign','Lua_frontend.py',166),
  ('expassign -> = exp','expassign',2,'p_expassign','Lua_frontend.py',167),
  ('explist -> empty','explist',1,'p_explist','Lua_frontend.py',177),
  ('explist -> lexp','explist',1,'p_explist','Lua_frontend.py',178),
  ('lexp -> ID','lexp',1,'p_lexp','Lua_frontend.py',187),
  ('lexp -> ID , lexp','lexp',3,'p_lexp','Lua_frontend.py',188),
  ('empty -> <empty>','empty',0,'p_empty','Lua_frontend.py',199),
]