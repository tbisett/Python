USE [dojos_and_ninjas];
INSERT INTO Dojos (name, created_at, updated_at)
VALUES ("Bellevue Dojo", NOW(), NOW());

INSERT INTO Dojos (name, created_at, updated_at)
VALUES ("Austin Dojo", NOW(), NOW());

INSERT INTO Dojos (name, created_at, updated_at)
VALUES ("Los Angeles Dojo", NOW(), NOW());

SET SQL_SAFE_UPDATES = 0;

DELETE FROM Dojos;

SELECT * FROM Dojos;

INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Taylor", "BISETT", 26, NOW(), NOW(), 4);
	
INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Ninja", "One", 28, NOW(), NOW(), 4);

INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Ninja", "Two", 22, NOW(), NOW(), 4);

SELECT * FROM Ninjas;

INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Ninja", "Three", 26, NOW(), NOW(), 5);

INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Ninja", "Four", 26, NOW(), NOW(), 5);

INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Ninja", "Five", 26, NOW(), NOW(), 5);

INSERT INTO Ninjas (first_name, last_name, age, created_at, updated_at, Dojo_id)
VALUES ("Ninja", "Six", 21, NOW(), NOW(), 6),
		("Ninja", "Seven", 22, NOW(), NOW(), 6),
        ("Ninja", "Eight", 19, NOW(), NOW(), 6);

SELECT first_name, last_name FROM ninjas WHERE Dojo_id = 6;

SELECT Dojo_id from ninjas WHERE id = 9;

SELECT * FROM ninjas
JOIN Dojos on Dojos.id = ninjas.dojo_id;

SELECT name FROM Dojos 

