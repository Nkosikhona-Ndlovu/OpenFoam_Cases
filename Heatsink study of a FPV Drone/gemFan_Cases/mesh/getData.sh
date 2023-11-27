#!/bin/sh

for i in mesh_n2 mesh_n1 mesh_0
do
  cd $i
  cd postProcessing
  cp -R Data /home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/Data/$i
  cd ../..
done
