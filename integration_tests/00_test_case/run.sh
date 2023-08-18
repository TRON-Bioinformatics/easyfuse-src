#!/bin/bash

test_folder=integration_tests/00_test_case
rm -rf $test_folder/output
mkdir -p $test_folder/output

easy-fuse pipeline \
  -c resources/config.ini.sample \
  -o $test_folder/output \
  --fastq1 $test_folder/SRR1659960_05pc_R1.fastq.gz \
  --fastq2 $test_folder/SRR1659960_05pc_R2.fastq.gz \
  --sample SRR1659960
