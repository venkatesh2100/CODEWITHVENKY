package OOPS;

public class interfaces {
    interface Interface1{
        final int a=100;
        public void display();


    }
     static class TestClass implements Interface1{
        @Override
        public void display() {
            System.out.println("Hello World");
        }
    }

    public static void main(String[] args) {
        TestClass obj1=new TestClass();
        obj1.display();
    }
}
