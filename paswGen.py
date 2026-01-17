import itertools;

characters = "abc";
min_length = 2;
max_length = 4;

for length in range(min_length, max_length + 1):

    for combo in itertools.product(characters, repeat=length):
        password = "" .join(combo);

print(password);
