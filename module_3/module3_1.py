calls = 0


def counts_calls():
    global calls
    calls += 1


def string_info(string):
    counts_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    counts_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)