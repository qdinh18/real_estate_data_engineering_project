DROP TABLE IF EXISTS dim_broker, dim_post, dim_project, fact_all_apartment CASCADE;
-- =====================================================
-- STAGING TABLE
-- =====================================================
CREATE TABLE IF NOT EXISTS staging_table (
    title           TEXT,
    price_per_m²    FLOAT,
    project_name    TEXT,
    address         TEXT,
    price           FLOAT,
    area            FLOAT,
    bedroom         REAL,
    bathroom        REAL,
    url             TEXT,
    posted_date     DATE,
    expired_date    DATE,
    project_status  TEXT,
    investor        TEXT,
    broker_name     TEXT,
    broker_rank     TEXT,
    project_area_range     TEXT,
    number_of_apartments   REAL,
    number_of_buildings    REAL,
    update_date     DATE NOT NULL
);
