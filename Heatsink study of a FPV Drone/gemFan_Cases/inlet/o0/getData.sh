#!/bin/sh

for i in inlet_u0 inlet_u5 inlet_u10 inlet_u20
do
  cd $i
  cd postProcessing
  cp -R Data /home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/inlet/o0/Data/$i
  cd ../..
done
