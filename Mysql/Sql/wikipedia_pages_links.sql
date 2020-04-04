CREATE TABLE `pages` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `url`  VARCHAR(255) NOT NULL,
    `created` timestamp NOT NULL default current_timestamp,
    primary key(`id`)
);

CREATE TABLE `links` (
	`id`  INT NOT NULL AUTO_INCREMENT,
    `fromPageId` INT NULL,
    `toPageId` INT NULL,
    `created` timestamp NOT NULL default current_timestamp,
    primary key(`id`)
);