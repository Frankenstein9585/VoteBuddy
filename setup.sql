-- sql script


CREATE DATABASE IF NOT EXISTS SWBuddy;
       CREATE USER IF NOT EXISTS 'vote_buddy'@'localhost' IDENTIFIED BY 'votebuddy123';
              GRANT ALL PRIVILEGES ON SWBuddy.* TO 'vote_buddy'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'vote_buddy'@'localhost';
FLUSH PRIVILEGES;