drop database if exists awesome;
create datebase awesome;
use awesome;
grant select,
    insert,
    update,
    delete on awesome.* to 'www-data' @'localhost' identified by 'www-data';
create table users(
    `id` varchar(50) not null,
    `email` varchar(50) not NULL,
    `passwd` VARCHAR(50) not null,
    `admin` bool not null,
    `name` VARCHAR(50) not null,
    `image` VARCHAR(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`) key `idx_created_at`(`created_at`),
    primary key (`id`)
) engine = InnoDB default charset = utf8;
create table blogs(
    `id` varchar(50) not null,
    `user_id` varchar(50) not NULL,
    `user_name` VARCHAR(50) not null,
    `user_image` VARCHAR(50) not null,
    `name` VARCHAR(50) not null,
    `summary` VARCHAR(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine = InnoDB default charset = utf8;
create table comments(
    `id` varchar(50) not null,
    `blog_id` VARCHAR(50) not null,
    `user_id` varchar(50) not NULL,
    `user_name` VARCHAR(50) not null,
    `user_image` VARCHAR(50) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine = InnoDB default charset = utf8;