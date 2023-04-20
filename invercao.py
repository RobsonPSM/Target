#Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente
#definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

string = "Toda a educação, no momento, não parece motivo de alegria, mas de tristeza. Depois, no entanto, produz naqueles que assim foram exercitados um fruto de paz e de justiça."

string_inversa = ""

for i in range(len(string)-1, -1, -1):
    string_inversa += string[i]

print(string_inversa)