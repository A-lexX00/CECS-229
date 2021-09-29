import java.util.Scanner;

public class mainPartOne {
	public static void main(String[] args)
	{
		boolean stop = false;
		
		while (!stop)
		{	
				// Just for fast testing
				Scanner sc = new Scanner(System.in);
				
				String alphabet[] = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
				System.out.println("Choose which line to decode (1, 2, 3, 4) *Hit anything else to break* : ");
				
				// Fast test cause already typed out
				String line1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc";
				String line2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy";
				String line3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae";
				String line4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun "
						+ "sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq "
						+ "shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun "
						+ "siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq "
						+ "uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz";
				
				// Pick whatever
				int enter = sc.nextInt();
				
				String encrypted = "";
				
				// First one
				if(enter == 1)
				{
					encrypted = line1.replaceAll(" ", "");		
				}
				
				// Second one
				else if(enter == 2) 
				{
					encrypted = line2.replaceAll(" ", "");		
				}
				
				// Third one
				else if(enter == 3) 
				{
					encrypted = line3.replaceAll(" ", "");		
				}
				
				// Fourth one
				else if(enter == 4) 
				{
					encrypted = line4.replaceAll(" ", "");		
				}
				
				encrypted = encrypted.toLowerCase();
				
				// Just leave
				if (enter < 1 || enter > 4) 
				{
					stop = true; 
					break;
				}	
			
				
				//Stores code message by letter
				String stored[] = new String[encrypted.length()];
					for (int i = 0; i <= encrypted.length() - 1; ++i )
					{	
						stored[i] = String.valueOf(encrypted.charAt(i));
					}
				
				// First two are Ceaser shift so do that
				if(enter == 1 || enter == 2)
				{
					// Count the common occuring letters
					int currentVowels = 0, currentConsonants = 0;
					int maxVowels = 0, maxConsonants = 0;
					
					// Decoded text
					String decrypt[] = {};
								
					int key = 0;
				
					// Check all possible letter coding
					for (int i = 1; i < 26; ++i) { 
						String decrypted[] = stored.clone();
									
						// Traverse the entire code
						for (int j = 0; j <= decrypted.length - 1; ++j)	
						{
										
							boolean end = false;
							// Go through alphabet
							for (int k = 0; k < 26; ++k) 
							{
								
								if (decrypted[j].equals(alphabet[k]) && !end) 
								{
									// From 26 back to 1
										if (  ((k - i) % 26) < 0) 
											decrypted[j] = alphabet[((k - i) % 26) + 26];	
										else
											decrypted[j] = alphabet[((k - i) % 26)];
										end = true;			
													
										// Vowel Count
										if (decrypted[j].equals("a") || decrypted[j].equals("e") || decrypted[j].equals("i") 
												|| decrypted[j].equals("o") || decrypted[j].equals("u"))
										{
											++currentVowels;
										}
										
										// Consonant Count
										if (decrypted[j].equals("r") || decrypted[j].equals("s") || 
													decrypted[j].equals("t")) 
										{
											++currentConsonants;
										}
									
								}	
							}				
						}						
					
					// Check to see if the new string had more vowels and common consonants than the last
					if (currentVowels > maxVowels && currentConsonants > maxConsonants)	
					{
						// Put the more correct version into the string and keep going
						// Also record the key
						maxVowels = currentVowels;
						decrypt = decrypted.clone();
						key = i;				
					}
				
					// Print it out decoded
					if (i == 25)		
					{
						System.out.print("(Key: " + key + ") ");
						for (int s = 0; s < decrypt.length; ++s)
							{
								System.out.print(decrypt[s]);
							}
								System.out.println("\n");
					}			
						// Just reset it all
						currentVowels = 0;
						currentConsonants = 0;
				}
				
			}
				
				// Monoalphabetic cypher encryption
				// I'll figure it out later
				else if(enter == 3 || enter == 4)
				{
					// Encode monoalphabetic cypher encryption
				}
				
			}
		}
}
