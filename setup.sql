
-- Create task table

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128),
    subtitle VARCHAR(256),
    body TEXT,
    active BOOLEAN DEFAULT 1
);

--Create a couple of dummy records

INSERT INTO task (
    title,
    subtitle,
    body
) VALUES (
    "Wash the car",
    "Go outside and wash the car",
    "Either do it yourself or take it to car wash"
);

INSERT INTO task (
    title,
    subtitle,
    body
) VALUES (
    "Surfing",
    "Get wetsuit and wax board",
    "Walk down to beach and shred"
);