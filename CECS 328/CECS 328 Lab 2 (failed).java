import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;


public class Main {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File f = new File("input.txt");
		String input = "";
		int arraySize = 0;
		
		try  // set array size
		{
			Scanner scan = new Scanner(f);
			input = scan.nextLine();
			arraySize = Integer.parseInt(input);
		}
		catch(FileNotFoundException ex) 
		{  
			System.out.print("File wasnt found.");
		}
		
		ArrayList<Integer> easyNums = new ArrayList<Integer>(arraySize);
		ArrayList<BigInteger> a = new ArrayList<BigInteger>(arraySize);
		ArrayList<BigInteger> b = new ArrayList<BigInteger>(arraySize);
	
		try  // Fill the arrays with the integers
		{
			Scanner scan = new Scanner(f);
			input = scan.nextLine();
			while(scan.hasNextLine()) 
			{
				input = scan.nextLine();
				if(input.indexOf(" ") == -1)
					easyNums.add(Integer.parseInt(input));
				else
				{
					String[] objects = input.split(" ");
					
					a.add(new BigInteger(objects[0]));
					b.add(new BigInteger(objects[1]));
				}
			}
		}
		catch(FileNotFoundException ex) 
		{  
			System.out.print("File wasnt found.");
		}
		
		/*
		 * Code here
		 */
		
		Map<Integer, Integer> gcdFound = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < easyNums.size(); i++)
		{
			// get common GCD
			
			int gcdTester = easyNums.get(i);
			
			BigInteger gcd = BigInteger.valueOf(gcdTester);
			BigInteger zero = new BigInteger("0");
			
			for (int j = 0; j < a.size(); j++) {
				
				// Two points
				
				// Are a and b divisible by the gcd
				if(a.get(j).remainder(gcd).equals(zero) && b.get(j).remainder(gcd).equals(zero)) {
					
					// Keep track of a and b
					BigInteger counter = a.get(j);	
					BigInteger counterTwo = b.get(j);
					
					// Check to see if a AND b are divisible by the gcd
					while(counter.mod(gcd).equals(zero) && counterTwo.mod(gcd).equals(zero))  {
						if(gcdFound.containsKey(gcdTester))
							gcdFound.replace(gcdTester, gcdFound.get(gcdTester) + 2);
						else
							gcdFound.put(gcdTester, 2);
						
							counter = counter.divide(gcd);
							counterTwo = counterTwo.divide(gcd);
					}
				}
				
				// One point
				
					
					// is A and only a divisible by the gcd
				if (a.get(j).remainder(gcd).equals(zero) && !(b.get(j).remainder(gcd).equals(zero))) {
						
						// Keep track of a
						BigInteger counter = a.get(j);		
						
						// is a divisible by gcd?
						while(counter.mod(gcd).equals(zero)) {
							if(gcdFound.containsKey(gcdTester))
								gcdFound.replace(gcdTester, gcdFound.get(gcdTester) + 1);
							else
								gcdFound.put(gcdTester, 1);
							
								// divide gcd from a
								counter = counter.divide(gcd);
						}
					}
					// is B and only b divisible by the gcd
				if (!(a.get(j).remainder(gcd).equals(zero)) && b.get(j).remainder(gcd).equals(zero)) {
						
						// Keep track of b
						BigInteger counter = b.get(j);		
						
						// is b divisble by gcd?
						while(counter.mod(gcd).equals(zero)) {
							if(gcdFound.containsKey(gcdTester))
								gcdFound.replace(gcdTester, gcdFound.get(gcdTester) + 1);
							else
								gcdFound.put(gcdTester, 1);
							
								// divide gcd from b
								counter = counter.divide(gcd);
						}
					}
					
			}
		}
		
		PrintWriter writer;
		try {
			writer = new PrintWriter("output.txt", "UTF-8");
			String output = "";
			
			Set set = gcdFound.entrySet();
		    Iterator iterator = set.iterator();
		    
		    while(iterator.hasNext()) {
		         Map.Entry mentry = (Map.Entry)iterator.next();
		         output += mentry.getKey().toString() + " " + mentry.getValue().toString() + '\n';
		    }
			
			writer.print(output);
			writer.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}