tipos_de_pessoa = 10
x = "Existem #{tipos_de_pessoa} tipos de pessoa."
binarios = "binários"
nao_sabem = "não sabem"
y = "Aquelas que sabem #{binarios} e aquelas que #{nao_sabem}."
# string inside string

puts x
puts y

puts "Eu disse: #{x}." # string inside string
puts "Eu também disse: '#{y}'." # string inside string

hilarious = false
joke_eval = "Essa piada não é engracada?! #{hilarious}"

puts joke_eval

w = "Esse é o lado esquerdo de..."
e = "uma string com um lado direito."

puts w + e
