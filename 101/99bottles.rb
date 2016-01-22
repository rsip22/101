#!/usr/bin/ruby

bottles_of_beer = 99
while bottles_of_beer > 1
  puts bottles_of_beer.to_s + ' bottles of beer on the wall, ' +
  bottles_of_beer.to_s + ' bottles of beer'
  bottles_of_beer = bottles_of_beer - 1
  puts 'You take one down, pass it around, ' + bottles_of_beer.to_s + '
  bottles of beer on the wall.'
  puts ''
end

puts 'Everyone passes out quite drunk.'
