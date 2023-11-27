#!/bin/sh

for i in mesh_n2 mesh_n1 mesh_0
do
  cd $i
  foamToVTK -region air
  cd postProcessing
  mkdir Data
  cd ../..
done
