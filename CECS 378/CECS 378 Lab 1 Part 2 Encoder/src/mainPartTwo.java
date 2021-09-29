import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class mainPartTwo {
	public static void main(String[] args)
	{
		boolean stop = false;
		
		while (!stop)
		{	
				// Just for fast testing
				Scanner sc = new Scanner(System.in);
				
				ArrayList<String> alphabet = new ArrayList<String>(
						Arrays.asList("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"));
				System.out.println("Choose which line to encode (1, 2, 3) *Hit anything else to break* : ");
				
				// Fast test cause already typed out
				String line1 = "He who fights with monsters should look to it that he himself does" + 
						"not become a monster . And if you gaze long into an abyss , the abyss" + 
						"also gazes into you" + 
						"";
				String line2 = "There is a theory which states that if ever anybody discovers"
						+ "exactly what the Universe is for and why it is here , it will" + 
						 
						"instantly disappear and be replaced by something even more bizarre" + 
						"and inexplicable . There is another theory which states that this" + 
						"has already happened .";
				String line3 = "Whenever I find myself growing grim about the mouth ; whenever it is" + 
						"a damp , drizzly November in my soul ; whenever I find myself" + 
						"involuntarily pausing before coffin warehouses , and bringing up the" + 
						"rear of every funeral I meet ; and especially whenever my hypos get" + 
						"such an upper hand of me , that it requires a strong moral principle" + 
						"to prevent me from deliberately stepping into the street , and" + 
						"methodically knocking people ’ s hats off - then , I account it high" + 
						"time to get to sea as soon as I can ." + 
						"";
				// Pick whatever
				int enter = sc.nextInt();
				
				String code = "";
				
				// First one
				if(enter == 1)
				{
					code = line1.replaceAll("[^a-zA-Z0-9]", "");
				}
				
				// Second one
				else if(enter == 2) 
				{
					code = line2.replaceAll("[^a-zA-Z0-9]", "");
				}
				
				// Third one
				else if(enter == 3) 
				{
					code = line3.replaceAll("[^a-zA-Z0-9]", "");
				}
				
				code = code.toLowerCase();
				
				// Just leave
				if (enter < 1 || enter > 3) 
				{
					stop = true; 
					break;
				}
				
				Random rand = new Random(); 
				  
				// Generate random integers in range 1 to 26 
				int rand_int1 = rand.nextInt(25) + 1;
		        
				//Stores code message by letter
				String stored[] = new String[code.length()];
					for (int i = 0; i <= code.length() - 1; ++i )
					{	
						stored[i] = String.valueOf(code.charAt(i));
					}
					
					
				// Store it here
					String encode[] = stored.clone();
					
		        
				// Replace and encode
			        for (int j = 0; j < encode.length; j++)	
					{
			        	if(rand_int1 > 26)
			        		encode[j] = alphabet.get((alphabet.indexOf(stored[j]) + rand_int1));
			        	else
			        		encode[j] = alphabet.get((alphabet.indexOf(stored[j]) + rand_int1) % 26);
			        	
					}
			        
			    // Print out
			        System.out.print("(Key: " + rand_int1 + ") ");
					for (int s = 0; s < encode.length; ++s)
						{
							System.out.print(encode[s]);
						}
							System.out.println("\n");
				
		}
		
		
	}
}
