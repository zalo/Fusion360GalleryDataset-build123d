"""Batch 016 - passing/01_2ops
197 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a simple elongated rectangular profile with smooth, tapered edges.
def model_56013_752d02cb_0008():
    """Model: shaft720 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=72
        extrude(amount=72)
    return part.part


# Description: This is a 3D parallelogram-shaped plate or flat panel with a trapezoidal profile, featuring internal diagonal creases or fold lines that suggest it may be a bent or faceted component with a slightly curved or angled surface along one edge.
def model_56016_7af50dfa_0000():
    """Model: sheet v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6, perimeter: 40.6
            with BuildLine():
                Line((0, 0.3), (0, 0))
                Line((0, 0), (20, 0))
                Line((20, 0), (20, 0.3))
                Line((20, 0.3), (0, 0.3))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a circular cross-section, featuring a central hole and textured or knurled surface patterns on portions of its outer and inner edges.
def model_56065_00bbe5da_0003():
    """Model: Air_Channel_Packing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6185010537, perimeter: 5.4977871438
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a horizontal cylindrical rod or shaft with rounded ends featuring two symmetrical rectangular slots or recesses on opposite sides near each end.
def model_56065_00bbe5da_0004():
    """Model: Piston_Pin v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=1.4
        extrude(amount=1.4, both=True)
    return part.part


# Description: This is a hexagonal or irregularly-shaped polyhedron with multiple internal cavities and cutouts, featuring complex triangulated surfaces and what appears to be two recessed pockets or holes on its face.
def model_56065_00bbe5da_0007():
    """Model: Slide v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6036504592, perimeter: 7.1707963268
            with BuildLine():
                Line((-0.9, 0.5), (0.9, 0.5))
                Line((-0.9, -0.5), (-0.9, 0.5))
                Line((0.9, -0.5), (-0.9, -0.5))
                Line((0.9, 0.5), (0.9, -0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.36
        extrude(amount=0.36, both=True)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a smooth, rounded barrel shape and visible linear surface texturing or threading along its length.
def model_56065_00bbe5da_0010():
    """Model: Heat_Exchange_Piston_Tube v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5419247327, perimeter: 21.6769893098
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4.375
        extrude(amount=4.375, both=True)
    return part.part


# Description: This is a tall, rectangular prism or column with a slightly tapered top section, featuring a hollow or open cavity on one of its long faces, and appears to be designed as a structural or support component.
def model_56078_6d7f171c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.335311363, perimeter: 17.5070034539
            with BuildLine():
                CenterArc((12.6973495559, 3.4033204788), 15.2809953543, 174.0023353676, 12.3129776754)
                CenterArc((-59.3605887296, 0), 56.8957516048, -2.0144767995, 3.7492635965)
                Line((-0.75, -2), (-2.5, -2))
                Line((-0.75, 5), (-0.75, -2))
                Line((-2.5, 5), (-0.75, 5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat, elongated oval or elliptical plate with a diagonal ribbed or corrugated surface pattern running across its top face.
def model_56106_8cdc7ee3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 94.2477796077, perimeter: 36.9698951018
            Ellipse(7.5, 4)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


# Description: This is a cylindrical dowel or spacer with rounded ends and shallow grooved or knurled texture along its length, designed for alignment or spacing applications.
def model_56157_d9157017_0007():
    """Model: 5_bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 46.8892428649), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((47.5032800979, -16.9754263027), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((47.5032800979, -16.9754263027), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-6.4
        extrude(amount=-6.4)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a textured surface pattern, featuring a hollow center and uniform cross-sectional thickness throughout its circumference.
def model_56157_d9157017_0011():
    """Model: 2_washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 46.8892428649), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((47.5032800979, -16.9754263027), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((47.5032800979, -16.9754263027), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((47.5032800979, -16.9754263027), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((47.5032800979, -16.9754263027), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a hollow cylindrical sleeve or tube with a rounded closed end on one side and an open end on the other, featuring a uniform bore throughout its length.
def model_56167_90101372_0000():
    """Model: Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5069123977, perimeter: 16.9960162559
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)
    return part.part


# Description: This is a torus or ring-shaped component with a circular cross-section and uniform wall thickness, featuring a textured or mesh-patterned surface on the outer diameter, commonly used as a seal, gasket, or retention ring in mechanical assemblies.
def model_56167_90101372_0001():
    """Model: Tire"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 254.4690049408, perimeter: 169.6460032938
            with BuildLine():
                CenterArc((0, 0), 15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 12, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.7
        extrude(amount=1.7, both=True)
    return part.part


# Description: This is a curved, elongated blade or lever with a tapered design, featuring a twisted shaft that transitions from a wider, textured upper section to a pointed tip at the lower end.
def model_56167_90101372_0007():
    """Model: Crosshead"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.5076330986, perimeter: 120.4423239067
            with BuildLine():
                Line((-69.9852680213, 13.248148879), (-69.9857655437, 12.748148879))
                Line((-69.9857655437, 12.748148879), (-66.4857655437, 12.748148879))
                CenterArc((-41.6633098693, 52.6586198646), 47, -121.8796895714, 64.2705722411)
                Line((-12.9857655437, 12.9712004256), (-16.4857655437, 12.9712004256))
                Line((-12.9857655437, 13.4712004256), (-12.9857655437, 12.9712004256))
                Line((-12.9857655437, 13.4712004256), (-16.4857655437, 13.4712004256))
                CenterArc((-41.6630635718, 53.1587761137), 47, -121.8793289117, 64.2698560083)
                Line((-69.9852680213, 13.248148879), (-66.4852680213, 13.248148879))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a long, slender rectangular rail or beam with a slightly tapered profile, featuring a hollow or recessed channel running along its top surface and flanged ends on both sides.
def model_56167_90101372_0008():
    """Model: Angle iron"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.25, perimeter: 18
            with BuildLine():
                Line((-13.7653366693, 17.853996956), (-9.7653366693, 17.853996956))
                Line((-9.7653366693, 17.853996956), (-9.7653366693, 13.853996956))
                Line((-9.7653366693, 13.853996956), (-9.2653366693, 13.853996956))
                Line((-9.2653366693, 13.853996956), (-9.2653366693, 18.353996956))
                Line((-13.7653366693, 18.353996956), (-9.2653366693, 18.353996956))
                Line((-13.7653366693, 17.853996956), (-13.7653366693, 18.353996956))
            make_face()
        # OneSide extrude, distance=140
        extrude(amount=140)
    return part.part


# Description: This is a curved blade or lever component with a tapered, elongated design that curves downward from left to right, featuring a textured or ribbed surface along its length and pointed ends.
def model_56167_90101372_0010():
    """Model: Crosshead (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.0076330986, perimeter: 122.4423239067
            with BuildLine():
                Line((-70.4852680213, 13.248148879), (-70.4857655437, 12.748148879))
                Line((-70.4857655437, 12.748148879), (-66.4857655437, 12.748148879))
                CenterArc((-41.6633098693, 52.6586198646), 47, -121.8796895714, 64.2705722411)
                Line((-12.4857655437, 12.9712004256), (-16.4857655437, 12.9712004256))
                Line((-12.4857655437, 13.4712004256), (-12.4857655437, 12.9712004256))
                Line((-12.4857655437, 13.4712004256), (-16.4857655437, 13.4712004256))
                CenterArc((-41.6630635718, 53.1587761137), 47, -121.8793289117, 64.2698560083)
                Line((-70.4852680213, 13.248148879), (-66.4852680213, 13.248148879))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a flat, elongated rectangular plate or panel with a slight 3D fold or bend running diagonally across its surface, creating two angled sections that form a shallow V-shape.
def model_56167_90101372_0011():
    """Model: Bucket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1975, perimeter: 208
            with BuildLine():
                Line((-79, 42.5), (0, 42.5))
                Line((-79, 17.5), (-79, 42.5))
                Line((0, 17.5), (-79, 17.5))
                Line((0, 42.5), (0, 17.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a slightly trapezoidal profile, featuring two diagonal cross-braces or reinforcement ribs running across its interior surface.
def model_56167_90101372_0012():
    """Model: Wing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5, perimeter: 21
            with BuildLine():
                Line((12.45, 17.5), (2.45, 17.5))
                Line((12.45, 18), (12.45, 17.5))
                Line((2.45, 18), (12.45, 18))
                Line((2.45, 17.5), (2.45, 18))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40)
    return part.part


# Description: This is an L-shaped angle bracket or corner brace with a long vertical flange and a shorter horizontal foot, featuring a simple rectangular profile with clean edges and a right-angle bend.
def model_56167_90101372_0014():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.2278306944, perimeter: 85.2113183212
            with BuildLine():
                Line((75.026576176, 17.5), (74.526576176, 17.5))
                Line((74.526576176, 17.5), (93.2742793134, -14.9719743592))
                Line((98.2742793134, -14.9719743592), (93.2742793134, -14.9719743592))
                Line((98.3118149613, -14.54293994), (98.2742793134, -14.9719743592))
                Line((98.3118149613, -14.54293994), (93.526576176, -14.54293994))
                Line((75.026576176, 17.5), (93.526576176, -14.54293994))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a textured cylindrical ring or sleeve with a uniform circular band shape and a knurled or ridged surface pattern around its entire outer circumference.
def model_56233_e0a640c6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0805033117, perimeter: 6.4402649399
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.075
        extrude(amount=0.075, both=True)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a hollow central bore and a hexagonal flange at the top, featuring vertical ribbed or grooved detailing along its outer surface.
def model_56250_3b6024e3_0002():
    """Model: Sleeve 56"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3063052837, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular base plate or frame component with a flat, elongated parallelogram shape featuring multiple internal rectangular slots or cutouts arranged in a grid pattern, designed to reduce weight while maintaining structural rigidity.
def model_56250_3b6024e3_0005():
    """Model: Flange"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7683009123, perimeter: 14.0212385966
            with BuildLine():
                Line((0, 0), (0, -2.1))
                Line((0, -2.1), (2.9, -2.1))
                Line((2.9, -2.1), (2.9, 0))
                Line((0, 0), (2.9, 0))
            make_face()
            with BuildLine():
                CenterArc((2.4, -1.65), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, -1.65), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4, -0.45), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, -0.45), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: A cylindrical tube or sleeve with a closed rounded top end and an open bottom end, featuring a smooth curved surface with subtle edge detailing along its length.
def model_56250_3b6024e3_0017():
    """Model: Sleeve 5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a solid dark base section and an open-mesh top section featuring a hexagonal or diamond-pattern perforated surface.
def model_56250_3b6024e3_0019():
    """Model: Roll Centering device"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.20165919, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a dark metal bracket or mounting clip with an angular V-shaped design, featuring a vertical upper arm, a horizontal lower arm, and a circular hole near the base for fastening.
def model_56250_3b6024e3_0020():
    """Model: Driver Thin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.2944100145, perimeter: 18.2974119805
            with BuildLine():
                CenterArc((0, 0), 0.5, 172, 98)
                Line((0, -0.5), (2.78, -0.5))
                Line((2.78, -0.5), (2.78, -0.1))
                Line((2.78, -0.1), (1.78, -0.1))
                Line((1.78, -0.1), (0.7, 0.2))
                Line((0.7, 0.2), (0.7, 3.15))
                Line((0.7, 3.15), (1.3, 3.7))
                Line((1.3, 3.7), (0.7, 3.7))
                Line((0.7, 3.7), (0.7, 4.7))
                Line((0.7, 4.7), (0.0322725755, 3.822279574))
                Line((-0.4951340344, 0.0695865505), (0.0322725755, 3.822279574))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical mesh or perforated basket with an open top and a cross-shaped divider, featuring a dark solid base with blue mesh panels on the upper portion for ventilation or visibility.
def model_56250_3b6024e3_0023():
    """Model: Roll lever"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7775441818, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a cylindrical capsule or pill-shaped part with two hemispherical ends and a central cylindrical body, featuring a fine hexagonal mesh pattern indicating a surface mesh or grid design.
def model_56343_60e8809c_0002():
    """Model: Scissors_rivet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-0.6000000089, 0.3000000045)):
                Circle(0.075)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a cylindrical dowel or pin with rounded ends and a knurled or textured surface along its shaft, designed for alignment, fastening, or mechanical connection purposes.
def model_56343_60e8809c_0003():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.7523450247, perimeter: 11.8274333882
            with BuildLine():
                Line((-4.5, 0), (-0.9, 0))
                CenterArc((-0.9, 0.9), 0.9, -90, 90)
                CenterArc((-0.9, 0.9), 0.9, 0, 90)
                Line((-0.9, 1.8), (-4.5, 1.8))
                Line((-4.5, 1.8), (-4.5, 0))
            make_face()
            # Profile area: 7.7523450247, perimeter: 11.8274333882
            with BuildLine():
                CenterArc((-8.1, 0.9), 0.9, 90, 90)
                CenterArc((-8.1, 0.9), 0.9, 180, 90)
                Line((-8.1, 0), (-4.5, 0))
                Line((-4.5, 1.8), (-4.5, 0))
                Line((-4.5, 1.8), (-8.1, 1.8))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a curved tube or hose component with a hook-like shape, featuring a smooth arc bend with textured mesh sections at both ends and dark end caps or fittings.
def model_56344_3a89f085_0001():
    """Model: arm 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.7000000402), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.8182420237, perimeter: 34.3004528185
            with BuildLine():
                CenterArc((40.0781660892, 20.0004459194), 4.1380193421, -65.1997112901, 155.0263220589)
                CenterArc((42.1075055074, 15.6086111456), 0.7, 114.8002887099, 180)
                CenterArc((40.0781660892, 20.0004459194), 5.5380193421, -65.1997112901, 165.6313548517)
                CenterArc((39.603566426, 26.296096177), 1, -121.8789919688, 17.3546165875)
                Line((39.4280111601, 25.3085634845), (39.3527745649, 25.3280551435))
                CenterArc((39.3527736018, 25.0181511745), 0.3, 24.8449063936, 50.6307182251)
                Line((40.0906885979, 24.1384463136), (39.6250081363, 25.1442002057))
            make_face()
            with BuildLine():
                CenterArc((42.1075055074, 15.6086111456), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.4290624179, perimeter: 10.2872325495
            with BuildLine():
                Line((40.0906885979, 24.1384463136), (39.6250081363, 25.1442002057))
                CenterArc((39.3527736018, 25.0181511745), 0.3, 24.8449063936, 50.6307182251)
                Line((39.4280111601, 25.3085634845), (39.3527745649, 25.3280551435))
                CenterArc((39.603566426, 26.296096177), 1, -121.8789919688, 17.3546165875)
                CenterArc((40.0781660892, 20.0004459194), 5.5380193421, 100.4316435616, 14.3686451483)
                CenterArc((38.0488266711, 24.3922806933), 0.7, 114.8002887099, 180)
                CenterArc((40.0781660892, 20.0004459194), 4.1380193421, 89.8266107687, 24.9736767337)
            make_face()
            with BuildLine():
                CenterArc((38.0488266711, 24.3922806933), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a simple planar geometry and no holes, slots, or features—characterized by its slanted sides and uniform thickness.
def model_56344_3a89f085_0013():
    """Model: pressure of the knife"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5.2000000402), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 64.9999987334, perimeter: 32.9999997467
            with BuildLine():
                Line((26.8432785452, 8.5000001267), (26.8432785452, 15))
                Line((36.8432785452, 8.5000001267), (26.8432785452, 8.5000001267))
                Line((36.8432785452, 15), (36.8432785452, 8.5000001267))
                Line((26.8432785452, 15), (36.8432785452, 15))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a torus or ring-shaped seal/washer with a circular cross-section, featuring a uniformly textured or knurled outer surface and a smooth central hole, commonly used as a gasket, O-ring, or mechanical seal component.
def model_56344_3a89f085_0015():
    """Model: washer M20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((56, 19), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((56, 19), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a tire or rubber ring with a toroidal (doughnut) shape, featuring a smooth outer surface and a hollow center, with tread pattern details visible on the outer circumference.
def model_56344_3a89f085_0018():
    """Model: washer M15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0341812432, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((55, 15), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((55, 15), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a hexagonal or octagonal box-like container with angled faceted sides, featuring a central rectangular opening or slot running across the top surface and mesh or perforated panels on several faces.
def model_56344_3a89f085_0021():
    """Model: nut M16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9776870275, perimeter: 13.3403921221
            with BuildLine():
                Line((12.2, 16.307179677), (12.2, 17.692820323))
                Line((12.2, 17.692820323), (11, 18.3856406461))
                Line((11, 18.3856406461), (9.8, 17.692820323))
                Line((9.8, 17.692820323), (9.8, 16.307179677))
                Line((9.8, 16.307179677), (11, 15.6143593539))
                Line((11, 15.6143593539), (12.2, 16.307179677))
            make_face()
            with BuildLine():
                CenterArc((11, 17), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a toggle latch or draw latch featuring a long cylindrical shaft with a looped handle at the top and a split fork-like mechanism at the bottom for engaging with a corresponding catch or pin.
def model_56344_3a89f085_0022():
    """Model: cotter 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8093632604, perimeter: 21.7330202767
            with BuildLine():
                Line((59.7946016932, 5.9384501602), (59.4303633475, 5.0278543774))
                Line((59.4303633475, 5.0278543774), (59.4999990985, 5.0000000745))
                Line((59.8642374442, 5.9105958573), (59.4999990985, 5.0000000745))
                CenterArc((59.3999991044, 6.0962912098), 0.5, -21.8014112528, 21.8014112528)
                Line((59.8999991044, 6.0962912098), (59.8999991044, 8.8375761447))
                CenterArc((59.5999991044, 8.8375761447), 0.3, 0, 50.6468468188)
                CenterArc((60.128570208, 9.4821429163), 0.5335788712, 123.3969261313, 107.2499206875)
                CenterArc((60, 9.6771526358), 0.3, 56.6030738687, 66.7938522624)
                CenterArc((59.871429792, 9.4821429163), 0.5335788712, -50.6468468188, 107.2499206873)
                CenterArc((60.4000008956, 8.8375761447), 0.3, 129.3531531812, 50.6468468188)
                Line((60.1000008956, 6.0962912098), (60.1000008956, 8.8375761447))
                CenterArc((60.6000008956, 6.0962912098), 0.5, -180, 21.8014112528)
                Line((60.1357625558, 5.9105958573), (60.5000009015, 5.0000000745))
                Line((60.5696366525, 5.0278543774), (60.5000009015, 5.0000000745))
                Line((60.2053983068, 5.9384501602), (60.5696366525, 5.0278543774))
                CenterArc((60.6000008956, 6.0962912098), 0.425, -180, 21.8014112528)
                Line((60.1750008956, 6.0962912098), (60.1750008956, 8.8375761447))
                CenterArc((60.4000008956, 8.8375761447), 0.225, 129.3531531812, 50.6468468188)
                CenterArc((59.871429792, 9.4821429163), 0.6085788712, -50.6468468188, 107.2499206873)
                CenterArc((60, 9.6771526358), 0.375, 56.6030738686, 66.7938522624)
                CenterArc((60.128570208, 9.4821429163), 0.6085788712, 123.3969261312, 107.2499206876)
                CenterArc((59.5999991044, 8.8375761447), 0.225, 0, 50.6468468188)
                Line((59.8249991044, 6.0962912098), (59.8249991044, 8.8375761447))
                CenterArc((59.3999991044, 6.0962912098), 0.425, -21.8014112528, 21.8014112528)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a funnel or hopper-shaped component with a tapered cylindrical body transitioning to a rectangular opening at the top, featuring ventilation slots or mesh cutouts along the sides for airflow or material passage.
def model_56344_3a89f085_0026():
    """Model: support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 18), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.463970054, perimeter: 16.3949222617
            with BuildLine():
                CenterArc((36.5000005513, 8.0000008111), 0.5, -36.8698959041, 36.8698959041)
                Line((37.0000005513, 8.4000001267), (37.0000005513, 8.0000008111))
                CenterArc((36.9000005513, 8.4000001267), 0.1, 0, 90)
                Line((33.1, 8.5000001267), (36.9000005513, 8.5000001267))
                CenterArc((33.1, 8.4000001267), 0.1, 90, 90)
                Line((33, 8.4000001267), (33, 8.000000076))
                CenterArc((33.5, 8.000000076), 0.5, 180, 36.8698959041)
                Line((33.0999999909, 7.7000000882), (33.9110011216, 6.6186651787))
                CenterArc((33.5110011125, 6.3186651909), 0.5, 6.943462434, 29.9264334702)
                CenterArc((35, 6.5), 1, -173.056537566, 166.113075132)
                CenterArc((36.4889988875, 6.3186651909), 0.5, 143.1301040959, 29.9264334702)
                Line((36.9000005605, 7.7000008233), (36.0889988784, 6.6186651787))
            make_face()
            with BuildLine():
                CenterArc((35, 6.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a torus or ring-shaped component with a circular cross-section, featuring a smooth curved geometry with a hollow center and uniform wall thickness throughout.
def model_56344_3a89f085_0029():
    """Model: washer M16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.663080611, perimeter: 12.0951317163
            with BuildLine():
                CenterArc((0, -15), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -15), 0.825, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a cylindrical form, featuring hemispherical or rounded ends on both sides, commonly used as a spacer, pin, or structural component in assemblies.
def model_56344_3a89f085_0030():
    """Model: Component20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-24.632621405, 0.021387757)):
                Circle(0.25)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a solid toroidal (doughnut-shaped) ring or washer with a circular cross-section, featuring a uniform wall thickness and a central hole, commonly used as a spacer, seal, or mechanical component.
def model_56344_3a89f085_0031():
    """Model: washer M12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4137166941, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((58, 10), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((58, 10), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a hexagonal torus or ring-shaped connector with a large central hole and faceted polygonal geometry, featuring triangulated mesh surfaces and an overall twisted, geometric form suitable for mechanical assembly or structural applications.
def model_56344_3a89f085_0035():
    """Model: nut M12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3331282598, perimeter: 10.6981144146
            with BuildLine():
                Line((67.1736773212, 14.4381296537), (67.1736773212, 13.2834291153))
                Line((67.1736773212, 13.2834291153), (68.1736773212, 12.7060788461))
                Line((68.1736773212, 12.7060788461), (69.1736773212, 13.2834291153))
                Line((69.1736773212, 13.2834291153), (69.1736773212, 14.4381296537))
                Line((69.1736773212, 14.4381296537), (68.1736773212, 15.0154799229))
                Line((68.1736773212, 15.0154799229), (67.1736773212, 14.4381296537))
            make_face()
            with BuildLine():
                CenterArc((68.1736773212, 13.8607793845), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a blue anodized aluminum structural beam or chassis component with an elongated parallelogram shape, featuring internal webbing/ribbing for lightweight reinforcement and two circular mounting holes at each end.
def model_56345_80dc7bcc_0000():
    """Model: Bottom Sujection"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.6230088816, perimeter: 55.7699111843
            with BuildLine():
                Line((2, -4), (2, 4))
                Line((2, 4), (-2, 4))
                Line((-2, 4), (-2, -4))
                Line((-2, -4), (2, -4))
            make_face()
            with BuildLine():
                Line((-1.5, -2), (-1, -2))
                Line((-1.5, 2), (-1.5, -2))
                Line((-1, 2), (-1.5, 2))
                Line((-1, -2), (-1, 2))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1, -2), (1, 2))
                Line((1, 2), (1.5, 2))
                Line((1.5, 2), (1.5, -2))
                Line((1.5, -2), (1, -2))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1, -3.5), (-1, -3))
                Line((-1, -3), (1, -3))
                Line((1, -3), (1, -3.5))
                Line((1, -3.5), (-1, -3.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1, 3), (-1, 3.5))
                Line((-1, 3.5), (1, 3.5))
                Line((1, 3.5), (1, 3))
                Line((1, 3), (-1, 3))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -2.5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2.5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a dual-chambered automotive undertray or skid plate with a curved, boat-like profile featuring two distinct blue-shaded compartments separated by a central ridge, reinforced ribbing along the underside, and angled end sections for mounting.
def model_56345_80dc7bcc_0001():
    """Model: Big Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1757889036, perimeter: 12.3924632763
            with BuildLine():
                Line((2.8560688433, -3.0451971787), (4.7060688433, -3.0451971787))
                Line((4.7060688433, -3.0451971787), (4.7060688433, -2.7451971787))
                Line((4.7060688433, -2.7451971787), (3.3060688433, -2.7451971787))
                CenterArc((4.0629747649, 1.0222531307), 3.8427318939, -158.2400674853, 56.880193008)
                Line((0.4940555758, -0.1523184646), (0.4940555758, -0.4023184646))
                Line((-0.0059444242, -0.1523184646), (0.4940555758, -0.1523184646))
                Line((-0.0059444242, -0.4023184646), (-0.0059444242, -0.1523184646))
                CenterArc((-0.2283955722, -0.7239702306), 0.3910810297, 25.5665465266, 29.7661065175)
                CenterArc((-0.2283955722, -0.7239702306), 0.3910810297, 18.7177526065, 6.8487939201)
                CenterArc((4.0629747649, 1.0222531307), 4.2427318939, -157.5423871127, 51.0155549213)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a flat, thin parallelogram-shaped plate with four straight edges and rounded corners, featuring no holes, slots, or additional features.
def model_56345_80dc7bcc_0003():
    """Model: Band"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.3823007676, perimeter: 233.8230076758
            with BuildLine():
                CenterArc((-17, -10.5), 1.2, -180, 90)
                Line((-17, -11.7), (17, -11.7))
                CenterArc((17, -10.5), 1.2, -90, 90)
                Line((18.2, -10.5), (18.2, 10.5))
                CenterArc((17, 10.5), 1.2, 0, 90)
                Line((17, 11.7), (-17, 11.7))
                CenterArc((-17, 10.5), 1.2, 90, 90)
                Line((-18.2, 10.5), (-18.2, -10.5))
            make_face()
            with BuildLine():
                Line((17, -11.5), (-17, -11.5))
                CenterArc((-17, -10.5), 1, -180, 90)
                Line((-18, 10.5), (-18, -10.5))
                CenterArc((-17, 10.5), 1, 90, 90)
                Line((-17, 11.5), (17, 11.5))
                CenterArc((17, 10.5), 1, 0, 90)
                Line((18, -10.5), (18, 10.5))
                CenterArc((17, -10.5), 1, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a dark gray structural component with an elongated, curved S-shaped profile featuring two raised flanges at each end and a central ribbed or latticed support structure running along its length.
def model_56345_80dc7bcc_0006():
    """Model: Small Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5156801452, perimeter: 10.8306544281
            with BuildLine():
                Line((-1.9995097254, -1.0002831543), (-1.9994628246, -1.2502831499))
                CenterArc((-5.3415064167, -6.2943376519), 6.0507636866, 23.3906539045, 33.0820508697)
                Line((1.8000000268, -3.9000000581), (0.2120018572, -3.8921954741))
                Line((1.8000000268, -3.6000000536), (1.8000000268, -3.9000000581))
                Line((0.4026086848, -3.6000000536), (1.8000000268, -3.6000000536))
                Line((0.3000000045, -3.4000000507), (0.4026086848, -3.6000000536))
                CenterArc((-5.3415064167, -6.2943376519), 6.3406454601, 27.1597918674, 25.5437749439)
                Line((-1.4995097166, -1.0002831543), (-1.4994628158, -1.2502831499))
                Line((-1.9995097254, -1.0002831543), (-1.4995097166, -1.0002831543))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat trapezoidal or wedge-shaped plate with a sloped top surface and triangular cross-bracing ribs on the upper face, designed as a lightweight structural component with minimal material while maintaining rigidity.
def model_56345_80dc7bcc_0011():
    """Model: Rubber 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.0308020111, -0.0148955769), x_dir=(-1, 0, 0), z_dir=(0, -0.9999879229, -0.0049146717))):
            # Profile area: 3.1760346965, perimeter: 7.1760346965
            with BuildLine():
                Line((6.6347669568, -4.3204019311), (4.6347669568, -4.3204019311))
                Line((6.6347669568, -2.7323845829), (6.6347669568, -4.3204019311))
                Line((4.6347669568, -2.7323845829), (6.6347669568, -2.7323845829))
                Line((4.6347669568, -4.3204019311), (4.6347669568, -2.7323845829))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a long, narrow rectangular plate or blade with a tapered wedge shape, featuring two parallel slot channels running along its length and beveled edges on the sides.
def model_56345_80dc7bcc_0012():
    """Model: Rubber 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.0451971787, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 7.4, perimeter: 11.7
            with BuildLine():
                Line((-1.7727536893, -0.4940555758), (-1.7727536893, -4.4940555758))
                Line((-1.7727536893, -4.4940555758), (0.0772463107, -4.4940555758))
                Line((0.0772463107, -4.4940555758), (0.0772463107, -0.4940555758))
                Line((0.0772463107, -0.4940555758), (-1.7727536893, -0.4940555758))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a tapered stylus or pen tool with an elongated, slender cylindrical body that gradually narrows to a sharp point at the end, featuring a flat or slightly beveled tip for precision input or marking applications.
def model_56430_4f35ba2f_0004():
    """Model: SideFrame (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1257.75, perimeter: 405.3847763109
            with BuildLine():
                Line((0, 0), (200, 0))
                Line((200, 0), (193.5, 6.5))
                Line((193.5, 6.5), (6.5, 6.5))
                Line((0, 0), (6.5, 6.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a horizontal cylindrical rod or shaft with rounded ends and shallow grooved or ribbed surface detailing on both ends, featuring a smooth central body section.
def model_56430_4f35ba2f_0005():
    """Model: CrankShaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-10, 0)):
                Circle(1.25)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: A rounded rectangular bar or shaft with chamfered or rounded edges at both ends, featuring a smooth cylindrical profile with no visible holes or protrusions.
def model_56430_4f35ba2f_0008():
    """Model: CrankShaft (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-10, 0)):
                Circle(1.25)
        # OneSide extrude, distance=27
        extrude(amount=27)
    return part.part


# Description: This is a bracket or mounting clamp with an elongated rectangular shape, featuring two circular holes for fastening, vertical slot channels along the sides, and a curved top section designed for securing or holding cylindrical components.
def model_56430_4f35ba2f_0011():
    """Model: CrankPartA (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 93.4657082647, perimeter: 56.9911485751
            with BuildLine():
                CenterArc((-2.5, 12), 2, 0, 90)
                Line((-2.5, 14), (-6, 14))
                CenterArc((-6, 12), 2, 90, 90)
                Line((-8, 12), (-8, 0))
                Line((-8, 0), (-0.5, 0))
                Line((-0.5, 0), (-0.5, 12))
            make_face()
            with BuildLine():
                CenterArc((-4.25, 2), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.25, 12), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular bar or rod with rounded ends and a uniform cylindrical profile, appearing to be a simple shaft or spacer component.
def model_56430_4f35ba2f_0018():
    """Model: Axle (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, 0)):
                Circle(2.5)
        # OneSide extrude, distance=150
        extrude(amount=150)
    return part.part


# Description: This is a cylindrical sleeve or tube with a closed bottom end and an open top end featuring a blue-textured rim or flange.
def model_56430_4f35ba2f_0021():
    """Model: RodArbor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a simple elongated rectangular profile with smoothly curved edges on both sides.
def model_56430_4f35ba2f_0022():
    """Model: HandleBar (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-15, 0)):
                Circle(4)
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tubular body featuring rounded end caps and a slight central groove or slot running along its length.
def model_56430_4f35ba2f_0023():
    """Model: Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 479.3340131507, perimeter: 246.3953202125
            with BuildLine():
                CenterArc((45.3340905116, -1.2485335751), 1.25, 92.7755880073, 354.4488239854)
                Line((-62.5, 0), (45.2735602561, 0))
                CenterArc((-62.5, -2.5), 2.5, 90, 180.0000051226)
                Line((-62.4999997765, -5), (45.5197226841, -3.7416321886))
                CenterArc((45.3340905116, -1.2485335751), 2.5, -85.7417048495, 115.7029052752)
                Line((45.3946207671, 0), (47.5, 0))
            make_face()
            with BuildLine():
                CenterArc((-62.5, -2.5), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical pin or dowel with a uniform round cross-section, tapered slightly at one end, used for alignment, fastening, or structural support purposes.
def model_56430_4f35ba2f_0026():
    """Model: HandleArbor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((0, 20)):
                Circle(2.25)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a flat diamond-shaped or rhombus-formed sheet metal part with a rectangular slot cut through its center and flanged edges that create a shallow three-dimensional structure.
def model_56430_4f35ba2f_0030():
    """Model: Floor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29881.4421860057, perimeter: 1067.2402039694
            with BuildLine():
                Line((-19.4153485655, -0.3263105897), (160, -0.3263105897))
                Line((160, -0.3263105897), (160, 197.5))
                Line((160, 197.5), (-19.4153485655, 197.5))
                Line((-19.4153485655, 197.5), (-19.4153485655, -0.3263105897))
            make_face()
            with BuildLine():
                Line((46.5286106622, 62.300030515), (46.5286106622, 162.8928244482))
                Line((46.5286106622, 162.8928244482), (102.3142595586, 162.8928244482))
                Line((102.3142595586, 162.8928244482), (102.3142595586, 62.300030515))
                Line((102.3142595586, 62.300030515), (46.5286106622, 62.300030515))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a dashboard or instrument panel cover with a trapezoidal overall shape, featuring a central curved cutout, two mounting holes, and a split design for vehicle interior installation.
def model_56436_2a8fc254_0001():
    """Model: pcb"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.35), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0215984495, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((1.96, -0.03), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.96, -0.03), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0215984495, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((-2.01, 0.35), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.01, 0.35), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0051507362, perimeter: 16.0896869741
            with BuildLine():
                CenterArc((-0.61, 1.36), 0.01, 0, 90)
                Line((-0.61, 1.37), (-2.145, 1.37))
                CenterArc((-2.145, 1.32), 0.05, 90, 90)
                Line((-2.195, 1.32), (-2.195, -0.53))
                Line((-2.195, -0.53), (-0.55, -0.53))
                Line((-0.55, 0), (-0.55, -0.53))
                CenterArc((0, 0), 0.55, 0, 180)
                Line((0.55, 0), (0.55, -0.53))
                Line((0.55, -0.53), (2.155, -0.53))
                Line((2.155, -0.53), (2.155, 1.3372110087))
                CenterArc((2.1080555522, 1.32), 0.05, 20.1341995157, 69.8658004843)
                Line((2.1080555522, 1.37), (0.61, 1.37))
                CenterArc((0.61, 1.36), 0.01, 90, 90)
                CenterArc((0.56, 1.36), 0.04, -90, 90)
                Line((0.56, 1.32), (-0.56, 1.32))
                CenterArc((-0.56, 1.36), 0.04, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((-2.01, 0.35), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.96, -0.03), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a long, narrow black plastic or composite bracket with an elongated rectangular profile, featuring a reflective blue stripe or inlay along its length and a curved end flange on the right side for mounting or attachment.
def model_56449_ad00f9f1_0000():
    """Model: Flathead Large v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.2022102596, perimeter: 30.403575265
            with BuildLine():
                CenterArc((0, 0), 1.2700000405, -90, 180)
                Line((0, 1.2700000405), (-7.3660002432, 1.2700000405))
                CenterArc((-7.3660002432, 1.0160000405), 0.254, 90, 90)
                Line((-7.6200002432, 0.7620000162), (-7.6200002432, 1.0160000405))
                CenterArc((-7.8740002432, 0.7620000162), 0.254, -90, 90)
                Line((-10.1600003242, 0.5080000162), (-7.8740002432, 0.5080000162))
                Line((-10.1600003242, 0.5080000162), (-10.1600003242, -0.5080000162))
                Line((-10.1600003242, -0.5080000162), (-7.8740002432, -0.5080000162))
                CenterArc((-7.8740002432, -0.7620000162), 0.254, 0, 90)
                Line((-7.6200002432, -0.7620000162), (-7.6200002432, -1.0160000405))
                CenterArc((-7.3660002432, -1.0160000405), 0.254, 180, 90)
                Line((0, -1.2700000405), (-7.3660002432, -1.2700000405))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a curved rectangular tray or bin with a saddle-shaped (concave) interior surface, featuring a ribbed or lattice pattern on the bottom and walls for structural reinforcement.
def model_56458_c027ed41_0003():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.9225439349, perimeter: 16.2300585798
            with BuildLine():
                Line((-6.6564023547, 9.9846035321), (-5.8243520604, 8.7365280905))
                CenterArc((0, 0), 10.5, 90, 33.690067526)
                Line((0, 12), (0, 10.5))
                CenterArc((0, 0), 12, 90, 33.690067526)
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a rectangular block or housing with a ribbed top surface featuring parallel longitudinal ribs or fins running across its length, creating a reinforced structural pattern.
def model_56458_c027ed41_0004():
    """Model: szyna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1806706651, perimeter: 8.4140698196
            with BuildLine():
                Line((-5.8243520604, 8.7365280905), (-6.4080192366, 9.6120288549))
                Line((-6.4080192366, 9.6120288549), (-6.6433916459, 9.3102651012))
                CenterArc((3.0786179194, 2.5), 11.8700118255, 144.988767822, 15.0592325171)
                Line((-7.1397510364, 6.2070329063), (-8.0789418269, 6.5504371669))
                CenterArc((3.0786179194, 2.5), 10.8700118255, 144.988767822, 15.0714087567)
            make_face()
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True)
    return part.part


# Description: This is a rectangular storage bin or tray with curved sides that taper inward toward the top and a latticed or ribbed interior surface for structural reinforcement.
def model_56458_c027ed41_0005():
    """Model: poduszka_g"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.9084085002, perimeter: 12.6694932185
            with BuildLine():
                CenterArc((0, 0), 10.5, 90, 28.7663400717)
                Line((-5.0530072042, 9.204190252), (-4.4043526216, 7.9631449807))
                CenterArc((0, 0), 9.1, 90, 28.9466349928)
                Line((0, 9.1), (0, 10.5))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a 3D CAD part consisting of two parallel dark gray parallelogram-shaped flat plates or flanges positioned at different heights, resembling a stepped or stacked configuration commonly used in structural or mounting applications.
def model_56459_7b640aed_0001():
    """Model: scianki_d"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180, perimeter: 362
            with BuildLine():
                Line((-90, 64), (-90, 65))
                Line((90, 64), (-90, 64))
                Line((90, 65), (90, 64))
                Line((-90, 65), (90, 65))
            make_face()
            # Profile area: 180, perimeter: 362
            with BuildLine():
                Line((90, -64), (-90, -64))
                Line((-90, -64), (-90, -65))
                Line((-90, -65), (90, -65))
                Line((90, -65), (90, -64))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a 3D CAD part depicting a flat parallelogram or trapezoidal plate with a single internal diagonal line dividing it into two triangular sections, featuring a simple planar geometry with no holes, slots, or complex features.
def model_56459_7b640aed_0002():
    """Model: podloga"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23400, perimeter: 620
            with BuildLine():
                Line((90, -65), (90, 65))
                Line((90, 65), (-90, 65))
                Line((-90, 65), (-90, -65))
                Line((-90, -65), (90, -65))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a curved duct or air flow component with an overall dome-like or curved shell shape, featuring a large central circular opening and mesh or perforated surfaces on the upper curved section, designed for air passage or filtration applications.
def model_56459_7b640aed_0005():
    """Model: otwor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 65), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 76.2103556706, perimeter: 60.596212135
            with BuildLine():
                CenterArc((0, -17), 3, 0, 360)
                CenterArc((0, 141.277027027), 161.277027027, -90, 2.91352762)
                CenterArc((0, -20), 8.2001580633, 1.45676381, 177.08647238)
                CenterArc((0, 141.277027027), 161.277027027, -92.91352762, 2.91352762)
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a pair of identical dark blue rectangular plates or fins with a slightly curved or tapered profile, featuring subtle surface details or ridges along their length, positioned at an angle to suggest a 3D perspective.
def model_56459_7b640aed_0012():
    """Model: scianki-k"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 128, perimeter: 258
            with BuildLine():
                Line((-89, -64), (-90, -64))
                Line((-89, -64), (-89, 64))
                Line((-89, 64), (-90, 64))
                Line((-90, 64), (-90, -64))
            make_face()
            # Profile area: 128, perimeter: 258
            with BuildLine():
                Line((90, 64), (89, 64))
                Line((89, 64), (89, -64))
                Line((90, -64), (89, -64))
                Line((90, -64), (90, 64))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a cylindrical roller or foam roller with a uniform circular cross-section, featuring a textured or knurled surface pattern across its length and rounded ends.
def model_56461_9a5be0e9_0002():
    """Model: wal-p"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) component featuring a large central oval hole and radial fin or blade-like structures extending across its surface, likely designed for heat dissipation or fluid dynamic purposes.
def model_56466_e682bec3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 169.6460032938, perimeter: 75.3982236862
            with BuildLine():
                CenterArc((0, 0), 8.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a polyhedron-based geometric solid with a dodecagonal (12-sided) base structure featuring spherical or ellipsoidal voids carved through its center and radial triangular facets extending outward from the core, creating a complex symmetrical form with deep cavities and pointed projections.
def model_56468_c18aba85_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.7166818828, perimeter: 30.0537141976
            with BuildLine():
                Line((-1.8660254038, -0.943375673), (-0.1339745962, 1.943375673))
                Line((-0.1339745962, 1.943375673), (-1.7679491924, 4.8867513459))
                Line((-1.7679491924, 4.8867513459), (-5.1339745962, 4.943375673))
                Line((-5.1339745962, 4.943375673), (-6.8660254038, 2.056624327))
                Line((-6.8660254038, 2.056624327), (-5.2320508076, -0.8867513459))
                Line((-5.2320508076, -0.8867513459), (-1.8660254038, -0.943375673))
            make_face()
            with BuildLine():
                CenterArc((-3.5, 2), 1.5684249054, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical rod or tube with rounded ends, tilted at an angle, featuring a uniform diameter throughout its length with no holes, slots, or flanges.
def model_56477_620f7fc8_0009():
    """Model: Handle leather v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.638937829, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a cylindrical spacer or bushing with a central axial bore and two smaller radial holes passing through opposite sides of the tube.
def model_56486_82b3e23a_0003():
    """Model: Tulejka 3x6x10mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a tapered cylindrical rod with a uniform diameter that gradually reduces toward one end, featuring a slightly rounded or chamfered tip.
def model_56486_82b3e23a_0004():
    """Model: Popychacz B v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # Symmetric extrude, each_side=2.4
        extrude(amount=2.4, both=True)
    return part.part


# Description: This is a snowboard or wakeboard featuring an elongated symmetrical design with rounded end caps, a central blue stripe running along the top surface, and a dark gray base material with curved edges for aerodynamic performance.
def model_56486_82b3e23a_0005():
    """Model: Tloczysko v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6249192865, perimeter: 22.931535041
            with BuildLine():
                Line((0, 0.3), (-3.9747067469, 0.5013242864))
                CenterArc((-4, 0.0019644448), 0.5, 87.1003691065, 185.74277209)
                Line((0, -0.3), (-3.9751990936, -0.4974200914))
                Line((0, -0.3), (3.9751990936, -0.4974200914))
                CenterArc((4, 0.0019644448), 0.5, -92.8431411966, 185.74277209)
                Line((0, 0.3), (3.9747067469, 0.5013242864))
            make_face()
            with BuildLine():
                CenterArc((4, 0.0019644448), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4, 0.0019644448), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a cylindrical roller or foam roller with a textured, knurled surface along its length and rounded hemispherical ends, designed for massage, exercise, or mechanical application.
def model_56486_82b3e23a_0014():
    """Model: Sworzen korby v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a cylindrical spacer or bushing with a central through-hole and a hexagonal outer profile, featuring a mesh/lattice texture pattern on its surface.
def model_56486_82b3e23a_0015():
    """Model: Lacznik A v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a toroidal ring or torus-shaped component with a smooth, curved cross-section and a central hollow opening, featuring a uniform wall thickness throughout its circumference.
def model_56486_82b3e23a_0017():
    """Model: Kolo rozrzadu v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0681415022, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a cylindrical threaded coupling or bushing with an internal hexagonal bore and external thread pattern, designed to connect two components with secure rotational alignment.
def model_56486_82b3e23a_0020():
    """Model: Tulejka 4x6x6mm v0 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a cylindrical bushing or sleeve with a hollow tubular body, featuring a rounded or domed top surface and a smooth inner bore, designed for use as a bearing component or mechanical connector.
def model_56486_82b3e23a_0022():
    """Model: Tulejka 6x8x6mm v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a curved bracket or clamp component with a distinctive C-shaped body, featuring two side flanges with textured/knurled surfaces, a central curved chamber, and what appears to be mounting holes or slots distributed across its surfaces.
def model_56486_82b3e23a_0023():
    """Model: Korba v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3373073675, perimeter: 12.8986687554
            with BuildLine():
                Line((0.4463961922, 0.8371534741), (0.3984778792, 1.3848622971))
                CenterArc((0, 1.35), 0.4, 5, 170)
                Line((-0.4463961921, 0.8371534741), (-0.3984778792, 1.3848622971))
                CenterArc((-1.1437324808, 0.898162494), 0.7000000001, -120.5935417697, 115.5935417697)
                CenterArc((0, 0.3), 1.5, -179.8320434616, 179.6640869232)
                CenterArc((1.1437324808, 0.898162494), 0.7, -175, 115.5935417697)
            make_face()
            with BuildLine():
                CenterArc((0, 1.35), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.2236067977, 0.2), (0.2236067977, 0.2))
                CenterArc((0, 0), 0.3, 138.1896851042, 263.6206297916)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a cylindrical drum or pulley with a solid body, featuring two large circular holes on opposite sides and a mesh or perforated upper surface, likely designed as a filter drum or ventilated cylindrical component.
def model_56486_82b3e23a_0024():
    """Model: Rozrzad v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4844025288, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0.35), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: A long, narrow rectangular light fixture with a black aluminum extrusion housing and integrated blue LED strip running along its length, tapering slightly at one end for mounting.
def model_56489_241ed182_0002():
    """Model: Limit_Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1021017612, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((15.8535367612, -59.3134346064), 0.35, 134.4153085972, 91.1693828056)
                CenterArc((15.8535367612, -59.3134346064), 0.35, -134.4153085972, 268.8306171944)
            make_face()
            with BuildLine():
                CenterArc((15.8535367612, -59.3134346064), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.1826027893, perimeter: 34.1340482378
            with BuildLine():
                Line((15.608587787, -59.0634346064), (-0.9015142645, -59.0634346064))
                CenterArc((-1.1464632388, -59.3134346064), 0.35, -45.5846914028, 91.1693828056)
                Line((-0.9015142645, -59.5634346064), (15.608587787, -59.5634346064))
                CenterArc((15.8535367612, -59.3134346064), 0.35, 134.4153085972, 91.1693828056)
            make_face()
            # Profile area: 0.1021017612, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((-1.1464632388, -59.3134346064), 0.35, -45.5846914028, 91.1693828056)
                CenterArc((-1.1464632388, -59.3134346064), 0.35, 45.5846914028, 268.8306171944)
            make_face()
            with BuildLine():
                CenterArc((-1.1464632388, -59.3134346064), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a segmented angular connector or joint assembly composed of four cubic modules arranged in a zigzag S-curve configuration, featuring triangulated faces and designed to articulate or flex along its bent axis.
def model_56489_241ed182_0010():
    """Model: Plus"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3825000159, perimeter: 8.4000001371
            with BuildLine():
                Line((-0.3750000067, 0.1), (-0.3, 0.1))
                Line((-0.3, 0.1), (-0.3, 0.9000000134))
                Line((-0.3, 0.9000000134), (-1.4000000209, 0.9000000134))
                Line((-1.4000000209, 0.9000000134), (-1.4000000209, 2.1000000313))
                Line((-1.4000000209, 2.1000000313), (-1.1000000164, 2.5000000373))
                Line((-1.1000000164, 3.0000000447), (-1.1000000164, 2.5000000373))
                Line((-1.2000000179, 3.0000000447), (-1.1000000164, 3.0000000447))
                Line((-1.2000000179, 2.5000000373), (-1.2000000179, 3.0000000447))
                Line((-1.5000000224, 2.1000000313), (-1.2000000179, 2.5000000373))
                Line((-1.5000000224, 0.8000000119), (-1.5000000224, 2.1000000313))
                Line((-0.3750000067, 0.8000000119), (-1.5000000224, 0.8000000119))
                Line((-0.3750000067, 0.1), (-0.3750000067, 0.8000000119))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a solid elliptical or oval disc with a smooth, curved surface and a slight 3D depth, featuring no holes, slots, or additional features.
def model_56489_241ed182_0013():
    """Model: Glass"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 311.025526687, perimeter: 62.5176938064
            Circle(9.95)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a pulley or wheel bracket assembly featuring a circular wheel with radial spokes mounted on an angled blue support arm with a tapered triangular base, designed to guide or support belt/cable routing.
def model_56490_0a0fba77_0000():
    """Model: Gym Symbol v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 71.4749406379, perimeter: 48.4043965639
            with BuildLine():
                CenterArc((-1.8105046084, 3.5520576521), 5.1678828218, -147.544388274, 65.1409547363)
                Line((0.5959049827, -7.494589475), (-1.1273260551, -1.5704690608))
                Line((8.5377591727, 8.5937763682), (0.5959049827, -7.494589475))
                Line((0.5959049827, 4.3976648243), (8.5377591727, 8.5937763682))
                CenterArc((-1.6386647977, 3.7700950726), 2.3210225971, -139.7587016254, 155.4458809526)
                Line((-6.1712026354, 0.77873373), (-3.4103723441, 2.2706957708))
            make_face()
            # Profile area: 10.4072973039, perimeter: 11.4359938359
            with Locations((-1.685876596, 3.7737427824)):
                Circle(1.8200949481)
            # Profile area: 34.0444325931, perimeter: 28.5670086788
            with BuildLine():
                Line((0.13109482, 5.3488208936), (2.8801375292, 6.7668977066))
                CenterArc((-1.6564850493, 3.7719522781), 5.4360502701, 33.4316245035, 168.4492857976)
                Line((-6.7009248333, 1.7460525262), (-3.908914109, 3.2443872563))
                CenterArc((-1.6596745394, 3.8565275359), 2.331050056, 39.8052983956, 155.419261118)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal or pentagonal prism with a tapered pyramidal end, featuring a elongated tubular body that transitions from a pointed/faceted head to a blunt rectangular base, resembling a mechanical shaft, drill bit, or connector component.
def model_56568_d3018fcb_0003():
    """Model: Head v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.0783890304, perimeter: 27.344069782
            with BuildLine():
                Line((5.1808409705, 34.3698764973), (6.8568108294, 37.932332677))
                Line((5.1808409705, 34.3698764973), (10.5920169408, 31.8241700044))
                Line((15.1932015647, 31.8241700044), (10.5920169408, 31.8241700044))
                Line((15.1932015647, 32.3338674445), (15.1932015647, 31.8241700044))
                Line((15.1932015647, 32.4591700044), (15.1932015647, 32.3338674445))
                Line((13.7179330381, 36.1080171789), (15.1932015647, 32.4591700044))
                Line((7.3974462677, 39.0815120898), (13.7179330381, 36.1080171789))
                Line((6.8568108294, 37.932332677), (7.3974462677, 39.0815120898))
            make_face()
        # OneSide extrude, distance=13.208
        extrude(amount=13.208)
    return part.part


# Description: This is a blue anodized aluminum bracket or mounting component with an angular L-shaped design featuring a slotted top opening, a rectangular window/cutout on the front face, and what appears to be mounting holes or fastening points on the lower section.
def model_56568_d3018fcb_0005():
    """Model: Arm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 209.5257898435, perimeter: 111.4684733158
            with BuildLine():
                Line((29.5, 4.2227519809), (21.8917875283, 9.731))
                Line((29.5, 4.2227519809), (29.5, 25.6031845265))
                Line((15.1932015647, 32.3338674445), (29.5, 25.6031845265))
                Line((15.1932015647, 32.3338674445), (15.1932015647, 31.8241700044))
                Line((15.1932015647, 31.8241700044), (10.5920169408, 31.8241700044))
                Line((5.1808409705, 34.3698764973), (10.5920169408, 31.8241700044))
                Line((4.6813660901, 33.3081883263), (5.1808409705, 34.3698764973))
                Line((2.4118570964, 32.9230672352), (4.6813660901, 33.3081883263))
                Line((2.4118570964, 32.9230672352), (5.3239036246, 31.5530848515))
                Line((5.3239036246, 31.5530848515), (5.5, 31.4702397013))
                Line((5.5, 31.4702397013), (11.245897064, 28.7670625096))
                Line((11.245897064, 28.7670625096), (21.8917875283, 23.758666437))
                Line((21.8917875283, 20.5125), (21.8917875283, 23.758666437))
                Line((21.8917875283, 17.1289487758), (21.8917875283, 20.5125))
                Line((21.8917875283, 9.731), (21.8917875283, 17.1289487758))
            make_face()
            with BuildLine():
                CenterArc((24.6934534606, 12.2830779314), 2.3495, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=13.208
        extrude(amount=13.208)
    return part.part


# Description: This is a rectangular trapezoidal enclosure or duct component with a tapered box shape, featuring internal ribbing/bracing structures, multiple openings on the top and side faces, and a hollow interior design typical of aerospace or industrial ducting.
def model_56568_d3018fcb_0006():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 134.1770228294, perimeter: 66.7154938242
            with BuildLine():
                Line((5.5, 3), (29.5, 3))
                Line((29.5, 3), (29.5, 4.2227519809))
                Line((29.5, 4.2227519809), (21.8917875283, 9.731))
                Line((16.2047631413, 9.731), (21.8917875283, 9.731))
                Line((7.1212851774, 9.731), (16.2047631413, 9.731))
                Line((5.5, 9.731), (7.1212851774, 9.731))
                Line((5.5, 3), (5.5, 9.731))
            make_face()
            with BuildLine():
                CenterArc((17.1572631413, 5.4940343462), 1.42875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=16.51
        extrude(amount=16.51)
    return part.part


# Description: This is a rectangular box or channel component with an elongated hexagonal or prismatic shape, featuring a central open slot or groove running lengthwise along the top surface, and tapered or angled side walls that converge toward the ends.
def model_56568_d3018fcb_0010():
    """Model: Stage Slider v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.4374153773, perimeter: 12.7973903122
            with BuildLine():
                Line((21.8917875283, 17.1289487758), (21.8917875283, 20.5125))
                Line((19.5672851774, 20.5125), (21.8917875283, 20.5125))
                Line((19.5672851774, 20.5125), (19.5672851774, 18.925))
                Line((19.5672851774, 18.925), (18.3505923721, 18.925))
                Line((18.3505923721, 18.925), (20.1466435963, 17.1289487758))
                Line((20.1466435963, 17.1289487758), (21.8917875283, 17.1289487758))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


# Description: This is a segmented auger or screw conveyor shaft consisting of five connected helical flighting sections arranged in a diagonal line, used for transporting bulk materials through a tube or casing.
def model_56711_61a0b988_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 53 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.544467506, perimeter: 12.3817863442
            with BuildLine():
                _nurbs_edge([(-11.2413446837, 1.0268806072), (-11.2446210079, 1.0584066305), (-11.2415220768, 1.0680994462), (-11.2298696351, 1.0879960479), (-11.217739308, 1.1087086412), (-11.1873249322, 1.1422299744), (-11.1298600829, 1.1765704895), (-11.0498044622, 1.2244110614), (-10.921153051, 1.2677376892), (-10.8096709833, 1.2800517331), (-10.7303674498, 1.2888114126), (-10.6631039821, 1.2818838889), (-10.6234458062, 1.2690485424), (-10.5858091132, 1.2568674477), (-10.5699112371, 1.2452845186), (-10.5479869003, 1.2181074012), (-10.5241640394, 1.1885768986), (-10.495693308, 1.1313376033), (-10.4733605056, 1.0540000925), (-10.4517125672, 0.9790342356), (-10.4356814174, 0.8876418114), (-10.4315219678, 0.8199235581), (-10.4307380162, 0.807160372), (-10.430360456, 0.7952604591), (-10.4303520741, 0.7847132236)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0462110889, 0.0462110889, 0.0462110889, 0.0943173689, 0.0943173689, 0.0943173689, 0.1613353486, 0.1613353486, 0.1613353486, 0.2090090481, 0.2090090481, 0.2090090481, 0.254252692, 0.254252692, 0.254252692, 0.3034141806, 0.3034141806, 0.3034141806, 0.3510680692, 0.3510680692, 0.3510680692, 0.3600496276, 0.3600496276, 0.3600496276, 0.3600496276], 3)
                _nurbs_edge([(-10.4303520741, 0.7847132236), (-10.4460207732, 0.7847482617), (-10.4648414295, 0.7853126472), (-10.4859898099, 0.7862722664), (-10.6122109321, 0.791999618), (-10.8216686181, 0.814110774), (-11.0370659781, 0.7594111242), (-11.1949623773, 0.7193137073), (-11.3519291989, 0.6347786111), (-11.4726626475, 0.5156352699), (-11.6473884307, 0.3432106945), (-11.7484782034, 0.1073568941), (-11.7618292305, -0.1225459082), (-11.7719051245, -0.2960513795), (-11.7293098585, -0.4662773116), (-11.6529404775, -0.603150531), (-11.5698759593, -0.7520231272), (-11.4542543523, -0.860603144), (-11.3420533903, -0.9416512749), (-11.2228656777, -1.0277462703), (-11.106456879, -1.0884482149), (-10.9793474155, -1.1303935136), (-10.8569446432, -1.1707856348), (-10.7184892871, -1.1889905153), (-10.5785659772, -1.1657928858), (-10.417075467, -1.1390196696), (-10.2636551153, -1.0625380599), (-10.1145237213, -0.9518228283), (-10.0143301408, -0.8774390572), (-9.9145474646, -0.7868013994), (-9.8121426748, -0.6798187005)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4558747214, 0.4558747214, 0.4558747214, 0.4558747214, 0.4670369822, 0.4670369822, 0.4670369822, 0.5336573594, 0.5336573594, 0.5336573594, 0.5824932304, 0.5824932304, 0.5824932304, 0.6531686388, 0.6531686388, 0.6531686388, 0.7065067013, 0.7065067013, 0.7065067013, 0.7645207955, 0.7645207955, 0.7645207955, 0.8261474256, 0.8261474256, 0.8261474256, 0.885492105, 0.885492105, 0.885492105, 0.9539839279, 0.9539839279, 0.9539839279, 1, 1, 1, 1], 3)
                Line((-10, -0.5), (-9.8121426748, -0.6798187005))
                _nurbs_edge([(-11.5, 1), (-11.5024059289, 1.0231507528), (-11.5039370964, 1.0684719582), (-11.4963914098, 1.1335130007), (-11.4666329673, 1.2143469597), (-11.3972379021, 1.3052950384), (-11.2977628893, 1.3853279363), (-11.1724624346, 1.4528768891), (-11.0287977291, 1.5052639302), (-10.8766639081, 1.5390196983), (-10.7266693118, 1.5505583071), (-10.5886651423, 1.5367472283), (-10.470275907, 1.4955093107), (-10.3751714848, 1.4264469082), (-10.3022059804, 1.3313611051), (-10.2478107454, 1.2142413776), (-10.2079837291, 1.0814164648), (-10.1802027429, 0.9415024311), (-10.1659269964, 0.8058028777), (-10.1708552746, 0.6872224432), (-10.2018523851, 0.5969372829), (-10.2648041657, 0.5417932509), (-10.3618513013, 0.520985303), (-10.4896117856, 0.5242637797), (-10.6408602708, 0.5361035426), (-10.8056951585, 0.538939876), (-10.9729108826, 0.5168613479), (-11.131236192, 0.4588707056), (-11.2707329988, 0.3629728031), (-11.3832435049, 0.2346066704), (-11.4626561256, 0.0839231809), (-11.5052347902, -0.0765078719), (-11.509944233, -0.2341888955), (-11.4787559704, -0.3790280593), (-11.4170590961, -0.5059341673), (-11.3324038686, -0.6136201677), (-11.2331563527, -0.7031788325), (-11.1271480031, -0.7767136234), (-11.0204238516, -0.8360355423), (-10.91569271, -0.8811144343), (-10.8129197511, -0.9103865354), (-10.7104454982, -0.9215175632), (-10.6058529483, -0.9119600955), (-10.4970918195, -0.879708273), (-10.3828825683, -0.8235306207), (-10.2624458791, -0.7427204448), (-10.1608212515, -0.6581265371), (-10.0815836227, -0.5834336408), (-10.0274179758, -0.5286436704), (-10, -0.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                Line((-11.2413446837, 1.0268806072), (-11.5, 1))
            make_face()
            # Profile area: 3, perimeter: 13
            with BuildLine():
                Line((-13, 0.5), (-13, 1.5))
                Line((-14, 0.5), (-13, 0.5))
                Line((-14, 1.5), (-14, 0.5))
                Line((-14.5, 1.5), (-14, 1.5))
                Line((-14.5, -1), (-14.5, 1.5))
                Line((-14, -1), (-14.5, -1))
                Line((-14, 0), (-14, -1))
                Line((-13, 0), (-14, 0))
                Line((-13, -1), (-13, 0))
                Line((-12.5, -1), (-13, -1))
                Line((-12.5, 1.5), (-12.5, -1))
                Line((-13, 1.5), (-12.5, 1.5))
            make_face()
            # Profile area: 0.402519267, perimeter: 3.5054805425
            with BuildLine():
                Line((4.38139172, 0.0310138), (3.13139172, 0.0310138))
                Line((3.13139172, 0.0310138), (2.9579985121, -0.2521238853))
                Line((2.9579985121, -0.2521238853), (4.5512743312, -0.2521238853))
                Line((4.5512743312, -0.2521238853), (4.38139172, 0.0310138))
            make_face()
            # Profile area: 2.37772346, perimeter: 12.1250608719
            with BuildLine():
                Line((4.5512743312, -0.2521238853), (4.38139172, 0.0310138))
                Line((5, -1), (4.5512743312, -0.2521238853))
                Line((5.5, -1), (5, -1))
                Line((4, 1.5), (5.5, -1))
                Line((3.515340128, 1.47443312), (4, 1.5))
                Line((2, -1), (3.515340128, 1.47443312))
                Line((2.5, -1), (2, -1))
                Line((2.9579985121, -0.2521238853), (2.5, -1))
                Line((3.13139172, 0.0310138), (2.9579985121, -0.2521238853))
                Line((3.76278344, 1.0620276), (3.13139172, 0.0310138))
                Line((4.38139172, 0.0310138), (3.76278344, 1.0620276))
            make_face()
            # Profile area: 0.402519267, perimeter: 3.5054805425
            with BuildLine():
                Line((0.6509996446, 0.0150035336), (-0.5990003554, 0.0150035336))
                Line((-0.5990003554, 0.0150035336), (-0.7723935633, -0.2681341517))
                Line((-0.7723935633, -0.2681341517), (0.8208822557, -0.2681341517))
                Line((0.8208822557, -0.2681341517), (0.6509996446, 0.0150035336))
            make_face()
            # Profile area: 2.37772346, perimeter: 12.1250608719
            with BuildLine():
                Line((0.8208822557, -0.2681341517), (0.6509996446, 0.0150035336))
                Line((1.2696079246, -1.0160102664), (0.8208822557, -0.2681341517))
                Line((1.7696079246, -1.0160102664), (1.2696079246, -1.0160102664))
                Line((0.2696079246, 1.4839897336), (1.7696079246, -1.0160102664))
                Line((-0.2150519475, 1.4584228536), (0.2696079246, 1.4839897336))
                Line((-1.7303920754, -1.0160102664), (-0.2150519475, 1.4584228536))
                Line((-1.2303920754, -1.0160102664), (-1.7303920754, -1.0160102664))
                Line((-0.7723935633, -0.2681341517), (-1.2303920754, -1.0160102664))
                Line((-0.5990003554, 0.0150035336), (-0.7723935633, -0.2681341517))
                Line((0.0323913645, 1.0460173336), (-0.5990003554, 0.0150035336))
                Line((0.6509996446, 0.0150035336), (0.0323913645, 1.0460173336))
            make_face()
            # Profile area: 1.3904657953, perimeter: 7.557872934
            with BuildLine():
                Line((-3.5, 0.5), (-4.7499928783, 1.5))
                Line((-4.7499928783, 1.5), (-5.024746683, 1.1565597009))
                Line((-5.024746683, 1.1565597009), (-3.8915535131, 0.25))
                Line((-3.8915535131, 0.25), (-5.024746683, -0.9620608788))
                Line((-5.024746683, -0.9620608788), (-4.458150098, -0.9620608788))
                Line((-4.458150098, -0.9620608788), (-3.5, 0.062774322))
                Line((-3.5, 0.062774322), (-3.5, 0.5))
            make_face()
            # Profile area: 1.25, perimeter: 6
            with BuildLine():
                Line((-3.5, 0.062774322), (-3.5, 0.5))
                Line((-3.5, -1), (-3.5, 0.062774322))
                Line((-3, -1), (-3.5, -1))
                Line((-3, 1.5), (-3, -1))
                Line((-3.5, 1.5), (-3, 1.5))
                Line((-3.5, 0.5), (-3.5, 1.5))
            make_face()
            # Profile area: 2.37772346, perimeter: 12.1250608719
            with BuildLine():
                Line((-6.4487256688, -0.2521238853), (-6.61860828, 0.0310138))
                Line((-6, -1), (-6.4487256688, -0.2521238853))
                Line((-5.5, -1), (-6, -1))
                Line((-7, 1.5), (-5.5, -1))
                Line((-7.484659872, 1.47443312), (-7, 1.5))
                Line((-9, -1), (-7.484659872, 1.47443312))
                Line((-8.5, -1), (-9, -1))
                Line((-8.0420014879, -0.2521238853), (-8.5, -1))
                Line((-7.86860828, 0.0310138), (-8.0420014879, -0.2521238853))
                Line((-7.23721656, 1.0620276), (-7.86860828, 0.0310138))
                Line((-6.61860828, 0.0310138), (-7.23721656, 1.0620276))
            make_face()
            # Profile area: 0.402519267, perimeter: 3.5054805425
            with BuildLine():
                Line((-6.61860828, 0.0310138), (-7.86860828, 0.0310138))
                Line((-7.86860828, 0.0310138), (-8.0420014879, -0.2521238853))
                Line((-8.0420014879, -0.2521238853), (-6.4487256688, -0.2521238853))
                Line((-6.4487256688, -0.2521238853), (-6.61860828, 0.0310138))
            make_face()
        # Symmetric extrude, each_side=-0.5
        extrude(amount=-0.5, both=True)
    return part.part


# Description: This is a hexagonal or octagonal container/enclosure with a faceted geometric design, featuring an open or mesh top section with radiating internal support structures and a solid dark base, resembling a modern geometric storage box or protective cage.
def model_56799_4512d89e_0002():
    """Model: Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6144430541, perimeter: 6.4476053574
            with BuildLine():
                Line((0.3278609362, 0.5678717993), (-0.3278609362, 0.5678717993))
                Line((-0.3278609362, 0.5678717993), (-0.6557218724, 0))
                Line((-0.6557218724, 0), (-0.3278609362, -0.5678717993))
                Line((-0.3278609362, -0.5678717993), (0.3278609362, -0.5678717993))
                Line((0.3278609362, -0.5678717993), (0.6557218724, 0))
                Line((0.6557218724, 0), (0.3278609362, 0.5678717993))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a hexagonal or octagonal box-shaped component with pointed pyramidal vertices at the corners, featuring a recessed central cavity or channel running along its length, and triangular faceted surfaces on the ends.
def model_56799_4512d89e_0012():
    """Model: M8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.744421794, perimeter: 6.670196123
            with BuildLine():
                Line((0.3464101667, 0.6000000089), (-0.3464101667, 0.6000000089))
                Line((-0.3464101667, 0.6000000089), (-0.6928203334, 0))
                Line((-0.6928203334, 0), (-0.3464101667, -0.6000000089))
                Line((-0.3464101667, -0.6000000089), (0.3464101667, -0.6000000089))
                Line((0.3464101667, -0.6000000089), (0.6928203334, 0))
                Line((0.6928203334, 0), (0.3464101667, 0.6000000089))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a slanted face that creates an asymmetrical parallelogram-like profile, featuring flat faceted surfaces and angular edges throughout.
def model_57000_cd1ddece_0001():
    """Model: lipo v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.9032, perimeter: 15.24
            with BuildLine():
                Line((2.54, -1.27), (2.54, 1.27))
                Line((2.54, 1.27), (-2.54, 1.27))
                Line((-2.54, 1.27), (-2.54, -1.27))
                Line((-2.54, -1.27), (2.54, -1.27))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a polyhedral geometric solid with an irregular, faceted shape featuring multiple planar surfaces in varying shades of blue and dark gray, characterized by sharp edges and angular faces with no apparent holes, slots, or curved surfaces.
def model_57000_cd1ddece_0006():
    """Model: hero v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((1.27, -1.27), (1.27, 1.27))
                Line((1.27, 1.27), (-1.27, 1.27))
                Line((-1.27, 1.27), (-1.27, -1.27))
                Line((-1.27, -1.27), (1.27, -1.27))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a flat, quadrilateral panel or plate with a trapezoidal shape, featuring internal triangular reinforcement ribs or webs for structural stiffening.
def model_57142_38a8651d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3557.9380400259, perimeter: 227.9822971503
            with BuildLine():
                CenterArc((-73, 53), 7, 90, 90)
                Line((-80, 7), (-80, 53))
                CenterArc((-73, 7), 7, -180, 90)
                Line((-27, 0), (-73, 0))
                CenterArc((-27, 7), 7, -90, 90)
                Line((-20, 53), (-20, 7))
                CenterArc((-27, 53), 7, 0, 90)
                Line((-73, 60), (-27, 60))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a elongated parallel-sided trim or molding piece with a slender, flattened parallelogram profile featuring a dark gray upper surface and a blue lower surface, designed for edge finishing or architectural detailing.
def model_57146_b0c068a5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 112.6112667726, perimeter: 64.3686027205
            with BuildLine():
                Line((-15.24, -2.54), (15.24, -2.54))
                Line((15.24, -2.54), (9.8297243642, 1.1922991624))
                CenterArc((5.5027550269, -5.0799999659), 7.62, 55.4, 34.5999997991)
                Line((5.5027550536, 2.5400000341), (3.5111296481, 2.5400000411))
                CenterArc((3.5111296348, -1.2699999589), 3.81, 89.9999997991, 36)
                Line((1.1205099533, 1.7025321694), (1.2716678344, 1.8123547976))
                CenterArc((0.0007790531, 3.2437095476), 1.905, -126, 71.9999997991)
                Line((-1.1189518525, 1.7025321733), (-1.2701097501, 1.8123548143))
                CenterArc((-3.5095715613, -1.2699999342), 3.81, 54, 35.9999997991)
                Line((-3.5095715479, 2.5400000658), (-5.501196944, 2.5400000727))
                CenterArc((-5.5011969707, -5.0799999273), 7.62, 89.9999997991, 34.5922902293)
                Line((-15.24, -2.54), (-9.8273222408, 1.1928814002))
            make_face()
        # OneSide extrude, distance=104.14
        extrude(amount=104.14)
    return part.part


# Description: This is a flat, elongated parallelepiped (rectangular tray or plate) with a slight curved or warped surface, featuring internal diagonal cross-bracing or reinforcement ribs visible on the top face.
def model_57152_3f47822e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 154.8384, perimeter: 71.12
            with BuildLine():
                Line((15.24, -2.54), (15.24, 2.54))
                Line((15.24, 2.54), (-15.24, 2.54))
                Line((-15.24, 2.54), (-15.24, -2.54))
                Line((-15.24, -2.54), (15.24, -2.54))
            make_face()
        # OneSide extrude, distance=101.6
        extrude(amount=101.6)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or tray with a shallow depth, featuring a beveled or chamfered edge on the left side and internal cross-bracing or reinforcement details visible on the top surface.
def model_57152_9359fc8e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 154.8384, perimeter: 71.12
            with BuildLine():
                Line((15.24, -2.54), (15.24, 2.54))
                Line((15.24, 2.54), (-15.24, 2.54))
                Line((-15.24, 2.54), (-15.24, -2.54))
                Line((-15.24, -2.54), (15.24, -2.54))
            make_face()
        # OneSide extrude, distance=96.52
        extrude(amount=96.52)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a curved, elongated oval opening or slot running through its upper portion, featuring a tapered/rounded body with mesh-textured surfaces indicating a hollow or perforated design.
def model_57153_2ec8170f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 98.1747704247, perimeter: 78.5398163397
            with BuildLine():
                CenterArc((0, -250), 7.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -250), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


# Description: This is a complex polyhedron or irregular 3D geometric shape with multiple faceted surfaces, featuring a hollow or recessed interior cavity and triangulated mesh geometry, characterized by angular faces in varying shades of dark and light blue.
def model_57535_4d975687_0000():
    """Model: block guide v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.821, perimeter: 10.76
            with BuildLine():
                Line((0.85, -1.015), (0.85, 1.015))
                Line((0.85, 1.015), (-0.85, 1.015))
                Line((-0.85, 1.015), (-0.85, -1.015))
                Line((-0.85, -1.015), (0.85, -1.015))
            make_face()
            with BuildLine():
                Line((0.525, 0.33), (-0.525, 0.33))
                Line((0.525, -0.27), (0.525, 0.33))
                Line((-0.525, -0.27), (0.525, -0.27))
                Line((-0.525, 0.33), (-0.525, -0.27))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.757
        extrude(amount=0.757, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a large central hole and a rounded outer surface, featuring a mesh-like or textured finish on portions of its geometry.
def model_57535_4d975687_0004():
    """Model: Small Bushing v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4979228006, perimeter: 5.042256209
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.208
        extrude(amount=0.208, both=True)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore and a textured or knurled outer surface for grip or friction.
def model_57535_4d975687_0005():
    """Model: Large Bushing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5343849104, perimeter: 5.0893800988
            with BuildLine():
                CenterArc((0, 0), 0.51, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3965
        extrude(amount=0.3965, both=True)
    return part.part


# Description: This is a pentahedron or wedge-shaped connector block with an irregular polygonal profile, featuring a triangulated internal structure, a recessed slot or channel on one face, and multiple planar surfaces designed for assembly or mounting purposes.
def model_57616_eb493477_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 80, perimeter: 44
            with BuildLine():
                Line((10, 7), (10, 0))
                Line((2, 7), (10, 7))
                Line((2, 12), (2, 7))
                Line((0, 12), (2, 12))
                Line((0, 0), (0, 12))
                Line((10, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


# Description: This is a curved bridge or arch component with two downward-facing flanges at each end and a ribbed or striated surface pattern across its top curved section.
def model_60180_eff9787a_0003():
    """Model: Handle v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.3532812164, perimeter: 46.2025503663
            with BuildLine():
                Line((15, 1), (15.0000002235, 0.200000003))
                Line((15.0000002235, 0.200000003), (14.6000002176, 0.200000003))
                Line((14.6000002176, 0.200000003), (14.6000002176, 0))
                Line((14.6000002176, 0), (17, 0))
                Line((17, 0), (17, 0.2))
                Line((17, 0.2), (15.2, 0.2))
                Line((15.2, 0.2), (15.2, 1.2855285114))
                CenterArc((7.5, -9.4359452679), 13.2, 54.3146652873, 71.3706694253)
                Line((-0.2, 0.2), (-0.2, 1.2855285114))
                Line((-2, 0.2), (-0.2, 0.2))
                Line((-2, 0), (-2, 0.2))
                Line((0.4, 0), (-2, 0))
                Line((0.4, 0.200000003), (0.4, 0))
                Line((0, 0.200000003), (0.4, 0.200000003))
                Line((0, 1), (0, 0.200000003))
                CenterArc((7.5, -9.6183802908), 13, 54.7655820154, 70.4688359692)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a trapezoidal top surface, featuring a thin recessed edge or flange along one side and subtle surface grooves or ribs running across its face.
def model_60281_3c62566a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 149.5287425281, perimeter: 54.2892951601
            with BuildLine():
                Line((19.4612312042, -7.6834163758), (0, -7.6834163758))
                Line((19.4612312042, 0), (19.4612312042, -7.6834163758))
                Line((0, 0), (19.4612312042, 0))
                Line((0, -7.6834163758), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a mussel or clam shell with an elongated, curved oval shape featuring radial ridges or striations that fan outward from the hinge point, creating a textured surface typical of bivalve mollusks.
def model_60287_1b0a1aa8_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 68.4416165126, perimeter: 33.3090024448
            with BuildLine():
                _nurbs_edge([(-6.5, 0), (-6.5283081824, -0.2057101592), (-6.571099076, -0.6016827724), (-6.5938075271, -1.149296929), (-6.5397776272, -1.785248909), (-6.3231078798, -2.4135578272), (-5.9471398879, -2.8638769876), (-5.4043719056, -3.1278244153), (-4.6993924085, -3.2105269817), (-3.8456177916, -3.1269753161), (-2.8578823636, -2.8937443343), (-1.9708459932, -2.5989477033), (-1.2548306333, -2.3211587143), (-0.7553070823, -2.1111835542), (-0.5, -2)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-6.5, 0), (-6.4509844246, 0.1821432), (-6.3365583677, 0.5347563438), (-6.1157338793, 1.0286563316), (-5.7226796711, 1.6169671306), (-5.06821174, 2.2340450295), (-4.2570036311, 2.7308510015), (-3.3037555665, 3.1049015236), (-2.2354420865, 3.3533776336), (-1.0931678125, 3.4733871442), (0.0741614775, 3.4623780737), (1.21465825, 3.3186021257), (2.2790224174, 3.0415743498), (3.2252970094, 2.6327208583), (4.0253083342, 2.0957500083), (4.6661583268, 1.4381801755), (5.1444865755, 0.6743266031), (5.4624645551, -0.1716365114), (5.6235750733, -1.0631781759), (5.6277389028, -1.9467975327), (5.4709559563, -2.756632355), (5.1476986511, -3.4247009168), (4.6523268912, -3.8885840824), (3.9813719181, -4.1021289237), (3.134023955, -4.0378874028), (2.1109235525, -3.6811982351), (1.1529713438, -3.1576199696), (0.3566745976, -2.6308259232), (-0.2086915079, -2.2201831977), (-0.5, -2)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an elliptical dish or bowl with a gently curved surface, featuring a flat rim or flange around its perimeter and internal radial ribs or stiffening elements that extend from the center outward.
def model_60288_015aa59d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical barrel or sleeve with a curved, tapered profile featuring a light blue top flange and a darker lower cylindrical body.
def model_60293_49808d27_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a curved dark metal bracket or deflector with a distinctive bend, featuring a ribbed or corrugated texture on the upper left section and a smooth curved surface that transitions from a narrow upper arm to a wider lower flange on the right end.
def model_60516_cb7667ea_0009():
    """Model: Untitleback joint v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.201537491, perimeter: 62.8354800193
            with BuildLine():
                CenterArc((-120.9121536348, 15.487449867), 121.9, -11.0873017275, 3.7881195784)
                Line((0, 0), (-0.1147813451, 0))
                CenterArc((-0.1147813451, -0.1), 0.1, 90, 80.8543642858)
                CenterArc((-120.563858991, 19.2912272495), 121.9, -13.9145222455, 4.7688865313)
                CenterArc((6.7186049303, -11.8412681245), 9.1422778064, 168.5253969225, 74.5472423543)
                CenterArc((3.4841492748, -18.2091899893), 2, -116.9273607232, 26.9273607232)
                Line((11.9, -20.2091899893), (3.4841492748, -20.2091899893))
                CenterArc((11.9, -20.1091899893), 0.1, -90, 90)
                Line((12, -19.9323866651), (12, -20.1091899893))
                CenterArc((11.9, -19.9323866651), 0.1, 0, 90)
                Line((3.0879499405, -19.8323866651), (11.9, -19.8323866651))
                CenterArc((7.1905116383, -11.7633244946), 9.0521144932, 168.9126982725, 74.1371046853)
                Line((-1.2873796026, -7.9544663888), (-1.6926479249, -10.0225623134))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a flat rectangular bar or plate with a simple, elongated shape and rounded end corners, commonly used as a structural support, spacer, or connector component.
def model_60529_79e8313a_0012():
    """Model: Upper Support Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            with Locations((-4, 5)):
                Circle(10)
        # OneSide extrude, distance=600
        extrude(amount=600)
    return part.part


# Description: This is a cylindrical rod or shaft with a tapered conical end, featuring a smooth, uniform circular cross-section along its length.
def model_60701_72ac971f_0001():
    """Model: Untitled v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, tapered slightly at both ends, and appears to be made of a dark metallic or composite material.
def model_60707_15529a7f_0004():
    """Model: Pin-4 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # TwoSides extrude (symmetric), distance=3.5
        extrude(amount=3.5, both=True)
    return part.part


# Description: This is a long, slender hexagonal prism or column with a uniform cross-section and grooved or ribbed details running along its length, angled at approximately 45 degrees.
def model_60709_e245ebbb_0006():
    """Model: PART3 v5 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, 1), (1, 1))
                Line((-1, -1), (-1, 1))
                Line((1, -1), (-1, -1))
                Line((1, 1), (1, -1))
            make_face()
        # OneSide extrude, distance=20.5
        extrude(amount=20.5)
    return part.part


# Description: This is a cylindrical-to-rectangular transition duct or connector featuring a curved cylindrical inlet on one end that tapers into a rectangular outlet box, with a mesh or perforated surface visible on the top face.
def model_60710_e4b3ae4f_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.7977661478, perimeter: 19.6639176368
            with BuildLine():
                Line((-0.0167765184, -2.5326938681), (4.9832234816, -2.5326938681))
                Line((4.9832233641, 1.4748352723), (4.9832234816, -2.5326938681))
                _nurbs_edge([(-0.0167765184, -0.0251647776), (-0.0992764588, -0.001821837), (-0.2558852804, 0.047207031), (-0.4656253611, 0.1277790887), (-0.6948810194, 0.2492821084), (-0.8975104672, 0.4238182096), (-1.0168819703, 0.6185017418), (-1.0547616096, 0.8281375574), (-1.0144408306, 1.0440738248), (-0.9012430627, 1.2529146272), (-0.7228662811, 1.4368048763), (-0.4893874669, 1.5773160286), (-0.2133068213, 1.6585075259), (0.0903219605, 1.6705152775), (0.4039867746, 1.6125034031), (0.7071819527, 1.4970515282), (0.9792927915, 1.3471682789), (1.2037302119, 1.1906641325), (1.371653228, 1.0554401908), (1.4859308339, 0.9643501104), (1.5649622624, 0.9303520503), (1.6469688445, 0.9511431699), (1.7734852337, 1.0144697895), (1.9671746854, 1.1048579679), (2.2271319835, 1.2069058755), (2.5379050866, 1.3060620241), (2.874542654, 1.3900956754), (3.2092740034, 1.4503181617), (3.5173453907, 1.4828646162), (3.7835114008, 1.4901149206), (4.0074620879, 1.4816744635), (4.1980799304, 1.4699960492), (4.3682954489, 1.4661992783), (4.5300799482, 1.4761731547), (4.6885872818, 1.4956942021), (4.8136429024, 1.5064608319), (4.9000112733, 1.5008439898), (4.9531907402, 1.4870200694), (4.9797636873, 1.4763023889), (4.9832233641, 1.4748352723)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.8537833309, 0.8537833309, 0.8537833309, 0.8537833309, 0.8537833309, 0.8537833309], 5)
                Line((-0.0167765184, -0.0251647776), (-0.0167765184, -2.5326938681))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cast or forged mounting bracket or connector with an angular, trapezoidal body featuring a large flat mounting surface, a perpendicular cylindrical boss or hub on one end, and appears designed for mechanical assembly or structural support applications.
def model_60710_e4b3ae4f_0003():
    """Model: hand v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 47.0269864644, perimeter: 30.6669310698
            with BuildLine():
                Line((5, -5), (5, 0))
                _nurbs_edge([(0, -5), (-0.0475555289, -5.0073273199), (-0.141753137, -5.0156077867), (-0.2803093271, -5.008905604), (-0.4595677767, -4.9617156828), (-0.6742139367, -4.8398551345), (-0.8785631781, -4.6579410331), (-1.0709231305, -4.4215946006), (-1.2484002033, -4.1404986125), (-1.4069608915, -3.8284038484), (-1.542310166, -3.5008202142), (-1.650579551, -3.1732345565), (-1.7291127406, -2.859088788), (-1.7771631138, -2.5679256316), (-1.7967445105, -2.3032992763), (-1.7931030526, -2.0612319578), (-1.7720006253, -1.8336884869), (-1.7369826083, -1.6118320887), (-1.6871816956, -1.3890127176), (-1.6136109793, -1.1647094711), (-1.5009400144, -0.9448713493), (-1.335027893, -0.7383228297), (-1.1094209609, -0.5540772575), (-0.8312304762, -0.3985733784), (-0.5299082723, -0.2722139783), (-0.2521803557, -0.1697115832), (-0.0488782833, -0.0827111669), (0.0357671045, -0.0017122874), (-0.0242160679, 0.0817319227), (-0.2250742429, 0.1729034794), (-0.5407217219, 0.2746561291), (-0.9304057809, 0.3882014263), (-1.346300344, 0.5138878577), (-1.7409948759, 0.6519476365), (-2.0753183057, 0.8033372135), (-2.3251803018, 0.9703101378), (-2.4788045072, 1.154654679), (-2.5347600603, 1.3560074693), (-2.4996927799, 1.5703652413), (-2.3862170979, 1.7879657653), (-2.2106846778, 1.9932247417), (-1.9909412434, 2.1688306224), (-1.7439537715, 2.2991479497), (-1.4837645473, 2.3735102928), (-1.2186345557, 2.3905089647), (-0.9511356502, 2.3581737877), (-0.6811653184, 2.2899261959), (-0.4083053362, 2.2015845756), (-0.1341545651, 2.1081567473), (0.1346279186, 2.0202158048), (0.3857950189, 1.9420754518), (0.6072057034, 1.8747142265), (0.791820273, 1.8179683529), (0.9419519251, 1.7726327341), (1.0764015815, 1.7435483962), (1.2229928105, 1.7373225559), (1.4059923595, 1.7581668253), (1.6325336614, 1.8033160643), (1.894042406, 1.8642677074), (2.1740547915, 1.9304643182), (2.4540998371, 1.9922844129), (2.7199565446, 2.0440529846), (2.9688729891, 2.0877496622), (3.2069018067, 2.1304854246), (3.4440978543, 2.1806642918), (3.6904223466, 2.2445631583), (3.951449776, 2.3228266079), (4.2238896669, 2.4067435713), (4.4978232041, 2.4808147562), (4.7593047283, 2.5256491647), (4.9928515663, 2.5207670999), (5.183913394, 2.4473655159), (5.3215253028, 2.2913022627), (5.397953747, 2.0426080317), (5.4080842158, 1.6947019011), (5.3489058187, 1.2437186151), (5.2449475846, 0.7989779226), (5.1349326577, 0.417946512), (5.0473506682, 0.1428312261), (5, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0133333333, 0.0266666667, 0.04, 0.0533333333, 0.0666666667, 0.08, 0.0933333333, 0.1066666667, 0.12, 0.1333333333, 0.1466666667, 0.16, 0.1733333333, 0.1866666667, 0.2, 0.2133333333, 0.2266666667, 0.24, 0.2533333333, 0.2666666667, 0.28, 0.2933333333, 0.3066666667, 0.32, 0.3333333333, 0.3466666667, 0.36, 0.3733333333, 0.3866666667, 0.4, 0.4133333333, 0.4266666667, 0.44, 0.4533333333, 0.4666666667, 0.48, 0.4933333333, 0.5066666667, 0.52, 0.5333333333, 0.5466666667, 0.56, 0.5733333333, 0.5866666667, 0.6, 0.6133333333, 0.6266666667, 0.64, 0.6533333333, 0.6666666667, 0.68, 0.6933333333, 0.7066666667, 0.72, 0.7333333333, 0.7466666667, 0.76, 0.7733333333, 0.7866666667, 0.8, 0.8133333333, 0.8266666667, 0.84, 0.8533333333, 0.8666666667, 0.88, 0.8933333333, 0.9066666667, 0.92, 0.9333333333, 0.9466666667, 0.96, 0.9733333333, 0.9866666667, 1, 1, 1, 1, 1, 1], 5)
                Line((0, -5), (5, -5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a simple cylindrical shape, featuring rounded ends and a uniform cross-section throughout its length.
def model_60716_dcd9370c_0006():
    """Model: motor shaft v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: A cylindrical metal pin with a long shaft and two circular flanged heads at each end, featuring a hole through each flange for securing fasteners or linkages.
def model_60719_76b5da02_0000():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.7981134891, perimeter: 29.1608782907
            with BuildLine():
                CenterArc((0, 0), 1.25, -5.3191147458, 64.0063042852)
                Line((1.2446172832, -0.1158784641), (14.4045971968, 0.9009115132))
                CenterArc((15, 2), 1.25, 176.3162520576, 65.2382718694)
                Line((0.6496376785, 1.0679283153), (13.7525826465, 2.0803115562))
            make_face()
            # Profile area: 3.1415926536, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((15, 2), 1.25, 176.3162520576, 65.2382718694)
                CenterArc((15, 2), 1.25, -118.445476073, 294.7617281306)
            make_face()
            with BuildLine():
                CenterArc((15, 2), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((0, 0), 1.25, 58.6871895394, 295.9936957148)
                CenterArc((0, 0), 1.25, -5.3191147458, 64.0063042852)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical tube or sleeve with a curved dome-shaped top end and a flat circular base, featuring a mesh or lattice pattern across its surface.
def model_60719_76b5da02_0002():
    """Model: Untitled v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a rectangular box or tray with a sloped or angled top surface that features internal triangular ribbing or bracing for structural reinforcement.
def model_60720_ef9a0a95_0002():
    """Model: FOOD TABLE v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((-2, -0.5), (2, -0.5))
                Line((2, -0.5), (2, 0.5))
                Line((-2, 0.5), (2, 0.5))
                Line((-2, -0.5), (-2, 0.5))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


# Description: This is a hexagonal prism or bar stock with a twisted or helical surface feature running along its length, creating a dark band or groove that spirals from one end to the other.
def model_60720_ef9a0a95_0004():
    """Model: SITING ARRANGEMENT v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((0, 1), (0, -0.5))
                Line((-1.5, 1), (0, 1))
                Line((-1.5, -0.5), (-1.5, 1))
                Line((0, -0.5), (-1.5, -0.5))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


# Description: This is a cylindrical mesh or perforated filter element with an open top and solid dark blue base, featuring a fine grid or mesh pattern on the upper curved surface.
def model_60720_ef9a0a95_0009():
    """Model: Untitled v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a long, narrow rectangular extrusion or beam with a flat top surface, angled end caps on both sides, and what appears to be a central slot or groove running along its length.
def model_60723_c8e7621d_0004():
    """Model: leg 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((0, 1.5), (0, 0))
                Line((0, 0), (1.5, 0))
                Line((1.5, 0), (1.5, 1.5))
                Line((1.5, 1.5), (0, 1.5))
            make_face()
        # TwoSides extrude (symmetric), distance=17.5
        extrude(amount=17.5, both=True)
    return part.part


# Description: This is a cylindrical pipe or tube with a slightly tapered or rounded end, featuring a smooth, uniform wall thickness and a hollow interior.
def model_60726_c2bd4537_0004():
    """Model: Untitled v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rectangular hollow tube or channel with a uniform cross-section, featuring a long, slender prismatic shape with a dark metallic finish and subtle edge details along its length.
def model_60728_99f07543_0005():
    """Model: F2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9, perimeter: 17.4
            with BuildLine():
                Line((-0.3, -2.5), (-1.5, -2.5))
                Line((-0.3, 5), (-0.3, -2.5))
                Line((-1.5, 5), (-0.3, 5))
                Line((-1.5, -2.5), (-1.5, 5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical shaft or rod with rounded ends featuring two hemispherical end caps and a central rectangular slot or keyway running along its length.
def model_60728_99f07543_0006():
    """Model: F4 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is an elongated wedge or tapered rectangular prism with a sloped top surface, featuring a flat base and angled sides that narrow toward one end.
def model_60729_c51868ec_0001():
    """Model: BED v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 86400, perimeter: 1320
            with BuildLine():
                Line((0, 480), (0, 0))
                Line((0, 0), (180, 0))
                Line((180, 0), (180, 480))
                Line((180, 480), (0, 480))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a curved, hollow rectangular duct or air passage component with a trapezoidal profile, featuring a mesh-filled interior cavity and a tapered shape that transitions from a wider top surface to a narrower bottom edge.
def model_60730_fa513b8a_0003():
    """Model: seat prt v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.625836495, perimeter: 11.9020871499
            with BuildLine():
                _nurbs_edge([(4, -2.5), (3.9896613421, -2.4951352698), (3.9621637323, -2.4865746181), (3.9004563629, -2.4772400458), (3.7770915825, -2.4718355535), (3.5544825715, -2.4771419647), (3.2654526721, -2.4951982036), (2.9153240549, -2.5271494901), (2.5144207057, -2.5747073794), (2.0768086289, -2.6398506604), (1.6189674199, -2.7244954312), (1.158581707, -2.8301620785), (0.7133231917, -2.9576096131), (0.2996830393, -3.1064677844), (-0.0683156607, -3.27478662), (-0.3802493599, -3.4586700292), (-0.6310115195, -3.6515807384), (-0.8209285346, -3.8445759804), (-0.9535924929, -4.0278393538), (-1.034309814, -4.1919533632), (-1.0685162623, -4.3291236769), (-1.0617023836, -4.4137080491), (-1.0380338517, -4.4625241928), (-1.0140462737, -4.4885878275), (-1, -4.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1, -4.5), (-0.9710362217, -4.5106122161), (-0.9141894298, -4.5291346327), (-0.8321615588, -4.548812181), (-0.7292841317, -4.5588154474), (-0.611002845, -4.5448398513), (-0.501425141, -4.5063383944), (-0.3972611295, -4.4473837612), (-0.2929320044, -4.3749592216), (-0.1820551316, -4.2974252904), (-0.059071072, -4.2228629308), (0.0793643083, -4.1576090161), (0.2324171243, -4.1043427136), (0.3959159723, -4.0623779996), (0.5642833162, -4.0288344547), (0.7321862805, -3.9995360283), (0.8961184482, -3.969956251), (1.0564694087, -3.9362789693), (1.2176490675, -3.895868923), (1.3860890176, -3.8470882286), (1.5688525904, -3.7892914066), (1.771940672, -3.7227612441), (1.9988645886, -3.6486594906), (2.2487290375, -3.5690205711), (2.516557906, -3.4864856768), (2.7945114713, -3.403925694), (3.0727936478, -3.3241052156), (3.3406835049, -3.2493232275), (3.5874849248, -3.1810759749), (3.8035599431, -3.1196722665), (3.9812174962, -3.0639409371), (4.1159670295, -3.0106918269), (4.206246934, -2.955226867), (4.2522274207, -2.8925126978), (4.2549500007, -2.8180882947), (4.2152404882, -2.7292354371), (4.1499454358, -2.6455877), (4.0822463526, -2.575607065), (4.0288008944, -2.525738224), (4, -2.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5)
    return part.part


# Description: This is a curved duct or elbow pipe component with a rectangular cross-section, featuring a 90-degree bend, a cylindrical inlet port on the left, and a complex internal mesh structure visible through the blue highlighted surface area.
def model_60730_fa513b8a_0004():
    """Model: footrest prt v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.081627078, perimeter: 10.6673058358
            with BuildLine():
                _nurbs_edge([(-4.9500000738, -7.6000001132), (-4.9397563181, -7.6244917654), (-4.9166206186, -7.6649971246), (-4.8739716475, -7.7003140375), (-4.8011074539, -7.6962144165), (-4.6830175232, -7.6073925311), (-4.5382661858, -7.4450137562), (-4.3679418033, -7.2276606218), (-4.1734970147, -6.978440231), (-3.9565914895, -6.7226001837), (-3.7189418656, -6.4846049671), (-3.4622436617, -6.2857918766), (-3.1881603756, -6.1409332005), (-2.8982558168, -6.0580681446), (-2.5938760156, -6.0408998358), (-2.2760919274, -6.0901394072), (-2.0117473981, -6.1819923846), (-1.8079948616, -6.2798227304), (-1.6697356668, -6.3578126883), (-1.6000000238, -6.4000000954)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.0000000149, -6.1000000909), (-0.9987956789, -6.1330430565), (-0.9975388923, -6.1967698841), (-0.9991092566, -6.2852830438), (-1.0082288335, -6.3889115802), (-1.0321336842, -6.492835774), (-1.069665708, -6.5688510169), (-1.1219435797, -6.6146662215), (-1.1895899847, -6.6290061056), (-1.2720117703, -6.6130854674), (-1.3681002533, -6.5691749309), (-1.4550105611, -6.5134851932), (-1.5254820736, -6.4608862709), (-1.5747753225, -6.4210847689), (-1.6000000238, -6.4000000954)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-4.9500000738, -7.6000001132), (-4.979766299, -7.5937625645), (-5.0322564843, -7.5743518229), (-5.0898622788, -7.524421678), (-5.124127182, -7.4159790357), (-5.0954215374, -7.2126593902), (-4.9970276931, -6.9521342489), (-4.8338184377, -6.654423578), (-4.6121954486, -6.3444176433), (-4.339376201, -6.0490081891), (-4.0226012919, -5.7936454319), (-3.6685764242, -5.5991692009), (-3.2829542003, -5.4781217323), (-2.8702947999, -5.4368396942), (-2.4340878243, -5.4774360514), (-1.9768163834, -5.5994213622), (-1.5954102782, -5.7607624447), (-1.3009502618, -5.9168407211), (-1.1009348843, -6.0363678037), (-1.0000000149, -6.1000000909)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flexible curved pipe or conduit with two perpendicular bends, featuring a smooth serpentine shape that transitions from a vertical orientation at the top to a horizontal orientation at the bottom, with both ends appearing to be open terminals.
def model_60730_fa513b8a_0006():
    """Model: base prt v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.3268385287, perimeter: 36.1091891731
            with BuildLine():
                _nurbs_edge([(-4.5581268229, -7.6946596368), (-4.5193428361, -7.6436672197), (-4.4433135852, -7.5433869637), (-4.33388563, -7.3980804172), (-4.1972187481, -7.2145685286), (-4.0411261308, -7.0025257048), (-3.8978207254, -6.8086696202), (-3.7632996499, -6.6346842706), (-3.631016464, -6.4832922679), (-3.4907568335, -6.3587130208), (-3.3299478659, -6.26610084), (-3.1373505525, -6.2099847894), (-2.9057505143, -6.1931270062), (-2.635835367, -6.214886189), (-2.3367749288, -6.270953685), (-2.0225987821, -6.3548396845), (-1.7096410558, -6.4589133344), (-1.4135081571, -6.5756446698), (-1.1463646317, -6.6987056243), (-0.9138068796, -6.824261692), (-0.712713541, -6.9518017553), (-0.5342703466, -7.0825374188), (-0.3663982938, -7.2180656396), (-0.1963361629, -7.3589967076), (-0.0133208148, -7.5034410535), (0.1892709309, -7.6460218484), (0.4145337744, -7.7795162529), (0.6622771657, -7.8961122952), (0.9293809008, -7.9888654441), (1.2101590477, -8.0529525323), (1.4965600774, -8.0873206297), (1.7794602268, -8.0941460965), (2.0502786676, -8.077639244), (2.3025241676, -8.0430558827), (2.5332854429, -7.9956564453), (2.7449570157, -7.9396124407), (2.9462740787, -7.8771535774), (3.1485611855, -7.8094926317), (3.3622530251, -7.73763838), (3.5937357754, -7.6631114823), (3.8410301097, -7.589036144), (4.0936251847, -7.5198748958), (4.337927744, -7.4593690991), (4.5615349581, -7.4087943069), (4.7575278319, -7.365358162), (4.9298507896, -7.3198802803), (5.0946809319, -7.2569007853), (5.2722235521, -7.1604906739), (5.4803645646, -7.0189781106), (5.7277227389, -6.8299911583), (6.0065687674, -6.6057007893), (6.2980583354, -6.3673444535), (6.5781148132, -6.139166705), (6.8229009667, -5.9427888265), (7.0148242963, -5.7909281509), (7.1474783793, -5.6824741022), (7.2331141617, -5.5943020988), (7.3016192219, -5.484067379), (7.3874202449, -5.3086430033), (7.5194272014, -5.038594147), (7.7095071672, -4.6746508235), (7.9557059544, -4.2403932795), (8.24554072, -3.7747333966), (8.5592479128, -3.324536829), (8.8730740843, -2.9370676384), (9.1624560808, -2.6528220225), (9.4054435258, -2.4974697654), (9.5855589054, -2.4758371397), (9.6960316559, -2.5608933681), (9.7394281329, -2.6993715679), (9.7215833373, -2.8371127314), (9.6612176556, -2.9224297483), (9.5904941578, -2.9682991017), (9.5320479624, -2.9907808344), (9.5, -3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(9.5, -3), (9.4368410871, -3.0695832516), (9.3138354519, -3.206480535), (9.139263542, -3.4050188113), (8.9263809316, -3.6561165984), (8.693131708, -3.9473932341), (8.4918370328, -4.2164308026), (8.3206391155, -4.4639799201), (8.1764119719, -4.6913166114), (8.0543828265, -4.9003995909), (7.9479085046, -5.0939693263), (7.8478679196, -5.2757917472), (7.7434113102, -5.4503906628), (7.6241176739, -5.6222450827), (7.481905349, -5.7950871017), (7.3127751409, -5.9712466301), (7.1192994731, -6.1507554404), (6.9098715131, -6.3315087177), (6.6954556888, -6.5102397851), (6.4871450872, -6.6832378282), (6.2932273521, -6.8472095294), (6.1168307009, -6.9999888673), (5.9523822867, -7.141539945), (5.7867652667, -7.2738152059), (5.6035916217, -7.3998525018), (5.3866230301, -7.5230876482), (5.1233723211, -7.6466048907), (4.809035202, -7.7723522361), (4.4490552975, -7.900559069), (4.0558784359, -8.0300463739), (3.6465821548, -8.1583991988), (3.2401861347, -8.2821934239), (2.8550665762, -8.3971929789), (2.5064098069, -8.4985698558), (2.2034508126, -8.5810871658), (1.9472535466, -8.6393591238), (1.7270765237, -8.6679207841), (1.5243537942, -8.6622891975), (1.3191428025, -8.6202812178), (1.0961959298, -8.54342038), (0.8502140157, -8.4379302177), (0.5939077716, -8.3168625144), (0.3534259722, -8.1973249427), (0.1566911615, -8.0950822821), (0.022997919, -8.0194335429), (-0.0459178385, -7.9691269859), (-0.0804802305, -7.924905145), (-0.1320261988, -7.8572284183), (-0.2346037423, -7.7504164588), (-0.4014264681, -7.6039923059), (-0.6311529884, -7.4272246337), (-0.9112919286, -7.2356741046), (-1.2227364755, -7.0469789768), (-1.5438825084, -6.8768450711), (-1.854692319, -6.7353098651), (-2.1378266669, -6.6275407608), (-2.3800251112, -6.5542965217), (-2.5734116042, -6.5124459951), (-2.7168017302, -6.4956060624), (-2.8171072868, -6.4943727559), (-2.8904644719, -6.4976257273), (-2.9578319382, -6.5051115524), (-3.0406903638, -6.5426688745), (-3.1563150409, -6.6447945479), (-3.311521912, -6.8260194016), (-3.5017925407, -7.0741498837), (-3.7151765602, -7.3603486023), (-3.9348465047, -7.6446123737), (-4.1422122612, -7.8831465977), (-4.3197560772, -8.034835743), (-4.4540731154, -8.0683016282), (-4.5216842092, -7.9881874243), (-4.5489988696, -7.865685727), (-4.5568162842, -7.7562898071), (-4.5581268229, -7.6946596368)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a plastic or composite channel/tray component with a long, shallow rectangular body, an upturned flange on the right end, and a slightly curved or tapered left end, designed for guiding, directing, or protecting cables or components.
def model_60739_f118b838_0001():
    """Model: prt3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.3532203464, perimeter: 30.8253527088
            with BuildLine():
                Line((-11.0559240626, 2.7189599705), (-11.0559240626, 2.1947893798))
                Line((-11.0559240626, 2.1947893798), (0.2492763937, 1.3298978004))
                CenterArc((0.5162597707, 4.8197000693), 3.5, -94.3748270572, 34.443409879)
                Line((3.4201902757, 2.456673288), (2.2698867176, 1.7907080702))
                Line((2.6501661975, 3.7867148775), (3.4201902757, 2.456673288))
                Line((0.8058622674, 2.7189599705), (2.6501661975, 3.7867148775))
                Line((-11.0559240626, 2.7189599705), (0.8058622674, 2.7189599705))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a bicycle seat or saddle featuring an ergonomic curved design with a mesh or perforated ventilation panel on top and a solid structural base, designed for comfort and airflow during cycling.
def model_60739_f118b838_0002():
    """Model: PRT6 v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.9533048533, perimeter: 10.8556762952
            with BuildLine():
                Line((-2.5, 0), (1.5, 0))
                _nurbs_edge([(-2.5, 0), (-2.541188196, 0.0110495606), (-2.617982017, 0.035994811), (-2.7164249455, 0.0819497969), (-2.8141267071, 0.1603393575), (-2.8799962847, 0.2852506703), (-2.889242884, 0.4321620144), (-2.8415786186, 0.5905779531), (-2.7370436811, 0.7439015725), (-2.5766129212, 0.8738833432), (-2.362795186, 0.9643617382), (-2.1001747626, 1.0049186975), (-1.796213348, 0.9955614282), (-1.4607713784, 0.9456137412), (-1.1051190447, 0.8702543131), (-0.741136653, 0.7878930164), (-0.3804362014, 0.7171982085), (-0.0335458324, 0.6743703021), (0.2910006923, 0.670098269), (0.5874052957, 0.7070733623), (0.8538060755, 0.7760375078), (1.0915886292, 0.8578970605), (1.3035749187, 0.9294448856), (1.4925721932, 0.9679445632), (1.6597827048, 0.9561756353), (1.8032675687, 0.8873273355), (1.91638062, 0.7700018411), (1.9899905716, 0.6219503242), (2.0145504342, 0.4642471923), (1.9824439273, 0.3147898214), (1.8895760526, 0.1837420588), (1.7652064393, 0.0977156492), (1.6436008413, 0.0444764446), (1.5499616955, 0.0139910272), (1.5, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a circular ring or bearing component with a uniform toroidal shape, featuring a textured or knurled outer surface and an open hollow center, commonly used as a spacer, bearing race, or structural ring in mechanical assemblies.
def model_60739_f118b838_0003():
    """Model: prt1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.0418294554, perimeter: 51.8080361126
            with BuildLine():
                CenterArc((0, 0), 4.4130902854, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8324147538, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a curved sheet metal or composite panel with a wavy, saddle-like shape featuring smooth longitudinal curves and flanged edges along the top and bottom perimeters.
def model_60753_80b955c8_0000():
    """Model: ch2 v1 v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5050114009, perimeter: 13.0558307687
            with BuildLine():
                _nurbs_edge([(-1.5, 4), (-1.4452000927, 3.9464765803), (-1.3402101699, 3.8395009145), (-1.1965548335, 3.6792508972), (-1.0327874638, 3.4660132577), (-0.8744402227, 3.2000074375), (-0.7615228855, 2.9340073574), (-0.6912076374, 2.6669104483), (-0.6579281449, 2.3968751956), (-0.6521975292, 2.1210367339), (-0.6620402293, 1.8362493864), (-0.6747633912, 1.5399862276), (-0.6785432249, 1.2311785601), (-0.6641485228, 0.9111582022), (-0.6264767885, 0.5844776719), (-0.5634757914, 0.2577206888), (-0.4752944177, -0.0615093186), (-0.3633961255, -0.3656841867), (-0.2297848501, -0.6483209197), (-0.0761169535, -0.9052667647), (0.0964492233, -1.1344356258), (0.2490108233, -1.2949272575), (0.3714140944, -1.4024423255), (0.456549201, -1.4684290839), (0.5, -1.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0.5, -1.5), (0.9245781785, -1.4150843643))
                _nurbs_edge([(-1.0754218215, 4.0849156357), (-1.0206219143, 4.031392216), (-0.9156319915, 3.9244165502), (-0.7719766551, 3.7641665328), (-0.6082092853, 3.5509288934), (-0.4498620442, 3.2849230731), (-0.336944707, 3.0189229931), (-0.266629459, 2.7518260839), (-0.2333499664, 2.4817908313), (-0.2276193507, 2.2059523695), (-0.2374620508, 1.9211650221), (-0.2501852128, 1.6249018633), (-0.2539650464, 1.3160941958), (-0.2395703444, 0.9960738379), (-0.2018986101, 0.6693933076), (-0.1388976129, 0.3426363245), (-0.0507162393, 0.0234063171), (0.061182053, -0.280768551), (0.1947933284, -0.563405284), (0.3484612249, -0.8203511291), (0.5210274017, -1.0495199901), (0.6735890017, -1.2100116218), (0.7959922729, -1.3175266898), (0.8811273794, -1.3835134482), (0.9245781785, -1.4150843643)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.5, 4), (-1.0754218215, 4.0849156357))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)
    return part.part


# Description: This is a flat, trapezoidal panel or cover plate with a slightly curved top edge and reinforced borders, featuring a dark blue finish and appearing to be a structural component or protective shield for an industrial or mechanical assembly.
def model_60753_80b955c8_0001():
    """Model: ch3 v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6594846338, perimeter: 24.1976061707
            with BuildLine():
                Line((-5.314683995, 0.4799923326), (-5.3775844659, -0.101837023))
                _nurbs_edge([(-5.3775844659, -0.101837023), (-5.2961902218, -0.1209215823), (-5.1316919932, -0.1583503023), (-4.8798154309, -0.2122721921), (-4.5336947936, -0.2797140326), (-4.0837764255, -0.3565246714), (-3.6164870639, -0.4257562785), (-3.131831011, -0.4873263521), (-2.6300141636, -0.5411803157), (-2.1115402103, -0.5873256145), (-1.5773449426, -0.6258208171), (-1.0289543527, -0.6567515497), (-0.468638459, -0.6802147843), (0.1003989903, -0.6963024086), (0.6738766366, -0.7050905056), (1.2461417487, -0.7066245177), (1.8104056258, -0.7009300491), (2.3594287485, -0.6880460758), (2.8860614222, -0.6680534599), (3.3838780818, -0.6411120076), (3.8477193029, -0.6074909522), (4.2744626899, -0.5676235229), (4.6631362267, -0.5220947473), (5.0141037531, -0.4715337609), (5.3285071319, -0.416532592), (5.6076293229, -0.3575558549), (5.8033808318, -0.3073967037), (5.9349077981, -0.2681489516), (6.0158160732, -0.241261935), (6.0545761169, -0.2276379648)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((6.1174765878, 0.3541913909), (6.0545761169, -0.2276379648))
                _nurbs_edge([(-5.314683995, 0.4799923326), (-5.233289751, 0.4609077734), (-5.0687915223, 0.4234790533), (-4.81691496, 0.3695571636), (-4.4707943227, 0.3021153231), (-4.0208759546, 0.2253046842), (-3.553586593, 0.1560730771), (-3.0689305401, 0.0945030035), (-2.5671136927, 0.0406490399), (-2.0486397394, -0.0054962589), (-1.5144444717, -0.0439914614), (-0.9660538818, -0.074922194), (-0.4057379881, -0.0983854287), (0.1632994612, -0.114473053), (0.7367771075, -0.1232611499), (1.3090422196, -0.1247951621), (1.8733060967, -0.1191006934), (2.4223292194, -0.1062167202), (2.948961893, -0.0862241043), (3.4467785526, -0.059282652), (3.9106197738, -0.0256615965), (4.3373631608, 0.0142058327), (4.7260366976, 0.0597346084), (5.077004224, 0.1102955947), (5.3914076028, 0.1652967637), (5.6705297938, 0.2242735007), (5.8662813027, 0.274432652), (5.997808269, 0.313680404), (6.0787165441, 0.3405674206), (6.1174765878, 0.3541913909)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a smooth, tapered body featuring a slightly larger diameter at one end and subtle surface texture or perforations along its length.
def model_60759_23829707_0006():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # Symmetric extrude, each_side=12
        extrude(amount=12, both=True)
    return part.part


# Description: This is a long, horizontally-oriented duct or channel component with a trapezoidal cross-section, featuring a sloped top surface with ventilation slots or louvers, a recessed central cavity, and flanged end sections for mounting or connection.
def model_60760_f95d00ad_0019():
    """Model: ppp v1"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.188580891, perimeter: 25.830902325
            with BuildLine():
                Line((-7.511397421, 4.8219332481), (-7.511397421, 3.0317512702))
                _nurbs_edge([(-7.511397421, 3.0317512702), (-7.4732895643, 2.9361449848), (-7.3951721792, 2.750861897), (-7.2722913871, 2.490724776), (-7.0968505916, 2.1800436978), (-6.8568784391, 1.8561457863), (-6.6379341317, 1.6448809397), (-6.4591448679, 1.5228391739), (-6.330750373, 1.4580926467), (-6.2597972904, 1.4286696626), (-6.2495052582, 1.4245312715)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.5168958017, 0.5168958017, 0.5168958017, 0.5168958017, 0.5168958017, 0.5168958017], 5)
                _nurbs_edge([(0.5, 2.0069430389), (0.4770344825, 2.1058037631), (0.4237407068, 2.2912840251), (0.3217124398, 2.5327819163), (0.1411729852, 2.7807909028), (-0.1593850572, 2.9664191793), (-0.5336429836, 3.0299843699), (-0.976263807, 2.9810789975), (-1.4758561929, 2.8398311254), (-2.0174989188, 2.6325175324), (-2.5845525919, 2.3883962224), (-3.1605903364, 2.1363110138), (-3.7310019761, 1.9018572227), (-4.2851140852, 1.7035970987), (-4.8168319323, 1.5519316157), (-5.3230551364, 1.4519864007), (-5.706830807, 1.4145994195), (-5.9827619765, 1.410372617), (-6.1614658934, 1.4180606771), (-6.2495052582, 1.4245312715)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((0.5, 1.6379251025), (0.5, 2.0069430389))
                Line((1.7968479078, 1.6379251025), (0.5, 1.6379251025))
                Line((1.7968479078, 2.0069430389), (1.7968479078, 1.6379251025))
                Line((1.7877771323, 2.0069430389), (1.7968479078, 2.0069430389))
                _nurbs_edge([(-6.5, 4.8219332481), (-6.5403581318, 4.7075677995), (-6.6077673314, 4.4850699145), (-6.6689592634, 4.1700215952), (-6.670384775, 3.7875113172), (-6.53861847, 3.3738400211), (-6.2769773163, 3.0287849568), (-5.8953013406, 2.7593032902), (-5.4131958054, 2.5762434374), (-4.8570126545, 2.4910110544), (-4.255746565, 2.5114274869), (-3.6373662711, 2.6375678459), (-3.0252209303, 2.8577432633), (-2.4338614256, 3.143167097), (-1.8703865061, 3.4526440738), (-1.3365602385, 3.7385783086), (-0.8305659176, 3.9525208336), (-0.3487375149, 4.0504950515), (0.1125967935, 3.9994545621), (0.5559297217, 3.7805064583), (0.9829578415, 3.3842033495), (1.3123155169, 2.9230174177), (1.5526393928, 2.4962883091), (1.7098917928, 2.1760216429), (1.7877771323, 2.0069430389)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-7.511397421, 4.8219332481), (-6.5, 4.8219332481))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20)
    return part.part


# Description: This is a double-loop connector or coupling device featuring two circular loops connected by a central rectangular bridge, with each loop containing a central hole for fastening or assembly purposes.
def model_60760_f95d00ad_0023():
    """Model: bbb v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1117977297, perimeter: 11.6839868235
            with BuildLine():
                CenterArc((-12.5, 5), 1.0249378106, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-12.5, 5), 0.8346264474, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.0876861534, perimeter: 48.6944593597
            with BuildLine():
                CenterArc((-12, 0), 4, 0, 95.7105931365)
                CenterArc((-12, 0), 4, 95.7105931365, 264.2894068635)
            make_face()
            with BuildLine():
                CenterArc((-12, 0), 3.7499639083, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3561944902, perimeter: 23.8935440135
            with BuildLine():
                CenterArc((-6, 0), 2, 0, 180)
                CenterArc((-6, 0), 2, -180, 180)
            make_face()
            with BuildLine():
                CenterArc((-6, 0), 1.8027756377, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 10.4956634443, perimeter: 47.4881049025
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5579666333, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a neti pot or nasal irrigation spout, characterized by a curved, elongated body with a tapered tail, a bulbous handle with a thumb hole on the right end, and a smooth, organic shape designed for pouring saline solution into the nasal passages.
def model_60760_f95d00ad_0024():
    """Model: part v1 (15)"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 120.2258410507, perimeter: 86.9651763494
            with BuildLine():
                CenterArc((-2, 25.5), 30.5655034312, -105.1729153455, 18.9246444161)
                CenterArc((0, 0), 5, -90, 242.6428991491)
                CenterArc((-9.5, 6.6643092637), 6.6830395751, -94.2906648897, 53.4929423415)
                _nurbs_edge([(-10, 0), (-10.341578697, 0.0143628286), (-11.0179407411, 0.0384420046), (-12.0120978791, 0.0606214031), (-13.2965714893, 0.0621118826), (-14.8314174708, 0.0158832441), (-16.2917334158, -0.0801701686), (-17.6724590271, -0.2277835313), (-18.9676279462, -0.4281215874), (-20.1709082322, -0.6810828379), (-21.2763644783, -0.9844071423), (-22.2794050427, -1.3327131887), (-23.1764016508, -1.7189299444), (-23.9646921375, -2.1355216419), (-24.6427205894, -2.575567128), (-25.2107776171, -3.0339459519), (-25.5790576505, -3.4131456685), (-25.8078378939, -3.7040573542), (-25.9394335133, -3.9008733646), (-26, -4)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-10, -4), (-10.3982620501, -3.8525935166), (-11.1883104003, -3.5699776175), (-12.3539568932, -3.1826426791), (-13.8686504639, -2.7405976022), (-15.6913906298, -2.3210667498), (-17.4361368682, -2.0484373724), (-19.0946007832, -1.9383206541), (-20.6595110031, -2.0044122154), (-22.1292425231, -2.2497727513), (-23.5086306678, -2.6652949329), (-24.5446805913, -3.1247746282), (-25.2860058696, -3.5366482208), (-25.7646048318, -3.8406468943), (-26, -4)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a polyhedron or irregular hexahedron featuring a combination of flat polygonal faces in dark and light blue tones, with multiple planar surfaces meeting at various angles and edges, suggesting a geometric solid used potentially for structural, mechanical, or design purposes.
def model_60787_6f3aa359_0013():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((-5, 5), (5, 5))
                Line((-5, -5), (-5, 5))
                Line((5, -5), (-5, -5))
                Line((5, 5), (5, -5))
            make_face()
        # Symmetric extrude, each_side=4.975
        extrude(amount=4.975, both=True)
    return part.part


# Description: This is a simple cylindrical rod or shaft with rounded ends, featuring a straight, elongated design without any holes, slots, or flanges.
def model_60787_6f3aa359_0015():
    """Model: solar_rot v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((0, 0), 0.1, -90, 90)
                CenterArc((0, 0), 0.1, 0, 270)
            make_face()
            # Profile area: 0.0021460184, perimeter: 0.3570796327
            with BuildLine():
                Line((0, -0.1), (0.1, -0.1))
                Line((0.1, -0.1), (0.1, 0))
                CenterArc((0, 0), 0.1, -90, 90)
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a simple cylindrical rod with a uniform circular cross-section, featuring a slightly tapered or rounded end at the top and a clean, straight body.
def model_60787_6f3aa359_0026():
    """Model: axe v1 (2) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a cylindrical tube or rod with rounded ends, featuring a uniform diameter throughout its length and a slight diagonal orientation.
def model_60865_19bbdeb4_0017():
    """Model: 1-Pillar v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.780972451, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a curved reinforcement rib or stiffener with a hollow lattice structure in the center, featuring a dark outer rim and a blue mesh-patterned interior panel, designed to provide structural support while minimizing weight.
def model_60865_19bbdeb4_0018():
    """Model: 1-Pillar Part v1 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 186.3859278833, perimeter: 105.3932475259
            with BuildLine():
                CenterArc((11.5000118335, -38.0246759436), 37.8781607088, 68.3198034872, 0.3038710927)
                CenterArc((26.5, 0), 3, -109.609558274, 169.6654975906)
                CenterArc((11.5000118335, -38.0246759436), 43.8462400088, 67.8979809839, 44.2041511671)
                CenterArc((-3.5, 0), 3, 119.9453070621, 169.66888501)
                CenterArc((11.5000118335, -38.0246759436), 37.8781607088, 68.6236745799, 43.0561884355)
            make_face()
            with BuildLine():
                CenterArc((-3.5, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((26.5, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical tube or pipe with rounded ends, featuring a smooth, uniform circular cross-section and a slight diagonal orientation.
def model_60865_19bbdeb4_0026():
    """Model: 1-Mini Part Pillar v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.812
        extrude(amount=6.812)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a straight, tapered design with a slightly pointed or rounded tip at one end.
def model_60865_19bbdeb4_0030():
    """Model: Untitled v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=34
        extrude(amount=34)
    return part.part


# Description: This is a cast or molded mounting bracket featuring an angled upper arm with a V-shaped channel or slot, mounted on a rectangular base platform with an internal geometric cutout pattern.
def model_60869_078e7c2a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.5380736842, perimeter: 57.0790364996
            with BuildLine():
                Line((-4, 0), (-2.5, 0))
                CenterArc((0, 0), 4, 180, 77.2795388542)
                Line((-0.8807782709, -7.5), (-0.8807782709, -3.901823886))
                Line((-6.5, -7.5), (-0.8807782709, -7.5))
                Line((-6.5, -9.5), (-6.5, -7.5))
                Line((6.5, -9.5), (-6.5, -9.5))
                Line((6.5, -7.5), (6.5, -9.5))
                Line((0.8807782709, -7.5), (6.5, -7.5))
                Line((0.8807782709, -3.901823886), (0.8807782709, -7.5))
                CenterArc((0, 0), 4, -77.2795388542, 77.2795388542)
                Line((2.5, 0), (4, 0))
                CenterArc((0, 0), 2.5, 180, 180)
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: A flat, trapezoidal or wedge-shaped plate with a tapered profile, featuring angled top surfaces and a recessed underside, resembling a streamlined or aerodynamic component with no holes or slots.
def model_60971_7fd762c1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((3, -2.5), (0, -2.5))
                Line((3, 0), (3, -2.5))
                Line((0, 0), (3, 0))
                Line((0, -2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a wedge-shaped or tapered enclosure component with a polygonal geometric form featuring multiple triangular facets, a flat base with a dark edge detail, and an overall streamlined, aerodynamic profile.
def model_60974_0eb2fc07_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.8275496309, perimeter: 27.0554985169
            with BuildLine():
                Line((0.7679491924, -4.443375673), (4.2320508076, -1.556624327))
                Line((4.2320508076, -1.556624327), (3.4641016151, 2.8867513459))
                Line((3.4641016151, 2.8867513459), (-0.7679491924, 4.443375673))
                Line((-0.7679491924, 4.443375673), (-4.2320508076, 1.556624327))
                Line((-4.2320508076, 1.556624327), (-3.4641016151, -2.8867513459))
                Line((-3.4641016151, -2.8867513459), (0.7679491924, -4.443375673))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a paraglider wing or airfoil component featuring an elongated elliptical profile with a curved upper surface, radial internal ribbing structure visible through the blue membrane, and a dark reinforced leading and trailing edge frame.
def model_60976_315b479a_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8225578848, perimeter: 14.7225840424
            with BuildLine():
                Line((6.5, -4.5), (0, -4.5))
                _nurbs_edge([(6.5, -4.5), (6.4643116737, -4.6154111207), (6.3869334873, -4.8461758471), (6.2561507408, -5.1795927191), (6.0555861924, -5.5864817026), (5.769835464, -6.0060499323), (5.4557943197, -6.3151768096), (5.1228109723, -6.497531897), (4.7753990252, -6.5525900264), (4.4130546724, -6.4994733005), (4.0316582861, -6.3725533698), (3.6267776264, -6.2111414495), (3.1962750782, -6.0513116144), (2.7434357193, -5.916245809), (2.2792297779, -5.8089061503), (1.8192699862, -5.7185993688), (1.3813163091, -5.6261096782), (0.9825860478, -5.5093353512), (0.6371341303, -5.3487184537), (0.3532289536, -5.1327031232), (0.1785521459, -4.9110384646), (0.0775979379, -4.7165088116), (0.0236415764, -4.5742628496), (0, -4.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5785411859, 0.5785411859, 0.5785411859, 0.5785411859, 0.5785411859, 0.5785411859, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 29.25, perimeter: 22
            with BuildLine():
                Line((6.5, 0), (6.5, -4.5))
                Line((0, 0), (6.5, 0))
                Line((0, -4.5), (0, 0))
                Line((6.5, -4.5), (0, -4.5))
            make_face()
            # Profile area: 7.8525173081, perimeter: 14.6962966395
            with BuildLine():
                Line((0, 0), (6.5, 0))
                _nurbs_edge([(0, 0), (0.0176619276, 0.1101212793), (0.0598179546, 0.3175673325), (0.143548848, 0.5903453963), (0.2962137935, 0.8772186847), (0.5545594092, 1.110761323), (0.8774550423, 1.2291343004), (1.2588107618, 1.252158271), (1.6879924849, 1.2144116719), (2.15104389, 1.1584367556), (2.632491613, 1.1254904472), (3.1170012427, 1.1466571142), (3.5909628996, 1.23486915), (4.0444446049, 1.3737136828), (4.471031858, 1.5238010844), (4.8668585804, 1.6357196483), (5.2299060878, 1.6610151471), (5.5592123102, 1.563498601), (5.8540888289, 1.3317476641), (6.1097094777, 0.9796222812), (6.2855887923, 0.6180028197), (6.4005426657, 0.3146871964), (6.4689162626, 0.103586154), (6.5, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4204671667, 0.4204671667, 0.4204671667, 0.4204671667, 0.4204671667, 0.4204671667], 5)
            make_face()
            # Profile area: 0.9766064553, perimeter: 9.0620663203
            with BuildLine():
                _nurbs_edge([(6.5, 0), (6.5026654244, -0.0088824924), (6.5389094801, -0.1304722187), (6.6042473897, -0.3709648744), (6.6878526658, -0.7422698855), (6.771311786, -1.2556822948), (6.8263640428, -1.9052096528), (6.8306006001, -2.5638710875), (6.7812903391, -3.2217307767), (6.6972571135, -3.7433250898), (6.6091678719, -4.1243103066), (6.5394086339, -4.3721935138), (6.5012696302, -4.4958941911), (6.5, -4.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4204671667, 0.4204671667, 0.4204671667, 0.4204671667, 0.4204671667, 0.4204671667, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.5785411859, 0.5785411859, 0.5785411859, 0.5785411859, 0.5785411859, 0.5785411859], 5)
                Line((6.5, 0), (6.5, -4.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat, parallelogram-shaped plate or panel with a shallow depth, featuring a slightly curved or beveled top surface with radiating ridge lines and a darker recessed edge or flange along one side.
def model_60978_158a44e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((5, -3), (0, -3))
                Line((5, 0), (5, -3))
                Line((0, 0), (5, 0))
                Line((0, -3), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a capsule-shaped container or housing with a rounded cylindrical body featuring a flat top surface with angular faceted geometry, a curved bottom, and what appears to be internal ribbing or structural reinforcement along the sides.
def model_61198_0c99f50a_0003():
    """Model: 支撐架"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.2831853072, perimeter: 14.2831853072
            with BuildLine():
                Line((-17.0671528901, -11.0091968384), (-17.0671528901, -9.0091968384))
                CenterArc((-15.0671528901, -11.0091968384), 2, 180, 180)
                Line((-13.0671528901, -9.0091968384), (-13.0671528901, -11.0091968384))
                Line((-17.0671528901, -9.0091968384), (-13.0671528901, -9.0091968384))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


# Description: This is a pentahedron or wedge-shaped solid with a trapezoidal profile, featuring five faces including two triangular ends and three quadrilateral sides, with a sharp apex at the top and a wider base at the bottom.
def model_61280_8bdbc90f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.625000108, perimeter: 8.6807858332
            with BuildLine():
                Line((1.4000000209, -1.0000000149), (-0.1000000015, 1.5000000224))
                Line((-0.1000000015, 1.5000000224), (-1.5000000224, -1.0000000149))
                Line((-1.5000000224, -1.0000000149), (1.4000000209, -1.0000000149))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a flat rectangular plate or panel with a tapered wedge-shaped profile, featuring a sloped top surface and a stepped edge design that creates a beveled or chamfered appearance along one side.
def model_61644_7833408f_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 80, perimeter: 36
            with BuildLine():
                Line((10, -8), (0, -8))
                Line((10, 0), (10, -8))
                Line((0, 0), (10, 0))
                Line((0, -8), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a trapezoidal prism or wedge-shaped block with an irregular polygonal cross-section, featuring multiple flat faces (both angular and planar surfaces) and internal geometric divisions, appearing to be a structural component or bracket with a tapered or sloped design.
def model_61767_6afe5575_0001():
    """Model: space saving sofa set part 3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.8, perimeter: 31.2
            with BuildLine():
                Line((-3.8, 4), (-3.8, -4))
                Line((-3.8, -4), (3.8, -4))
                Line((3.8, -4), (3.8, 4))
                Line((3.8, 4), (-3.8, 4))
            make_face()
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)
    return part.part


# Description: This is a segmented connector or joint assembly consisting of three identical trapezoidal blocks linked in a zigzag chain formation with triangular pivot plates on top, designed to allow articulated movement between segments.
def model_61767_6afe5575_0003():
    """Model: space saving sofa set part 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.8374769249, perimeter: 86.2
            with BuildLine():
                Line((-31.0848724803, 3.4), (-31.0848724803, 0))
                Line((-31.0848724803, 0), (-30.6848724803, 0))
                Line((-30.6848724803, 0), (-30.6848724803, 3))
                Line((-30.6848724803, 3), (-22.9848724803, 3))
                Line((-22.9848724803, 0.0966077871), (-22.9848724803, 3))
                Line((-22.9848724803, 0.0966077871), (-22.2848724803, 0.0966077871))
                Line((-22.2848724803, 5.6966077871), (-22.2848724803, 0.0966077871))
                Line((-14.1848724803, 5.6966077871), (-22.2848724803, 5.6966077871))
                Line((-14.1848724803, 0.0966077871), (-14.1848724803, 5.6966077871))
                Line((-13.4848724803, 0.0966077871), (-14.1848724803, 0.0966077871))
                Line((-13.4848724803, 3.0966077871), (-13.4848724803, 0.0966077871))
                Line((-5.7848724803, 3.0966077871), (-13.4848724803, 3.0966077871))
                Line((-5.7848724803, 0.0966077871), (-5.7848724803, 3.0966077871))
                Line((-5.3848724803, 0.0966077871), (-5.7848724803, 0.0966077871))
                Line((-5.3848724803, 3.4), (-5.3848724803, 0.0966077871))
                Line((-13.4848724803, 3.4), (-5.3848724803, 3.4))
                Line((-13.4848724803, 5.8966077871), (-13.4848724803, 3.4))
                Line((-22.9848724803, 5.8966077871), (-13.4848724803, 5.8966077871))
                Line((-22.9848724803, 3.4), (-22.9848724803, 5.8966077871))
                Line((-22.9848724803, 3.4), (-31.0848724803, 3.4))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a dark metal L-shaped bracket or corner brace with two perpendicular flanges of equal length, featuring a hollow rectangular profile with uniform wall thickness throughout.
def model_61826_b4fd2318_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.1058741134, perimeter: 47.5399378023
            with BuildLine():
                Line((-11.5384226894, 6.3), (-3.4615773106, 6.3))
                Line((-3.4615773106, 6.3), (-0.7615773106, 0))
                Line((0, 0), (-0.7615773106, 0))
                Line((-3, 7), (0, 0))
                Line((-12, 7), (-3, 7))
                Line((-12, 7), (-15, 0))
                Line((-15, 0), (-14.2384226894, 0))
                Line((-11.5384226894, 6.3), (-14.2384226894, 0))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a folded sheet metal bracket or angle iron with a bent rectangular form creating two perpendicular flanges and an internal triangular reinforcement or gusset for structural support.
def model_62183_49ed881a_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((5, 5), (4, 5))
                Line((4, 0), (4, 5))
                Line((5, 0), (4, 0))
                Line((5, 5), (5, 0))
            make_face()
            # Profile area: 12.5, perimeter: 17.0710678119
            with BuildLine():
                Line((5, 10), (5, 5))
                Line((0, 5), (5, 10))
                Line((4, 5), (0, 5))
                Line((5, 5), (4, 5))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a multi-directional connector or junction piece featuring four triangular/pyramidal protrusions extending in different directions from a central cylindrical hub, with one cylindrical passage running through the middle and visible apertures or holes throughout.
def model_62955_58bbef9f_0000():
    """Model: chair v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.7985040812, perimeter: 47.2881095286
            with BuildLine():
                Line((-0.4258740026, 1.6823972583), (-1.5904604454, 4.7445163686))
                CenterArc((-1.6839288549, 4.7089684233), 0.1, 20.8228317956, 179.9999987926)
                Line((-0.6128108217, 1.6113013678), (-1.7773972652, 4.67342048))
                CenterArc((1.7238994173, 2.5), 2.5, -159.1771682044, 69.1771682044)
                Line((1.7238994173, 0), (5, 0))
                CenterArc((5, -0.7), 0.7, -90, 180)
                Line((5, -1.4), (2.5335579484, -1.4))
                CenterArc((2.5335579484, -2.4), 1, 90, 56.1650110129)
                Line((1.7029133488, -1.8431970285), (-0.5056133719, -5.1379006983))
                CenterArc((-0.422548912, -5.1935809955), 0.1, 146.1650110129, 179.9999987926)
                Line((1.8690422687, -1.9545576228), (-0.3394844532, -5.2492612944))
                CenterArc((2.5335579484, -2.4), 0.8, 90, 56.1650110129)
                Line((2.5335579484, -1.6), (2.983853509, -1.6))
                CenterArc((2.983853509, -2.1), 0.5, 28.9692993933, 61.0307006067)
                Line((3.4212931867, -1.8578295469), (5.3404954432, -5.3245415509))
                CenterArc((5.4279833788, -5.2761074603), 0.1, -151.0307006067, 180.0000014788)
                Line((3.7125954753, -1.9710852265), (5.5154713131, -5.2276733674))
                CenterArc((3.9313153142, -1.85), 0.25, 90, 118.9692993933)
                Line((5, -1.6), (3.9313153142, -1.6))
                CenterArc((5, -0.7), 0.9, -90, 180)
                Line((1.7238994173, 0.2), (5, 0.2))
                CenterArc((1.7238994173, 2.5), 2.3, -159.1771682044, 69.1771682044)
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a bicycle fork with a vertical steerer tube, two curved blade-like legs, and a central junction point, designed to connect the handlebars to the front wheel.
def model_63065_8eed712c_0002():
    """Model: Left frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.5418653597, perimeter: 53.7984253245
            with BuildLine():
                Line((-6.6129204999, -7.1619896518), (-5.6702014973, -7.1619896518))
                Line((-5.6702014973, -7.1619896518), (-2.6218578725, -0.9119590073))
                CenterArc((-1.273666803, -1.5695157275), 1.5, 81.203670044, 72.796329956)
                Line((3.0181625283, -0.7157918032), (-1.0442829996, -0.0871584592))
                CenterArc((2.7576902617, -2.1930034328), 1.5, 16, 64)
                Line((4.1995828057, -1.779547399), (5.7232961307, -7.0933672569))
                Line((6.5894124632, -7.0933672569), (5.7232961307, -7.0933672569))
                Line((4.9998951254, -1.5500615342), (6.5894124632, -7.0933672569))
                CenterArc((2.7576902617, -2.1930034328), 2.3325644547, 16, 64)
                Line((-1.5446427612, 0.9341619804), (3.1627358286, 0.1041241266))
                CenterArc((-1.2320760414, 2.7068159358), 1.8, -157.5125368065, 57.5125368065)
                Line((-4.1234342931, 4.9853817624), (-2.895209882, 2.018349649))
                Line((-5.0632277138, 4.6436386914), (-4.1234342931, 4.9853817624))
                Line((-5.0632277138, 4.6436386914), (-3.7233161632, 1.421672543))
                CenterArc((-5.1083241091, 0.8456925175), 1.5, -21.2500505071, 43.830897251)
                Line((-6.6129204999, -7.1619896518), (-3.7103127844, 0.3020342277))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical sleeve or tube with a tapered conical section on one end and a flat circular face on the other, featuring a fine mesh or grid pattern on its curved surface.
def model_63132_330141d7_0007():
    """Model: Separation Mechanism"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.1830724035, perimeter: 20.4203522483
            with Locations((0, 5)):
                Circle(3.25)
        # OneSide extrude, distance=-8
        extrude(amount=-8)
    return part.part


# Description: This is a cylindrical tube or sleeve with a slight taper, featuring a mesh or perforated surface pattern along its body and an open top end with a blue-tinted rim.
def model_63132_330141d7_0012():
    """Model: Pack"""
    with BuildPart() as part:
        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((1.5, 2.5)):
                Circle(1)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a carabiner clip featuring an elongated oval shape with a gate mechanism, designed for securing and connecting equipment in climbing, safety, and outdoor applications. The part has a continuous loop with textured grip surfaces and a curved gate opening on one side.
def model_63328_85753146_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 23.2691702662, perimeter: 71.5974461742
            with BuildLine():
                CenterArc((1.5041252536, 8.7772541867), 1.5, 90.8008338099, 89.1991661901)
                Line((0.0041252536, 8.7772541867), (0.0041252536, 2.4996421274))
                CenterArc((2.5041252536, 2.4996421274), 2.5, -180, 90)
                Line((2.5041252536, -0.0003578726), (8.2041841586, -0.0003578726))
                CenterArc((8.2041841586, 2.8505742514), 2.850932124, -90, 73.300755766)
                Line((10.9348818844, 2.0313649337), (11.28775752, 3.2076170523))
                CenterArc((9.8510180922, 3.6386388807), 1.5, -16.699244234, 113.0394359799)
                Line((9.6853708031, 5.1294644827), (5.8133375705, 4.699238568))
                CenterArc((5.5924745184, 6.6870060373), 2, -165.9637565321, 82.303948278)
                Line((3.6521895181, 6.2019347872), (2.9174088088, 9.1410576242))
                CenterArc((1.4621950586, 8.7772541867), 1.5, 14.0362434679, 75.1629227222)
            make_face()
            with BuildLine():
                CenterArc((5.5924745184, 6.6870060373), 2.65, -165.9637565321, 82.303948278)
                Line((9.757151295, 4.4834400552), (5.8851180625, 4.0532141404))
                CenterArc((9.8510180922, 3.6386388807), 0.85, -16.699244234, 113.0394359799)
                Line((10.312294799, 2.2181410593), (10.6651704346, 3.3943931779))
                CenterArc((8.2041841586, 2.8505742514), 2.200932124, -90, 73.300755766)
                Line((2.5041252536, 0.6496421274), (8.2041841586, 0.6496421274))
                CenterArc((2.5041252536, 2.4996421274), 1.85, -180, 90)
                Line((0.6541252536, 8.7772541867), (0.6541252536, 2.4996421274))
                CenterArc((1.5041252536, 8.7772541867), 0.85, 91.4133334459, 88.5866665541)
                CenterArc((1.4621950586, 8.7772541867), 0.85, 14.0362434679, 74.5504230861)
                Line((3.021596893, 6.044286631), (2.2868161838, 8.983409468))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a hollow cylindrical capsule (pill or tank-shaped part) with rounded hemispherical ends and multiple longitudinal slots or grooves running along its length, featuring a central hollow core.
def model_65356_aaee1519_0000():
    """Model: main button"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((2.9919332131, 2)):
                Circle(0.45)
        # Symmetric extrude, each_side=0.975
        extrude(amount=0.975, both=True)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a slight 3D depth, featuring a beveled or chamfered edge along one side and a clean, minimalist design with no holes or slots.
def model_65378_8c7c2895_0004():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0000000447, perimeter: 8.1189620121
            with BuildLine():
                Line((4.6500000693, -3.2500000484), (1.6500000693, -3.2500000484))
                Line((5.0000000298, -2.2500000335), (4.6500000693, -3.2500000484))
                Line((2.0000000298, -2.2500000335), (5.0000000298, -2.2500000335))
                Line((1.6500000693, -3.2500000484), (2.0000000298, -2.2500000335))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical tube or rod with a slightly tapered design, featuring rounded ends and a uniform hollow or solid cylindrical body oriented at an angle.
def model_65484_cf3c6d7d_0000():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5761060527, perimeter: 5.6896663699
            Circle(0.9055385273)
        # OneSide extrude, distance=-16
        extrude(amount=-16)
    return part.part


# Description: This is a flat trapezoidal or wedge-shaped plate with a uniform thickness, featuring a diagonal internal partition line that divides the top surface into two triangular sections, and a beveled or chamfered edge on the left side.
def model_65556_26765aeb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96, perimeter: 40
            with BuildLine():
                Line((-6, 4), (-6, -4))
                Line((-6, -4), (6, -4))
                Line((6, -4), (6, 4))
                Line((6, 4), (-6, 4))
            make_face()
        # TwoSides extrude (symmetric), distance=0.25
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is an L-shaped angle bracket or corner brace with two perpendicular flanges of unequal lengths, featuring a hollow tubular or channel-like cross-section along both arms.
def model_65569_bd890a32_0003():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 337.398127571, perimeter: 360.6488687156
            with BuildLine():
                Line((0, 0), (41.6769163131, 0))
                Line((41.6769163131, 0), (63.8041080561, 66.4107475155))
                Line((63.8041080561, 66.4107475155), (61.8041080561, 66.4107475155))
                Line((61.8041080561, 66.4107475155), (40.3091217914, 1.897449929))
                Line((1.3223393111, 1.897449929), (40.3091217914, 1.897449929))
                Line((-21.5435477899, 65.9219338116), (1.3223393111, 1.897449929))
                Line((-23.5435477899, 65.9219338116), (-21.5435477899, 65.9219338116))
                Line((0, 0), (-23.5435477899, 65.9219338116))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical roller or drum with a solid end face and a perforated or slotted tubular body, commonly used in filtration, conveying, or separation applications.
def model_65827_d1469ad6_0001():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.1000000611, 4.2000000626)):
                Circle(0.2)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a cylindrical tube or sleeve with a smooth, uniform hollow circular cross-section and rounded edges at both ends, designed as a basic structural or connector component.
def model_65858_61e9b51a_0001():
    """Model: 2nd Level"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4836139188, perimeter: 21.9440246853
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth, tapered or slightly rounded exterior surface and what appears to be a hollow interior, featuring uniform diameter along its length.
def model_65858_61e9b51a_0003():
    """Model: 3rd Level"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1169982677, perimeter: 25.9338473554
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a cylindrical sleeve or tube with a threaded or knurled top rim and bottom end, featuring a smooth cylindrical body with subtle vertical ribbing or fluting along its length.
def model_65858_61e9b51a_0005():
    """Model: 4th Level"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7503826165, perimeter: 29.9236700254
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is an organic, helmet-like or pod-shaped component with a rounded top transitioning to a tapered lower section, featuring a mesh or lattice pattern on the upper surface and internal triangular structural reinforcements visible through semi-transparent walls.
def model_65858_61e9b51a_0008():
    """Model: Head Level"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 174.9243507445, perimeter: 59.5886047762
            with BuildLine():
                CenterArc((0, 0), 6.35, -18.0497342499, 216.0945394542)
                Line((-2.5399980579, -12.703140801), (-6.0376725497, -1.9669799651))
                Line((2.54, -12.6999998093), (-2.5399980579, -12.703140801))
                Line((2.54, -12.6999998093), (6.0375033118, -1.9674993672))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered, curved design and a hollow interior, featuring vertical ribbed or fluted surface texture along its body.
def model_65858_61e9b51a_0012():
    """Model: 3rd Level (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.1840730586, perimeter: 57.8524287159
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.445, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: A hollow cylindrical tube with an open top, featuring vertical ribbing or fluting along its exterior surface and rounded edges.
def model_65858_61e9b51a_0015():
    """Model: 1st Level (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9173043609, perimeter: 49.8727833757
            with BuildLine():
                CenterArc((0, 0), 4.1275, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a cylindrical sleeve or tube with vertical ribbed/grooved surface texture, featuring an open top with a rolled or flanged rim edge.
def model_65858_61e9b51a_0017():
    """Model: 2nd Level (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.5506887098, perimeter: 53.8626060458
            with BuildLine():
                CenterArc((0, 0), 4.445, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.1275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a sheet metal enclosure or housing component with a curved, asymmetrical body featuring a large flat base panel, a ribbed vertical wall section, and a curved top surface with a mesh or grid pattern cutout.
def model_66020_3c24ec33_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.609804586, perimeter: 11.541860872
            with BuildLine():
                CenterArc((-2.0145970653, 1.8822985327), 1.02140141, -59.7472976022, 66.3644928502)
                Line((-1.5, 1), (1.5, 1))
                CenterArc((2.0759195596, 1.9129597798), 1.0794345273, 175.3749326128, 62.3802371285)
                CenterArc((3.7000000346, 2.25), 2.7115494071, 157.2175934487, 28.0724876892)
                CenterArc((0.4000002146, 3.4500000514), 0.8139408369, -10.6196579825, 53.1301125994)
                Line((-1, 4), (1, 4))
                CenterArc((-0.5750001892, 3.5000000522), 0.6562200751, 130.3645269325, 67.3801495004)
                CenterArc((-3.7000000346, 2.25), 2.7115494071, -5.2900811379, 28.0724876892)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a rectangular prism or block with a pyramidal or peaked top surface, featuring internal diagonal structural ribs or bracing elements visible on its faces, giving it a reinforced, box-like appearance with a distinctive angled upper geometry.
def model_66163_10ed8c84_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300, perimeter: 130
            with BuildLine():
                Line((4.9240387651, 0.8682408883), (0, 0))
                Line((0, 0), (10.41889066, -59.0884651807))
                Line((10.41889066, -59.0884651807), (15.3429294251, -58.2202242924))
                Line((15.3429294251, -58.2202242924), (4.9240387651, 0.8682408883))
            make_face()
        # OneSide extrude, distance=45
        extrude(amount=45)
    return part.part


# Description: This is a bent or hinged bracket assembly with an angular, zigzag profile featuring multiple rectangular slots or openings along its dark blue structural members and lighter blue panel sections, designed to connect or support components at offset angles.
def model_66271_2715ff8e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 29 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 56.1118578949, perimeter: 141.8796447372
            with BuildLine():
                CenterArc((-7, 13), 2.8, 0, 90)
                Line((-7, 15.8), (-23, 15.8))
                CenterArc((-23, 13), 2.8, 90, 90)
                Line((-25.8, 13), (-25.8, 4.2))
                Line((-25.8, 4.2), (-18.2, 4.2))
                Line((-18.2, 4.2), (-18.2, 9.2))
                Line((-18.2, 9.2), (-12, 9.2))
                Line((-12, 9.2), (-12, 10))
                Line((-19, 10), (-12, 10))
                Line((-19, 5), (-19, 10))
                Line((-25, 5), (-19, 5))
                Line((-25, 13), (-25, 5))
                CenterArc((-23, 13), 2, 90, 90)
                Line((-7, 15), (-23, 15))
                CenterArc((-7, 13), 2, 0, 90)
                Line((-5, 13), (-5, 4.2))
                Line((-5, 4.2), (0, 4.2))
                Line((0, 4.2), (0, 10))
                Line((0, 10), (1, 10))
                Line((1, 10.8), (1, 10))
                Line((-0.8, 10.8), (1, 10.8))
                Line((-0.8, 5), (-0.8, 10.8))
                Line((-4.2, 5), (-0.8, 5))
                Line((-4.2, 13), (-4.2, 5))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


# Description: This is a surfboard or hydrofoil wing with an elongated elliptical shape, featuring a curved aerodynamic profile and internal structural ribbing or reinforcement lines running across its surface.
def model_66288_5cea5285_0001():
    """Model: table 4 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.7450173055, perimeter: 26.7035375555
            Circle(4.25)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


# Description: This is a cylindrical capsule or pill-shaped component with hemispherical ends, featuring a central cylindrical body with horizontal surface details or grooves running along its length.
def model_66803_dbe9d79a_0002():
    """Model: candle2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender body and rounded ends, featuring a smooth uniform diameter throughout its length.
def model_67262_d9978c87_0002():
    """Model: pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1734944543, perimeter: 1.4765485472
            Circle(0.235)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2)
    return part.part


# Description: This is a toroidal (donut-shaped) solid ring or collar with a circular cross-section, featuring a central hole and smooth, curved outer and inner surfaces.
def model_67578_a806a2cf_0002():
    """Model: toolprt3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a rectangular block or housing component with a complex internal structure featuring multiple parallel slots, rectangular cutouts, and passages, designed for fluid or air circulation or component mounting.
def model_69038_c6eff267_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6848749811, perimeter: 13.9011584293
            with BuildLine():
                CenterArc((0.625, 1.0825317547), 0.3, 156.8921025793, 166.2157948413)
                CenterArc((0, 0), 1.25, 73.7842051587, 32.4315896826)
                CenterArc((-0.625, 1.0825317547), 0.3, -143.1078974207, 166.2157948413)
                CenterArc((0, 0), 1.25, 133.7842051587, 32.4315896826)
                CenterArc((-1.25, 0), 0.3, -83.1078974207, 166.2157948413)
                CenterArc((0, 0), 1.25, -166.2157948413, 32.4315896826)
                CenterArc((-0.625, -1.0825317547), 0.3, -23.1078974207, 166.2157948413)
                CenterArc((0, 0), 1.25, -106.2157948413, 32.4315896826)
                CenterArc((0.625, -1.0825317547), 0.3, 36.8921025793, 166.2157948413)
                CenterArc((0, 0), 1.25, -46.2157948413, 32.4315896826)
                CenterArc((1.25, 0), 0.3, 96.8921025793, 166.2157948413)
                CenterArc((0, 0), 1.25, 13.7842051587, 32.4315896826)
            make_face()
            with BuildLine():
                Line((0, -0.7390083446), (0.64, -0.3695041723))
                Line((-0.64, -0.3695041723), (0, -0.7390083446))
                Line((-0.64, 0.3695041723), (-0.64, -0.3695041723))
                Line((0, 0.7390083446), (-0.64, 0.3695041723))
                Line((0.64, 0.3695041723), (0, 0.7390083446))
                Line((0.64, -0.3695041723), (0.64, 0.3695041723))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat rectangular plate with four evenly-spaced circular mounting holes arranged in a rectangular pattern.
def model_69291_cbefc92b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((1.5000000224, 1.0000000149)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-1.5000000224, 1.0000000149)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((1.5000000224, -1.0000000149)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-1.5000000224, -1.0000000149)):
                Circle(0.200000003)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a slanted rectangular form, featuring a diagonal internal line or ridge that divides the surface and suggests a bent or creased geometric structure.
def model_69488_025cf0a2_0000():
    """Model: Tablas"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9000, perimeter: 420
            with BuildLine():
                Line((75, -30), (75, 30))
                Line((75, 30), (-75, 30))
                Line((-75, 30), (-75, -30))
                Line((-75, -30), (75, -30))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: These are two parallelogram-shaped flat plates or shims with a simple geometric form and no holes or features, appearing to be scaled versions of the same basic design.
def model_69488_f2085c68_0004():
    """Model: Jardin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(9.0439788105, -18.455439529, -0.3500000001), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 143437.499999999, perimeter: 1725
            with BuildLine():
                Line((3038.393168898, -11500.2291621441), (3038.393168898, -10862.7291621441))
                Line((3263.393168898, -11500.2291621441), (3038.393168898, -11500.2291621441))
                Line((3263.393168898, -10862.7291621441), (3263.393168898, -11500.2291621441))
                Line((3038.393168898, -10862.7291621441), (3263.393168898, -10862.7291621441))
            make_face()
            # Profile area: 59399.9999999998, perimeter: 1050
            with BuildLine():
                Line((1973.393168898, -11027.7291621441), (2333.393168898, -11027.7291621441))
                Line((2333.393168898, -11027.7291621441), (2333.393168898, -10862.7291621441))
                Line((2333.393168898, -10862.7291621441), (1973.393168898, -10862.7291621441))
                Line((1973.393168898, -10862.7291621441), (1973.393168898, -11027.7291621441))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a thin-walled sheet metal or composite angular component with an arrow or chevron-like shape, featuring multiple flat faceted surfaces, internal diagonal ribbing or bracing, and sharp directional geometry that suggests aerodynamic or structural functionality.
def model_69488_f2085c68_0005():
    """Model: Piso"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 648225.0000000003, perimeter: 3585
            with BuildLine():
                Line((3013.6564902908, 11468.3885422414), (1948.6564902908, 11468.3885422414))
                Line((3238.6564902908, 11468.3885422414), (3013.6564902908, 11468.3885422414))
                Line((3238.6564902908, 11970.8885422414), (3238.6564902908, 11468.3885422414))
                Line((1948.6564902908, 11970.8885422414), (3238.6564902908, 11970.8885422414))
                Line((1948.6564902908, 11468.3885422414), (1948.6564902908, 11970.8885422414))
            make_face()
            # Profile area: 503212.5000000003, perimeter: 3075
            with BuildLine():
                Line((1948.6564902908, 11468.3885422414), (1948.6564902908, 10995.8885422414))
                Line((1948.6564902908, 10995.8885422414), (2308.6564902908, 10995.8885422414))
                Line((2308.6564902908, 10995.8885422414), (3013.6564902908, 10995.8885422414))
                Line((3013.6564902908, 10995.8885422414), (3013.6564902908, 11468.3885422414))
                Line((3013.6564902908, 11468.3885422414), (1948.6564902908, 11468.3885422414))
            make_face()
            # Profile area: 116325.0000000001, perimeter: 1740
            with BuildLine():
                Line((2308.6564902908, 10830.8885422414), (2308.6564902908, 10995.8885422414))
                Line((3013.6564902908, 10830.8885422414), (2308.6564902908, 10830.8885422414))
                Line((3013.6564902908, 10995.8885422414), (3013.6564902908, 10830.8885422414))
                Line((2308.6564902908, 10995.8885422414), (3013.6564902908, 10995.8885422414))
            make_face()
        # OneSide extrude, distance=-25
        extrude(amount=-25)
    return part.part


# Description: This is a long, slender hexagonal prism or rod with a uniform cross-section, featuring subtle grooves or ridges running along its length and tapered or beveled ends.
def model_69589_c2c993fc_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (5, 0))
                Line((5, 0), (5, 5))
                Line((5, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


# Description: This is a curved duct or elbow component featuring a hollow, tubular design that gradually tapers and bends from a rectangular opening at the top to a narrower pointed outlet at the bottom, with a mesh-like surface texture indicating it's likely a flexible or perforated duct element.
def model_69809_c94cd0f1_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.8485670915, perimeter: 28.8878489915
            with BuildLine():
                Line((4.1144171518, 4.2726403439), (4.2080771318, 4.0959264278))
                _nurbs_edge([(4.1144171518, 4.2726403439), (3.8957047324, 4.1567207758), (3.6473362412, 3.9804198114), (3.3817663261, 3.7625778719), (3.0415166803, 3.4834775727), (2.6797513963, 3.1387632375), (2.3629253339, 2.8107904327), (2.111723763, 2.5507509549), (1.8906981588, 2.3032408797), (1.6949179052, 2.0953083809), (1.4807684777, 1.867866518), (1.2951832151, 1.6891176872), (1.0827508666, 1.5487587024), (0.894508382, 1.4243825222), (0.6792572452, 1.3258773052), (0.4080636696, 1.2464806042), (0.0551586952, 1.1431614505), (-0.3907057635, 1.0748840222), (-0.8921339665, 1.0416662529), (-1.4338835431, 1.0057773413), (-2.033805046, 1.0115592793), (-2.6249131738, 1.0488680969), (-3.2696494893, 1.0895617508), (-3.9027380996, 1.1674157359), (-4.5114349969, 1.2462207141), (-5.0671122829, 1.3181615054), (-5.6073917129, 1.3889446667), (-6.1285937335, 1.4353555216), (-6.6510914411, 1.481881752), (-7.1560230239, 1.5027692384), (-7.5917612807, 1.5052849603), (-7.9586198867, 1.5074030076), (-8.2731302514, 1.4983026848), (-8.500602525, 1.4898286899), (-8.6557501715, 1.4840489949), (-8.7703412443, 1.4786167435), (-8.8428431504, 1.4747433725), (-8.8766411063, 1.4729377369), (-8.9008741252, 1.4714923194), (-8.9190335918, 1.4700772513)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0682350234, 0.0682350234, 0.0682350234, 0.1556581132, 0.1556581132, 0.1556581132, 0.2249731732, 0.2249731732, 0.2249731732, 0.3007917511, 0.3007917511, 0.3007917511, 0.3679767989, 0.3679767989, 0.3679767989, 0.4554048934, 0.4554048934, 0.4554048934, 0.5498633481, 0.5498633481, 0.5498633481, 0.6528915306, 0.6528915306, 0.6528915306, 0.746945601, 0.746945601, 0.746945601, 0.8412334859, 0.8412334859, 0.8412334859, 0.920616743, 0.920616743, 0.920616743, 0.974760157, 0.974760157, 0.974760157, 1, 1, 1, 1], 3)
                Line((-8.9190335918, 1.4700772513), (-8.9034957869, 1.2706817233))
                _nurbs_edge([(4.2080771318, 4.0959264278), (4.1494472618, 4.0648520643), (4.0268796396, 3.994072427), (3.8271036718, 3.8620098198), (3.5327167185, 3.6375464424), (3.1394959339, 3.2966989143), (2.7474377139, 2.9228173993), (2.3805001293, 2.5448312784), (2.0538367263, 2.1887430187), (1.7648909043, 1.8716893944), (1.4932950261, 1.6006094354), (1.2104532761, 1.3759956932), (0.8866625144, 1.1942965637), (0.4988649459, 1.0507214521), (0.0390882019, 0.9421132984), (-0.4881164967, 0.8666589575), (-1.0697716875, 0.823114829), (-1.6878736472, 0.8102239594), (-2.3231698504, 0.8260063496), (-2.9584145597, 0.8671863983), (-3.5826847059, 0.9283118243), (-4.1914580552, 1.0020589008), (-4.7839680103, 1.0802984292), (-5.3613877142, 1.1549325222), (-5.9247339212, 1.2188044972), (-6.4728061516, 1.2666252758), (-7.0003174848, 1.2958071476), (-7.4953547534, 1.3076200154), (-7.9415380182, 1.3061830136), (-8.3212376571, 1.296975647), (-8.618467945, 1.2855120461), (-8.7811608171, 1.277895188), (-8.8593414668, 1.2737008145), (-8.8920184565, 1.271576089), (-8.9034957869, 1.2706817233)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


# Description: This is a pair of dark blue steel support brackets or angle irons with elongated rectangular profiles, each featuring mounting holes at the ends and a uniform cross-sectional shape designed for structural support or frame assembly.
def model_70169_914780d4_0005():
    """Model: carriage 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2653237349, perimeter: 14.1999625088
            with BuildLine():
                Line((-4.6403372284, 3.4758424688), (-4.9745372284, 3.4758799621))
                Line((-4.9745372284, 3.4758799621), (-4.9745372284, -3.0241200379))
                Line((-4.9745372284, -3.0241200379), (-4.3745372284, -3.0241200379))
                Line((-4.3745372284, -3.0241200379), (-4.3745372284, -2.6741200379))
                Line((-4.3745372284, -2.6741200379), (-4.6403372284, -2.6741200379))
                Line((-4.6403372284, -2.6741200379), (-4.6403372284, 3.4758424688))
            make_face()
            # Profile area: 2.2653237349, perimeter: 14.1999625088
            with BuildLine():
                Line((2.9912627716, -2.6741200379), (2.9912627716, 3.4758424688))
                Line((2.7254627716, -2.6741200379), (2.9912627716, -2.6741200379))
                Line((2.7254627716, -3.0241200379), (2.7254627716, -2.6741200379))
                Line((3.3254627716, -3.0241200379), (2.7254627716, -3.0241200379))
                Line((3.3254627716, 3.4758799621), (3.3254627716, -3.0241200379))
                Line((2.9912627716, 3.4758424688), (3.3254627716, 3.4758799621))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a parallelepiped or wedge-shaped solid block featuring a rectangular base with angled top surfaces and internal diagonal cuts or chamfers that create a faceted, asymmetrical geometry.
def model_70169_914780d4_0006():
    """Model: table stop dogs v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((2, 2), (1.5, 2))
                Line((1.5, 2), (1.5, 1.5))
                Line((1.5, 1.5), (2, 1.5))
                Line((2, 1.5), (2, 2))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a hexagonal or octagonal box-shaped component with a curved/tapered profile, featuring a flat top surface with triangulated mesh details and darker side panels, suggesting it may be an enclosure, duct, or structural housing with aerodynamic or aesthetic contouring.
def model_70169_914780d4_0013():
    """Model: nut base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2844633687, perimeter: 1.9963350126
            with BuildLine():
                Line((-0.0500000007, 0.3500000052), (0.317506713, 0.3500000052))
                Line((-0.0500000007, 0.3500000052), (-0.1360635114, 0.2781094743))
                Line((-0.1360635114, 0.2781094743), (-0.1360635114, -0.1285639378))
                Line((-0.1360635114, -0.1285639378), (-0.0500000007, -0.200000003))
                Line((0.317506713, -0.200000003), (-0.0500000007, -0.200000003))
                Line((0.4035702237, -0.1285639378), (0.317506713, -0.200000003))
                Line((0.4035702237, 0.2781094743), (0.4035702237, -0.1285639378))
                Line((0.317506713, 0.3500000052), (0.4035702237, 0.2781094743))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a long, rectangular tool holder or tray with a flat base, slightly raised edges, and angled end caps, featuring a shallow channeled or grooved surface along its length.
def model_70188_002060a2_0000():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6565004316, perimeter: 5.2086672421
            with BuildLine():
                Line((0.75, -0.5521668105), (0.75, 0.5521668105))
                Line((0.75, 0.5521668105), (-0.75, 0.5521668105))
                Line((-0.75, 0.5521668105), (-0.75, -0.5521668105))
                Line((-0.75, -0.5521668105), (0.75, -0.5521668105))
            make_face()
        # OneSide extrude, distance=21
        extrude(amount=21)
    return part.part


# Description: This is a rectangular plastic or composite connector block with a tapered end, featuring multiple evenly-spaced rectangular slots or channels running along its length, designed for modular assembly or cable management applications.
def model_70483_e8b5a756_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1435575532, perimeter: 3.2790147483
            with BuildLine():
                Line((-0.1316011425, 0.786186503), (-0.1765144335, 0.7693364932))
                Line((-0.1765144335, 0.7693364932), (-0.1553674146, 0.3149402236))
                Line((-0.1553674146, 0.3149402236), (-0.1289668338, 0.302669737))
                Line((-0.1289668338, 0.302669737), (-0.1266389679, 0.2526497507))
                Line((-0.1266389679, 0.2526497507), (-0.1553674146, 0.246211931))
                Line((-0.1553674146, 0.246211931), (-0.1510286022, -0.7655567145))
                Line((-0.1510286022, -0.7655567145), (-0.118338343, -0.7654165274))
                Line((-0.118338343, -0.7654165274), (-0.046495315, -0.1399842143))
                Line((-0.046495315, -0.1399842143), (-0.030445221, 0.1342177722))
                _nurbs_edge([(-0.030445221, 0.1342177722), (-0.0319371539, 0.1354031477), (-0.0348054342, 0.1377648365), (-0.0387611123, 0.1412801836), (-0.0433303359, 0.1459120373), (-0.0477864987, 0.1516034287), (-0.0508728051, 0.1571874179), (-0.0524738226, 0.1626549546), (-0.0525200144, 0.1680005869), (-0.051064464, 0.1732284766), (-0.048217028, 0.178347237), (-0.044915158, 0.1823619659), (-0.041899147, 0.1853307051), (-0.0396525491, 0.1872913672), (-0.038470268, 0.1882670738)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.038470268, 0.1882670738), (-0.038470268, 0.3827336419))
                _nurbs_edge([(-0.038470268, 0.3827336419), (-0.0410453877, 0.3853231834), (-0.0460029006, 0.3904863135), (-0.0528610012, 0.3981831486), (-0.0608403002, 0.4083491887), (-0.0688293572, 0.4208857014), (-0.0747897687, 0.433227493), (-0.0787088444, 0.4453324193), (-0.0806338759, 0.457136151), (-0.0807255898, 0.4685453235), (-0.079244494, 0.4794440478), (-0.076493905, 0.4897092645), (-0.0727812288, 0.4992258177), (-0.0683799749, 0.507901436), (-0.063486795, 0.5156908853), (-0.0582219507, 0.5225884633), (-0.0537652891, 0.5274030985), (-0.0502966507, 0.5306263111), (-0.0479285862, 0.5326040139), (-0.0467306431, 0.5335500895)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.0467306431, 0.5335500895), (-0.0536837787, 0.7041682254))
                Line((-0.0536837787, 0.7041682254), (-0.1316011425, 0.786186503))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a mounting bracket or support arm with an angular, hook-like shape featuring two perpendicular flanges connected at a right angle, with textured or ribbed surfaces and internal cavities or slots along its faces.
def model_70571_938500e6_0003():
    """Model: Rey"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3779031034, perimeter: 3.8987938256
            with BuildLine():
                _nurbs_edge([(-10.0975807317, 9.6395038192), (-10.0970424815, 9.6420071559), (-10.0951105383, 9.6462857255), (-10.0896465473, 9.6505193679), (-10.0772227548, 9.6517914299), (-10.0533955734, 9.6462466239), (-10.022072154, 9.6340459845), (-9.9849663917, 9.6162060404), (-9.9446423236, 9.5943213906), (-9.904030736, 9.5704449814), (-9.8660670177, 9.5470116729), (-9.8332701947, 9.5267504675), (-9.8073683202, 9.5125914326), (-9.7888482139, 9.507602628), (-9.7766942061, 9.5148312474), (-9.769169651, 9.5365515858), (-9.7644319975, 9.573637062), (-9.761290509, 9.6247587112), (-9.7591567031, 9.6867888668), (-9.7578667358, 9.7554062014), (-9.7575510974, 9.8256227986), (-9.7584813258, 9.89234811), (-9.7609369586, 9.9509191931), (-9.765041211, 9.9976854979), (-9.7706625985, 10.0304822547), (-9.7771586041, 10.0493791752), (-9.783632132, 10.0565313704), (-9.7897700922, 10.0548727471), (-9.7967367539, 10.0469375215), (-9.8074644531, 10.0340977444), (-9.8250345818, 10.0173155488), (-9.8515296659, 9.9975578281), (-9.8864467793, 9.9764399044), (-9.9271370861, 9.9560709472), (-9.9697202976, 9.9387290887), (-10.0098184372, 9.9266004624), (-10.0433997149, 9.9214753966), (-10.0674890596, 9.9244990722), (-10.0811590039, 9.9358016108), (-10.0852173507, 9.9546889836), (-10.0813479467, 9.9800674844), (-10.0713863846, 10.0108139923), (-10.0566642074, 10.0461049499), (-10.038152714, 10.0853380956), (-10.0164965227, 10.1281095923), (-9.9920895045, 10.1741699411), (-9.970523359, 10.213545486), (-9.9532329436, 10.244476924), (-9.9412104621, 10.2657195181), (-9.9350753383, 10.2764962234)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-9.9350753383, 10.2764962234), (-9.9376382599, 10.2779223269), (-9.9428508837, 10.2808056), (-9.9509301582, 10.2852237144), (-9.9622270128, 10.2913022427), (-9.9772550322, 10.2992108616), (-9.9932490487, 10.3074071477), (-10.0102949061, 10.3158352428), (-10.0285056428, 10.3243843979), (-10.0480136651, 10.3328953877), (-10.0689565397, 10.3411888152), (-10.0914592039, 10.3490876952), (-10.1156160827, 10.3564400582), (-10.1414582824, 10.3631502651), (-10.1689628037, 10.3691758627), (-10.1980832728, 10.3745057948), (-10.2226308739, 10.378219236), (-10.2417272722, 10.3807003551), (-10.254760742, 10.3822203265), (-10.2613531124, 10.3829467846)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-10.2613531124, 10.3829467846), (-10.2613531124, 9.2015566429))
                Line((-10.0466950199, 9.2015566429), (-10.2613531124, 9.2015566429))
                CenterArc((-10.0790628672, 9.1271144614), 0.0811746015, 48.2510875925, 18.2492583893)
                _nurbs_edge([(-10.0250113379, 9.1876763975), (-10.020874058, 9.190459031), (-10.0129208368, 9.1959964417), (-10.0019549992, 9.2042189662), (-9.9892699275, 9.2150146651), (-9.9767096686, 9.2282637945), (-9.9675760708, 9.2413805149), (-9.9620616504, 9.2545912699), (-9.9604420584, 9.2682972588), (-9.9630017111, 9.2830323562), (-9.9698762371, 9.2993393943), (-9.9809332423, 9.3176807522), (-9.9955823332, 9.3383073815), (-10.0127876152, 9.3612396483), (-10.0312692855, 9.3863490314), (-10.0496461376, 9.413407502), (-10.0665985556, 9.4421458684), (-10.0810212683, 9.4723046998), (-10.0921882451, 9.5036872403), (-10.0996708265, 9.5361520217), (-10.1032582423, 9.5696045317), (-10.1029596399, 9.5971119625), (-10.1009584991, 9.6181500557), (-10.0988377617, 9.6323558342), (-10.0975807317, 9.6395038192)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, full_length=True, total=0.2
        extrude(amount=0.1, both=True)
    return part.part


# Description: Two parallel rectangular trays or shallow bins with sloped side walls and open tops, featuring a nested or stacked configuration with dark edges and light blue surfaces.
def model_70582_5500b76d_0000():
    """Model: component v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.785, perimeter: 25.9
            with BuildLine():
                Line((0, 5.1), (0, 3))
                Line((0, 3), (10.85, 3))
                Line((10.85, 3), (10.85, 5.1))
                Line((10.85, 5.1), (0, 5.1))
            make_face()
            # Profile area: 21.7, perimeter: 25.7
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (10.85, 0))
                Line((10.85, 0), (10.85, 2))
                Line((10.85, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is an elongated rectangular extrusion or channel with a tapered wedge-shaped end, featuring internal slots or grooves running along its length and a recessed cavity at the base.
def model_70585_cc4f9350_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.6, perimeter: 52.8
            with BuildLine():
                Line((5, -2.5), (-5, -2.5))
                Line((5, -2.5), (5, -1))
                Line((5, -1), (4, -1))
                Line((4, -1), (4, 0))
                Line((4, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 2))
                Line((7.5, 2), (0.8, 2))
                Line((0.8, 2), (0.8, 0.5))
                Line((0.8, 0.5), (1.5, 0.5))
                Line((1.5, 0.5), (1.5, -1.5))
                Line((-1.5, -1.5), (1.5, -1.5))
                Line((-1.5, 0.5), (-1.5, -1.5))
                Line((-0.8, 0.5), (-1.5, 0.5))
                Line((-0.8, 2), (-0.8, 0.5))
                Line((-7.5, 2), (-0.8, 2))
                Line((-7.5, 0), (-7.5, 2))
                Line((-4, 0), (-7.5, 0))
                Line((-4, -1), (-4, 0))
                Line((-5, -1), (-4, -1))
                Line((-5, -2.5), (-5, -1))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a boat or ship hull component featuring a complex angular, faceted geometry with a pointed bow section on the left, a main rectangular body in the center, and an open deck area on the right, characterized by multiple planar surfaces and sharp edges typical of low-poly 3D modeling.
def model_72073_e9d96404_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 277.0000000001, perimeter: 102.1421356237
            with BuildLine():
                Line((-9, 15), (-5, 15))
                Line((-9, 15), (-9, 2))
                Line((-17, 2), (-9, 2))
                Line((-17, 0), (-17, 2))
                Line((-17, 0), (17, 0))
                Line((17, 0), (17, 2))
                Line((17, 2), (9, 2))
                Line((9, 15), (9, 2))
                Line((9, 15), (5, 15))
                Line((5, 15), (0, 10))
                Line((-5, 15), (0, 10))
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)
    return part.part


# Description: This is an aerodynamic pod or fairing with an elongated, streamlined teardrop shape featuring a pointed nose cone, tapered body with subtle surface curves, and a rounded tail section, designed to minimize drag in fluid flow applications.
def model_72736_b2f56682_0000():
    """Model: Untitled"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9194027522, perimeter: 12.4483758629
            with BuildLine():
                CenterArc((0.9, 4.7), 0.3, 90, 270)
                Line((0.9, 5), (0, 5))
                Line((0, 5), (0, 0))
                Line((0, 0), (0.1000000015, 0))
                _nurbs_edge([(0.1000000015, 0), (0.2010807596, 0.1008242395), (0.3883188755, 0.2939449842), (0.6244444711, 0.5580737992), (0.8607268206, 0.8730164602), (1.058814068, 1.2736965085), (1.1546671959, 1.6687175369), (1.1917544213, 2.0463460038), (1.2, 2.3415354632), (1.2, 2.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((1.2, 2.5), (1.2, 4.7))
            make_face()
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0.9, 4.7), 0.3, 90, 270)
                CenterArc((0.9, 4.7), 0.3, 0, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: A horizontal cylindrical rod or beam with rounded ends featuring two rectangular slots or vents on opposite sides near each end.
def model_72824_38a3b7ba_0000():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.5, 1.5)):
                Circle(0.6)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a long, thin rectangular shaft or rod with a tapered or pointed end on one side, featuring a uniform cross-section along its length and appearing to be made of a dark material, likely designed as a fastener, tool, or structural component.
def model_73066_9e28b956_0000():
    """Model: K8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.875, perimeter: 12.7071067812
            with BuildLine():
                Line((0, 2), (6, 2))
                Line((0, 2), (0, 1.5))
                Line((5.5, 1.5), (0, 1.5))
                Line((6, 2), (5.5, 1.5))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


MODELS = {
    "model_56013_752d02cb_0008": {"func": model_56013_752d02cb_0008, "volume": 353.4291735289, "area": 575.3041546886},
    "model_56016_7af50dfa_0000": {"func": model_56016_7af50dfa_0000, "volume": 180, "area": 1230},
    "model_56065_00bbe5da_0003": {"func": model_56065_00bbe5da_0003, "volume": 0.0927751581, "area": 2.0616701789},
    "model_56065_00bbe5da_0004": {"func": model_56065_00bbe5da_0004, "volume": 0.5497787144, "area": 4.7909287967},
    "model_56065_00bbe5da_0007": {"func": model_56065_00bbe5da_0007, "volume": 1.1546283306, "area": 8.3702742736},
    "model_56065_00bbe5da_0010": {"func": model_56065_00bbe5da_0010, "volume": 4.7418414115, "area": 190.757505926},
    "model_56078_6d7f171c_0000": {"func": model_56078_6d7f171c_0000, "volume": 12.335311363, "area": 42.17762618},
    "model_56106_8cdc7ee3_0000": {"func": model_56106_8cdc7ee3_0000, "volume": 2.8274333882, "area": 189.6046560684},
    "model_56157_d9157017_0007": {"func": model_56157_d9157017_0007, "volume": 7.2382294739, "area": 74.6442414493},
    "model_56157_d9157017_0011": {"func": model_56157_d9157017_0011, "volume": 0.8694357669, "area": 9.6603974098},
    "model_56167_90101372_0000": {"func": model_56167_90101372_0000, "volume": 9.5262671114, "area": 69.598686568},
    "model_56167_90101372_0001": {"func": model_56167_90101372_0001, "volume": 865.1946167986, "area": 1085.7344210806},
    "model_56167_90101372_0007": {"func": model_56167_90101372_0007, "volume": 114.0305323943, "area": 538.7845618239},
    "model_56167_90101372_0008": {"func": model_56167_90101372_0008, "volume": 595, "area": 2528.5},
    "model_56167_90101372_0010": {"func": model_56167_90101372_0010, "volume": 116.0305323943, "area": 547.7845618239},
    "model_56167_90101372_0011": {"func": model_56167_90101372_0011, "volume": 987.5, "area": 4054},
    "model_56167_90101372_0012": {"func": model_56167_90101372_0012, "volume": 200, "area": 850},
    "model_56167_90101372_0014": {"func": model_56167_90101372_0014, "volume": 72.9113227778, "area": 377.3009346739},
    "model_56233_e0a640c6_0000": {"func": model_56233_e0a640c6_0000, "volume": 0.0120754968, "area": 1.1270463645},
    "model_56250_3b6024e3_0002": {"func": model_56250_3b6024e3_0002, "volume": 0.3063052837, "area": 4.6966810171},
    "model_56250_3b6024e3_0005": {"func": model_56250_3b6024e3_0005, "volume": 1.7304902737, "area": 15.7429734035},
    "model_56250_3b6024e3_0017": {"func": model_56250_3b6024e3_0017, "volume": 0.4335397862, "area": 9.0477868423},
    "model_56250_3b6024e3_0019": {"func": model_56250_3b6024e3_0019, "volume": 0.720995514, "area": 5.6077428867},
    "model_56250_3b6024e3_0020": {"func": model_56250_3b6024e3_0020, "volume": 1.0588820029, "area": 14.2483024251},
    "model_56250_3b6024e3_0023": {"func": model_56250_3b6024e3_0023, "volume": 0.2721404636, "area": 2.7646015352},
    "model_56343_60e8809c_0002": {"func": model_56343_60e8809c_0002, "volume": 0.0035342917, "area": 0.129590697},
    "model_56343_60e8809c_0003": {"func": model_56343_60e8809c_0003, "volume": 4.6514070148, "area": 37.0258401318},
    "model_56344_3a89f085_0001": {"func": model_56344_3a89f085_0001, "volume": 21.2473046207, "area": 83.5741965524},
    "model_56344_3a89f085_0013": {"func": model_56344_3a89f085_0013, "volume": 25.9999994934, "area": 143.1999973655},
    "model_56344_3a89f085_0015": {"func": model_56344_3a89f085_0015, "volume": 0.7853981634, "area": 10.9955742876},
    "model_56344_3a89f085_0018": {"func": model_56344_3a89f085_0018, "volume": 0.3051271865, "area": 5.8119464091},
    "model_56344_3a89f085_0021": {"func": model_56344_3a89f085_0021, "volume": 2.9776870275, "area": 19.2957661771},
    "model_56344_3a89f085_0022": {"func": model_56344_3a89f085_0022, "volume": 0.2023408151, "area": 7.0519815899},
    "model_56344_3a89f085_0026": {"func": model_56344_3a89f085_0026, "volume": 9.6959550811, "area": 37.5203235006},
    "model_56344_3a89f085_0029": {"func": model_56344_3a89f085_0029, "volume": 0.3326161222, "area": 5.7451875653},
    "model_56344_3a89f085_0030": {"func": model_56344_3a89f085_0030, "volume": 1.1780972451, "area": 9.8174770425},
    "model_56344_3a89f085_0031": {"func": model_56344_3a89f085_0031, "volume": 0.2120575041, "area": 4.2411500823},
    "model_56344_3a89f085_0035": {"func": model_56344_3a89f085_0035, "volume": 1.1665641299, "area": 10.015313727},
    "model_56345_80dc7bcc_0000": {"func": model_56345_80dc7bcc_0000, "volume": 6.4057522204, "area": 65.1884955592},
    "model_56345_80dc7bcc_0001": {"func": model_56345_80dc7bcc_0001, "volume": 8.7031556144, "area": 53.9214309125},
    "model_56345_80dc7bcc_0003": {"func": model_56345_80dc7bcc_0003, "volume": 11.6911503838, "area": 163.6761053731},
    "model_56345_80dc7bcc_0006": {"func": model_56345_80dc7bcc_0006, "volume": 3.0313602903, "area": 24.6926691465},
    "model_56345_80dc7bcc_0011": {"func": model_56345_80dc7bcc_0011, "volume": 0.6352069393, "area": 7.7872763323},
    "model_56345_80dc7bcc_0012": {"func": model_56345_80dc7bcc_0012, "volume": 1.48, "area": 17.14},
    "model_56430_4f35ba2f_0004": {"func": model_56430_4f35ba2f_0004, "volume": 3773.25, "area": 3731.6543289326},
    "model_56430_4f35ba2f_0005": {"func": model_56430_4f35ba2f_0005, "volume": 98.1747704247, "area": 166.897109722},
    "model_56430_4f35ba2f_0008": {"func": model_56430_4f35ba2f_0008, "volume": 132.5359400733, "area": 221.8749811598},
    "model_56430_4f35ba2f_0011": {"func": model_56430_4f35ba2f_0011, "volume": 93.4657082647, "area": 243.9225651046},
    "model_56430_4f35ba2f_0018": {"func": model_56430_4f35ba2f_0018, "volume": 2945.2431127404, "area": 2395.4643983622},
    "model_56430_4f35ba2f_0021": {"func": model_56430_4f35ba2f_0021, "volume": 24.5436926062, "area": 49.0873852123},
    "model_56430_4f35ba2f_0022": {"func": model_56430_4f35ba2f_0022, "volume": 4021.2385965949, "area": 2111.1502632123},
    "model_56430_4f35ba2f_0023": {"func": model_56430_4f35ba2f_0023, "volume": 479.3340131516, "area": 1205.0633465139},
    "model_56430_4f35ba2f_0026": {"func": model_56430_4f35ba2f_0026, "volume": 795.2156404399, "area": 738.6669726753},
    "model_56430_4f35ba2f_0030": {"func": model_56430_4f35ba2f_0030, "volume": 149407.2109300286, "area": 65099.0853918584},
    "model_56436_2a8fc254_0001": {"func": model_56436_2a8fc254_0001, "volume": 0.7048347635, "area": 15.6742480413},
    "model_56449_ad00f9f1_0000": {"func": model_56449_ad00f9f1_0000, "volume": 7.3667017574, "area": 56.0575556658},
    "model_56458_c027ed41_0003": {"func": model_56458_c027ed41_0003, "volume": 39.6901757395, "area": 84.765322189},
    "model_56458_c027ed41_0004": {"func": model_56458_c027ed41_0004, "volume": 8.2697437292, "area": 28.2379228611},
    "model_56458_c027ed41_0005": {"func": model_56458_c027ed41_0005, "volume": 20.7252255007, "area": 51.8252966561},
    "model_56459_7b640aed_0001": {"func": model_56459_7b640aed_0001, "volume": 10800, "area": 22440},
    "model_56459_7b640aed_0002": {"func": model_56459_7b640aed_0002, "volume": 35100, "area": 47730},
    "model_56459_7b640aed_0005": {"func": model_56459_7b640aed_0005, "volume": 381.0517783528, "area": 455.4017720162},
    "model_56459_7b640aed_0012": {"func": model_56459_7b640aed_0012, "volume": 7680.0000000001, "area": 15992},
    "model_56461_9a5be0e9_0002": {"func": model_56461_9a5be0e9_0002, "volume": 150.7964473723, "area": 175.929188601},
    "model_56466_e682bec3_0000": {"func": model_56466_e682bec3_0000, "volume": 169.6460032938, "area": 414.6902302739},
    "model_56468_c18aba85_0000": {"func": model_56468_c18aba85_0000, "volume": 65.1500456483, "area": 133.5945063582},
    "model_56477_620f7fc8_0009": {"func": model_56477_620f7fc8_0009, "volume": 31.6672539482, "area": 110.8353888186},
    "model_56486_82b3e23a_0003": {"func": model_56486_82b3e23a_0003, "volume": 0.2120575041, "area": 3.2515483965},
    "model_56486_82b3e23a_0004": {"func": model_56486_82b3e23a_0004, "volume": 0.3392920066, "area": 4.6652650906},
    "model_56486_82b3e23a_0005": {"func": model_56486_82b3e23a_0005, "volume": 3.9749515719, "area": 27.0087595976},
    "model_56486_82b3e23a_0014": {"func": model_56486_82b3e23a_0014, "volume": 0.1507964474, "area": 1.759291886},
    "model_56486_82b3e23a_0015": {"func": model_56486_82b3e23a_0015, "volume": 0.1272345025, "area": 2.1205750412},
    "model_56486_82b3e23a_0017": {"func": model_56486_82b3e23a_0017, "volume": 0.6408849013, "area": 8.5451320178},
    "model_56486_82b3e23a_0020": {"func": model_56486_82b3e23a_0020, "volume": 0.0942477796, "area": 2.1991148575},
    "model_56486_82b3e23a_0022": {"func": model_56486_82b3e23a_0022, "volume": 0.1319468915, "area": 3.0787608005},
    "model_56486_82b3e23a_0023": {"func": model_56486_82b3e23a_0023, "volume": 2.6023844204, "area": 16.4138159883},
    "model_56486_82b3e23a_0024": {"func": model_56486_82b3e23a_0024, "volume": 0.8906415173, "area": 6.9272118012},
    "model_56489_241ed182_0002": {"func": model_56489_241ed182_0002, "volume": 16.7736126235, "area": 96.9226143582},
    "model_56489_241ed182_0010": {"func": model_56489_241ed182_0010, "volume": 0.2295000095, "area": 5.805000114},
    "model_56489_241ed182_0013": {"func": model_56489_241ed182_0013, "volume": 62.2051053374, "area": 634.5545921353},
    "model_56490_0a0fba77_0000": {"func": model_56490_0a0fba77_0000, "volume": 115.9266705348, "area": 320.2607401482},
    "model_56568_d3018fcb_0003": {"func": model_56568_d3018fcb_0003, "volume": 582.1873623137, "area": 449.3172517416},
    "model_56568_d3018fcb_0005": {"func": model_56568_d3018fcb_0005, "volume": 2767.4166322533, "area": 1891.3271752418},
    "model_56568_d3018fcb_0006": {"func": model_56568_d3018fcb_0006, "volume": 2215.2626469127, "area": 1369.8268486966},
    "model_56568_d3018fcb_0010": {"func": model_56568_d3018fcb_0010, "volume": 75.0086227044, "area": 130.6436306304},
    "model_56711_61a0b988_0000": {"func": model_56711_61a0b988_0000, "volume": 15.5253518434, "area": 112.0334589974},
    "model_56799_4512d89e_0002": {"func": model_56799_4512d89e_0002, "volume": 0.2457772216, "area": 3.8079282512},
    "model_56799_4512d89e_0012": {"func": model_56799_4512d89e_0012, "volume": 0.2605476279, "area": 3.8234122311},
    "model_57000_cd1ddece_0001": {"func": model_57000_cd1ddece_0001, "volume": 81.93532, "area": 122.5804},
    "model_57000_cd1ddece_0006": {"func": model_57000_cd1ddece_0006, "volume": 16.387064, "area": 38.7096},
    "model_57142_38a8651d_0000": {"func": model_57142_38a8651d_0000, "volume": 3557.9380400259, "area": 7343.8583772021},
    "model_57146_b0c068a5_0000": {"func": model_57146_b0c068a5_0000, "volume": 11727.3373216936, "area": 6928.5688208588},
    "model_57152_3f47822e_0000": {"func": model_57152_3f47822e_0000, "volume": 15731.58144, "area": 7535.4688},
    "model_57152_9359fc8e_0000": {"func": model_57152_9359fc8e_0000, "volume": 14945.002368, "area": 7174.1792},
    "model_57153_2ec8170f_0000": {"func": model_57153_2ec8170f_0000, "volume": 785.3981633974, "area": 824.6680715673},
    "model_57535_4d975687_0000": {"func": model_57535_4d975687_0000, "volume": 4.270994, "area": 21.93264},
    "model_57535_4d975687_0004": {"func": model_57535_4d975687_0004, "volume": 0.2071358851, "area": 3.0934241842},
    "model_57535_4d975687_0005": {"func": model_57535_4d975687_0005, "volume": 0.4237672339, "area": 5.1046482391},
    "model_57616_eb493477_0000": {"func": model_57616_eb493477_0000, "volume": 600, "area": 490},
    "model_60180_eff9787a_0003": {"func": model_60180_eff9787a_0003, "volume": 22.0598436491, "area": 153.3142135317},
    "model_60281_3c62566a_0000": {"func": model_60281_3c62566a_0000, "volume": 149.5287425281, "area": 353.3467802163},
    "model_60287_1b0a1aa8_0000": {"func": model_60287_1b0a1aa8_0000, "volume": 34.2208223564, "area": 153.5377402202},
    "model_60288_015aa59d_0000": {"func": model_60288_015aa59d_0000, "volume": 19.2422550032, "area": 87.9645943005},
    "model_60293_49808d27_0000": {"func": model_60293_49808d27_0000, "volume": 471.2388980385, "area": 345.5751918949},
    "model_60516_cb7667ea_0009": {"func": model_60516_cb7667ea_0009, "volume": 52.8061499639, "area": 277.744995059},
    "model_60529_79e8313a_0012": {"func": model_60529_79e8313a_0012, "volume": 188495.5592153876, "area": 38327.4303737955},
    "model_60701_72ac971f_0001": {"func": model_60701_72ac971f_0001, "volume": 2.8274333882, "area": 19.4150425992},
    "model_60707_15529a7f_0004": {"func": model_60707_15529a7f_0004, "volume": 1.3744467859, "area": 11.3882733693},
    "model_60709_e245ebbb_0006": {"func": model_60709_e245ebbb_0006, "volume": 82, "area": 172},
    "model_60710_e4b3ae4f_0000": {"func": model_60710_e4b3ae4f_0000, "volume": 103.9884826633, "area": 139.9147897658},
    "model_60710_e4b3ae4f_0003": {"func": model_60710_e4b3ae4f_0003, "volume": 94.0542650191, "area": 155.3879364407},
    "model_60716_dcd9370c_0006": {"func": model_60716_dcd9370c_0006, "volume": 7.853981634, "area": 32.9867228627},
    "model_60719_76b5da02_0000": {"func": model_60719_76b5da02_0000, "volume": 22.0812987963, "area": 92.8168586263},
    "model_60719_76b5da02_0002": {"func": model_60719_76b5da02_0002, "volume": 4.4178646691, "area": 15.3152641863},
    "model_60720_ef9a0a95_0002": {"func": model_60720_ef9a0a95_0002, "volume": 22, "area": 63},
    "model_60720_ef9a0a95_0004": {"func": model_60720_ef9a0a95_0004, "volume": 12.375, "area": 37.5},
    "model_60720_ef9a0a95_0009": {"func": model_60720_ef9a0a95_0009, "volume": 0.0392699082, "area": 0.7068583471},
    "model_60723_c8e7621d_0004": {"func": model_60723_c8e7621d_0004, "volume": 78.75, "area": 214.5},
    "model_60726_c2bd4537_0004": {"func": model_60726_c2bd4537_0004, "volume": 0.0981747704, "area": 1.6689710972},
    "model_60728_99f07543_0005": {"func": model_60728_99f07543_0005, "volume": 1.8, "area": 21.48},
    "model_60728_99f07543_0006": {"func": model_60728_99f07543_0006, "volume": 2.5446900494, "area": 12.5820785776},
    "model_60729_c51868ec_0001": {"func": model_60729_c51868ec_0001, "volume": 2592000, "area": 212400},
    "model_60730_fa513b8a_0003": {"func": model_60730_fa513b8a_0003, "volume": 20.8162379037, "area": 62.8108635291},
    "model_60730_fa513b8a_0004": {"func": model_60730_fa513b8a_0004, "volume": 9.2448813252, "area": 38.1650494659},
    "model_60730_fa513b8a_0006": {"func": model_60730_fa513b8a_0006, "volume": 3.663415777, "area": 32.7082626026},
    "model_60739_f118b838_0001": {"func": model_60739_f118b838_0001, "volume": 15.3532203464, "area": 61.5317934015},
    "model_60739_f118b838_0002": {"func": model_60739_f118b838_0002, "volume": 11.8599095948, "area": 40.4735296398},
    "model_60739_f118b838_0003": {"func": model_60739_f118b838_0003, "volume": 22.5627441832, "area": 107.7957130798},
    "model_60753_80b955c8_0000": {"func": model_60753_80b955c8_0000, "volume": 16.2825731437, "area": 89.8728905316},
    "model_60753_80b955c8_0001": {"func": model_60753_80b955c8_0001, "volume": 66.5947956416, "area": 255.2948581099},
    "model_60759_23829707_0006": {"func": model_60759_23829707_0006, "volume": 169.6460032938, "area": 240.3318379996},
    "model_60760_f95d00ad_0019": {"func": model_60760_f95d00ad_0019, "volume": 223.7717090739, "area": 538.9944401613},
    "model_60760_f95d00ad_0023": {"func": model_60760_f95d00ad_0023, "volume": 100.2567090879, "area": 698.9031591306},
    "model_60760_f95d00ad_0024": {"func": model_60760_f95d00ad_0024, "volume": 60.112918912, "area": 283.9342707482},
    "model_60787_6f3aa359_0013": {"func": model_60787_6f3aa359_0013, "volume": 995, "area": 598},
    "model_60787_6f3aa359_0015": {"func": model_60787_6f3aa359_0015, "volume": 0.2013716694, "area": 4.094557278},
    "model_60787_6f3aa359_0026": {"func": model_60787_6f3aa359_0026, "volume": 0.1884955592, "area": 3.8327430374},
    "model_60865_19bbdeb4_0017": {"func": model_60865_19bbdeb4_0017, "volume": 353.4291735289, "area": 494.8008429404},
    "model_60865_19bbdeb4_0018": {"func": model_60865_19bbdeb4_0018, "volume": 372.7718560672, "area": 583.5583508184},
    "model_60865_19bbdeb4_0026": {"func": model_60865_19bbdeb4_0026, "volume": 4.0125992168, "area": 33.2788909795},
    "model_60865_19bbdeb4_0030": {"func": model_60865_19bbdeb4_0030, "volume": 26.7035375555, "area": 108.3849465488},
    "model_60869_078e7c2a_0000": {"func": model_60869_078e7c2a_0000, "volume": 380.3045894734, "area": 551.7084393649},
    "model_60971_7fd762c1_0000": {"func": model_60971_7fd762c1_0000, "volume": 3.75, "area": 20.5},
    "model_60974_0eb2fc07_0000": {"func": model_60974_0eb2fc07_0000, "volume": 26.4137748154, "area": 119.1828485202},
    "model_60976_315b479a_0000": {"func": model_60976_315b479a_0000, "volume": 23.4508390994, "area": 106.5438571913},
    "model_60978_158a44e7_0000": {"func": model_60978_158a44e7_0000, "volume": 7.5, "area": 38},
    "model_61198_0c99f50a_0003": {"func": model_61198_0c99f50a_0003, "volume": 114.2654824574, "area": 142.8318530718},
    "model_61280_8bdbc90f_0000": {"func": model_61280_8bdbc90f_0000, "volume": 10.8750003241, "area": 33.2923577155},
    "model_61644_7833408f_0002": {"func": model_61644_7833408f_0002, "volume": 80, "area": 196},
    "model_61767_6afe5575_0001": {"func": model_61767_6afe5575_0001, "volume": 176.32, "area": 212.08},
    "model_61767_6afe5575_0003": {"func": model_61767_6afe5575_0003, "volume": 142.6998153989, "area": 725.2749538497},
    "model_61826_b4fd2318_0000": {"func": model_61826_b4fd2318_0000, "volume": 16.1058741134, "area": 79.7516860291},
    "model_62183_49ed881a_0001": {"func": model_62183_49ed881a_0001, "volume": 105, "area": 197.4264068712},
    "model_62955_58bbef9f_0000": {"func": model_62955_58bbef9f_0000, "volume": 21.5932683596, "area": 222.3935010408},
    "model_63065_8eed712c_0002": {"func": model_63065_8eed712c_0002, "volume": 26.5418655799, "area": 106.8821560438},
    "model_63132_330141d7_0007": {"func": model_63132_330141d7_0007, "volume": 265.4645792283, "area": 229.7289627938},
    "model_63132_330141d7_0012": {"func": model_63132_330141d7_0012, "volume": 18.8495559215, "area": 43.9822971503},
    "model_63328_85753146_0000": {"func": model_63328_85753146_0000, "volume": 11.6345851331, "area": 82.3370636195},
    "model_65356_aaee1519_0000": {"func": model_65356_aaee1519_0000, "volume": 1.2405363991, "area": 6.7858401318},
    "model_65378_8c7c2895_0004": {"func": model_65378_8c7c2895_0004, "volume": 0.3000000045, "area": 6.8118962906},
    "model_65484_cf3c6d7d_0000": {"func": model_65484_cf3c6d7d_0000, "volume": 41.2176968435, "area": 96.1868740232},
    "model_65556_26765aeb_0000": {"func": model_65556_26765aeb_0000, "volume": 48, "area": 212},
    "model_65569_bd890a32_0003": {"func": model_65569_bd890a32_0003, "volume": 1686.9906378549, "area": 2478.04059872},
    "model_65827_d1469ad6_0001": {"func": model_65827_d1469ad6_0001, "volume": 0.1005309649, "area": 1.2566370614},
    "model_65858_61e9b51a_0001": {"func": model_65858_61e9b51a_0001, "volume": 44.2418967687, "area": 285.6563413412},
    "model_65858_61e9b51a_0003": {"func": model_65858_61e9b51a_0003, "volume": 52.2858779994, "area": 337.5938579487},
    "model_65858_61e9b51a_0005": {"func": model_65858_61e9b51a_0005, "volume": 60.32985923, "area": 389.5313745562},
    "model_65858_61e9b51a_0008": {"func": model_65858_61e9b51a_0008, "volume": 888.615701782, "area": 652.5588137521},
    "model_65858_61e9b51a_0012": {"func": model_65858_61e9b51a_0012, "volume": 116.6377278448, "area": 753.0939908087},
    "model_65858_61e9b51a_0015": {"func": model_65858_61e9b51a_0015, "volume": 100.5497653834, "area": 649.2189575937},
    "model_65858_61e9b51a_0017": {"func": model_65858_61e9b51a_0017, "volume": 108.5937466141, "area": 701.1564742012},
    "model_66020_3c24ec33_0000": {"func": model_66020_3c24ec33_0000, "volume": 19.8294137581, "area": 47.8451917881},
    "model_66163_10ed8c84_0000": {"func": model_66163_10ed8c84_0000, "volume": 13500.0000000001, "area": 6450},
    "model_66271_2715ff8e_0000": {"func": model_66271_2715ff8e_0000, "volume": 448.8948631591, "area": 1247.2608736876},
    "model_66288_5cea5285_0001": {"func": model_66288_5cea5285_0001, "volume": 2.2698006922, "area": 114.5581761132},
    "model_66803_dbe9d79a_0002": {"func": model_66803_dbe9d79a_0002, "volume": 8.9064151729, "area": 24.8814138164},
    "model_67262_d9978c87_0002": {"func": model_67262_d9978c87_0002, "volume": 0.9021711623, "area": 8.025041354},
    "model_67578_a806a2cf_0002": {"func": model_67578_a806a2cf_0002, "volume": 16.3362817987, "area": 57.8053048261},
    "model_69038_c6eff267_0000": {"func": model_69038_c6eff267_0000, "volume": 5.3697499621, "area": 33.1720668208},
    "model_69291_cbefc92b_0000": {"func": model_69291_cbefc92b_0000, "volume": 0.025132742, "area": 1.2566370951},
    "model_69488_025cf0a2_0000": {"func": model_69488_025cf0a2_0000, "volume": 22500, "area": 19050},
    "model_69488_f2085c68_0004": {"func": model_69488_f2085c68_0004, "volume": 1014187.4999999939, "area": 419549.9999999977},
    "model_69488_f2085c68_0005": {"func": model_69488_f2085c68_0005, "volume": 31694062.5000000224, "area": 2657025.0000000019},
    "model_69589_c2c993fc_0001": {"func": model_69589_c2c993fc_0001, "volume": 2000, "area": 1650},
    "model_69809_c94cd0f1_0000": {"func": model_69809_c94cd0f1_0000, "volume": 15.6678409416, "area": 164.592659962},
    "model_70169_914780d4_0005": {"func": model_70169_914780d4_0005, "volume": 4.5306474697, "area": 37.4612199571},
    "model_70169_914780d4_0006": {"func": model_70169_914780d4_0006, "volume": 0.05, "area": 0.9},
    "model_70169_914780d4_0013": {"func": model_70169_914780d4_0013, "volume": 0.0568926737, "area": 0.9681937399},
    "model_70188_002060a2_0000": {"func": model_70188_002060a2_0000, "volume": 34.7865090627, "area": 112.6950129466},
    "model_70483_e8b5a756_0000": {"func": model_70483_e8b5a756_0000, "volume": 0.0287114974, "area": 0.9429180604},
    "model_70571_938500e6_0003": {"func": model_70571_938500e6_0003, "volume": 0.0755803681, "area": 1.5355633914},
    "model_70582_5500b76d_0000": {"func": model_70582_5500b76d_0000, "volume": 26.691, "area": 119.93},
    "model_70585_cc4f9350_0000": {"func": model_70585_cc4f9350_0000, "volume": 1338, "area": 1673.2},
    "model_72073_e9d96404_0002": {"func": model_72073_e9d96404_0002, "volume": 8310.0000000024, "area": 3618.2640687114},
    "model_72736_b2f56682_0000": {"func": model_72736_b2f56682_0000, "volume": 1.0404292057, "area": 12.7054717975},
    "model_72824_38a3b7ba_0000": {"func": model_72824_38a3b7ba_0000, "volume": 9.0477868423, "area": 32.421236185},
    "model_73066_9e28b956_0000": {"func": model_73066_9e28b956_0000, "volume": 0.43125, "area": 7.6560660172},
}

if __name__ == "__main__":
    import time
    from build123d import export_step
    
    passed = 0
    failed = 0
    errors = []
    
    for name, info in MODELS.items():
        t0 = time.time()
        try:
            result = info["func"]()
            vol_err = abs(result.volume - info["volume"]) / max(info["volume"], 1e-10)
            area_err = abs(result.area - info["area"]) / max(info["area"], 1e-10)
            dt = time.time() - t0
            if vol_err < 0.01 and area_err < 0.01:
                print(f"  PASS  {name} ({dt:.1f}s)")
                passed += 1
            else:
                print(f"  FAIL  {name} vol_err={vol_err:.4%} area_err={area_err:.4%} ({dt:.1f}s)")
                failed += 1
                errors.append(name)
        except Exception as e:
            dt = time.time() - t0
            print(f"  ERROR {name}: {e} ({dt:.1f}s)")
            failed += 1
            errors.append(name)
    
    print(f"\nResults: {passed} passed, {failed} failed out of {len(MODELS)}")
    if errors:
        print(f"Failed: {errors}")
