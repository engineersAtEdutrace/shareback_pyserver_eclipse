--THIS


BEGIN;
--
-- Create model Feedbacks
--
CREATE TABLE "feedbacks" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
--
-- Create model SessionFiles
--
CREATE TABLE "session_files" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
--
-- Create model Sessions
--
CREATE TABLE "sessions" ("session_id" varchar(32) NOT NULL PRIMARY KEY, "session_name" varchar(120) NOT NULL, "timestamp" date NOT NULL, "rating_1" integer NOT NULL, "rating_2" integer NOT NULL, "rating_3" integer NOT NULL, "rating_4" integer NOT NULL, "rating_5" integer NOT NULL);
--
-- Add field session_id to sessionfiles
--
ALTER TABLE "session_files" RENAME TO "session_files__old";
CREATE TABLE "session_files" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "session_id" varchar(32) NOT NULL REFERENCES "sessions" ("session_id"));
INSERT INTO "session_files" ("id", "session_id") SELECT "id", NULL FROM "session_files__old";
DROP TABLE "session_files__old";
CREATE INDEX "session_files_7fc8ef54" ON "session_files" ("session_id");
--
-- Add field session_id to feedbacks
--
ALTER TABLE "feedbacks" RENAME TO "feedbacks__old";
CREATE TABLE "feedbacks" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "session_id" varchar(32) NOT NULL REFERENCES "sessions" ("session_id"));
INSERT INTO "feedbacks" ("id", "session_id") SELECT "id", NULL FROM "feedbacks__old";
DROP TABLE "feedbacks__old";
CREATE INDEX "feedbacks_7fc8ef54" ON "feedbacks" ("session_id");
COMMIT;