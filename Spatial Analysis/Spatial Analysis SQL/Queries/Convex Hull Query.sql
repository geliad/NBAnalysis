
SELECT ST_AsText(ST_ConvexHull(ST_Collect(Coordinates)))
FROM Locations;
