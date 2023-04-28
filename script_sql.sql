DROP DATABASE IF EXISTS movies_ratings;
CREATE DATABASE movies_ratings;
USE movies_ratings;

DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
    movie_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    tipo VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    release_year INT NOT NULL,
    director VARCHAR(80) NOT NULL,
    length DECIMAL NOT NULL,

    PRIMARY KEY (movie_id)
);

-- Cria tabela 
DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (
    rating_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT NOT NULL,
    comment VARCHAR(200) NOT NULL,
    score INT NOT NULL,

    PRIMARY KEY (rating_id),
    CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
        REFERENCES movies (movie_id)
        ON DELETE CASCADE
);

-- Insere alguns dados na tabela movies : 
INSERT INTO 
    movies (name, tipo,  description, release_year, director , length) 
VALUES 
    ('Orgulho e preconceito', 'Drama' , 'Elizabeth Bennet mora com a mãe, o pai e as irmãs no interior da Inglaterra. Como filha mais velha, ela enfrenta uma pressão crescente dos pais para se casar.' , 2005 , 'Joe Wright' , 127),
    ('Titanic', 'Drama/Romance' , 'Um artista pobre e uma jovem rica se conhecem e se apaixonam na fatídica viagem do Titanic, em 1912. Embora esteja noiva do arrogante herdeiro de uma siderúrgica, a jovem desafia sua família e amigos em busca do verdadeiro amor.' , 1998 , 'James Cameron' , 194);

-- Insere alguns dados na tabela rating :
INSERT INTO 
    ratings (movie_id, comment,  score) 
VALUES
    (1, 'Ótimo filme , chorei muito' , 5),
    (2, 'Cabia mais uma pessoa na porta ... ' , 4);
