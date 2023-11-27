# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

i = '0'
num = 100

# create a new 'XML MultiBlock Data Reader'
mesh_n2_100vtm = XMLMultiBlockDataReader(registrationName=f'mesh_{i}_{num}.vtm', FileName=[f'/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/mesh_{i}/VTK/air/mesh_{i}_{num}.vtm'])
mesh_n2_100vtm.CellArrayStatus = ['T', 'alphat', 'epsilon', 'heatTransferCoeff(T)', 'k', 'nut', 'p', 'p_rgh', 'rho', 'yPlus', 'U']
mesh_n2_100vtm.PointArrayStatus = ['T', 'alphat', 'epsilon', 'heatTransferCoeff(T)', 'k', 'nut', 'p', 'p_rgh', 'rho', 'yPlus', 'U']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
mesh_n2_100vtmDisplay = Show(mesh_n2_100vtm, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
mesh_n2_100vtmDisplay.Representation = 'Surface'
mesh_n2_100vtmDisplay.ColorArrayName = [None, '']
mesh_n2_100vtmDisplay.SelectTCoordArray = 'None'
mesh_n2_100vtmDisplay.SelectNormalArray = 'None'
mesh_n2_100vtmDisplay.SelectTangentArray = 'None'
mesh_n2_100vtmDisplay.OSPRayScaleArray = 'T'
mesh_n2_100vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
mesh_n2_100vtmDisplay.SelectOrientationVectors = 'None'
mesh_n2_100vtmDisplay.ScaleFactor = 1.2000000000000002
mesh_n2_100vtmDisplay.SelectScaleArray = 'None'
mesh_n2_100vtmDisplay.GlyphType = 'Arrow'
mesh_n2_100vtmDisplay.GlyphTableIndexArray = 'None'
mesh_n2_100vtmDisplay.GaussianRadius = 0.06
mesh_n2_100vtmDisplay.SetScaleArray = ['POINTS', 'T']
mesh_n2_100vtmDisplay.ScaleTransferFunction = 'PiecewiseFunction'
mesh_n2_100vtmDisplay.OpacityArray = ['POINTS', 'T']
mesh_n2_100vtmDisplay.OpacityTransferFunction = 'PiecewiseFunction'
mesh_n2_100vtmDisplay.DataAxesGrid = 'GridAxesRepresentation'
mesh_n2_100vtmDisplay.PolarAxes = 'PolarAxesRepresentation'
mesh_n2_100vtmDisplay.SelectInputVectors = ['POINTS', 'T']
mesh_n2_100vtmDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mesh_n2_100vtmDisplay.OSPRayScaleFunction.Points = [-231.89349365234375, 0.0, 0.5, 0.0, 1546.929931640625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mesh_n2_100vtmDisplay.ScaleTransferFunction.Points = [299.7855224609375, 0.0, 0.5, 0.0, 312.1433410644531, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mesh_n2_100vtmDisplay.OpacityTransferFunction.Points = [299.7855224609375, 0.0, 0.5, 0.0, 312.1433410644531, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(mesh_n2_100vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
mesh_n2_100vtmDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=mesh_n2_100vtm)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'T']
clip1.Value = 305.9644317626953

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, -0.6000000238418579]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.0, 0.0, -0.6000000238418579]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1
clip1.ClipType = 'Cylinder'

# Properties modified on clip1.ClipType
clip1.ClipType.Center = [0.0, 0.0, 0.0]
clip1.ClipType.Axis = [0.0, 0.0, 1.0]
clip1.ClipType.Radius = 0.3

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'T'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.5200000047683716
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.02600000023841858
clip1Display.SetScaleArray = ['POINTS', 'T']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'T']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.11261043833319008
clip1Display.OpacityArrayName = ['POINTS', 'T']
clip1Display.SelectInputVectors = ['POINTS', 'T']
clip1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [-231.89349365234375, 0.0, 0.5, 0.0, 1546.929931640625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [299.7855224609375, 0.0, 0.5, 0.0, 312.1433410644531, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [299.7855224609375, 0.0, 0.5, 0.0, 312.1433410644531, 1.0, 0.5, 0.0]

# hide data in view
Hide(mesh_n2_100vtm, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=clip1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, -0.6000000238418579]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.0, 0.0, -0.6000000238418579]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.3]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

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
slice1Display.ScaleFactor = 0.05999504625797272
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.002999752312898636
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
slice1Display.ScaleTransferFunction.Points = [300.000732421875, 0.0, 0.5, 0.0, 300.0071716308594, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [300.000732421875, 0.0, 0.5, 0.0, 300.0071716308594, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data bounds
renderView1.ResetCamera(-0.2999752461910248, 0.2999751567840576, -0.29997512698173523, 0.29997533559799194, 0.30000001192092896, 0.30000001192092896, False)

# set active source
SetActiveSource(mesh_n2_100vtm)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(slice1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# Rescale transfer function
uLUT.RescaleTransferFunction(0.014247017487227806, 0.22208717620301377)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.014247017487227806, 0.22208717620301377)

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

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 39.74894798292003)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 39.74894798292003)

# Properties modified on spreadSheetView1
spreadSheetView1.FieldAssociation = 'Cell Data'

# export view
ExportView(f'/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/mesh_{i}/postProcessing/Data/L1.csv', view=spreadSheetView1)

# hide data in view
Hide(integrateVariables1, spreadSheetView1)

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=clip1)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.0, 0.0, -0.6000000238418579]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [0.0, 0.0, -0.6000000238418579]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0, 0.0, 0.0]

# show data in view
slice2Display = Show(slice2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Integrate Variables'
integrateVariables2 = IntegrateVariables(registrationName='IntegrateVariables2', Input=slice2)

# Properties modified on integrateVariables2
integrateVariables2.DivideCellDataByVolume = 1

# show data in view
integrateVariables2Display = Show(integrateVariables2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables2Display
integrateVariables2Display.Assembly = ''

# set active source
SetActiveSource(slice2)

# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# set active source
SetActiveSource(integrateVariables2)

# set active source
SetActiveSource(slice2)

# set active source
SetActiveSource(integrateVariables2)

# export view
ExportView(f'/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/mesh_{i}/postProcessing/Data/L2.csv', view=spreadSheetView1)

# hide data in view
Hide(integrateVariables2, spreadSheetView1)

# set active source
SetActiveSource(clip1)

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=clip1)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [0.0, 0.0, -0.6000000238418579]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = [0.0, 0.0, -0.6000000238418579]

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.0, 0.0, -0.3]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice3Display = Show(slice3, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Integrate Variables'
integrateVariables3 = IntegrateVariables(registrationName='IntegrateVariables3', Input=slice3)

# Properties modified on integrateVariables3
integrateVariables3.DivideCellDataByVolume = 1

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables3Display
integrateVariables3Display.Assembly = ''

# export view
ExportView(f'/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/mesh_{i}/postProcessing/Data/L3.csv', view=spreadSheetView1)

# hide data in view
Hide(integrateVariables3, spreadSheetView1)

# set active source
SetActiveSource(clip1)

# create a new 'Slice'
slice4 = Slice(registrationName='Slice4', Input=clip1)
slice4.SliceType = 'Plane'
slice4.HyperTreeGridSlicer = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = [0.0, 0.0, -0.6000000238418579]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice4.HyperTreeGridSlicer.Origin = [0.0, 0.0, -0.6000000238418579]

# Properties modified on slice4.SliceType
slice4.SliceType.Origin = [0.0, 0.0, -0.6]
slice4.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice4Display = Show(slice4, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Integrate Variables'
integrateVariables4 = IntegrateVariables(registrationName='IntegrateVariables4', Input=slice4)

# Properties modified on integrateVariables4
integrateVariables4.DivideCellDataByVolume = 1

# show data in view
integrateVariables4Display = Show(integrateVariables4, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables4Display
integrateVariables4Display.Assembly = ''

# export view
ExportView(f'/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/mesh_{i}/postProcessing/Data/L4.csv', view=spreadSheetView1)

# set active source
SetActiveSource(mesh_n2_100vtm)

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(registrationName='ExtractBlock1', Input=mesh_n2_100vtm)

# Properties modified on extractBlock1
extractBlock1.Selectors = ['/Root/boundary/air_to_heatSink']

# show data in view
extractBlock1Display = Show(extractBlock1, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Integrate Variables'
integrateVariables5 = IntegrateVariables(registrationName='IntegrateVariables5', Input=extractBlock1)

# Properties modified on integrateVariables5
integrateVariables5.DivideCellDataByVolume = 1

# show data in view
integrateVariables5Display = Show(integrateVariables5, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables5Display
integrateVariables5Display.Assembly = ''

# export view
ExportView(f'/home/hello/openfoam/openfoam2206/tutorials/incompressible/pimpleFoam/RAS/Drone/Test_Case/gemFan_Cases/mesh/mesh_{i}/postProcessing/Data/H.csv', view=spreadSheetView1)

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
renderView1.CameraPosition = [1.2339259056049583, 0.12201271358124498, 1.3719945559268751]
renderView1.CameraFocalPoint = [-4.47034835849654e-08, 1.0430812835619727e-07, 0.30000001192092896]
renderView1.CameraViewUp = [-0.6530561113730323, -0.039972442823523927, 0.7562538721970644]
renderView1.CameraParallelScale = 0.42422901939270735

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
