#!/usr/bin/ruby
puts 'Olá! Qual seu número favorito?'
numer = gets.chomp
meunumer = numer.to_i+1
puts 'É mesmo? Mas ' + meunumer.to_s + ' é maior e melhor do que ' + numer.to_s + '.'
