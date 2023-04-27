DROP DATABASE IF EXISTS movies_ratings;
CREATE DATABASE movies_ratings;
USE movies_ratings;

CREATE TABLE movies (
    movie_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    description VARCHAR(200) NOT NULL,
    release_year INT NOT NULL,
    length DECIMAL NOT NULL,

    PRIMARY KEY (movie_id)
);

CREATE TABLE ratings (
    rating_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT NOT NULL,
    comment VARCHAR(200) NOT NULL,
    socre INT NOT NULL,

    PRIMARY KEY (rating_id),
    CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
        REFERENCES movies (movie_id)
        ON DELETE CASCADE
);