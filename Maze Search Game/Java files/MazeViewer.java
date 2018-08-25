
// Name:Georgios Iliadis
// USC loginid: giliadis
// CS 455 PA3
// Spring 2018

import java.io.FileNotFoundException;
import java.io.IOException;
import javax.swing.JFrame;
import java.util.Scanner;
import java.io.File;

/**
 * MazeViewer class
 * 
 * Program to read in and display a maze and a path through the maze. At user
 * command displays a path through the maze if there is one.
 * 
 * How to call it from the command line:
 * java MazeViewer mazeFile
 * where mazeFile is a text file of the maze. The format is the number of rows
 * and number of columns, followed by one line per row, followed by the start
 * location, and ending with the exit location. Each maze location is either a
 * wall (1) or free (0). Here is an example of contents of a file for a 3x4
 * maze, with start location as the top left, and exit location as the bottom
 * right (we count locations from 0, similar to Java arrays):
 * 3 4 0111 0000 1110 0 0 2 3 
 */

public class MazeViewer {

	private static final char WALL_CHAR = '1';
	private static final char FREE_CHAR = '0';
	int numRows, numCols;
	boolean[][] array; // True = wall, False = not a wall
	int startX, startY;
	int exitX, exitY;

	public static void main(String[] args) {

		String fileName = "";

		try {
			if (args.length < 1) {
				System.out.println("ERROR: missing file name command line argument");
			} else {
				fileName = args[0];
				JFrame frame = readMazeFile(fileName);
				frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				frame.setVisible(true);
			}
		} catch (FileNotFoundException exc) {
			System.out.println("ERROR: File not found: " + fileName);
		} catch (IOException exc) {
			exc.printStackTrace();
		}
	}

	/**
	 * readMazeFile reads in maze from the file whose name is given and returns a
	 * MazeFrame created from it.
	 * @param fileName
	 *            the name of a file to read from (file format shown in class
	 *            comments, above)
	 * @returns a MazeFrame containing the data from the file.
	 * @throws FileNotFoundException
	 *             if there's no such file (subclass of IOException)
	 * @throws IOException
	 *             (hook given in case you want to do more error-checking -- that
	 *             would also involve changing main to catch other exceptions)
	 */
	private static MazeFrame readMazeFile(String fileName) throws IOException {
		Scanner in = new Scanner(new File(fileName));
		int numRows = in.nextInt();
		int numCols = in.nextInt();

		// my boolean 2Darray will have the size of the maze read from the file and
		// if there is a wall it will be set to true, otherwise false.
		// this is the boolean array that I will pass on my MazeFrame object
		boolean[][] array = new boolean[numRows][numCols]; // boolean an exei wall true, otherwise false
		in.nextLine();
		for (int x = 0; x < numRows; x++) {
			String line = in.nextLine();
			for (int y = 0; y < numCols; y++) {
				char c = line.charAt(y);
				if (c == WALL_CHAR) {
					array[x][y] = true;
				} else if (c == FREE_CHAR) {
					array[x][y] = false;
				}
			}
		}
		int startX = in.nextInt();
		int startY = in.nextInt();
		in.nextLine();
		int exitX = in.nextInt();
		int exitY = in.nextInt();

		return new MazeFrame(array, new MazeCoord(startX, startY), new MazeCoord(exitX, exitY));
	}
}