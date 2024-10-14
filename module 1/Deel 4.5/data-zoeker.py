toets_data = ( 'Sofie:8', 'Emma:7', 'Ahmed:9', 'Daan:6', 'Lisa:8', 'Fatima:7', 'Ruben:9', 'Ayoub:6', 'Bram:8', 'Maria:7' )
separator = ','
position = 8 # position of Bram, first position starts with 0

def get_value(data: str, separator: str, position: int) -> str:
  gegevens = data[position].split(separator)
  return f"{gegevens[0]}, {gegevens[1]}"

for i in range(10): value = get_value(toets_data, ":", i); print(value)

#splitted_strings = toets_data.split(separator) # string splits itself into collection of strings
#if 0 <= position < len(splitted_strings): value = splitted_strings[position] # read value at position of split_values
#else: value = None
#print(value)