#!/bin/sh

for i in rpm_0 rpm_2500 rpm_5000 rpm_10000 rpm_20000
do
  cd $i
  foamToVTK -region air
  cd postProcessing
  mkdir Data
  cd ../..
done
