CREATE TABLE wildberries_product (
    name              VARCHAR   PRIMARY KEY                      NOT NULL,
    article           VARCHAR   UNIQUE                           NOT NULL,
    sale_price        INTEGER                                    NOT NULL,
    rating            INTEGER                                    NOT NULL,
    total_quantity    INTEGER                                    NOT NULL,
    create_date       TIMESTAMP WITHOUT TIME ZONE DEFAULT now()          ,
    update_date       TIMESTAMP WITHOUT TIME ZONE DEFAULT now()
);
