class Fixnum

	def ehPrimo?
	  self % 2 != 0 and self % 3 != 0
	end

	def divisores
	  range = 1..self
	  range.select do |i|
	  	self % i == 0  
	  end
	end

	def ehPerfeito?
	  return false if self.ehPrimo? 
	  sum = 0
	  self.divisores.each do |n| sum += n end
	  return self == sum - self
	end
end

def numerosPerfeitos(ate)	
  range = 0..ate
  range.select do |n| 
  	n.ehPerfeito?  
  end
end

numero = gets.to_i
puts numerosPerfeitos(numero)

#puts "Os numeros perfeitos ate 1000 sao : #{numerosPerfeitos(10000)}"
