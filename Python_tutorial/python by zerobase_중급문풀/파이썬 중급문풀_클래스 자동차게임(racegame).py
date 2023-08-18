import racegame as rg

myCarGame = rg.CarRacing()

car1 = rg.Car('Car01', 'White', 250)
car2 = rg.Car('Car02', 'Black', 200)
car3 = rg.Car('Car03', 'Yellow', 220)
car4 = rg.Car('Car04', 'Red', 280)
car5 = rg.Car('Car05', 'Blue', 150)

myCarGame.addCar(car1)
myCarGame.addCar(car2)
myCarGame.addCar(car3)
myCarGame.addCar(car4)
myCarGame.addCar(car5)

myCarGame.startRacing()
