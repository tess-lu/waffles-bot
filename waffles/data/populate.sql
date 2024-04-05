-- populate.sql

-- Drop existing tables
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS gifs;

-- Create tables
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE gifs (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample question data
INSERT INTO questions (text, status) VALUES
    ('Sample pending question 1', 'pending'),
    ('Sample pending question 2', 'pending'),
    ('Sample pending question 3', 'pending'),
    ('Sample archived question 1', 'archived'),
    ('Sample archived question 2', 'archived'),
    ('Sample archived question 3', 'archived'),
    ('Sample delayed question 1', 'delayed'),
    ('Sample delayed question 2', 'delayed'),
    ('Sample delayed question 3', 'delayed'),
    ('Sample deleted question 1', 'deleted'),
    ('Sample deleted question 2', 'deleted'),
    ('Sample deleted question 3', 'deleted');

-- Insert GIF URLs
INSERT INTO gifs (url) VALUES
    ('http://forgifs.com/gallery/d/228932-2/Raccoon-gives-cat-food.gif'),
    ('https://media0.giphy.com/media/10eSPfhWNat2Xm/200w.gif'),
    ('https://media.tenor.com/vsmRFBP77_YAAAAM/cat-eating.gif'),
    ('https://media.tenor.com/IMYZL-7t2ucAAAAM/cat-butt.gif'),
    ('https://media.tenor.com/RMBrWjoO5dUAAAAM/cat-eating-fast.gif'),
    ('https://media.tenor.com/lq12HUSJY9sAAAAM/cat-kitty.gif'),
    ('https://i.gifer.com/1VLl.gif'),
    ('https://media.tenor.com/sUu2QVXex34AAAAd/cat-steal.gif'),
    ('https://gifgalaxy.com/storage/uploads/gifs/patkaimackajeduhranu.gif'),
    ('https://i.imgflip.com/4t7adv.gif'),
    ('https://media.tenor.com/bfpCE4UVnswAAAAC/cat-ringing.gif'),
    ('https://media.tenor.com/iWcBTUcwDq8AAAAM/cat-eating-cat.gif'),
    ('https://i.imgflip.com/3vvo6f.gif'),
    ('https://i.pinimg.com/originals/c4/6d/5f/c46d5f828d12de9544ce4a4939a63735.gif'),
    ('https://laughingsquid.com/wp-content/uploads/2017/10/cat-grabs-back-food-bowl.gif?w=468'),
    ('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmw4MnA3ajIwcXpvNTJycWFzMHQ1ZWdpc3A0MmxtMHZkcHlmb3B0OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d8pnch1sdXgmQ/giphy.gif'),
    ('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGx5djd0NG4zeHhxbzR3YXAwa2dyM284OWN6MWE3OGtsN2pqbXo2MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aOqVDcqUQt1BK/giphy-downsized-large.gif'),
    ('https://media.tenor.com/sUbf9lKFG8wAAAAd/cat-eat.gif'),
    ('https://gifdb.com/images/high/cute-white-cat-eating-strawberry-6rl4trimyrqvtbgc.gif'),
    ('https://1.bp.blogspot.com/-25BrAfMiDjY/YEQfPw512RI/AAAAAAAAOxY/040-VLCJ4Yk2B5US9C12jjQzHLE7L-p4gCLcBGAsYHQ/s16000/Funny%2BCat%2BGIF%2B%25E2%2580%25A2%2BAmazing%2Bvegan%2Bcat%2Beating%2Bhis%2Bdaily%2Bbanana.%2BMmmm%2Bit%2527s%2BDelicious%2B%255Bcat-gifs.com%255D.gif'),
    ('https://4.bp.blogspot.com/-lIF5zDKgO0A/XOW-Z7Gm--I/AAAAAAAAC_U/DSGY5WKW9WIE0OwEEu-lca-SsPsVA0NGQCLcBGAs/s1600/Hilarious%2BKitten%2BGIF%2B%25E2%2580%25A2%2BClumsy%2BMommy%2Bdidn%2527t%2Brealize%2Bshe%2Bsplashed%2Bmilk%2Bon%2Bthe%2Bkitten%2527s%2Bhead.gif'),
    ('https://media.tenor.com/wH2IUBQS5UwAAAAC/cat-cute.gif'),
    ('https://38.media.tumblr.com/ae53850f7ea9063f5cd42a3c0ba68a77/tumblr_nrzgsplauN1uzsb7xo1_500.gif'),
    ('https://media.tenor.com/VBzV6GGJbogAAAAd/cat-cat-eat.gif'),
    ('https://media.tenor.com/kTDi03sAbXEAAAAM/uwuanna-cats.gif'),
    ('https://media.tenor.com/Ea3D6joviD8AAAAM/cat-funny-cat.gif'),
    ('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGR4b25lZjNrZzE2d3dyYzNocW1iYWtjcGdkcmV3bHg3eTk0c2c5aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5f3XPhSmHYtG0pt8ec/giphy.gif'),
    ('https://media.tenor.com/Xo-xvADZWiUAAAAM/feeding-cat.gif'),
    ('https://h2.gifposter.com/gifs/animal/Cat-stealing-food.gif'),
    ('https://forgifs.com/gallery/d/213734-2/Kitten-steals-food.gif');
