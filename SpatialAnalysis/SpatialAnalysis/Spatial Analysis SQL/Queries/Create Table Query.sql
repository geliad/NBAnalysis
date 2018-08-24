CREATE TABLE Locations(Name varchar(30), Coordinates geometry);

INSERT INTO Locations VALUES
('Jeff/Vermont' , 'POINT(-118.291421 34.025386)'),
('Expo/Vermont' , 'POINT(-118.291422 34.018414)'),
('Expo/Figueora', 'POINT(-118.282340 34.018447)'),
('Jeff/Figueora', 'POINT(-118.280159 34.021885)'),
('Home' , 'POINT(-118.277964 34.027441)'),
('Leavey Lib' , 'POINT(-118.282982 34.021656)'),
('Tommy Trojan' , 'POINT(-118.285447 34.020565)'),
('RTH' , 'POINT(-118.289941 34.020331)'),
('Lyon Gym', 'POINT(-118.287979 34.024598)');

/*Using this query
SELECT Name, ST_AsText(Coordinates) FROM Locations;
I can see the table
*/




