REVOKE CREATE ON SCHEMA public FROM PUBLIC;

create schema business;
 
create table business.financial (
    ts_id INTEGER not null,
	dt DATE NOT NULL,
	cust_id INTEGER not NULL,
	amt float not NULL,
	typ varchar(50) not NULL,
	descrip varchar(100) not NULL
);