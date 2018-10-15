# OOP(객체지향 프로그래밍) 의 개념

## (1) Class
- A class is a template that defines what an object's data fields and methods will be.
> 클래스는 오브젝트의 템플렛이고 데이터 필드와 함수 필드를 가지고 있다.
```
class Car{
    private String model;
    private int yearl

    public String getModel(){
        return model;
    }
    public void setModel(String model){
        this.model = model;
    }
    public int getYear(){
        return year;
    }
    public void setYear(int year){
        this.year = year;
    }
    void printDescription(){
        System.out.println("this is a car");
    }
}
```
## (2) Object
- An Instance of a class
> 오브젝트는 클래스의 인스턴스이다.
```
public class YourProgram{
    public static void main(String[] args){
        Car camry = new Car(); // here we instantiate Car class to camry object
        camry.setModel("camry");
        camry.setYear(2000);

        Tesla modelx = new Tesla();
        modelx.setModel("model x");
        modelx.setYear(2017);

        camry.printDescription();
        modelx.printDescription();
        modelx.printDescription("all")
    }
}
```
> 클래스에서 선언한 함수들은 오브젝트에 값을 설정할 수 있다. 프로그램에서 직접 들어가는 것은 오브젝트이다. 클래스는 오브젝트를 생성하기 위한 하나의 파일이라고 보면 된다.

## (3) Encapsulation
- Provides the security that keeps data and methods safe from inadvertent changes.
> 클래스에 보안을 제공해주고 외부 개발자가 클래스의 데이터와 함수를 함부로 바꿀 수 없게 하는 역할이다.
```
...
camry.setModel("camry");
camry.setYear(2000);
...
```
> setModel함수와 setYear함수에 값을 넣어서 사용할 수 있지만 권한이 없다면 저 함수의 기능을 바꿀 수 없다.

## (4) Inheritance
- Parent-Child relationship of class which is mainly Used for code reusability.
> 상속은 부모 자식간의 관계라고 보고 코드의 재사용성을 위해 존재하는 개념이다.
```
public class Tesla extends Car{
    void printDescription(){
        System.out.println("this is a electric car");
    }
    void printDescription(String param){
        System.out.println("this is a electric car, year: "+super.getYear()+", model: "+super.getModel(+".");)
    }
}
```
> Car라는 클래스를 부모로 갖는다. 부모가 가지고 있는 함수와 데이터필드를 자식클래스에서 사용할 수 있다.

## (5) Polymorphism
- Methods having same name works differently in different context.(overloading, overriding)
> 자바에서 다형성은 오버로딩과 오버라이딩으로 표현된다. 같은 이름이지만 다르게 행동한다.

### overloading
```
public class Tesla extends Car{
    void printDescription(){
        System.out.println("this is a electric car");
    }
    void printDescription(String param){
        System.out.println("this is a electric car, year: "+super.getYear()+", model: "+super.getModel(+".");)
    }
}
```
> 같은 이름의 함수지만 위 함수는 매개변수가 없고 다른 함수는 매개변수가 있다. 즉 다른 행동을 한다.

### overriding
> 같은 함수 이름이지만 다른 클래스에서 다르게 활동한다.
```
class Car{
    ...
    void printDescription(){
        System.out.println("this is a car");
    }
}
```
```
public class Tesla extends Car{
    void printDescription(){
        System.out.println("this is a electric car");
    }
    ...
}
```

## (6) Abstraction
- An abstract class is something which is incomplete and you can not create instance of abstract class. If you want to use it you need to make it complete or concrete by extending it.
> 가상 클래스는 가상 함수를 가지고 있는데 가상 클래스에서 구현하지 않는다. 다만 가상 클래스를 부모로 가지고 있는 자식 클래스, 즉 상속받은 클래스는 가상 함수를 구현해야 한다.
```
public abstract class Abstract_Car{
    public abstract void start();
    public abstract void stop();
}
```
```
public class GasCar extends Abstract_Car{
    @Override
    public void start(){
        System.out.println("start Gas Engine");
    }
    @Override
    public void stop(){
        System.out.println("stop Gas Engine");
    }
}
```
