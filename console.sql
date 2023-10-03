create table Investor(
    investor_id integer primary key autoincrement,
    user_name text unique,
    password text
)

pragma foreign_keys = on

create table Stock(
    stock_id integer primary key autoincrement,
    symbol text,
    purchase_price real,
    purchase_date text,
    quantity real,
    investor_id integer,
    foreign key (investor_id) references Investor(investor_id)
)

drop table Stock

create table Bond(
    bond_id integer primary key autoincrement,
    symbol text,
    purchase_price real,
    purchase_date text,
    coupon real,
    yield real,
    quantity real,
    investor_id integer,
    foreign key (investor_id) references Investor(investor_id)
)