import java.text.DecimalFormat;
import java.util.Scanner;

public class PlusMinus {

	public static int minusCount, plusCount, zeroCount;
	
	public static void main(String[] args) {
		DecimalFormat formatter = new DecimalFormat("0.000000");
		Scanner scan = new Scanner(System.in);
		int arrSize = scan.nextInt();
		int[] numArray = new int[arrSize];
		for (int i = 0; i < arrSize; i++) {
			numArray[i] = scan.nextInt();
		}
		evaluator(numArray);
		double minusFraction = (double) minusCount/arrSize;
		double plusFraction = (double) plusCount/arrSize;
		double zeroFraction = (double) zeroCount/arrSize;
		
		System.out.println(formatter.format(plusFraction));
		System.out.println(formatter.format(minusFraction));
		System.out.println(formatter.format(zeroFraction));
		scan.close();
	}
	
	public static void evaluator(int[] arr){
		for (int i = 0; i < arr.length; i++) {
			if(arr[i] > 0) {
				plusCount++;
			}
			else if (arr[i] < 0) {
				minusCount++;
			}
			else if (arr[i] == 0) {
				zeroCount++;
			}
		}
	}

}
