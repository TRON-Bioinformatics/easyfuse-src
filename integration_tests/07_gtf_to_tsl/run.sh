#!/bin/bash


source integration_tests/assert.sh
test_folder=integration_tests/07_gtf_to_tsl
input_gtf=$test_folder/input.gtf

easy-fuse gtf-to-tsl \
  --gtf $input_gtf \
  --tsl $test_folder/observed.tsl

test -s $test_folder/observed.tsl || { echo "Missing TSL output file!"; exit 1; }
assert_eq `wc -l $test_folder/observed.tsl | cut -d " " -f 1` 160 "Wrong number of output transcripts"
