-- =====================================================
-- DIMENSION TABLES
-- =====================================================

-- 1. DIM_BROKER
CREATE TABLE IF NOT EXISTS dim_broker (
    broker_id   INT NOT NULL,
    update_date DATE NOT NULL,
    broker_name TEXT NOT NULL,   
    broker_rank TEXT,
    PRIMARY KEY (broker_id, update_date)
);

-- 2. DIM_PROJECT
CREATE TABLE IF NOT EXISTS dim_project (
    project_id            INT NOT NULL,
    update_date           DATE NOT NULL,
    project_name          TEXT,
    investor              TEXT,
    project_area_range    TEXT,
    project_status        TEXT,
    address               TEXT,
    number_of_apartments  REAL,
    number_of_buildings   REAL,
    PRIMARY KEY (project_id, update_date)
);

-- 3. DIM_POST
CREATE TABLE IF NOT EXISTS dim_post (
    post_id      INT NOT NULL,
    update_date  DATE NOT NULL,
    title        TEXT NOT NULL,   
    url          TEXT,
    posted_date  DATE,           
    expired_date DATE,
    PRIMARY KEY (post_id, update_date)           
);

-- =====================================================
-- FACT TABLE: fact_all_apartment
-- Using (post_id, update_date_id) as composite PK
-- =====================================================

CREATE TABLE IF NOT EXISTS fact_all_apartment (
    -- Composite key columns
    post_id         INT NOT NULL,
    update_date     DATE NOT NULL,

    -- Other dimension FKs
    broker_id       INT NOT NULL,
    project_id      INT NOT NULL,

    -- Measures
    price                   FLOAT,
    price_unit              TEXT,  
    price_per_m²            FLOAT,
    price_per_m²_unit       TEXT,   
    area                    FLOAT,
    area_unit               TEXT,
    bedroom                 REAL,
    bathroom                REAL,

    -- Composite primary key
    PRIMARY KEY (post_id, update_date),

    -- Foreign Key constraints
    CONSTRAINT fk_post
      FOREIGN KEY (post_id, update_date)
      REFERENCES dim_post(post_id, update_date),

    CONSTRAINT fk_broker
      FOREIGN KEY (broker_id, update_date)
      REFERENCES dim_broker(broker_id, update_date),

    CONSTRAINT fk_project
      FOREIGN KEY (project_id, update_date)
      REFERENCES dim_project(project_id, update_date)
);

-- =====================================================
-- INDEXES on Foreign Keys
-- =====================================================

CREATE INDEX IF NOT EXISTS idx_fact_post_id
  ON fact_all_apartment(post_id);

CREATE INDEX IF NOT EXISTS idx_fact_broker_id
  ON fact_all_apartment(broker_id);

CREATE INDEX IF NOT EXISTS idx_fact_project_id
  ON fact_all_apartment(project_id);
