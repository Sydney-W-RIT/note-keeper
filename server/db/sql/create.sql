CREATE TABLE notes (
    id SERIAL NOT NULL, 
    title TEXT NOT NULL, -- could get rid of "NOT NULL" and instead "DEFAULT 'untitled'"
    content TEXT
);

-- CREATE TABLE daily_schedule (
--     id SERIAL NOT NULL, 
--     hour_of_day INTEGER NOT NULL, 
--     task TEXT
-- );

CREATE TABLE daily_schedule AS
SELECT generate_series(1, 24) AS hour_of_day;
ALTER TABLE daily_schedule
ADD COLUMN task TEXT;

-- make term unique?
CREATE TABLE flashcards (
    id SERIAL NOT NULL, 
    term TEXT NOT NULL, 
    solution TEXT NOT NULL, -- is definition a keyword?
    topic TEXT NOT NULL
);

CREATE TABLE pomodoro_timer (
    id SERIAL NOT NULL, 
    start_time TIMESTAMP NOT NULL, 
    end_time TIMESTAMP, 
    work_session BOOLEAN DEFAULT true
);