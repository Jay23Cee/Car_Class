class cars:
  def __init__(self, year, model,make):
    self.year= year
    self.model= model
    self.make= make   
  
  def toString(self):
  	print( self.make, self.model, str(self.year)  )
    

p1 = cars(2016, "Altima coupe", "Nissan")
p2= cars(2020, "GTR", "Nissa")
p3= cars(2001, "Celica", "Toyota")

dealer= { p1.make:p1,p2.make:p2,
p3.make:p3
}


for car in dealer:
	print(car)
	
#	for veh in dealer[car]:
	print(dealer[car].toString())
	#	print(veh)
	
