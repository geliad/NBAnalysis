
// Name: Georgios Iliadis	
// USC loginid: giliadis
// CS 455 PA3
// Spring 2018

import java.util.LinkedList;

/**
 * Maze class
 * 
 * Stores information about a maze and can find a path through the maze (if
 * there is one).
 * 
 * Assumptions about structure of the maze, as given in mazeData, startLoc, and
 * endLoc (parameters to constructor), and the path: -- no outer walls given in
 * mazeData -- search assumes there is a virtual border around the maze (i.e.,
 * the maze path can't go outside of the maze boundaries) -- start location for
 * a path is maze coordinate startLoc -- exit location is maze coordinate
 * exitLoc -- mazeData input is a 2D array of booleans, where true means there
 * is a wall at that location, and false means there isn't (see public FREE /
 * WALL constants below) -- in mazeData the first index indicates the row. e.g.,
 * mazeData[row][col] -- only travel in 4 compass directions (no diagonal paths)
 * -- can't travel through walls
 * 
 */

public class Maze {

	public static final boolean FREE = false; // en mes to maze.
	public static final boolean WALL = true; // toixos pas to phantom
	private boolean[][] myMaze;
	private boolean[][] visited; // I created a new boolean array so that I know the visited coordinates
	// If true, the coordinate was visited, false = not visited.
	// Everytime that I go to a mazeCoord using search, I want that coordinate to
	// become true.
	private MazeCoord startCoord, exitCoord;
	int numbRows, numbCols;
	LinkedList<MazeCoord> path;

	/**
	 * Constructs a maze.
	 * 
	 * @param mazeData
	 *            the maze to search. See general Maze comments above for what goes
	 *            in this array.
	 * @param startLoc
	 *            the location in maze to start the search (not necessarily on an
	 *            edge)
	 * @param exitLoc
	 *            the "exit" location of the maze (not necessarily on an edge) PRE:
	 *            0 <= startLoc.getRow() < mazeData.length and 0 <=
	 *            startLoc.getCol() < mazeData[0].length and 0 <= endLoc.getRow() <
	 *            mazeData.length and 0 <= endLoc.getCol() < mazeData[0].length
	 * 
	 */
	public Maze(boolean[][] mazeData, MazeCoord startLoc, MazeCoord exitLoc) {
		path = new LinkedList<MazeCoord>();
		numbRows = mazeData.length;
		numbCols = mazeData[0].length;
		myMaze = mazeData;
		startCoord = startLoc;
		exitCoord = exitLoc;
		visited = new boolean[numbRows][numbCols];
	}

	/**
	 * Returns the number of rows in the maze
	 * @return number of rows
	 */
	public int numRows() {
		return numbRows;
	}

	/**
	 * Returns the number of columns in the maze
	 * @return number of columns
	 */
	public int numCols() {
		return numbCols;
	}

	/**
	 * Returns true iff there is a wall at this location
	 * @param loc
	 *            the location in maze coordinates
	 * @return whether there is a wall here PRE: 0 <= loc.getRow() < numRows() and 0
	 *         <= loc.getCol() < numCols()
	 */
	public boolean hasWallAt(MazeCoord loc) {
		int ro = loc.getRow();
		int co = loc.getCol();
		if (myMaze[ro][co]) { // if at that coordinate there is a wall (boolean array is true), return true
			return true;
		} else {
			return false;
		}
	}

	/**
	 * Returns the entry location of this maze.
	 */
	public MazeCoord getEntryLoc() {
		return startCoord;
	}

	/**
	 * Returns the exit location of this maze.
	 */
	public MazeCoord getExitLoc() {
		return exitCoord;
	}

	/**
	 * Returns the path through the maze. First element is start location, and last
	 * element is exit location. If there was not path, or if this is called before
	 * a call to search, returns empty list.
	 * 
	 * @return the maze path
	 */
	public LinkedList<MazeCoord> getPath() {
		return path;
	}

	/**
	 * Find a path from start location to the exit location (see Maze constructor
	 * parameters, startLoc and exitLoc) if there is one. Client can access the path
	 * found via getPath method.
	 * 
	 * @return whether a path was found.
	 */
	public boolean search() {
		return searchHelp(startCoord);
	}

	private boolean searchHelp(MazeCoord currentCoord) {
		int row = currentCoord.getRow();
		int col = currentCoord.getCol();

		if (row < 0 || row >= numbRows || col < 0 || col >= numbCols) { // outside of maze
			return false;
		}
		if (hasWallAt(currentCoord) == true) { // false = failure, true = success
			return false;
		}
		if (visited[currentCoord.getRow()][currentCoord.getCol()] == true) {
			return false;
		}
		if (currentCoord.equals(exitCoord)) { // If the current locationn equals the exit loc.
			path.add(currentCoord);
			return true;
		}

		visited[row][col] = true; // visited[row][col] is visited
									// MazeCoord(row,col) visited

		MazeCoord right = new MazeCoord(row, col + 1); // right = currentloc(row,col +1)
		MazeCoord left = new MazeCoord(row, col - 1); // left = CurrentLoc(row, col -1)
		MazeCoord up = new MazeCoord(row - 1, col);
		MazeCoord down = new MazeCoord(row + 1, col);

		if (searchHelp(right) || searchHelp(left) || searchHelp(up) || searchHelp(down)) {
			path.add(currentCoord);
			return true;
		}
		return false;
	}
}
