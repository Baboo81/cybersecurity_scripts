import itertools;

characters = "abc123";
min_length = 2;
max_length = 4;

with open(filename, "w") as file:
    for length in range(min_length, max_length + 1):

        for combo in itertools.product(characters, repeat=length):
            password = "" .join(combo);
            file.write(password + \n);

print("wordlist générée avec succès !");
