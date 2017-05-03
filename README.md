# Enrichment Engine

## Explanation
These scripts read data from the database through LOG component and perform some operations. When they finish the results are stored again in the database through LOG api.

## Installation
We have the script `statistics.py` added as a task inside the `cron` in a Linux server. We run it every 30 minutes between 8AM and 6PM every day. 
```
$ crontab -e
1,31 8-18 * * * python path/to/script/statistics.py
```

ATM `transform.py` is not used.
