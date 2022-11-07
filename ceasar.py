class Ceasar:
    def __init__(self):
        self.direction = input("Type encode to 'encrypt', type decode to 'decrypt': ").lower()
        self.text = input("Type your message: ")
        self.shift = int(input("Type the shift number: "))
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz' * 20000

    def cipher(self):
        if self.direction == 'decode':
            self.shift *= -1
        word = ''
        for i in self.text:
            if i in self.alphabets:
                position = self.alphabets.index(i) + self.shift
                if position > len(self.alphabets):
                    new_shift = position - len(self.alphabets)
                else:
                    new_shift = position
                word += self.alphabets[new_shift]
            else:
                word += i
        print(f"Here is your {self.direction}d word: {word}")
