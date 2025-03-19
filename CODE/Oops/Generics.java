
/**
 * generics These are used For TypeSaftey.
 */


  class Box<T>{
    private  T value;


    public void setValue(T value){
      this.value  = value;
    }
    public T  getvalue(){
      return value;
    }
  }

 public class Generics {
  public static void main(String[] args) {
    Box<Integer> intBox  = new Box<>();
    intBox.setValue(1000);
    System.out.println(intBox.getvalue());

    Box<String> strBox = new Box<>();
    strBox.setValue("Hello JAVA");
    System.out.println(strBox.getvalue());
  }
 }