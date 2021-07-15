influx -o influxdata -t oDFiLWJDWKKamAyHeaOn4EJ1DKXjImFc bucket list
influx -o influxdata -t oDFiLWJDWKKamAyHeaOn4EJ1DKXjImFc v1 auth create --read-bucket 11b4bb17710171e2 --write-bucket 11b4bb17710171e2 --username admin
influx -o influxdata -t oDFiLWJDWKKamAyHeaOn4EJ1DKXjImFc v1 dbrp create --db default --rp default --bucket-id 11b4bb17710171e2 --default
