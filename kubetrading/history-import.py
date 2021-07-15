import argparse
import quandl

from kubetrading.utils import EnvDefault
from influxdb_client import InfluxDBClient, Point

parser = argparse.ArgumentParser(description='Import stock history')
parser.add_argument('-t', '--ticker', action=EnvDefault, required=True, envvar='TICKER')
parser.add_argument('-i', '--interval', action=EnvDefault, default="daily", envvar='INTERVAL')
parser.add_argument('-u', '--influxdb-url', action=EnvDefault, envvar='INTERVAL')
parser.add_argument('-p', '--influxdb-token', action=EnvDefault, envvar='INTERVAL')
parser.add_argument('-o', '--influxdb-org', action=EnvDefault, envvar='INTERVAL')
args = parser.parse_args()

client = InfluxDBClient(url=args.influxdb_url, token=args.influxdb_token, org=args.influxdb_org)
query_api = client.query_api()

last_value = query_api.query(f'from(bucket:"{args.interval}") |> range(start: -5y) |> last()')

period = "max"
if len(last_value) > 0:
    print(last_value)

# TODO map based on args.interval
interval = "1d"

# TODO enable on daily?
prepost = False

quandl.ApiConfig.api_key = 'd_z_6rs6ibMGUQ_sXfQ3'

quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
history = ticker.history(period=period, interval=interval, prepost=prepost)

print(history)

write_api = client.write_api()
for index, row in history.iterrows():
    point = Point("daily").tag("ticker", "daily_NVDA")\
        .field("open", row['open'])\
        .field("high", row['high'])\
        .field("low", row['low'])\
        .field("close", row['close'])\
        .field("adj_close", row['adj_close'])\
        .field("volume", row['volume'])\
        .time(index)
    write_api.write('default', record=point)

