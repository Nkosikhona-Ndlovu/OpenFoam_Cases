#! /bin/bash

surfaceTransformPoints -translate "(-0.075 0.075 0)" prop_CW.stl R1.stl
surfaceTransformPoints -translate "(0.075 0.075 0)" prop_CCW.stl R2.stl
surfaceTransformPoints -translate "(0.075 -0.075 0)" prop_CW.stl R3.stl
surfaceTransformPoints -translate "(-0.075 -0.075 0)" prop_CCW.stl R4.stl

