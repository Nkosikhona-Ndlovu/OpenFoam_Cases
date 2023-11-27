#!/bin/sh

for i in rpm_0 rpm_2500 rpm_5000 rpm_10000 rpm_20000
do
  cd $i
  cd postProcessing
  cp -R Data /home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/rpm/Data/$i
  cd ../..
done
