import java.util.Scanner;
public class Staircase {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int height = scan.nextInt();
		int hash = 1;
		for(int i = 0; i < height; i++, hash++) {
			for(int j = 0; j < height-1-i; j++){
				System.out.print(" ");
			}
			for(int k = 0; k < hash; k++){
				System.out.print("#");
			}
			System.out.println();
		}
		scan.close();
	}
}
