public class SparseMatrix {
    private int rows;
    private int columns;
    private int[][] sparseMatrix;

    // Constructor to initialize the Sparse Matrix
    public SparseMatrix(int rows, int columns) {
        this.rows = rows;
        this.columns = columns;
        sparseMatrix = new int[rows][columns];
    }

    // Method to add an element to the matrix
    public void addElement(int row, int col, int value) {
        if (row < rows && col < columns) {
            sparseMatrix[row][col] = value;
        } else {
            System.out.println("Invalid index.");
        }
    }

    // Method to print the Sparse Matrix
    public void printMatrix() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(sparseMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Method to transpose the Sparse Matrix
    public SparseMatrix transpose() {
        SparseMatrix transposedMatrix = new SparseMatrix(columns, rows);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                transposedMatrix.addElement(j, i, sparseMatrix[i][j]);
            }
        }
        return transposedMatrix;
    }
}
