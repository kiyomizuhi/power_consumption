#!/bin/bash

wget https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip
mv household_power_consumption.zip data/raw
unzip data/raw/household_power_consumption.zip data/raw/
