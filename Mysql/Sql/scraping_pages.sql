CREATE TABLE pages(
	id BIGINT(7) NOT NULL auto_increment,
    title VARCHAR(200),
    content VARCHAR(10000),
    created timestamp default current_timestamp, primary key(id)
);
