### Python Data Types
### Text Type:	str
### Numeric Types:	int, float, complex
### Sequence Types:	list, tuple, range
### Mapping Type:	dict
### Set Types:	set, frozenset
### Boolean Type:	bool
### Binary Types:	bytes, bytearray, memoryview


def fn_populateDataTypes():
  thisStr = 'hello, world'
  thisInt = 1024
  thisFloat = 1.23
  thisComplex = 2j
  thisList = [22,33,44]
  thisTuple = (23,34,45)
  thisRange = range(5)
  thisDict = {'key1': 'value1', 'key2': 'value2'}
  thisSet = {24,35,46}
  thisFrozenSet = frozenset({"apple", "banana", "cherry"})
  thisBool = True
  thisBytes = b"Hello"
  thisByteArray = bytearray(5)
  thisMemoryView = memoryview(bytes(5))


def fn_convertDataTypes():
  x = str("Hello World")
  x = int(20)
  x = float(20.5)
  x = complex(1j)
  x = list(("apple", "banana", "cherry"))
  x = tuple(("apple", "banana", "cherry"))
  x = range(6)
  x = dict(name="John", age=36)
  x = set(("apple", "banana", "cherry"))
  x = frozenset(("apple", "banana", "cherry"))
  x = bool(5)
  x = bytes(5)
  x = bytearray(5)
  x = memoryview(bytes(5))


def fn_start():
  print('fn_start')


fn_start()