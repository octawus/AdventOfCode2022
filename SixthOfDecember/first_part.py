f = open("data_stream", "r")

stream = f.read()
counter = 1

def iterate_over_overlaping_substrings(input_stream, no_of_characters):
    return [''.join(item) for item in zip(*[input_stream[no_of_characters:] for no_of_characters in range(no_of_characters)])]


for item in iterate_over_overlaping_substrings(stream, 14):
    print(item)
    print(counter)
    counter = counter + 1
    if len(set(item)) == len(item):
        break

print(counter+12)

