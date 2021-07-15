helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx --values ingress-nginx/values.yaml
helm upgrade --install influxdb2 influxdata/influxdb2 --values influxdb2/values.yaml
helm upgrade --install chronograf influxdata/chronograf --values chronograf/values.yaml
helm upgrade --install grafana grafana/grafana --values grafana/values.yaml