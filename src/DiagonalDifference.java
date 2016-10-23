import java.util.Scanner;

public class DiagonalDifference {

	public static int arrSize;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		arrSize = scan.nextInt();
		int[][] matrix = new int[arrSize][arrSize];
		for(int i = 0; i < arrSize; i++) {
			for (int j = 0; j < arrSize; j++) {
				matrix[i][j] = scan.nextInt();
			}
		}
		int result = Math.abs(leftDiagonalAdd(matrix)-rightDiagonalAdd(matrix));
		System.out.println(result);
		scan.close();
	}
	
	// *
	//   *
	//     *
	public static int leftDiagonalAdd(int[][] matrix) {
		int leftDiagonalSum = 0;
		for(int i = 0; i < arrSize; i++) {
			leftDiagonalSum += matrix[i][i];
		}
		return leftDiagonalSum;
	}
	
	//      *
	//    *
	//  *
	public static int rightDiagonalAdd(int[][] matrix) {
		int rightDiagonalSum = 0;
		for(int i = 0; i < arrSize; i++) {
			rightDiagonalSum += matrix[i][arrSize -1 - i];
		}
		return rightDiagonalSum;
	}

}
