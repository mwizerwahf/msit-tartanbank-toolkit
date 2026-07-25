#!/bin/bash
RED='\031m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

CRED_FILE="secrets/credentials.txt"
HASH_FILE="secrets/operator.hash"
echo -e "${YELLOW}Info:${NC}starting..."

# verify that credentials file exists
if [ ! -f "$CRED_FILE" ]; then
	echo -e "${RED}Error: ${RED} Credentials file is not found!">&2
	exit 1
fi
echo -e "${YELLOW}Found file: ${NC} '$CRED_FILE' Exists"
OPERATOR=$(grep '^operator_id:' "$CRED_FILE"|cut -d ":" -f2|xargs)
PASSPHRASE=$(grep '^passphrase:' "$CRED_FILE"|cut -d ":" -f2|xargs)

echo -e "${YELLOW}Verification... ${YELLOW}"


#verify  if operator and passphrase exists
if [ -z "$OPERATOR" ] || [ -z "$PASSPHRASE" ]; then
	echo -e "${RED}Error:${NC} credentials are not set">&2
	exit 1
fi

echo -e "${YELLOW}Process: ${NC} Ready to Hash"

HASHED=$(echo -n "$PASSPHRASE"|sha256sum|awk '{print $1}' )

echo "operator_id: "$OPERATOR"">$HASH_FILE
echo "passphrase: "$HASHED"">>$HASH_FILE

echo "SUCCESSFULLY HASHED THE PASSPHRASE"
echo -e "${YELLOW}Output: ${NC}"
cat $HASH_FILE
