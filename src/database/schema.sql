
CREATE TABLE IF NOT EXISTS server_blocks (
    id VARCHAR(255) PRIMARY KEY,
    server_name VARCHAR(100) NOT NULL,
    app_root VARCHAR(512) NOT NULL
)