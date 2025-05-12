Create model Author
--
CREATE TABLE `catalog_author` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `first_name` varchar(100) NOT NULL, `last_name` varchar(100) NOT NULL, `date_of_birth` date NULL, `date_of_death` date NULL);
--
-- Create model Genre
--
CREATE TABLE `catalog_genre` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(200) NOT NULL UNIQUE);
--
-- Create model Book
--
CREATE TABLE `catalog_book` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(200) NOT NULL, `summary` longtext NOT NULL, `isbn` varchar(13) NOT NULL UNIQUE, `author_id` bigint NULL);
--
-- Create model BookInstance
--
CREATE TABLE `catalog_bookinstance` (`id` char(32) NOT NULL PRIMARY KEY, `imprint` varchar(200) NOT NULL, `due_back` date NULL, `status` varchar(1) NOT NULL, `book_id` bigint NULL);
--
-- Create constraint genre_name_case_insensitive_unique on model genre
--
CREATE UNIQUE INDEX `genre_name_case_insensitive_unique` ON `catalog_genre` ((LOWER(`name`)));
--
-- Add field genre to book
--
CREATE TABLE `catalog_book_genre` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `book_id` bigint NOT NULL, `genre_id` bigint NOT NULL);
ALTER TABLE `catalog_book` ADD CONSTRAINT `catalog_book_author_id_b0849980_fk_catalog_author_id` FOREIGN KEY (`author_id`) REFERENCES `catalog_author` (`id`);
ALTER TABLE `catalog_bookinstance` ADD CONSTRAINT `catalog_bookinstance_book_id_69f93415_fk_catalog_book_id` FOREIGN KEY (`book_id`) REFERENCES `catalog_book` (`id`);
ALTER TABLE `catalog_book_genre` ADD CONSTRAINT `catalog_book_genre_book_id_genre_id_d15f6922_uniq` UNIQUE (`book_id`, `genre_id`);
ALTER TABLE `catalog_book_genre` ADD CONSTRAINT `catalog_book_genre_book_id_e5a77c43_fk_catalog_book_id` FOREIGN KEY (`book_id`) REFERENCES `catalog_book` (`id`);
ALTER TABLE `catalog_book_genre` ADD CONSTRAINT `catalog_book_genre_genre_id_77d7ffde_fk_catalog_genre_id` FOREIGN KEY (`genre_id`) REFERENCES `catalog_genre` (`id`);


 Create model Language
--
CREATE TABLE `catalog_language` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(200) NOT NULL UNIQUE);
--
-- Create constraint language_name_case_insensitive_unique on model language
--
CREATE UNIQUE INDEX `language_name_case_insensitive_unique` ON `catalog_language` ((LOWER(`name`)));
--
-- Add field language to book
--
ALTER TABLE `catalog_book` ADD COLUMN `language_id` bigint NULL , ADD CONSTRAINT `catalog_book_language_id_447f859e_fk_catalog_language_id` FOREIGN KEY (`language_id`) REFERENCES `catalog_language`(`id`);