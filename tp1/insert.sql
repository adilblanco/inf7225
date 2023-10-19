INSERT INTO SPECIALITE (code, titre, description) VALUES (1, 'Cardiologie', 'Sp ́ecialit ́e en cardiologie');
INSERT INTO SPECIALITE (code, titre, description) VALUES (2, 'Dermatologie', 'Sp ́ecialit ́e en dermatologie');

INSERT INTO CATEGORIES (IdCategorie, nom, description) VALUES (1, 'Analgesiques', 'M ́edicaments pour la douleur');
INSERT INTO CATEGORIES (IdCategorie, nom, description) VALUES (2, 'Antibiotiques', 'M ́edicaments antibiotiques');
INSERT INTO CATEGORIES (IdCategorie, nom, description) VALUES (3, 'Anti-inflammatoires', 'M ́edicaments anti-inflammatoires');

INSERT INTO SALLE (idSalle, nom) VALUES (101, 'Salle 1');
INSERT INTO SALLE (idSalle, nom) VALUES (102, 'Salle 2');
INSERT INTO SALLE (idSalle, nom) VALUES (103, 'Salle 3');
INSERT INTO SALLE (idSalle, nom) VALUES (104, 'Salle 4');

INSERT INTO TYPECHIRURGIE (IdType, nom, Description) VALUES (1, 'Chirurgie cardiaque', 'Chirurgie du cœur');
INSERT INTO TYPECHIRURGIE (IdType, nom, Description) VALUES (2, 'Chirurgie dermatologique', 'Chirurgie de la peau');
INSERT INTO TYPECHIRURGIE (IdType, nom, Description) VALUES (3, 'Chirurgie orthop ́edique', 'Chirurgie des os et des articulations');
INSERT INTO TYPECHIRURGIE (IdType, nom, Description) VALUES (4, 'Chirurgie neurologique', 'Chirurgie du syst`eme nerveux');

INSERT INTO DOCTEUR (matricule, nomM, prenomM, specialite, ville, adresse, niveau) VALUES (101, 'Zaier', 'Zied', 1, 'Montr ́eal', '123 Rue de la Sant ́e', 'Docteur');
INSERT INTO DOCTEUR (matricule, nomM, prenomM, specialite, ville, adresse, niveau) VALUES (102, 'Godin', 'Robert', 2, 'Montr ́eal', '123 Rue de la Sant ́e', 'Docteur');
INSERT INTO DOCTEUR (matricule, nomM, prenomM, specialite, ville, adresse, niveau) VALUES (103, 'joe', 'Doe', 2, 'Montr ́eal', '123 Rue de la Sant ́e', 'Docteur');

INSERT INTO ORDONNANCE (numOrd, recommandations, typeOrd, dateC, numOrdPrinc) VALUES (1, 'Repos complet', 'M ́edicaments', SYSDATE, NULL);
INSERT INTO ORDONNANCE (numOrd, recommandations, typeOrd, dateC, numOrdPrinc) VALUES (2, 'Aucune', 'Chirurgie', SYSDATE, NULL);

INSERT INTO MEDICAMENT (idMed, nomMed, prix, idCategorie) VALUES (1, 'Parac ́etamol', 5.99, 1);
INSERT INTO MEDICAMENT (idMed, nomMed, prix, idCategorie) VALUES (2, 'Amoxicilline', 10.49, 2);
INSERT INTO MEDICAMENT (idMed, nomMed, prix, idCategorie) VALUES (3, 'Asperin', 9.99, 2);

INSERT INTO DOSSIERPATIENT (numDos, nomP, prenomP, NomJeuneFille, genre, numAS, dateNaiss, dateC, matricule) VALUES (1001, 'Durand', 'Alice', 'Dupont', 'F', 1234567890, TO_DATE('1990-05-15', 'YYYY-MM-DD'), TO_DATE('2022-06-01', 'YYYY-MM-DD'), 101);
INSERT INTO DOSSIERPATIENT (numDos, nomP, prenomP, NomJeuneFille, genre, numAS, dateNaiss, dateC, matricule) VALUES (1002, 'Leclerc', 'Paul', NULL, 'M', 9876543210, TO_DATE('1985-09-20', 'YYYY-MM-DD'), TO_DATE('2022-03-01', 'YYYY-MM-DD'), 102);

INSERT INTO CHIRURGIE (idChir, idType, idSalle, dateChirurgie, HeureDebut, HeureFin) VALUES (1, 1, 101, TO_DATE('2022-06-15', 'YYYY-MM-DD'), 900, 1300);
INSERT INTO CHIRURGIE (idChir, idType, idSalle, dateChirurgie, HeureDebut, HeureFin) VALUES (2, 1, 101, TO_DATE('2022-06-15', 'YYYY-MM-DD'), 1400, 1800);
INSERT INTO CHIRURGIE (idChir, idType, idSalle, dateChirurgie, HeureDebut, HeureFin) VALUES (3, 3, 102, TO_DATE('2022-06-16', 'YYYY-MM-DD'), 1000, 1300);
INSERT INTO CHIRURGIE (idChir, idType, idSalle, dateChirurgie, HeureDebut, HeureFin) VALUES (4, 4, 103, TO_DATE('2022-06-17', 'YYYY-MM-DD'), 1100, 1400);

INSERT INTO CONSULTATION (CodeDocteur, numDos, dateC, diagnostic, numOrd) VALUES (101, 1001, TO_DATE('2022-06-01', 'YYYY-MM-DD'), 'Fi`evre', 1);
INSERT INTO CONSULTATION (CodeDocteur, numDos, dateC, diagnostic, numOrd) VALUES (102, 1002, TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'Rash cutan ́e', 2);

INSERT INTO ORDONNANCECHIRURGIE (numOrd, idChir, rang)  VALUES (1, 1, 1);
INSERT INTO ORDONNANCECHIRURGIE (numOrd, idChir, rang)  VALUES (1, 2, 2);
INSERT INTO ORDONNANCECHIRURGIE (numOrd, idChir, rang)  VALUES (2, 3, 1);
INSERT INTO ORDONNANCECHIRURGIE (numOrd, idChir, rang)  VALUES (2, 4, 2);

INSERT INTO SPECIALISATIONSALLE (IdType, idSalle, dateC) VALUES (1, 101, SYSDATE);
INSERT INTO SPECIALISATIONSALLE (IdType, idSalle, dateC) VALUES (2, 102, SYSDATE);
INSERT INTO SPECIALISATIONSALLE (IdType, idSalle, dateC) VALUES (3, 103, SYSDATE);
INSERT INTO SPECIALISATIONSALLE (IdType, idSalle, dateC) VALUES (4, 104, SYSDATE);

INSERT INTO ORDONNANCEMEDICAMENTS (numOrd, idMed, nbBoites) VALUES (1, 1, 2);
INSERT INTO ORDONNANCEMEDICAMENTS (numOrd, idMed, nbBoites) VALUES (2, 2, 1);
