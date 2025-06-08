#!/bin/bash

# Enhanced reimbursement calculation using interview insights
# Based on Kevin's efficiency analysis, Lisa's receipt patterns, Marcus's observations
# Incorporating all key insights: efficiency sweet spots, spending thresholds, 5-day bonuses

if [ $# -ne 3 ]; then
    echo "Usage: $0 <trip_duration_days> <miles_traveled> <total_receipts_amount>"
    exit 1
fi

days=$1
miles=$2
receipts=$3

# Use the proven solution_ultimate.py
result=$(python3 Solution/solution_ultimate.py $days $miles $receipts)

echo $result
