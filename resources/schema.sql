-- Lantern Trails: questions table + seed data
-- difficulty: 1 = easy, 2 = medium, 3 = hard
-- character : NULL  -> the hint is shown to every player
--             name  -> the hint is shown only when playing that character
--                      (must match the name in your characters list exactly)
-- answer    : stored lowercase; normalise player input the same way
--             (strip spaces, lowercase, drop a leading "the"/"a"/"an")

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS questions;

CREATE TABLE questions (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    room       TEXT    NOT NULL
               CHECK (room IN ('Corps Armory', 'Will Forge', 'Garden of Mogo', 'Void of Fear')),
    difficulty INTEGER NOT NULL
               CHECK (difficulty BETWEEN 1 AND 3),
    question   TEXT    NOT NULL UNIQUE,
    answer     TEXT    NOT NULL,
    hint       TEXT,
    character  TEXT,
    CHECK (character IS NULL OR hint IS NOT NULL)
);

CREATE INDEX idx_questions_room_difficulty ON questions (room, difficulty);

INSERT INTO questions (room, difficulty, question, answer, hint, character) VALUES

-- Corps Armory
('Corps Armory', 1,
 'Lanterns recharge their rings at a giant power ____ shaped like a lantern. What is the missing word?',
 'battery', 'Think of what keeps your phone alive.', NULL),
('Corps Armory', 2,
 'Which city is Hal Jordan''s hometown?',
 'coast city', 'You learned to fly here, right beside the sea.', 'Hal Jordan'),

-- Will Forge
('Will Forge', 1,
 'What color is the light of willpower?',
 'green', 'Look at the ring on your finger.', NULL),
('Will Forge', 1,
 'What planet is the home of the Green Lantern Corps?',
 'oa', 'You drilled rookies here every single day.', 'Kilowog'),
('Will Forge', 2,
 'What do Lanterns recite while charging their rings?',
 'oath', 'A short promise, spoken aloud.', NULL),
('Will Forge', 2,
 'What are the immortal beings who founded the Green Lantern Corps called?',
 'guardians', 'They guard the universe, right there in the name.', NULL),
('Will Forge', 2,
 'What do Lanterns call the objects they create from ring energy?',
 'constructs', 'Things that are built.', NULL),
('Will Forge', 3,
 'Earth''s Green Lanterns patrol which space sector number?',
 '2814', 'Four digits, and it starts with 28.', 'John Stewart'),

-- Garden of Mogo
('Garden of Mogo', 1,
 'What color is the light of hope?',
 'blue', 'The color of a clear sky.', NULL),
('Garden of Mogo', 1,
 'Mogo is a Green Lantern, but he is also a living what?',
 'planet', 'He is enormous and round, and you are standing on him.', NULL),
('Garden of Mogo', 2,
 'I am what you hold on to when everything seems lost, and I shine blue. What am I?',
 'hope', 'It rhymes with rope, and you hold on to it.', NULL),
('Garden of Mogo', 2,
 'What color is the light of love on the emotional spectrum?',
 'violet', 'The last color of the rainbow.', NULL),
('Garden of Mogo', 3,
 'What color is the light of compassion?',
 'indigo', 'It sits between blue and violet. You know it well.', 'Jessica Cruz'),

-- Void of Fear
('Void of Fear', 1,
 'What color is the light of fear?',
 'yellow', 'You have faced this feeling and kept going. Think of warning signs.', 'Jessica Cruz'),
('Void of Fear', 1,
 'The more of me there is, the less you can see. What am I?',
 'darkness', 'Switch off the lights.', NULL),
('Void of Fear', 2,
 'What gets bigger the more you take away from it?',
 'hole', 'You dig it.', NULL),
('Void of Fear', 2,
 'Which former Green Lantern, once Hal Jordan''s mentor, started a Corps powered by fear?',
 'sinestro', 'His name starts with S, and he wears yellow.', NULL),
('Void of Fear', 3,
 'What is the name of the fear entity that once possessed Hal Jordan?',
 'parallax', 'You carried it inside you once. Its name is also an optics term.', 'Hal Jordan');

-- Handy queries to try (uncomment to run):
-- SELECT COUNT(*) FROM questions;
-- SELECT room, COUNT(*) FROM questions GROUP BY room;
-- SELECT * FROM questions WHERE room = 'Will Forge' ORDER BY difficulty;
-- SELECT question, answer FROM questions WHERE room = 'Void of Fear' ORDER BY RANDOM() LIMIT 1;
-- Hint for the current player: general hint, or one meant for their character
-- SELECT hint FROM questions WHERE id = 5 AND (character IS NULL OR character = 'Hal Jordan');