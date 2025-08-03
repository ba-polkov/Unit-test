def get_receipt(burger) -> str:
    receipt = [f'(==== {burger.bun.get_name()} ====)']

    for ingredient in burger.ingredients:
        receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')

    receipt.append(f'(==== {burger.bun.get_name()} ====)\n')
    receipt.append(f'Price: {burger.get_price()}')
    return '\n'.join(receipt)
