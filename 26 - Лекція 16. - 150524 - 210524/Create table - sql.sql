CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    user_type VARCHAR(10) CHECK (user_type IN ('host', 'guest')) NOT NULL
);

CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    capacity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    ac BOOLEAN NOT NULL,
    refrigerator BOOLEAN NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES Users(user_id)
);

CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),
    FOREIGN KEY (room_id)
        REFERENCES Rooms(room_id)
);

CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    room_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),
    FOREIGN KEY (room_id)
        REFERENCES Rooms(room_id)
);



INSERT INTO Users (username, email, password, user_type) VALUES
    ('host1', 'host1@example.com', 'password1', 'host'),
    ('host2', 'host2@example.com', 'password2', 'host'),
    ('guest1', 'guest1@example.com', 'password3', 'guest');


INSERT INTO Rooms (user_id, capacity, price, ac, refrigerator) VALUES
    (1, 2, 100.00, TRUE, TRUE),
    (1, 4, 150.00, TRUE, TRUE),
    (2, 3, 120.00, TRUE, FALSE);


INSERT INTO Reservations (user_id, room_id, check_in, check_out) VALUES
    (3, 1, '2024-05-15', '2024-05-20'),
    (3, 2, '2024-06-01', '2024-06-05'),
    (3, 3, '2024-07-10', '2024-07-15');


INSERT INTO Reviews (user_id, room_id, rating, comment) VALUES
    (3, 1, 5, 'Great place to stay!'),
    (3, 2, 4, 'Nice room but noisy at night.'),
    (3, 3, 4, 'Cozy room, but lacks a refrigerator.');



SELECT u.user_id, u.username
FROM (
    SELECT user_id, COUNT(*) AS reservation_count
    FROM Reservations
    GROUP BY user_id
    ORDER BY reservation_count DESC
    LIMIT 1
) AS max_reservation
JOIN Users u ON max_reservation.user_id = u.user_id;


