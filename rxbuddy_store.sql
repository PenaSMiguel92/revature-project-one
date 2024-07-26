--Run these before running this application
CREATE DATABASE rxbuddy_storeDB;

USE rxbuddy_storeDB;

CREATE TABLE roles (
    roleID INT AUTO_INCREMENT PRIMARY KEY,
    roleName VARCHAR(255) NOT NULL
);

INSERT INTO roles (roleID, roleName) VALUES (DEFAULT, 'Admin'),
    (DEFAULT, 'Patient'),
    (DEFAULT, 'Doctor');

CREATE TABLE accounts (
    accountID INT AUTO_INCREMENT PRIMARY KEY,
    accountUsername VARCHAR(255) NOT NULL,
    accountPassword VARCHAR(255) NOT NULL, --In an actual database, NEVER store passwords, but hashing/encyrption/etc. is out of scope for this project.
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    accountRole INT,
    FOREIGN KEY (accountRole) REFERENCES roles(roleID)
);

INSERT INTO accounts (accountID, accountUsername, accountPassword, firstName, lastName, accountRole) VALUES (DEFAULT, 'admin', 'pass123', 'chad', 'dev', 1);

CREATE TABLE medications (
    medicationID INT AUTO_INCREMENT PRIMARY KEY,
    medicationName VARCHAR(255) UNIQUE NOT NULL, --I can add support for MongoDB querying for getting the description of any of these medications. Focus on MySQL.
    medicationCost DECIMAL(5, 2) NOT NULL
);

CREATE TABLE prescriptions (
    prescriptionID INT AUTO_INCREMENT PRIMARY KEY,
    prescribedBy INT,
    prescribedTo INT,
    medicationID INT,
    FOREIGN KEY (prescribedBy) REFERENCES accounts(accountID),
    FOREIGN KEY (prescribedTo) REFERENCES accounts(accountID),
    FOREIGN KEY (medicationID) REFERENCES medications(medicationID)
);

CREATE TABLE orders (
    orderID INT AUTO_INCREMENT PRIMARY KEY,
    accountID INT NOT NULL,
    medicationID INT NOT NULL, 
    quantity INT NOT NULL,
    total_sales DECIMAL(6, 2) NOT NULL, 
    FOREIGN KEY (accountID) REFERENCES accounts(accountID),
    FOREIGN KEY (medicationID) REFERENCES medications(medicationID)
);



