#!/usr/bin/ruby

print '1 elefante incomoda muita gente.'
  puts ''

elefantes = 2
  puts ''

while elefantes <= 100
  puts elefantes.to_s + ' elefantes ' + ('incomodam ' * elefantes.to_i) + 'muito mais.'

elefantes = elefantes + 1
  puts elefantes.to_s + ' elefantes incomodam muita gente.'
  puts ''
end
