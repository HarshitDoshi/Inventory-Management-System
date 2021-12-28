-- Create Queries

CREATE TABLE supplier(
    id  INT     PRIMARY KEY     NOT NULL,
    name    VARCHAR(100)	NOT NULL,
    address     VARCHAR(250),
    phone   VARCHAR(250),
    email   VARCHAR(250)
);

CREATE TABLE category(
    id  INT     PRIMARY KEY     NOT NULL,
    name    VARCHAR(100)	NOT NULL,
    description     VARCHAR(250)
);

CREATE TABLE customer_group(
    id  INT     PRIMARY KEY     NOT NULL,
    name    VARCHAR(100)	NOT NULL
);

CREATE TABLE product(
    id  INT     PRIMARY KEY     NOT NULL,
    name    VARCHAR(100)	NOT NULL,
    price 	INT NOT NULL,
	supplier_id 	INT NOT NULL,
	category_id 	INT NOT NULL,
	FOREIGN KEY(supplier_id) REFERENCES supplier(supplier_id),
	FOREIGN KEY(category_id) REFERENCES category(category_id)
);

CREATE TABLE customer(
    id  INT     PRIMARY KEY     NOT NULL,
    first_name    VARCHAR(100)	NOT NULL,
    last_name    VARCHAR(100)	NOT NULL,
    address     VARCHAR(250),
    phone   VARCHAR(250),
    email   VARCHAR(250),
    group_id  INT     NOT NULL,
    FOREIGN KEY(group_id) REFERENCES customer_group(group_id)
);

CREATE TABLE product_order(
    id  INT     PRIMARY KEY     NOT NULL,
	customer_id  INT     NOT NULL,
	product_id  INT     NOT NULL,
	order_discount  INT,
	total_price  INT,
	order_date 	 DATETIME not null,
	FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
	FOREIGN KEY(product_id) REFERENCES product(product_id)
);

-- Insert Queries

INSERT INTO supplier VALUES (1, 'JSW Cement Ltd.', '17/306 (6) NH Road, Manapullikave, Palakkad – 678 013, India', '9847444411', 'jsw@gmail.com');
INSERT INTO supplier VALUES (2, 'ACC Cement Ltd.', 'Cement House. 121, Maharshi Karve Road Mumbai - 400 020, India', '+91-22-41593 321', 'acc@gmail.com');
INSERT INTO supplier VALUES (3, 'Ultratech Cement Ltd.', 'Gr. Floor, Ahura Centre, Mahakali Caves Road Andheri (East) Mumbai 400 093, India', '1800 210 3311', 'ultratech@gmail.com');
INSERT INTO supplier VALUES (4, 'Bangur Cement Ltd.', 'B-21 INDUSTRIAL ESTATE 22 GODOWN JAIPUR Jaipur RJ 302006, India', '092165 00270', 'ultratech@gmail.com');


INSERT INTO category VALUES (1, 'Portland Pozzolana Cement (PPC)', 'It is prepared by grinding pozzolanic clinker with Portland cement.');
INSERT INTO category VALUES (2, 'Ordinary Portland Cement (OPC)', 'It is the most widely used type of cement, which is suitable for all general concrete construction.');
INSERT INTO category VALUES (3, 'Rapid Hardening Cement (RHC)', 'Rapid hardening cement attains high strength in the early days; it is used in concrete where formworks are removed at an early stage and are similar to ordinary portland cement (OPC).	');
INSERT INTO category VALUES (4, 'Quick Setting Cement (QSC)', 'The difference between the quick setting cement and rapid hardening cement is that quick-setting cement sets earlier.');


INSERT INTO customer_group VALUES (1, 'Government Employee');
INSERT INTO customer_group VALUES (2, 'House Wife');
INSERT INTO customer_group VALUES (3, 'Army Personnel');
INSERT INTO customer_group VALUES (4, 'Private Job Employee');
INSERT INTO customer_group VALUES (5, 'Business Person');


INSERT INTO product VALUES (1, 'PPC Cement by ACC', 700, 2, 1);
INSERT INTO product VALUES (2, 'OPC Cement by JSW', 1000, 1, 2);
INSERT INTO product VALUES (3, 'RHC Cement by Ultratech', 1500, 3, 3);
INSERT INTO product VALUES (4, 'QSC Cement by Bangur', 1500, 4, 4);
INSERT INTO product VALUES (5, 'PPC Cement by Bangur', 750, 4, 1);
INSERT INTO product VALUES (6, 'OPC Cement by Ultratech', 9700, 3, 2);
INSERT INTO product VALUES (7, 'RHC Cement by JSW', 1700, 1, 3);
INSERT INTO product VALUES (8, 'QSC Cement by ACC', 1280, 2, 4);
INSERT INTO product VALUES (9, 'PPC Cement by JSW', 650, 1, 1);
INSERT INTO product VALUES (10, 'OPC Cement by ACC', 9700, 2, 2);
INSERT INTO product VALUES (11, 'RHC Cement by Bangur', 1400, 4, 3);
INSERT INTO product VALUES (12, 'QSC Cement by Ultratech', 1280, 2, 4);
INSERT INTO product VALUES (13, 'PPC Cement by Ultratech', 650, 2, 1);
INSERT INTO product VALUES (14, 'OPC Cement by Bangur', 9700, 4, 2);
INSERT INTO product VALUES (15, 'RHC Cement by ACC', 1400, 2, 3);
INSERT INTO product VALUES (16, 'QSC Cement by JSW', 1280, 1, 4);