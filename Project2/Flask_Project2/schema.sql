DROP TABLE IF EXISTS logs;

CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visited TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    req_url TEXT NOT NULL
);