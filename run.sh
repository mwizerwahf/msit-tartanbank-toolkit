#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

TRANSACTIONS_PATH="data/transactions.csv"
TODAY_DATE=$(date +%Y-%m-%d)
REPORT_DIR=reports
PROCESS_PATH=src/process.py

./setup.sh

if [ ! -f "$TRANSACTIONS_PATH" ]; then
    echo -e "${RED}WARNING !:${NC} $TRANSACTIONS_PATH does not exist. Please add transactions.csv into data/ directory."
	exit 1
fi

REPORT_FILE=$REPORT_DIR/report_$TODAY_DATE-Tartan-Bank.txt

touch $REPORT_FILE
# echo -e "\ncreated report file: $REPORT_FILE \n"

python3 $PROCESS_PATH $TRANSACTIONS_PATH $REPORT_FILE

echo -e "\n${BLUE}Total input transactions:${NC} $(tail -n +2 $TRANSACTIONS_PATH | wc -l) " 
echo -e "${BLUE}Flagged Transactions:${NC} $(grep "Flagged transactions:" $REPORT_FILE|cut -d ':' -f2)"

echo -e "\nReport successfully  generated and saved at ${YELLOW} $REPORT_FILE ${NC}"
