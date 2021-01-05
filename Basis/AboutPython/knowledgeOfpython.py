# 类和继承
# 创建类
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + "is now sitting")
    def roll_over(self):
        print(self.name.title()+"rolled over")

# 初始化类
my_dog = Dog('lucy',6)
my_dog.roll_over() # 调用实例对象中的方法
my_dog.sit()

# 通过方法修改属性值
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_description(self):
        long_name = str(self.year)+' '+self.make +' '+self.model
        return long_name.tile()
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you can not roll back an odometer!')
        self.odometer_reading = mileage
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+" miles on it.")
my_new_car = Car('audi','a8',2016)




# 将实例用作属性
class Wheel():
    def __init__(self,size): # 可以看成是java中的构造方法,但是不需要声明变量
        self.size = size
    def describe_wheel(self):
        print("ebike's wheel size is "+str(self.size))


# 继承
class ElectricCar(Car):
    def __init__(self,make,model,year,battery):
        super().__init__(make,model,year) # 继承父类中的属性
        self.battery=battery # 子类中自己的属性
        self.wheel = Wheel(70)
    def describe_battery(self):
        print('This ebike has a '+ str(self.battery)+'-kwh')


my_ebike = ElectricCar('xiao','s6',2018,80)
my_ebike.describe_battery()
my_ebike.wheel.describe_wheel()






<<<<<<< HEAD


=======
>>>>>>> 9957cc782d910bb4ac9e14e7406e1d7ab3e47784
