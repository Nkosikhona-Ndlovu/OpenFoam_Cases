#!/bin/sh

for i in inlet_u0 inlet_u5 inlet_u10 inlet_u20
do
  cd $i
  foamToVTK -region air
  cd postProcessing
  mkdir Data
  cd ../..
done
