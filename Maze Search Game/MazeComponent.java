
// Name: Georgios Iliadis
// USC loginid: giliadis
// CS 455 PA3
// Spring 2018

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.util.LinkedList;
import java.util.ListIterator;
import javax.swing.JComponent;

/**
 * MazeComponent class A component that displays the maze and path through it if
 * one has been found.
 */
public class MazeComponent extends JComponent {
	private static final int START_X = 10; // top left of corner of maze in frame
	private static final int START_Y = 10;
	private static final int BOX_WIDTH = 20; // width and height of one maze "location"
	private static final int BOX_HEIGHT = 20;
	private static final int INSET = 2; // how much smaller on each side to make entry/exit inner box
	private Maze mazeDesign; // create new maze object to use all the methods from Maze class

	/**
	 * Constructs the component.
	 * 
	 * @param maze
	 *            the maze to display
	 */
	public MazeComponent(Maze maze) {
		mazeDesign = maze;
	}

	/**
	 * Draws the current state of maze including the path through it if one has been
	 * found.
	 * 
	 * @param g
	 *            the graphics context
	 */
	public void paintComponent(Graphics g) {
		Graphics2D g2 = (Graphics2D) g;
		g2.setColor(Color.BLACK);
		g2.fillRect(START_X - 1, START_Y - 1, (mazeDesign.numCols() * BOX_WIDTH) + INSET,
				(mazeDesign.numRows() * BOX_HEIGHT) + INSET);

		for (int i = 0; i < mazeDesign.numRows(); i++) {
			for (int j = 0; j < mazeDesign.numCols(); j++) {
				Color color;
				MazeCoord cord = new MazeCoord(i, j);
				if (mazeDesign.hasWallAt(cord)) {
					g2.setColor(Color.BLACK);
					g2.fillRect((BOX_WIDTH * j) + START_X, (BOX_HEIGHT * i) + START_Y, BOX_WIDTH, BOX_HEIGHT);
				} else {
					g2.setColor(Color.WHITE);
					g2.fillRect((BOX_WIDTH * j) + START_X, (BOX_HEIGHT * i) + START_Y, BOX_WIDTH, BOX_HEIGHT);// to idio
				}
			}
		}
		g2.setColor(Color.YELLOW);
		g2.fillRect(START_X + INSET + (BOX_WIDTH * mazeDesign.getEntryLoc().getCol()),
				START_Y + INSET + (BOX_HEIGHT * mazeDesign.getEntryLoc().getRow()), BOX_WIDTH - (INSET * 2),
				BOX_HEIGHT - (INSET * 2));
		g2.setColor(Color.GREEN);
		g2.fillRect(START_X + INSET + (BOX_WIDTH * mazeDesign.getExitLoc().getCol()),
				START_Y + INSET + (BOX_HEIGHT * mazeDesign.getExitLoc().getRow()), BOX_WIDTH - (INSET * 2),
				BOX_HEIGHT - (INSET * 2));

		LinkedList<MazeCoord> finalPath = mazeDesign.getPath();
		if (finalPath.size() == 0) {
			return;
		}
		ListIterator<MazeCoord> iter = finalPath.listIterator();
		MazeCoord curr = iter.next(); // curr is the current coordinate
		while (iter.hasNext()) {
			MazeCoord next = iter.next();
			g2.setColor(Color.BLUE);
			g2.drawLine(curr.getCol() * BOX_WIDTH + BOX_WIDTH / 2 + START_X,
					curr.getRow() * BOX_HEIGHT + BOX_HEIGHT / 2 + START_Y,
					next.getCol() * BOX_WIDTH + BOX_WIDTH / 2 + START_X,
					next.getRow() * BOX_HEIGHT + BOX_HEIGHT / 2 + START_Y);
			curr = next;
		}
	}

}
