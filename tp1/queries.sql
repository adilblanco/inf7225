SELECT DP.numDos, DP.nomP, DP.prenomP
FROM CONSULTATION C
INNER JOIN DOCTEUR D ON C.CodeDocteur = D.matricule
INNER JOIN DOSSIERPATIENT DP ON C.numDos = DP.numDos
WHERE D.nomM = 'Zaier' AND C.dateC = DATE '2022-06-01';

SELECT D.matricule, D.nomM, D.prenomM, S.titre AS TitreSpecialite
FROM DOCTEUR D
INNER JOIN CONSULTATION C ON D.matricule = C.CodeDocteur
INNER JOIN SPECIALITE S ON D.specialite = S.code
WHERE C.dateC >= DATE '2022-03-01' AND C.dateC < DATE '2022-04-01'

SELECT D.matricule, D.nomM, D.prenomM
FROM DOCTEUR D
WHERE D.matricule NOT IN (SELECT DISTINCT CodeDocteur FROM CONSULTATION);

SELECT M.idMed, M.nomMed, C.nom AS NomCategorie
FROM MEDICAMENT M
INNER JOIN CATEGORIES C ON M.idCategorie = C.IdCategorie
WHERE M.prix = (SELECT MAX(prix) FROM MEDICAMENT);

SELECT T.IdType, T.nom, T.Description, COUNT(*) AS NombreChirurgies
FROM CHIRURGIE C
INNER JOIN TYPECHIRGIE T ON C.idType = T.IdType
GROUP BY T.IdType, T.nom, T.Description;

SELECT S.idSalle, S.nom
FROM SALLE S
INNER JOIN CHIRURGIE C ON S.idSalle = C.idSalle
GROUP BY S.idSalle, S.nom
HAVING COUNT(*) > 0;

SELECT C1.idChir, C1.idType, C1.dateChirurgie
FROM CHIRURGIE C1
INNER JOIN CHIRURGIE C2 ON C1.idType = C2.idType 
AND C1.dateChirurgie = C2.dateChirurgie
WHERE C1.idChir <> C2.idChir;