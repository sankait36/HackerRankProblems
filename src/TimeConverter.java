import java.util.Scanner;

public class TimeConverter {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String time = scan.nextLine();
		char[] timeElements = time.toCharArray();
		if (timeElements[time.length()-2] == 'A'){
			//Checking for 12 am
			if(timeElements[0] == '1' && timeElements[1] == '2') {
				timeElements[0] = '0';
				timeElements[1] = '0';
			}
		}
		else if(timeElements[time.length()-2] == 'P') {
			if(timeElements[0] != '1' || timeElements[1] != '2'){
				int hours1 = timeElements[0];
				int hours2 = timeElements[1];
				hours1 += 1;
				hours2 += 2;
				timeElements[0] = (char) hours1;
				timeElements[1] = (char) hours2;
			}
		}
		for(int i = 0; i<timeElements.length-2; i++) {
			System.out.print(timeElements[i]);
		}
		scan.close();
	}
}
