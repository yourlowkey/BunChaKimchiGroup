CREATE TABLE users (
    id serial PRIMARY KEY,
    username character varying NOT NULL,
    password character varying NOT NULL,
    gender character varying NOT NULL,
    phone_number character varying NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    image_path TEXT NOT NULL,
    hash_tag VARCHAR(255) NOT NULL,
    user_id INTEGER REFERENCES users(id) NOT NULL
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comments VARCHAR(255) NOT NULL,
    post_id INTEGER REFERENCES posts(id) NOT NULL
);