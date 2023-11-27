#!/bin/sh

for i in heat_sink_u5 heat_sink_u6 heat_sink_u7 heat_sink_u8 heat_sink_u9 heat_sink_u10
do
  cd $i
  foamToVTK -region air
  cd postProcessing
  mkdir Data
  cd ../..
done
