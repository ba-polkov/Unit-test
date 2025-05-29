const = {
'TESTS_DATA_BUN' : ('black bun', 100),
'TESTS_DATA_INGREDIENT' : ('SAUCE', 'hot sauce', 100),
'TESTS_DATA_INGREDIENT_2' : ('FILLING', 'cutlet', 100),
'TESTS_DATA_BURGER' :  [ [], [('SAUCE', 'hot sauce', 100)], [('SAUCE', 'hot sauce', 100), ('FILLING', 'cutlet', 100)] ],
'TESTS_DATA_BURGER_RECEIPT' :  [ [ [], "(==== black bun ====)\n(==== black bun ====)\n\nPrice: 200" ], [ [('SAUCE', 'hot sauce', 100)], "(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 300"  ], [ [('SAUCE', 'hot sauce', 100), ('FILLING', 'cutlet', 100)], "(==== black bun ====)\n= sauce hot sauce =\n= filling cutlet =\n(==== black bun ====)\n\nPrice: 400"  ] ],
}