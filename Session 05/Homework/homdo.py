inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
print()

inventory['backpack'].remove('dagger')
print(inventory)
print()

inventory['gold'] += 50
print(inventory['gold'])
print()