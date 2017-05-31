# nhs-waiting-data
Data-as-a-service underpinning Cut ToThe Bone (http://cuttothebone.surge.sh/ &amp; https://github.com/DeckOfPandas/cuttothebone) from NHS Hack Day London 2017

## Install
```
virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install -r requirements.txt
```

To run localy:
```
source env/bin/activate
python run_app.py
```

Should be deployable to Heroku with minimal tweaking, but data should be loaded localy for speed

## Data

To load data, download .xls files from https://www.england.nhs.uk/statistics/statistical-work-areas/rtt-waiting-times/rtt-data-2016-17/ and use appropriate script as follows (needs manual intervation/ more work etc.):
```
source env/bin/activate
python wrangle_incomplete_commissioner.py
```
