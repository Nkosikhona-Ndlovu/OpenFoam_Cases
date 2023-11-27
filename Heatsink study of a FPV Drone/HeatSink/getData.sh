#!/bin/sh

for i in heat_sink_u5 heat_sink_u6 heat_sink_u7 heat_sink_u8 heat_sink_u9 heat_sink_u10
do
  cd $i
  cd postProcessing
  cp -R Data /home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/HeatSink/Data/U$i
  cd ../..
done
