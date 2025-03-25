FROM redislabs/memtier_benchmark:latest

RUN mkdir -p /tmp

ENTRYPOINT memtier_benchmark -s 172.17.0.2 -p 13300 --protocol=redis --clients=50 --threads=4 --requests=10000 --data-size=1024 --pipeline=1 --key-pattern=R:R --ratio=1:1 > /tmp/memtier_benchmark.txt 