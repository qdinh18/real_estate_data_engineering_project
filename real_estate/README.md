
## Core Models

### Dimension Models

1. **dim_broker**  
   Broker information with key attributes:  
   - `broker_id` (PK, not null, unique)  
   - `broker_name` (not null)  
   - `broker_rank`  
   - `update_date` (not null)

2. **dim_project**  
   Real estate project details:  
   - `project_id` (PK, not null, unique)  
   - `project_name`, `investor`, `address`  
   - `project_status`, `project_area_range`  
   - `number_of_apartments`, `number_of_buildings`  
   - `update_date` (not null)

3. **dim_post**  
   Property listing information:  
   - `post_id` (PK, not null, unique)  
   - `title`, `url` (not null)  
   - `price`, `posted_date`, `expired_date`  
   - `update_date` (not null)

### Fact Table

**fact_all_apartment**  
Transactional data with:  
- Foreign keys to all dimensions (`post_id`, `broker_id`, `project_id`)  
- Pricing details (`price`, `price_per_m²`)  
- Property specs (`area`, `bedroom`, `bathroom`)  
- Unit measurements (`price_unit`, `area_unit`)  
- `update_date` (not null)

## Data Sources

- **Raw Data**: `real_estate_raw.public.staging_table`  
- Configured in `models/staging/sources.yml`

## Configuration

### Database Connections
Configured in `profiles.yml` with support for:
- **PostgreSQL** 
- **Redshift** 

Example configuration:
```yaml
target: dev  # Set default environment
outputs:
  dev_postgres:  # Local Postgres
    type: postgres
    host: localhost
    dbname: re
    
  dev_redshift:  # AWS Redshift
    type: redshift
    host: [redshift-host]
    region: ap-southeast-2
    sslmode: verify-full
