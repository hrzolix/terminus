class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

b = Bus("School", "90kph", "12")
print(b.seating_capacity(40))


for i in c:
    start = time.time()
    print(i)
    stop = time.time()
    print(stop-start)


def generateParentheses(openBr, closeBr, n, s = []):
	if closeBr == n:
		print(''.join(s))
		return 
	
	if closeBr < openBr:
		s.append(')')
		generateParentheses(openBr, closeBr+1, n, s)
		s.pop()
	if openBr < n:
		s.append('(')
		generateParentheses(openBr+1, closeBr, n, s)
		s.pop()
	return