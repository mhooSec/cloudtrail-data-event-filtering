#!/bin/bash
DST_DIR=/home/$USER/tmp

# Downloading S3 logs to local 
aws s3 sync s3://path/to/bucket $DST_DIR

# Copying python script to DST_DIR
cp filter_data.py $DST_DIR

# Accessing DST_DIR
cd $DST_DIR

# Decompressing gzipped logs
gzip -d *.gz

# Combining all .json files into one
jq -s . *.json > combined.json

# Running python script to filter data to obtain only data events with an access key associated to it
python3 filter_data.py

# Obtaining unique eventName and eventSource
cat filtered_file.json | grep "eventName" | sort | uniq
