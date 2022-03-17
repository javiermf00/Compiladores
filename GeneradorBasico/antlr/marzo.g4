grammar marzo;

program: expression+ | statement+ | comparation+ | ifstatement+;

expression:
	expression '+' expression	# suma
	| expression '-' expression	# resta
	| '(' expression ')'		# parens
	| Numero					# primaria
	| Variable					# var;

statement:
	'int' Variable			# declaracion
	| Variable '=' Numero	# asignacion
	| 'print' Numero		# printint;

comparation:
	Numero '==' Numero	# equals
	| Numero '<' Numero	# less
	| Numero '>' Numero	# bigg;

ifstatement:
	'if' comparation '{' statement '}'								# if
	| 'if' comparation '{' statement '}' 'else' '{' statement '}'	# ifelse;

Numero: [0-9]+;
Variable: [a-z]+;
WS: [ \t\n\r]+ -> skip;
