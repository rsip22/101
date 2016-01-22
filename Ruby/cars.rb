cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

puts "Temos #{cars} carros disponíveis."
puts "Temos apenas #{drivers} motoristas disponíveis."
puts "Haverá #{cars_not_driven} carros vazios hoje."
puts "Podemos transportar #{carpool_capacity} pessoas hoje."
puts "Temos #{passengers} para dar carona hoje."
puts "Temos de colocar cerca de #{average_passengers_per_car} pessoas por carro."
