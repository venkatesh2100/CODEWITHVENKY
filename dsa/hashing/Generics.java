package HASHING;

public class Generics {
    public static void main(String[] args) {
        Test<String,Integer> obj=new Test<String,Integer>("Venky",2005);
        obj.print();

    }
    public static class Test<T ,U>{
        T  obj1;
        U obj2;
        Test(T obj1,U Obj2){
            this.obj1=obj1;
            this.obj2=obj2;
        }
        public void print(){
            System.out.println(obj1);
            System.out.println(obj2);
        }
    }
}
