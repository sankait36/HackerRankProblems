import java.util.Scanner;

public class CircularArrayRotation {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int arrSize = scan.nextInt();
		int numRotations = scan.nextInt();
		int numQueries = scan.nextInt();
		
		// 2nd Attempt: Using the mod operator, I can bring down complexity to O(n)
		int step = numRotations % arrSize;
		
		int[] numArray = new int[arrSize];
		for(int i = 0; i < arrSize; i++) {
			numArray[i] = scan.nextInt();
		}
		int[] queryResults = new int[numQueries];
		for(int j = 0; j < numQueries; j++) {
			int query = scan.nextInt();
			if (query-step >= 0) {
				queryResults[j] = numArray[query-step];
			}
			else
			{
				queryResults[j] = numArray[arrSize - step+query];
			}
		}
		for(int k = 0; k < queryResults.length; k++) {
			System.out.println(queryResults[k]);
		}
		/*
		rotator(numArray, numRotations);
		int[] queryResults = new int[numQueries];
		for(int j = 0; j < numQueries; j++) {
			int query = scan.nextInt();
			queryResults[j] = numArray[query];
		}
		for(int k = 0; k < queryResults.length; k++) {
			System.out.println(queryResults[k]);
		}
		*/
		scan.close();
	}
	
	// 1st Attempt:  This caused the test cases to time-out due to O(n^2) complexity
	 /*private static void rotator(int[] arr, int numOfRotations) {
		for(int i = 0; i < numOfRotations; i++){
			int temp = arr[arr.length-1];
			for(int j = arr.length - 1; j >= 1; j-- ){
				arr[j] = arr[j-1];
			}
			arr[0] = temp;
		}
	}
	*/
}
