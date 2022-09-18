def split_name(name):
	first_name, last_name = name.split(maxsplit=1)
	return {
		'first_name': first_name,
		'last_name': last_name,
	}

def is_palindrome(item):
	str_item = str(item)
	return str_item == str_item[::-1]

def build_list(item, count=1):
	items = []
	for _ in range(count):
		items.append(item)
	return items
	


# ASSERT SECTION -----------------------

# split name
assert split_name("Kevin Bacon") == {
	"first_name":"Kevin",
	"last_name":"Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"
assert split_name("Victor Von Doom") == {
	"first_name":"Victor",
	"last_name":"Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

# is palindrome
assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# build list
assert build_list("Apple",3) == [
	"Apple",
	"Apple",
	"Apple",
], f"Expected ['Apple','Apple','Apple'] but got {repr(build_list('Apple',3))}"
assert build_list("Orange") == [
	"Orange"
], f"Expected ['Orange'] but got {repr(build_list('Orange'))}"

	
