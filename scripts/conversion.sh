#!/bin/bash
for run in {1..124}
do
	python conversion_h5.py --run ${run} --inputDir ../data/20210317/ --channels 1 2 3 
done
