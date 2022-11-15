import keyboard as key
key.wait("esc")
a = """

package q10862;
import java.math.BigDecimal;
import java.math.MathContext;
public class BigDecimalUsage {
public static void main(String[] args) {
MathContext mathContext = new MathContext(5);
BigDecimal x = new BigDecimal("3.145", mathContext);
BigDecimal y = new BigDecimal("1.792", mathContext);
BigDecimal sum = x.add(y ,mathContext); //fill
BigDecimal difference =x.subtract( y,mathContext ) ; //fill
BigDecimal product =x.multiply( y,mathContext) ; //fill
BigDecimal quotient = x.divide( y,mathContext); //fill
System.out.println("sum = " + sum); 
System.out.println("difference = " + difference);
System.out.println("product = " + product);
System.out.println("quotient = " + quotient);
}
}

"""
key.write(a, exact=True, delay=0.05)
