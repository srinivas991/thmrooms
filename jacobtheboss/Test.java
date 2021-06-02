import java.io.*;
import org.jboss.invocation.MarshalledValue;

class Test
{
    public static void main(String[] args) {
        org.jboss.invocation.MarshalledValue object1 = null;
  
        // Deserialization
        try
        {   
            // Reading the object from a file
            String filename = "pyfile.ser";
            FileInputStream file = new FileInputStream(filename);
            ObjectInputStream in = new ObjectInputStream(file);
              
            // Method for deserialization of object
            object1 = (org.jboss.invocation.MarshalledValue)in.readObject();
              
            in.close();
            file.close();
              
            System.out.println("Object has been deserialized ");
            System.out.println("a = " + object1);
        }
          
        catch(IOException ex)
        {
            System.out.println("IOException is caught");
        }
          
        catch(ClassNotFoundException ex)
        {
            System.out.println("ClassNotFoundException is caught");
        }
  
    }
}