container:
	docker run --name neo4j_tpg -p7474:7474 -p7473:7473 -p7687:7687 --rm -ti neo4j

setpass:
	#echo "ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'neo4j'" | docker exec --interactive neo4j_tpg cypher-shell -u neo4j -p neo4j
	echo neo4j | docker exec -i neo4j_tpg cypher-shell -u neo4j -p neo4j -d system --change-password
	#curl -H "Content-Type: application/json" -X POST -d '{"password":"k"}' -u neo4j:neo4j http://localhost:7474/user/neo4j/password


load:
	cat tpg.cypher | docker exec --interactive neo4j_tpg cypher-shell -u neo4j -p k

regenerate_cypher:
	./xls2cypher.py > tpg.cypher
