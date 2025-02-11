/*QUERIES*/

CREATE DATABASE etlgamesdb;

CREATE TABLE games(
id serial primary key,
name varchar(185) NOT NULL,
developers varchar(100) not null,
publishers varchar(100) not null,
is_released boolean DEFAULT FALSE,
release_date DATE DEFAULT CURRENT_DATE,
total_reviews INT NOT NULL DEFAULT 0,
total_positive INT NOT NULL DEFAULT 0,
total_negative INT NOT NULL DEFAULT 0,
review_score FLOAT NOT NULL DEFAULT 0.0,
positive_percentual FLOAT NOT NULL DEFAULT 0.0,
metacritic INT NOT NULL DEFAULT 0,
is_free boolean DEFAULT false,
price_initial FLOAT not null DEFAULT 0.00
);