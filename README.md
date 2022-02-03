Neo4j mapping of TPG Systems

# Requirements
- docker
- python3
- pipenv

# Setup

Get source data (not stored in this repository for client confidentiality reasons) from 
`https://twodegrees1.sharepoint.com/:x:/r/teams/TPGTMigration/Shared%20Documents/General/Apps%20Analysis/TPG%20Dependency%20Matrix%20-%20Provider%20Consumer.xlsx?d=w3a8f156ef81e4d08b86b06b5a6812473&csf=1&web=1&e=ZHZbc7`

Save it in this directory as "TPG Dependency Matrix - Provider Consumer.xlsx"

Run `pipenv install && pipenv shell && python3 ./xls2cypher.py > tpg.cypher` to generate the cypher statements, which will be used to populate the db

`make container` will start neo4j container running

http://localhost:7474 to connect to neo4j

Initial password is 'neo4j' after which you will be asked to change it. Change it to 'k' (this is hardcoded in the population command in Makefile)

`make load`

Refresh your neo4j window to view

An example cypher query to find all systems containing "Frontier" would be `MATCH (n) where n.name =~ '.*Frontier.*' RETURN n LIMIT 250`

# References
https://neo4j.com/docs/cypher-manual/current/
