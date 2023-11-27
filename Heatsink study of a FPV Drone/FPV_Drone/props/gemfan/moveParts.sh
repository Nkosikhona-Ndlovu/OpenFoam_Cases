#! /bin/bash

surfaceTransformPoints -translate "(-0.075 0.075 0)" propCW.stl R1.stl
surfaceTransformPoints -translate "(0.075 0.075 0)" propCCW.stl R2.stl
surfaceTransformPoints -translate "(0.075 -0.075 0)" propCW.stl R3.stl
surfaceTransformPoints -translate "(-0.075 -0.075 0)" propCCW.stl R4.stl

