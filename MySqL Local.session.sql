create DATABASE player_info;

-- @block
USE player_info

-- @block
CREATE TABLE player_stats (
    player_name VARCHAR(255),
    age INT,
    position VARCHAR(255),
    nation VARCHAR(255),
    team VARCHAR(255),
    market_value FLOAT
)



-- @block
SELECT * from player_stats