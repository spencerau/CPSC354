

public class Loop {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
        boolean found = false;

        top:
        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[row].length; col++) {
                // found something divisible by 3, then break
                if (matrix[row][col] % 3 == 0) {
                    //System.out.println("Found " + matrix[row][col] + " at row " + row + " and column " + col);
                    found = true;
                    // use a labeled break to break out of both loops
                    break top;
                }
            }
            System.out.println("Finished row " + row);
        }
        
        if (found) {
            System.out.println("Found a number divisible by 3");
        } else {
            System.out.println("Did not find a number divisible by 3");
        }
    }
}