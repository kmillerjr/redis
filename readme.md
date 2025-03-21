**Steps to reproduce**
- following the following link [redis quickstart](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart/#run-the-container) link to:
    - run redis enterprise in docker
- setup dbs: source-db and replica-db
    -   Note: change the connection for the replica of connection to 172.17.0.2:12000
- Use memtier_benchmark to populate data in source-db 
    - Create a new network:   
    `docker network create redis-net`
    - Connect your Redis container to this network:   
    `docker network connect redis-net <redis-container-name>
         - Run memtier_benchmark in a separate container, connecting it to the same network as your Redis container:   
    `docker run --rm --network bridge redislabs/memtier_benchmark \
  --server=172.17.0.2 --port=12000 \
  --test-time=60 --ratio=1:10
`
` ` 