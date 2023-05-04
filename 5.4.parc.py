# Car class 만들기

# 예를 들어, 자동차 클래스를 만들어서 자동차 객체를 생성할 수 있습니다. 자동차 클래스는 자동차 객체가
# 가져야 할 속성(예: 모델명, 제조사, 색상, 최고속도)과 동작(예: 전진, 후진, 가속, 감속)을 정의할 수 있습니다. 
# 이러한 자동차 객체들은 모두 같은 클래스에서 생성되었기 때문에, 같은 속성과 동작을 가지고 있지만, 
# 각 객체는 서로 다른 값을 가질 수 있습니다.

class Car:
    def __init__(self,company, model,color,top_speed):
        self.model = model
        self.company = company
        self.color = color
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        if self.speed > self.top_speed:
            self.speed = self.top_speed

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
    
    def get_speed(self):
        return self.speed
    


my_car = Car("현대","코나","black",100)
print("모델은",my_car.model) #.하고 속성값을 가져온다
print("회사는",my_car.company)
print("색깔은",my_car.color)
print("최고속도는",my_car.top_speed)
my_car.accelerate(50) #.메소드(값=amount)를 이용해 메소드를 실행시킨다
print(my_car.get_speed())
my_car.accelerate(90)
print(my_car.get_speed())
my_car.brake(70)
print(my_car.get_speed())
#9분 20초 걸림



# Animal 클래스로 상속 연습하기

# Animal 클래스를 만들어서 이름과 나이를 속성으로 speak를 메소드로 갖게 해주세요
# Dog 클래스와 Cat 클래스를 각각 Animal 상속을 받아 만들어주세요.
# speak 메소드를 각각의 클래스에 맞게 구현해주세요



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return print("어떻게 울까요?")

class Dog(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return print("멍멍") 
    
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    
    def speak(self):
        return print("야옹")



my_dog = Dog("몽이",3,"pink")
my_dog.speak()
my_cat = Cat("코코",4,"white")
my_cat.speak()
#7분 45초걸림




#추상 클래스와 상속 연습하기

#Shape 클래스를 만들어서 get_area 메소드를 갖게 해주세요.
#Circle과 Rectangle 클래스를 Shape를 상속받아 만들어주세요 Circle은 radius 속성을 가지게
#Rectangle은 length와 widht 속성을 가지게 get_area 메소드는 각각에 맞게 구현해주세요

#추상클래스
class shape:
    def __init__(self):
        pass
    
    def get_area(self):
        pass

class Cirecle(shape):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius**2
    
class Rectangle(shape):
    def __init__(self,length, widht):
        self.widht = widht
        self.length = length

    def get_area(self):
        return self.widht * self.length
    
cir = Cirecle(4)
print(cir.get_area())
Rec = Rectangle(3,5)
print(Rec.get_area())
#4분초과됨

