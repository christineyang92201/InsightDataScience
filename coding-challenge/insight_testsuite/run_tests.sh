#!/bin/bash

if [ -d "./test-1-venmo-trans" ]; then
	mkdir -p ./test-1-venmo-trans/venmo_output
fi
if [ -d "./your-own-test" ]; then
	mkdir -p ./your-own-test/venmo_output
fi

cd ..
python median_degree.py ./insight_testsuite/tests/test-1-venmo-trans/venmo_input/venmo-trans.txt ./insight_testsuite/tests/test-1-venmo-trans/venmo_output/output.txt

python median_degree.py ./insight_testsuite/tests/your-own-test/venmo_input/venmo-trans.txt ./insight_testsuite/tests/your-own-test/venmo_output/output.txt

