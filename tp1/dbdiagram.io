Table SPECIALITE {
  code number [pk]
  titre varchar
  description varchar 
}

Table CATEGORIES {
  IdCategorie number [pk]
  nom varchar
  description varchar
}

Table SALLE {
  idSalle number [pk]
  nom varchar
}

Table TYPECHIRGIE {
    IdType number [pk]
    nom varchar unique
    description varchar
}

Table DOCTEUR {
    matricule number [pk]
    nomM varchar
    prenomM varchar
    specialite number [ref: > SPECIALITE.code]
    ville varchar
    adresse varchar
    niveau varchar
}

Table ORDONNANCE {
    numOrd number [pk]
    recommandations varchar
    typeOrd varchar
    dateC date
    numOrdPrinc number [ref: > ORDONNANCE.numOrd]
}

Table CHIRURGIE {
    idChir number [pk]
    idType number [ref: > TYPECHIRGIE.IdType]
    idSalle number [ref : > SALLE.idSalle]
    dateChirurgie date
    HeureDebut number
    HeureFin number
}

Table ORDONNANCECHIRURGIE {
    numOrd number [ref: > ORDONNANCE.numOrd]
    idChir number [ref: > CHIRURGIE.idChir]
    rang number
    indexes {
      (numOrd, idChir) [pk]
    }
}

Table SPECIALISATIONSALLE {
    IdType number [ref: > TYPECHIRGIE.IdType]
    idSalle number [ref: > SALLE.idSalle]
    dateC date
    indexes {
        (IdType, idSalle) [pk]
    }
}

Table MEDICAMENT {
    idMed number [pk]
    nomMed varchar
    prix number
    idCategorie number [ref: > CATEGORIES.IdCategorie]
}

Table DOSSIERPATIENT {
    numDos number [pk]
    nomP varchar
    prenomP varchar
    NomJeuneFille varchar
    genre char(1)
    numAS number
    dateNaiss date
    dateC date
    matricule number [ref: > DOCTEUR.matricule]
}

Table CONSULTATION {
    CodeDocteur number [ref: > DOCTEUR.matricule]
    numDos number [ref: > DOSSIERPATIENT.numDos]
    dateC date
    diagnostic varchar
    numOrd number [ref: > ORDONNANCE.numOrd]
    indexes {
        (CodeDocteur, numDos, dateC) [pk]
    }
}

Table ORDONNANCEMEDICAMENTS {
    numOrd number [ref: > ORDONNANCE.numOrd]
    idMed number [ref: > MEDICAMENT.idMed]
    nbBoites number
    indexes {
        (numOrd, idMed) [pk]
    }
}

