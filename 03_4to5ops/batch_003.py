"""Batch 003 - passing/03_4to5ops
112 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical rod or shaft with a long, slender tubular body and a slightly tapered or beveled end at the top.
def model_134013_9b4cfef2_0008():
    """Model: Seiten_halterung v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0204, perimeter: 1.10623638
            with BuildLine():
                Line((-0.155, -0.155), (-0.155, 0.155))
                Line((-0.155, 0.355), (-0.155, 0.155))
                Line((-0.235, 0.355), (-0.155, 0.355))
                Line((-0.155, -0.155), (-0.235, 0.355))
            make_face()
            # Profile area: 0.0204, perimeter: 1.10623638
            with BuildLine():
                Line((0.355, -0.155), (0.155, -0.155))
                Line((0.155, -0.155), (-0.155, -0.155))
                Line((-0.155, -0.155), (0.2160943632, -0.2132108805))
                Line((0.355, -0.235), (0.2160943632, -0.2132108805))
                Line((0.355, -0.235), (0.355, -0.155))
            make_face()
            # Profile area: 0.0961, perimeter: 1.24
            with BuildLine():
                Line((0.155, -0.155), (-0.155, -0.155))
                Line((0.155, 0.155), (0.155, -0.155))
                Line((-0.155, 0.155), (0.155, 0.155))
                Line((-0.155, -0.155), (-0.155, 0.155))
            make_face()
        # OneSide extrude, distance=15.4
        extrude(amount=15.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0961, perimeter: 1.24
            with BuildLine():
                Line((0.155, -0.155), (-0.155, -0.155))
                Line((0.155, 0.155), (0.155, -0.155))
                Line((-0.155, 0.155), (0.155, 0.155))
                Line((-0.155, -0.155), (-0.155, 0.155))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0961, perimeter: 1.24
            with BuildLine():
                Line((-0.155, 0.155), (-0.155, -0.155))
                Line((-0.155, -0.155), (0.155, -0.155))
                Line((0.155, -0.155), (0.155, 0.155))
                Line((0.155, 0.155), (-0.155, 0.155))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a shallow rectangular box or tray with a long, narrow footprint, featuring a recessed top surface with internal geometric patterns or ribbing, and dark side flanges.
def model_134027_a6a95d00_0002():
    """Model: Slider"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 20.32), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.6773997093, perimeter: 17.779999733
            with BuildLine():
                Line((-41.9099993706, 3.8099999428), (-41.9099993706, 2.5399999619))
                Line((-41.9099993706, 2.5399999619), (-34.289999485, 2.5399999619))
                Line((-34.289999485, 2.5399999619), (-34.289999485, 3.8099999428))
                Line((-34.289999485, 3.8099999428), (-41.9099993706, 3.8099999428))
            make_face()
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8099999428, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((38.0999994278, 27.9399995804)):
                Circle(0.127)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a parallelogram-shaped duct or channel component with a trapezoidal profile, featuring a recessed slot or groove running along one side and a slightly angled top surface, designed for directing airflow or serving as a structural duct element.
def model_134123_e3bfe65c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.44, perimeter: 30.2
            with BuildLine():
                Line((-4.4, 3.15), (4.4, 3.15))
                Line((-4.4, -3.15), (-4.4, 3.15))
                Line((4.4, -3.15), (-4.4, -3.15))
                Line((4.4, 3.15), (4.4, -3.15))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((-4.4, 1.5), (-4.4, 1.8))
                Line((-3.9, 1.5), (-4.4, 1.5))
                Line((-3.9, 1.8), (-3.9, 1.5))
                Line((-4.4, 1.8), (-3.9, 1.8))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((-3.9, 0), (-3.9, 0.3))
                Line((-3.9, 0.3), (-4.4, 0.3))
                Line((-4.4, 0.3), (-4.4, 0))
                Line((-4.4, 0), (-3.9, 0))
            make_face()
        # OneSide extrude, distance=-6.3
        extrude(amount=-6.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular hollow box or enclosure with an open top, featuring two triangular reinforcement gussets or flanges on the front and back faces, and a flat base.
def model_134129_059b7f53_0000():
    """Model: Caixa"""
    with BuildPart() as part:
        # Caixa -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 98.7853981634, perimeter: 39.1415926536
            with BuildLine():
                CenterArc((1, 1), 0.5, 180, 90)
                Line((1, 0.5), (9, 0.5))
                CenterArc((9, 1), 0.5, -90, 90)
                Line((9.5, 1), (9.5, 11))
                CenterArc((9, 11), 0.5, 0, 90)
                Line((9, 11.5), (1, 11.5))
                CenterArc((1, 11), 0.5, 90, 90)
                Line((0.5, 11), (0.5, 1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Caixa -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.3561944902, perimeter: 81.4247779608
            with BuildLine():
                CenterArc((9, 1), 1, -90, 90)
                Line((10, 1), (10, 11))
                CenterArc((9, 11), 1, 0, 90)
                Line((9, 12), (1, 12))
                CenterArc((1, 11), 1, 90, 90)
                Line((0, 11), (0, 1))
                CenterArc((1, 1), 1, -180, 90)
                Line((1, 0), (9, 0))
            make_face()
            with BuildLine():
                Line((0.5, 11), (0.5, 1))
                CenterArc((1, 11), 0.5, 90, 90)
                Line((9, 11.5), (1, 11.5))
                CenterArc((9, 11), 0.5, 0, 90)
                Line((9.5, 1), (9.5, 11))
                CenterArc((9, 1), 0.5, -90, 90)
                Line((1, 0.5), (9, 0.5))
                CenterArc((1, 1), 0.5, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


# Description: A dark blue rectangular plate with rounded corners, a slight trapezoidal shape due to perspective, and a vertical slot or channel running along the left edge.
def model_134129_059b7f53_0001():
    """Model: Tampa"""
    with BuildPart() as part:
        # Tampa -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.3561944902, perimeter: 81.4247779608
            with BuildLine():
                CenterArc((-10, 11), 1, 90, 90)
                Line((-11, 1), (-11, 11))
                CenterArc((-10, 1), 1, 180, 90)
                Line((-2, 0), (-10, 0))
                CenterArc((-2, 1), 1, -90, 90)
                Line((-1, 11), (-1, 1))
                CenterArc((-2, 11), 1, 0, 90)
                Line((-10, 12), (-2, 12))
            make_face()
            with BuildLine():
                Line((-1.5, 11), (-1.5, 1))
                CenterArc((-2, 1), 0.5, -90, 90)
                Line((-2, 0.5), (-10, 0.5))
                CenterArc((-10, 1), 0.5, 180, 90)
                Line((-10.5, 1), (-10.5, 11))
                CenterArc((-10, 11), 0.5, 90, 90)
                Line((-10, 11.5), (-2, 11.5))
                CenterArc((-2, 11), 0.5, 0, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Tampa -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 98.7853981634, perimeter: 39.1415926536
            with BuildLine():
                CenterArc((-2, 11), 0.5, 0, 90)
                Line((-10, 11.5), (-2, 11.5))
                CenterArc((-10, 11), 0.5, 90, 90)
                Line((-10.5, 1), (-10.5, 11))
                CenterArc((-10, 1), 0.5, 180, 90)
                Line((-2, 0.5), (-10, 0.5))
                CenterArc((-2, 1), 0.5, -90, 90)
                Line((-1.5, 11), (-1.5, 1))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


# Description: This is a composite 3D part featuring an angular, faceted geometry with a conical/pyramidal section on the left transitioning into a rectangular prismatic base on the right, created from triangulated surfaces with both dark and light blue shaded faces.
def model_134444_f4a48508_0001():
    """Model: P19 Teacher v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.8709, perimeter: 23.6290501198
            with BuildLine():
                Line((7.62, 5.08), (0, 5.08))
                Line((0, 5.08), (0, 0))
                Line((0, 0), (5.08, 0))
                Line((7.62, 3.81), (5.08, 0))
                Line((7.62, 3.81), (7.62, 5.08))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 9.6774, perimeter: 13.7521024484
            with BuildLine():
                Line((0, 2.54), (-5.08, 2.54))
                Line((-2.54, 5.08), (0, 2.54))
                Line((-5.08, 5.08), (-2.54, 5.08))
                Line((-5.08, 2.54), (-5.08, 5.08))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular plate or panel with a trapezoidal or wedge-like profile, featuring internal diagonal reinforcement ribs or bracing elements that cross the face to add structural rigidity.
def model_134564_f00f1c90_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 390, perimeter: 142
            with BuildLine():
                Line((0, 65), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 65))
                Line((6, 65), (0, 65))
            make_face()
        # OneSide extrude, distance=86.5
        extrude(amount=86.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 86.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 122, perimeter: 126
            with BuildLine():
                Line((-2, -63), (-4, -63))
                Line((-2, -2), (-2, -63))
                Line((-4, -2), (-2, -2))
                Line((-4, -63), (-4, -2))
            make_face()
        # OneSide extrude, distance=-86.5
        extrude(amount=-86.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped metal panel or bracket with a slanted rectangular frame featuring two vertical slot openings and flanged edges for mounting or assembly purposes.
def model_134568_1011a501_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 58.0644, perimeter: 30.48
            with BuildLine():
                Line((7.62, -7.62), (0, -7.62))
                Line((7.62, 0), (7.62, -7.62))
                Line((0, 0), (7.62, 0))
                Line((0, -7.62), (0, 0))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.508), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.5437625113, perimeter: 12.1480324043
            with BuildLine():
                Line((-2.7183526401, 0.8801712778), (-3.352268428, 2.386863832))
                CenterArc((-2.4257, 1.0033), 0.3175, -157.1818868751, 67.1818868751)
                CenterArc((-2.4257, 1.0033), 0.3175, -90, 66.9715672485)
                Line((-2.1335013078, 0.8790978492), (-0.4112726146, 4.9308229507))
                CenterArc((-0.762, 5.0799033427), 0.3810966573, -23.0284327515, 51.7284327515)
                CenterArc((-0.762, 5.0799033427), 0.3810966573, 28.7, 61.3)
                Line((-0.762, 5.461), (-2.032, 5.461))
                Line((-3.352268428, 2.386863832), (-2.032, 5.461))
            make_face()
        # OneSide extrude, distance=0.381
        extrude(amount=0.381, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.508), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.7231933387, perimeter: 9.3063449475
            with BuildLine():
                Line((-0.762, 5.461), (-2.032, 5.461))
                CenterArc((-0.762, 5.0799033427), 0.3810966573, 28.7, 61.3)
                Line((-1.3391025593, 6.9275845953), (-0.4277225291, 5.2629149123))
                CenterArc((-1.63322, 6.76656), 0.3353117791, 28.7, 64.8004334033)
                CenterArc((-1.5748, 5.81152), 1.2921368927, 93.5004334033, 27.7234550496)
                Line((-4.1792651811, 5.7437245862), (-2.2446225653, 6.9164885427))
                CenterArc((-4.1002635215, 5.6134), 0.1524, 121.223888453, 148.776111547)
                Line((-2.032, 5.461), (-4.1002635215, 5.461))
            make_face()
            # Profile area: 11.5983751857, perimeter: 17.8785629021
            with BuildLine():
                Line((-5.3402907413, 7.112), (-7.14502, 7.112))
                Line((-7.14502, 7.112), (-4.5186722457, 0.8696904039))
                CenterArc((-4.2418, 0.9861797881), 0.3003797881, -157.1818868751, 67.1818868751)
                Line((-2.4257, 0.6858), (-4.2418, 0.6858))
                CenterArc((-2.4257, 1.0033), 0.3175, -157.1818868751, 67.1818868751)
                Line((-2.7183526401, 0.8801712778), (-3.352268428, 2.386863832))
                Line((-3.352268428, 2.386863832), (-5.3402907413, 7.112))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or elongated wedge-shaped connector with a tapered end on the left side, featuring a flat top surface and angled side faces, designed for mechanical assembly or fastening applications.
def model_134602_7dd4fb67_0000():
    """Model: Train"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49576583.3023701981, perimeter: 38510.252490795
            with BuildLine():
                Line((-1450.1768720383, 644.5230542392), (-17643.8186097994, 644.5230542392))
                Line((-1450.1768720383, 3706.0075618757), (-1450.1768720383, 644.5230542392))
                Line((-17643.8186097994, 3706.0075618757), (-1450.1768720383, 3706.0075618757))
                Line((-17643.8186097994, 644.5230542392), (-17643.8186097994, 3706.0075618757))
            make_face()
        # OneSide extrude, distance=3000
        extrude(amount=3000)
    return part.part


# Description: This is a parallelogram-shaped bracket or mounting plate with a rectangular cutout in the center and a cylindrical hole or boss protruding from the left side.
def model_134629_2bffd7ca_0001():
    """Model: pin2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.32, perimeter: 11.4
            with BuildLine():
                Line((0, 0.735), (0, 0.565))
                Line((0, 0.565), (0, 0))
                Line((0, 0), (2, 0))
                Line((2, 0), (2, 1.3))
                Line((2, 1.3), (0, 1.3))
                Line((0, 1.3), (0, 0.735))
            make_face()
            with BuildLine():
                Line((0.2, 0.25), (0.2, 1.05))
                Line((0.2, 1.05), (1.8, 1.05))
                Line((1.8, 1.05), (1.8, 0.25))
                Line((1.8, 0.25), (0.2, 0.25))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0655857293, perimeter: 1.075619449
            with BuildLine():
                CenterArc((-0.325, 0.66), 0.075, 90, 90)
                Line((-0.4, 0.64), (-0.4, 0.66))
                CenterArc((-0.325, 0.64), 0.075, 180, 90)
                Line((0, 0.565), (-0.325, 0.565))
                Line((0, 0.735), (0, 0.565))
                Line((0, 0.735), (-0.325, 0.735))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a circular fan or impeller assembly featuring a large flat disc with a textured mesh or perforated section on the upper portion and a small protruding hub or mounting boss on the right side.
def model_134763_dca8d2ef_0002():
    """Model: planet gear 2"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 11.3236150143, perimeter: 13.6025935352
            with BuildLine():
                CenterArc((0, 0), 1.91492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4966325609, perimeter: 2.7085454252
            with BuildLine():
                _nurbs_edge([(2.2313326103, -0.3276625986), (2.232946152, -0.3278988468), (2.2361771548, -0.3283194178), (2.2410354167, -0.3287945008), (2.247535559, -0.3291320463), (2.2556919796, -0.3291513212), (2.2638716676, -0.3288823228), (2.272066546, -0.3284371555), (2.2802703026, -0.3278964806), (2.2884797309, -0.3272889588), (2.2966936726, -0.3266098411), (2.3049122664, -0.3258346221), (2.3131361291, -0.3249336577), (2.3213654492, -0.3238885597), (2.3295995115, -0.322700454), (2.3378371147, -0.3213815447), (2.3460768056, -0.319950092), (2.3543171628, -0.3184245036), (2.3625571152, -0.3168166669), (2.3707960349, -0.3151299521), (2.3790335585, -0.3133628119), (2.3872694768, -0.3115109849), (2.3955036071, -0.3095700517), (2.4037356471, -0.3075383674), (2.4119651497, -0.3054175325), (2.4201915936, -0.3032109362), (2.4284144267, -0.3009228318), (2.4366331166, -0.2985572824), (2.4448472092, -0.2961169431), (2.4530563302, -0.2936030016), (2.4612601556, -0.2910157819), (2.4694583901, -0.2883551575), (2.4776507452, -0.2856210057), (2.485836912, -0.2828137378), (2.494016561, -0.2799342997), (2.5021893542, -0.2769839274), (2.5103549525, -0.2739639755), (2.5185130255, -0.2708757307), (2.5266632614, -0.267720194), (2.5348053665, -0.2644980888), (2.5429390594, -0.2612099654), (2.5510640666, -0.2578562787), (2.559180118, -0.2544374704), (2.5672869419, -0.2509540662), (2.5753842648, -0.2474066768), (2.5834718145, -0.2437959531), (2.591549322, -0.2401225558), (2.5996165238, -0.2363871213), (2.6076731648, -0.232590224), (2.6157189972, -0.2287323743), (2.6237537778, -0.2248140404), (2.6317772649, -0.2208356633), (2.6397892162, -0.2167976735), (2.6477893855, -0.2127005115), (2.6557775242, -0.2085446296), (2.6637533856, -0.2043304804), (2.6717167297, -0.200058508), (2.6796673265, -0.1957291407), (2.6876049623, -0.1913427801), (2.6955294374, -0.1868998015), (2.7034405552, -0.1824005652), (2.7113381129, -0.1778454258), (2.7192218928, -0.1732347418), (2.727091651, -0.1685688883), (2.7349471163, -0.1638482593), (2.742788014, -0.1590732488), (2.7506140846, -0.1542442362), (2.7584251033, -0.1493615714), (2.7662209018, -0.1444255589), (2.7740013829, -0.1394364454), (2.7817665002, -0.1343944217), (2.7879662938, -0.1303185825), (2.7926092229, -0.1272379902), (2.7957014362, -0.1251737265), (2.7972467747, -0.1241389607)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.8, -2.5410609694, 5.0821219387)
                _nurbs_edge([(2.2313326103, 0.3276625986), (2.232946152, 0.3278988468), (2.2361771548, 0.3283194178), (2.2410354167, 0.3287945008), (2.247535559, 0.3291320463), (2.2556919796, 0.3291513212), (2.2638716676, 0.3288823228), (2.272066546, 0.3284371555), (2.2802703026, 0.3278964806), (2.2884797309, 0.3272889588), (2.2966936726, 0.3266098411), (2.3049122664, 0.3258346221), (2.3131361291, 0.3249336577), (2.3213654492, 0.3238885597), (2.3295995115, 0.322700454), (2.3378371147, 0.3213815447), (2.3460768056, 0.319950092), (2.3543171628, 0.3184245036), (2.3625571152, 0.3168166669), (2.3707960349, 0.3151299521), (2.3790335585, 0.3133628119), (2.3872694768, 0.3115109849), (2.3955036071, 0.3095700517), (2.4037356471, 0.3075383674), (2.4119651497, 0.3054175325), (2.4201915936, 0.3032109362), (2.4284144267, 0.3009228318), (2.4366331166, 0.2985572824), (2.4448472092, 0.2961169431), (2.4530563302, 0.2936030016), (2.4612601556, 0.2910157819), (2.4694583901, 0.2883551575), (2.4776507452, 0.2856210057), (2.485836912, 0.2828137378), (2.494016561, 0.2799342997), (2.5021893542, 0.2769839274), (2.5103549525, 0.2739639755), (2.5185130255, 0.2708757307), (2.5266632614, 0.267720194), (2.5348053665, 0.2644980888), (2.5429390594, 0.2612099654), (2.5510640666, 0.2578562787), (2.559180118, 0.2544374704), (2.5672869419, 0.2509540662), (2.5753842648, 0.2474066768), (2.5834718145, 0.2437959531), (2.591549322, 0.2401225558), (2.5996165238, 0.2363871213), (2.6076731648, 0.232590224), (2.6157189972, 0.2287323743), (2.6237537778, 0.2248140404), (2.6317772649, 0.2208356633), (2.6397892162, 0.2167976735), (2.6477893855, 0.2127005115), (2.6557775242, 0.2085446296), (2.6637533856, 0.2043304804), (2.6717167297, 0.200058508), (2.6796673265, 0.1957291407), (2.6876049623, 0.1913427801), (2.6955294374, 0.1868998015), (2.7034405552, 0.1824005652), (2.7113381129, 0.1778454258), (2.7192218928, 0.1732347418), (2.727091651, 0.1685688883), (2.7349471163, 0.1638482593), (2.742788014, 0.1590732488), (2.7506140846, 0.1542442362), (2.7584251033, 0.1493615714), (2.7662209018, 0.1444255589), (2.7740013829, 0.1394364454), (2.7817665002, 0.1343944217), (2.7879662938, 0.1303185825), (2.7926092229, 0.1272379902), (2.7957014362, 0.1251737265), (2.7972467747, 0.1241389607)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((1.8936121659, 0.2782149403), (2.2313326103, 0.3276625986))
                Line((1.8936121659, -0.2782149403), (1.8936121659, 0.2782149403))
                Line((1.8936121659, -0.2782149403), (2.2313326103, -0.3276625986))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a black plastic electronic component bracket or mounting assembly featuring an elongated curved body with integrated circuit board sections, multiple mounting slots and holes, and protruding flanges designed for cable or connector attachment.
def model_134769_524913ff_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.1289148556, perimeter: 58.3349742906
            with BuildLine():
                CenterArc((-4.4541377849, 4.1436998032), 0.2983550795, 1.8526756109, 108.0507216104)
                Line((-4.5557083865, 4.4242335202), (-4.5557083865, 1.8000000268))
                CenterArc((-6.910811931, -2.4178303363), 4.8307976234, 26.2514288544, 34.5709567532)
                CenterArc((-2.7644269303, 0.3644268945), 0.6718516831, -73.9125943153, 41.0639510117)
                CenterArc((-1.7188349563, -2.1162620114), 2.1702729625, 0.6582733724, 102.1510497356)
                CenterArc((0.9107088861, -3.0050076232), 1.0226785393, 29.5912269769, 87.1028291341)
                CenterArc((2.2000000328, -3.4903458426), 1.0680752871, -9.4851696991, 121.478919048)
                CenterArc((0.9537464847, -2.110248763), 2.7767269761, -34.0842093225, 73.3722411558)
                Line((2.893510325, -0.2472771935), (3.1028567929, -0.351971884))
                Line((-2.2000000328, 2.3000000343), (2.893510325, -0.2472771935))
                Line((-2.2000000328, 3.4000000507), (-2.2000000328, 2.3000000343))
                CenterArc((-1.5000000224, 5.7500000857), 2.4520400036, -106.5873385569, 33.1746771139)
                CenterArc((-0.7874381278, 3.4500000514), 0.0515538651, -104.1029664138, 208.2059328276)
                CenterArc((-0.4682782236, 5.053825773), 1.5888403682, -132.6097967016, 30.5587936937)
                CenterArc((-1.2240486546, 4.1473884731), 0.414063091, 147.8863741161, 71.531729952)
                CenterArc((-1.6614589647, 4.4485059334), 0.1186518467, -43.0536017201, 101.8569440173)
                CenterArc((2.3793501308, 6.065528689), 4.258175038, -178.1880929632, 19.0373416687)
                CenterArc((-2.8708779415, 5.7982089162), 1.0029968682, 7.6017309933, 10.9831291922)
                CenterArc((7.6092381261, 14.0404912147), 12.3926502475, -142.6939208011, 2.4335448498)
                CenterArc((-2.3102890063, 6.5228934974), 0.0626639174, 6.1832999497, 167.6334001005)
                CenterArc((-3.5789956195, 6.609478654), 1.2090459805, -35.9308615661, 32.1447552911)
                CenterArc((-3.0215004496, 5.8269350276), 0.4277862777, -34.1798670775, 44.0140894392)
                CenterArc((-5.1005423877, 6.3708698663), 2.556220772, -31.6911477664, 13.8243402855)
                CenterArc((-2.9584558294, 5.0472473019), 0.0381951831, -149.7131568639, 119.4263137278)
                CenterArc((-2.2754044413, 5.5270505156), 0.8727948299, 176.0872414018, 38.7887660157)
                CenterArc((-3.161074331, 5.6587713892), 0.0736876762, -78.3265791696, 112.3482192911)
                CenterArc((-1.0911014306, 7.0169493974), 2.4020884953, -160.1170584425, 13.3642192392)
                CenterArc((-3.3750000503, 6.1949997712), 0.0254951609, 11.3106401236, 157.3787197527)
                CenterArc((-1.9651963066, 5.5550655085), 1.5730869021, 155.7964049595, 22.2941196666)
                CenterArc((-39.2975017503, 6.6641114578), 35.7756991555, -4.6552189915, 2.962750528)
                CenterArc((-4.0084760505, 3.7084760461), 0.3723166391, -55.9481630321, 63.9916492249)
                CenterArc((-1.913198502, 4.752230085), 2.3213242282, -165.0490142453, 20.6773679937)
            make_face()
            with BuildLine():
                CenterArc((-2.4548624418, 4.5724176641), 0.5888465757, -26.3286332247, 72.8920245054)
                CenterArc((-1.7050495381, 4.706214348), 0.4531014184, 139.5797921524, 101.0751737511)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.158632513, -3.3850695131), 1.1764286862, 14.0233720325, 86.6365359168)
                CenterArc((-3.6455299373, 2.6508420856), 7.4176694523, -41.1368383456, 15.6618643337)
                CenterArc((1.114433311, -2.0202952824), 2.4377170352, -26.2901051591, 63.6919556846)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((37.110540649, -24.4274086614), 41.7929511807, 145.2895588915, 2.4992024771)
                CenterArc((1.0035714435, -2.6464286109), 0.8964356992, 33.6267572981, 56.601511532)
                CenterArc((-29.7206259483, 48.2930015283), 58.7201742516, -58.4548786451, 2.0319546432)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((24.116479962, -35.8497199381), 41.4069426961, 120.9863739951, 3.4520779859)
                CenterArc((-1.7082089807, -1.9529851037), 2.4214607151, 5.9969905823, 56.7667082831)
                CenterArc((-4.1627011377, -32.4773025698), 32.8709437462, 77.7732042002, 6.0045977867)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.1857457252, perimeter: 26.4839019911
            with BuildLine():
                CenterArc((-1.9000000283, -2.0513789918), 2.5662169425, -96.7134341147, 13.4268682294)
                Line((-1.6000000238, -4.6000000685), (-1.3556170569, -4.7259673161))
                Line((-1.3556170569, -4.7259673161), (-1.0177299144, -4.5636489829))
                Line((-1.0177299144, -4.5636489829), (-0.686879778, -4.7341857497))
                Line((-0.686879778, -4.7341857497), (-0.5000000075, -4.4000000656))
                Line((-0.5000000075, -4.4000000656), (-0.0622211, -4.5670929076))
                Line((-0.0622211, -4.5670929076), (0.1274316479, -4.1991567805))
                Line((0.1274316479, -4.1991567805), (0.7000000104, -4.6000000685))
                Line((0.7000000104, -4.6000000685), (0.7000000104, -4.0000000596))
                Line((0.7000000104, -4.0000000596), (1.2820155152, -4.3000000641))
                Line((1.2820155152, -4.3000000641), (1.2820155152, -3.6000000536))
                Line((1.2820155152, -3.6000000536), (1.8000000268, -3.7000000551))
                Line((1.8000000268, -3.7000000551), (1.7000000253, -3.1000000462))
                Line((1.7000000253, -3.1000000462), (2.3000000343, -2.8000000417))
                Line((2.3000000343, -2.8000000417), (2.1744709267, -2.4225756971))
                CenterArc((2.2000000328, -3.4903458426), 1.0680752871, 91.3696125748, 20.6241367741)
                CenterArc((0.9107088861, -3.0050076232), 1.0226785393, 29.5912269769, 87.1028291341)
                CenterArc((-1.7188349563, -2.1162620114), 2.1702729625, 0.6582733724, 102.1510497356)
                CenterArc((-2.5000000373, -2.2000000328), 2.2203603642, 7.7651660184, 74.4696679631)
                CenterArc((-1.6615384863, -1.9846154142), 1.3641652396, -74.6315366782, 78.1877177725)
                CenterArc((-3.1817267446, 4.7807204369), 8.2969234685, -93.5813538392, 16.6899910599)
                CenterArc((-2.3287308209, -5.151057755), 2.1462457573, 129.7109830131, 20.9668917893)
                Line((-4.2000000626, -4.1000000611), (-4.2000000626, -5.7500000857))
                CenterArc((-3.8631308648, -5.2386701989), 0.6123227168, -123.377287971, 27.363238272)
                CenterArc((-3.8934599309, -5.7774766744), 0.0778758132, -115.7439834074, 182.823438162)
                CenterArc((-3.5416064447, -5.2845629695), 0.5298830358, 127.3573093238, 105.2853813524)
                CenterArc((-2.8631802622, -5.7949825008), 1.366671515, 60.9710090455, 76.0554506951)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube featuring two flat or slightly curved end faces connected by cylindrical sides, with a smooth, hollow interior geometry visible through the wireframe rendering.
def model_134947_91949c2f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2)
    return part.part


# Description: This is a mounting bracket or clamp with a blue base body featuring slots on the front face and a dark gray circular handle or loop extending from the top for gripping or hanging purposes.
def model_134948_f1f30b1b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 56.3849185461, perimeter: 47.3018308164
            with BuildLine():
                Line((0.0000000447, 5.500000082), (0.0000000447, 1.500000082))
                Line((1.2000001043, -0.499999918), (0.0000000447, 1.500000082))
                Line((8.0000001043, -0.499999918), (1.2000001043, -0.499999918))
                CenterArc((8.0000001043, 1.500000082), 2, -90, 90)
                Line((10.0000001043, 5.500000082), (10.0000001043, 1.500000082))
                Line((7.4494898477, 5.500000082), (10.0000001043, 5.500000082))
                CenterArc((7.4494898477, 6.000000082), 0.5, -168.4630411066, 78.4630411066)
                CenterArc((5.0000000745, 5.500000082), 2.0000000298, 11.5369588934, 156.9260822132)
                CenterArc((2.5505103013, 6.000000082), 0.5, -90, 78.4630411066)
                Line((2.5505103013, 5.500000082), (0.0000000447, 5.500000082))
            make_face()
            with BuildLine():
                CenterArc((5.0000000745, 5.500000082), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6, 2.4999999925), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.0000001043, 3.500000082), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.0000001043, 1.500000082), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.9227433388, perimeter: 9.4849555922
            with BuildLine():
                CenterArc((1.5000000179, 1.800000082), 0.3, -180, 90)
                Line((1.5000000179, 1.500000082), (2.9000000179, 1.500000082))
                CenterArc((2.9000000179, 1.800000082), 0.3, -90, 90)
                Line((3.2000000179, 1.800000082), (3.2000000179, 4.200000082))
                CenterArc((2.9000000179, 4.200000082), 0.3, 0, 90)
                Line((2.9000000179, 4.500000082), (1.5000000179, 4.500000082))
                CenterArc((1.5000000179, 4.200000082), 0.3, 90, 90)
                Line((1.2000000179, 4.200000082), (1.2000000179, 1.800000082))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a closed bottom end and open top, featuring a slightly tapered or rounded upper edge and vertical ribbed or textured surface details along its length.
def model_134996_bcf890ef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2261946711, perimeter: 4.5238934212
            with BuildLine():
                CenterArc((0, 0), 0.41, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.55
        extrude(amount=-1.55)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0895353906, perimeter: 3.5814156251
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated cage component with a curved bracket or lug protruding from one side, designed for filtering, ventilation, or structural support applications.
def model_135001_e76e4574_0000():
    """Model: Spur Gear (15 teeth)"""
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
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.4414723278, perimeter: 7.0680808158
            with BuildLine():
                CenterArc((0, 0), 0.62492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrusion2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0325308607, perimeter: 0.6968666326
            with BuildLine():
                _nurbs_edge([(0.6997328735, -0.084106512), (0.700155186, -0.0841566453), (0.7010005799, -0.0842447703), (0.7022709775, -0.0843405336), (0.7039692905, -0.0843988682), (0.7060986262, -0.0843765271), (0.7082331352, -0.0842848485), (0.7103715026, -0.0841495189), (0.7125126375, -0.0839898432), (0.7146559067, -0.0838134537), (0.7168009998, -0.083620053), (0.7189478204, -0.0834045225), (0.7210963708, -0.0831601637), (0.7232466322, -0.0828821172), (0.7253984702, -0.0825699961), (0.7275516835, -0.0822261877), (0.7297060348, -0.0818546839), (0.7318612873, -0.0814597668), (0.7340172422, -0.0810446209), (0.7361737644, -0.0806103982), (0.7383307599, -0.0801569894), (0.7404881608, -0.0796835265), (0.7426459085, -0.0791889604), (0.7448039356, -0.0786726773), (0.7469621548, -0.0781348704), (0.7491204679, -0.0775762068), (0.7512787717, -0.0769976215), (0.7534369645, -0.076400076), (0.7555949531, -0.0757842986), (0.7577526568, -0.0751506436), (0.7599100028, -0.0744992367), (0.7620669239, -0.0738300656), (0.7642233549, -0.0731430854), (0.7663792297, -0.0724383331), (0.7685344793, -0.0717159868), (0.7706890334, -0.0709763038), (0.7728428216, -0.0702195841), (0.7749957745, -0.0694461259), (0.777147825, -0.0686561786), (0.779298909, -0.0678499193), (0.7814489645, -0.0670274794), (0.783597931, -0.0661889614), (0.7857457486, -0.0653344584), (0.7878923577, -0.0644640753), (0.7900376983, -0.06357794), (0.7921817106, -0.062676192), (0.7943243356, -0.0617589757), (0.7964655148, -0.0608264322), (0.7986051914, -0.0598786912), (0.8007433098, -0.0589158664), (0.8028798153, -0.0579380604), (0.8050146537, -0.0569453683), (0.8071477705, -0.0559378817), (0.8092791102, -0.0549156926), (0.8114086165, -0.0538788963), (0.8135362335, -0.0528275886), (0.8156619061, -0.051761864), (0.8177855811, -0.0506818141), (0.8199072087, -0.0495875254), (0.8220267424, -0.0484790782), (0.824144137, -0.0473565493), (0.8262593458, -0.046220013), (0.8283723191, -0.0450695438), (0.8304830015, -0.043905218), (0.8325913306, -0.0427271156), (0.8346972426, -0.0415353166), (0.836800676, -0.0403298988), (0.8389015771, -0.0391109346), (0.8409999042, -0.0378784887), (0.843095632, -0.0366326154), (0.8451887475, -0.035373358), (0.8468611463, -0.0343552702), (0.8481142679, -0.0335857045), (0.8489491592, -0.033069995), (0.849366474, -0.0328114738)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.85, -2.2122660809, 4.4245321618)
                _nurbs_edge([(0.6997328735, 0.084106512), (0.700155186, 0.0841566453), (0.7010005799, 0.0842447703), (0.7022709775, 0.0843405336), (0.7039692905, 0.0843988682), (0.7060986262, 0.0843765271), (0.7082331352, 0.0842848485), (0.7103715026, 0.0841495189), (0.7125126375, 0.0839898432), (0.7146559067, 0.0838134537), (0.7168009998, 0.083620053), (0.7189478204, 0.0834045225), (0.7210963708, 0.0831601637), (0.7232466322, 0.0828821172), (0.7253984702, 0.0825699961), (0.7275516835, 0.0822261877), (0.7297060348, 0.0818546839), (0.7318612873, 0.0814597668), (0.7340172422, 0.0810446209), (0.7361737644, 0.0806103982), (0.7383307599, 0.0801569894), (0.7404881608, 0.0796835265), (0.7426459085, 0.0791889604), (0.7448039356, 0.0786726773), (0.7469621548, 0.0781348704), (0.7491204679, 0.0775762068), (0.7512787717, 0.0769976215), (0.7534369645, 0.076400076), (0.7555949531, 0.0757842986), (0.7577526568, 0.0751506436), (0.7599100028, 0.0744992367), (0.7620669239, 0.0738300656), (0.7642233549, 0.0731430854), (0.7663792297, 0.0724383331), (0.7685344793, 0.0717159868), (0.7706890334, 0.0709763038), (0.7728428216, 0.0702195841), (0.7749957745, 0.0694461259), (0.777147825, 0.0686561786), (0.779298909, 0.0678499193), (0.7814489645, 0.0670274794), (0.783597931, 0.0661889614), (0.7857457486, 0.0653344584), (0.7878923577, 0.0644640753), (0.7900376983, 0.06357794), (0.7921817106, 0.062676192), (0.7943243356, 0.0617589757), (0.7964655148, 0.0608264322), (0.7986051914, 0.0598786912), (0.8007433098, 0.0589158664), (0.8028798153, 0.0579380604), (0.8050146537, 0.0569453683), (0.8071477705, 0.0559378817), (0.8092791102, 0.0549156926), (0.8114086165, 0.0538788963), (0.8135362335, 0.0528275886), (0.8156619061, 0.051761864), (0.8177855811, 0.0506818141), (0.8199072087, 0.0495875254), (0.8220267424, 0.0484790782), (0.824144137, 0.0473565493), (0.8262593458, 0.046220013), (0.8283723191, 0.0450695438), (0.8304830015, 0.043905218), (0.8325913306, 0.0427271156), (0.8346972426, 0.0415353166), (0.836800676, 0.0403298988), (0.8389015771, 0.0391109346), (0.8409999042, 0.0378784887), (0.843095632, 0.0366326154), (0.8451887475, 0.035373358), (0.8468611463, 0.0343552702), (0.8481142679, 0.0335857045), (0.8489491592, 0.033069995), (0.849366474, 0.0328114738)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6194611937, 0.0745773534), (0.6997328735, 0.084106512))
                Line((0.6194611937, -0.0745773534), (0.6194611937, 0.0745773534))
                Line((0.6194611937, -0.0745773534), (0.6997328735, -0.084106512))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or deflector with an elongated parallelogram shape, featuring two parallel slots or grooves running along its length and a notched cutout at the upper left corner.
def model_135008_353681c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 140, perimeter: 51
            with BuildLine():
                Line((-4, 8.75), (4, 8.75))
                Line((-4, -8.75), (-4, 8.75))
                Line((4, -8.75), (-4, -8.75))
                Line((4, 8.75), (4, -8.75))
            make_face()
        # OneSide extrude, distance=0.175
        extrude(amount=0.175)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.175, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.44, perimeter: 9.8
            with BuildLine():
                Line((1.6, -8.7500001177), (-1.6, -8.7500001177))
                Line((1.6, -7.0500001177), (1.6, -8.7500001177))
                Line((-1.6, -7.0500001177), (1.6, -7.0500001177))
                Line((-1.6, -8.7500001177), (-1.6, -7.0500001177))
            make_face()
        # OneSide extrude, distance=-0.175
        extrude(amount=-0.175, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or clamp assembly featuring an L-shaped design with a blue rectangular mounting plate, a black cylindrical grip or handle section, and a dual-slot or fork-like end for attachment or gripping purposes.
def model_135033_4c0f554a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9396377858, perimeter: 9.7964707591
            with BuildLine():
                Line((0, -2), (0, 0))
                Line((0, 0), (-3, 0))
                Line((-3, 0), (-3, -1.6505495605))
                Line((-3, -1.6505495605), (-2.6545306151, -2))
                Line((-2.6545306151, -2), (0, -2))
            make_face()
            # Profile area: 1.9516031063, perimeter: 9.4712902353
            with BuildLine():
                Line((-3, -2), (-2.6545306151, -2))
                Line((-3, -1.6505495605), (-3, -2))
                Line((-5.9385531544, -4.5556257495), (-3, -1.6505495605))
                CenterArc((-6.1185889857, -5.0753247966), 0.55, 17.8251644023, 53.067560843)
                Line((-2.6545306151, -2), (-5.5949917142, -4.9069623978))
            make_face()
            # Profile area: 0.3527640244, perimeter: 5.4501021221
            with BuildLine():
                Line((-5.5949917142, -4.9069623978), (-5.6110544375, -4.9228421293))
                Line((-5.6110544375, -4.9228421293), (-5.9565238225, -4.5733916898))
                Line((-5.9565238225, -4.5733916898), (-5.9385531544, -4.5556257495))
                CenterArc((-6.1185889857, -5.0753247966), 0.55, 70.8927252453, 127.7311078316)
                Line((-6.4901699575, -5.223404442), (-6.6397885942, -5.250969233))
                CenterArc((-6.1185889857, -5.0753247966), 0.4, -110.3407026306, 312.0686002814)
                Line((-6.2576297199, -5.4503816912), (-6.2829985134, -5.6001766873))
                CenterArc((-6.1185889857, -5.0753247966), 0.55, -107.393132478, 125.2182968803)
            make_face()
            # Profile area: 0.0309457012, perimeter: 1.0486597078
            with BuildLine():
                CenterArc((-6.1185889857, -5.0753247966), 0.55, 17.8251644023, 53.067560843)
                Line((-5.9565238225, -4.5733916898), (-5.9385531544, -4.5556257495))
                Line((-5.6110544375, -4.9228421293), (-5.9565238225, -4.5733916898))
                Line((-5.5949917142, -4.9069623978), (-5.6110544375, -4.9228421293))
            make_face()
            # Profile area: 0.0603622142, perimeter: 1.1863104079
            with BuildLine():
                Line((-3, -1.6505495605), (-2.6545306151, -2))
                Line((-3, -1.6505495605), (-3, -2))
                Line((-3, -2), (-2.6545306151, -2))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5900001368, perimeter: 8.8000001311
            with BuildLine():
                Line((2.7000000402, 0), (2.7000000402, 1.7000000253))
                Line((2.7000000402, 1.7000000253), (0, 1.7000000253))
                Line((0, 1.7000000253), (0, 0))
                Line((0, 0), (2.7000000402, 0))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular fan or impeller component with a disc-like body featuring a central hub, radial blade passages visible through mesh cutouts on the outer rim, and a small protruding shaft or mounting point on the side.
def model_135092_c3610d5c_0001():
    """Model: Spur Gear (16 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.3427723082, perimeter: 2.7967714439
            with BuildLine():
                CenterArc((0, 0), 0.34512, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.168
        extrude(amount=0.168)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0089232171, perimeter: 0.3659660441
            with BuildLine():
                _nurbs_edge([(0.3846807515, -0.0436857346), (0.3849012197, -0.04371019), (0.3853425322, -0.0437530239), (0.3860056295, -0.0437990447), (0.3868919452, -0.0438256587), (0.3880030589, -0.0438109825), (0.3891168337, -0.0437611197), (0.3902326867, -0.0436887646), (0.3913501234, -0.043603603), (0.3924688415, -0.0435096186), (0.3935886786, -0.0434068324), (0.3947095661, -0.0432928366), (0.3958314831, -0.0431643718), (0.3969544071, -0.0430189555), (0.3980782725, -0.0428562841), (0.3992029875, -0.0426774652), (0.4003284469, -0.0424844298), (0.4014545453, -0.0422792947), (0.4025811916, -0.0420637056), (0.4037083201, -0.0418383085), (0.4048358824, -0.0416030993), (0.4059638415, -0.0413576787), (0.4070921648, -0.0411015326), (0.4082208176, -0.0408343244), (0.4093497577, -0.0405561164), (0.4104789386, -0.0402672185), (0.4116083117, -0.0399680832), (0.4127378292, -0.0396591881), (0.4138674462, -0.039340913), (0.4149971231, -0.0390134507), (0.4161268235, -0.0386768751), (0.4172565137, -0.0383311857), (0.4183861609, -0.0379763606), (0.4195157323, -0.0376124095), (0.4206451939, -0.0372394133), (0.4217745113, -0.0368574946), (0.4229036503, -0.0364667995), (0.4240325767, -0.0360674754), (0.4251612577, -0.0356596492), (0.4262896613, -0.0352434113), (0.4274177567, -0.0348188282), (0.4285455136, -0.034385951), (0.4296729023, -0.0339448249), (0.4307998929, -0.0334954993), (0.4319264556, -0.0330380355), (0.4330525607, -0.0325725006), (0.4341781785, -0.0320989646), (0.43530328, -0.0316174965), (0.4364278367, -0.03112816), (0.4375518207, -0.0306310108), (0.4386752046, -0.0301260989), (0.4397979611, -0.0296134703), (0.4409200627, -0.0290931692), (0.4420414816, -0.0285652393), (0.4431621895, -0.0280297262), (0.444282158, -0.0274866756), (0.4454013593, -0.026936133), (0.4465197665, -0.0263781421), (0.4476373541, -0.0258127445), (0.4487540985, -0.0252399791), (0.4498699765, -0.0246598824), (0.4509849647, -0.02407249), (0.4520990378, -0.0234778373), (0.4532121678, -0.0228759599), (0.4543243232, -0.0222668953), (0.4554354713, -0.0216506809), (0.4565455808, -0.021027353), (0.4576546239, -0.0203969458), (0.458762579, -0.01975949), (0.4598694326, -0.019115012), (0.4609751775, -0.0184635335), (0.4618588844, -0.0179367629), (0.4625211643, -0.0175385463), (0.462962462, -0.0172716741), (0.4631830553, -0.0171378894)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.4635, -2.1189916072, 4.2379832145)
                _nurbs_edge([(0.3846807515, 0.0436857346), (0.3849012197, 0.04371019), (0.3853425322, 0.0437530239), (0.3860056295, 0.0437990447), (0.3868919452, 0.0438256587), (0.3880030589, 0.0438109825), (0.3891168337, 0.0437611197), (0.3902326867, 0.0436887646), (0.3913501234, 0.043603603), (0.3924688415, 0.0435096186), (0.3935886786, 0.0434068324), (0.3947095661, 0.0432928366), (0.3958314831, 0.0431643718), (0.3969544071, 0.0430189555), (0.3980782725, 0.0428562841), (0.3992029875, 0.0426774652), (0.4003284469, 0.0424844298), (0.4014545453, 0.0422792947), (0.4025811916, 0.0420637056), (0.4037083201, 0.0418383085), (0.4048358824, 0.0416030993), (0.4059638415, 0.0413576787), (0.4070921648, 0.0411015326), (0.4082208176, 0.0408343244), (0.4093497577, 0.0405561164), (0.4104789386, 0.0402672185), (0.4116083117, 0.0399680832), (0.4127378292, 0.0396591881), (0.4138674462, 0.039340913), (0.4149971231, 0.0390134507), (0.4161268235, 0.0386768751), (0.4172565137, 0.0383311857), (0.4183861609, 0.0379763606), (0.4195157323, 0.0376124095), (0.4206451939, 0.0372394133), (0.4217745113, 0.0368574946), (0.4229036503, 0.0364667995), (0.4240325767, 0.0360674754), (0.4251612577, 0.0356596492), (0.4262896613, 0.0352434113), (0.4274177567, 0.0348188282), (0.4285455136, 0.034385951), (0.4296729023, 0.0339448249), (0.4307998929, 0.0334954993), (0.4319264556, 0.0330380355), (0.4330525607, 0.0325725006), (0.4341781785, 0.0320989646), (0.43530328, 0.0316174965), (0.4364278367, 0.03112816), (0.4375518207, 0.0306310108), (0.4386752046, 0.0301260989), (0.4397979611, 0.0296134703), (0.4409200627, 0.0290931692), (0.4420414816, 0.0285652393), (0.4431621895, 0.0280297262), (0.444282158, 0.0274866756), (0.4454013593, 0.026936133), (0.4465197665, 0.0263781421), (0.4476373541, 0.0258127445), (0.4487540985, 0.0252399791), (0.4498699765, 0.0246598824), (0.4509849647, 0.02407249), (0.4520990378, 0.0234778373), (0.4532121678, 0.0228759599), (0.4543243232, 0.0222668953), (0.4554354713, 0.0216506809), (0.4565455808, 0.021027353), (0.4576546239, 0.0203969458), (0.458762579, 0.01975949), (0.4598694326, 0.019115012), (0.4609751775, 0.0184635335), (0.4618588844, 0.0179367629), (0.4625211643, 0.0175385463), (0.462962462, 0.0172716741), (0.4631830553, 0.0171378894)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.3419222302, 0.0389427609), (0.3846807515, 0.0436857346))
                Line((0.3419222302, -0.0389427609), (0.3419222302, 0.0389427609))
                Line((0.3419222302, -0.0389427609), (0.3846807515, -0.0436857346))
            make_face()
        # OneSide extrude, distance=0.168
        extrude(amount=0.168, mode=Mode.ADD)
    return part.part


# Description: This is a circular fan or impeller wheel with a large flat disk face, a small central hub protruding from one side, and radial blade passages or vanes visible on the curved back surface.
def model_135092_c3610d5c_0002():
    """Model: Spur Gear (26 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 1.1094561612, perimeter: 4.4146916605
            with BuildLine():
                CenterArc((0, 0), 0.60262, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.168
        extrude(amount=0.168)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0094290323, perimeter: 0.3801401886
            with BuildLine():
                _nurbs_edge([(0.6273405277, -0.0473406104), (0.6276059627, -0.0473599125), (0.6281370229, -0.0473922845), (0.6289341844, -0.0474221459), (0.6299981847, -0.0474263158), (0.6313299023, -0.0473822937), (0.6326631359, -0.0473020723), (0.6339976614, -0.0471986415), (0.635333265, -0.0470819598), (0.6366697735, -0.046956182), (0.638007048, -0.0468214052), (0.6393449777, -0.0466752333), (0.6406834743, -0.0465143802), (0.6420224661, -0.0463363153), (0.6433618927, -0.0461407173), (0.6447017023, -0.0459287132), (0.6460418499, -0.0457022755), (0.6473822947, -0.0454635759), (0.6487229981, -0.0452143231), (0.6500639211, -0.0449552087), (0.6514050258, -0.0446862543), (0.6527462748, -0.0444070722), (0.6540876325, -0.0441171515), (0.6554290653, -0.0438161516), (0.656770542, -0.0435041375), (0.6581120332, -0.0431814295), (0.659453511, -0.0428484956), (0.6607949486, -0.042505832), (0.6621363198, -0.0421538393), (0.6634775986, -0.0417927274), (0.6648187595, -0.0414225826), (0.6661597773, -0.041043414), (0.6675006274, -0.0406552068), (0.6688412858, -0.0402579764), (0.6701817292, -0.0398518101), (0.6715219349, -0.0394368386), (0.6728618805, -0.0390132168), (0.6742015443, -0.0385811014), (0.6755409047, -0.0381406287), (0.6768799404, -0.0376918978), (0.6782186306, -0.0372349827), (0.6795569544, -0.0367699411), (0.6808948914, -0.0362968244), (0.6822324212, -0.035815688), (0.6835695237, -0.0353265986), (0.6849061791, -0.0348296293), (0.6862423676, -0.0343248562), (0.68757807, -0.0338123538), (0.6889132672, -0.0332921916), (0.6902479407, -0.0327644306), (0.691582072, -0.0322291258), (0.6929156428, -0.0316863281), (0.6942486346, -0.031136086), (0.6955810289, -0.0305784478), (0.6969128066, -0.0300134633), (0.6982439488, -0.0294411828), (0.6995744369, -0.0288616555), (0.7009042528, -0.0282749295), (0.7022333798, -0.02768105), (0.7035618018, -0.027080059), (0.7048895037, -0.0264719965), (0.7062164696, -0.025856901), (0.7075426828, -0.025234811), (0.7088681247, -0.0246057654), (0.710192774, -0.0239698053), (0.711516609, -0.0233269717), (0.7128396086, -0.0226773041), (0.7141617544, -0.0220208397), (0.7154830319, -0.0213576115), (0.7168034322, -0.020687647), (0.7181229508, -0.0200109683), (0.7191778589, -0.0194642667), (0.7199686426, -0.0190512307), (0.720495655, -0.0187745361), (0.7207591171, -0.0186358545)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.721, -1.4811022732, 2.9622045463)
                _nurbs_edge([(0.6273405277, 0.0473406104), (0.6276059627, 0.0473599125), (0.6281370229, 0.0473922845), (0.6289341844, 0.0474221459), (0.6299981847, 0.0474263158), (0.6313299023, 0.0473822937), (0.6326631359, 0.0473020723), (0.6339976614, 0.0471986415), (0.635333265, 0.0470819598), (0.6366697735, 0.046956182), (0.638007048, 0.0468214052), (0.6393449777, 0.0466752333), (0.6406834743, 0.0465143802), (0.6420224661, 0.0463363153), (0.6433618927, 0.0461407173), (0.6447017023, 0.0459287132), (0.6460418499, 0.0457022755), (0.6473822947, 0.0454635759), (0.6487229981, 0.0452143231), (0.6500639211, 0.0449552087), (0.6514050258, 0.0446862543), (0.6527462748, 0.0444070722), (0.6540876325, 0.0441171515), (0.6554290653, 0.0438161516), (0.656770542, 0.0435041375), (0.6581120332, 0.0431814295), (0.659453511, 0.0428484956), (0.6607949486, 0.042505832), (0.6621363198, 0.0421538393), (0.6634775986, 0.0417927274), (0.6648187595, 0.0414225826), (0.6661597773, 0.041043414), (0.6675006274, 0.0406552068), (0.6688412858, 0.0402579764), (0.6701817292, 0.0398518101), (0.6715219349, 0.0394368386), (0.6728618805, 0.0390132168), (0.6742015443, 0.0385811014), (0.6755409047, 0.0381406287), (0.6768799404, 0.0376918978), (0.6782186306, 0.0372349827), (0.6795569544, 0.0367699411), (0.6808948914, 0.0362968244), (0.6822324212, 0.035815688), (0.6835695237, 0.0353265986), (0.6849061791, 0.0348296293), (0.6862423676, 0.0343248562), (0.68757807, 0.0338123538), (0.6889132672, 0.0332921916), (0.6902479407, 0.0327644306), (0.691582072, 0.0322291258), (0.6929156428, 0.0316863281), (0.6942486346, 0.031136086), (0.6955810289, 0.0305784478), (0.6969128066, 0.0300134633), (0.6982439488, 0.0294411828), (0.6995744369, 0.0288616555), (0.7009042528, 0.0282749295), (0.7022333798, 0.02768105), (0.7035618018, 0.027080059), (0.7048895037, 0.0264719965), (0.7062164696, 0.025856901), (0.7075426828, 0.025234811), (0.7088681247, 0.0246057654), (0.710192774, 0.0239698053), (0.711516609, 0.0233269717), (0.7128396086, 0.0226773041), (0.7141617544, 0.0220208397), (0.7154830319, 0.0213576115), (0.7168034322, 0.020687647), (0.7181229508, 0.0200109683), (0.7191778589, 0.0194642667), (0.7199686426, 0.0190512307), (0.720495655, 0.0187745361), (0.7207591171, 0.0186358545)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.5999142976, 0.0453462102), (0.6273405277, 0.0473406104))
                Line((0.5999142976, -0.0453462102), (0.5999142976, 0.0453462102))
                Line((0.5999142976, -0.0453462102), (0.6273405277, -0.0473406104))
            make_face()
        # OneSide extrude, distance=0.168
        extrude(amount=0.168, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or wheel component with a large flat face, a protruding hub or axle on one side, and a mesh or perforated ring section around the outer edge.
def model_135092_c3610d5c_0003():
    """Model: Spur Gear (19 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.5290329462, perimeter: 3.2821475089
            with BuildLine():
                CenterArc((0, 0), 0.42237, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.168
        extrude(amount=0.168)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0091046917, perimeter: 0.3707787203
            with BuildLine():
                _nurbs_edge([(0.4575576351, -0.0447897462), (0.4577916294, -0.0448120548), (0.4582599157, -0.0448505906), (0.4589632382, -0.0448901507), (0.4599027364, -0.0449081229), (0.4610796932, -0.0448825965), (0.4622588259, -0.0448218389), (0.463439703, -0.044738554), (0.4646219479, -0.0446424533), (0.4658053135, -0.0445375521), (0.4669896477, -0.0444238966), (0.4681748655, -0.0442990989), (0.4693609185, -0.044159911), (0.4705477648, -0.0440038471), (0.4717353414, -0.0438305959), (0.4729235741, -0.0436412621), (0.4741123831, -0.0434377768), (0.4753016902, -0.0432222611), (0.4764914265, -0.0429963728), (0.4776815377, -0.0427607702), (0.47887198, -0.042515459), (0.4800627167, -0.0422600467), (0.4812537143, -0.0419940237), (0.482444939, -0.0417170529), (0.4836363535, -0.0414291966), (0.4848279188, -0.0411307655), (0.4860195954, -0.0408222142), (0.4872113444, -0.0405040234), (0.488403129, -0.0401765778), (0.4895949155, -0.0398400755), (0.4907866725, -0.039494594), (0.4919783699, -0.0391401363), (0.4931699788, -0.0387766829), (0.4943614703, -0.0384042454), (0.4955528151, -0.0380229061), (0.4967439841, -0.0376327895), (0.4979349482, -0.0372340434), (0.4991256788, -0.0368268178), (0.5003161478, -0.036411242), (0.5015063283, -0.0359874086), (0.5026961935, -0.0355553864), (0.5038857177, -0.0351152285), (0.5050748751, -0.0346669818), (0.5062636401, -0.0342106975), (0.5074519872, -0.0337464381), (0.508639891, -0.0332742724), (0.5098273264, -0.0327942719), (0.5110142686, -0.0323065071), (0.5122006933, -0.0318110433), (0.5133865768, -0.0313079374), (0.5145718956, -0.030797241), (0.5157566265, -0.0302790013), (0.5169407459, -0.0297532635), (0.5181242302, -0.0292200727), (0.5193070553, -0.0286794756), (0.5204891968, -0.0281315191), (0.5216706312, -0.0275762494), (0.5228513354, -0.0270137116), (0.5240312878, -0.026443948), (0.5252104682, -0.0258669983), (0.526388857, -0.0252829), (0.5275664341, -0.0246916892), (0.5287431781, -0.0240934019), (0.529919065, -0.0234880749), (0.5310940681, -0.0228757463), (0.5322681595, -0.0222564543), (0.5334413124, -0.0216302361), (0.5346135033, -0.0209971265), (0.5357847136, -0.0203571567), (0.536954932, -0.0197103533), (0.5381241524, -0.0190567375), (0.5390587285, -0.0185284078), (0.5397592104, -0.0181291065), (0.5402259983, -0.0178615487), (0.5404593423, -0.0177274306)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.54075, -1.8786666253, 3.7573332507)
                _nurbs_edge([(0.4575576351, 0.0447897462), (0.4577916294, 0.0448120548), (0.4582599157, 0.0448505906), (0.4589632382, 0.0448901507), (0.4599027364, 0.0449081229), (0.4610796932, 0.0448825965), (0.4622588259, 0.0448218389), (0.463439703, 0.044738554), (0.4646219479, 0.0446424533), (0.4658053135, 0.0445375521), (0.4669896477, 0.0444238966), (0.4681748655, 0.0442990989), (0.4693609185, 0.044159911), (0.4705477648, 0.0440038471), (0.4717353414, 0.0438305959), (0.4729235741, 0.0436412621), (0.4741123831, 0.0434377768), (0.4753016902, 0.0432222611), (0.4764914265, 0.0429963728), (0.4776815377, 0.0427607702), (0.47887198, 0.042515459), (0.4800627167, 0.0422600467), (0.4812537143, 0.0419940237), (0.482444939, 0.0417170529), (0.4836363535, 0.0414291966), (0.4848279188, 0.0411307655), (0.4860195954, 0.0408222142), (0.4872113444, 0.0405040234), (0.488403129, 0.0401765778), (0.4895949155, 0.0398400755), (0.4907866725, 0.039494594), (0.4919783699, 0.0391401363), (0.4931699788, 0.0387766829), (0.4943614703, 0.0384042454), (0.4955528151, 0.0380229061), (0.4967439841, 0.0376327895), (0.4979349482, 0.0372340434), (0.4991256788, 0.0368268178), (0.5003161478, 0.036411242), (0.5015063283, 0.0359874086), (0.5026961935, 0.0355553864), (0.5038857177, 0.0351152285), (0.5050748751, 0.0346669818), (0.5062636401, 0.0342106975), (0.5074519872, 0.0337464381), (0.508639891, 0.0332742724), (0.5098273264, 0.0327942719), (0.5110142686, 0.0323065071), (0.5122006933, 0.0318110433), (0.5133865768, 0.0313079374), (0.5145718956, 0.030797241), (0.5157566265, 0.0302790013), (0.5169407459, 0.0297532635), (0.5181242302, 0.0292200727), (0.5193070553, 0.0286794756), (0.5204891968, 0.0281315191), (0.5216706312, 0.0275762494), (0.5228513354, 0.0270137116), (0.5240312878, 0.026443948), (0.5252104682, 0.0258669983), (0.526388857, 0.0252829), (0.5275664341, 0.0246916892), (0.5287431781, 0.0240934019), (0.529919065, 0.0234880749), (0.5310940681, 0.0228757463), (0.5322681595, 0.0222564543), (0.5334413124, 0.0216302361), (0.5346135033, 0.0209971265), (0.5357847136, 0.0203571567), (0.536954932, 0.0197103533), (0.5381241524, 0.0190567375), (0.5390587285, 0.0185284078), (0.5397592104, 0.0181291065), (0.5402259983, 0.0178615487), (0.5404593423, 0.0177274306)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.4193655663, 0.0411485954), (0.4575576351, 0.0447897462))
                Line((0.4193655663, -0.0411485954), (0.4193655663, 0.0411485954))
                Line((0.4193655663, -0.0411485954), (0.4575576351, -0.0447897462))
            make_face()
        # OneSide extrude, distance=0.168
        extrude(amount=0.168, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or bushing component with a hollow circular bore, featuring mesh-textured openings on opposite sides and a protruding rectangular flange or tab extending from one end.
def model_135092_c3610d5c_0006():
    """Model: Spur Gear (8 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.0293876339, perimeter: 1.5024352707
            with BuildLine():
                CenterArc((0, 0), 0.13912, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.168
        extrude(amount=0.168)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0081203269, perimeter: 0.3460086583
            with BuildLine():
                _nurbs_edge([(0.1892732289, -0.0405903415), (0.1894565297, -0.0406289422), (0.1898240991, -0.0406995381), (0.190378356, -0.0407856155), (0.191122948, -0.0408626219), (0.1920616827, -0.0409068032), (0.1930067151, -0.0409127713), (0.1939563195, -0.0408942733), (0.1949091148, -0.040861672), (0.1958643946, -0.0408190888), (0.1968219211, -0.040766382), (0.1977817555, -0.0407008128), (0.1987440791, -0.0406187759), (0.1997090078, -0.0405176168), (0.2006764429, -0.0403970712), (0.2016461544, -0.0402583724), (0.2026178386, -0.0401036224), (0.2035911821, -0.0399350908), (0.2045659292, -0.0397544792), (0.2055419297, -0.0395624007), (0.2065191007, -0.039358787), (0.2074974007, -0.0391431586), (0.2084768007, -0.0389149327), (0.2094572532, -0.0386737507), (0.2104386727, -0.0384196879), (0.2114209512, -0.038153077), (0.2124039692, -0.0378743982), (0.2133876066, -0.0375841493), (0.2143717562, -0.0372827084), (0.2153563306, -0.0369702532), (0.2163412548, -0.0366468378), (0.217326462, -0.0363124414), (0.2183118879, -0.0359670247), (0.2192974653, -0.0356105907), (0.2202831205, -0.0352432189), (0.2212687764, -0.0348650326), (0.2222543544, -0.0344761788), (0.2232397769, -0.0340768049), (0.2242249689, -0.0336670336), (0.2252098598, -0.0332469486), (0.2261943821, -0.03281661), (0.2271784698, -0.0323760618), (0.2281620578, -0.0319253438), (0.2291450806, -0.0314645015), (0.2301274718, -0.0309935938), (0.2311091647, -0.030512686), (0.2320900927, -0.0300218464), (0.2330701903, -0.0295211426), (0.2340493933, -0.0290106363), (0.2350276391, -0.0284903809), (0.2360048664, -0.0279604246), (0.2369810139, -0.0274208116), (0.23795602, -0.0268715846), (0.2389298224, -0.0263127866), (0.239902357, -0.0257444628), (0.2408735601, -0.025166659), (0.2418433689, -0.0245794207), (0.2428117226, -0.0239827924), (0.243778564, -0.0233768163), (0.2447438397, -0.022761532), (0.2457074976, -0.0221369776), (0.2466694841, -0.0215031899), (0.2476297421, -0.0208602059), (0.248588208, -0.0202080637), (0.2495448104, -0.0195468028), (0.2504994755, -0.0188764631), (0.251452133, -0.0181970839), (0.2524027202, -0.0175087024), (0.2533511885, -0.016811353), (0.2542975076, -0.0161050662), (0.2552416608, -0.0153898673), (0.2559952454, -0.0148105941), (0.2565594559, -0.014372143), (0.2569351617, -0.0140780668), (0.257122906, -0.0139305849)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.2575, -3.1011789143, 6.2023578287)
                _nurbs_edge([(0.1892732289, 0.0405903415), (0.1894565297, 0.0406289422), (0.1898240991, 0.0406995381), (0.190378356, 0.0407856155), (0.191122948, 0.0408626219), (0.1920616827, 0.0409068032), (0.1930067151, 0.0409127713), (0.1939563195, 0.0408942733), (0.1949091148, 0.040861672), (0.1958643946, 0.0408190888), (0.1968219211, 0.040766382), (0.1977817555, 0.0407008128), (0.1987440791, 0.0406187759), (0.1997090078, 0.0405176168), (0.2006764429, 0.0403970712), (0.2016461544, 0.0402583724), (0.2026178386, 0.0401036224), (0.2035911821, 0.0399350908), (0.2045659292, 0.0397544792), (0.2055419297, 0.0395624007), (0.2065191007, 0.039358787), (0.2074974007, 0.0391431586), (0.2084768007, 0.0389149327), (0.2094572532, 0.0386737507), (0.2104386727, 0.0384196879), (0.2114209512, 0.038153077), (0.2124039692, 0.0378743982), (0.2133876066, 0.0375841493), (0.2143717562, 0.0372827084), (0.2153563306, 0.0369702532), (0.2163412548, 0.0366468378), (0.217326462, 0.0363124414), (0.2183118879, 0.0359670247), (0.2192974653, 0.0356105907), (0.2202831205, 0.0352432189), (0.2212687764, 0.0348650326), (0.2222543544, 0.0344761788), (0.2232397769, 0.0340768049), (0.2242249689, 0.0336670336), (0.2252098598, 0.0332469486), (0.2261943821, 0.03281661), (0.2271784698, 0.0323760618), (0.2281620578, 0.0319253438), (0.2291450806, 0.0314645015), (0.2301274718, 0.0309935938), (0.2311091647, 0.030512686), (0.2320900927, 0.0300218464), (0.2330701903, 0.0295211426), (0.2340493933, 0.0290106363), (0.2350276391, 0.0284903809), (0.2360048664, 0.0279604246), (0.2369810139, 0.0274208116), (0.23795602, 0.0268715846), (0.2389298224, 0.0263127866), (0.239902357, 0.0257444628), (0.2408735601, 0.025166659), (0.2418433689, 0.0245794207), (0.2428117226, 0.0239827924), (0.243778564, 0.0233768163), (0.2447438397, 0.022761532), (0.2457074976, 0.0221369776), (0.2466694841, 0.0215031899), (0.2476297421, 0.0208602059), (0.248588208, 0.0202080637), (0.2495448104, 0.0195468028), (0.2504994755, 0.0188764631), (0.251452133, 0.0181970839), (0.2524027202, 0.0175087024), (0.2533511885, 0.016811353), (0.2542975076, 0.0161050662), (0.2552416608, 0.0153898673), (0.2559952454, 0.0148105941), (0.2565594559, 0.014372143), (0.2569351617, 0.0140780668), (0.257122906, 0.0139305849)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.1350494201, 0.029171532), (0.1892732289, 0.0405903415))
                Line((0.1350494201, -0.029171532), (0.1350494201, 0.029171532))
                Line((0.1350494201, -0.029171532), (0.1892732289, -0.0405903415))
            make_face()
        # OneSide extrude, distance=0.168
        extrude(amount=0.168, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow tubular body, featuring two rectangular slots or cutouts on opposite sides and an internal mesh or perforated surface pattern.
def model_135092_c3610d5c_0007():
    """Model: Spur Gear (8 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.0293876339, perimeter: 1.5024352707
            with BuildLine():
                CenterArc((0, 0), 0.13912, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.323
        extrude(amount=0.323)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0081203269, perimeter: 0.3460086583
            with BuildLine():
                _nurbs_edge([(0.1892732289, -0.0405903415), (0.1894565297, -0.0406289422), (0.1898240991, -0.0406995381), (0.190378356, -0.0407856155), (0.191122948, -0.0408626219), (0.1920616827, -0.0409068032), (0.1930067151, -0.0409127713), (0.1939563195, -0.0408942733), (0.1949091148, -0.040861672), (0.1958643946, -0.0408190888), (0.1968219211, -0.040766382), (0.1977817555, -0.0407008128), (0.1987440791, -0.0406187759), (0.1997090078, -0.0405176168), (0.2006764429, -0.0403970712), (0.2016461544, -0.0402583724), (0.2026178386, -0.0401036224), (0.2035911821, -0.0399350908), (0.2045659292, -0.0397544792), (0.2055419297, -0.0395624007), (0.2065191007, -0.039358787), (0.2074974007, -0.0391431586), (0.2084768007, -0.0389149327), (0.2094572532, -0.0386737507), (0.2104386727, -0.0384196879), (0.2114209512, -0.038153077), (0.2124039692, -0.0378743982), (0.2133876066, -0.0375841493), (0.2143717562, -0.0372827084), (0.2153563306, -0.0369702532), (0.2163412548, -0.0366468378), (0.217326462, -0.0363124414), (0.2183118879, -0.0359670247), (0.2192974653, -0.0356105907), (0.2202831205, -0.0352432189), (0.2212687764, -0.0348650326), (0.2222543544, -0.0344761788), (0.2232397769, -0.0340768049), (0.2242249689, -0.0336670336), (0.2252098598, -0.0332469486), (0.2261943821, -0.03281661), (0.2271784698, -0.0323760618), (0.2281620578, -0.0319253438), (0.2291450806, -0.0314645015), (0.2301274718, -0.0309935938), (0.2311091647, -0.030512686), (0.2320900927, -0.0300218464), (0.2330701903, -0.0295211426), (0.2340493933, -0.0290106363), (0.2350276391, -0.0284903809), (0.2360048664, -0.0279604246), (0.2369810139, -0.0274208116), (0.23795602, -0.0268715846), (0.2389298224, -0.0263127866), (0.239902357, -0.0257444628), (0.2408735601, -0.025166659), (0.2418433689, -0.0245794207), (0.2428117226, -0.0239827924), (0.243778564, -0.0233768163), (0.2447438397, -0.022761532), (0.2457074976, -0.0221369776), (0.2466694841, -0.0215031899), (0.2476297421, -0.0208602059), (0.248588208, -0.0202080637), (0.2495448104, -0.0195468028), (0.2504994755, -0.0188764631), (0.251452133, -0.0181970839), (0.2524027202, -0.0175087024), (0.2533511885, -0.016811353), (0.2542975076, -0.0161050662), (0.2552416608, -0.0153898673), (0.2559952454, -0.0148105941), (0.2565594559, -0.014372143), (0.2569351617, -0.0140780668), (0.257122906, -0.0139305849)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.2575, -3.1011789143, 6.2023578287)
                _nurbs_edge([(0.1892732289, 0.0405903415), (0.1894565297, 0.0406289422), (0.1898240991, 0.0406995381), (0.190378356, 0.0407856155), (0.191122948, 0.0408626219), (0.1920616827, 0.0409068032), (0.1930067151, 0.0409127713), (0.1939563195, 0.0408942733), (0.1949091148, 0.040861672), (0.1958643946, 0.0408190888), (0.1968219211, 0.040766382), (0.1977817555, 0.0407008128), (0.1987440791, 0.0406187759), (0.1997090078, 0.0405176168), (0.2006764429, 0.0403970712), (0.2016461544, 0.0402583724), (0.2026178386, 0.0401036224), (0.2035911821, 0.0399350908), (0.2045659292, 0.0397544792), (0.2055419297, 0.0395624007), (0.2065191007, 0.039358787), (0.2074974007, 0.0391431586), (0.2084768007, 0.0389149327), (0.2094572532, 0.0386737507), (0.2104386727, 0.0384196879), (0.2114209512, 0.038153077), (0.2124039692, 0.0378743982), (0.2133876066, 0.0375841493), (0.2143717562, 0.0372827084), (0.2153563306, 0.0369702532), (0.2163412548, 0.0366468378), (0.217326462, 0.0363124414), (0.2183118879, 0.0359670247), (0.2192974653, 0.0356105907), (0.2202831205, 0.0352432189), (0.2212687764, 0.0348650326), (0.2222543544, 0.0344761788), (0.2232397769, 0.0340768049), (0.2242249689, 0.0336670336), (0.2252098598, 0.0332469486), (0.2261943821, 0.03281661), (0.2271784698, 0.0323760618), (0.2281620578, 0.0319253438), (0.2291450806, 0.0314645015), (0.2301274718, 0.0309935938), (0.2311091647, 0.030512686), (0.2320900927, 0.0300218464), (0.2330701903, 0.0295211426), (0.2340493933, 0.0290106363), (0.2350276391, 0.0284903809), (0.2360048664, 0.0279604246), (0.2369810139, 0.0274208116), (0.23795602, 0.0268715846), (0.2389298224, 0.0263127866), (0.239902357, 0.0257444628), (0.2408735601, 0.025166659), (0.2418433689, 0.0245794207), (0.2428117226, 0.0239827924), (0.243778564, 0.0233768163), (0.2447438397, 0.022761532), (0.2457074976, 0.0221369776), (0.2466694841, 0.0215031899), (0.2476297421, 0.0208602059), (0.248588208, 0.0202080637), (0.2495448104, 0.0195468028), (0.2504994755, 0.0188764631), (0.251452133, 0.0181970839), (0.2524027202, 0.0175087024), (0.2533511885, 0.016811353), (0.2542975076, 0.0161050662), (0.2552416608, 0.0153898673), (0.2559952454, 0.0148105941), (0.2565594559, 0.014372143), (0.2569351617, 0.0140780668), (0.257122906, 0.0139305849)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.1350494201, 0.029171532), (0.1892732289, 0.0405903415))
                Line((0.1350494201, -0.029171532), (0.1350494201, 0.029171532))
                Line((0.1350494201, -0.029171532), (0.1892732289, -0.0405903415))
            make_face()
        # OneSide extrude, distance=0.323
        extrude(amount=0.323, mode=Mode.ADD)
    return part.part


# Description: This is a circular fan or impeller wheel featuring a large flat disk face with a central hub protrusion, surrounded by a perforated or mesh-textured rim band on the outer edge.
def model_135092_c3610d5c_0008():
    """Model: Spur Gear (27 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 1.2090383416, perimeter: 4.5764836822
            with BuildLine():
                CenterArc((0, 0), 0.62837, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.168
        extrude(amount=0.168)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0094671502, perimeter: 0.3813472009
            with BuildLine():
                _nurbs_edge([(0.6515773822, -0.0477035531), (0.6518473038, -0.0477225533), (0.6523873267, -0.0477542919), (0.6531979004, -0.0477831152), (0.6542797227, -0.0477857312), (0.6556336325, -0.0477395225), (0.6569889934, -0.0476569214), (0.6583456023, -0.0475509701), (0.6597032614, -0.0474316707), (0.6610618049, -0.0473032014), (0.6624210948, -0.0471656673), (0.6637810173, -0.0470166701), (0.6651414799, -0.0468529169), (0.6665024076, -0.0466718703), (0.66786374, -0.0464732089), (0.6692254276, -0.0462580642), (0.6705874286, -0.0460284168), (0.6719497062, -0.0457864469), (0.6733122246, -0.0455338715), (0.6746749464, -0.0452713868), (0.676037834, -0.0449990166), (0.67740085, -0.0447163736), (0.6787639586, -0.0444229467), (0.6801271258, -0.0441183946), (0.6814903211, -0.0438027833), (0.682853516, -0.0434764349), (0.6842166836, -0.0431398198), (0.6855797983, -0.0427934366), (0.6869428349, -0.0424376884), (0.6883057682, -0.042072787), (0.6896685731, -0.0416988196), (0.6910312249, -0.0413157965), (0.6923936993, -0.0409237034), (0.6937559729, -0.0405225564), (0.6951180227, -0.0401124437), (0.6964798267, -0.0396934971), (0.6978413631, -0.0392658723), (0.6992026107, -0.0388297274), (0.7005635487, -0.0383851997), (0.7019241563, -0.0379323891), (0.703284413, -0.0374713705), (0.7046442986, -0.0370022024), (0.706003793, -0.0365249368), (0.7073628764, -0.0360396297), (0.708721529, -0.0355463484), (0.7100797316, -0.035045167), (0.711437465, -0.0345361619), (0.7127947103, -0.0340194085), (0.714151449, -0.0334949768), (0.715507663, -0.0329629286), (0.7168633343, -0.0324233193), (0.7182184451, -0.0318762004), (0.7195729772, -0.0313216208), (0.7209269125, -0.0307596294), (0.7222802326, -0.0301902766), (0.7236329189, -0.029613613), (0.7249849533, -0.0290296885), (0.7263363182, -0.0284385515), (0.7276869972, -0.0278402477), (0.7290369747, -0.0272348196), (0.7303862359, -0.0266223074), (0.7317347654, -0.0260027502), (0.7330825469, -0.0253761865), (0.734429562, -0.0247426561), (0.7357757903, -0.0241022002), (0.7371212104, -0.0234548603), (0.7384658019, -0.0228006764), (0.7398095466, -0.0221396859), (0.7411524304, -0.0214719223), (0.7424944449, -0.0207974132), (0.7438355854, -0.0201161807), (0.7449077975, -0.019565829), (0.7457115626, -0.0191500514), (0.746247231, -0.0188715272), (0.7465150215, -0.0187319304)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.74675, -1.4373928908, 2.8747857817)
                _nurbs_edge([(0.6515773822, 0.0477035531), (0.6518473038, 0.0477225533), (0.6523873267, 0.0477542919), (0.6531979004, 0.0477831152), (0.6542797227, 0.0477857312), (0.6556336325, 0.0477395225), (0.6569889934, 0.0476569214), (0.6583456023, 0.0475509701), (0.6597032614, 0.0474316707), (0.6610618049, 0.0473032014), (0.6624210948, 0.0471656673), (0.6637810173, 0.0470166701), (0.6651414799, 0.0468529169), (0.6665024076, 0.0466718703), (0.66786374, 0.0464732089), (0.6692254276, 0.0462580642), (0.6705874286, 0.0460284168), (0.6719497062, 0.0457864469), (0.6733122246, 0.0455338715), (0.6746749464, 0.0452713868), (0.676037834, 0.0449990166), (0.67740085, 0.0447163736), (0.6787639586, 0.0444229467), (0.6801271258, 0.0441183946), (0.6814903211, 0.0438027833), (0.682853516, 0.0434764349), (0.6842166836, 0.0431398198), (0.6855797983, 0.0427934366), (0.6869428349, 0.0424376884), (0.6883057682, 0.042072787), (0.6896685731, 0.0416988196), (0.6910312249, 0.0413157965), (0.6923936993, 0.0409237034), (0.6937559729, 0.0405225564), (0.6951180227, 0.0401124437), (0.6964798267, 0.0396934971), (0.6978413631, 0.0392658723), (0.6992026107, 0.0388297274), (0.7005635487, 0.0383851997), (0.7019241563, 0.0379323891), (0.703284413, 0.0374713705), (0.7046442986, 0.0370022024), (0.706003793, 0.0365249368), (0.7073628764, 0.0360396297), (0.708721529, 0.0355463484), (0.7100797316, 0.035045167), (0.711437465, 0.0345361619), (0.7127947103, 0.0340194085), (0.714151449, 0.0334949768), (0.715507663, 0.0329629286), (0.7168633343, 0.0324233193), (0.7182184451, 0.0318762004), (0.7195729772, 0.0313216208), (0.7209269125, 0.0307596294), (0.7222802326, 0.0301902766), (0.7236329189, 0.029613613), (0.7249849533, 0.0290296885), (0.7263363182, 0.0284385515), (0.7276869972, 0.0278402477), (0.7290369747, 0.0272348196), (0.7303862359, 0.0266223074), (0.7317347654, 0.0260027502), (0.7330825469, 0.0253761865), (0.734429562, 0.0247426561), (0.7357757903, 0.0241022002), (0.7371212104, 0.0234548603), (0.7384658019, 0.0228006764), (0.7398095466, 0.0221396859), (0.7411524304, 0.0214719223), (0.7424944449, 0.0207974132), (0.7438355854, 0.0201161807), (0.7449077975, 0.019565829), (0.7457115626, 0.0191500514), (0.746247231, 0.0188715272), (0.7465150215, 0.0187319304)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6256953595, 0.0458816848), (0.6515773822, 0.0477035531))
                Line((0.6256953595, -0.0458816848), (0.6256953595, 0.0458816848))
                Line((0.6256953595, -0.0458816848), (0.6515773822, -0.0477035531))
            make_face()
        # OneSide extrude, distance=0.168
        extrude(amount=0.168, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or connector component with two cubic end sections joined by a central rectangular channel, featuring angled or beveled edges and internal ribbing or structural supports along the top surface.
def model_135205_958cc1f8_0000():
    """Model: Albatros distributors 1/4 scale"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((1, 1), (1, -1))
                Line((3, -1), (1, -1))
                Line((3, 1), (3, -1))
                Line((1, 1), (3, 1))
            make_face()
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, -1), (-3, -1))
                Line((-1, 1), (-1, -1))
                Line((-3, 1), (-1, 1))
                Line((-3, -1), (-3, 1))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7696535211, perimeter: 6.7696535303
            with BuildLine():
                Line((-1.0000000149, -0.6848267398), (-1.0000000149, 0.7000000104))
                Line((1, -0.6848267398), (-1.0000000149, -0.6848267398))
                Line((1, 0.7000000104), (1, -0.6848267398))
                Line((-1.0000000149, 0.7000000104), (1, 0.7000000104))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a curved duct or air channel component with a serpentine S-shape, featuring a hollow interior cavity with mesh/lattice patterning on the upper surface and a solid lower base with a mounting flange on one end.
def model_135278_8675dea7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 34.8700221759, perimeter: 38.8700221759
            with BuildLine():
                Line((14.6, 2), (17, 2))
                Line((17, 2), (17, 4))
                Line((14.6, 4), (17, 4))
                CenterArc((14.6, -3), 7, 90, 36.8698976458)
                CenterArc((8.6, 5), 3, -90, 36.8698976458)
                Line((0, 2), (8.6, 2))
                Line((0, 0), (0, 2))
                Line((0, 0), (8.6, 0))
                CenterArc((8.6, 5), 5, -90, 36.8698976458)
                CenterArc((14.6, -3), 5, 90, 36.8698976458)
            make_face()
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True)

        # Sketch1 -> Extrude2 (Intersect)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.8188565401, perimeter: 42.54590436
            with BuildLine():
                Line((8.7678792037, 4), (17, 4))
                Line((17, 4), (17, 7))
                Line((8.7678792037, 7), (17, 7))
                CenterArc((8.7678792037, -1), 8, 90, 53.1301023542)
                CenterArc((0.7678792037, 5), 2, -90.0000479105, 53.1301502647)
                Line((0, 3), (0.7678775313, 3))
                Line((0, 0), (0, 3))
                Line((0, 0), (0.7678837831, 0))
                CenterArc((0.7678792037, 5), 5, -89.9999475233, 53.1300498774)
                CenterArc((8.7678792037, -1), 5, 90, 53.1301023542)
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True, mode=Mode.INTERSECT)
    return part.part


# Description: This is an open-top rectangular bin or container with angled side walls, a recessed interior, and reinforced rim edges, designed for holding or transporting materials.
def model_135443_be53bf45_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.819, perimeter: 3.74
            with BuildLine():
                Line((-0.585, 0.35), (0.585, 0.35))
                Line((-0.585, -0.35), (-0.585, 0.35))
                Line((0.585, -0.35), (-0.585, -0.35))
                Line((0.585, 0.35), (0.585, -0.35))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.414, perimeter: 8.28
            with BuildLine():
                Line((-0.685, 0.45), (-0.685, -0.45))
                Line((-0.685, -0.45), (0.685, -0.45))
                Line((0.685, -0.45), (0.685, 0.45))
                Line((0.685, 0.45), (-0.685, 0.45))
            make_face()
            with BuildLine():
                Line((0.585, 0.35), (-0.585, 0.35))
                Line((0.585, -0.35), (0.585, 0.35))
                Line((-0.585, -0.35), (0.585, -0.35))
                Line((-0.585, 0.35), (-0.585, -0.35))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a cylindrical capsule or rounded-end tank with a symmetrical shape featuring two hemispherical end caps connected to a central cylindrical body, commonly used for pressure vessels or storage containers.
def model_135460_6471e973_0001():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 40.5366009152, perimeter: 22.5698460461
            Circle(3.5921025631)
        # TwoSides extrude, along=-4.318, against=6.096
        extrude(amount=-4.318)
        extrude(sk.sketch, amount=6.096)
    return part.part


# Description: This is a cylindrical sleeve or tube with a tapered conical top end, featuring a hollow interior and smooth curved surfaces throughout its length.
def model_135892_ab8f21bf_0003():
    """Model: Pin Lever"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, full_length=True, total=2.4
        extrude(amount=1.2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2933698066, perimeter: 2.3492343031
            with BuildLine():
                CenterArc((0, 0), 0.5, 101.5369590328, 156.9260819344)
                Line((-0.1, -0.4898979486), (-0.1, 0.4898979486))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular box or container with an open top, featuring a hinged or removable lid with multiple rectangular slots or vents across its upper surface, and a trapezoidal side panel with diagonal reinforcing ribs.
def model_136129_9b1934a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.4, perimeter: 11.2
            with BuildLine():
                Line((0, 0.0075768625), (0, 1.6))
                Line((0, 0.0075768625), (0, 0))
                Line((0, 0), (3.9936714895, 0))
                Line((3.9936714895, 0), (4, 0))
                Line((4, 0), (4, 1.6))
                Line((0, 1.6), (4, 1.6))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5150029712, 0.55)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5150029712, 1.45)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.2150029712, 1.45)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.2150029712, 0.55)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.9150029712, 1.45)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.9150029712, 0.55)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.6150029712, 1.45)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.6150029712, 0.55)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-3.3150029712, 1.45)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-3.3150029712, 0.55)):
                Circle(0.25)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: A cylindrical sleeve or tube with a tapered, cone-shaped top end and a flat base, featuring vertical ribbing or fluting along its sides.
def model_136206_f765760a_0000():
    """Model: Pin-lever"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2933698066, perimeter: 2.3492343031
            with BuildLine():
                CenterArc((0, 0), 0.5, 101.5369590328, 156.9260819344)
                Line((-0.1, -0.4898979486), (-0.1, 0.4898979486))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a T-shaped connector or junction piece with three cylindrical ports of equal diameter extending perpendicular to each other, featuring a central body with what appears to be internal passages or threaded holes for joining multiple components.
def model_136206_f765760a_0001():
    """Model: Cross"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, full_length=True, total=4
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, full_length=True, total=4
        extrude(amount=2, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling sleeve with a hexagonal or polygonal cross-section, featuring a flange on one end and a mesh or perforated surface on the top, designed for joining or coupling applications.
def model_136239_e80b9e8e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0639781258, perimeter: 1.0097516708
            with BuildLine():
                Line((-0.254, 5.0736460263), (-0.254, 4.826000154))
                Line((0, 4.826000154), (-0.254, 4.826000154))
                Line((0, 5.08), (0, 4.826000154))
                CenterArc((0, 0), 5.08, 90, 2.8659839826)
            make_face()
            # Profile area: 0.1946237516, perimeter: 1.7909201772
            with BuildLine():
                Line((-0.254, 5.0736460263), (-0.254, 5.461000154))
                CenterArc((0, 0), 5.08, 90, 2.8659839826)
                CenterArc((0, 0), 5.08, 87.1340159259, 2.8659840741)
                Line((0.2540000081, 5.0736460259), (0.2540000081, 5.461000154))
                Line((-0.254, 5.461000154), (0.2540000081, 5.461000154))
            make_face()
            # Profile area: 0.0639781278, perimeter: 1.0097516866
            with BuildLine():
                Line((0, 5.08), (0, 4.826000154))
                Line((0, 4.826000154), (0.2540000081, 4.826000154))
                Line((0.2540000081, 4.826000154), (0.2540000081, 5.0736460259))
                CenterArc((0, 0), 5.08, 87.1340159259, 2.8659840741)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0063646344, perimeter: 0.6149433284
            with BuildLine():
                CenterArc((0.0817853892, 5.2887855352), 0.1722146189, 0, 90)
                Line((0.2540000081, 5.3086000459), (0.2540000081, 5.2887855352))
                Line((0.2540000081, 5.461000154), (0.2540000081, 5.3086000459))
                Line((0.0817853892, 5.461000154), (0.2540000081, 5.461000154))
            make_face()
            # Profile area: 0.0063646344, perimeter: 0.6149433284
            with BuildLine():
                CenterArc((-0.0817853811, 5.2887855352), 0.1722146189, 90, 90)
                Line((-0.254, 5.461000154), (-0.0817853811, 5.461000154))
                Line((-0.254, 5.461000154), (-0.254, 5.3086000459))
                Line((-0.254, 5.3086000459), (-0.254, 5.2887855352))
            make_face()
        # OneSide extrude, distance=-0.7112
        extrude(amount=-0.7112, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a compact solar panel assembly featuring a rectangular blue photovoltaic panel with internal geometric segments and a protruding cylindrical antenna or communication rod mounted at an angle from the upper surface.
def model_136322_81d84c1b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 126, perimeter: 46
            with BuildLine():
                Line((14, -9), (0, -9))
                Line((14, 0), (14, -9))
                Line((0, 0), (14, 0))
                Line((0, -9), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-13, 4.5)):
                Circle(0.25)
        # OneSide extrude, distance=11
        extrude(amount=11)
    return part.part


# Description: This is a dual-cylinder connector or manifold block featuring two cylindrical ports with mesh-textured ends on either side of a central rectangular body with a slot or groove running through the top surface.
def model_136594_1f36c7d3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((3, -4)):
                Circle(2)
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((13, -4)):
                Circle(2)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8.2362347037, perimeter: 66.7026860182
            with BuildLine():
                Line((13, 6.2309155946), (13.2967185349, 6.2303493249))
                Line((12.7117965736, 6.2314656137), (13, 6.2309155946))
                Line((3.0085879512, 6.2499836104), (12.7117965736, 6.2314656137))
                Line((3, 6.25), (3.0085879512, 6.2499836104))
                CenterArc((3, 4), 2.25, 90, 178.7981216552)
                Line((2.952805809, 1.7504950082), (3, 1.750492683))
                Line((3, 1.750492683), (3.0469725309, 1.7504903687))
                Line((3.0469725309, 1.7504903687), (12.9998891457, 1.7500000027))
                CenterArc((13, 4), 2.25, -90.0028228811, 172.4248735532)
            make_face()
            with BuildLine():
                CenterArc((13, 4), 2, -90, 180)
                Line((13, 2), (3, 2))
                CenterArc((3, 4), 2, -180, 90)
                CenterArc((3, 4), 2, 90, 90)
                Line((3, 6), (13, 6))
            make_face(mode=Mode.SUBTRACT)
        # Start offset: -1 (not directly supported, may affect result)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)
    return part.part


# Description: This is a curved composite bracket or mounting clamp with an organic, asymmetrical shape featuring a solid curved base that tapers to a flat upper section with geometric surface facets and what appears to be mounting holes or attachment points.
def model_136617_c41e239f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7702761426, perimeter: 8.0934237669
            with BuildLine():
                CenterArc((0, 0), 0.9, -35.8376529543, 125.8376529543)
                CenterArc((2.5196575001, -2.0422332235), 2.3452876989, 93.3902817486, 46.3614753969)
                CenterArc((2.4164463241, -0.3), 0.6, 90, 3.3902817486)
                Line((3, 0.3), (2.4164463241, 0.3))
                Line((3, 0.9), (3, 0.3))
                Line((0, 0.9), (3, 0.9))
            make_face()
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.9, 90, 234.1623470457)
                CenterArc((0, 0), 0.9, -35.8376529543, 125.8376529543)
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1540221288, perimeter: 1.7657458002
            with BuildLine():
                CenterArc((0, 0), 0.9, -13.3079981996, 26.1909194887)
                Line((0.8758320746, -0.2071670272), (1.3000000194, -0.2071670272))
                Line((1.3000000194, -0.2071670272), (1.3000000194, -0.09148633))
                CenterArc((1.3000000194, -0.0035835121), 0.0879028179, 90, 180)
                Line((1.3000000194, 0.0843193058), (1.3000000194, 0.200000003))
                Line((1.3000000194, 0.200000003), (0.8773449275, 0.2006635946))
            make_face()
            # Profile area: 0.0529662189, perimeter: 1.1470927167
            with BuildLine():
                Line((1.3000000194, 0.0843193058), (1.3000000194, 0.200000003))
                CenterArc((1.3000000194, -0.0035835121), 0.0879028179, -90, 180)
                Line((1.3000000194, -0.2071670272), (1.3000000194, -0.09148633))
                CenterArc((1.3000000194, -0.0035835121), 0.2035835151, -90, 180)
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical ring or collar with an elliptical cross-section, featuring a mesh or perforated pattern on the upper curved surface and solid bands on the lower portions, with an open interior cavity.
def model_136627_98da0c2f_0002():
    """Model: Tire v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8428439415, perimeter: 70.7794541668
            with BuildLine():
                CenterArc((0, 0), 5.715, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.5499, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 57.0395542145, perimeter: 57.2140570886
            with BuildLine():
                CenterArc((0, 0), 5.5499, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.556, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.794
        extrude(amount=2.794)
    return part.part


# Description: This is a bent metal bracket or channel with a elongated rectangular main body and two perpendicular flanges at each end, featuring a hollow U-shaped cross-section designed for structural support or mounting applications.
def model_136640_16741d62_0001():
    """Model: onderstel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21250, perimeter: 670
            with BuildLine():
                Line((125, -42.5), (-125, -42.5))
                Line((125, 42.5), (125, -42.5))
                Line((-125, 42.5), (125, 42.5))
                Line((-125, -42.5), (-125, 42.5))
            make_face()
        # OneSide extrude, distance=32
        extrude(amount=32)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 42.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5104, perimeter: 508
            with BuildLine():
                Line((116, 0), (116, 22))
                Line((116, 22), (-116, 22))
                Line((-116, 22), (-116, 0))
                Line((-116, 0), (116, 0))
            make_face()
            # Profile area: 4176.0052821615, perimeter: 500.0000455359
            with BuildLine():
                Line((-116, 0), (116, 0))
                Line((-116, 0), (-116, -18.0000227679))
                Line((-116, -18.0000227679), (116, -18.0000227679))
                Line((116, -18.0000227679), (116, 0))
            make_face()
        # OneSide extrude, distance=-140
        extrude(amount=-140, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a structural bracket or support arm with an angular, bent shape featuring a hollow triangulated upper section and solid base flanges, designed for load-bearing applications with internal ribbing for reinforcement.
def model_136640_16741d62_0002():
    """Model: hoek"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12755.8641506929, perimeter: 470.1379800163
            with BuildLine():
                Line((-125, 42.5), (-210, 42.5))
                Line((-210, 42.5), (-210, -107.5689900082))
                Line((-210, -107.5689900082), (-125, -107.5689900082))
                Line((-125, -107.5689900082), (-125, -42.5))
                Line((-125, 42.5), (-125, -42.5))
            make_face()
        # OneSide extrude, distance=32
        extrude(amount=32)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-125, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2861.5177801793, perimeter: 304.1379800163
            with BuildLine():
                Line((32.5, 0), (32.5, 22))
                Line((-42.5, 22), (32.5, 22))
                Line((-42.5, 22), (-97.5689900082, 22))
                Line((-97.5689900082, 22), (-97.5689900082, 0))
                Line((-97.5689900082, 0), (32.5, 0))
            make_face()
        # OneSide extrude, distance=-130
        extrude(amount=-130, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a 3D-printed or molded organic-shaped bracket or connector featuring a rounded, curved body with a flat top surface and an angled upper flange, designed to provide structural support or mounting functionality.
def model_136688_ae3c4ae7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2080892808, perimeter: 6.7404983418
            with BuildLine():
                CenterArc((0, 0), 0.9, -23.1971895786, 113.318585307)
                CenterArc((1.9017309945, -0.8149725299), 1.169, 90.1213957284, 66.681414693)
                Line((2.474252881, 0.3552431295), (1.8992541716, 0.3540248462))
                Line((2.4730875665, 0.905241895), (2.474252881, 0.3552431295))
                Line((-0.0019068782, 0.8999979799), (2.4730875665, 0.905241895))
            make_face()
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.9, 90.1213957284, 246.681414693)
                CenterArc((0, 0), 0.9, -23.1971895786, 113.318585307)
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1025299013, perimeter: 2.5561638929
            with BuildLine():
                CenterArc((0, 0), 0.9, 167.1604115931, 25.6791768138)
                Line((-0.8774964387, 0.2), (-1.1684964387, 0.2))
                CenterArc((-1.1684964387, 0), 0.2, 90, 180)
                Line((-0.8774964387, -0.2), (-1.1684964387, -0.2))
            make_face()
            with BuildLine():
                CenterArc((-1.1684964387, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a pair of elongated rectangular troughs or channels with angled side walls, featuring triangulated internal bracing and tapered end sections, designed as a modular or stackable component system.
def model_136716_076bbbb3_0000():
    """Model: PCB Ribbon Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.84, perimeter: 5
            with BuildLine():
                Line((2.1, -0.4), (0, -0.4))
                Line((2.1, 0), (2.1, -0.4))
                Line((0, 0), (2.1, 0))
                Line((0, -0.4), (0, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.735000011, perimeter: 4.9000000626
            with BuildLine():
                Line((2.1000000313, -0.8500000075), (0, -0.8500000075))
                Line((2.1000000313, -0.5000000075), (2.1000000313, -0.8500000075))
                Line((0, -0.5000000075), (2.1000000313, -0.5000000075))
                Line((0, -0.8500000075), (0, -0.5000000075))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a parallelogram-shaped window frame or skylight component with a dark gray border frame and two blue-tinted glass panes separated by an internal divider, designed for roof or sloped surface installation.
def model_136716_076bbbb3_0004():
    """Model: PCB Board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8743362939, perimeter: 12.3132741229
            with BuildLine():
                Line((2.5, -2.4), (0, -2.4))
                Line((2.5, 0), (2.5, -2.4))
                Line((0, 0), (2.5, 0))
                Line((0, -2.4), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((2.3000000343, -1.6000000238), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.200000003, -1.6), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3000000343, -0.200000003), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.200000003, -0.200000003), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a long, narrow rectangular duct or channel with a trapezoidal cross-section, featuring a small rectangular flange or bracket protruding from the left end and curved or angled sides that taper slightly toward the right, likely designed for air/fluid flow or as a structural component.
def model_136716_076bbbb3_0008():
    """Model: Ribbon Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.735, perimeter: 4.9
            with BuildLine():
                Line((2.1, -0.35), (0, -0.35))
                Line((2.1, 0), (2.1, -0.35))
                Line((0, 0), (2.1, 0))
                Line((0, -0.35), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.24, perimeter: 9.6
            with BuildLine():
                Line((-0.05, 0.25), (-0.05, -0.05))
                Line((-0.05, -0.05), (2.15, -0.05))
                Line((2.15, -0.05), (2.15, 0.25))
                Line((2.15, 0.25), (-0.05, 0.25))
            make_face()
            with BuildLine():
                Line((2.1, 0.2), (0, 0.2))
                Line((2.1, 0), (2.1, 0.2))
                Line((0, 0), (2.1, 0))
                Line((0, 0.2), (0, 0))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.42, perimeter: 4.6
            with BuildLine():
                Line((0, 0.2), (0, 0))
                Line((0, 0), (2.1, 0))
                Line((2.1, 0), (2.1, 0.2))
                Line((2.1, 0.2), (0, 0.2))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped structural component with a elongated rectangular body, featuring angled end faces and internal geometric divisions visible through its transparent wireframe representation.
def model_136745_de48e6a0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1635.0936083657, perimeter: 1072.8960342407
            with BuildLine():
                Line((213.3600068092, 30.4800009727), (0, 30.4800009727))
                Line((0, 30.4800009727), (0, -30.4800009727))
                Line((0, -30.4800009727), (213.3600068092, -30.4800009727))
                Line((213.3600068092, -30.4800009727), (213.3600068092, 30.4800009727))
            make_face()
            with BuildLine():
                Line((210.312006712, -27.4320008755), (3.0480000973, -27.4320008755))
                Line((3.0480000973, -27.4320008755), (3.0480000973, 27.4320008755))
                Line((3.0480000973, 27.4320008755), (207.2640066147, 27.4320008755))
                Line((207.2640066147, 27.4320008755), (210.312006712, 27.4320008755))
                Line((210.312006712, 27.4320008755), (210.312006712, -27.4320008755))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=91.44
        extrude(amount=91.44)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11371.3328218162, perimeter: 524.2560167313
            with BuildLine():
                Line((3.0480000973, 27.4320008755), (3.0480000973, -27.4320008755))
                Line((3.0480000973, -27.4320008755), (210.312006712, -27.4320008755))
                Line((210.312006712, -27.4320008755), (210.312006712, 27.4320008755))
                Line((3.0480000973, 27.4320008755), (210.312006712, 27.4320008755))
            make_face()
        # OneSide extrude, distance=0.0003048
        extrude(amount=0.0003048, mode=Mode.ADD)
    return part.part


# Description: This is a circular lens cap or cover featuring a flat circular body with a textured knurled rim around the perimeter and a small protruding tab or grip on the edge for easy removal.
def model_136795_e6ced33d_0001():
    """Model: Spur Gear (24 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 14.588551622, perimeter: 13.5397616821
            Circle(2.15492)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1349255767, perimeter: 1.4339193394
            with BuildLine():
                _nurbs_edge([(2.2479853152, -0.1810249127), (2.2489932449, -0.181105278), (2.2510097809, -0.1812409099), (2.2540366139, -0.1813690624), (2.258076319, -0.181396655), (2.2631317102, -0.1812348102), (2.2681918052, -0.1809307277), (2.2732554668, -0.1805379479), (2.2783216732, -0.1800965105), (2.2833896885, -0.1796220691), (2.2884589897, -0.1791138378), (2.2935292136, -0.1785610664), (2.2986000975, -0.1779498181), (2.3036714193, -0.1772701815), (2.308742949, -0.1765215787), (2.3138144607, -0.1757091396), (2.3188857357, -0.1748412793), (2.323956569, -0.1739269493), (2.3290267747, -0.1729727055), (2.33409619, -0.171980877), (2.3391646687, -0.1709512046), (2.3442320777, -0.169881883), (2.3492982919, -0.1687707658), (2.3543631896, -0.1676166686), (2.3594266494, -0.166420078), (2.3644885518, -0.1651824457), (2.3695487802, -0.1639057631), (2.3746072218, -0.1625920577), (2.3796637686, -0.1612428441), (2.384718318, -0.1598588629), (2.3897707717, -0.1584403884), (2.3948210349, -0.1569874149), (2.3998690151, -0.1554998769), (2.4049146216, -0.1539778908), (2.4099577648, -0.1524218627), (2.4149983564, -0.1508323589), (2.4200363098, -0.1492100297), (2.4250715399, -0.1475555176), (2.4301039639, -0.1458693576), (2.4351335006, -0.1441519348), (2.4401600707, -0.1424035407), (2.4451835962, -0.1406244077), (2.4502039999, -0.1388147498), (2.4552212055, -0.1369748074), (2.4602351375, -0.1351048673), (2.465245721, -0.1332052394), (2.4702528825, -0.1312762421), (2.4752565495, -0.1293181863), (2.4802566513, -0.1273313572), (2.485253119, -0.1253160063), (2.4902458842, -0.1232723622), (2.4952348791, -0.1212006377), (2.5002200356, -0.119101038), (2.5052012847, -0.1169737697), (2.5101785566, -0.1148190458), (2.5151517817, -0.1126370798), (2.5201208921, -0.1104280819), (2.5250858225, -0.108192255), (2.5300465117, -0.1059297901), (2.535002903, -0.1036408647), (2.5399549411, -0.1013256478), (2.5449025688, -0.0989843039), (2.5498457252, -0.0966169983), (2.5547843416, -0.0942239014), (2.5597183409, -0.0918051925), (2.5646476439, -0.0893610511), (2.5695721751, -0.0868916507), (2.5744918688, -0.0843971514), (2.5794066751, -0.0818776935), (2.5843165655, -0.0793333911), (2.5892215267, -0.0767643324), (2.5931415498, -0.0746893307), (2.5960793488, -0.0731219842), (2.5980368958, -0.0720721569), (2.5990154229, -0.0715460109)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.6, -1.576846918, 3.1536938361)
                _nurbs_edge([(2.2479853152, 0.1810249127), (2.2489932449, 0.181105278), (2.2510097809, 0.1812409099), (2.2540366139, 0.1813690624), (2.258076319, 0.181396655), (2.2631317102, 0.1812348102), (2.2681918052, 0.1809307277), (2.2732554668, 0.1805379479), (2.2783216732, 0.1800965105), (2.2833896885, 0.1796220691), (2.2884589897, 0.1791138378), (2.2935292136, 0.1785610664), (2.2986000975, 0.1779498181), (2.3036714193, 0.1772701815), (2.308742949, 0.1765215787), (2.3138144607, 0.1757091396), (2.3188857357, 0.1748412793), (2.323956569, 0.1739269493), (2.3290267747, 0.1729727055), (2.33409619, 0.171980877), (2.3391646687, 0.1709512046), (2.3442320777, 0.169881883), (2.3492982919, 0.1687707658), (2.3543631896, 0.1676166686), (2.3594266494, 0.166420078), (2.3644885518, 0.1651824457), (2.3695487802, 0.1639057631), (2.3746072218, 0.1625920577), (2.3796637686, 0.1612428441), (2.384718318, 0.1598588629), (2.3897707717, 0.1584403884), (2.3948210349, 0.1569874149), (2.3998690151, 0.1554998769), (2.4049146216, 0.1539778908), (2.4099577648, 0.1524218627), (2.4149983564, 0.1508323589), (2.4200363098, 0.1492100297), (2.4250715399, 0.1475555176), (2.4301039639, 0.1458693576), (2.4351335006, 0.1441519348), (2.4401600707, 0.1424035407), (2.4451835962, 0.1406244077), (2.4502039999, 0.1388147498), (2.4552212055, 0.1369748074), (2.4602351375, 0.1351048673), (2.465245721, 0.1332052394), (2.4702528825, 0.1312762421), (2.4752565495, 0.1293181863), (2.4802566513, 0.1273313572), (2.485253119, 0.1253160063), (2.4902458842, 0.1232723622), (2.4952348791, 0.1212006377), (2.5002200356, 0.119101038), (2.5052012847, 0.1169737697), (2.5101785566, 0.1148190458), (2.5151517817, 0.1126370798), (2.5201208921, 0.1104280819), (2.5250858225, 0.108192255), (2.5300465117, 0.1059297901), (2.535002903, 0.1036408647), (2.5399549411, 0.1013256478), (2.5449025688, 0.0989843039), (2.5498457252, 0.0966169983), (2.5547843416, 0.0942239014), (2.5597183409, 0.0918051925), (2.5646476439, 0.0893610511), (2.5695721751, 0.0868916507), (2.5744918688, 0.0843971514), (2.5794066751, 0.0818776935), (2.5843165655, 0.0793333911), (2.5892215267, 0.0767643324), (2.5931415498, 0.0746893307), (2.5960793488, 0.0731219842), (2.5980368958, 0.0720721569), (2.5990154229, 0.0715460109)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((2.1469700228, 0.1729706592), (2.2479853152, 0.1810249127))
                Line((2.1469700228, -0.1729706592), (2.1469700228, 0.1729706592))
                Line((2.1469700228, -0.1729706592), (2.2479853152, -0.1810249127))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a stepped cylindrical connector or adapter featuring two coaxial cylinders of different diameters with a flanged shoulder junction, designed to connect or transition between two different-sized circular components.
def model_136804_e0013c2b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or tube component with an elongated body, featuring a rounded left end, a tapered right end with an angular face, and internal longitudinal slots or channels running along its length.
def model_136864_161ce067_0004():
    """Model: motor v1 (2)"""
    with BuildPart() as part:
        # Sketch8 -> Extrude12 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2276389414, perimeter: 1.9939822696
            with BuildLine():
                CenterArc((-0.280000006, 0.280000006), 0.12, 90, 90)
                Line((-0.400000006, 0.280000006), (-0.400000006, 0.2200000015))
                CenterArc((-0.280000006, 0.2200000015), 0.12, 180, 90)
                Line((-0.280000006, 0.1000000015), (0.280000006, 0.1000000015))
                CenterArc((0.280000006, 0.2200000015), 0.12, -90, 90)
                Line((0.400000006, 0.2200000015), (0.400000006, 0.280000006))
                CenterArc((0.280000006, 0.280000006), 0.12, 0, 90)
                Line((0.280000006, 0.400000006), (-0.280000006, 0.400000006))
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2)
    return part.part


# Description: This is a rectangular enclosure or base plate with a sloped/angled top surface, featuring a recessed channel or slot along one edge and internal mounting features visible through transparent surfaces.
def model_136885_b23ae817_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7256637318, perimeter: 34.8566370495
            with BuildLine():
                CenterArc((2.8, -1.3), 0.2, -90, 90)
                Line((3, 1.3), (3, -1.3))
                CenterArc((2.8, 1.3), 0.2, 0, 90)
                Line((-2.8, 1.5), (2.8, 1.5))
                CenterArc((-2.8, 1.3), 0.2, 90, 90)
                Line((-3, -1.3), (-3, 1.3))
                CenterArc((-2.8, -1.3), 0.2, 180, 90)
                Line((2.8, -1.5), (-2.8, -1.5))
            make_face()
            with BuildLine():
                Line((-2.8999999985, -1.3999999985), (-2.8999999985, 1.3999999985))
                Line((-2.8999999985, 1.3999999985), (2.8999999985, 1.3999999985))
                Line((2.8999999985, 1.3999999985), (2.8999999985, -1.3999999985))
                Line((2.8999999985, -1.3999999985), (-2.8999999985, -1.3999999985))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 16.2399999744, perimeter: 17.1999999881
            with BuildLine():
                Line((2.8999999985, -1.3999999985), (-2.8999999985, -1.3999999985))
                Line((2.8999999985, 1.3999999985), (2.8999999985, -1.3999999985))
                Line((-2.8999999985, 1.3999999985), (2.8999999985, 1.3999999985))
                Line((-2.8999999985, -1.3999999985), (-2.8999999985, 1.3999999985))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.2399999744, perimeter: 17.1999999881
            with BuildLine():
                Line((2.8999999985, -1.3999999985), (-2.8999999985, -1.3999999985))
                Line((2.8999999985, 1.3999999985), (2.8999999985, -1.3999999985))
                Line((-2.8999999985, 1.3999999985), (2.8999999985, 1.3999999985))
                Line((-2.8999999985, -1.3999999985), (-2.8999999985, 1.3999999985))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or deflector with a trapezoidal base plate featuring an internal triangular reinforcement rib and a perpendicular mounting flange on one end.
def model_136900_4fe212e6_0016():
    """Model: CornerShelf v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4164.2509209025, perimeter: 273.5782267006
            with BuildLine():
                Line((0, 0), (-71.12, 0))
                Line((-71.12, 0), (-71.12, -45.72))
                Line((-55.88, -45.72), (-71.12, -45.72))
                CenterArc((-55.88, -71.12), 25.4, 0, 90)
                Line((0, -71.12), (-30.48, -71.12))
                Line((0, 0), (0, -71.12))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.064399128, perimeter: 64.7699990845
            with BuildLine():
                Line((30.4799995422, 69.215), (0, 69.215))
                Line((30.48, 71.12), (30.4799995422, 69.215))
                Line((0, 71.12), (30.48, 71.12))
                Line((0, 69.215), (0, 71.12))
            make_face()
        # OneSide extrude, distance=4.445
        extrude(amount=4.445, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or support component with a rectangular base flanked by two perpendicular vertical flanges on opposing sides, forming a U-shaped or channel-like structure with open ends.
def model_136900_4fe212e6_0017():
    """Model: Closet Walls v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6460.3548963807, perimeter: 1155.7
            with BuildLine():
                Line((0, 0), (0, 12.065))
                Line((0, 12.065), (-9.525, 12.065))
                Line((-9.525, 12.065), (-9.525, 73.025))
                Line((-9.525, 73.025), (295.91, 73.025))
                Line((295.91, 73.025), (295.91, -80.645))
                Line((307.34, -80.645), (295.91, -80.645))
                Line((307.34, 84.455), (307.34, -80.645))
                Line((-20.6828455513, 84.455), (307.34, 84.455))
                Line((-20.6828455513, 11.43), (-20.6828455513, 84.455))
                Line((-22.86, 11.43), (-20.6828455513, 11.43))
                Line((-22.86, 0), (-22.86, 11.43))
                Line((0, 0), (-22.86, 0))
            make_face()
        # OneSide extrude, distance=225.425
        extrude(amount=225.425)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 225.425, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3476.202725, perimeter: 615.3156813297
            with BuildLine():
                Line((-295.91, 0), (-295.91, -11.43))
                Line((-295.91, -11.43), (0, -12.065))
                Line((0, -12.065), (0, 0))
                Line((0, 0), (-295.91, 0))
            make_face()
        # OneSide extrude, distance=-19.05
        extrude(amount=-19.05, mode=Mode.ADD)
    return part.part


# Description: This is a torus-shaped ring or band with a circular cross-section, featuring a smooth, curved geometry with a hollow center and textured or mesh-patterned surface on the outer edges.
def model_136925_70fb0381_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 493.1043829075, perimeter: 205.4601595448
            with BuildLine():
                CenterArc((0, 0), 18.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 13.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2578365147, perimeter: 4.5792859598
            with BuildLine():
                CenterArc((3.4593843741, -16.3888730471), 0.9, 13.458577331, 176.9210503472)
                CenterArc((0, 0), 16.75, -81.1598471483, 6.1578993056)
            make_face()
            # Profile area: 1.2868535347, perimeter: 4.6760140159
            with BuildLine():
                CenterArc((0, 0), 16.75, -81.1598471483, 6.1578993056)
                CenterArc((3.4593843741, -16.3888730471), 0.9, -169.6203723219, 183.0789496528)
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or trapezoidal prismatic housing or container with a segmented, faceted design featuring triangulated surface panels, a recessed or stepped interior geometry, and appears to be a complex molded or fabricated structural component with multiple internal compartments or features.
def model_136994_a3a2f50f_0001():
    """Model: body"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 122.28, perimeter: 154.4
            with BuildLine():
                Line((3, -1.25), (3, 11.25))
                Line((3, 11.25), (-27, 11.25))
                Line((-27, 11.25), (-27, -1.25))
                Line((-27, -1.25), (3, -1.25))
            make_face()
            with BuildLine():
                Line((0, 0), (0, 10.4))
                Line((-24.3, 0), (0, 0))
                Line((-24.3, 10.4), (-24.3, 0))
                Line((0, 10.4), (-24.3, 10.4))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 252.4686725877, perimeter: 71.9132741229
            with BuildLine():
                Line((0, 10.4), (-24.3, 10.4))
                Line((-24.3, 10.4), (-24.3, 0))
                Line((-24.3, 0), (0, 0))
                Line((0, 0), (0, 10.4))
            make_face()
            with BuildLine():
                CenterArc((-0.9968397148, 5.2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-23.3013590808, 5.2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.9968397148, 5.2)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-23.3013590808, 5.2)):
                Circle(0.2)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -11.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 408, perimeter: 83
            with BuildLine():
                Line((-0.75, 18), (24.75, 18))
                Line((-0.75, 2), (-0.75, 18))
                Line((24.75, 2), (-0.75, 2))
                Line((24.75, 18), (24.75, 2))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a curved, oval-shaped enclosure or housing with a dark gray body featuring multiple rectangular slot openings or vents across its top surface and blue mesh or perforated panels visible through cutouts, suggesting ventilation or cooling functionality.
def model_137098_0a45d1c8_0001():
    """Model: Hub"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4013548846, perimeter: 10.8384946549
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.5, 0.5), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, 0.5), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.5, -0.5), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, -0.5), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cubic or hexagonal structural frame assembly with an open lattice design, featuring dark metal struts forming a skeletal box structure with triangulated bracing and what appears to be mounting flanges or attachment points on the visible faces.
def model_137098_0a45d1c8_0003():
    """Model: Stepper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.64, perimeter: 16.8
            with BuildLine():
                Line((-2.1, 2.1), (2.1, 2.1))
                Line((-2.1, -2.1), (-2.1, 2.1))
                Line((2.1, -2.1), (-2.1, -2.1))
                Line((2.1, 2.1), (2.1, -2.1))
            make_face()
        # Symmetric extrude, full_length=True, total=4
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.5637441664, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.55, 1.55)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.55, -1.55)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.55, -1.55)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.55, 1.55)):
                Circle(0.15)
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a longitudinal slot running along its length, designed for applications requiring flexible gripping, alignment, or component insertion.
def model_137098_0a45d1c8_0015():
    """Model: Pipe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8535396656, perimeter: 37.0707933124
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=30
        extrude(amount=15, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((1.5, -15), (1.5, -21))
                Line((-1.5, -15), (1.5, -15))
                Line((-1.5, -21), (-1.5, -15))
                Line((1.5, -21), (-1.5, -21))
            make_face()
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((1.5, -9), (1.5, -15))
                Line((-1.5, -9), (1.5, -9))
                Line((-1.5, -15), (-1.5, -9))
                Line((-1.5, -15), (1.5, -15))
            make_face()
        # Symmetric extrude, full_length=True, total=7
        extrude(amount=3.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting plate with a rectangular, bent channel shape featuring a central elongated hole and multiple mounting surfaces on the top and bottom flanges.
def model_137099_58f819ec_0003():
    """Model: L Block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.8914824629, perimeter: 20.9973445725
            with BuildLine():
                Line((-2, -1.2), (-2, 2))
                Line((2, -1.2), (-2, -1.2))
                Line((2, 2), (2, -1.2))
                Line((-2, 2), (2, 2))
            make_face()
            with BuildLine():
                CenterArc((-1.3649, 0.1283), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.0586283306, perimeter: 11.4849555922
            with BuildLine():
                Line((-2, -1.2), (-2, -2))
                Line((-2, -2), (2, -2))
                Line((2, -2), (2, -1.2))
                Line((2, -1.2), (-2, -1.2))
            make_face()
            with BuildLine():
                CenterArc((1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0586283306, perimeter: 11.4849555922
            with BuildLine():
                Line((-2, -1.2), (-2, -2))
                Line((-2, -2), (2, -2))
                Line((2, -2), (2, -1.2))
                Line((2, -1.2), (-2, -1.2))
            make_face()
            with BuildLine():
                CenterArc((1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1, 0.5)):
                Circle(0.15)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, 0.5)):
                Circle(0.25)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved cylindrical shell or bowl-shaped component with a tilted elliptical opening at the top and a solid dark base that transitions to a blue wireframe mesh surface, suggesting it's designed to contain or direct fluid/air flow.
def model_137099_58f819ec_0008():
    """Model: Rotor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, full_length=True, total=0.6
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a circular filter or strainer cover with a large flat circular face, a meshed or perforated outer ring section, and a small protruding lug or mounting tab on the edge.
def model_137118_4ff32ab1_0006():
    """Model: Spur Gear (36 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 2.140889856, perimeter: 6.0313552401
            with BuildLine():
                CenterArc((0, 0), 0.83492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0091996072, perimeter: 0.3803448382
            with BuildLine():
                _nurbs_edge([(0.8442747724, -0.0494783597), (0.8445759716, -0.0494945159), (0.8451784765, -0.0495205575), (0.8460825542, -0.0495408079), (0.8472886295, -0.0495319015), (0.8487972676, -0.0494709305), (0.8503069116, -0.0493729583), (0.8518175014, -0.0492508039), (0.8533289509, -0.0491143475), (0.8548411447, -0.0489678034), (0.8563539521, -0.048811408), (0.8578672402, -0.0486429448), (0.8593808868, -0.0484593041), (0.860894795, -0.048258079), (0.8624089043, -0.0480389929), (0.8639231803, -0.047803171), (0.8654376048, -0.047552556), (0.8669521664, -0.0472892844), (0.8684668501, -0.0470150491), (0.8699816291, -0.0467305562), (0.8714964689, -0.0464358581), (0.8730113313, -0.0461306064), (0.8745261782, -0.0458143292), (0.8760409752, -0.0454867134), (0.8775556951, -0.0451478373), (0.8790703155, -0.0447980264), (0.8805848172, -0.0444377497), (0.8820991824, -0.0440675031), (0.8836133929, -0.0436876915), (0.8851274284, -0.0432985343), (0.8866412674, -0.0429001294), (0.888154888, -0.042492499), (0.8896682686, -0.0420756409), (0.8911813885, -0.0416495805), (0.8926942283, -0.0412144125), (0.8942067699, -0.0407702734), (0.8957189959, -0.0403173229), (0.8972308893, -0.0398557222), (0.8987424332, -0.039385613), (0.9002536106, -0.0389071002), (0.9017644042, -0.0384202642), (0.9032747971, -0.0379251692), (0.9047847723, -0.0374218728), (0.9062943131, -0.0369104357), (0.9078034031, -0.0363909299), (0.9093120262, -0.035863433), (0.9108201667, -0.0353280253), (0.912327809, -0.0347847857), (0.9138349379, -0.0342337876), (0.9153415382, -0.0336750963), (0.9168475952, -0.033108771), (0.9183530939, -0.0325348664), (0.9198580192, -0.0319534352), (0.9213623561, -0.0313645294), (0.9228660892, -0.0307682026), (0.9243692032, -0.0301645085), (0.9258716829, -0.0295534999), (0.9273735139, -0.028935228), (0.9288746824, -0.0283097411), (0.9303751758, -0.0276770841), (0.9318749815, -0.0270372998), (0.9333740869, -0.0263904294), (0.9348724785, -0.0257365142), (0.936370141, -0.0250755961), (0.9378670573, -0.0244077193), (0.9393632098, -0.0237329278), (0.9408585814, -0.0230512643), (0.942353157, -0.0223627686), (0.9438469251, -0.0216674758), (0.9453398784, -0.0209654148), (0.9468320136, -0.0202566087), (0.9480250663, -0.0196841808), (0.9489194871, -0.0192518364), (0.9495156039, -0.0189622635), (0.9498136213, -0.0188171412)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.95, -1.1349613534, 2.2699227067)
                _nurbs_edge([(0.8442747724, 0.0494783597), (0.8445759716, 0.0494945159), (0.8451784765, 0.0495205575), (0.8460825542, 0.0495408079), (0.8472886295, 0.0495319015), (0.8487972676, 0.0494709305), (0.8503069116, 0.0493729583), (0.8518175014, 0.0492508039), (0.8533289509, 0.0491143475), (0.8548411447, 0.0489678034), (0.8563539521, 0.048811408), (0.8578672402, 0.0486429448), (0.8593808868, 0.0484593041), (0.860894795, 0.048258079), (0.8624089043, 0.0480389929), (0.8639231803, 0.047803171), (0.8654376048, 0.047552556), (0.8669521664, 0.0472892844), (0.8684668501, 0.0470150491), (0.8699816291, 0.0467305562), (0.8714964689, 0.0464358581), (0.8730113313, 0.0461306064), (0.8745261782, 0.0458143292), (0.8760409752, 0.0454867134), (0.8775556951, 0.0451478373), (0.8790703155, 0.0447980264), (0.8805848172, 0.0444377497), (0.8820991824, 0.0440675031), (0.8836133929, 0.0436876915), (0.8851274284, 0.0432985343), (0.8866412674, 0.0429001294), (0.888154888, 0.042492499), (0.8896682686, 0.0420756409), (0.8911813885, 0.0416495805), (0.8926942283, 0.0412144125), (0.8942067699, 0.0407702734), (0.8957189959, 0.0403173229), (0.8972308893, 0.0398557222), (0.8987424332, 0.039385613), (0.9002536106, 0.0389071002), (0.9017644042, 0.0384202642), (0.9032747971, 0.0379251692), (0.9047847723, 0.0374218728), (0.9062943131, 0.0369104357), (0.9078034031, 0.0363909299), (0.9093120262, 0.035863433), (0.9108201667, 0.0353280253), (0.912327809, 0.0347847857), (0.9138349379, 0.0342337876), (0.9153415382, 0.0336750963), (0.9168475952, 0.033108771), (0.9183530939, 0.0325348664), (0.9198580192, 0.0319534352), (0.9213623561, 0.0313645294), (0.9228660892, 0.0307682026), (0.9243692032, 0.0301645085), (0.9258716829, 0.0295534999), (0.9273735139, 0.028935228), (0.9288746824, 0.0283097411), (0.9303751758, 0.0276770841), (0.9318749815, 0.0270372998), (0.9333740869, 0.0263904294), (0.9348724785, 0.0257365142), (0.936370141, 0.0250755961), (0.9378670573, 0.0244077193), (0.9393632098, 0.0237329278), (0.9408585814, 0.0230512643), (0.942353157, 0.0223627686), (0.9438469251, 0.0216674758), (0.9453398784, 0.0209654148), (0.9468320136, 0.0202566087), (0.9480250663, 0.0196841808), (0.9489194871, 0.0192518364), (0.9495156039, 0.0189622635), (0.9498136213, 0.0188171412)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.832491631, 0.0488463179), (0.8442747724, 0.0494783597))
                Line((0.832491631, -0.0488463179), (0.832491631, 0.0488463179))
                Line((0.832491631, -0.0488463179), (0.8442747724, -0.0494783597))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a donut-shaped collar or ring component with a large central hole, featuring a small protruding nub or lip on one side and a mesh-textured surface on the upper portion, likely designed for mechanical assembly or functional fastening.
def model_137118_4ff32ab1_0008():
    """Model: Spur Gear (18 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.4163816839, perimeter: 3.2039218518
            with BuildLine():
                CenterArc((0, 0), 0.38492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0085424308, perimeter: 0.3588187241
            with BuildLine():
                _nurbs_edge([(0.4206564971, -0.0431290078), (0.4208792482, -0.0431512595), (0.4213250621, -0.0431898733), (0.4219947184, -0.0432301249), (0.4228894086, -0.0432501135), (0.4240104663, -0.0432286124), (0.4251337814, -0.0431729758), (0.4262588928, -0.0430955006), (0.4273854024, -0.0430055868), (0.4285130545, -0.0429071202), (0.4296416984, -0.0428001443), (0.430771256, -0.0426823462), (0.4319016878, -0.0425505802), (0.4330329583, -0.0424024384), (0.434165006, -0.0422376179), (0.4352977537, -0.0420571867), (0.4364311171, -0.0418630129), (0.4375650128, -0.0416571487), (0.4386993677, -0.0414411979), (0.4398341258, -0.0412157969), (0.4409692433, -0.0409809503), (0.4421046843, -0.040736277), (0.4432404167, -0.0404812828), (0.4443764074, -0.0402156404), (0.4455126188, -0.039939409), (0.4466490109, -0.0396528884), (0.4477855429, -0.0393565179), (0.4489221745, -0.0390507619), (0.4500588677, -0.0387359923), (0.4511955882, -0.0384123997), (0.4523323041, -0.0380800587), (0.453468985, -0.0377389713), (0.4546056019, -0.0373891179), (0.4557421256, -0.0370305092), (0.4568785263, -0.0366632238), (0.4580147744, -0.0362873818), (0.4591508399, -0.0359031257), (0.4602866938, -0.0355105999), (0.4614223073, -0.0351099289), (0.4625576528, -0.0347012021), (0.4636927034, -0.0342844852), (0.4648274325, -0.033859829), (0.4659618142, -0.0334272787), (0.4670958224, -0.032986883), (0.468229431, -0.032538702), (0.4693626142, -0.0320828018), (0.4704953464, -0.0316192513), (0.4716276022, -0.031148118), (0.4727593569, -0.0306694647), (0.4738905862, -0.0301833462), (0.4750212663, -0.0296898118), (0.4761513733, -0.029188907), (0.4772808834, -0.0286806751), (0.4784097724, -0.0281651594), (0.4795380156, -0.0276424046), (0.4806655884, -0.0271124557), (0.4817924665, -0.0265753572), (0.4829186265, -0.0260311522), (0.4840440464, -0.0254798816), (0.4851687054, -0.0249215833), (0.4862925836, -0.0243562934), (0.4874156605, -0.0237840468), (0.4885379141, -0.0232048779), (0.4896593201, -0.0226188219), (0.4907798511, -0.0220259155), (0.4918994787, -0.0214261953), (0.4930181756, -0.020819697), (0.4941359176, -0.020206454), (0.4952526859, -0.0195864963), (0.4963684687, -0.0189598496), (0.49748326, -0.0183265346), (0.4983742979, -0.0178145603), (0.4990421289, -0.01742759), (0.4994871509, -0.0171682816), (0.4997096122, -0.0170382954)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.5, -1.9528228938, 3.9056457875)
                _nurbs_edge([(0.4206564971, 0.0431290078), (0.4208792482, 0.0431512595), (0.4213250621, 0.0431898733), (0.4219947184, 0.0432301249), (0.4228894086, 0.0432501135), (0.4240104663, 0.0432286124), (0.4251337814, 0.0431729758), (0.4262588928, 0.0430955006), (0.4273854024, 0.0430055868), (0.4285130545, 0.0429071202), (0.4296416984, 0.0428001443), (0.430771256, 0.0426823462), (0.4319016878, 0.0425505802), (0.4330329583, 0.0424024384), (0.434165006, 0.0422376179), (0.4352977537, 0.0420571867), (0.4364311171, 0.0418630129), (0.4375650128, 0.0416571487), (0.4386993677, 0.0414411979), (0.4398341258, 0.0412157969), (0.4409692433, 0.0409809503), (0.4421046843, 0.040736277), (0.4432404167, 0.0404812828), (0.4443764074, 0.0402156404), (0.4455126188, 0.039939409), (0.4466490109, 0.0396528884), (0.4477855429, 0.0393565179), (0.4489221745, 0.0390507619), (0.4500588677, 0.0387359923), (0.4511955882, 0.0384123997), (0.4523323041, 0.0380800587), (0.453468985, 0.0377389713), (0.4546056019, 0.0373891179), (0.4557421256, 0.0370305092), (0.4568785263, 0.0366632238), (0.4580147744, 0.0362873818), (0.4591508399, 0.0359031257), (0.4602866938, 0.0355105999), (0.4614223073, 0.0351099289), (0.4625576528, 0.0347012021), (0.4636927034, 0.0342844852), (0.4648274325, 0.033859829), (0.4659618142, 0.0334272787), (0.4670958224, 0.032986883), (0.468229431, 0.032538702), (0.4693626142, 0.0320828018), (0.4704953464, 0.0316192513), (0.4716276022, 0.031148118), (0.4727593569, 0.0306694647), (0.4738905862, 0.0301833462), (0.4750212663, 0.0296898118), (0.4761513733, 0.029188907), (0.4772808834, 0.0286806751), (0.4784097724, 0.0281651594), (0.4795380156, 0.0276424046), (0.4806655884, 0.0271124557), (0.4817924665, 0.0265753572), (0.4829186265, 0.0260311522), (0.4840440464, 0.0254798816), (0.4851687054, 0.0249215833), (0.4862925836, 0.0243562934), (0.4874156605, 0.0237840468), (0.4885379141, 0.0232048779), (0.4896593201, 0.0226188219), (0.4907798511, 0.0220259155), (0.4918994787, 0.0214261953), (0.4930181756, 0.020819697), (0.4941359176, 0.020206454), (0.4952526859, 0.0195864963), (0.4963684687, 0.0189598496), (0.49748326, 0.0183265346), (0.4983742979, 0.0178145603), (0.4990421289, 0.01742759), (0.4994871509, 0.0171682816), (0.4997096122, 0.0170382954)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.3819178948, 0.0392592152), (0.4206564971, 0.0431290078))
                Line((0.3819178948, -0.0392592152), (0.3819178948, 0.0392592152))
                Line((0.3819178948, -0.0392592152), (0.4206564971, -0.0431290078))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular prism or box-shaped structural component with a slightly tapered top and internal ribbed or latticed reinforcement patterns visible on its surfaces, suggesting it's a lightweight engineering part designed for structural support with minimal material use.
def model_137141_748596d0_0008():
    """Model: R0805-NO v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0007392699, perimeter: 0.2577079633
            with BuildLine():
                Line((0.094, -0.0625), (0.094, 0.0625))
                Line((0.094, -0.0625), (0.095, -0.0625))
                CenterArc((0.095, -0.0575), 0.005, -90.0000000014, 90.0000000014)
                Line((0.1, -0.0575), (0.1, 0.0575))
                CenterArc((0.095, 0.0575), 0.005, 0, 89.9999999987)
                Line((0.095, 0.0625), (0.094, 0.0625))
            make_face()
            # Profile area: 0.0026713571, perimeter: 0.2834630458
            with BuildLine():
                CenterArc((0.32, 0), 0.25, 165.5224878141, 28.9550243719)
                Line((0.0779385409, -0.0625), (0.094, -0.0625))
                Line((0.094, -0.0625), (0.094, 0.0625))
                Line((0.094, 0.0625), (0.0779385409, 0.0625))
            make_face()
        # OneSide extrude, distance=0.045
        extrude(amount=0.045)
    return part.part


# Description: This is a segmented connector or link component with a zigzag/articulated shape consisting of three stacked rectangular blocks joined at angled joints, featuring triangulated surface details and angled mounting faces on the top and bottom segments.
def model_137164_339dce36_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.8387003088, perimeter: 15.2400004053
            with BuildLine():
                Line((0, 0), (0, 5.0800001621))
                Line((0, 5.0800001621), (-1.2700000405, 5.0800001621))
                Line((-1.2700000405, 5.0800001621), (-1.2700000405, 4.4450001621))
                Line((-1.2700000405, 4.4450001621), (-0.6350000405, 4.4450001621))
                Line((-0.6350000405, 4.4450001621), (-0.6350000405, 3.1750001621))
                Line((-0.6350000405, 3.1750001621), (-1.2700000405, 3.1750001621))
                Line((-1.2700000405, 3.1750001621), (-1.2700000405, 1.9050001621))
                Line((-1.2700000405, 1.9050001621), (-0.6350000405, 1.9050001621))
                Line((-0.6350000405, 1.9050001621), (-0.6350000405, 0.635))
                Line((-1.2700000405, 0.635), (-0.6350000405, 0.635))
                Line((-1.2700000405, 0), (-1.2700000405, 0.635))
                Line((0, 0), (-1.2700000405, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6129001802, perimeter: 6.3500004053
            with BuildLine():
                Line((0.6350000405, -1.9050001621), (0, -1.9050001621))
                Line((0.6350000405, -0.635), (0.6350000405, -1.9050001621))
                Line((1.2700000405, -0.635), (0.6350000405, -0.635))
                Line((1.2700000405, 0), (1.2700000405, -0.635))
                Line((0, 0), (1.2700000405, 0))
                Line((0, -1.9050001621), (0, 0))
            make_face()
            # Profile area: 1.6129000772, perimeter: 6.3500000811
            with BuildLine():
                Line((0, -3.1750001621), (0, -5.0800001621))
                Line((0, -5.0800001621), (1.2700000405, -5.0800001621))
                Line((1.2700000405, -5.0800001621), (1.2700000405, -4.4450001621))
                Line((1.2700000405, -4.4450001621), (0.6350000405, -4.4450001621))
                Line((0.6350000405, -4.4450001621), (0.6350000405, -3.1750001621))
                Line((0.6350000405, -3.1750001621), (0, -3.1750001621))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a hexahedron or irregular polyhedron featuring a trapezoidal prism-like shape with multiple angled facets, a top surface with triangulated geometry, and dark shadowing that suggests depth and internal structure.
def model_137373_22e709d8_0000():
    """Model: Lego Brick"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0244, perimeter: 9.52
            with BuildLine():
                Line((0, 1.58), (0, 0))
                Line((0, 0), (3.18, 0))
                Line((3.18, 0), (3.18, 1.58))
                Line((3.18, 1.58), (0, 1.58))
            make_face()
        # OneSide extrude, distance=0.96
        extrude(amount=0.96)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.96), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.39, -1.19)):
                Circle(0.25)
        # OneSide extrude, distance=0.17
        extrude(amount=0.17, mode=Mode.ADD)
    return part.part


# Description: This is a flat, rectangular base plate or platform with a tapered wedge-shaped profile, featuring a slightly curved or beveled top surface with internal geometric divisions, and a recessed or stepped underside.
def model_137483_cdb8989d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 149.6, perimeter: 49.2
            with BuildLine():
                Line((6.8, -5.5), (-6.8, -5.5))
                Line((6.8, 5.5), (6.8, -5.5))
                Line((-6.8, 5.5), (6.8, 5.5))
                Line((-6.8, -5.5), (-6.8, 5.5))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


# Description: This is a channel or bracket-shaped structural component with a bent L-shaped profile, featuring sharp angular geometry, multiple planar faces, and what appears to be a reinforcing flange or gusset along the inner bend.
def model_137646_14bca880_0002():
    """Model: DESIGN: Drag Chain Cable Support"""
    with BuildPart() as part:
        # Arc -> Extrude1 (NewBody)
        # Sketch on Motor Mount Right Plane construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6000000238, 0.2917941714, 2.425), x_dir=(0, 1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0600000174, perimeter: 1
            with BuildLine():
                Line((1.7379904907, -1.6750000581), (1.4379904907, -1.6750000581))
                Line((1.7379904907, -1.4750000581), (1.7379904907, -1.6750000581))
                Line((1.7379904907, -1.4750000581), (1.4379904907, -1.4750000581))
                Line((1.4379904907, -1.4750000581), (1.4379904907, -1.6750000581))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Arc -> Extrude4 (Join)
        # Sketch on Motor Mount Right Plane construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6000000238, 0.2917941714, 2.425), x_dir=(0, 1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.6741718069, perimeter: 5.0944787128
            with BuildLine():
                Line((1.4379904907, -2.8750000581), (2.7852298471, -2.8750000581))
                Line((2.7852298471, -2.5750000581), (2.7852298471, -2.8750000581))
                Line((1.7379904907, -2.5750000581), (2.7852298471, -2.5750000581))
                Line((1.7379904907, -1.6750000581), (1.7379904907, -2.5750000581))
                Line((1.7379904907, -1.6750000581), (1.4379904907, -1.6750000581))
                Line((1.4379904907, -1.6750000581), (1.4379904907, -2.8750000581))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Zip Tie Cutout -> Extrude5 (Cut)
        # Sketch on Motor Mount Right Plane construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6000000238, 2.9398923691, 4.2000000581), x_dir=(0, 1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.26, perimeter: 2.52
            with BuildLine():
                Line((-0.1501077069, -0.45), (-0.1501077069, -1.45))
                Line((-0.4101077069, -0.45), (-0.1501077069, -0.45))
                Line((-0.4101077069, -1.45), (-0.4101077069, -0.45))
                Line((-0.1501077069, -1.45), (-0.4101077069, -1.45))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pyramidal or wedge-shaped structural component with a trapezoidal base, featuring an internal skeletal framework of triangular bracing elements that provide rigidity while minimizing material and weight.
def model_137837_9c9f163d_0011():
    """Model: BOTTOM PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 750, perimeter: 110
            with BuildLine():
                Line((15, -12.5), (-15, -12.5))
                Line((15, 12.5), (15, -12.5))
                Line((-15, 12.5), (15, 12.5))
                Line((-15, -12.5), (-15, 12.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((2.761, 0)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-2.761, 0)):
                Circle(1.5)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a elongated rectangular flat plate with a tapered wedge profile, featuring two parallel slots or grooves running along its length and a beveled or angled edge on one side.
def model_137837_9c9f163d_0013():
    """Model: EJECTOR RETAINER PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 350.4, perimeter: 77.2
            with BuildLine():
                Line((7.3, -12), (-7.3, -12))
                Line((7.3, 12), (7.3, -12))
                Line((-7.3, 12), (7.3, 12))
                Line((-7.3, -12), (-7.3, 12))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)
    return part.part


# Description: This is a bracket or mounting adapter featuring a cylindrical shaft on the left side connected to a larger angled flange or plate on the right, with visible holes or slots for fastening and assembly purposes.
def model_137905_bef6aac2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=14.5
        extrude(amount=14.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 10.3561113074, perimeter: 16.3683691926
            with BuildLine():
                CenterArc((0, 0), 1.6, -14.4775121859, 104.4775121859)
                Line((1.5491933385, -0.4), (6.5, -0.4))
                Line((6.5, 1.6), (6.5, -0.4))
                Line((0, 1.6), (6.5, 1.6))
            make_face()
            # Profile area: 10.3561113074, perimeter: 16.3683691926
            with BuildLine():
                Line((-6.5, 1.6), (-6.5, -0.4))
                Line((-6.5, -0.4), (-1.5491933385, -0.4))
                CenterArc((0, 0), 1.6, 90, 104.4775121859)
                Line((-6.5, 1.6), (0, 1.6))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.ADD)
    return part.part


# Description: This is a dual-channel structural bracket or guide with two vertical flanges connected by curved transitions, featuring horizontal slot patterns along the surfaces and angled feet for base mounting.
def model_137997_9a5922be_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3667058859, perimeter: 12.4214818042
            with BuildLine():
                CenterArc((1.1641661389, 4.6472761188), 3.5, 180, 90)
                CenterArc((-6.2358338611, 4.6472761188), 3.9, -18.4286696038, 18.4286696038)
                CenterArc((1.1641661389, 4.6472761188), 3.9, -161.5713303962, 36.2769357195)
                CenterArc((-1.4358338611, 0.9744025844), 0.6, 0, 54.7056053233)
                Line((-0.8358338611, 0.7472761188), (-0.8358338611, 0.9744025844))
                Line((1.1641661389, 0.7472761188), (-0.8358338611, 0.7472761188))
                Line((1.1641661389, 1.1472761188), (1.1641661389, 0.7472761188))
            make_face()
            # Profile area: 1.4715822124, perimeter: 8.6142472609
            with BuildLine():
                Line((-2.3358338611, 4.6472761188), (-2.3358338611, 7.5))
                Line((-2.3358338611, 7.5), (-2.7358338611, 7.5))
                Line((-2.7358338611, 4.6472761188), (-2.7358338611, 7.5))
                CenterArc((1.1641661389, 4.6472761188), 3.9, 180, 18.4286696038)
                CenterArc((-6.2358338611, 4.6472761188), 3.9, -18.4286696038, 18.4286696038)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3667058859, perimeter: 12.4214818042
            with BuildLine():
                CenterArc((1.1641661389, 4.6472761188), 3.9, 180, 18.4286696038)
                CenterArc((-6.2358338611, 4.6472761188), 3.5, -90, 90)
                Line((-6.2358338611, 1.1472761188), (-6.2358338611, 0.7472761188))
                Line((-6.2358338611, 0.7472761188), (-4.2358338611, 0.7472761188))
                Line((-4.2358338611, 0.7472761188), (-4.2358338611, 0.9744025844))
                CenterArc((-3.6358338611, 0.9744025844), 0.6, 125.2943946767, 54.7056053233)
                CenterArc((-6.2358338611, 4.6472761188), 3.9, -54.7056053233, 36.2769357195)
            make_face()
            # Profile area: 1.4715822124, perimeter: 8.6142472609
            with BuildLine():
                Line((-2.3358338611, 4.6472761188), (-2.3358338611, 7.5))
                Line((-2.3358338611, 7.5), (-2.7358338611, 7.5))
                Line((-2.7358338611, 4.6472761188), (-2.7358338611, 7.5))
                CenterArc((1.1641661389, 4.6472761188), 3.9, 180, 18.4286696038)
                CenterArc((-6.2358338611, 4.6472761188), 3.9, -18.4286696038, 18.4286696038)
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.3358338611, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.8105637508, perimeter: 8.9977871438
            with BuildLine():
                CenterArc((7.5, 0), 1.75, 90, 180)
                Line((7.5, -1.75), (7.5, 1.75))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a centrifugal fan or blower impeller featuring a curved, snail-shell-shaped (volute) housing with multiple backward-curved fan blades arranged radially around a central hub, designed to move air or gas efficiently through the spiral discharge passage.
def model_138071_f8d5a493_0000():
    """Model: GoPro male mount v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.8731855177, perimeter: 7.0586899288
            with BuildLine():
                Line((1.5, 0), (1.5, 0.797))
                CenterArc((0.75, 0.797), 0.75, 0, 180)
                Line((0, 0.797), (0, 0))
                Line((0, 0), (1.5, 0))
            make_face()
            with BuildLine():
                CenterArc((0.75, 0.791), 0.256, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.944
        extrude(amount=0.944)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.26301, perimeter: 2.254
            with BuildLine():
                Line((-0.307, 0), (-0.307, 0.797))
                Line((-0.307, 0.797), (-0.637, 0.797))
                Line((-0.637, 0.797), (-0.637, 0))
                Line((-0.637, 0), (-0.307, 0))
            make_face()
            # Profile area: 0.7088438392, perimeter: 4.9560232681
            with BuildLine():
                Line((-0.307, 0.797), (-0.637, 0.797))
                Line((-0.307, 0.797), (-0.307, 2.945011634))
                Line((-0.307, 2.945011634), (-0.637, 2.945011634))
                Line((-0.637, 2.945011634), (-0.637, 0.797))
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an oval or elliptical ring/band with a hollow center, featuring a curved outer surface and an open-top design with internal ribbing or structural reinforcement patterns.
def model_138117_188eed23_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.4165304173, perimeter: 15.2127889177
            Circle(2.4211905545)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical pin or dowel with a rounded end on one side and a slightly tapered or beveled end on the other, featuring a uniform diameter along its length.
def model_138121_ccc9851b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: These are two finger ring straps with black elastomeric bands and blue mounting plates, designed to secure devices or tools to a user's finger or hand, featuring oval-shaped loops for comfortable grip and angled attachment plates for device mounting.
def model_138131_8cca28d3_0000():
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
        # Sketch19 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.6313692223, perimeter: 30.1777701426
            with BuildLine():
                Line((0.6901891416, 2.562638347), (1.2925464966, -0.4755595601))
                _nurbs_edge([(1.2925464966, -0.4755595601), (1.2156374678, -0.5787849515), (1.0731269126, -0.7849250198), (0.8932835474, -1.0932035882), (0.7216145018, -1.5023657923), (0.6217839313, -2.008946102), (0.6375068709, -2.5053755372), (0.7681296098, -2.9812699482), (1.0103803932, -3.4188667007), (1.3571738026, -3.7925652941), (1.7967791306, -4.0747136783), (2.3116229851, -4.240677304), (2.8773475204, -4.2737364285), (3.4607824625, -4.1717223793), (4.0225136933, -3.945192603), (4.5211921264, -3.6122895264), (4.9174401496, -3.1948144195), (5.1775625491, -2.714295036), (5.2786044384, -2.1874392067), (5.208072066, -1.6253001969), (4.9603726063, -1.034829829), (4.6197088398, -0.5427039815), (4.2845663236, -0.1631399599), (4.0258857328, 0.0945378136), (3.8877322869, 0.2245354263)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((2.3129824895, 3.374035021), (3.8877322869, 0.2245354263))
                Line((0.6901891416, 2.562638347), (2.3129824895, 3.374035021))
            make_face()
            with BuildLine():
                CenterArc((3, -2), 1.6263436447, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch20 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.6367667398, perimeter: 32.3956497509
            with BuildLine():
                _nurbs_edge([(-6.441592895, 0.9489652648), (-6.5279314645, 0.9328064601), (-6.69694048, 0.8945479843), (-6.9394495134, 0.8193375818), (-7.2407470981, 0.6833478961), (-7.5803536464, 0.4539254097), (-7.8825609539, 0.1659790779), (-8.1468749487, -0.1781870709), (-8.3728363427, -0.5741929913), (-8.5596655879, -1.0152894144), (-8.705538759, -1.4924124322), (-8.8068825023, -1.9940863146), (-8.8578476626, -2.5064238726), (-8.8492438472, -3.0129113025), (-8.7692386566, -3.4947721139), (-8.6070647786, -3.9323542547), (-8.3562742837, -4.3062973264), (-8.0177813813, -4.5987717111), (-7.6041161937, -4.7947678832), (-7.1394936604, -4.8831776885), (-6.6539579313, -4.8574690308), (-6.1788333925, -4.7166086254), (-5.7420948244, -4.4657373725), (-5.3627149175, -4.1175440436), (-5.0499846632, -3.6911212305), (-4.8065201338, -3.2090311595), (-4.6301257186, -2.6949272709), (-4.5160544511, -2.1710052165), (-4.4591024169, -1.6554566924), (-4.455626446, -1.1601098475), (-4.5032013374, -0.69192006), (-4.580975047, -0.3417532093), (-4.6613513071, -0.0932923564), (-4.7247161223, 0.0660646011), (-4.7588436824, 0.1441721631)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.4121939168, 2.6737675409), (-4.7588436824, 0.1441721631))
                Line((-4.9469456382, 3.1817239289), (-3.4121939168, 2.6737675409))
                Line((-6.441592895, 0.9489652648), (-4.9469456382, 3.1817239289))
            make_face()
            with BuildLine():
                EllipticalCenterArc((-6.657833841, -1.9875950844), 2.0936283294, 1.3499201224, 0, 360, 71.6870186785)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a curved, oblong container or tray with a rounded rectangular basin featuring an open top, internal ribbed reinforcement patterns, and sloped side walls that create a boat-like or elongated bowl shape.
def model_138138_0938b9fb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 79.4832083857, perimeter: 35.8861457138
            with BuildLine():
                Line((-3.5, 1.5), (-2.5, 1.5))
                CenterArc((-3.5, -1.5058234463), 3.0058234463, 90, 180)
                Line((-3.5, -4.5116468926), (5, -4.5116468926))
                CenterArc((5, -1.5058234463), 3.0058234463, -90, 180)
                Line((5, 1.5), (3.5, 1.5))
                Line((-2.5, 1.5), (3.5, 1.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a hexagonal or polygonal connector block featuring a complex geometric shape with multiple faceted surfaces, internal geometric divisions, and a roughly prismatic form with tapered or angled edges, suitable for mechanical assembly or structural applications.
def model_138148_d6277b0d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch12 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1794270546, perimeter: 10.1350273212
            with BuildLine():
                Line((4.2637950962, 3.4941324031), (1.2396337181, 3.4941324031))
                Line((4.2637950962, 5.5374846856), (4.2637950962, 3.4941324031))
                Line((1.2396337181, 5.5374846856), (4.2637950962, 5.5374846856))
                Line((1.2396337181, 3.4941324031), (1.2396337181, 5.5374846856))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a structural beam or support bar with a elongated hexagonal cross-section, featuring pointed/chamfered ends on both sides and a central longitudinal ridge or groove running along its length.
def model_138159_43a27dbd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0001312898, perimeter: 0.1687650983
            with BuildLine():
                Line((0.2385058964, 1.3548641817), (0.1899999958, 1.3548641817))
                Line((0.2476281158, 1.3506061742), (0.2385058964, 1.3548641817))
                Line((0.2614347181, 1.3548641817), (0.2476281158, 1.3506061742))
                Line((0.2584560958, 1.3557283935), (0.2614347181, 1.3548641817))
                Line((0.1838183443, 1.3557283935), (0.2584560958, 1.3557283935))
                Line((0.179999996, 1.3499999698), (0.1838183443, 1.3557283935))
                Line((0.1899999958, 1.3548641817), (0.179999996, 1.3499999698))
            make_face()
        # OneSide extrude, distance=0.008
        extrude(amount=0.008)
    return part.part


# Description: This is a circular disk or plate with an overall flat, disc-shaped geometry featuring a mesh or perforated pattern on its curved edge, suggesting it may be a filter, strainer, or component designed for fluid or air passage.
def model_138186_5b1b2266_0000():
    """Model: Helmet"""
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
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 15.2653143114, perimeter: 13.8502562136
            with Locations((-4.3725337633, 0.2604175052)):
                Circle(2.2043367395)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a folded metal bracket or sheet metal component with an angular, triangular profile featuring two flat perpendicular flanges connected at a bend, creating a corner or L-shaped support structure with reinforcing internal geometry.
def model_138242_d520d083_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1600, perimeter: 340
            with BuildLine():
                Line((0, 10), (0, 0))
                Line((0, 10), (-160, 10))
                Line((-160, 10), (-160, 0))
                Line((-160, 0), (0, 0))
            make_face()
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 10))
                Line((10, 10), (0, 10))
                Line((0, 10), (0, 0))
            make_face()
            # Profile area: 3000, perimeter: 620
            with BuildLine():
                Line((0, 0), (0, -300))
                Line((0, -300), (10, -300))
                Line((10, -300), (10, 0))
                Line((0, 0), (10, 0))
            make_face()
        # OneSide extrude, distance=360
        extrude(amount=360)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 837, perimeter: 282.4
            with BuildLine():
                Line((-10, -12.4), (-10, -6.2))
                Line((-10, -6.2), (-145, -6.2))
                Line((-145, -6.2), (-145, -12.4))
                Line((-145, -12.4), (-10, -12.4))
            make_face()
        # Start offset: 15 (not directly supported, may affect result)
        # OneSide extrude, distance=40
        extrude(amount=40)
    return part.part


# Description: This is a curved boat hull or fairings component with an elongated, asymmetrical shape featuring a smooth curved bottom surface, a flat or slightly angled top deck area, and vertical ribbed reinforcement structures along the sides for structural support.
def model_138256_ae3bde67_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 92.809071961, perimeter: 37.3594664428
            with BuildLine():
                Line((-6, -3), (-6, 3))
                CenterArc((0, 2.9), 8.4148677946, -135.4814658058, 90.9629316117)
                Line((6, 3), (6, -3))
                Line((-6, 3), (6, 3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a phone case or protective cover with a rectangular body, rounded corners, a raised camera cutout hole in the upper right corner, and a textured surface design in dark blue.
def model_138263_895e2c6e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 47 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45.3857856147, perimeter: 42.4216008811
            with BuildLine():
                Line((-2.2489839763, 18.9405381173), (-4.3214955822, 16.8680265114))
                CenterArc((-2.826123293, 17.4953979722), 1.5561233338, 68.2299303313, 21.7604974866)
                Line((-7.6178438338, 19.0515212843), (-2.8258633176, 19.0515212843))
                CenterArc((-4.9918197183, 15.3281799765), 4.5562345362, 125.1948184316, 199.5771784515)
                Line((-1.2699999809, 17.4953979722), (-1.2699999809, 12.6999998093))
                CenterArc((-2.826123293, 17.4953979722), 1.5561233121, 0.0000000001, 19.6144673063)
                Line((-3.4342440666, 15.9592268298), (-1.3602975833, 18.0177721207))
                CenterArc((-5.0799999237, 15.2399997711), 1.7960511972, 65.0189951109, 318.5872608432)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 47 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 238.3185907989, perimeter: 68.2618367323
            with BuildLine():
                CenterArc((-5.1173679468, 15.2308566476), 5.4082116107, 147.9845000814, 0.9440491672)
                CenterArc((-10.2821489481, 18.4012316685), 0.6537098813, -27.6353800672, 111.7717771744)
                Line((-10.3489323626, 19.0515212843), (-10.2153655337, 19.0515212843))
                Line((-17.3790424076, 19.0515212843), (-10.3489323626, 19.0515212843))
                CenterArc((-17.3790424076, 17.380563978), 1.6709573063, 90, 90)
                Line((-19.0499997139, 2.9198897206), (-19.0499997139, 17.380563978))
                CenterArc((-17.4001099742, 2.9198897206), 1.6498897397, 180, 90)
                Line((-2.9260130431, 1.2699999809), (-17.4001099742, 1.2699999809))
                CenterArc((-2.9260130431, 2.9260130431), 1.6560130622, -90, 89.9999924894)
                Line((-1.2699999809, 10.0173640285), (-1.2699999809, 2.926012826))
                Line((-1.2699999809, 10.1496713035), (-1.2699999809, 10.0173640285))
                CenterArc((-1.9203539654, 10.083517666), 0.6537098813, 5.8081171914, 111.2554766518)
                CenterArc((-5.1173679468, 15.2308566476), 5.4082116107, -58.732786392, 1.1544323241)
                CenterArc((-5.1173679468, 15.2308566476), 5.4082116107, 148.9285492485, 152.3386643594)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 47 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 107.81883472, perimeter: 172.6163312512
            with BuildLine():
                Line((-1.6437730712, 19.5457490224), (-2.2489839763, 18.9405381173))
                Line((-1.5889262835, 19.6005958102), (-1.6437730712, 19.5457490224))
                CenterArc((-1.884358002, 19.841180741), 0.3810000122, -39.1576617489, 102.5640703829)
                CenterArc((-2.5399999619, 17.779999733), 2.5399999619, 71.0177256004, 2.6738098414)
                CenterArc((-2.5399999619, 17.779999733), 2.5399999619, 73.6915354417, 16.3084645583)
                Line((-17.779999733, 20.3199996948), (-2.5399999619, 20.3199996948))
                CenterArc((-17.779999733, 17.779999733), 2.5399999619, 90, 90)
                Line((-20.3199996948, 2.5399999619), (-20.3199996948, 17.779999733))
                CenterArc((-17.779999733, 2.5399999619), 2.5399999619, -180, 90)
                Line((-2.5399999619, 0), (-17.779999733, 0))
                CenterArc((-2.5399999619, 2.5399999619), 2.5399999619, -90, 90)
                Line((0, 17.779999733), (0, 2.5399999619))
                CenterArc((-2.5399999619, 17.779999733), 2.5399999619, 0, 14.9636718494)
                CenterArc((-2.5399999619, 17.779999733), 2.5399999619, 14.9636718494, 1.9751050722)
                CenterArc((-0.4620666773, 18.3739235997), 0.3810000122, 22.5491543272, 108.0846393644)
                Line((-0.7493453767, 18.6241873768), (-0.7101822408, 18.663059686))
                Line((-1.3602975833, 18.0177721207), (-0.7493453767, 18.6241873768))
                CenterArc((-2.826123293, 17.4953979722), 1.5561233121, 0.0000000001, 19.6144673063)
                Line((-1.2699999809, 17.4953979722), (-1.2699999809, 12.6999998093))
                CenterArc((-4.9918197183, 15.3281799765), 4.5562345362, 125.1948184316, 199.5771784515)
                Line((-7.6178438338, 19.0515212843), (-2.8258633176, 19.0515212843))
                CenterArc((-2.826123293, 17.4953979722), 1.5561233338, 68.2299303313, 21.7604974866)
            make_face()
            with BuildLine():
                CenterArc((-5.1173679468, 15.2308566476), 5.4082116107, 148.9285492485, 152.3386643594)
                CenterArc((-1.9203539654, 10.083517666), 0.6537098813, 117.0635938431, 9.5616718538)
                CenterArc((-1.9203539654, 10.083517666), 0.6537098813, 5.8081171914, 111.2554766518)
                CenterArc((-1.9203539654, 10.083517666), 0.6537098813, -5.8081171914, 11.6162343828)
                Line((-1.2699999809, 10.0173640285), (-1.2699999809, 2.926012826))
                CenterArc((-2.9260130431, 2.9260130431), 1.6560130622, -90, 89.9999924894)
                Line((-2.9260130431, 1.2699999809), (-17.4001099742, 1.2699999809))
                CenterArc((-17.4001099742, 2.9198897206), 1.6498897397, 180, 90)
                Line((-19.0499997139, 2.9198897206), (-19.0499997139, 17.380563978))
                CenterArc((-17.3790424076, 17.380563978), 1.6709573063, 90, 90)
                Line((-17.3790424076, 19.0515212843), (-10.3489323626, 19.0515212843))
                CenterArc((-10.2821489481, 18.4012316685), 0.6537098813, 84.1363971072, 11.7272057857)
                CenterArc((-10.2821489481, 18.4012316685), 0.6537098813, -27.6353800672, 111.7717771744)
                CenterArc((-10.2821489481, 18.4012316685), 0.6537098813, -35.4515706029, 7.8161905357)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or mounting arm with an elongated vertical shaft connecting a rectangular head/plate at the top to a horizontal foot or flange at the bottom, designed for wall or surface mounting applications.
def model_138313_ceb6bcca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Grundform -> Extrusion1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 8.2309004592, perimeter: 24.2515926536
            with BuildLine():
                Line((0.5, 1.655), (4.1, 1.655))
                Line((4.1, 1.655), (4.1, 0))
                Line((4.1, 0), (7.05, 0))
                Line((7.05, 0), (7.05, 2.055))
                Line((7.05, 2.055), (0, 2.055))
                Line((0, 2.055), (0, 0.205))
                Line((0, 0.205), (0.5, 0.205))
                Line((0.5, 0.205), (0.5, 1.655))
            make_face()
            with BuildLine():
                CenterArc((0.25, 0.455), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.25, 1.205), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.35, 1.205), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.35, 0.455), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.25, 0.455)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.25, 1.205)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((4.35, 1.205)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((4.35, 0.455)):
                Circle(0.125)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a cylindrical container or canister with a removable cap, featuring a ribbed or textured surface pattern and a small protruding handle or loop on top for carrying or opening.
def model_138423_553700e1_0005():
    """Model: motor v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 201.0619298297, perimeter: 50.2654824574
            Circle(8)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


# Description: This is a long, hexagonal prism or extruded hexagonal tube with a hollow interior channel running lengthwise, featuring angular faceted surfaces and open ends.
def model_138563_a93c9c1c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1820.8983049618, perimeter: 1194.8160095215
            with BuildLine():
                Line((0, 0), (60.9599990845, 0))
                Line((60.9599990845, 0), (60.9599990845, 243.8399963379))
                Line((60.9599990845, 243.8399963379), (0, 243.8399963379))
                Line((0, 243.8399963379), (0, 0))
            make_face()
            with BuildLine():
                Line((3.0480000973, 3.0480000973), (57.9120018482, 3.0480000973))
                Line((3.0480000973, 240.7920076847), (3.0480000973, 3.0480000973))
                Line((57.9120018482, 240.7920076847), (3.0480000973, 240.7920076847))
                Line((57.9120018482, 3.0480000973), (57.9120018482, 240.7920076847))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13043.5876485538, perimeter: 585.2160186768
            with BuildLine():
                Line((3.0480000973, 3.0480000973), (57.9120018482, 3.0480000973))
                Line((57.9120018482, 3.0480000973), (57.9120018482, 240.7920076847))
                Line((57.9120018482, 240.7920076847), (3.0480000973, 240.7920076847))
                Line((3.0480000973, 3.0480000973), (3.0480000973, 240.7920076847))
            make_face()
        # OneSide extrude, distance=15.24
        extrude(amount=15.24, mode=Mode.ADD)
    return part.part


# Description: This is a solid cylindrical roller or spacer with a smooth circular cross-section and flat circular end faces, featuring a textured or knurled surface pattern along its length.
def model_138620_e21e10ee_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4964162502, perimeter: 2.4976289915
            Circle(0.39751)
        # OneSide extrude, distance=1.96342
        extrude(amount=1.96342)
    return part.part


# Description: This is a rectangular box or container with a sloped/angled top surface, featuring an internal cavity or recessed area on the upper face, and appears to be a hollow molded component with angled side walls and a tapered or beveled edge design.
def model_138752_d35ee151_0004():
    """Model: Component10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70, perimeter: 34
            with BuildLine():
                Line((-5, 3.5), (-5, -3.5))
                Line((-5, -3.5), (5, -3.5))
                Line((5, -3.5), (5, 3.5))
                Line((5, 3.5), (-5, 3.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 13.6, perimeter: 14.8
            with BuildLine():
                Line((0, -3.5), (1.7, -3.5))
                Line((1.7, -3.5), (1.7, 0.5))
                Line((1.7, 0.5), (-1.7, 0.5))
                Line((-1.7, -3.5), (-1.7, 0.5))
                Line((0, -3.5), (-1.7, -3.5))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, elliptical metallic plate with a fine mesh or perforated surface featuring diagonal striped patterns, likely used as a strainer, filter, or drainage component.
def model_138764_891914eb_0001():
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
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 628.318530718, perimeter: 96.8844822513
            Ellipse(20, 10)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a wheel or pulley with a circular rim and central hub connected by three equally-spaced radial spokes, featuring a central axle hole for mounting.
def model_138842_b33b37d5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0684524496, perimeter: 7.2275132886
            with BuildLine():
                Line((0.9683929295, -3.3633636637), (0.3458546177, -1.2012013085))
                CenterArc((0, 0), 1.25, -106.8376234998, 32.9)
                Line((-1.0138112677, -3.3499532405), (-0.3620754528, -1.1964118716))
                CenterArc((0, 0), 3.5, -106.8376234998, 32.9)
            make_face()
            # Profile area: 3.0684524496, perimeter: 7.2275132886
            with BuildLine():
                Line((-3.350323763, -1.0125861361), (-1.1965442011, -0.3616379057))
                CenterArc((0, 0), 1.25, 163.9166706723, 32.9)
                Line((-3.3630093015, 0.9696228327), (-1.2010747505, 0.3462938688))
                CenterArc((0, 0), 3.5, 163.9166706723, 32.9)
            make_face()
            # Profile area: 3.0684524496, perimeter: 7.2275132886
            with BuildLine():
                Line((-0.9910093342, 3.3567693545), (-0.3539319051, 1.198846198))
                CenterArc((0, 0), 1.25, 73.5480294751, 32.9)
                Line((0.9912402248, 3.3567011807), (0.354014366, 1.1988218503))
                CenterArc((0, 0), 3.5, 73.5480294751, 32.9)
            make_face()
            # Profile area: 3.0684524496, perimeter: 7.2275132886
            with BuildLine():
                CenterArc((0, 0), 3.5, -16.8303228405, 32.9)
                Line((3.3632402432, 0.9688214832), (1.2011572297, 0.3460076726))
                CenterArc((0, 0), 1.25, -16.8303228405, 32.9)
                Line((3.3500823937, -1.0133844067), (1.1964579977, -0.3619230024))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 40.0553063333, perimeter: 53.407075111
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, -73.9376234998, 57.1073006594)
                CenterArc((0, 0), 3.5, -106.8376234998, 32.9)
                CenterArc((0, 0), 3.5, -163.1833293277, 56.3457058278)
                CenterArc((0, 0), 3.5, 163.9166706723, 32.9)
                CenterArc((0, 0), 3.5, 106.4480294751, 57.4686411972)
                CenterArc((0, 0), 3.5, 73.5480294751, 32.9)
                CenterArc((0, 0), 3.5, 16.0696771595, 57.4783523156)
                CenterArc((0, 0), 3.5, -16.8303228405, 32.9)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2581806788, perimeter: 10.8479048215
            with BuildLine():
                CenterArc((0, 0), 1.25, -16.8303228405, 32.9)
                CenterArc((0, 0), 1.25, 16.0696771595, 57.4783523156)
                CenterArc((0, 0), 1.25, 73.5480294751, 32.9)
                CenterArc((0, 0), 1.25, 106.4480294751, 57.4686411972)
                CenterArc((0, 0), 1.25, 163.9166706723, 32.9)
                CenterArc((0, 0), 1.25, -163.1833293277, 56.3457058278)
                CenterArc((0, 0), 1.25, -106.8376234998, 32.9)
                CenterArc((0, 0), 1.25, -73.9376234998, 57.1073006594)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, -45.5543074815, 90.4943261073)
                Line((0.3501164496, -0.3569572408), (0.106776377, -0.3708492449))
                Line((0.106776377, -0.3708492449), (-0.0002104543, -0.3769569998))
                Line((-0.0002104543, -0.3769569998), (-0.3072175538, -0.3944836811))
                CenterArc((0, 0), 0.5, 138.3695677891, 93.7195465486)
                Line((0.3539233221, 0.3531830716), (-0.3737226729, 0.3321616531))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a nail or pin with a cylindrical shaft and a rounded, slightly enlarged head, featuring a smooth, tapered design typical of a common fastener or structural pin.
def model_138888_857538fd_0000():
    """Model: M5x50 LowP"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0577854762, perimeter: 2.9564369728
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                Line((0, 0.2309401077), (-0.2, 0.1154700538))
                Line((0.2, 0.1154700538), (0, 0.2309401077))
                Line((0.2, -0.1154700538), (0.2, 0.1154700538))
                Line((0, -0.2309401077), (0.2, -0.1154700538))
                Line((-0.2, -0.1154700538), (0, -0.2309401077))
                Line((-0.2, 0.1154700538), (-0.2, -0.1154700538))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((-0.2, 0.1154700538), (-0.2, -0.1154700538))
                Line((-0.2, -0.1154700538), (0, -0.2309401077))
                Line((0, -0.2309401077), (0.2, -0.1154700538))
                Line((0.2, -0.1154700538), (0.2, 0.1154700538))
                Line((0.2, 0.1154700538), (0, 0.2309401077))
                Line((0, 0.2309401077), (-0.2, 0.1154700538))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4398229715, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((-0.2, 0.1154700538), (-0.2, -0.1154700538))
                Line((-0.2, -0.1154700538), (0, -0.2309401077))
                Line((0, -0.2309401077), (0.2, -0.1154700538))
                Line((0.2, -0.1154700538), (0.2, 0.1154700538))
                Line((0.2, 0.1154700538), (0, 0.2309401077))
                Line((0, 0.2309401077), (-0.2, 0.1154700538))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped frame or bracket with a hollow rectangular opening, featuring uniform wall thickness and a slanted rectangular profile typical of a structural support component or trim ring.
def model_138915_28fbd2f7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 454.464, perimeter: 113.88
            with BuildLine():
                Line((3, -95), (3, -104.6))
                Line((50.34, -104.6), (3, -104.6))
                Line((50.34, -95), (50.34, -104.6))
                Line((3, -95), (50.34, -95))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.8, perimeter: 25.2
            with BuildLine():
                Line((0, -95), (3, -95))
                Line((0, -95), (0, -104.6))
                Line((3, -104.6), (0, -104.6))
                Line((3, -95), (3, -104.6))
            make_face()
            # Profile area: 28.8, perimeter: 25.2
            with BuildLine():
                Line((50.34, -95), (50.34, -104.6))
                Line((53.34, -104.6), (50.34, -104.6))
                Line((53.34, -95), (53.34, -104.6))
                Line((50.34, -95), (53.34, -95))
            make_face()
            # Profile area: 276, perimeter: 190
            with BuildLine():
                Line((50.34, -95), (53.34, -95))
                Line((53.34, -3), (53.34, -95))
                Line((50.34, -3), (53.34, -3))
                Line((50.34, -3), (50.34, -95))
            make_face()
            # Profile area: 276, perimeter: 190
            with BuildLine():
                Line((3, -3), (3, -95))
                Line((0, -3), (3, -3))
                Line((0, -3), (0, -95))
                Line((0, -95), (3, -95))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 160.02, perimeter: 112.68
            with BuildLine():
                Line((3, -3), (50.34, -3))
                Line((50.34, -3), (53.34, -3))
                Line((53.34, 0), (53.34, -3))
                Line((0, 0), (53.34, 0))
                Line((0, 0), (0, -3))
                Line((0, -3), (3, -3))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal coffin or casket-shaped container with a tapered top lid featuring angled faceted surfaces and a dark navy base with lighter blue panel inlays on the upper portion.
def model_138954_6b7ae636_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0244, perimeter: 9.52
            with BuildLine():
                Line((-0.575502436, 0.2871503301), (-2.155502436, 0.2871503301))
                Line((-0.575502436, 3.4671503301), (-0.575502436, 0.2871503301))
                Line((-2.155502436, 3.4671503301), (-0.575502436, 3.4671503301))
                Line((-2.155502436, 0.2871503301), (-2.155502436, 3.4671503301))
            make_face()
        # OneSide extrude, distance=0.96
        extrude(amount=0.96)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.96, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1809557368, perimeter: 1.5079644737
            with Locations((0.965502436, -3.0771503301)):
                Circle(0.24)
        # OneSide extrude, distance=0.12
        extrude(amount=0.12, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or rod with a circular flange on one end, featuring a smooth body extending horizontally with a larger diameter disk-like feature at the left terminus.
def model_139222_2c10ca9a_0019():
    """Model: Untitled v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=32
        extrude(amount=32)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a rugged smartphone case with a rectangular body, rounded corners, and reinforced edges featuring a dark blue/navy color scheme with protective bumpers at the corners and sides.
def model_139253_33608dfd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 35 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.059734239, perimeter: 81.1946903808
            with BuildLine():
                CenterArc((-5.0000000909, -5.0000000909), 1.1, 180, 90)
                Line((0.0000000164, -6.1000000909), (-5.0000000909, -6.1000000909))
                CenterArc((0.0000000164, -5.0000000909), 1.1, -90, 90)
                Line((1.1000000164, 7.0000001207), (1.1000000164, -5.0000000909))
                CenterArc((0.0000000164, 7.0000001207), 1.1, 0, 90)
                Line((-5.0000000909, 8.1000001207), (0.0000000164, 8.1000001207))
                CenterArc((-5.0000000909, 7.0000001207), 1.1, 90, 90)
                Line((-6.1000000909, -5.0000000909), (-6.1000000909, 7.0000001207))
            make_face()
            with BuildLine():
                Line((-6.0000000894, 0.6000000089), (-6.0000002991, 3.1984560351))
                Line((-6.0000001331, 7.0000001192), (-6.0000002991, 3.1984560351))
                CenterArc((-5.0000001331, 7.0000000755), 1, 89.999997498, 90)
                Line((-3.2701438395, 8), (-5.0000000894, 8.0000000755))
                Line((-0.000000013, 8.0000000913), (-3.2701438395, 8))
                CenterArc((0.0000000149, 7.0000000913), 1, 0, 90.0000015995)
                Line((1.0000000149, -5.0000000894), (1.0000000149, 7.0000000913))
                CenterArc((0.0000000149, -5.0000000894), 1, -90, 90)
                Line((-5.0000000894, -6.0000000894), (0.0000000149, -6.0000000894))
                CenterArc((-5.0000000894, -5.0000000894), 1, 180, 90)
                Line((-6.0000000894, 0.6000000089), (-6.0000000894, -5.0000000894))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 97.1415926536, perimeter: 40.2831853072
            with BuildLine():
                CenterArc((-5, -5), 1, 180, 90)
                Line((-5, -6), (0, -6))
                CenterArc((0, -5), 1, -90, 90)
                Line((1, -5), (1, 7))
                CenterArc((0, 7), 1, 0, 90)
                Line((0, 8), (-5, 8))
                CenterArc((-5, 7), 1, 90, 90)
                Line((-6, 7), (-6, -5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a circular disk or wheel with a mesh or perforated section featuring a large flat face and a textured, grid-patterned curved side, likely representing a fan blade, filter housing, or ventilation component.
def model_139371_557edc08_0000():
    """Model: Final Exam Component 1 v3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0106193582, perimeter: 5.0265483206
            Circle(0.8000000119)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical or oval-shaped container or housing with a mesh or perforated top surface and a solid dark body, resembling a filter basket or ventilation enclosure with an open grid-pattern lid.
def model_139383_d8f77b30_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.4134441667, perimeter: 21.3912326607
            Circle(3.4045204168)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a dark blue angled bracket or connector with a lightning bolt-like zigzag shape, featuring two rectangular notches or slots cut into opposite sides along its length.
def model_139518_5ee97bb7_0000():
    """Model: Frame Side"""
    with BuildPart() as part:
        # 1515 Frame Mount -> Extrude6 (NewBody)
        # Sketch on HALO Plane construction plane
        # Sketch has 34 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.4, perimeter: 11.6
            with BuildLine():
                Line((-5.8305640716, -6.8172071324), (-5.8305634584, -9.8172071324))
                Line((-5.8305634584, -9.8172071324), (-4.5305634584, -9.8172068667))
                Line((-4.5305634584, -9.8172068667), (-3.0305634584, -9.8172065601))
                Line((-3.0305640716, -6.8172065601), (-3.0305634584, -9.8172065601))
                Line((-3.0305640716, -6.8172065601), (-4.5305640716, -6.8172068667))
                Line((-4.5305640716, -6.8172068667), (-5.8305640716, -6.8172071324))
            make_face()
            # Profile area: 2.2499997701, perimeter: 5.9999996934
            with BuildLine():
                Line((-3.0305640716, -6.8172065601), (-4.5305640716, -6.8172068667))
                Line((-3.0305643782, -5.3172068667), (-3.0305640716, -6.8172065601))
                Line((-4.5305643782, -5.3172068667), (-3.0305643782, -5.3172068667))
                Line((-4.5305643782, -5.3172068667), (-4.5305640716, -6.8172068667))
            make_face()
            # Profile area: 0.3, perimeter: 3.4
            with BuildLine():
                Line((-4.5305634584, -9.8172068667), (-3.0305634584, -9.8172065601))
                Line((-4.5305634175, -10.0172068667), (-4.5305634584, -9.8172068667))
                Line((-3.0305634175, -10.0172065601), (-4.5305634175, -10.0172068667))
                Line((-3.0305634584, -9.8172065601), (-3.0305634175, -10.0172065601))
            make_face()
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((-3.0305634175, -10.0172065601), (-4.5305634175, -10.0172068667))
                Line((-4.5305634175, -10.0172068667), (-4.5305631109, -11.5172068667))
                Line((-3.0305631109, -11.5172065601), (-4.5305631109, -11.5172068667))
                Line((-3.0305634175, -10.0172065601), (-3.0305631109, -11.5172065601))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a brake caliper bracket with a curved, hook-like shape featuring two mounting flanges with holes on each end, a central curved arm with internal ribbing for structural reinforcement, and a slot opening on the side.
def model_139677_8e558c30_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 27.8336269741, perimeter: 46.3893782902
            with BuildLine():
                Line((-2.7, 5), (-2.7, 0))
                CenterArc((0, 0), 2.7, 180, 162.9479257995)
                CenterArc((0, 0), 2.7, -17.0520742005, 17.0520742005)
                Line((2.7, 0), (2.7, 5))
                CenterArc((0, 5), 2.7, 0, 129.0434605518)
                CenterArc((0, 5), 2.7, 129.0434605518, 50.9565394482)
            make_face()
            with BuildLine():
                Line((-1.5, 5), (-1.5, 0))
                CenterArc((0, 5), 1.5, 0, 180)
                Line((1.5, 0), (1.5, 5))
                CenterArc((0, 0), 1.5, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 105.7370795523, perimeter: 69.3841789614
            with BuildLine():
                CenterArc((0, 5), 2.7, 0, 129.0434605518)
                Line((2.7, 0), (2.7, 5))
                CenterArc((0, 0), 2.7, -17.0520742005, 17.0520742005)
                CenterArc((16.9218838262, -5.1903610444), 15, 90, 72.9479257995)
                CenterArc((16.9218838262, 2.8096389556), 7, 61.0772400116, 28.9227599884)
                CenterArc((22, 12), 3.5, 90, 151.0772400116)
                CenterArc((22, -22.1256410256), 37.6256410256, 90, 39.0434605518)
            make_face()
            # Profile area: 28.8633825049, perimeter: 32.9867228627
            with BuildLine():
                CenterArc((22, 12), 3.5, 90, 151.0772400116)
                CenterArc((22, 12), 3.5, -118.9227599884, 208.9227599884)
            make_face()
            with BuildLine():
                CenterArc((22, 12), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=3
        extrude(amount=1.5, both=True)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 27.8336269741, perimeter: 46.3893782902
            with BuildLine():
                Line((-2.7, 5), (-2.7, 0))
                CenterArc((0, 0), 2.7, 180, 162.9479257995)
                CenterArc((0, 0), 2.7, -17.0520742005, 17.0520742005)
                Line((2.7, 0), (2.7, 5))
                CenterArc((0, 5), 2.7, 0, 129.0434605518)
                CenterArc((0, 5), 2.7, 129.0434605518, 50.9565394482)
            make_face()
            with BuildLine():
                Line((-1.5, 5), (-1.5, 0))
                CenterArc((0, 5), 1.5, 0, 180)
                Line((1.5, 0), (1.5, 5))
                CenterArc((0, 0), 1.5, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.8633825049, perimeter: 32.9867228627
            with BuildLine():
                CenterArc((22, 12), 3.5, 90, 151.0772400116)
                CenterArc((22, 12), 3.5, -118.9227599884, 208.9227599884)
            make_face()
            with BuildLine():
                CenterArc((22, 12), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 9.2088315753, perimeter: 18.260214187
            with BuildLine():
                Line((10, 18), (10, 13.535105778))
                CenterArc((22, -22.1256410256), 37.6256410256, 102.2759917054, 6.3223237141)
                Line((14, 18), (14, 14.6396804416))
                CenterArc((12, 18), 2, 180, 180)
            make_face()
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((12, 18), 2, 180, 180)
                CenterArc((12, 18), 2, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((12, 18), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a curved structural bracket or lever arm with a cylindrical mounting boss at one end, a curved body with reinforcing ribs along its length, and rectangular slots or cutouts near the opposite end for fastening or attachment purposes.
def model_139744_58088e94_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 132.704892898, perimeter: 73.401369997
            with BuildLine():
                CenterArc((0, 0), 2.7, -17.0520742005, 17.0520742005)
                CenterArc((16.9218838262, -5.1903610444), 15, 90, 72.9479257995)
                CenterArc((16.9218838262, 2.8096389556), 7, 61.0772400116, 28.9227599884)
                CenterArc((22, 12), 3.5, 75.5712383532, 165.5060016584)
                CenterArc((16.9218838262, -7.736820001), 23.8796302132, 75.5712383532, 26.3233773074)
                CenterArc((16.9218838262, -7.736820001), 23.8796302132, 101.8946156606, 10.0443693234)
                CenterArc((16.9218838262, -7.736820001), 23.8796302132, 111.9389849839, 31.0928479205)
                CenterArc((0, 5), 2.7, 0, 143.0318329044)
                Line((2.7, 0), (2.7, 5))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.8336269741, perimeter: 46.3893782902
            with BuildLine():
                Line((2.7, 0), (2.7, 5))
                CenterArc((0, 5), 2.7, 0, 143.0318329044)
                CenterArc((0, 5), 2.7, 143.0318329044, 36.9681670956)
                Line((-2.7, 5), (-2.7, 0))
                CenterArc((0, 0), 2.7, -180, 162.9479257995)
                CenterArc((0, 0), 2.7, -17.0520742005, 17.0520742005)
            make_face()
            with BuildLine():
                Line((1.5, 0), (1.5, 5))
                CenterArc((0, 0), 1.5, 180, 180)
                Line((-1.5, 5), (-1.5, 0))
                CenterArc((0, 5), 1.5, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.8633825049, perimeter: 32.9867228627
            with BuildLine():
                CenterArc((22, 12), 3.5, -118.9227599884, 194.4939983416)
                CenterArc((22, 12), 3.5, 75.5712383532, 165.5060016584)
            make_face()
            with BuildLine():
                CenterArc((22, 12), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.7988126085, perimeter: 22.7090679626
            with BuildLine():
                Line((12, 18), (12, 15.630075358))
                CenterArc((10, 18), 2, 0, 180)
                Line((8, 14.413501173), (8, 18))
                CenterArc((16.9218838262, -7.736820001), 23.8796302132, 101.8946156606, 10.0443693234)
            make_face()
            with BuildLine():
                CenterArc((10, 18), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a tapered cylindrical rod or stylus with a pointed tip, featuring a smooth conical shape that gradually narrows from a thicker rounded end to a sharp point.
def model_139801_97e2ca6a_0004():
    """Model: zip tie v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1160000315, perimeter: 21.4288021071
            with BuildLine():
                Line((0, 0), (0, -10.16))
                Line((0, -10.16), (0.1000000015, -10.5000001565))
                Line((0.200000003, -10.5000001565), (0.1000000015, -10.5000001565))
                Line((0.3, -10.16), (0.200000003, -10.5000001565))
                Line((0.3, 0), (0.3, -10.16))
                Line((0, 0), (0.3, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a grinding wheel or abrasive disc with a circular disc shape, a central axle hole, and a textured abrasive surface featuring radial grooves or flutes across its face for material removal applications.
def model_139939_3daabd82_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.7215246471, perimeter: 20.5475867508
            with BuildLine():
                CenterArc((0, 0), 2.25425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.381
        extrude(amount=0.1905, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.845390896, perimeter: 10.7842662721
            with BuildLine():
                CenterArc((0, 0), 1.016, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.3667125, -0.6351646818), (0.3667125, -0.6351646818))
                Line((-0.733425, 0), (-0.3667125, -0.6351646818))
                Line((-0.3667125, 0.6351646818), (-0.733425, 0))
                Line((0.3667125, 0.6351646818), (-0.3667125, 0.6351646818))
                Line((0.733425, 0), (0.3667125, 0.6351646818))
                Line((0.3667125, -0.6351646818), (0.733425, 0))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.762
        extrude(amount=0.381, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8003060932, perimeter: 29.9236700254
            with BuildLine():
                CenterArc((0, 0), 2.50825, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.9652
        extrude(amount=0.4826, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.8167101363, perimeter: 34.7114572295
            with BuildLine():
                CenterArc((0, 0), 3.01625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.50825, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.016
        extrude(amount=0.508, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a disk or wheel with a central hole, featuring a toroidal (donut-shaped) profile with a flat top surface, a recessed inner rim, and a mesh-textured outer edge, commonly used as a pulley, spacer, or mounting component.
def model_139940_dba1c52b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9942355909, perimeter: 16.5577640807
            with BuildLine():
                CenterArc((0, 0), 1.61925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.381
        extrude(amount=0.1905, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.845390896, perimeter: 10.7842662721
            with BuildLine():
                CenterArc((0, 0), 1.016, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.3667125, -0.6351646818), (0.3667125, -0.6351646818))
                Line((-0.733425, 0), (-0.3667125, -0.6351646818))
                Line((-0.3667125, 0.6351646818), (-0.733425, 0))
                Line((0.3667125, 0.6351646818), (-0.3667125, 0.6351646818))
                Line((0.733425, 0), (0.3667125, 0.6351646818))
                Line((0.3667125, -0.6351646818), (0.733425, 0))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.762
        extrude(amount=0.381, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.786891135, perimeter: 21.9440246853
            with BuildLine():
                CenterArc((0, 0), 1.87325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.61925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.9652
        extrude(amount=0.4826, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.7898802199, perimeter: 26.7318118894
            with BuildLine():
                CenterArc((0, 0), 2.38125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.87325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.016
        extrude(amount=0.508, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a black plastic mounting bracket or clamp assembly featuring a curved top section with blue reinforcing ribs, a central rectangular body with horizontal mounting slots on both sides, and a solid base for attachment.
def model_140059_6f242172_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7199570614, perimeter: 7.7673921455
            with BuildLine():
                CenterArc((0.0412504324, -1.3423583576), 2.3756185605, -130.5996867814, 27.4068996318)
                Line((-0.5009329684, -3.6552787421), (-0.400000006, -3.5000000522))
                CenterArc((0.1176100195, -1.456940827), 2.107607918, -134.6243133246, 30.4075369332)
                CenterArc((-48.6935114199, -58.0422136981), 72.6262363524, 49.3299951094, 1.1725156493)
                CenterArc((-4.1767815155, -4.2600351923), 2.8141348691, 53.4272764804, 23.1321798219)
                Line((-3.5695669675, -1.643244476), (-3.5226746944, -1.522974848))
                CenterArc((-4.7178047244, -4.8853631544), 3.4394452272, 54.0792456265, 16.4185038511)
                CenterArc((-8.3931037904, -9.8107816131), 9.5847578432, 44.0544024764, 9.5060216347)
            make_face()
            # Profile area: 7.09564938, perimeter: 13.8259731625
            with BuildLine():
                CenterArc((-0.0805420056, -5.6887626328), 2.9143469269, 119.253992852, 20.348167031)
                CenterArc((-8.3931037904, -9.8107816131), 9.5847578432, 44.0544024764, 9.5060216347)
                CenterArc((-3.3016308521, -2.2327897656), 0.6161109863, -72.6980248985, 85.1445845099)
                CenterArc((-17.4725129582, 47.818762807), 52.634860355, -74.4927043397, 0.3183699833)
                CenterArc((-4.3571429221, -2.807142899), 0.961636587, -68.1985905136, 62.6573857356)
                CenterArc((-4.7440000782, -2.4620000217), 1.4443614888, -67.8744727703, 8.8790478948)
                CenterArc((-4.8660000725, -3.8460000573), 0.6675867084, -101.5792408527, 105.5303320369)
                CenterArc((-5.8348485718, -4.1863636987), 0.8918182466, -114.1700456602, 93.5798212165)
                CenterArc((-0.0639369527, -4.0327874504), 6.2118251033, -171.0423100796, 10.7048001165)
                CenterArc((-5.5271704556, -6.0525133289), 0.3927514935, -169.6707983622, 69.0327253457)
                CenterArc((-5.0500000753, -10.3092446658), 3.9095643123, 89.2672157585, 8.8151932811)
                CenterArc((-2.7597605347, -8.478287534), 3.0558062559, 122.4634595174, 14.6842231497)
                CenterArc((-6.8500001021, -1.2500000186), 5.2559490887, -62.2160735878, 11.8122822275)
                CenterArc((-5.067179637, -3.3495604258), 2.5020524959, -51.2180991373, 21.2336089846)
                CenterArc((1.2670013867, -7.1002511317), 4.8595428072, 137.2244688224, 11.8112670635)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.3749001095, perimeter: 46.3640569879
            with BuildLine():
                CenterArc((-48.6935114199, -58.0422136981), 72.6262363524, 49.3299951094, 1.1725156493)
                Line((-1.3628899878, -2.9569844478), (-0.7232236224, -2.3097976106))
                Line((-0.7232236224, -2.3097976106), (-0.9563763431, -2.2922080008))
                CenterArc((-0.8920437806, -2.1972642174), 0.1146865319, 102.9171177208, 132.961871717)
                Line((-0.9176809601, -2.085479891), (-0.5223831323, -2.0566835682))
                Line((-0.5223831323, -2.0566835682), (-0.3226272852, -1.8545792184))
                Line((-0.3226272852, -1.8545792184), (-0.5296895245, -1.8175602608))
                CenterArc((-0.4752523429, -1.7232603892), 0.1088846753, 103.6418272827, 136.3613055489)
                Line((-0.5009329684, -1.6174474505), (-0.1227845604, -1.5899004142))
                Line((-0.1227845604, -1.5899004142), (0.1000000015, -1.4000000209))
                Line((0.1000000015, -1.4000000209), (-0.1195409547, -1.3462201705))
                CenterArc((-0.0462390131, -1.2550001901), 0.1170224742, 113.5951428942, 117.6204274744)
                Line((-0.0930797567, -1.1477611851), (0.2832624719, -1.1203457238))
                Line((0.2832624719, -1.1203457238), (0.5000000075, -0.9000000134))
                Line((0.5000000075, -0.9000000134), (0.305492039, -0.8798415548))
                CenterArc((0.4135382698, -0.7975814979), 0.1357965573, 102.1850890879, 115.0984268822)
                Line((0.3848756331, -0.6648443206), (0.7265137064, -0.6697153893))
                Line((0.7265137064, -0.6697153893), (0.9306184517, -0.4622127757))
                Line((0.9306184517, -0.4622127757), (0.7702168297, -0.4266935382))
                CenterArc((0.8131282469, -0.320106174), 0.1149010702, 106.6846095756, 141.3859779277)
                Line((0.780139779, -0.2100424791), (1.1635764889, -0.2100424791))
                Line((1.1635764889, -0.2100424791), (1.3627362478, -0.0075671745))
                Line((1.3627362478, -0.0075671745), (1.1406736025, 0.0231468287))
                CenterArc((1.2308206421, 0.1203506406), 0.1325709991, 102.6159661576, 124.5411215656)
                Line((1.201865123, 0.249720837), (1.566082841, 0.249720837))
                Line((1.566082841, 0.249720837), (1.7751792457, 0.4622982094))
                Line((1.7751792457, 0.4622982094), (1.6202828172, 0.4895254443))
                CenterArc((1.6403151936, 0.5941287185), 0.1065041833, 98.1349583245, 161.0236994434)
                Line((1.6252442918, 0.6995612039), (2.0000000298, 0.6995612039))
                Line((2.0000000298, 0.6995612039), (2.2066826221, 0.9096845796))
                Line((2.2066826221, 0.9096845796), (2.0552387601, 0.9310966868))
                CenterArc((2.097689508, 1.0475769641), 0.1239746788, 95.8713005203, 154.1046426041)
                Line((2.0850076079, 1.1709012942), (2.4168211052, 1.1239873679))
                Line((2.4168211052, 1.1239873679), (2.6833457245, 1.3949490009))
                Line((2.6833457245, 1.3949490009), (2.5150020763, 1.4322056249))
                CenterArc((2.541575161, 1.5347023084), 0.1058853103, 90.060543198, 165.405069552)
                Line((2.5414632743, 1.6405875596), (2.9253609502, 1.640993216))
                Line((2.9253609502, 1.640993216), (3.8555032026, 2.5557499567))
                CenterArc((12.8472855852, -0.4834969087), 9.4915315901, 132.6040550987, 28.7205519906)
                CenterArc((9.4198244142, -3.5641786392), 10.5037391639, 106.5819391916, 38.0378964479)
                CenterArc((0.7252399205, 2.3799734939), 0.1896316333, -113.9019631825, 160.3790600057)
                CenterArc((0.5395742808, 2.0900365755), 0.1594757973, -126.3013804549, 173.2670786731)
                CenterArc((0.3235928134, 1.8349515982), 0.1754883872, -122.2472442307, 168.4004033978)
                CenterArc((0.1068086246, 1.5759414531), 0.1655163807, -117.7668118152, 159.6914668396)
                CenterArc((-0.1016814677, 1.3099271165), 0.1776363048, -126.1327953471, 168.4352153553)
                CenterArc((-0.3157955132, 1.0423700565), 0.1654074538, -120.602112125, 169.2098081026)
                CenterArc((-0.5423776673, 0.7881375011), 0.1810652371, -116.0476861772, 154.2035068827)
                CenterArc((-0.7440143419, 0.5088951816), 0.1688290226, -127.186378444, 170.8521574802)
                CenterArc((-0.9937261792, 0.2721786564), 0.1795948045, -109.0322432656, 143.7226395514)
                CenterArc((-1.1939249889, 0.0025634694), 0.1732844081, -123.0452413294, 158.2254820264)
                CenterArc((-5.533560472, 2.6335604288), 5.0723575285, -47.3968768303, 14.2128789097)
                CenterArc((-2.550000038, -1.3500000201), 0.5147815147, -60.9453959009, 90)
                CenterArc((-2.777025216, -1.522974848), 0.5516302872, -59.8547686855, 29.709537371)
            make_face()
            with BuildLine():
                CenterArc((3.0587222922, 2.2747901197), 0.1600325414, 159.2932141584, 128.3172562853)
                Line((2.9090275073, 2.3313753268), (3.2678297761, 2.6923788365))
                CenterArc((3.3341077905, 2.5557499567), 0.1518559382, -31.3886505233, 147.2664516455)
                Line((3.1071391895, 2.1222574401), (3.4637402174, 2.4766572271))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.4442093603, -1.8298977848), (2.2697253288, 2.1851667439))
                CenterArc((2.3547154555, 2.1065508768), 0.1157746786, -66.9742937873, 204.2054683953)
                Line((-1.3000000194, -2.0000000298), (2.4000000358, 2.0000000298))
                CenterArc((-1.4156400927, -1.9518573664), 0.1252610977, 103.1839263893, 234.2133934507)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2376486084, perimeter: 1.7281147209
            with Locations((-4.9009687191, 5.6500133374)):
                Circle(0.2750380001)
        # OneSide extrude, distance=-2.7661
        extrude(amount=-2.7661, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or pin with a slightly tapered or rounded end, featuring a smooth, uniform shaft with a simple geometric form suitable for mechanical assembly or fastening applications.
def model_140194_b0abb2bf_0003():
    """Model: Legs (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 933.8691, perimeter: 260.35
            with BuildLine():
                Line((190.5, -122.555), (182.88, -122.555))
                Line((190.5, 0), (190.5, -122.555))
                Line((182.88, 0), (190.5, 0))
                Line((182.88, -122.555), (182.88, 0))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 933.8691, perimeter: 260.35
            with BuildLine():
                Line((0, -122.555), (0, 0))
                Line((0, 0), (-7.62, 0))
                Line((-7.62, 0), (-7.62, -122.555))
                Line((-7.62, -122.555), (0, -122.555))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a flat, rectangular panel or plate with a diamond-like rotated orientation, featuring diagonal reinforcement ribs or creases running across its surface and a small protruding flange or bracket on one edge.
def model_140194_b0abb2bf_0011():
    """Model: Left Arm Support Front"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.43), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 127.015875, perimeter: 137.16
            with BuildLine():
                Line((-5.715, -114.935), (-3.81, -114.935))
                Line((-3.81, -114.935), (-3.81, -48.26))
                Line((-3.81, -48.26), (-5.715, -48.26))
                Line((-5.715, -48.26), (-5.715, -114.935))
            make_face()
        # OneSide extrude, distance=83.82
        extrude(amount=83.82)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 95.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 156.048075, perimeter: 156.21
            with BuildLine():
                Line((-5.715, -48.26), (-7.62, -48.26))
                Line((-7.62, -48.26), (-7.62, -122.555))
                Line((-7.62, -122.555), (-3.81, -122.555))
                Line((-3.81, -122.555), (-3.81, -114.935))
                Line((-5.715, -114.935), (-3.81, -114.935))
                Line((-5.715, -48.26), (-5.715, -114.935))
            make_face()
            # Profile area: 127.015875, perimeter: 137.16
            with BuildLine():
                Line((-5.715, -48.26), (-5.715, -114.935))
                Line((-5.715, -114.935), (-3.81, -114.935))
                Line((-3.81, -114.935), (-3.81, -48.26))
                Line((-3.81, -48.26), (-5.715, -48.26))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)
    return part.part


# Description: This is a shoulder bolt or shoulder screw, featuring a cylindrical shaft with a larger diameter head at one end, commonly used as a pivot pin or hinge component in mechanical assemblies.
def model_140760_c36e4bec_0026():
    """Model: pin 110x30 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical pin or dowel with a uniform shaft and a slightly enlarged circular head or flange at one end, designed for alignment or fastening applications.
def model_140760_c36e4bec_0027():
    """Model: pin 60x20 v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or pin with a long, smooth shaft and a larger diameter head or flange at one end, designed for assembly or alignment purposes.
def model_140760_c36e4bec_0028():
    """Model: pin 20x80 v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular sheet metal tray or pan with a parallelogram shape (skewed top view), featuring a shallow depth, flat bottom, and raised edge flanges on all sides.
def model_140862_9005288e_0000():
    """Model: Case"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 602.775, perimeter: 113.7
            with BuildLine():
                Line((21.375, -7.05), (21.375, 7.05))
                Line((21.375, 7.05), (-21.375, 7.05))
                Line((-21.375, 7.05), (-21.375, -7.05))
                Line((-21.375, -7.05), (21.375, -7.05))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 267.9, perimeter: 75.8
            with BuildLine():
                Line((14.25, -4.7), (-14.25, -4.7))
                Line((14.25, 4.7), (14.25, -4.7))
                Line((-14.25, 4.7), (14.25, 4.7))
                Line((-14.25, -4.7), (-14.25, 4.7))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a computer mouse pad featuring an ergonomic contoured shape with a curved, elevated wrist rest on one end and a flat mousing surface, combining a textured mesh material on top with a solid base for comfort and stability.
def model_141177_0ce4dd24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 301.5928947446, perimeter: 72.7337250239
            Ellipse(16, 6)
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a flat steel mounting plate with a parallelogram shape, featuring two mounting holes near the top corners for fastening purposes.
def model_141186_d75414a5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17, perimeter: 21
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (8.5, 0))
                Line((8.5, 0), (8.5, 2))
                Line((8.5, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.04), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.5, 1)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((8, 1)):
                Circle(0.15)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, trapezoidal or parallelogram-shaped plate with a triangular internal division, featuring a simple geometric form with no holes, slots, or curves—essentially a planar structural element with clean edges and a divided surface.
def model_141665_0564e852_0002():
    """Model: Table bottom v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11200, perimeter: 440
            with BuildLine():
                Line((140, -80), (0, -80))
                Line((140, 0), (140, -80))
                Line((0, 0), (140, 0))
                Line((0, -80), (0, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 68
            with BuildLine():
                Line((-32, 78), (0, 78))
                Line((0, 78), (0, 80))
                Line((0, 80), (-32, 80))
                Line((-32, 80), (-32, 78))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered bracket or support arm with a rectangular cross-section, featuring a mounting hole at the wide end and longitudinal slots or ribs running along its length, designed to provide structural support while minimizing weight.
def model_141694_b5ac3112_0000():
    """Model: wheelHolder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0270383931, perimeter: 22.8517030409
            with BuildLine():
                Line((0.563202433, -2.8847857828), (1.0083971304, -2.6001452342))
                Line((1.0083971304, -2.6001452342), (-1.2464753154, 3.4695364352))
                Line((-1.2464753154, 3.4695364352), (-3.3859438225, 1.560635069))
                Line((-3.3859438225, 1.560635069), (0.563202433, -2.8847857828))
            make_face()
            with BuildLine():
                Line((-2.2188930804, 1.663789965), (-1.3524314987, 2.4368743509))
                CenterArc((-2.3853320814, 1.8503323434), 0.25, 131.740350126, 180)
                Line((-1.6853095007, 2.8099591077), (-2.5517710824, 2.0368747218))
                CenterArc((-1.5188704997, 2.6234167293), 0.25, -48.259649874, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.8330337896, 1.450878741), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5114753397, -2.2579782039), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7769559351, perimeter: 3.8932219039
            with BuildLine():
                CenterArc((-1.5188704997, 2.6234167293), 0.25, -48.259649874, 180)
                Line((-1.6853095007, 2.8099591077), (-2.5517710824, 2.0368747218))
                CenterArc((-2.3853320814, 1.8503323434), 0.25, 131.740350126, 180)
                Line((-2.2188930804, 1.663789965), (-1.3524314987, 2.4368743509))
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.8330337896, 1.450878741)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.5114753397, -2.2579782039)):
                Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7769559351, perimeter: 3.8932219039
            with BuildLine():
                CenterArc((-1.5188704997, 2.6234167293), 0.25, -48.259649874, 180)
                Line((-1.6853095007, 2.8099591077), (-2.5517710824, 2.0368747218))
                CenterArc((-2.3853320814, 1.8503323434), 0.25, 131.740350126, 180)
                Line((-2.2188930804, 1.663789965), (-1.3524314987, 2.4368743509))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.8330337896, 1.450878741)):
                Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.5114753397, -2.2579782039)):
                Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or corner connector with an L-shaped profile featuring two perpendicular flanges composed of stacked cubic blocks, designed to provide structural support or alignment with a modular, segmented construction.
def model_141706_43d0b09e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.77, perimeter: 23.6
            with BuildLine():
                Line((-1.1, 2.2), (0, 2.2))
                Line((-1.1, 1.1), (-1.1, 2.2))
                Line((-3.7, 1.1), (-1.1, 1.1))
                Line((-3.7, 3.7), (-3.7, 1.1))
                Line((-2.6, 3.7), (-3.7, 3.7))
                Line((-2.6, 4.8), (-2.6, 3.7))
                Line((-4.8, 4.8), (-2.6, 4.8))
                Line((-4.8, 0), (-4.8, 4.8))
                Line((0, 0), (-4.8, 0))
                Line((0, 2.2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.27, perimeter: 14.8
            with BuildLine():
                Line((2.5, 0), (2.5, 2.6))
                Line((2.5, 0), (5.1, 0))
                Line((5.1, 1.1), (5.1, 0))
                Line((6.2, 1.1), (5.1, 1.1))
                Line((6.2, 3.7), (6.2, 1.1))
                Line((3.6, 3.7), (6.2, 3.7))
                Line((3.6, 2.6), (3.6, 3.7))
                Line((2.5, 2.6), (3.6, 2.6))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a rectangular box-shaped enclosure or housing with an open top, featuring internal structural ribs and multiple apertures or cutouts along its sides for component mounting or cable routing.
def model_141720_481ac718_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.03216, perimeter: 29.972
            with BuildLine():
                Line((10.16, -4.826), (0, -4.826))
                Line((10.16, 0), (10.16, -4.826))
                Line((0, 0), (10.16, 0))
                Line((0, -4.826), (0, 0))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.8530545838, perimeter: 26.8563383879
            with BuildLine():
                Line((-6.731090712, 4.064), (-9.398, 4.064))
                Line((-9.398, 4.064), (-9.398, 0.762))
                Line((-9.398, 0.762), (-8.03402, 0.762))
                CenterArc((-7.239, 0.762), 0.79502, 0, 180)
                Line((-6.44398, 0.762), (-3.71602, 0.762))
                CenterArc((-2.921, 0.762), 0.79502, 0, 180)
                Line((-2.12598, 0.762), (-0.762, 0.762))
                Line((-0.762, 0.762), (-0.762, 4.064))
                Line((-0.762, 4.064), (-3.4317636467, 4.064))
                Line((-4.740672008, 2.7501650687), (-3.4317636467, 4.064))
                CenterArc((-5.0789632986, 3.087187847), 0.47752, -135, 90.1076244631)
                Line((-5.4166209288, 2.7495302168), (-6.731090712, 4.064))
            make_face()
            # Profile area: 1.4528714673, perimeter: 5.9665538743
            with BuildLine():
                Line((-4.5073758487, 4.064), (-3.7482331684, 4.826))
                Line((-3.7482331684, 4.826), (-6.4154599774, 4.826))
                Line((-5.6534599774, 4.064), (-6.4154599774, 4.826))
                Line((-4.5073758487, 4.064), (-5.6534599774, 4.064))
            make_face()
            # Profile area: 0.2761166213, perimeter: 2.554898841
            with BuildLine():
                CenterArc((-5.08, 4.191), 0.4953, -135, 90.1076244631)
                Line((-4.7291127571, 3.8414285012), (-4.5073758487, 4.064))
                Line((-4.5073758487, 4.064), (-5.6534599774, 4.064))
                Line((-5.4302299887, 3.8407700113), (-5.6534599774, 4.064))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_134013_9b4cfef2_0008": {"func": model_134013_9b4cfef2_0008, "volume": 2.16592, "area": 35.0898805029},
    "model_134027_a6a95d00_0002": {"func": model_134027_a6a95d00_0002, "volume": 122.9673281582, "area": 246.1742109856},
    "model_134123_e3bfe65c_0000": {"func": model_134123_e3bfe65c_0000, "volume": 97.902, "area": 164.64},
    "model_134129_059b7f53_0000": {"func": model_134129_059b7f53_0000, "volume": 151.1736715327, "area": 625.8362787842},
    "model_134129_059b7f53_0001": {"func": model_134129_059b7f53_0001, "volume": 79.3278759595, "area": 267.2530964915},
    "model_134444_f4a48508_0001": {"func": model_134444_f4a48508_0001, "volume": 98.322384, "area": 151.6763574139},
    "model_134564_f00f1c90_0000": {"func": model_134564_f00f1c90_0000, "volume": 23182, "area": 23718},
    "model_134568_1011a501_0000": {"func": model_134568_1011a501_0000, "volume": 42.1000847298, "area": 150.6957687337},
    "model_134602_7dd4fb67_0000": {"func": model_134602_7dd4fb67_0000, "volume": 148729749907.1105957031, "area": 214683924.0771254301},
    "model_134629_2bffd7ca_0001": {"func": model_134629_2bffd7ca_0001, "volume": 0.0692792865, "area": 3.3779524311},
    "model_134763_dca8d2ef_0002": {"func": model_134763_dca8d2ef_0002, "volume": 9.4497338861, "area": 35.7795479301},
    "model_134769_524913ff_0000": {"func": model_134769_524913ff_0000, "volume": 37.3533350374, "area": 153.3317088975},
    "model_134947_91949c2f_0000": {"func": model_134947_91949c2f_0000, "volume": 40.2123859659, "area": 65.3451271947},
    "model_134948_f1f30b1b_0000": {"func": model_134948_f1f30b1b_0000, "volume": 53.4235468766, "area": 164.8141457046},
    "model_134996_bcf890ef_0000": {"func": model_134996_bcf890ef_0000, "volume": 0.3640320487, "area": 7.5963710364},
    "model_135001_e76e4574_0000": {"func": model_135001_e76e4574_0000, "volume": 0.3787293838, "area": 6.91808155},
    "model_135008_353681c9_0000": {"func": model_135008_353681c9_0000, "volume": 23.5480000659, "area": 278.6400003767},
    "model_135033_4c0f554a_0000": {"func": model_135033_4c0f554a_0000, "volume": 3.5397189139, "area": 32.4086507643},
    "model_135092_c3610d5c_0001": {"func": model_135092_c3610d5c_0001, "volume": 0.0590526207, "area": 1.2077808723},
    "model_135092_c3610d5c_0002": {"func": model_135092_c3610d5c_0002, "volume": 0.1879402001, "area": 3.0120689483},
    "model_135092_c3610d5c_0003": {"func": model_135092_c3610d5c_0003, "volume": 0.0903748566, "area": 1.6615438924},
    "model_135092_c3610d5c_0006": {"func": model_135092_c3610d5c_0006, "volume": 0.0062714944, "area": 0.3651333846},
    "model_135092_c3610d5c_0007": {"func": model_135092_c3610d5c_0007, "volume": 0.0120576403, "area": 0.6331293739},
    "model_135092_c3610d5c_0008": {"func": model_135092_c3610d5c_0008, "volume": 0.2046763152, "area": 3.2383341098},
    "model_135205_958cc1f8_0000": {"func": model_135205_958cc1f8_0000, "volume": 20.1544802817, "area": 55.3848268362},
    "model_135278_8675dea7_0000": {"func": model_135278_8675dea7_0000, "volume": 112.2477796188, "area": 199.0796327004},
    "model_135443_be53bf45_0000": {"func": model_135443_be53bf45_0000, "volume": 0.7992, "area": 7.074},
    "model_135460_6471e973_0001": {"func": model_135460_6471e973_0001, "volume": 422.1481619308, "area": 316.1155785549},
    "model_135892_ab8f21bf_0003": {"func": model_135892_ab8f21bf_0003, "volume": 1.7382706888, "area": 8.915797441},
    "model_136129_9b1934a3_0000": {"func": model_136129_9b1934a3_0000, "volume": 13.1926990817, "area": 38.3415926536},
    "model_136206_f765760a_0000": {"func": model_136206_f765760a_0000, "volume": 1.4241114235, "area": 7.6591603795},
    "model_136206_f765760a_0001": {"func": model_136206_f765760a_0001, "volume": 5.6165186405, "area": 24.2743338823},
    "model_136239_e80b9e8e_0000": {"func": model_136239_e80b9e8e_0000, "volume": 0.1967552175, "area": 1.9774392462},
    "model_136322_81d84c1b_0000": {"func": model_136322_81d84c1b_0000, "volume": 191.1598449493, "area": 338.6714586764},
    "model_136594_1f36c7d3_0000": {"func": model_136594_1f36c7d3_0000, "volume": 150.3724102546, "area": 317.1114923768},
    "model_136617_c41e239f_0000": {"func": model_136617_c41e239f_0000, "volume": 7.2351272636, "area": 27.319569573},
    "model_136627_98da0c2f_0002": {"func": model_136627_98da0c2f_0002, "volume": 175.6934204479, "area": 288.5192385981},
    "model_136640_16741d62_0001": {"func": model_136640_16741d62_0001, "volume": 246160, "area": 57472},
    "model_136640_16741d62_0002": {"func": model_136640_16741d62_0002, "volume": 164958.6415069297, "area": 38573.1081015489},
    "model_136688_ae3c4ae7_0000": {"func": model_136688_ae3c4ae7_0000, "volume": 6.0249529087, "area": 22.1970750427},
    "model_136716_076bbbb3_0000": {"func": model_136716_076bbbb3_0000, "volume": 0.3990000022, "area": 5.6300000344},
    "model_136716_076bbbb3_0004": {"func": model_136716_076bbbb3_0004, "volume": 0.5874336294, "area": 12.98},
    "model_136716_076bbbb3_0008": {"func": model_136716_076bbbb3_0008, "volume": 0.213, "area": 3.43},
    "model_136745_de48e6a0_0000": {"func": model_136745_de48e6a0_0000, "volume": 149516.425531206, "area": 124118.3064381016},
    "model_136795_e6ced33d_0001": {"func": model_136795_e6ced33d_0001, "volume": 7.3607678973, "area": 36.5826958911},
    "model_136804_e0013c2b_0000": {"func": model_136804_e0013c2b_0000, "volume": 0.4162610266, "area": 3.4714598822},
    "model_136864_161ce067_0004": {"func": model_136864_161ce067_0004, "volume": 0.500805671, "area": 4.8420388759},
    "model_136885_b23ae817_0000": {"func": model_136885_b23ae817_0000, "volume": 13.509699099, "area": 49.8283185248},
    "model_136900_4fe212e6_0016": {"func": model_136900_4fe212e6_0016, "volume": 8190.994258443, "area": 9137.5710096001},
    "model_136900_4fe212e6_0017": {"func": model_136900_4fe212e6_0017, "volume": 1522547.164427862, "area": 291223.3919720919},
    "model_136925_70fb0381_0000": {"func": model_136925_70fb0381_0000, "volume": 1962.2387714322, "area": 1825.579491001},
    "model_136994_a3a2f50f_0001": {"func": model_136994_a3a2f50f_0001, "volume": 7867.2, "area": 2524.7},
    "model_137098_0a45d1c8_0001": {"func": model_137098_0a45d1c8_0001, "volume": 1.1672863434, "area": 10.6608897548},
    "model_137098_0a45d1c8_0003": {"func": model_137098_0a45d1c8_0003, "volume": 70.141775478, "area": 118.7220340191},
    "model_137098_0a45d1c8_0015": {"func": model_137098_0a45d1c8_0015, "volume": 51.8295608253, "area": 1043.0828967064},
    "model_137099_58f819ec_0003": {"func": model_137099_58f819ec_0003, "volume": 9.8200554269, "area": 53.1028758088},
    "model_137099_58f819ec_0008": {"func": model_137099_58f819ec_0008, "volume": 1.8849555922, "area": 10.0530964915},
    "model_137118_4ff32ab1_0006": {"func": model_137118_4ff32ab1_0006, "volume": 0.4299797806, "area": 5.5426291854},
    "model_137118_4ff32ab1_0008": {"func": model_137118_4ff32ab1_0008, "volume": 0.0849481953, "area": 1.5301594964},
    "model_137141_748596d0_0008": {"func": model_137141_748596d0_0008, "volume": 0.0001534782, "area": 0.0199239495},
    "model_137164_339dce36_0000": {"func": model_137164_339dce36_0000, "volume": 5.1209578595, "area": 27.4193011839},
    "model_137373_22e709d8_0000": {"func": model_137373_22e709d8_0000, "volume": 4.8568034219, "area": 19.4550353756},
    "model_137483_cdb8989d_0000": {"func": model_137483_cdb8989d_0000, "volume": 359.04, "area": 417.28},
    "model_137646_14bca880_0002": {"func": model_137646_14bca880_0002, "volume": 0.5495374508, "area": 5.6719266015},
    "model_137837_9c9f163d_0011": {"func": model_137837_9c9f163d_0011, "volume": 1863.6902664471, "area": 1790.0796447372},
    "model_137837_9c9f163d_0013": {"func": model_137837_9c9f163d_0013, "volume": 525.6, "area": 816.6},
    "model_137905_bef6aac2_0000": {"func": model_137905_bef6aac2_0000, "volume": 271.9575889126, "area": 361.2779606989},
    "model_137997_9a5922be_0000": {"func": model_137997_9a5922be_0000, "volume": 17.2672149909, "area": 96.2226231569},
    "model_138071_f8d5a493_0000": {"func": model_138071_f8d5a493_0000, "volume": 1.1501359079, "area": 11.826777687},
    "model_138117_188eed23_0000": {"func": model_138117_188eed23_0000, "volume": 18.4165304173, "area": 52.0458497524},
    "model_138121_ccc9851b_0000": {"func": model_138121_ccc9851b_0000, "volume": 8.0236276373, "area": 34.117696218},
    "model_138131_8cca28d3_0000": {"func": model_138131_8cca28d3_0000, "volume": 21.1877126619, "area": 104.3376815914},
    "model_138138_0938b9fb_0000": {"func": model_138138_0938b9fb_0000, "volume": 198.7080209643, "area": 248.681781056},
    "model_138148_d6277b0d_0000": {"func": model_138148_d6277b0d_0000, "volume": 9.269140582, "area": 27.5613950911},
    "model_138159_43a27dbd_0000": {"func": model_138159_43a27dbd_0000, "volume": 0.0000010503, "area": 0.0016127004},
    "model_138186_5b1b2266_0000": {"func": model_138186_5b1b2266_0000, "volume": 7.6326571557, "area": 37.4557567296},
    "model_138242_d520d083_0000": {"func": model_138242_d520d083_0000, "volume": 1725480, "area": 367970},
    "model_138256_ae3bde67_0000": {"func": model_138256_ae3bde67_0000, "volume": 185.618143922, "area": 260.3370768075},
    "model_138263_895e2c6e_0000": {"func": model_138263_895e2c6e_0000, "volume": 282.8497190935, "area": 897.8853417556},
    "model_138313_ceb6bcca_0000": {"func": model_138313_ceb6bcca_0000, "volume": 4.213625, "area": 27.4095},
    "model_138423_553700e1_0005": {"func": model_138423_553700e1_0005, "volume": 4084.0704496667, "area": 1470.26536188},
    "model_138563_a93c9c1c_0000": {"func": model_138563_a93c9c1c_0000, "volume": 309786.2364344309, "area": 93646.2637228272},
    "model_138620_e21e10ee_0000": {"func": model_138620_e21e10ee_0000, "volume": 0.974673594, "area": 5.8967272148},
    "model_138752_d35ee151_0004": {"func": model_138752_d35ee151_0004, "volume": 88.68, "area": 200.6},
    "model_138764_891914eb_0001": {"func": model_138764_891914eb_0001, "volume": 942.4777960769, "area": 1401.9637848129},
    "model_138842_b33b37d5_0000": {"func": model_138842_b33b37d5_0000, "volume": 178.8823061498, "area": 350.1646981433},
    "model_138888_857538fd_0000": {"func": model_138888_857538fd_0000, "volume": 1.0489276889, "area": 9.5855001679},
    "model_138915_28fbd2f7_0000": {"func": model_138915_28fbd2f7_0000, "volume": 4302.564, "area": 5157.448},
    "model_138954_6b7ae636_0000": {"func": model_138954_6b7ae636_0000, "volume": 4.8451386884, "area": 19.3689557368},
    "model_139222_2c10ca9a_0019": {"func": model_139222_2c10ca9a_0019, "volume": 245.8296251434, "area": 356.5707661824},
    "model_139253_33608dfd_0000": {"func": model_139253_33608dfd_0000, "volume": 13.367920407, "area": 271.4495630678},
    "model_139371_557edc08_0000": {"func": model_139371_557edc08_0000, "volume": 1.7467255394, "area": 10.1787602276},
    "model_139383_d8f77b30_0000": {"func": model_139383_d8f77b30_0000, "volume": 72.8268883334, "area": 115.6093536548},
    "model_139518_5ee97bb7_0000": {"func": model_139518_5ee97bb7_0000, "volume": 5.279999908, "area": 33.5999994175},
    "model_139677_8e558c30_0000": {"func": model_139677_8e558c30_0000, "volume": 534.2843813694, "area": 737.6638175427},
    "model_139744_58088e94_0000": {"func": model_139744_58088e94_0000, "volume": 453.2593893629, "area": 719.9204468267},
    "model_139801_97e2ca6a_0004": {"func": model_139801_97e2ca6a_0004, "volume": 0.3116000032, "area": 8.3748802738},
    "model_139939_3daabd82_0000": {"func": model_139939_3daabd82_0000, "volume": 18.878921693, "area": 88.4832937013},
    "model_139940_dba1c52b_0000": {"func": model_139940_dba1c52b_0000, "volume": 12.8974172499, "area": 60.3610286114},
    "model_140059_6f242172_0000": {"func": model_140059_6f242172_0000, "volume": 12.7904278659, "area": 83.0642270303},
    "model_140194_b0abb2bf_0003": {"func": model_140194_b0abb2bf_0003, "volume": 7116.082542, "area": 5719.3434},
    "model_140194_b0abb2bf_0011": {"func": model_140194_b0abb2bf_0011, "volume": 12803.4179415, "area": 13253.1993},
    "model_140760_c36e4bec_0026": {"func": model_140760_c36e4bec_0026, "volume": 97.3893722613, "area": 158.6504290063},
    "model_140760_c36e4bec_0027": {"func": model_140760_c36e4bec_0027, "volume": 25.9181393921, "area": 61.261056745},
    "model_140760_c36e4bec_0028": {"func": model_140760_c36e4bec_0028, "volume": 32.2013246993, "area": 73.8274273594},
    "model_140862_9005288e_0000": {"func": model_140862_9005288e_0000, "volume": 1272.525, "area": 1698.25},
    "model_141177_0ce4dd24_0000": {"func": model_141177_0ce4dd24_0000, "volume": 5428.6721054032, "area": 1912.3928496819},
    "model_141186_d75414a5_0000": {"func": model_141186_d75414a5_0000, "volume": 0.6743451332, "area": 34.6326548849},
    "model_141665_0564e852_0002": {"func": model_141665_0564e852_0002, "volume": 33408, "area": 23592},
    "model_141694_b5ac3112_0000": {"func": model_141694_b5ac3112_0000, "volume": 2.7081115179, "area": 24.9095876984},
    "model_141706_43d0b09e_0000": {"func": model_141706_43d0b09e_0000, "volume": 18.432, "area": 76.8},
    "model_141720_481ac718_0000": {"func": model_141720_481ac718_0000, "volume": 60.9170706061, "area": 190.4049649191},
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
