
SELECT DISTINCT l1.Name, l2.Name, ST_DISTANCE(l1.Coordinates,l2.Coordinates)
FROM Locations AS l1, Locations AS l2  
WHERE l1.Name = 'Home' 
ORDER BY l1.Name, ST_Distance(l1.Coordinates,l2.Coordinates)
LIMIT 10;

/*I print out 3 columns, where the first and the second are the names
of the locations that are being compared for the distance.
I also included Home in the second column to make sure my query works
correctly, that's why I use limit 4 instead of 3.
*/

