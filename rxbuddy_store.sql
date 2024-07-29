--Run these before running this application
CREATE DATABASE rxbuddy_storeDB;

USE rxbuddy_storeDB;

CREATE TABLE roles (
    roleID INT AUTO_INCREMENT,
    roleName VARCHAR(255) NOT NULL,
    PRIMARY KEY (roleID)
);

INSERT INTO roles (roleID, roleName) VALUES (DEFAULT, 'Admin'),
    (DEFAULT, 'Patient'),
    (DEFAULT, 'Doctor');

CREATE TABLE accounts (
    accountID INT AUTO_INCREMENT,
    accountUsername VARCHAR(255) NOT NULL,
    accountPassword VARCHAR(255) NOT NULL, --In an actual database, NEVER store passwords, but hashing/encyrption/etc. is out of scope for this project.
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    balance DECIMAL(6, 2) NOT NULL,
    accountRole INT,
    PRIMARY KEY (accountID),
    FOREIGN KEY (accountRole) REFERENCES roles(roleID)
);

INSERT INTO accounts (accountID, accountUsername, accountPassword, firstName, lastName, balance, accountRole) VALUES (DEFAULT, 'admin', 'pass123', 'chad', 'dev', 0.00, 1);

CREATE TABLE medications (
    medicationID INT AUTO_INCREMENT,
    medicationName VARCHAR(255) UNIQUE NOT NULL, --I can add support for MongoDB querying for getting the description of any of these medications. Focus on MySQL.
    medicationCost DECIMAL(6, 2) NOT NULL,
    PRIMARY KEY (medicationID)
);

CREATE TABLE prescriptions (
    prescriptionID INT AUTO_INCREMENT,
    prescribedBy INT,
    prescribedTo INT,
    medicationID INT,
    PRIMARY KEY (prescriptionID),
    FOREIGN KEY (prescribedBy) REFERENCES accounts(accountID),
    FOREIGN KEY (prescribedTo) REFERENCES accounts(accountID),
    FOREIGN KEY (medicationID) REFERENCES medications(medicationID)
);

CREATE TABLE orders (
    orderID INT AUTO_INCREMENT,
    accountID INT NOT NULL,
    medicationID INT NOT NULL, 
    quantity INT NOT NULL,
    totalAmount DECIMAL(6, 2) NOT NULL, 
    PRIMARY KEY (orderID),
    FOREIGN KEY (accountID) REFERENCES accounts(accountID),
    FOREIGN KEY (medicationID) REFERENCES medications(medicationID)
);
-- The following were generated with a python script.
INSERT INTO medications (medicationID, medicationName, medicationCost) VALUES
(DEFAULT, 'trehalose dihydrate', 15.69),
(DEFAULT, 'molindone', 44.29),
(DEFAULT, 'sodium chloride', 26.43),
(DEFAULT, 'ontruzant', 21.55),
(DEFAULT, 'tussigon', 37.14),
(DEFAULT, 'kedbumin', 28.00),
(DEFAULT, 'collagen type i, bovine', 37.33),
(DEFAULT, 'imidurea', 9.44),
(DEFAULT, 'peg-8 dimethicone', 6.39),
(DEFAULT, 'osphena', 6.05),
(DEFAULT, 'micafungin', 10.79),
(DEFAULT, 'elevidys kit patient weight 16.5 - 17.4 kg', 44.34),
(DEFAULT, 'rivastigmine tartrate', 36.27),
(DEFAULT, 'aluminum chlorohydrate', 12.81),
(DEFAULT, 'TOLAZamide', 41.55),
(DEFAULT, 'summers eve medicated', 16.51),
(DEFAULT, 'propylene carbonate', 54.38),
(DEFAULT, 'emapalumab-lzsg', 21.04),
(DEFAULT, 'green olive allergenic extract', 24.30),
(DEFAULT, 'valACYclovir', 42.38),
(DEFAULT, '4-(p-hydroxyphenyl)-2-butanone', 44.10),
(DEFAULT, 'zinc chloride', 33.43),
(DEFAULT, 'propylene glycol 1,2-distearate', 38.28),
(DEFAULT, 'sage oil', 30.50),
(DEFAULT, 'aldioxa', 38.71),
(DEFAULT, 'c14-22 alcohols', 42.75),
(DEFAULT, 'baza cleanse and protect', 30.04),
(DEFAULT, 'ahist antihistamine', 8.97),
(DEFAULT, 'propranolol hydrochloride', 46.64),
(DEFAULT, 'cladosporium herbarum allergenic extract', 27.76),
(DEFAULT, 'trelstar', 48.01),
(DEFAULT, 'nitrate ion', 40.59),
(DEFAULT, 'tudorza', 54.27),
(DEFAULT, 'hibiscus syriacus bark extract', 42.35),
(DEFAULT, 'peg-55 propylene glycol oleate', 17.33),
(DEFAULT, 'bonine', 24.49),
(DEFAULT, 'imvexxy 4 mcg maintenance pack', 17.66),
(DEFAULT, 'amoxicillin anhydrous', 5.10),
(DEFAULT, 'citrus paradisi fruit oil', 14.61),
(DEFAULT, 'sheep sorrel pollen extract', 20.20),
(DEFAULT, 'cloNIDine hydrochloride', 38.47),
(DEFAULT, 'calcium carbonate', 29.60),
(DEFAULT, 'aspirin', 31.64),
(DEFAULT, 'methoxy peg ppg-7-3 aminopropyl dimethicone', 12.61),
(DEFAULT, 'homatropine methylbromide', 52.75),
(DEFAULT, 'c12-13 pareth-9', 6.55),
(DEFAULT, 'geraniol', 25.24),
(DEFAULT, '1,2-distearoyl-sn-glycero-3-(phospho-rac-(1-glycerol))', 15.13),
(DEFAULT, 'lovastatin', 18.62),
(DEFAULT, 'skyrizi 90 mg/1 ml x 4 (360 mg) dose prefilled syringe pack', 37.46),
(DEFAULT, 'histidine monohydrochloride', 41.20),
(DEFAULT, 'DACTINomycin', 45.41),
(DEFAULT, 'fd &c yellow #6 aluminum lake', 53.87),
(DEFAULT, 'tabasco pepper extract', 26.60),
(DEFAULT, 'methyl gluceth-10', 8.48),
(DEFAULT, 'peg-15 glyceryl stearate', 19.00),
(DEFAULT, 'buPROPion hydrochloride', 5.18),
(DEFAULT, 'increlex', 31.98),
(DEFAULT, 'pyrukynd 50 mg 4-week pack', 18.06),
(DEFAULT, 'nupercainal', 21.62),
(DEFAULT, 'danicopan', 22.33),
(DEFAULT, 'populus tremuloides bark extract', 13.83),
(DEFAULT, 'cambia', 44.74),
(DEFAULT, 'faslodex', 44.83),
(DEFAULT, 'goserelin', 29.77),
(DEFAULT, 'shark liver oil', 30.96),
(DEFAULT, 'linoleic acid', 43.37),
(DEFAULT, 'levamisole', 17.41),
(DEFAULT, 'ascorbic acid', 12.05),
(DEFAULT, 'coceth-7', 33.18),
(DEFAULT, 'qbrexza', 21.55),
(DEFAULT, 'urso forte', 8.45),
(DEFAULT, 'iloperidone', 24.59),
(DEFAULT, '1,2,6-hexanetriol', 35.48),
(DEFAULT, 'abacavir', 7.44),
(DEFAULT, 'chlorhexidine', 44.45),
(DEFAULT, 'duofilm', 41.18),
(DEFAULT, 'mesalamine', 6.34),
(DEFAULT, 'thyrogen kit (0.9 mg vial)', 50.84),
(DEFAULT, 'chondroitin sulfates', 37.93),
(DEFAULT, 'movantik', 53.36),
(DEFAULT, 'prezatide copper', 30.15),
(DEFAULT, 'duavee', 47.71),
(DEFAULT, 'streptococcus pneumoniae type 23f capsular polysaccharide antigen', 22.78),
(DEFAULT, 'indium in-111 pentetate disodium', 28.30),
(DEFAULT, 'carboxymethylcellulose', 24.62),
(DEFAULT, 'lopinavir', 31.15),
(DEFAULT, 'alogliptin', 53.15),
(DEFAULT, 'saw palmetto extract', 36.67),
(DEFAULT, 'sofosbuvir', 21.88),
(DEFAULT, 'bicnu', 44.16),
(DEFAULT, 'lymepak 14 tablet, 21 day supply', 45.28),
(DEFAULT, 'efgartigimod alfa', 52.77),
(DEFAULT, 'risedronate sodium monohydrate', 43.64),
(DEFAULT, 'psoriasin wash', 27.82),
(DEFAULT, 'medicone', 20.79),
(DEFAULT, 'alanine', 34.52),
(DEFAULT, 'telavancin hydrochloride', 13.93),
(DEFAULT, 'jinteli', 50.78),
(DEFAULT, 'hazelnut allergenic extract', 15.92);
