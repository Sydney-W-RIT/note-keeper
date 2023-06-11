INSERT INTO notes (title, content)
VALUES ("title", "content");

INSERT INTO daily_schedule (task) 
VALUES ("start")
WHERE hour_of_day=1;

INSERT INTO flashcards (term, solution, topic) 
VALUES ("term", "solution", "general topics");

INSERT INTO pomodoro_timer (start_time, work_session)
VALUES (NOW(), true); -- can use NOW() or CURRENT_TIMESTAMP
