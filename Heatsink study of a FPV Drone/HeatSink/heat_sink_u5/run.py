# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML MultiBlock Data Reader'
heat_sink_u5_500vtm = XMLMultiBlockDataReader(registrationName='heat_sink_u5_500.vtm', FileName=['/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/HeatSink/heat_sink_u5/VTK/air/heat_sink_u5_500.vtm'])
heat_sink_u5_500vtm.CellArrayStatus = ['T', 'alphat', 'epsilon', 'heatTransferCoeff(T)', 'k', 'nut', 'p', 'p_rgh', 'rho', 'yPlus', 'U']
heat_sink_u5_500vtm.PointArrayStatus = ['T', 'alphat', 'epsilon', 'heatTransferCoeff(T)', 'k', 'nut', 'p', 'p_rgh', 'rho', 'yPlus', 'U']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
heat_sink_u5_500vtmDisplay = Show(heat_sink_u5_500vtm, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
heat_sink_u5_500vtmDisplay.Representation = 'Surface'
heat_sink_u5_500vtmDisplay.ColorArrayName = [None, '']
heat_sink_u5_500vtmDisplay.SelectTCoordArray = 'None'
heat_sink_u5_500vtmDisplay.SelectNormalArray = 'None'
heat_sink_u5_500vtmDisplay.SelectTangentArray = 'None'
heat_sink_u5_500vtmDisplay.OSPRayScaleArray = 'T'
heat_sink_u5_500vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
heat_sink_u5_500vtmDisplay.SelectOrientationVectors = 'None'
heat_sink_u5_500vtmDisplay.ScaleFactor = 0.012700000032782556
heat_sink_u5_500vtmDisplay.SelectScaleArray = 'None'
heat_sink_u5_500vtmDisplay.GlyphType = 'Arrow'
heat_sink_u5_500vtmDisplay.GlyphTableIndexArray = 'None'
heat_sink_u5_500vtmDisplay.GaussianRadius = 0.0006350000016391278
heat_sink_u5_500vtmDisplay.SetScaleArray = ['POINTS', 'T']
heat_sink_u5_500vtmDisplay.ScaleTransferFunction = 'PiecewiseFunction'
heat_sink_u5_500vtmDisplay.OpacityArray = ['POINTS', 'T']
heat_sink_u5_500vtmDisplay.OpacityTransferFunction = 'PiecewiseFunction'
heat_sink_u5_500vtmDisplay.DataAxesGrid = 'GridAxesRepresentation'
heat_sink_u5_500vtmDisplay.PolarAxes = 'PolarAxesRepresentation'
heat_sink_u5_500vtmDisplay.SelectInputVectors = ['POINTS', 'T']
heat_sink_u5_500vtmDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
heat_sink_u5_500vtmDisplay.OSPRayScaleFunction.Points = [-231.89349365234375, 0.0, 0.5, 0.0, 1546.929931640625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
heat_sink_u5_500vtmDisplay.ScaleTransferFunction.Points = [291.1345520019531, 0.0, 0.5, 0.0, 296.16363525390625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
heat_sink_u5_500vtmDisplay.OpacityTransferFunction.Points = [291.1345520019531, 0.0, 0.5, 0.0, 296.16363525390625, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(heat_sink_u5_500vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
heat_sink_u5_500vtmDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=heat_sink_u5_500vtm)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.012999998405575752, 0.004999999888241291, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [-0.012999998405575752, 0.004999999888241291, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.02447558003311584, 0.004999999888241291, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'T'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.0009999999776482583
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 4.9999998882412914e-05
slice1Display.SetScaleArray = ['POINTS', 'T']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'T']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'T']
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [-231.89349365234375, 0.0, 0.5, 0.0, 1546.929931640625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [291.1374816894531, 0.0, 0.5, 0.0, 295.68511962890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [291.1374816894531, 0.0, 0.5, 0.0, 295.68511962890625, 1.0, 0.5, 0.0]

# hide data in view
Hide(heat_sink_u5_500vtm, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=slice1)

# Properties modified on integrateVariables1
integrateVariables1.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# Properties modified on integrateVariables1Display
integrateVariables1Display.Assembly = ''

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on spreadSheetView1
spreadSheetView1.FieldAssociation = 'Cell Data'

# export view
ExportView('/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/HeatSink/heat_sink_u5/postProcessing/Data/L1.csv', view=spreadSheetView1)

# set active source
SetActiveSource(heat_sink_u5_500vtm)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(heat_sink_u5_500vtm)

# show data in view
heat_sink_u5_500vtmDisplay = Show(heat_sink_u5_500vtm, renderView1, 'GeometryRepresentation')

# show color bar/color legend
heat_sink_u5_500vtmDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=heat_sink_u5_500vtm)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-0.012999998405575752, 0.004999999888241291, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [-0.012999998405575752, 0.004999999888241291, 0.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [-0.024714397257369233, 0.004999999888241291, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = [None, '']
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'T'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.0009999999776482583
slice2Display.SelectScaleArray = 'None'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'None'
slice2Display.GaussianRadius = 4.9999998882412914e-05
slice2Display.SetScaleArray = ['POINTS', 'T']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'T']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.SelectInputVectors = ['POINTS', 'T']
slice2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice2Display.OSPRayScaleFunction.Points = [-231.89349365234375, 0.0, 0.5, 0.0, 1546.929931640625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [293.3341064453125, 0.0, 0.5, 0.0, 296.163330078125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [293.3341064453125, 0.0, 0.5, 0.0, 296.163330078125, 1.0, 0.5, 0.0]

# hide data in view
Hide(heat_sink_u5_500vtm, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice2Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Integrate Variables'
integrateVariables2 = IntegrateVariables(registrationName='IntegrateVariables2', Input=slice2)

# Properties modified on integrateVariables2
integrateVariables2.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView2 = CreateView('SpreadSheetView')
spreadSheetView2.ColumnToSort = ''
spreadSheetView2.BlockSize = 1024

# show data in view
integrateVariables2Display = Show(integrateVariables2, spreadSheetView2, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView2, layout=layout1, hint=1)

# Properties modified on integrateVariables2Display
integrateVariables2Display.Assembly = ''

# update the view to ensure updated data information
spreadSheetView2.Update()

# set active view
SetActiveView(spreadSheetView1)

# Properties modified on spreadSheetView2
spreadSheetView2.FieldAssociation = 'Cell Data'

# set active view
SetActiveView(spreadSheetView2)

# export view
ExportView('/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/HeatSink/heat_sink_u5/postProcessing/Data/L2.csv', view=spreadSheetView2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(heat_sink_u5_500vtm)

# set active source
SetActiveSource(heat_sink_u5_500vtm)

# show data in view
heat_sink_u5_500vtmDisplay = Show(heat_sink_u5_500vtm, renderView1, 'GeometryRepresentation')

# show color bar/color legend
heat_sink_u5_500vtmDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(registrationName='ExtractBlock1', Input=heat_sink_u5_500vtm)

# Properties modified on extractBlock1
extractBlock1.Selectors = ['/Root/boundary/air_to_heatsink']

# show data in view
extractBlock1Display = Show(extractBlock1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractBlock1Display.Representation = 'Surface'
extractBlock1Display.ColorArrayName = [None, '']
extractBlock1Display.SelectTCoordArray = 'None'
extractBlock1Display.SelectNormalArray = 'None'
extractBlock1Display.SelectTangentArray = 'None'
extractBlock1Display.OSPRayScaleArray = 'T'
extractBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock1Display.SelectOrientationVectors = 'None'
extractBlock1Display.ScaleFactor = 0.0050999999046325685
extractBlock1Display.SelectScaleArray = 'None'
extractBlock1Display.GlyphType = 'Arrow'
extractBlock1Display.GlyphTableIndexArray = 'None'
extractBlock1Display.GaussianRadius = 0.00025499999523162845
extractBlock1Display.SetScaleArray = ['POINTS', 'T']
extractBlock1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractBlock1Display.OpacityArray = ['POINTS', 'T']
extractBlock1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock1Display.PolarAxes = 'PolarAxesRepresentation'
extractBlock1Display.SelectInputVectors = ['POINTS', 'T']
extractBlock1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractBlock1Display.OSPRayScaleFunction.Points = [-231.89349365234375, 0.0, 0.5, 0.0, 1546.929931640625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractBlock1Display.ScaleTransferFunction.Points = [295.041259765625, 0.0, 0.5, 0.0, 296.16363525390625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractBlock1Display.OpacityTransferFunction.Points = [295.041259765625, 0.0, 0.5, 0.0, 296.16363525390625, 1.0, 0.5, 0.0]

# hide data in view
Hide(heat_sink_u5_500vtm, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Integrate Variables'
integrateVariables3 = IntegrateVariables(registrationName='IntegrateVariables3', Input=extractBlock1)

# Properties modified on integrateVariables3
integrateVariables3.DivideCellDataByVolume = 1

# Create a new 'SpreadSheet View'
spreadSheetView3 = CreateView('SpreadSheetView')
spreadSheetView3.ColumnToSort = ''
spreadSheetView3.BlockSize = 1024

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView3, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView3, layout=layout1, hint=3)

# Properties modified on integrateVariables3Display
integrateVariables3Display.Assembly = ''

# update the view to ensure updated data information
spreadSheetView1.Update()

# update the view to ensure updated data information
spreadSheetView2.Update()

# update the view to ensure updated data information
spreadSheetView3.Update()

# set active view
SetActiveView(spreadSheetView1)

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(spreadSheetView2)

# destroy spreadSheetView2
Delete(spreadSheetView2)
del spreadSheetView2

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(spreadSheetView3)

# Properties modified on spreadSheetView3
spreadSheetView3.FieldAssociation = 'Cell Data'

# export view
ExportView('/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/HeatSink/heat_sink_u5/postProcessing/Data/H.csv', view=spreadSheetView3)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1133, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.021285997475883073, 0.08651175622115476, -0.23001181723811043]
renderView1.CameraFocalPoint = [-0.012999998405575752, 0.004999999888241291, 0.0]
renderView1.CameraViewUp = [-0.1780258827818059, 0.9355622312804929, 0.30500835474003757]
renderView1.CameraParallelScale = 0.06377940514096375

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).