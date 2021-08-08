#!/bin/bash
if [ "$1" = "shared" ]; then
	echo "SAMPLE_SHARED=True" >> $GITHUB_ENV
else
	echo "SAMPLE_SHARED=False" >> $GITHUB_ENV
fi