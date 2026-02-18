"""Batch 005 - passing/03_4to5ops
129 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical rod or shaft with rounded ends and a slightly tapered or chamfered profile, featuring a smooth, elongated rectangular appearance when viewed from above.
def model_21557_53eafe15_0024():
    """Model: Part 16 - Handle v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7316855998, perimeter: 3.0322652292
            Circle(0.4826)
        # TwoSides extrude (symmetric), distance=4.445
        extrude(amount=4.445, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.445, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0191282073, perimeter: 6.0246322318
            with BuildLine():
                CenterArc((0, 0), 0.4826, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.016
        extrude(amount=-1.016, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or rod with a hexagonal or angular connector head on one end, featuring cooling fins or heat dissipation vanes on both the cylindrical body and the connector end.
def model_21557_53eafe15_0027():
    """Model: Short (1.5") Bolt v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4007106478, perimeter: 6.0091766994
            with BuildLine():
                Line((0.5080000162, -0.2932939461), (0.5080000162, 0.2932939461))
                Line((0.5080000162, 0.2932939461), (0, 0.5865878922))
                Line((0, 0.5865878922), (-0.5080000162, 0.2932939461))
                Line((-0.5080000162, 0.2932939461), (-0.5080000162, -0.2932939461))
                Line((-0.5080000162, -0.2932939461), (0, -0.5865878922))
                Line((0, -0.5865878922), (0.5080000162, -0.2932939461))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.39624, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625, mode=Mode.ADD)
    return part.part


# Description: This is a horizontal cylindrical rod or shaft with rounded ends and two small holes or attachment points near each end, featuring a sleek, streamlined design with a dark metallic finish.
def model_21557_53eafe15_0031():
    """Model: Part 6 - Link v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 23.7012552497, perimeter: 37.959962576
            with BuildLine():
                CenterArc((-6.3500002027, 0), 0.889, 90, 180)
                Line((-6.3500002027, -0.889), (6.3500002027, -0.889))
                CenterArc((6.3500002027, 0), 0.889, -90, 180)
                Line((-6.3500002027, 0.889), (6.3500002027, 0.889))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.24638, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3500002027, 0), 0.4318, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.3500002027, 0), 0.4318, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.508), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.8960674927, perimeter: 23.1438951456
            with BuildLine():
                CenterArc((-4.5212, 0), 0.5588, 89.9999561048, 180.0000877977)
                Line((-4.5211995718, -0.5588), (4.521199525, -0.5588))
                CenterArc((4.5212, 0), 0.5588, -90.0000487032, 180.0000974125)
                Line((-4.5211995719, 0.5588), (4.5211995249, 0.5588))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.24638, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1524
        extrude(amount=-0.1524, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft or rod with a cylindrical body, rounded left end, and a hexagonal flange on the right end, featuring small slots or grooves along its length.
def model_21557_53eafe15_0036():
    """Model: Long (2.5") Bolt v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=-6.35
        extrude(amount=-6.35)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4007106478, perimeter: 6.0091766994
            with BuildLine():
                Line((0.5080000162, -0.2932939461), (0.5080000162, 0.2932939461))
                Line((0.5080000162, 0.2932939461), (0, 0.5865878922))
                Line((0, 0.5865878922), (-0.5080000162, 0.2932939461))
                Line((-0.5080000162, 0.2932939461), (-0.5080000162, -0.2932939461))
                Line((-0.5080000162, -0.2932939461), (0, -0.5865878922))
                Line((0, -0.5865878922), (0.5080000162, -0.2932939461))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.39624, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625, mode=Mode.ADD)
    return part.part


# Description: This is a linear actuator or slide mechanism featuring a long cylindrical gray body with a blue angled connector/bracket on the right end, equipped with ventilation slots along its length for heat dissipation.
def model_21557_53eafe15_0052():
    """Model: Medium (1.75") Bolt v1 v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=-4.445
        extrude(amount=-4.445)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4007106478, perimeter: 6.0091766994
            with BuildLine():
                Line((0.5080000162, -0.2932939461), (0.5080000162, 0.2932939461))
                Line((0.5080000162, 0.2932939461), (0, 0.5865878922))
                Line((0, 0.5865878922), (-0.5080000162, 0.2932939461))
                Line((-0.5080000162, 0.2932939461), (-0.5080000162, -0.2932939461))
                Line((-0.5080000162, -0.2932939461), (0, -0.5865878922))
                Line((0, -0.5865878922), (0.5080000162, -0.2932939461))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.39624, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or octagonal prism-based geometric solid with a rectangular top face and tapered/slanted side faces, featuring clean edges and a pyramidal upper section.
def model_21636_f65686bc_0006():
    """Model: bolt v1"""
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1436722243, perimeter: 6.6000000089
            with BuildLine():
                Line((0.9526279455, 0.5500000007), (0, 1.1000000015))
                Line((0, 1.1000000015), (-0.9526279454, 0.5500000008))
                Line((-0.9526279454, 0.5500000008), (-0.9526279455, -0.5500000007))
                Line((-0.9526279455, -0.5500000007), (0, -1.1000000015))
                Line((0, -1.1000000015), (0.9526279454, -0.5500000008))
                Line((0.9526279454, -0.5500000008), (0.9526279455, 0.5500000007))
            make_face()
        # OneSide extrude, distance=0.765
        extrude(amount=0.765)
    return part.part


# Description: This is a boat hull or watercraft component with an elongated, tapered trapezoidal shape featuring internal ribbing/reinforcement struts and what appear to be mounting points or openings at each end for structural support and assembly.
def model_21638_0a984848_0001():
    """Model: Assembly Full v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 102.5496682223, perimeter: 44.4557519189
            with BuildLine():
                Line((18, 0), (18, 11.5))
                Line((18, 11.5), (9, 11.5))
                Line((9, 0), (9, 11.5))
                Line((9, 0), (18, 0))
            make_face()
            with BuildLine():
                CenterArc((12, 4.4539781109), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 102.5496682223, perimeter: 44.4557519189
            with BuildLine():
                Line((9, 0), (9, 11.5))
                Line((9, 11.5), (0, 11.5))
                Line((0, 11.5), (0, 0))
                Line((0, 0), (9, 0))
            make_face()
            with BuildLine():
                CenterArc((6, 4.4539781109), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 102.5496682223, perimeter: 44.4557519189
            with BuildLine():
                Line((9, 11.5), (0, 11.5))
                Line((9, 11.5), (9, 18.5460218891))
                Line((9, 18.5460218891), (9, 23))
                Line((0, 23), (9, 23))
                Line((0, 23), (0, 11.5))
            make_face()
            with BuildLine():
                CenterArc((6, 18.5460218891), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 102.5496682223, perimeter: 46.9057519189
            with BuildLine():
                Line((9, 18.5460218891), (9, 23))
                Line((9, 18.5460218891), (11.45, 18.5460218891))
                CenterArc((12, 18.5460218891), 0.55, 0, 360)
                Line((9, 11.5), (9, 18.5460218891))
                Line((18, 11.5), (9, 11.5))
                Line((18, 11.5), (18, 23))
                Line((18, 23), (9, 23))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5943582717, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((6, -18.5460218891), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6, -18.5460218891), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5943582717, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((12, -18.5460218891), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12, -18.5460218891), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5943582717, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((12, -4.4539781109), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12, -4.4539781109), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5943582717, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((6, -4.4539781109), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6, -4.4539781109), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or dowel pin with a smooth, uniform diameter and rounded ends, commonly used as a structural support or alignment component in mechanical assemblies.
def model_21638_0a984848_0007():
    """Model: Crankshaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=10.6
        extrude(amount=10.6)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                CenterArc((-0.5, 0), 0.15, 90, 270)
                Line((-0.35, 0), (-0.5, 0))
                Line((-0.5, 0), (-0.5, 0.15))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((-0.5, 0), (-0.5, 0.15))
                Line((-0.35, 0), (-0.5, 0))
                CenterArc((-0.5, 0), 0.15, 0, 90)
            make_face()
        # TwoSides extrude, along=0.85, against=-0.8
        extrude(amount=0.85, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical filter or silencer component with a rounded end cap, a perforated mesh body for filtration or sound dampening, and a tapered stem or connector at the base.
def model_21638_0a984848_0010():
    """Model: Crankshaft valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, -0.3)):
                Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is an elliptical or oval-shaped structural frame with a mesh or lattice pattern on the upper surface and a solid rim/flange around the perimeter, featuring internal cross-bracing elements visible through the transparent mesh.
def model_21644_aa203dc5_0007():
    """Model: PT-201-P-027 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.3626933984, perimeter: 32.6291969146
            with BuildLine():
                CenterArc((1.767766953, -1.767766953), 1.2, -135.0426952171, 180)
                Line((2.6169271543, -0.9198713506), (-0.9159702082, 2.6182951724))
                CenterArc((-1.7651304095, 1.77039957), 1.2, 44.9573047829, 180)
                Line((-2.6142906107, 0.9225039677), (0.9186067517, -2.6156625554))
            make_face()
            with BuildLine():
                Line((-2.3383135453, 1.1980700384), (1.1945838171, -2.3400964846))
                CenterArc((-1.7651304095, 1.77039957), 0.81, 44.9573047829, 180)
                Line((2.3409500888, -1.1954374214), (-1.1919472736, 2.3427291017))
                CenterArc((1.767766953, -1.767766953), 0.81, -135.0426952171, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.23
        extrude(amount=-0.23, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a curved slot or opening cut along its top edge and vertical ribbing or fluting running along its outer surface.
def model_21644_aa203dc5_0009():
    """Model: PT-201-P-012 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8773225947, perimeter: 21.6769893098
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a elongated metal bracket or support beam with an angular, faceted design featuring multiple planar surfaces, a central raised ridge, and asymmetrical geometry optimized for structural rigidity.
def model_21644_aa203dc5_0016():
    """Model: PT-201-P-036 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 28
            with BuildLine():
                Line((-6, 1), (6, 1))
                Line((-6, -1), (-6, 1))
                Line((6, -1), (-6, -1))
                Line((6, 1), (6, -1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9632526082, perimeter: 7.9265054683
            with BuildLine():
                Line((1.5, 0), (1.5007098128, -1))
                Line((1.5, 0), (-1.4628977018, 0))
                Line((-1.4628977018, -1), (-1.4628977018, 0))
                Line((1.5007098128, -1), (-1.4628977018, -1))
            make_face()
            # Profile area: 2.963962421, perimeter: 9.9265054683
            with BuildLine():
                Line((-1.4628977018, 0), (-1.4628977018, 1))
                Line((1.5, 0), (-1.4628977018, 0))
                Line((1.5, 0), (1.5007098128, -1))
                Line((1.5007098128, 1), (1.5007098128, -1))
                Line((-1.4628977018, 1), (1.5007098128, 1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a timing belt featuring an elongated oval loop with a textured driving surface and a rectangular pulley or tensioner component positioned along its length.
def model_21646_a2dd0d00_0002():
    """Model: Saturn Planet v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.3890337877, perimeter: 115.7048574317
            with BuildLine():
                CenterArc((0, 0), 9.4615, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 8.9535, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with BuildLine():
                CenterArc((0, 0), 1.27, 4.7698762171, 170.4602475658)
                CenterArc((0, 0), 1.27, 175.2301237829, 189.5397524342)
            make_face()
            # Profile area: 13.5924481234, perimeter: 22.5621602794
            with BuildLine():
                CenterArc((0, 0), 1.27, 4.7698762171, 170.4602475658)
                Line((1.2656016292, 0.105605474), (0.5286184388, 8.937881449))
                CenterArc((0, 0), 8.9535, 86.6152645196, 6.7694709607)
                Line((-1.2656016292, 0.105605474), (-0.5286184388, 8.937881449))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a timing or V-belt characterized by its continuous looped design with a textured outer surface, featuring a rigid rectangular pulley or idler attachment integrated along its length.
def model_21646_a2dd0d00_0005():
    """Model: Jupiter Planet v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.1333870744, perimeter: 110.3584950538
            with BuildLine():
                CenterArc((0, 0), 9.0551, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 8.509, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.1327116603, perimeter: 21.1934668158
            with BuildLine():
                CenterArc((0, 0), 1.27, 6.3667007845, 167.266598431)
                Line((1.2621673194, 0.1408320201), (0.3291738806, 8.502630508))
                CenterArc((0, 0), 8.509, 87.7829378883, 4.4341242233)
                Line((-1.2621673194, 0.1408320201), (-0.3291738806, 8.502630508))
            make_face()
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with BuildLine():
                CenterArc((0, 0), 1.27, 6.3667007845, 167.266598431)
                CenterArc((0, 0), 1.27, 173.6332992155, 192.733401569)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a reinforced belt or strap assembly with an oval/elliptical loop shape, featuring dual rectangular slot cutouts and mesh or perforated reinforcement panels on the outer surfaces for flexibility and weight reduction.
def model_21646_a2dd0d00_0025():
    """Model: Venus Planet v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.6676869774, perimeter: 39.8982267006
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.8575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6466485327, perimeter: 7.6608207812
            with BuildLine():
                CenterArc((0, 0), 0.635, 9.7360037159, 160.5279925683)
                Line((0.6258543481, 0.1073840537), (0.1547365861, 2.8533073509))
                CenterArc((0, 0), 2.8575, 86.8958558383, 6.2082883234)
                Line((-0.6258543481, 0.1073840537), (-0.1547365861, 2.8533073509))
            make_face()
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with BuildLine():
                CenterArc((0, 0), 0.635, 9.7360037159, 160.5279925683)
                CenterArc((0, 0), 0.635, 170.2639962841, 199.4720074317)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a timing belt with a rectangular tooth profile and a flat rectangular drive element or sensor attachment mounted on its inner surface, designed for power transmission in mechanical systems.
def model_21646_a2dd0d00_0027():
    """Model: Mars Planet v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.0522012141, perimeter: 75.0086661971
            with BuildLine():
                CenterArc((0, 0), 6.223, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.715, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7380276083, perimeter: 13.889881636
            with BuildLine():
                CenterArc((0, 0), 0.635, 3.3244762887, 173.3510474226)
                Line((0.6339313805, 0.0368239708), (0.3045733941, 5.7068783102))
                CenterArc((0, 0), 5.715, 86.9450496468, 6.1099007063)
                Line((-0.6339313805, 0.0368239708), (-0.3045733941, 5.7068783102))
            make_face()
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with BuildLine():
                CenterArc((0, 0), 0.635, 3.3244762887, 173.3510474226)
                CenterArc((0, 0), 0.635, 176.6755237113, 186.6489525774)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular enclosure or housing component with a curved, box-like shape featuring a central open slot or channel running lengthwise, flanged edges on the sides, and rounded corners for structural reinforcement.
def model_21646_a2dd0d00_0041():
    """Model: Crank Lever v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7994464943, perimeter: 11.4992617889
            with BuildLine():
                CenterArc((5.0800001621, 0), 1.11125, -180, 91.4989048149)
                Line((1.2446, 0), (3.9687501621, 0))
                CenterArc((0, 0), 1.2446, -88.4959785868, 88.4959785868)
                Line((0.0326671545, -1.2441712169), (5.1090680622, -1.1108697629))
            make_face()
            # Profile area: 3.7994464941, perimeter: 11.4994382703
            with BuildLine():
                CenterArc((0, 0), 1.2446, 0, 88.4957995123)
                Line((1.2446, 0), (3.9687501621, 0))
                CenterArc((5.0800001621, 0), 1.11125, 88.4963449518, 91.5036550482)
                Line((0.032671043, 1.2441711148), (5.1091601611, 1.1108673444))
            make_face()
            # Profile area: 4.8664186293, perimeter: 7.8200524333
            with BuildLine():
                CenterArc((0, 0), 1.2446, 88.4957995123, 183.0082219009)
                CenterArc((0, 0), 1.2446, -88.4959785868, 88.4959785868)
                CenterArc((0, 0), 1.2446, 0, 88.4957995123)
            make_face()
            # Profile area: 3.8794791368, perimeter: 6.9821896726
            with BuildLine():
                CenterArc((5.0800001621, 0), 1.11125, 88.4963449518, 91.5036550482)
                CenterArc((5.0800001621, 0), 1.11125, -180, 91.4989048149)
                CenterArc((5.0800001621, 0), 1.11125, -88.501095185, 176.9974401368)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((-5.0800001621, 0)):
                Circle(0.47625)
        # OneSide extrude, distance=-2.286
        extrude(amount=-2.286, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flexible hose or cable conduit with an elongated oval/elliptical loop shape, featuring a ribbed or textured exterior surface and a central rectangular core or insert running through its length.
def model_21646_a2dd0d00_0060():
    """Model: Mercury Drive v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.6658145366, perimeter: 90.7920276887
            with BuildLine():
                CenterArc((0, 0), 7.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 1.15, 6.9384622146, 166.1230755708)
                CenterArc((0, 0), 1.15, 173.0615377854, 193.8769244292)
            make_face()
            # Profile area: 7.9806782735, perimeter: 17.2241695737
            with BuildLine():
                CenterArc((0, 0), 1.15, 6.9384622146, 166.1230755708)
                Line((1.141577942, 0.1389237284), (0.3442141954, 6.6911521121))
                CenterArc((0, 0), 6.7, 87.0551183971, 5.8897632059)
                Line((-1.141577942, 0.1389237284), (-0.3442141954, 6.6911521121))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a timing belt or drive belt featuring an elongated oval loop shape with evenly spaced teeth or ribs running along its inner surfaces for grip and power transmission.
def model_21646_a2dd0d00_0064():
    """Model: Venus Drive v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.9171764609, perimeter: 70.5400648066
            with BuildLine():
                CenterArc((0, 0), 5.8674, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.3594, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8369421366, perimeter: 14.4666625012
            with BuildLine():
                CenterArc((0, 0), 1.27, 10.8079628522, 158.3840742955)
                Line((1.2474717232, 0.2381476429), (0.2711193614, 5.3525379636))
                CenterArc((0, 0), 5.3594, 87.100304451, 5.7993910979)
                Line((-1.2474717232, 0.2381476429), (-0.2711193614, 5.3525379636))
            make_face()
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with BuildLine():
                CenterArc((0, 0), 1.27, 10.8079628522, 158.3840742955)
                CenterArc((0, 0), 1.27, 169.1920371478, 201.6159257045)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a timing belt featuring a flat, elongated oval loop with regularly spaced teeth on the inner surfaces and a rectangular slot or opening cut through the belt structure for engagement or mounting purposes.
def model_21646_a2dd0d00_0065():
    """Model: Earth Drive v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1878094147, perimeter: 55.8575173808
            with BuildLine():
                CenterArc((0, 0), 4.699, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.191, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with BuildLine():
                CenterArc((0, 0), 1.27, 12.7586174843, 154.4827650313)
                CenterArc((0, 0), 1.27, 167.2413825157, 205.5172349687)
            make_face()
            # Profile area: 4.3942907259, perimeter: 12.1261817064
            with BuildLine():
                CenterArc((0, 0), 1.27, 12.7586174843, 154.4827650313)
                Line((1.2386425771, 0.2804720418), (0.3566101608, 4.1758005452))
                CenterArc((0, 0), 4.191, 85.1188276023, 9.7623447954)
                Line((-1.2386425771, 0.2804720418), (-0.3566101608, 4.1758005452))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a timing belt (or synchronous belt) featuring an elongated oval shape with internal teeth along the inner surfaces and a rectangular drive block or pulley attachment integrated into the center opening.
def model_21646_a2dd0d00_0072():
    """Model: Earth Planet v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.8472764088, perimeter: 55.4585351138
            with BuildLine():
                CenterArc((0, 0), 4.699, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.1275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7510566791, perimeter: 10.3748809383
            with BuildLine():
                CenterArc((0, 0), 0.635, 6.327036717, 167.345926566)
                Line((0.6311322553, 0.0699791138), (0.1816868218, 4.1234992602))
                CenterArc((0, 0), 4.1275, 87.4771041103, 5.0457917794)
                Line((-0.6311322553, 0.0699791138), (-0.1816868218, 4.1234992602))
            make_face()
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with BuildLine():
                CenterArc((0, 0), 0.635, 6.327036717, 167.345926566)
                CenterArc((0, 0), 0.635, 173.672963283, 192.654073434)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal bolt consisting of a long cylindrical shaft with a hexagonal head at the base, designed for fastening applications.
def model_21680_360ba5c7_0002():
    """Model: Machine-Screw-13 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=4.60502
        extrude(amount=4.60502)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.0552832681, perimeter: 7.9417021852
            with BuildLine():
                Line((0.714375, -0.4124445986), (0.714375, 0.4124445986))
                Line((0.714375, 0.4124445986), (0, 0.8248891971))
                Line((0, 0.8248891971), (-0.714375, 0.4124445986))
                Line((-0.714375, 0.4124445986), (-0.714375, -0.4124445986))
                Line((-0.714375, -0.4124445986), (0, -0.8248891971))
                Line((0, -0.8248891971), (0.714375, -0.4124445986))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical standoff or spacer with an angled base mount, featuring a hollow cylindrical body with a mesh or perforated top section and a multi-faceted pyramidal base for secure mounting.
def model_21680_360ba5c7_0017():
    """Model: Machine-Screw-15 v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.0552832681, perimeter: 7.9417021852
            with BuildLine():
                Line((0.714375, -0.4124445986), (0.714375, 0.4124445986))
                Line((0.714375, 0.4124445986), (0, 0.8248891971))
                Line((0, 0.8248891971), (-0.714375, 0.4124445986))
                Line((-0.714375, 0.4124445986), (-0.714375, -0.4124445986))
                Line((-0.714375, -0.4124445986), (0, -0.8248891971))
                Line((0, -0.8248891971), (0.714375, -0.4124445986))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with two coaxial bores of different diameters, featuring a stepped design that allows two shafts or components of different sizes to be joined end-to-end.
def model_21697_06656699_0001():
    """Model: 11. End Cap v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0956282467, perimeter: 3.7105350832
            Circle(0.59055)
        # OneSide extrude, distance=0.9906
        extrude(amount=0.9906)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9906, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1451589028, perimeter: 9.0169992343
            with BuildLine():
                CenterArc((0, 0), 0.84455, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.59055, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0956282467, perimeter: 3.7105350832
            Circle(0.59055)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


# Description: This is a connector or coupling component featuring a cylindrical shaft with an enlarged hexagonal or polygonal flange head on top, designed to join or mount components together.
def model_21702_3390d14a_0007():
    """Model: Plastic Stop v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7203819497, perimeter: 3.1832037385
            with BuildLine():
                CenterArc((0.55, 0), 0.25, -74.1733798668, 148.3475978327)
                Line((0.1090908561, 0.3848365694), (0.6181782999, 0.2405238438))
                CenterArc((0, 0), 0.4, 74.1733877648, 211.6532336983)
                Line((0.6181818182, -0.2405228465), (0.109090918, -0.3848365518))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical component with a hemispherical or domed top surface, featuring a fine mesh or lattice pattern across the upper portion, suggesting it may be a filter, strainer, or perforated structural element.
def model_21703_42d28e69_0011():
    """Model: Adjusting Rod Handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=-1.5875
        extrude(amount=-1.5875)
    return part.part


# Description: This is a hexagonal prism or box-shaped component with a truncated/beveled top surface featuring multiple triangulated facets, creating an irregular polyhedron with both planar and angled surfaces.
def model_21707_c15f2c00_0018():
    """Model: 6 Cylinder - Radial Engine (pneumatic) Crankcase v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 97.3066190308, perimeter: 36.719478
            with BuildLine():
                Line((-3.0599565, 5.3), (3.0599565, 5.3))
                Line((-6.1199132199, 0), (-3.0599565, 5.3))
                Line((-3.0599565, -5.3), (-6.1199132199, 0))
                Line((3.0599565, -5.3), (-3.0599565, -5.3))
                Line((3.0599565, -5.3), (6.1199132199, 0))
                Line((3.0599565, 5.3), (6.1199132199, 0))
            make_face()
        # OneSide extrude, distance=5.7
        extrude(amount=5.7)
    return part.part


# Description: This is a dumbbell or barbell weight with cylindrical end weights connected by a central bar shaft, featuring rounded knobs on each end for grip.
def model_21732_adaf1650_0007():
    """Model: Connecting Rod v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((6, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.32, perimeter: 2.4
            with BuildLine():
                Line((0.4, 0.3000000104), (-0.4, 0.3000000104))
                Line((0.4, 0.7000000104), (0.4, 0.3000000104))
                Line((-0.4, 0.7000000104), (0.4, 0.7000000104))
                Line((-0.4, 0.3000000104), (-0.4, 0.7000000104))
            make_face()
        # OneSide extrude, distance=6.1
        extrude(amount=6.1, mode=Mode.ADD)
    return part.part


# Description: This is a vertical rectangular panel or enclosure component with three diamond-shaped or rhombus-patterned openings arranged in a column, featuring a flat face with recessed frame details and reinforced edges.
def model_21734_7cf58bd0_0011():
    """Model: STEAM CHEST COVER v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24.13, perimeter: 20.3
            with BuildLine():
                Line((-3.8, 6.35), (0, 6.35))
                Line((-3.8, 0), (-3.8, 6.35))
                Line((0, 0), (-3.8, 0))
                Line((0, 6.35), (0, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 26 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3, 5.725)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.5, 5.725)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3, 4.025)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.5000014431, 4.025)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.5000018437, 2.325)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.5000034508, 0.625)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3, 2.325)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3, 0.625)):
                Circle(0.225)
        # OneSide extrude, distance=-3.7
        extrude(amount=-3.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or washer with a circular cross-section, featuring a uniform thickness and a hollow center, with textured or patterned surfaces visible on the inner and outer edges.
def model_21736_fc59650e_0011():
    """Model: rpl009 v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stamped or cast metal bracket with an elongated oval opening, featuring a D-shaped or carabiner-like profile with mounting holes along its perimeter for fastening purposes.
def model_21773_01f6bc23_0019():
    """Model: Gasket v6 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 48 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.8710892341, perimeter: 62.6409688
            with BuildLine():
                CenterArc((5.8, 11.8000000001), 3.7, 86.9014133766, 3.0985866234)
                Line((5.8, 15.5000000001), (6.0000004724, 15.5000000001))
                Line((6.0000004724, 17), (6.0000004724, 15.5000000001))
                Line((6.0000004724, 17), (3, 17))
                CenterArc((3, 14), 3, 90, 90)
                Line((0, 14), (0, 2.9999990554))
                CenterArc((3, 3), 3, -179.9999819604, 89.9999639176)
                Line((2.9999990553, 0), (6.0000004724, 0))
                Line((6.0000004724, 1.5000000001), (6.0000004724, 0))
                Line((6.0000004724, 1.5000000001), (5.8, 1.5000000001))
                CenterArc((5.8, 5.2000000001), 3.7, -90, 3.0985866234)
                CenterArc((6.2, 5.2000000001), 3.7, -179.9999764626, 86.9014044492)
                Line((2.5, 6.5158514533), (2.5, 5.1999984801))
                Line((2.5, 6.5158514533), (1.487038185, 6.5158514533))
                Line((1.487038185, 6.5158514533), (1.487038185, 10.4635250826))
                Line((1.487038185, 10.4635250826), (2.5, 10.4635250826))
                Line((2.5, 11.8000015195), (2.5, 10.4635250826))
                CenterArc((6.2, 11.8000000001), 3.7, 93.0985720134, 86.9014044581)
            make_face()
            with BuildLine():
                CenterArc((0.9872615729, 11.4635250826), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9872615729, 5.4635250826), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.4019243821, 1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3844502142, 15.9937918379), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 47.9222554534, perimeter: 62.6150315331
            with BuildLine():
                Line((9.5, 5.2000000001), (9.5, 6.5158514533))
                CenterArc((5.8, 5.2000000001), 3.7, -86.9014133338, 86.9014133338)
                CenterArc((6.2, 5.2000000001), 3.7, -93.0985720134, 3.0985484784)
                Line((6.1999984802, 1.5000000001), (6.0000004724, 1.5000000001))
                Line((6.0000004724, 1.5000000001), (6.0000004724, 0))
                Line((6.0000004724, 0), (9, 0))
                CenterArc((9, 3), 3, -90, 90)
                Line((12, 3), (12, 14.0000009449))
                CenterArc((9, 14), 3, 0.0000180454, 89.9999639092)
                Line((9.0000009449, 17), (6.0000004724, 17))
                Line((6.0000004724, 17), (6.0000004724, 15.5000000001))
                Line((6.0000004724, 15.5000000001), (6.1999984808, 15.5000000001))
                CenterArc((6.2, 11.8000000001), 3.7, 90.0000235258, 3.0985484876)
                CenterArc((5.8, 11.8000000001), 3.7, 0, 86.9014133338)
                Line((9.5, 10.4635250826), (9.5, 11.8000000001))
                Line((9.5, 10.4635250826), (10.5, 10.4635250826))
                Line((10.5, 10.4635250826), (10.5, 6.5158514533))
                Line((10.5, 6.5158514533), (9.5, 6.5158514533))
            make_face()
            with BuildLine():
                CenterArc((8.6155507307, 15.9937918379), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.5980765628, 1), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.9872615729, 5.4635250826), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.9872615729, 11.4635250826), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((6.0000004724, 1)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((6.0000004724, 15.9937918379)):
                Circle(0.3)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a multi-chambered rectangular block with two prominent cubic protrusions on top, featuring internal cavities and triangulated internal structures, resembling a complex industrial enclosure or manifold block with internal passages and structural bracing.
def model_21800_040f0143_0000():
    """Model: Jack Pad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 39.6, perimeter: 30.8
            with BuildLine():
                Line((-3.5, 6.4), (-3.5, 0))
                Line((-3.5, 0), (3.5, 0))
                Line((3.5, 0), (3.5, 6.4))
                Line((3.5, 6.4), (1.3, 6.4))
                Line((1.3, 6.4), (1.3, 4.4))
                Line((1.3, 4.4), (-1.3, 4.4))
                Line((-1.3, 4.4), (-1.3, 6.4))
                Line((-1.3, 6.4), (-3.5, 6.4))
            make_face()
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.5, 1)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((2.5, 1)):
                Circle(0.3175)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: A flat, trapezoidal sheet metal or composite plate with a dark frame/border and multiple rectangular cutouts or windows distributed across its surface, featuring a slightly beveled or angled edge profile.
def model_21803_8a36dcda_0010():
    """Model: Cylinder Head v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.5, perimeter: 19
            with BuildLine():
                Line((5, -4.5), (0, -4.5))
                Line((5, 0), (5, -4.5))
                Line((0, 0), (5, 0))
                Line((0, -4.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-3.8263455967, 3.8763455967)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-3.8263455967, 0.6236544033)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-0.5736544033, 3.8763455967)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-0.5736544033, 0.6236544033)):
                Circle(0.35)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flexible sealing ring or gasket with an oval/elliptical shape featuring a textured exterior surface and a small radial slot or opening, designed to create a watertight or airtight seal in mechanical assemblies.
def model_21803_8a36dcda_0033():
    """Model: Piston Compression Ring v5 (13)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.437278639, perimeter: 19.1637151869
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0300215942, perimeter: 0.7009379817
            with BuildLine():
                CenterArc((0, 0), 1.45, 86.0454278189, 7.9091443622)
                Line((0.1000000015, 1.5968719422), (0.1000000015, 1.446547614))
                CenterArc((0, 0), 1.6, 86.4166782481, 7.1666435039)
                Line((-0.1000000015, 1.446547614), (-0.1000000015, 1.5968719422))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polymer or composite housing/enclosure with an asymmetrical, tapered wedge-like shape featuring multiple internal ribbing for structural reinforcement, openings/slots on the upper surface, and a hollow interior cavity designed for component mounting or assembly.
def model_21822_7d3db422_0006():
    """Model: Main Bearing Foot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.3658838238, perimeter: 18.7874858513
            with BuildLine():
                Line((0, -2.5000000373), (-1.55, -2.5000000373))
                CenterArc((-2.25, -2.5000000373), 0.7, 180, 180)
                Line((-2.95, -2.5000000373), (-4.5, -2.5000000373))
                Line((-4.5, -2.5000000373), (-4.5, -3.0000000373))
                CenterArc((-7.0054939633, -4.6500000373), 3, -33.3670129692, 66.7340259385)
                Line((-4.5, -6.3000000373), (-4.5, -6.8000001013))
                Line((-4.5, -6.8000001013), (0, -6.8000001013))
                Line((0, -6.8000001013), (0, -6.3000000939))
                CenterArc((2.5054939446, -4.6500000656), 3, 146.6329863833, 66.7340272334)
                Line((0, -2.5000000373), (0, -3.0000000373))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.8000001013), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-3.55, 0.8)):
                Circle(0.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling body with a rectangular flange extension at the top featuring triangular mounting points or attachment features, designed for mechanical assembly or pipeline connection applications.
def model_21822_7d3db422_0011():
    """Model: Packnut Piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-8.0000001192, -5.0000000745), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.0000001192, -5.0000000745), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4876592181, perimeter: 7.3415927162
            with BuildLine():
                Line((7.650000114, 5.6062178662), (7.3000001088, 5.0000000745))
                Line((7.3000001088, 5.0000000745), (7.650000114, 4.3937822828))
                Line((7.650000114, 4.3937822828), (8.3500001244, 4.3937822828))
                Line((8.3500001244, 4.3937822828), (8.7000001296, 5.0000000745))
                Line((8.7000001296, 5.0000000745), (8.3500001244, 5.6062178662))
                Line((8.3500001244, 5.6062178662), (7.650000114, 5.6062178662))
            make_face()
            with BuildLine():
                CenterArc((8.0000001192, 5.0000000745), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((8.0000001192, 5.0000000745), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.0000001192, 5.0000000745), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a curved cylindrical sleeve or clip with a vertical slot running along its length, designed to wrap around and secure a cylindrical object.
def model_21822_7d3db422_0015():
    """Model: Crosshead Container Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8502938495, perimeter: 34.2057448061
            with BuildLine():
                Line((-13.35, -17.8), (-13.2535750803, -17.8))
                CenterArc((-15, -15), 3.3, -58.0472535997, 296.0945071995)
                Line((-16.65, -17.8), (-16.7464249197, -17.8))
                CenterArc((-15, -15), 3.25, -59.4897625939, 298.9795251878)
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3026548246, perimeter: 14.5132741229
            with BuildLine():
                Line((-14.6, 2.5), (-14.6, 8.5))
                CenterArc((-15, 8.5), 0.4, 0, 180)
                Line((-15.4, 8.5), (-15.4, 2.5))
                CenterArc((-15, 2.5), 0.4, 180, 180)
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, thin parallelogram-shaped metal strip or blade with a beveled left edge and a slightly curved or textured surface, appearing to be a cutting tool, shim, or structural component.
def model_21822_7d3db422_0016():
    """Model: Ground"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 184, perimeter: 89.2
            with BuildLine():
                Line((67.5, -4.6), (27.5, -4.6))
                Line((67.5, 0), (67.5, -4.6))
                Line((27.5, 0), (67.5, 0))
                Line((27.5, -4.6), (27.5, 0))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 124.2, perimeter: 63.2
            with BuildLine():
                Line((-40.5, 0), (-67.5, 0))
                Line((-40.5, 4.6), (-40.5, 0))
                Line((-67.5, 4.6), (-40.5, 4.6))
                Line((-67.5, 0), (-67.5, 4.6))
            make_face()
        # OneSide extrude, distance=-0.075
        extrude(amount=-0.075, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoe last or form featuring a curved, anatomical foot-shaped base with a tall vertical post/stem extending upward, designed with ribbed surface details and a flange around the bottom perimeter for stability and support.
def model_21822_7d3db422_0017():
    """Model: Crank"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3194689145, perimeter: 5.598229715
            with BuildLine():
                Line((3.0000000447, 4.0000000447), (3.0000000447, 3.4000000447))
                CenterArc((3.0000000447, 3.0000000447), 0.4, -90, 180)
                Line((3.0000000447, 2.6000000447), (3.0000000447, 2.0000000447))
                CenterArc((3.0000000447, 3.0000000447), 1, -90, 180)
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.191774955, perimeter: 25.4238395491
            with BuildLine():
                Line((3.8000000447, 4.7000000447), (3.8000000447, 5.5000000447))
                CenterArc((3.0000000447, 5.5000000447), 0.8, 0, 90)
                Line((3.0000000447, 6.3000000447), (3.0000000447, 4.0000000447))
                CenterArc((3.0000000447, 3.0000000447), 1, -90, 180)
                Line((3.0000000447, 2.0000000447), (3.0000000447, 1.4000000447))
                CenterArc((3.0000000447, 3.0000000447), 1.6, -90, 56.0484500934)
                CenterArc((4.5345937986, 1.9667904772), 0.25, 50.3465427795, 95.7019073139)
                CenterArc((6.8000000447, 4.7000000447), 3.3, -129.6534572205, 26.1653496919)
                CenterArc((5.9719855096, 1.2479148879), 0.25, -30.5207763647, 107.0326688361)
                CenterArc((3.0000000447, 3.0000000447), 3.7, -90, 59.4792236353)
                Line((3.0000000447, -0.6999999553), (3.0000000447, -0.9999999553))
                CenterArc((3.0000000447, 3.0000000447), 4, -90, 60.593805564)
                CenterArc((6.0490626095, 1.2815072528), 0.5, -29.406194436, 107.0168578743)
                CenterArc((6.8000000447, 4.7000000447), 3, 180, 77.6106634383)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.065361648, perimeter: 9.897781083
            with BuildLine():
                Line((3.0000000447, 1.4000000447), (3.0000000447, -0.6999999553))
                CenterArc((3.0000000447, 3.0000000447), 3.7, -90, 59.4792236353)
                CenterArc((5.9719855096, 1.2479148879), 0.25, -30.5207763647, 107.0326688361)
                CenterArc((6.8000000447, 4.7000000447), 3.3, -129.6534572205, 26.1653496919)
                CenterArc((4.5345937986, 1.9667904772), 0.25, 50.3465427795, 95.7019073139)
                CenterArc((3.0000000447, 3.0000000447), 1.6, -90, 56.0484500934)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.065361648, perimeter: 9.897781083
            with BuildLine():
                Line((3.0000000447, 1.4000000447), (3.0000000447, -0.6999999553))
                CenterArc((3.0000000447, 3.0000000447), 3.7, -90, 59.4792236353)
                CenterArc((5.9719855096, 1.2479148879), 0.25, -30.5207763647, 107.0326688361)
                CenterArc((6.8000000447, 4.7000000447), 3.3, -129.6534572205, 26.1653496919)
                CenterArc((4.5345937986, 1.9667904772), 0.25, 50.3465427795, 95.7019073139)
                CenterArc((3.0000000447, 3.0000000447), 1.6, -90, 56.0484500934)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: A dark cylindrical battery or power cell housing with vertical ribbed/fluted sides, a recessed top opening with contact terminals or connectors, and a slightly tapered upper section.
def model_21822_7d3db422_0018():
    """Model: Crosshead Container"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.9520415666, perimeter: 27.0810547043
            with BuildLine():
                Line((19.0000002831, -12.8000001907), (21, -12.8000001907))
                Line((19.0000002831, -12.8000001907), (19.0000002831, -10.600000158))
                Line((19.0000002831, -10.600000158), (18.7000002787, -10.600000158))
                Line((18.7000002787, -10.600000158), (18.7000002787, -9.6000001431))
                Line((18.7000002787, -9.6000001431), (17.7000002638, -9.6000001431))
                Line((17.7000002638, -9.6000001431), (17.7000002638, -9.0000001341))
                Line((17.7000002638, -9.0000001341), (17.4382622038, -9.0000001341))
                CenterArc((20, -11), 3.25, 142.0201305547, 97.4696320392)
                Line((18.35, -13.8), (21.65, -13.8))
                CenterArc((20, -11), 3.25, -59.4897625939, 97.4696320392)
                Line((22.3000003323, -9.0000001341), (22.5617377962, -9.0000001341))
                Line((22.3000003323, -9.6000001431), (22.3000003323, -9.0000001341))
                Line((21.3000003174, -9.6000001431), (22.3000003323, -9.6000001431))
                Line((21.3000003174, -10.6), (21.3000003174, -9.6000001431))
                Line((21, -10.6), (21.3000003174, -10.6))
                Line((21, -12.8000001907), (21, -10.6))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-22.349231552, 10.1449496417)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-22.349231552, 11.8550503583)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-21.25, 13.1650635095)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-18.75, 13.1650635095)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-17.650768448, 11.8550503583)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-17.650768448, 10.1449496417)):
                Circle(0.2)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bent or L-shaped hollow duct or channel with a rectangular cross-section, featuring a 90-degree elbow joint connecting two parallel tubular sections with visible internal geometry and structural ribbing or bracing.
def model_21822_7d3db422_0019():
    """Model: Crosshead"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1800001115, perimeter: 12.3999997973
            with BuildLine():
                Line((-15, -5), (-15, -5.75))
                Line((-15, -5.75), (-13.6, -5.75))
                Line((-13.6000002027, -6.85), (-13.6, -5.75))
                Line((-15, -6.85), (-13.6000002027, -6.85))
                Line((-15, -7.6), (-15, -6.85))
                Line((-12.8, -7.6), (-15, -7.6))
                Line((-12.8, -5), (-12.8, -7.6))
                Line((-15, -5), (-12.8, -5))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-15, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.06, perimeter: 1
            with BuildLine():
                Line((5.3, 0.2), (5.3, 0))
                Line((5, 0.2), (5.3, 0.2))
                Line((5, 0.2), (5, 0))
                Line((5, 0), (5.3, 0))
            make_face()
        # OneSide extrude, distance=-3.6
        extrude(amount=-3.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a slotted spoon or spatula utensil featuring an elongated handle with a rounded, perforated bowl head at one end for draining or serving food.
def model_21822_7d3db422_0021():
    """Model: Eccentric Trap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.752295225, perimeter: 50.8758607486
            with BuildLine():
                CenterArc((0, -13), 0.4, -89.6374023723, 179.2748047446)
                Line((-15.8, -12.5), (0.0025313921, -12.60000801))
                Line((-15.8, -12.5), (-16.6411546205, -12.5))
                CenterArc((-16.6411546205, -12.1), 0.4, -149.99999288, 59.99999288)
                CenterArc((-18.2000002354, -13.0000001937), 1.4, 30.00000712, 300)
                CenterArc((-16.6411543968, -13.9), 0.4, 90, 60.00000712)
                Line((-15.8, -13.5), (-16.6411543968, -13.5))
                Line((0.0025313921, -13.39999199), (-15.8, -13.5))
            make_face()
            with BuildLine():
                CenterArc((-18.2000002354, -13.0000001937), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -13), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4065048269, perimeter: 17.7619537545
            with BuildLine():
                Line((15.8000002354, 13.0000001937), (15.8, 13.5))
                Line((15.8000002354, 13.0000001937), (15.8, 12.5))
                Line((15.8, 12.5), (16.6411546205, 12.5))
                CenterArc((16.6411546205, 12.1), 0.4, 30.00000712, 59.99999288)
                CenterArc((18.2000002354, 13.0000001937), 1.4, -149.99999288, 300)
                CenterArc((16.6411543968, 13.9), 0.4, -90, 60.00000712)
                Line((16.6411543968, 13.5), (15.8, 13.5))
            make_face()
            with BuildLine():
                CenterArc((18.2000002354, 13.0000001937), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


# Description: This is a structural bracket or mounting assembly with an overall cubic/box-like shape featuring internal ribbing, a protruding cylindrical or rectangular post element, and multiple flat flanges designed for bolted attachment and load support.
def model_21822_7d3db422_0034():
    """Model: Slide Valve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4485840714, perimeter: 9.4283185516
            with BuildLine():
                Line((-6.3000001043, 1.7000000373), (-6.3000001043, 3.3000000373))
                Line((-6.3000001043, 3.3000000373), (-7.7000001043, 3.3000000373))
                Line((-7.7000001043, 3.3000000373), (-7.7000001043, 1.7000000373))
                Line((-7.7000001043, 1.7000000373), (-6.3000001043, 1.7000000373))
            make_face()
            with BuildLine():
                Line((-7.3000001043, 2.0000000373), (-6.7000346265, 2.0000000373))
                CenterArc((-7.3000001043, 2.1000000373), 0.1, 180, 90)
                Line((-7.4000001043, 2.9000000373), (-7.4000001043, 2.1000000373))
                CenterArc((-7.3000001043, 2.9000000373), 0.1, 90, 90)
                Line((-6.7000346265, 3.0000000373), (-7.3000001043, 3.0000000373))
                CenterArc((-6.7000000998, 2.9000000432), 0.1, -0.0171320093, 90.0369143504)
                Line((-6.6000001043, 2.1000299323), (-6.6000001043, 2.8999701422))
                CenterArc((-6.7000000998, 2.1000000313), 0.1, -90.0197823406, 90.0369143494)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4085841071, perimeter: 7.9283186261
            with BuildLine():
                Line((7.5000001118, -3.1000000462), (7.5000001118, -1.9000000283))
                Line((7.5000001118, -1.9000000283), (6.5000000969, -1.9000000283))
                Line((6.5000000969, -1.9000000283), (6.5000000969, -3.1000000462))
                Line((6.5000000969, -3.1000000462), (7.0000001043, -3.1000000462))
                Line((7.0000001043, -3.0000000373), (7.0000001043, -3.1000000462))
                Line((7.0000001043, -3.0000000373), (6.7000346265, -3.0000000373))
                CenterArc((6.7000000998, -2.9000000432), 0.1, 179.9828679907, 90.0369143504)
                Line((6.6000001043, -2.8999701422), (6.6000001043, -2.1000299323))
                CenterArc((6.7000000998, -2.1000000313), 0.1, 89.9802176594, 90.0369143494)
                Line((6.7000346265, -2.0000000373), (7.3000001043, -2.0000000373))
                CenterArc((7.3000001043, -2.1000000373), 0.1, 0, 90)
                Line((7.4000001043, -2.1000000373), (7.4000001043, -2.9000000373))
                CenterArc((7.3000001043, -2.9000000373), 0.1, -90, 90)
                Line((7.3000001043, -3.0000000373), (7.0000001043, -3.0000000373))
                Line((7.0000001043, -3.1000000462), (7.5000001118, -3.1000000462))
            make_face()
            # Profile area: 0.7914159286, perimeter: 3.4283185516
            with BuildLine():
                Line((7.3000001043, -3.0000000373), (7.0000001043, -3.0000000373))
                CenterArc((7.3000001043, -2.9000000373), 0.1, -90, 90)
                Line((7.4000001043, -2.1000000373), (7.4000001043, -2.9000000373))
                CenterArc((7.3000001043, -2.1000000373), 0.1, 0, 90)
                Line((6.7000346265, -2.0000000373), (7.3000001043, -2.0000000373))
                CenterArc((6.7000000998, -2.1000000313), 0.1, 89.9802176594, 90.0369143494)
                Line((6.6000001043, -2.8999701422), (6.6000001043, -2.1000299323))
                CenterArc((6.7000000998, -2.9000000432), 0.1, 179.9828679907, 90.0369143504)
                Line((7.0000001043, -3.0000000373), (6.7000346265, -3.0000000373))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a curved drainage gutter or downspout elbow with a flat top flange for mounting and a rounded, tapered bottom section that directs water flow downward and outward.
def model_21847_b2de7eb8_0003():
    """Model: 07A (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.6469346884, perimeter: 29.1983941362
            with BuildLine():
                CenterArc((5.5, -4), 1.9, -148.3229126945, 116.645825389)
                Line((10.17, -0.05), (7.1169402392, -4.9977495993))
                Line((11, -0.05), (10.17, -0.05))
                Line((11, 0), (11, -0.05))
                Line((0, 0), (11, 0))
                Line((0, -0.05), (0, 0))
                Line((0.83, -0.05), (0, -0.05))
                Line((0.83, -0.05), (3.8830597608, -4.9977495993))
            make_face()
            with BuildLine():
                CenterArc((5.5, -4), 0.15, 180, 180)
                CenterArc((5.5, -4), 0.15, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.15, perimeter: 23.3
            with BuildLine():
                Line((0, 0.6), (0, -0.05))
                Line((0, -0.05), (11, -0.05))
                Line((11, -0.05), (11, 0.6))
                Line((11, 0.6), (0, 0.6))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or connector housing with an elongated rectangular body, rounded end caps on both sides, a central slot or opening along the top surface, and textured or knurled circular features on the ends for gripping or assembly purposes.
def model_21847_b2de7eb8_0004():
    """Model: 04A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0427433388, perimeter: 7.1132741229
            with BuildLine():
                CenterArc((0.2, -0.6), 0.2, 180, 90)
                Line((2.3, -0.8), (0.2, -0.8))
                CenterArc((2.3, -0.4), 0.4, -90, 180)
                Line((0.2, 0), (2.3, 0))
                CenterArc((0.2, -0.2), 0.2, 90, 90)
                Line((0, -0.6), (0, -0.2))
            make_face()
            with BuildLine():
                CenterArc((0.9, -0.4), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((2.3, -0.4), 0.4, 90, 180)
                CenterArc((2.3, -0.4), 0.4, -90, 180)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a bicycle fork with a curved top tube, two parallel downtubes, a center mounting hole, and reinforced end flanges designed to attach to a bike frame and hold the front wheel.
def model_21847_b2de7eb8_0005():
    """Model: 05A FIXED"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.2006206229, perimeter: 33.2479770187
            with BuildLine():
                Line((3.1732637677, 1.264467267), (2.7732637677, 1.264467267))
                Line((2.7732637677, 1.264467267), (2.7732637677, 1.464467267))
                CenterArc((2.9732637677, -0.0221396077), 1.5, 97.6622556608, 64.0698243382)
                Line((0.0732637677, -4.0221396077), (1.5488620671, 0.4480516252))
                Line((0.0732637677, -4.0221396077), (-0.0267362323, -4.0221396077))
                Line((-0.0267362323, -4.0221396077), (-0.0267362323, -5.0221396077))
                Line((0.5732637677, -5.0221396077), (-0.0267362323, -5.0221396077))
                Line((0.5732637677, -5.0221396077), (0.5732637677, -4.0221396077))
                Line((0.5732637677, -4.0221396077), (1.8109359715, -0.4347713186))
                CenterArc((2.0000000298, -0.5000000075), 0.2, 13.8754650036, 147.0896704048)
                Line((2.1941638822, -0.4520375387), (2.4881204102, -1.6420457559))
                CenterArc((2.9735300413, -1.5221395841), 0.5, -166.1245349964, 149.8999180775)
                Line((3.453616906, -1.6618414175), (3.8079653137, -0.4441192741))
                CenterArc((4.0000000596, -0.5000000075), 0.2, 18.2679200011, 145.50746308)
                Line((5.3732637677, -4.0221396077), (4.1899202863, -0.4373078431))
                Line((5.3732637677, -5.0221396077), (5.3732637677, -4.0221396077))
                Line((5.9732637677, -5.0221396077), (5.3732637677, -5.0221396077))
                Line((5.9732637677, -4.0221396077), (5.9732637677, -5.0221396077))
                Line((5.8732637677, -4.0221396077), (5.9732637677, -4.0221396077))
                Line((5.8732637677, -4.0221396077), (4.3976654682, 0.4480516252))
                CenterArc((2.9732637677, -0.0221396077), 1.5, 18.2679200011, 64.0698243382)
                Line((3.1732637677, 1.264467267), (3.1732637677, 1.464467267))
            make_face()
            with BuildLine():
                CenterArc((2.9735300413, -1.5221395841), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1, perimeter: 2.2
            with BuildLine():
                Line((5.8732637677, -5.0221396077), (5.9732637677, -5.0221396077))
                Line((5.9732637677, -5.0221396077), (5.9732637677, -4.0221396077))
                Line((5.9732637677, -4.0221396077), (5.8732637677, -4.0221396077))
                Line((5.8732637677, -4.0221396077), (5.8732637677, -5.0221396077))
            make_face()
            # Profile area: 0.1, perimeter: 2.2
            with BuildLine():
                Line((-0.0267362323, -4.0221396077), (0.0732637677, -4.0221396077))
                Line((-0.0267362323, -5.0221396077), (-0.0267362323, -4.0221396077))
                Line((0.0732637677, -5.0221396077), (-0.0267362323, -5.0221396077))
                Line((0.0732637677, -4.0221396077), (0.0732637677, -5.0221396077))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical industrial component with a rounded, barrel-like shape featuring three evenly-spaced circular holes or ports around its circumference and a central axial bore.
def model_21847_b2de7eb8_0008():
    """Model: 02B"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7147123287, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
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
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a bicycle fork, characterized by a curved upper crown, two parallel downward-extending legs with dropouts at the ends, and a central hole for headtube insertion.
def model_21847_b2de7eb8_0011():
    """Model: 05A (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.2514828029, perimeter: 33.1626217081
            with BuildLine():
                Line((3.2, 1.2866068747), (2.8, 1.2866068747))
                Line((2.8, 1.2866068747), (2.8, 1.4866068747))
                CenterArc((3, 0), 1.5, 97.6622556608, 64.0698243382)
                Line((0.1, -4), (1.5755982995, 0.4701912329))
                Line((0.1, -4), (0, -4))
                Line((0, -4), (0, -5))
                Line((0.6, -5), (0, -5))
                Line((0.6, -5), (0.6, -4))
                Line((0.6, -4), (1.8106253454, -0.4356787037))
                CenterArc((2.0000000298, -0.5000000075), 0.200000003, 15.4753600829, 145.7645320299)
                Line((2.1927490905, -0.4466352178), (2.52132114, -1.6334093869))
                CenterArc((3.0031967506, -1.4999965936), 0.5000030775, -164.5246399171, 149.3367750655)
                Line((3.8069856588, -0.4476030507), (3.4857357227, -1.6309897918))
                CenterArc((4.0000000596, -0.5000000075), 0.2, 18.7601078037, 146.0520273447)
                Line((5.4000000805, -4), (4.1893747412, -0.435678705))
                Line((5.4000000805, -5), (5.4000000805, -4))
                Line((6, -5), (5.4000000805, -5))
                Line((6, -5), (6, -4))
                Line((6, -4), (5.9, -4))
                Line((5.9, -4), (4.4244017005, 0.4701912329))
                CenterArc((3, 0), 1.5, 18.2679200011, 64.0698243382)
                Line((3.2, 1.2866068747), (3.2, 1.4866068747))
            make_face()
            with BuildLine():
                CenterArc((3.0031967506, -1.4999965936), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1, perimeter: 2.2
            with BuildLine():
                Line((5.9, -5), (6, -5))
                Line((6, -5), (6, -4))
                Line((6, -4), (5.9, -4))
                Line((5.9, -4), (5.9, -5))
            make_face()
            # Profile area: 0.1, perimeter: 2.2
            with BuildLine():
                Line((0, -4), (0.1, -4))
                Line((0, -5), (0, -4))
                Line((0.1, -5), (0, -5))
                Line((0.1, -4), (0.1, -5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a dark gray metal angle bracket or L-shaped corner brace with two perpendicular tubular arms of equal length, featuring a reinforced joint at the corner bend.
def model_21847_b2de7eb8_0014():
    """Model: 01A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.219999994, perimeter: 4.599999997
            with BuildLine():
                Line((0.1000000015, -0.1000000015), (0.1000000015, -0.7))
                Line((0.1000000015, -0.1000000015), (0.9000000134, -0.1000000015))
                Line((0.9000000134, -0.1000000015), (0.9000000134, -0.7))
                Line((1, -0.7), (0.9000000134, -0.7))
                Line((1, 0), (1, -0.7))
                Line((0, 0), (1, 0))
                Line((0, -0.7), (0, 0))
                Line((0.1000000015, -0.7), (0, -0.7))
            make_face()
        # OneSide extrude, distance=11.3
        extrude(amount=11.3)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2200000031, perimeter: 4.6000000179
            with BuildLine():
                Line((0.1000000015, -0.7000000104), (0, -0.7000000104))
                Line((0.1000000015, -0.1000000015), (0.1000000015, -0.7000000104))
                Line((0.9, -0.1000000015), (0.1000000015, -0.1000000015))
                Line((0.9, -0.7), (0.9, -0.1000000015))
                Line((1, -0.7), (0.9, -0.7))
                Line((1, 0), (1, -0.7))
                Line((0, 0), (1, 0))
                Line((0, -0.7000000104), (0, 0))
            make_face()
        # OneSide extrude, distance=11.3
        extrude(amount=11.3)
    return part.part


# Description: This is a conical funnel or strainer with a triangular trapezoidal profile, featuring a wide flat rim at the top for mounting or pouring, tapered sides that converge downward, and a rounded cone-shaped base that narrows to a central point or drain opening.
def model_21847_b2de7eb8_0015():
    """Model: 07A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.6469346884, perimeter: 29.1983941362
            with BuildLine():
                CenterArc((5.5, -4), 1.9, -148.3229126945, 116.645825389)
                Line((10.17, -0.05), (7.1169402392, -4.9977495993))
                Line((11, -0.05), (10.17, -0.05))
                Line((11, 0), (11, -0.05))
                Line((0, 0), (11, 0))
                Line((0, -0.05), (0, 0))
                Line((0.83, -0.05), (0, -0.05))
                Line((0.83, -0.05), (3.8830597608, -4.9977495993))
            make_face()
            with BuildLine():
                CenterArc((5.5, -4), 0.15, 0, 90)
                CenterArc((5.5, -4), 0.15, -180, 180)
                CenterArc((5.5, -4), 0.15, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4465437945, perimeter: 22.6867661724
            with BuildLine():
                Line((1.2000000089, -0.05), (0.0000000089, -0.05))
                CenterArc((0.6000000089, -0.05), 0.6, -180, 90)
                Line((10.4018594167, -0.65), (0.6000000089, -0.65))
                CenterArc((10.4018594167, -0.05), 0.6, -90, 85.4880675472)
                Line((11, -0.05), (11, -0.0972000276))
                Line((11, -0.05), (9.8018594167, -0.05))
                Line((9.8018594167, -0.05), (1.2000000089, -0.05))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical pipe or sleeve with a smooth barrel body and threaded ends on both sides for connection or assembly purposes.
def model_21852_6cf9a734_0007():
    """Model: Heat Exchange Cylinder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5811946409, perimeter: 23.2477856366
            with BuildLine():
                CenterArc((0, 0), 1.875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.825, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.8
        extrude(amount=12.8)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5811946409, perimeter: 23.2477856366
            with BuildLine():
                CenterArc((0, 0), 1.875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.825, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2964878067, perimeter: 23.7190245346
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.6
        extrude(amount=-3.6, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal box or container with a complex internal cavity featuring multiple angled walls and internal geometric divisions, designed with chamfered or beveled edges on the exterior faces.
def model_21852_6cf9a734_0016():
    """Model: Slide v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8, perimeter: 5.6
            with BuildLine():
                Line((0.9, -0.5), (0.9, 0.5))
                Line((0.9, 0.5), (-0.9, 0.5))
                Line((-0.9, 0.5), (-0.9, -0.5))
                Line((-0.9, -0.5), (0.9, -0.5))
            make_face()
        # OneSide extrude, distance=0.72
        extrude(amount=0.72)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.72, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple two-bar linkage or connector bracket consisting of two parallel rounded rectangular bars (or flat straps) positioned at different heights, likely designed to be joined together or mounted to a larger assembly.
def model_21859_35124f79_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-20, 0)):
                Circle(2.5)
        # Symmetric extrude, each_side=40
        extrude(amount=40, both=True)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.2619467106, perimeter: 6.1699111843
            with BuildLine():
                Line((-74.0727392965, -48.9402734817), (-72.4923282376, -47.1340894145))
                CenterArc((-73.2825337671, -48.0371814481), 1.2, -131.1859251657, 180)
            make_face()
            # Profile area: 2.2619467106, perimeter: 6.1699111843
            with BuildLine():
                CenterArc((-73.2825337671, -48.0371814481), 1.2, 48.8140748343, 180)
                Line((-74.0727392965, -48.9402734817), (-72.4923282376, -47.1340894145))
            make_face()
        # Symmetric extrude, each_side=50
        extrude(amount=50, both=True)
    return part.part


# Description: This is a spacer or standoff with a simple cylindrical shape, featuring two parallel flat surfaces (top and bottom) separated by a vertical gap, used to maintain distance or alignment between components in an assembly.
def model_21865_c190b734_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 49.5955659336, perimeter: 24.9647003257
            with Locations((-43.2196239026, 1.64893893)):
                Circle(3.9732554596)
        # Symmetric extrude, each_side=60
        extrude(amount=60, both=True)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-137, -57)):
                Circle(2.5)
        # Symmetric extrude, each_side=70
        extrude(amount=70, both=True)
    return part.part


# Description: This is an L-shaped bracket or handle with a rounded horizontal arm extending to the right and a vertical curved section on the left, featuring a circular hole or opening in the vertical portion.
def model_21881_f3bee5e5_0005():
    """Model: Centre v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 180)
                CenterArc((0, 0), 1.5, -180, 180)
            make_face()
            # Profile area: 8.7328541324, perimeter: 21.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.5, -180, 180)
                Line((-1.5, 0), (-1.5, -3.5))
                CenterArc((0, -3.5), 1.5, -180, 180)
                Line((1.5, -3.5), (1.5, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -3.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, -3.5)):
                Circle(0.75)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 180)
                CenterArc((0, 0), 1.5, -180, 180)
            make_face()
        # OneSide extrude, distance=18
        extrude(amount=18, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, -3.5)):
                Circle(0.75)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or vessel with an open top featuring an inward-curved rim or flange and a flat or slightly recessed bottom.
def model_21893_0500d043_0026():
    """Model: ISO 4026-M3 x 3 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0346410162, perimeter: 0.692820323
            with BuildLine():
                Line((-0.1, 0.0577350269), (-0.1, -0.0577350269))
                Line((-0.1, -0.0577350269), (0, -0.1154700538))
                Line((0, -0.1154700538), (0.1, -0.0577350269))
                Line((0.1, -0.0577350269), (0.1, 0.0577350269))
                Line((0.1, 0.0577350269), (0, 0.1154700538))
                Line((0, 0.1154700538), (-0.1, 0.0577350269))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal prism or column with a hollow or internally structured core, featuring triangulated internal geometry visible through the semi-transparent left face, and solid outer walls forming a tall, angular elongated shape.
def model_21893_0500d043_0038():
    """Model: SEMI CUSCINETTO v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.61, perimeter: 7.6
            with BuildLine():
                Line((0.95, -0.95), (0.95, 0.95))
                Line((0.95, 0.95), (-0.95, 0.95))
                Line((-0.95, 0.95), (-0.95, -0.95))
                Line((-0.95, -0.95), (0.95, -0.95))
            make_face()
        # Symmetric extrude, each_side=2.35
        extrude(amount=2.35, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.95), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.08, perimeter: 7.2
            with BuildLine():
                Line((-0.7, 1.1), (0.7, 1.1))
                Line((-0.7, -1.1), (-0.7, 1.1))
                Line((0.7, -1.1), (-0.7, -1.1))
                Line((0.7, 1.1), (0.7, -1.1))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an angular bracket or lever assembly with a horizontal bar section at the top and a angled arm extending downward, featuring dark metallic construction with a blue accent stripe and textured grip surfaces at the connection points.
def model_21893_0500d043_0041():
    """Model: T DI CONNESSIONE v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.7040012379, perimeter: 39.7448147303
            with BuildLine():
                Line((-4.2500039011, 0.5999999679), (-0.0000000186, 0.6))
                CenterArc((-4.2500000086, -0.0000000321), 0.6, -95.5000004288, 185.5003721408)
                Line((-4.3075074646, -0.5972377507), (-0.6135, -0.9529301822))
                Line((-0.6135, -0.9529301822), (-0.4894399499, -5.8542727473))
                CenterArc((-0.0000051866, -6.9499253557), 1.2000004274, 114.0706094474, 65.9777485651)
                Line((-1.2000051866, -7.55), (-1.2000051866, -6.9509381638))
                Line((1.1999948134, -7.55), (-1.2000051866, -7.55))
                Line((1.1999948134, -7.55), (1.1999948134, -6.9509381638))
                CenterArc((-0.0000051866, -6.9499253557), 1.2000004274, -0.0483580126, 65.9778301254)
                Line((0.4894280171, -5.8542720506), (0.6135, -0.9529301822))
                Line((0.6135, -0.9529301822), (4.3075074585, -0.5972376873))
                CenterArc((4.250000011, 0.0000000321), 0.6, 90.0006190826, 185.4993805269)
                Line((-0.0000000186, 0.6), (4.249993528, 0.6000000321))
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-4.2500000086, -0.0000000321), 0.6, 90.000371712, 174.4996278592)
                CenterArc((-4.2500000086, -0.0000000321), 0.6, -95.5000004288, 185.5003721408)
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((4.250000011, 0.0000000321), 0.6, -84.5000003905, 174.5006194731)
                CenterArc((4.250000011, 0.0000000321), 0.6, 90.0006190826, 185.4993805269)
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # Symmetric extrude, each_side=0.225
        extrude(amount=0.225, both=True)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-4.2500000086, -0.0000000321)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((4.250000011, 0.0000000321)):
                Circle(0.6)
            # Profile area: 2.2619274315, perimeter: 6.1698848904
            with BuildLine():
                CenterArc((-0.0000000726, -7.55), 1.199994886, 0, 180)
                Line((-1.1999949587, -7.55), (1.1999948134, -7.55))
            make_face()
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or tube with an open top and an inward-facing flange or lip around the upper rim, featuring a slightly tapered or curved upper edge and smooth cylindrical sidewalls.
def model_21894_93f0d052_0001():
    """Model: Piston v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple cylindrical rod or tube with a uniform circular cross-section, tapered slightly at the ends, and appears to be made of dark metal or composite material.
def model_21894_93f0d052_0016():
    """Model: Flywheelshaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2)
    return part.part


# Description: This is a rectangular boat hull or container structure with a trapezoidal profile, featuring two prominent vertical fin or blade-like protrusions extending upward from the center, reinforced internal ribbing and cross-bracing, and sloped side panels.
def model_21899_d55d6c08_0011():
    """Model: BSE005-1 v1 (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8391504561, perimeter: 10.2106192983
            with BuildLine():
                Line((1.25, -0.8), (1.25, 0.8))
                Line((1.25, 0.8), (-1.25, 0.8))
                Line((-1.25, 0.8), (-1.25, -0.8))
                Line((-1.25, -0.8), (1.25, -0.8))
            make_face()
            with BuildLine():
                CenterArc((-0.8, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.96, perimeter: 4.4
            with BuildLine():
                Line((-0.3, 0.8), (-0.3, -0.8))
                Line((-0.3, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, 0.8))
                Line((0.3, 0.8), (-0.3, 0.8))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex composite housing or structural component featuring an irregular polygonal shape with multiple angular faces, internal cavities, ribbed reinforcement sections, and cutout areas designed for assembly or integration purposes.
def model_21899_d55d6c08_0012():
    """Model: BSE041-1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7918252296, perimeter: 9.2853981634
            with BuildLine():
                Line((0, 0), (0, 1.7))
                Line((1.95, 0), (0, 0))
                Line((1.95, 1.7), (1.95, 0))
                Line((1.225, 1.7), (1.95, 1.7))
                Line((1.225, 0.85), (1.225, 1.7))
                CenterArc((0.975, 0.85), 0.25, 180, 180)
                Line((0.725, 0.85), (0.725, 1.7))
                Line((0, 1.7), (0.725, 1.7))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.90112529, perimeter: 4.9812559873
            with BuildLine():
                Line((0, 0), (-1.95, 0))
                Line((-1.95, 0), (-1.95, -0.5))
                Line((-1.95, -0.5), (-1.3320714214, -0.5))
                CenterArc((-0.975, -0.85), 0.5, 44.4270040008, 91.1459919984)
                Line((-0.6179285786, -0.5), (0, -0.5))
                Line((0, -0.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is an adjustable wrench (crescent wrench) featuring a fixed upper jaw with teeth, a movable lower jaw operated by a worm screw mechanism, and a tapered handle for gripping.
def model_21899_d55d6c08_0024():
    """Model: BSE023-1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4966942613, perimeter: 3.2151467436
            with BuildLine():
                CenterArc((0, 1.95), 0.5, -120, 60)
                Line((-0.25, 1.5169872981), (-0.25, 0.4330127019))
                CenterArc((0, 0), 0.5, 60, 60)
                Line((0.25, 0.4330127019), (0.25, 1.5169872981))
            make_face()
            # Profile area: 0.4480705236, perimeter: 4.2694174452
            with BuildLine():
                CenterArc((0, 1.95), 0.5, -60, 300)
                Line((-0.25, 1.95), (-0.25, 1.5169872981))
                CenterArc((0, 1.95), 0.25, 0, 180)
                Line((0.25, 1.5169872981), (0.25, 1.95))
            make_face()
            # Profile area: 0.4480705236, perimeter: 4.2694174452
            with BuildLine():
                Line((0.25, 0), (0.25, 0.4330127019))
                CenterArc((0, 0), 0.25, -180, 180)
                Line((-0.25, 0.4330127019), (-0.25, 0))
                CenterArc((0, 0), 0.5, 120, 300)
            make_face()
            # Profile area: 0.1409780989, perimeter: 2.1750223428
            with BuildLine():
                CenterArc((0, 0), 0.5, 60, 60)
                Line((-0.25, 0.4330127019), (-0.25, 0))
                CenterArc((0, 0), 0.25, 0, 180)
                Line((0.25, 0), (0.25, 0.4330127019))
            make_face()
            # Profile area: 0.1409780989, perimeter: 2.1750223428
            with BuildLine():
                Line((0.25, 1.5169872981), (0.25, 1.95))
                CenterArc((0, 1.95), 0.25, 180, 180)
                Line((-0.25, 1.95), (-0.25, 1.5169872981))
                CenterArc((0, 1.95), 0.5, -120, 60)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, -60, 300)
                CenterArc((0, 0), 0.5, -120, 60)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, -1.95), 0.5, 120, 300)
                CenterArc((0, -1.95), 0.5, 60, 60)
            make_face()
            with BuildLine():
                CenterArc((0, -1.95), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.15, against=-0.45
        extrude(amount=0.15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.45, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box or enclosure with an open top featuring a recessed rectangular slot or cutout on the upper surface and angled side walls that taper inward toward the top.
def model_21900_760d2078_0000():
    """Model: Screen Box v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.8192, perimeter: 17.96
            with BuildLine():
                Line((0, 2.96), (0, 0))
                Line((0, 0), (6.02, 0))
                Line((6.02, 0), (6.02, 2.96))
                Line((6.02, 2.96), (0, 2.96))
            make_face()
        # OneSide extrude, distance=1.36
        extrude(amount=1.36)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.36, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5985, perimeter: 11.99
            with BuildLine():
                Line((-4.45, -0.56), (-0.275, -0.56))
                Line((-4.45, -2.38), (-4.45, -0.56))
                Line((-0.275, -2.38), (-4.45, -2.38))
                Line((-0.275, -0.56), (-0.275, -2.38))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, elongated hexagonal or trapezoidal tray/pan with a shallow depth, featuring an internal ribbed or truss-like structural framework visible through a recessed top surface.
def model_21900_760d2078_0002():
    """Model: Bottom Box v12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 218.24, perimeter: 67.2
            with BuildLine():
                Line((0, 8.8), (0, 0))
                Line((0, 0), (24.8, 0))
                Line((24.8, 0), (24.8, 8.8))
                Line((24.8, 8.8), (0, 8.8))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 105.5088520653, perimeter: 91.7052978331
            with BuildLine():
                CenterArc((24.05, -0.75), 0.575, 0, 90)
                Line((24.05, -0.175), (23.0003332299, -0.175))
                Line((22.3406110076, -0.8), (23.0003332299, -0.175))
                Line((16.8442988206, -0.8), (22.3406110076, -0.8))
                Line((14.35, -2.2172152389), (16.8442988206, -0.8))
                Line((14.35, -2.2172152389), (8.55, -2.2172152389))
                CenterArc((6.55, -2.6801125313), 2.0528696752, 13.0315706699, 153.9368586602)
                Line((4.55, -2.2172152389), (0.7, -2.2172152389))
                Line((0.7, -2.2172152389), (0.7, -8.1))
                Line((0.7, -8.1), (21.2, -8.1))
                Line((21.2, -8.1), (21.5031088913, -8.625))
                Line((21.5031088913, -8.625), (24.05, -8.625))
                CenterArc((24.05, -8.05), 0.575, -90, 90)
                Line((24.625, -8.05), (24.625, -4.8))
                Line((24.625, -4.8), (24, -7.85))
                Line((24, -7.85), (23.4, -8.45))
                Line((23.4, -8.45), (22.7, -8.45))
                Line((22.7, -8.45), (22, -7.87))
                Line((22, -7.87), (21.4, -6.5))
                Line((21.4, -6.5), (16.4, -6.5))
                Line((16.4, -6.5), (14.75, -6.15))
                Line((14.75, -6.15), (14.75, -2.45))
                Line((14.75, -2.45), (16.95, -1.2))
                Line((16.95, -1.2), (22.5, -1.2))
                Line((22.5, -1.2), (23.45, -0.3))
                Line((23.45, -0.3), (24.25, -0.3))
                Line((24.25, -0.3), (24.625, -2.5))
                Line((24.625, -2.5), (24.625, -0.75))
            make_face()
        # OneSide extrude, distance=-1.36
        extrude(amount=-1.36, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular tray or pan with an elongated, shallow box shape featuring angled side walls, recessed central channels or slots running lengthwise, and raised flanged edges along the perimeter.
def model_21900_760d2078_0003():
    """Model: Face Stay Bar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.67693, perimeter: 3.754
            with BuildLine():
                Line((1.39, -0.487), (0, -0.487))
                Line((1.39, 0), (1.39, -0.487))
                Line((0, 0), (1.39, 0))
                Line((0, -0.487), (0, 0))
            make_face()
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.12, 0.2435)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.27, 0.2435)):
                Circle(0.15)
        # OneSide extrude, distance=-0.07
        extrude(amount=-0.07, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh filter or strainer basket with an open top, featuring a curved mesh screen interior and a solid dark base, designed for filtering or sieving applications.
def model_21900_760d2078_0005():
    """Model: Battery v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.47
        extrude(amount=0.47)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.47, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4589670517, perimeter: 6.6758843889
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a geometric wedge or tapered box with a rectangular base, sloping top surface, and internal structural ribs or bracing elements visible through the translucent blue faceted design.
def model_21900_760d2078_0015():
    """Model: Battery Cover v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4288, perimeter: 6.28
            with BuildLine():
                Line((0, 1.76), (0, 0))
                Line((0, 0), (1.38, 0))
                Line((1.38, 0), (1.38, 1.76))
                Line((1.38, 1.76), (0, 1.76))
            make_face()
        # OneSide extrude, distance=0.23
        extrude(amount=0.23)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.23, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0692820323, perimeter: 1.2
            with BuildLine():
                Line((-0.7464101615, -0.88), (-0.4, -1.08))
                Line((-0.4, -1.08), (-0.4, -0.68))
                Line((-0.4, -0.68), (-0.7464101615, -0.88))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)
    return part.part


# Description: This is a hand wheel featuring a large circular disc with a textured rim, connected to a cylindrical handle shaft, commonly used for manual adjustment or control mechanisms.
def model_21908_385686ec_0011():
    """Model: 13A v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical toroidal or torus-shaped component with a large central rectangular passage, featuring radial ribbing or fins on its outer surface and symmetrical rounded ends.
def model_21908_385686ec_0027():
    """Model: 02B v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7147123287, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a coffin or casket with a tapered hexagonal shape, featuring a dark gray body and a blue transparent or translucent lid/viewing panel on top.
def model_21908_385686ec_0028():
    """Model: 11A v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2833959173, perimeter: 3.9747579139
            with BuildLine():
                Line((0, 0), (1.3, 0))
                Line((1.3, 0), (1.3, 0.15))
                Line((1.3, 0.15), (0.2958039892, 0.15))
                CenterArc((0.2958039892, 0.25), 0.1, -170.4059317731, 80.4059317731)
                CenterArc((0, 0.2), 0.2, 9.5940682269, 260.4059317731)
            make_face()
            with BuildLine():
                CenterArc((0, 0.2), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, 0.2)):
                Circle(0.075)
        # TwoSides extrude, along=0.15, against=-0.45
        extrude(amount=0.15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.45, mode=Mode.ADD)
    return part.part


# Description: This is a shaft with a large radial flange, featuring a cylindrical main body extending from a significantly larger disk-like flange on one end, with a central axial hole running through the shaft.
def model_21918_976c2754_0012():
    """Model: Upper Rivet v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3041511643, perimeter: 1.9550131083
            Circle(0.31115)
        # OneSide extrude, distance=1.9177
        extrude(amount=1.9177)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.9177, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9626175334, perimeter: 5.9448357784
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3041511643, perimeter: 1.9550131083
            Circle(0.31115)
        # OneSide extrude, distance=0.16002
        extrude(amount=0.16002, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal enclosure or bracket with a trapezoidal/wedge-shaped body featuring a large open face, reinforcing flanges on the left side, and angled surfaces for structural rigidity.
def model_21923_41fa6eda_0009():
    """Model: Movable Jaw v6 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27.48, perimeter: 28.2
            with BuildLine():
                Line((-2.5, 2.5), (-2.5, -8.1))
                Line((-2.5, -8.1), (-0.3, -8.1))
                Line((-0.3, -8.1), (-0.3, -0.7))
                Line((-0.3, -0.7), (1, -0.7))
                Line((1, 2.5), (1, -0.7))
                Line((-2.5, 2.5), (1, 2.5))
            make_face()
        # OneSide extrude, distance=17.6
        extrude(amount=17.6)
    return part.part


# Description: This is a circular disk or pulley wheel with a flat main body featuring a textured or ribbed rim around its outer edge and what appears to be a central hub or mounting point, designed for rotational applications.
def model_21941_1a683ec2_0009():
    """Model: endscheibe v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.1995568259, perimeter: 54.6637121725
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 55.4176944093, perimeter: 26.3893782902
            Circle(4.2)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((0, -2)):
                Circle(0.65)
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((0, 2)):
                Circle(0.65)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue/navy structural bracket or support component with an angular, asymmetrical design featuring a flat upper flange, a curved/angled body, and a faceted lower section with triangulated geometry, likely designed for mounting or reinforcement applications.
def model_21941_1a683ec2_0014():
    """Model: versteifung v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.2664, perimeter: 38.2093713275
            with BuildLine():
                Line((9.708, -15.222), (8.508, -15.222))
                Line((1.2, -3.072), (9.708, -15.222))
                Line((1.2, 0), (1.2, -3.072))
                Line((0, 0), (1.2, 0))
                Line((0, 0), (0, -3.072))
                Line((8.508, -15.222), (0, -3.072))
            make_face()
            # Profile area: 9.2736, perimeter: 17.856
            with BuildLine():
                Line((8.508, -15.222), (8.508, -22.95))
                Line((8.508, -22.95), (9.708, -22.95))
                Line((9.708, -22.95), (9.708, -15.222))
                Line((9.708, -15.222), (8.508, -15.222))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.708, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.125, perimeter: 11.9497474683
            with BuildLine():
                Line((0, -19.45), (-3.5, -22.95))
                Line((0, -22.95), (-3.5, -22.95))
                Line((0, -22.95), (0, -19.45))
            make_face()
            # Profile area: 6.125, perimeter: 11.9497474683
            with BuildLine():
                Line((-20, -22.95), (-16.5, -22.95))
                Line((-20, -19.45), (-16.5, -22.95))
                Line((-20, -22.95), (-20, -19.45))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered, curved profile and vertical ribbed or fluted surface detailing on its exterior walls.
def model_21941_1a683ec2_0022():
    """Model: gleitlagerbuchse v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            Circle(2.2)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a dark blue/gray finish, featuring a simple rectangular form with slightly beveled or rounded edges on the corners, commonly used as a structural component, cover plate, or mounting surface in mechanical assemblies.
def model_21979_29f59427_0004():
    """Model: Tooling Plate v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 387.096, perimeter: 86.36
            with BuildLine():
                Line((15.24, -6.35), (15.24, 6.35))
                Line((15.24, 6.35), (-15.24, 6.35))
                Line((-15.24, 6.35), (-15.24, -6.35))
                Line((-15.24, -6.35), (15.24, -6.35))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a rectangular base tray or chassis with an elongated, shallow box shape featuring internal ribbed reinforcement structures and a dark curved or angled section on one end, designed for structural support and component mounting.
def model_22003_c3e3616f_0013():
    """Model: 02 Standard v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 74.6620578056, perimeter: 51.1946891451
            with BuildLine():
                Line((-4, 3), (-4, -3))
                Line((-4, -3), (9, -3))
                Line((9, -3), (9, 3))
                Line((9, 3), (-4, 3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9445436483, 1.9445436483), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9445436483, -1.9445436483), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.9445436483, -1.9445436483), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.9445436483, 1.9445436483), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a flat, trapezoidal base plate or tray with an internal lattice or web-like reinforcement structure featuring diagonal cross-bracing for structural support.
def model_22003_c3e3616f_0014():
    """Model: 01 Base v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 110.7578142648, perimeter: 53.6761053731
            with BuildLine():
                Line((-7, 4), (-7, -4))
                Line((-7, -4), (7, -4))
                Line((7, -4), (7, 4))
                Line((7, 4), (-7, 4))
            make_face()
            with BuildLine():
                CenterArc((-6, 3), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6, -3), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6, -3), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6, 3), 0.26, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.5, 0.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.5, -1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: Two small dark gray cylindrical or oval-shaped fasteners (likely screws or rivets) positioned symmetrically on a white background.
def model_22010_95d37f0e_0007():
    """Model: arm v2"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((6, 0)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-6, 0)):
                Circle(1)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a rectangular base enclosure or chassis with an open top framework, featuring internal cross-bracing and support structures, designed to house components while maintaining structural rigidity.
def model_22011_0832eefe_0006():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 286, perimeter: 70
            with BuildLine():
                Line((0, 13), (0, 0))
                Line((0, 0), (22, 0))
                Line((22, 0), (22, 13))
                Line((22, 13), (0, 13))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-18, -2)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-18, -11)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4, -2)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-3.9903850452, -11.000023112)):
                Circle(0.5)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fastener or mounting component featuring a cylindrical shaft with a hexagonal base flange, designed for secure fastening or alignment in mechanical assemblies.
def model_22011_0832eefe_0013():
    """Model: M10x0.5 Bolt v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5028134169, perimeter: 5.8889727457
            with BuildLine():
                Line((0.4907477288, 0.8999999881), (-0.4907477288, 0.8999999881))
                Line((-0.4907477288, 0.8999999881), (-0.9814954576, 0.0499999881))
                Line((-0.9814954576, 0.0499999881), (-0.4907477288, -0.8000000119))
                Line((-0.4907477288, -0.8000000119), (0.4907477288, -0.8000000119))
                Line((0.4907477288, -0.8000000119), (0.9814954576, 0.0499999881))
                Line((0.9814954576, 0.0499999881), (0.4907477288, 0.8999999881))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a pipe elbow or corner bracket connector featuring a curved cylindrical base transitioning to a rectangular vertical tube, with a 90-degree bent configuration for directional flow or structural support.
def model_22016_c1658896_0000():
    """Model: Locator v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.887819787, perimeter: 29.6574958052
            with BuildLine():
                Line((-1.4037479026, 0), (-1.4037479026, 11.425))
                Line((-1.4037479026, 0), (2, 0))
                Line((2, 11.425), (2, 0))
                Line((-1.4037479026, 11.425), (2, 11.425))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 22.9232948473, perimeter: 25.5357111809
            with BuildLine():
                Line((-1.4037479026, 3.0570400998), (-1.4037479026, 0))
                CenterArc((-0.2905479026, 0), 3.2534148847, 110.0087444149, 295.2388769647)
                Line((2, 0), (2, 2.3104325824))
                Line((-1.4037479026, 0), (2, 0))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


# Description: This is a hollow cylindrical spacer or sleeve with a rounded/domed end cap on one side and an open end on the other, designed for use as a standoff, bushing, or protective covering in mechanical assemblies.
def model_22016_c1658896_0007():
    """Model: Fixed Axle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.077016117, perimeter: 1.1583675661
            with BuildLine():
                Line((-0.2, 0.6999964387), (-0.2, 0.8774964387))
                Line((-0.2, 0.6999964387), (0.2, 0.6999964387))
                Line((0.2, 0.8774964387), (0.2, 0.6999964387))
                CenterArc((0, 0), 0.9, 77.1604115931, 25.6791768138)
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical spacer or washer with an oval/elliptical overall shape, featuring a central rectangular slot or opening and a mesh-textured upper surface, designed for spacing or alignment purposes in an assembly.
def model_22016_c1658896_0011():
    """Model: Spacer v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.9638654063, perimeter: 15.4371940772
            Circle(2.4569057449)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rubber drive belt with an elliptical/oval loop shape, featuring a textured outer surface and uniform width throughout, commonly used in machinery to transmit power between rotating shafts.
def model_22019_0ef07114_0001():
    """Model: Shorter Split Bushing  v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4940397921, perimeter: 25.9338473554
            with BuildLine():
                CenterArc((0, 0), 2.0828, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.0447, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.508, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0006862684, perimeter: 0.1383271316
            with BuildLine():
                CenterArc((0, 0), 2.0447, -90.8038521227, 1.5969450324)
                Line((-0.0286859264, -2.0444987668), (-0.0286859264, -2.0566761568))
                Line((-0.0286859264, -2.0566761568), (0.0283020024, -2.0566761568))
                Line((0.0283020024, -2.0566761568), (0.0283020024, -2.0445041175))
            make_face()
            # Profile area: 0.0093390057, perimeter: 0.4414667901
            with BuildLine():
                Line((0.0283020024, -2.0445041175), (0.0283020024, -1.8807568984))
                Line((0.0283020024, -1.8807568984), (-0.0286859264, -1.8807568984))
                Line((-0.0286859264, -1.8807568984), (-0.0286859264, -2.0444987668))
                CenterArc((0, 0), 2.0447, -90.8038521227, 1.5969450324)
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a plastic connector or coupling component with a cylindrical main body, a curved flange base, and what appears to be an internal bore or slot design for mechanical assembly or fluid/cable routing.
def model_22040_6461a147_0000():
    """Model: Gland v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.6814150222, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 2.2, 18.3165282071, 143.3671142183)
                CenterArc((0, 0), 2.2, 161.6836424254, 36.6327151492)
                CenterArc((0, 0), 2.2, -161.6836424254, 143.3671142183)
                CenterArc((0, 0), 2.2, -18.3165282071, 36.6330564141)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.4729471131, perimeter: 18.3584522195
            with BuildLine():
                CenterArc((0, 3.5), 1.1000000002, 18.3187428425, 143.3648770681)
                Line((-1.0442692402, 3.8456902582), (-2.0885387521, 0.6913796958))
                CenterArc((0, 0), 2.2, 18.3165282071, 143.3671142183)
                Line((2.0885366929, 0.6913859156), (1.0442549837, 3.8457333213))
            make_face()
            with BuildLine():
                CenterArc((0, 3.5), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.4729471137, perimeter: 18.3584522198
            with BuildLine():
                CenterArc((0, 0), 2.2, -161.6836424254, 143.3671142183)
                Line((-1.0442692402, -3.8456902582), (-2.0885387521, -0.6913796958))
                CenterArc((0, -3.5), 1.1000000003, -161.6836199106, 143.3648770681)
                Line((2.0885366929, -0.6913859156), (1.0442549837, -3.8457333213))
            make_face()
            with BuildLine():
                CenterArc((0, -3.5), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8172560583, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polygonal bracket or connector block with an irregular, angular geometry featuring multiple planar faces, internal voids or recesses, and a complex chamfered or faceted surface design typical of a structural support component or mechanical interface part.
def model_22047_5a090f16_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 43.1491824706, perimeter: 36.9644948478
            with BuildLine():
                Line((3.5914850144, 6.5), (0.8631016182, 6.5))
                Line((0.8631016182, 6.5), (-0.9736610818, 1.4535359569))
                Line((-0.9736610818, 1.4535359569), (-2.2864116731, 1.9313380971))
                Line((-2.2864116731, 1.9313380971), (-1.3721290468, 4.4433089677))
                Line((-1.3721290468, 4.4433089677), (-6, 4.4433089677))
                Line((-6, 4.4433089677), (-6, 0.1835359569))
                Line((-6, 0.1835359569), (3.5914850144, 0.1835359569))
                Line((3.5914850144, 0.1835359569), (3.5914850144, 6.5))
            make_face()
        # OneSide extrude, distance=7.5438
        extrude(amount=7.5438)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5438, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 43.1491824706, perimeter: 36.9644948478
            with BuildLine():
                Line((-0.9736610818, 1.4535359569), (-2.2864116731, 1.9313380971))
                Line((-2.2864116731, 1.9313380971), (-1.3721290468, 4.4433089677))
                Line((-1.3721290468, 4.4433089677), (-6, 4.4433089677))
                Line((-6, 4.4433089677), (-6, 0.1835359569))
                Line((-6, 0.1835359569), (3.5914850144, 0.1835359569))
                Line((3.5914850144, 0.1835359569), (3.5914850144, 6.5))
                Line((3.5914850144, 6.5), (0.8631016182, 6.5))
                Line((0.8631016182, 6.5), (0.1145273013, 4.4433089677))
                Line((0.1145273013, 4.4433089677), (-0.9736610818, 1.4535359569))
            make_face()
            # Profile area: 4.0896012336, perimeter: 8.7384898967
            with BuildLine():
                Line((0.1145273013, 4.4433089677), (-0.9736610818, 1.4535359569))
                Line((-1.3721290468, 4.4433089677), (0.1145273013, 4.4433089677))
                Line((-2.2864116731, 1.9313380971), (-1.3721290468, 4.4433089677))
                Line((-0.9736610818, 1.4535359569), (-2.2864116731, 1.9313380971))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a flat, elongated rectangular plate or bar with a slight parallelogram shape, featuring a beveled or chamfered edge along the top rim and a dark blue/gray finish typical of anodized aluminum.
def model_22110_0bc70e9f_0003():
    """Model: Car Floor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.24, perimeter: 16
            with BuildLine():
                Line((-3.2, 0.8), (3.2, 0.8))
                Line((-3.2, -0.8), (-3.2, 0.8))
                Line((3.2, -0.8), (-3.2, -0.8))
                Line((3.2, 0.8), (3.2, -0.8))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.8, -0.4)):
                Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a solid toroidal (donut-shaped) ring with a smooth, curved surface and a central circular hole, featuring a uniform cross-section throughout its circumference.
def model_22124_6f71410e_0001():
    """Model: Collar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6906464039, perimeter: 10.8473303842
            with BuildLine():
                CenterArc((4.0150759295, 1.3866194236), 1.11125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.0150759295, 1.3866194236), 0.61515625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.072965877, perimeter: 0.9575574408
            with Locations((4.0150759295, -0.3175)):
                Circle(0.1524)
        # OneSide extrude, distance=3.048
        extrude(amount=3.048, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a torus (donut-shaped ring) with a smooth, curved surface featuring a continuous circular hole through its center and a textured mesh-like surface pattern.
def model_22124_6f71410e_0004():
    """Model: Washer v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((3.7735595151, -1.0944322659)):
                Circle(2.54)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.47625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.092697016, perimeter: 6.234097922
            with Locations((-3.7735595151, 1.0944322659)):
                Circle(0.9921875)
        # OneSide extrude, distance=-3.048
        extrude(amount=-3.048, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bolt or screw with a hexagonal head (shown in blue) and a long cylindrical shaft (shown in dark gray), featuring a threaded section along the shaft for fastening applications.
def model_22131_6b4b60f8_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3653544672, perimeter: 2.25
            with BuildLine():
                Line((0.1875, 0.3247595264), (0.375, 0))
                Line((-0.1875, 0.3247595264), (0.1875, 0.3247595264))
                Line((-0.375, 0), (-0.1875, 0.3247595264))
                Line((-0.1875, -0.3247595264), (-0.375, 0))
                Line((0.1875, -0.3247595264), (-0.1875, -0.3247595264))
                Line((0.375, 0), (0.1875, -0.3247595264))
            make_face()
        # OneSide extrude, distance=0.313
        extrude(amount=0.313)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a flat, rectangular panel or plate with a parallelogram-like trapezoidal shape, featuring a beveled or angled edge on one side and what appears to be mounting or alignment slots on its upper surface.
def model_22198_327974c6_0008():
    """Model: Floor v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 500, perimeter: 90
            with BuildLine():
                Line((25, -20), (0, -20))
                Line((25, 0), (25, -20))
                Line((0, 0), (25, 0))
                Line((0, -20), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-3.7, 5)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a composite 3D part consisting of two stacked rectangular boxes or housings with a diagonal slot or channel cut through them, featuring angled surfaces and what appears to be a mounting or alignment interface between the two sections.
def model_22201_473a3a65_0004():
    """Model: Moveable Jaw v11 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.2301701848, perimeter: 9.24052
            with BuildLine():
                Line((3.88874, 0), (1.905, 0))
                Line((3.88874, 2.63652), (3.88874, 0))
                Line((1.905, 2.63652), (3.88874, 2.63652))
                Line((1.905, 0), (1.905, 2.63652))
            make_face()
            # Profile area: 14.8703380012, perimeter: 18.11528
            with BuildLine():
                Line((1.905, 0), (1.905, 2.63652))
                Line((1.905, 2.63652), (3.88874, 2.63652))
                Line((3.88874, 5.1689), (3.88874, 2.63652))
                Line((0, 5.1689), (3.88874, 5.1689))
                Line((0, 0), (0, 5.1689))
                Line((1.905, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=2.45872
        extrude(amount=2.45872)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.2301701848, perimeter: 9.24052
            with BuildLine():
                Line((3.88874, 0), (1.905, 0))
                Line((3.88874, 2.63652), (3.88874, 0))
                Line((1.905, 2.63652), (3.88874, 2.63652))
                Line((1.905, 0), (1.905, 2.63652))
            make_face()
        # OneSide extrude, distance=3.2512
        extrude(amount=3.2512, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.0204484752, perimeter: 11.90244
            with BuildLine():
                Line((-3.88874, 3.10642), (0, 3.10642))
                Line((0, 5.1689), (0, 3.10642))
                Line((-3.88874, 5.1689), (0, 5.1689))
                Line((-3.88874, 3.10642), (-3.88874, 5.1689))
            make_face()
        # OneSide extrude, distance=-0.79248
        extrude(amount=-0.79248, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a black polymer housing or enclosure with an asymmetrical design featuring a curved upper dome, a flat base, side flanges, ventilation slots or openings, and an angled front section, likely designed for electronics cooling or cable management.
def model_22202_c9c16395_0008():
    """Model: GROUNDING LINK MOUNTING BLOCK v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3256021084, perimeter: 4.2647698769
            with BuildLine():
                Line((-0.71628, 0.07874), (-0.71628, -0.07874))
                Line((-0.71628, -0.07874), (0.71628, -0.07874))
                Line((0.71628, -0.07874), (0.71628, 0.07874))
                Line((0.71628, 0.07874), (0.3231690876, 0.07874))
                CenterArc((0.3231694614, 0.20574), 0.127, 173.7208071235, 96.2790242103)
                CenterArc((0, 0.2413), 0.19812, -6.2793495059, 192.5586378284)
                CenterArc((-0.3231694614, 0.20574), 0.127, -90, 96.2792883226)
                Line((-0.3231694614, 0.07874), (-0.71628, 0.07874))
            make_face()
            with BuildLine():
                CenterArc((0, 0.2413), 0.1016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.23749
        extrude(amount=0.23749, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.07874, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0324292787, perimeter: 0.6383716272
            with Locations((-0.55118, 0)):
                Circle(0.1016)
            # Profile area: 0.0324292787, perimeter: 0.6383716272
            with Locations((0.5588, 0)):
                Circle(0.1016)
        # OneSide extrude, distance=-0.5334
        extrude(amount=-0.5334, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket or sleeve with a threaded or knurled top end and a smooth cylindrical body, designed to fit over or connect to another component.
def model_22205_f48b96b3_0006():
    """Model: 13-Sleeve Pin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=7.2
        extrude(amount=7.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.254092729, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)
    return part.part


# Description: This is a flashlight or torch featuring a cylindrical dark gray body with a textured grip section and a blue polyhedron-shaped head containing reflective surfaces and lens elements at the top.
def model_22205_f48b96b3_0008():
    """Model: 12-M12 Set Screw v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9953783524, perimeter: 10.3517042531
            with BuildLine():
                Line((-0.95, 0.5484827557), (-0.95, -0.5484827557))
                Line((-0.95, -0.5484827557), (0, -1.0969655115))
                Line((0, -1.0969655115), (0.95, -0.5484827557))
                Line((0.95, -0.5484827557), (0.95, 0.5484827557))
                Line((0.95, 0.5484827557), (0, 1.0969655115))
                Line((0, 1.0969655115), (-0.95, 0.5484827557))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical socket or pipe fitting with a threaded hexagonal head at one end and a smooth cylindrical body, tapering slightly toward the opposite end.
def model_22205_f48b96b3_0012():
    """Model: 14-Jaw Lever and Front Cover Pin v2 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.254092729, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or bolt with a long shaft and a hexagonal head at one end, designed for mechanical assembly applications.
def model_22206_703c82ed_0005():
    """Model: HEX HEAD MACHINE SCREW (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0937206153, perimeter: 1.0852317663
            Circle(0.17272)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0738968695, perimeter: 2.6092317663
            with BuildLine():
                Line((-0.127, 0.2199704526), (0.127, 0.2199704526))
                Line((-0.254, 0), (-0.127, 0.2199704526))
                Line((-0.127, -0.2199704526), (-0.254, 0))
                Line((0.127, -0.2199704526), (-0.127, -0.2199704526))
                Line((0.254, 0), (0.127, -0.2199704526))
                Line((0.127, 0.2199704526), (0.254, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17272, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0937206153, perimeter: 1.0852317663
            Circle(0.17272)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


# Description: This is a curved polymer magazine or clip with a banana-shaped profile, featuring a ribbed rectangular body with internal compartments and a smooth curved feed surface designed to hold and dispense ammunition or similar items.
def model_22216_4b032400_0000():
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
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0436716773, perimeter: 31.183630878
            with BuildLine():
                _nurbs_edge([(3.8943430381, -2.1258322766), (3.8850890567, -2.1153700474), (3.8758350752, -2.1049078183), (3.8665810938, -2.0944455891), (3.4942575923, -1.6735096056), (3.1165381733, -1.3418039967), (2.7221666086, -1.1117689848), (2.4064774827, -0.927629056), (2.0816185892, -0.8141130928), (1.7573486234, -0.7470327003), (1.4054310135, -0.6742329534), (1.0522962314, -0.6474589797), (0.6813803804, -0.6332626501), (0.4605527664, -0.6248107557), (0.2337067831, -0.6220480348), (0, -0.6241293723)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [-0.0081483901, -0.0081483901, -0.0081483901, -0.0081483901, 0, 0, 0, 0.3136208034, 0.3136208034, 0.3136208034, 0.5646700325, 0.5646700325, 0.5646700325, 0.8371240184, 0.8371240184, 0.8371240184, 0.9993316013, 0.9993316013, 0.9993316013, 0.9993316013], 3)
                Line((0, -0.9425716462), (0, -0.6241293723))
                _nurbs_edge([(3.6280664864, -2.3054149461), (3.5826391993, -2.2540564374), (3.4918142767, -2.1538990468), (3.3556658288, -2.0113417014), (3.1743138984, -1.8367355745), (2.9478686693, -1.6448490131), (2.721493555, -1.4799338448), (2.4948193103, -1.3422022802), (2.2672225415, -1.2310995221), (2.0377147587, -1.1446041838), (1.8050129294, -1.079379718), (1.5677484806, -1.0315514367), (1.3246437741, -0.9972151248), (1.0747131066, -0.9729788972), (0.8174919963, -0.9564692385), (0.5528677651, -0.9461727968), (0.335308129, -0.9422307044), (0.1689031291, -0.941530196), (0.0565389607, -0.9420585933), (0, -0.9425716462)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(4.2514918728, -5), (4.2567353505, -4.9513588329), (4.2656233479, -4.8536025043), (4.2741583459, -4.7055459911), (4.2757875805, -4.5052467946), (4.2605178953, -4.2497425474), (4.2265815519, -3.9887047633), (4.1727476993, -3.7217685695), (4.0988813171, -3.4488939404), (4.0062829021, -3.1704663949), (3.89659878, -2.8869739691), (3.7964128852, -2.6564927357), (3.7147390477, -2.4816947507), (3.6574334357, -2.3643160145), (3.6280664864, -2.3054149461)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((4, -5), (4.2514918728, -5))
                Line((4, -5), (4, -10))
                Line((4.6000000685, -10), (4, -10))
                Line((4.6000000685, -9.1000001356), (4.6000000685, -10))
                Line((4.8000000715, -9.1000001356), (4.6000000685, -9.1000001356))
                Line((4.8000000715, -9.6999050071), (4.8000000715, -9.1000001356))
                Line((5, -9.6999050071), (4.8000000715, -9.6999050071))
                Line((5, -4), (5, -9.6999050071))
                Line((4.8000000715, -4), (5, -4))
                Line((4.8000000715, -5.8905461104), (4.8000000715, -4))
                Line((4.6000000685, -5.8905461104), (4.8000000715, -5.8905461104))
                Line((4.6000000685, -5), (4.6000000685, -5.8905461104))
                Line((4.571619793, -5), (4.6000000685, -5))
                _nurbs_edge([(4.5716197916, -4.9999999999), (4.6122423835, -4.5906014959), (4.5915874645, -4.1623858189), (4.4933934888, -3.7160575317), (4.3886355948, -3.2398937843), (4.199967447, -2.7522381895), (3.957287904, -2.2531860691), (3.9427473567, -2.2232845338), (3.9279981692, -2.1933341189), (3.9130399823, -2.1633325963), (3.9068076676, -2.1508324897), (3.9005753529, -2.1383323831), (3.8943430381, -2.1258322766)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.012889549, 0.012889549, 0.012889549, 0.012889549, 0.4761545794, 0.4761545794, 0.4761545794, 0.9703872312, 0.9703872312, 0.9703872312, 1, 1, 1, 1.0127333241, 1.0127333241, 1.0127333241, 1.0127333241], 3)
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


# Description: This is a linear rail or shaft component with an elongated rectangular profile, featuring a central slot running its length, mounting holes at each end, and a slightly raised flange or lip on the right side.
def model_22225_a3ce4d29_0003():
    """Model: Rocker Arm  v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6899183274, perimeter: 23.7055389673
            with BuildLine():
                Line((4.88188, 0), (4.88188, -0.15875))
                Line((4.88188, -0.15875), (5.51688, -0.15875))
                Line((5.51688, -0.15875), (5.51688, 0.47625))
                Line((4.88188, 0.47625), (5.51688, 0.47625))
                Line((4.88188, 0.3175), (4.88188, 0.47625))
                Line((1.4756344084, 0.3175), (4.88188, 0.3175))
                CenterArc((1.4756344084, 0.4445), 0.127, 180, 90)
                Line((1.3486344084, 0.635), (1.3486344084, 0.4445))
                Line((-5.47878, 0.635), (1.3486344084, 0.635))
                Line((-5.47878, 0.3175), (-5.47878, 0.635))
                Line((-2.0305640418, 0.3175), (-5.47878, 0.3175))
                CenterArc((-2.0305640418, 0), 0.3175, 0, 90)
                Line((4.88188, 0), (-1.7130640418, 0))
            make_face()
        # Symmetric extrude, each_side=0.27813
        extrude(amount=0.27813, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.27813, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0401362994, perimeter: 0.7101884353
            with Locations((-5.19938, -0.15875)):
                Circle(0.11303)
        # OneSide extrude, distance=0.381
        extrude(amount=0.381, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or wedge-shaped prism with a tapered end, featuring a rectangular base body with an angled, faceted top surface that transitions to a pointed or chamfered leading edge, resembling an aerodynamic or streamlined geometric form.
def model_22225_a3ce4d29_0011():
    """Model: Intake/Exhaust Valve Block v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.03225, perimeter: 8.255
            with BuildLine():
                Line((1.27, -0.79375), (1.27, 0.79375))
                Line((1.27, 0.79375), (-1.27, 0.79375))
                Line((-1.27, 0.79375), (-1.27, -0.79375))
                Line((-1.27, -0.79375), (1.27, -0.79375))
            make_face()
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True)
    return part.part


# Description: This is a boat hull or elongated pontoon with a tapered wedge shape, featuring a flat bottom, angled sides, and a pointed bow, designed for water displacement and flotation.
def model_22225_a3ce4d29_0013():
    """Model: Crankshaft Support v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.3628405, perimeter: 22.1526907213
            with BuildLine():
                Line((0, 6.35), (0, 0))
                Line((0, 0), (5.3975, 0))
                Line((5.3975, 0), (5.3975, 3.175))
                Line((5.3975, 3.175), (3.56362, 6.35))
                Line((3.56362, 6.35), (0, 6.35))
            make_face()
        # OneSide extrude, distance=0.79502
        extrude(amount=0.79502)
    return part.part


# Description: This is a hex bolt or socket head cap screw featuring a polygonal (hexagonal) head on one end and a long, cylindrical threaded shaft with helical grooves running along its length.
def model_22228_1c82530b_0004():
    """Model: Component23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0023382686, perimeter: 0.18
            with BuildLine():
                Line((0.9849999776, -0.0240192368), (0.9699999776, -0.0499999989))
                Line((0.9699999776, -0.0499999989), (0.9849999776, -0.075980761))
                Line((0.9849999776, -0.075980761), (1.0149999776, -0.075980761))
                Line((1.0149999776, -0.075980761), (1.0299999776, -0.0499999989))
                Line((1.0299999776, -0.0499999989), (1.0149999776, -0.0240192368))
                Line((1.0149999776, -0.0240192368), (0.9849999776, -0.0240192368))
            make_face()
        # OneSide extrude, distance=0.015
        extrude(amount=0.015)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.015), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0007669904, perimeter: 0.0981747704
            with Locations((0.9999999776, -0.0499999989)):
                Circle(0.015625)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a torus or ring-shaped bearing component with an elliptical/oval cross-section, featuring a central slot or opening and a mesh-textured surface, designed for rotational or sliding applications.
def model_22228_1c82530b_0011():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0213836922, perimeter: 0.8050331175
            with BuildLine():
                CenterArc((0, 0), 0.090625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.00625
        extrude(amount=0.00625)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0044485443, perimeter: 0.5694136685
            with BuildLine():
                CenterArc((0, 0), 0.053125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.01875
        extrude(amount=-0.01875, mode=Mode.ADD)
    return part.part


# Description: This is a C-clamp or clamping fixture with a U-shaped frame featuring two cylindrical leg supports, a curved upper jaw mechanism, and mounting holes for fastening applications.
def model_22240_d2a6a35c_0001():
    """Model: Cover v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0761722878, perimeter: 1.8756982446
            with BuildLine():
                CenterArc((1.8923, 0), 0.238125, 32.4282576515, 174.8525728936)
                Line((2.093292635, 0.1276928984), (1.9257257611, 0.4196363542))
                Line((1.9257257611, 0.4196363542), (1.5130946191, 0.1827983324))
                Line((1.5130946191, 0.1827983324), (1.6806614929, -0.1091451234))
            make_face()
            # Profile area: 0.0507524695, perimeter: 1.3557947674
            with BuildLine():
                CenterArc((1.8923, 0), 0.238125, 32.4282576515, 174.8525728936)
                Line((1.6806614929, -0.1091451234), (1.755127516, -0.0664038375))
                CenterArc((1.8923, 0), 0.1524, 33.8779250137, 171.9532381692)
                Line((2.0188266119, 0.0849516126), (2.093292635, 0.1276928984))
            make_face()
            # Profile area: 1.4345765785, perimeter: 6.8292029471
            with BuildLine():
                Line((1.1176, 1.19126), (1.9257257611, 0.4196363542))
                Line((0.175976362, 1.19126), (1.1176, 1.19126))
                Line((0, 1.19126), (0.175976362, 1.19126))
                Line((0, 0), (0, 1.19126))
                CenterArc((0.3048, 0), 0.3048, 180, 180)
                Line((0.6096, 0), (0.6096, 0.78486))
                Line((0.6096, 0.78486), (0.9330502967, 0.78486))
                CenterArc((0.933050281, 0.53594), 0.24892, 41.2344859323, 48.765510453)
                Line((1.5130946191, 0.1827983324), (1.1202426792, 0.7000136799))
                Line((1.9257257611, 0.4196363542), (1.5130946191, 0.1827983324))
            make_face()
            # Profile area: 0.1034786994, perimeter: 1.6863645431
            with BuildLine():
                Line((0, 1.19126), (0.175976362, 1.19126))
                Line((-0.1855177285, 1.8173861314), (0.175976362, 1.19126))
                Line((-0.3175, 1.7411861314), (-0.1855177285, 1.8173861314))
                Line((0, 1.19126), (-0.3175, 1.7411861314))
            make_face()
            # Profile area: 0.0544210017, perimeter: 1.4413877239
            with BuildLine():
                Line((2.0188266119, 0.0849516126), (2.093292635, 0.1276928984))
                CenterArc((1.8923, 0), 0.1524, -154.1688368171, 188.0467618308)
                Line((1.6806614929, -0.1091451234), (1.755127516, -0.0664038375))
                CenterArc((1.8923, 0), 0.238125, -152.7191694549, 185.1474271064)
            make_face()
        # OneSide extrude, distance=2.286
        extrude(amount=2.286)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 0.365782886, perimeter: 2.4206522628
            with BuildLine():
                Line((2.286, 1.8173861314), (1.7018, 1.8173861314))
                Line((1.7018, 1.8173861314), (1.7018, 1.19126))
                Line((1.7018, 1.19126), (2.286, 1.19126))
                Line((2.286, 1.8173861314), (2.286, 1.19126))
            make_face()
            # Profile area: 0.365782886, perimeter: 2.4206522628
            with BuildLine():
                Line((0.5842, 1.19126), (0, 1.19126))
                Line((0.5842, 1.8173861314), (0.5842, 1.19126))
                Line((0, 1.8173861314), (0.5842, 1.8173861314))
                Line((0, 1.19126), (0, 1.8173861314))
            make_face()
            # Profile area: 0.9387904631, perimeter: 5.0670696208
            with BuildLine():
                Line((0.1016, 0), (2.1844, 0))
                Line((0.1016, 0), (0.1016, -0.4507348104))
                Line((2.1844, -0.4507348104), (0.1016, -0.4507348104))
                Line((2.1844, 0), (2.1844, -0.4507348104))
            make_face()
            # Profile area: 2.163737608, perimeter: 6.24332
            with BuildLine():
                Line((2.1844, 1.03886), (2.1844, 0))
                Line((0.1016, 1.03886), (2.1844, 1.03886))
                Line((0.1016, 1.03886), (0.1016, 0))
                Line((0.1016, 0), (2.1844, 0))
            make_face()
        # TwoSides extrude, along=1.143, against=-3.048
        extrude(amount=1.143, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-3.048, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved sheet metal bracket or deflector with a swept, aerodynamic shape featuring a main horizontal flange and a perpendicular vertical section, with internal ribbing or support structure visible on the inner surfaces.
def model_22240_d2a6a35c_0004():
    """Model: Ground strap v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0882427569, perimeter: 6.9990485743
            with BuildLine():
                Line((0.381, 0.9398), (2.6924, 0.9398))
                Line((2.6924, 0.9398), (2.6924, 0.9652))
                Line((0.381, 0.9652), (2.6924, 0.9652))
                CenterArc((0.381, 0.5842), 0.381, 90, 89.9999202928)
                Line((0, 0), (0, 0.58420053))
                Line((0.0254, 0), (0, 0))
                Line((0.0254, 0), (0.0254, 0.58420053))
                CenterArc((0.381, 0.5842), 0.3556, 90, 89.9999145994)
            make_face()
        # OneSide extrude, distance=0.8128
        extrude(amount=0.8128)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9652, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.061311605, perimeter: 0.8777609874
            with Locations((-2.413, 0.4064)):
                Circle(0.1397)
        # OneSide extrude, distance=-0.381
        extrude(amount=-0.381, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter with a dark gray cylindrical body and a blue polygonal geometric head on top, featuring what appears to be a mounting flange or interface surface.
def model_22247_1484e60d_0002():
    """Model: #10 Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=-13
        extrude(amount=-13)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.9519052838, perimeter: 30
            with BuildLine():
                Line((-2.5, 4.3301270189), (-5, 0))
                Line((-5, 0), (-2.5, -4.3301270189))
                Line((-2.5, -4.3301270189), (2.5, -4.3301270189))
                Line((2.5, -4.3301270189), (5, 0))
                Line((5, 0), (2.5, 4.3301270189))
                Line((2.5, 4.3301270189), (-2.5, 4.3301270189))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or rod with a long, slender tapered tubular form, featuring rounded ends and a uniform diameter along its length.
def model_22276_69c5036b_0007():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=15.4
        extrude(amount=15.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=-3.27
        extrude(amount=-3.27, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or collar with a hollow center, featuring multiple evenly-spaced rectangular slots or cutouts distributed around its circumference, designed for structural lightweighting or functional access points.
def model_22276_69c5036b_0008():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 123.6845027718, perimeter: 79.7964534012
            with BuildLine():
                CenterArc((0, 0), 7.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-5.5425625842, 3.2)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 6.4)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((5.5425625842, 3.2)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((5.5425625842, -3.2)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, -6.4)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-5.5425625842, -3.2)):
                Circle(0.6)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered end, featuring a smooth, uniform circular cross-section along its length.
def model_22276_69c5036b_0010():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((0.7, 0)):
                Circle(0.7)
        # OneSide extrude, distance=13.55
        extrude(amount=13.55)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((0, 1.2)):
                Circle(0.35)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved plastic or composite arch/fender component with a ribbed or textured upper surface and flat mounting flanges at both ends, designed to fit over a curved surface or frame structure.
def model_22305_5b45cdb3_0001():
    """Model: 21-DRIVER-PROTECTION-COVER-PLATE v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3024306711, perimeter: 12.1973626684
            with BuildLine():
                Line((2.085665358, 0.7000000104), (2.3713203399, 0.7000000104))
                Line((2.3713203399, 0.7000000104), (2.3713203399, 0.7500000104))
                Line((2.3713203399, 0.7500000104), (2.1213203399, 0.7500000104))
                CenterArc((0, 0), 2.25, 19.4712209162, 141.0575581676)
                Line((-2.1213203399, 0.7500000104), (-2.3713203399, 0.7500000104))
                Line((-2.3713203399, 0.7500000104), (-2.3713203399, 0.7000000104))
                Line((-2.3713203399, 0.7000000104), (-2.085665358, 0.7000000104))
                CenterArc((0, 0), 2.2, 18.5530048216, 142.8939903569)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7500000104, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.2463203399, 0.1000000075)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.2463203399, 0.5000000075)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-2.2463203399, 0.5)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-2.2463203399, 0.1)):
                Circle(0.05)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular bar or beam with a series of parallel slots or grooves machined across its top surface, transitioning from single cuts on the left to multiple closely-spaced parallel slots on the right end.
def model_22305_5b45cdb3_0003():
    """Model: 35-RAILING v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7, perimeter: 27.4
            with BuildLine():
                Line((13.5, -0.2), (0, -0.2))
                Line((13.5, 0), (13.5, -0.2))
                Line((0, 0), (13.5, 0))
                Line((0, -0.2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 24 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-13.2000001907, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-12.8000001907, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-12.4, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-12, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-11.6, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-11.2, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-10.8, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-9, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-6.8, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-4.6, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-2.4, 0.1000000015)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.2, 0.1000000015)):
                Circle(0.05)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with a hexagonal base, featuring a curved top section and a flat mounting surface, designed for rotational or alignment purposes.
def model_22320_e9f9e6ae_0010():
    """Model: Pivot v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0219467106, perimeter: 10.9699111843
            with BuildLine():
                Line((1.2, 0), (1.2, -2.4))
                CenterArc((0, 0), 1.2, 0, 180)
                Line((-1.2, -2.4), (-1.2, 0))
                Line((1.2, -2.4), (-1.2, -2.4))
            make_face()
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)
    return part.part


# Description: This is a cylindrical container or vessel with a curved, slightly tapered body and an open top with a rounded rim flange.
def model_22323_aa6edb8b_0005():
    """Model: Hand Wheel v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True)
    return part.part


# Description: This is a cylindrical housing or manifold body with a horizontal tubular main chamber, featuring a rectangular connector block on the right end, internal ribbed reinforcement, and what appears to be mounting or access features on the underside.
def model_22340_ec24cd79_0011():
    """Model: stud and nut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=6.3
        extrude(amount=6.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2400000966, perimeter: 7.2000001073
            with BuildLine():
                Line((0.9000000134, -0.9000000134), (-0.9000000134, -0.9000000134))
                Line((0.9000000134, 0.9000000134), (0.9000000134, -0.9000000134))
                Line((-0.9000000134, 0.9000000134), (0.9000000134, 0.9000000134))
                Line((-0.9000000134, -0.9000000134), (-0.9000000134, 0.9000000134))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or axle with a hexagonal or polygonal flanged head on one end and a rounded end on the other, featuring small rectangular slots or vents on both ends.
def model_22340_ec24cd79_0020():
    """Model: jaw lever 14 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or rod assembly with a larger hexagonal or octagonal flanged head on the left end and a smaller cylindrical end on the right, featuring what appear to be grooved or textured surfaces on both ends.
def model_22340_ec24cd79_0022():
    """Model: part 13 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=7.2
        extrude(amount=7.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or standoff with a dark gray tubular body and a blue hexagonal or polygonal head at the top, designed for mechanical assembly or mounting applications.
def model_22341_0f9c52ed_0006():
    """Model: 8 v7 (2)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4252324499, perimeter: 5.0170475915
            with BuildLine():
                Line((-0.5000000075, 0.1500000022), (-0.3799038162, -0.3580127072))
                Line((-0.3799038162, -0.3580127072), (0.1200961912, -0.5080127095))
                Line((0.1200961912, -0.5080127095), (0.5000000075, -0.1500000022))
                Line((0.5000000075, -0.1500000022), (0.3799038162, 0.3580127072))
                Line((0.3799038162, 0.3580127072), (-0.1200961912, 0.5080127095))
                Line((-0.1200961912, 0.5080127095), (-0.5000000075, 0.1500000022))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or housing with a rectangular flanged top cap featuring a polygonal geometric design, used for assembly or interface purposes.
def model_22342_274ed8a6_0004():
    """Model: 11 v4 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3783531096, perimeter: 6.5767905842
            with BuildLine():
                Line((-0.6247592011, 0.0129241865), (-0.3235722744, -0.5345952462))
                Line((-0.3235722744, -0.5345952462), (0.3011869267, -0.5475194326))
                Line((0.3011869267, -0.5475194326), (0.6247592011, -0.0129241865))
                Line((0.6247592011, -0.0129241865), (0.3235722744, 0.5345952462))
                Line((0.3235722744, 0.5345952462), (-0.3011869267, 0.5475194326))
                Line((-0.3011869267, 0.5475194326), (-0.6247592011, 0.0129241865))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a dark gray plastic or composite bracket with a curved, angular L-shaped design featuring blue internal cutouts or slots, designed to mount or support components at an offset angle.
def model_22357_e2f7b060_0013():
    """Model: Valve Linkage Dual Rocker v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-1.5589921037, -0.359921687), 0.4, -84.1807557815, 194.3615115629)
                CenterArc((-1.5589921037, -0.359921687), 0.4, 110.1807557815, 165.6384884371)
            make_face()
            with BuildLine():
                CenterArc((-1.5589921037, -0.359921687), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 1.6), 0.4, 172.8192442185, 194.3615115629)
                CenterArc((0, 1.6), 0.4, 7.1807557815, 165.6384884371)
            make_face()
            with BuildLine():
                CenterArc((0, 1.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5790353793, perimeter: 11.0971372886
            with BuildLine():
                Line((0.595294045, 0.075), (0.3968626967, 1.65))
                CenterArc((0, 1.6), 0.4, 172.8192442185, 194.3615115629)
                Line((-0.519235337, 0.6786972792), (-0.3968626967, 1.65))
                CenterArc((-0.9160980337, 0.7286972792), 0.4, -69.8192442185, 62.6384884371)
                Line((-0.7781048484, 0.3532537004), (-1.6969852889, 0.0155218918))
                CenterArc((-1.5589921037, -0.359921687), 0.4, -84.1807557815, 194.3615115629)
                Line((0.0608342682, -0.5969080263), (-1.5184359249, -0.7578603711))
                CenterArc((0, 0), 0.6, 7.1807557815, 268.6384884371)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8482300165, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.6, 7.1807557815, 268.6384884371)
                CenterArc((0, 0), 0.6, -84.1807557815, 91.3615115629)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.55)):
                Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue/gray plastic or composite bracket or mounting plate with an elongated rectangular base, featuring a curved or contoured center section, slot openings on the upper surface, and angled flanges on the sides for structural support and attachment purposes.
def model_22369_481ab478_0002():
    """Model: grounding link mounting v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3560989699, perimeter: 3.6441581501
            with BuildLine():
                Line((0.71628, -0.07874), (0.71628, 0.07874))
                Line((0.71628, 0.07874), (-0.71628, 0.07874))
                Line((-0.71628, 0.07874), (-0.71628, -0.07874))
                Line((-0.71628, -0.07874), (-0.2997198203, -0.07874))
                CenterArc((-0.29972, -0.18034), 0.1016, 0.0001013367, 89.9997973264)
                Line((-0.19812, -0.2413), (-0.19812, -0.1803398203))
                CenterArc((0, -0.2413), 0.19812, -180, 180)
                Line((0.19812, -0.2413), (0.19812, -0.18034))
                CenterArc((0.29972, -0.18034), 0.1016, 90, 90)
                Line((0.29972, -0.07874), (0.71628, -0.07874))
            make_face()
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0410433058, perimeter: 0.7181680806
            with Locations((0, 0.2413)):
                Circle(0.1143)
        # OneSide extrude, distance=-0.8636
        extrude(amount=-0.8636, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular housing or enclosure with a hollow interior, featuring vertical walls, a top opening with internal bracing/ribbing, and what appears to be a central divider or mounting structure inside the cavity.
def model_22369_481ab478_0016():
    """Model: slide valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3174604291, perimeter: 2.5528337563
            with BuildLine():
                Line((0.07874, -0.39878), (0.07874, -0.47498))
                Line((0.07874, -0.47498), (0.23622, -0.47498))
                Line((0.23622, -0.47498), (0.3937, -0.2540000081))
                Line((0.3937, -0.2540000081), (0.3937, 0))
                Line((-0.3937, 0), (0.3937, 0))
                Line((-0.3937, 0), (-0.3937, -0.2540000081))
                Line((-0.23622, -0.47498), (-0.3937, -0.2540000081))
                Line((-0.23622, -0.47498), (-0.07874, -0.47498))
                Line((-0.07874, -0.39878), (-0.07874, -0.47498))
                CenterArc((0, -0.39878), 0.07874, 0, 180)
            make_face()
        # OneSide extrude, distance=0.7874
        extrude(amount=0.7874)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2231995536, perimeter: 1.88976
            with BuildLine():
                Line((-0.23622, -0.15748), (-0.23622, -0.62992))
                Line((0.23622, -0.62992), (-0.23622, -0.62992))
                Line((0.23622, -0.15748), (0.23622, -0.62992))
                Line((0.23622, -0.15748), (-0.23622, -0.15748))
            make_face()
        # OneSide extrude, distance=-0.15748
        extrude(amount=-0.15748, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a barbell or dumbbell bar featuring a long blue cylindrical shaft with dark gray knurled grip sections at each end for handling.
def model_22369_481ab478_0028():
    """Model: grounding link v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0980174948, perimeter: 2.4896493461
            with BuildLine():
                CenterArc((0, 0), 0.23749, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15748
        extrude(amount=0.15748)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.462090909, perimeter: 4.704207217
            with BuildLine():
                CenterArc((0, 0), 0.23749, 152.1745281531, 55.6509436937)
                Line((-2.331407248, 0.1108555466), (-0.2100298738, 0.1108555466))
                CenterArc((-2.54, 0), 0.23622, -27.988181091, 55.976362182)
                Line((-2.331407248, -0.1108555466), (-0.2100298738, -0.1108555466))
            make_face()
            # Profile area: 0.0961274759, perimeter: 2.4816697008
            with BuildLine():
                CenterArc((-2.54, 0), 0.23622, 27.988181091, 304.023637818)
                CenterArc((-2.54, 0), 0.23622, -27.988181091, 55.976362182)
            make_face()
            with BuildLine():
                CenterArc((-2.54, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15748
        extrude(amount=0.15748, mode=Mode.ADD)
    return part.part


# Description: This is a hexahedral polyhedron or wedge-shaped solid with an irregular geometric form characterized by multiple planar faces, angular edges, and a tapered design that appears to transition from a wider rectangular base to a narrower apex.
def model_22391_023436bc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5567860952, perimeter: 8.5818861469
            with BuildLine():
                Line((-2.2909430735, 1.9890437907), (0, 1.9890437907))
                Line((-2.5, 0), (-2.2909430735, 1.9890437907))
                Line((-0.2090569265, 0), (-2.5, 0))
                Line((0, 1.9890437907), (-0.2090569265, 0))
            make_face()
        # OneSide extrude, distance=5.4
        extrude(amount=5.4)
    return part.part


# Description: This is a snap ring (or retaining ring) with a C-shaped circular design featuring two protruding tabs or ears on one end for installation and removal, used to hold components in place on shafts or in grooves.
def model_22395_7f99d894_0001():
    """Model: EXTERNAL RETAINING RING v1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5508969402, perimeter: 13.5195226221
            with BuildLine():
                Line((0.1, -1.3252758551), (0.5, -1.3252758551))
                Line((0.9, -0.632455532), (0.5, -1.3252758551))
                CenterArc((0, 0), 1.1, -35.0968012276, 250.1936024552)
                Line((-0.9, -0.632455532), (-0.5, -1.3252758551))
                Line((-0.5, -1.3252758551), (-0.1, -1.3252758551))
                Line((-0.1, -1.3252758551), (-0.1, -0.894427191))
                CenterArc((0, 0), 0.9, -83.6206297916, 347.2412595831)
                Line((0.1, -1.3252758551), (0.1, -0.894427191))
            make_face()
        # OneSide extrude, distance=0.18
        extrude(amount=0.18)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.3, 1.1012425157)):
                Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.3, 1.1012425157)):
                Circle(0.125)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a microphone shock mount with a cylindrical grip handle and an upper clamp assembly featuring vertical slots and a rounded cap for securing and suspending a microphone.
def model_22395_7f99d894_0002():
    """Model: JOINT B v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.5660177631, perimeter: 18.5699111843
            with BuildLine():
                Line((-4.5, 4.6), (-3.8, 4.6))
                Line((-4.5, 2.2), (-4.5, 4.6))
                Line((-5.5, 2.2), (-4.5, 2.2))
                Line((-5.5, 2.2), (-5.5, 0))
                Line((-5.5, 0), (-2.3, 0))
                Line((-2.3, 0), (-2.3, 4.6))
                Line((-3, 4.6), (-2.3, 4.6))
                CenterArc((-3.4, 4.6), 0.4, -180, 180)
            make_face()
            with BuildLine():
                CenterArc((-3.4, 1.1), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6493361431, perimeter: 6.1123889804
            with BuildLine():
                Line((-4.5, 4.6), (-3.8, 4.6))
                CenterArc((-3.4, 4.6), 0.4, 0, 180)
                Line((-3, 4.6), (-2.3, 4.6))
                CenterArc((-3.4, 4.6), 1.1, 0, 180)
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0.65, 1.1)):
                Circle(0.6)
        # OneSide extrude, distance=5.1
        extrude(amount=5.1, mode=Mode.ADD)
    return part.part


# Description: This is a mounting bracket or suspension arm with an elongated, slightly curved body featuring two circular mounting holes at each end and a central slot or cutout along its length for attachment or alignment purposes.
def model_22404_66db7dd7_0001():
    """Model: Insert1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.361923277, perimeter: 23.9847378871
            with BuildLine():
                CenterArc((-96.8564087068, -19.2829215609), 99.8599682846, 5.448429027, 0.4641021976)
                Line((2.5120845597, -8.9922251339), (2.4723356484, -8.9963375498))
                CenterArc((2.50694161, -8.9425155085), 0.0499749616, -84.0932035146, 90.0343809411)
                CenterArc((-96.8564125645, -19.2828978999), 99.9499232139, 5.9411774265, 0.5907879244)
                CenterArc((2.3950147844, -7.9185313383), 0.05, 6.5319653512, 44.429905027)
                CenterArc((3.3429539699, -6.7495154826), 1.4550537433, 143.2976903309, 87.6641800473)
                CenterArc((2.1362747946, -5.8500088745), 0.05, -36.7023096691, 44.4299050273)
                CenterArc((-96.8564125662, -19.2828979009), 99.9499232157, 7.7275953587, 1.5075781017)
                CenterArc((1.7486254835, -3.250239594), 0.0499749616, 9.23517346, 90.0344084171)
                Line((1.70113492, -3.2073543847), (1.7405755227, -3.2009172368))
                CenterArc((-96.8564087074, -19.2829215595), 99.8599682849, 9.2638471366, 0.8651794898)
                CenterArc((0.7966683886, -1.8306393888), 0.6596694932, 9.5669792254, 180.5620474023)
                CenterArc((-49.221332598, -10.267465059), 50.0649165386, 0.433020774, 9.133958452)
                CenterArc((1.6992002608, -9.8826187656), 0.8570705916, -179.566979226, 185.015408253)
            make_face()
            with BuildLine():
                CenterArc((0.796499983, -1.834553836), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6983767094, -9.8841885091), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2510183362, perimeter: 12.2177123918
            with BuildLine():
                CenterArc((2.1362747946, -5.8500088745), 0.05, -36.7023096691, 44.4299050273)
                CenterArc((-96.8564125661, -19.2828979009), 99.9499232156, 7.7275953587, 1.5075781017)
                CenterArc((1.7486254835, -3.250239594), 0.0499749616, 9.23517346, 38.7277928005)
                CenterArc((6.2633785745, -5.5450306964), 5.0517075721, 152.5090890047, 70.1643050402)
                CenterArc((2.50694161, -8.9425155085), 0.0499749616, -32.2334855381, 38.1746629646)
                CenterArc((-96.8564125645, -19.2828978999), 99.9499232139, 5.9411774265, 0.5907879244)
                CenterArc((2.3950147844, -7.9185313383), 0.05, 6.5319653524, 44.4299050258)
                CenterArc((3.3429539699, -6.7495154826), 1.4550537433, 143.2976903309, 87.6641800473)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a hollow hexagonal or cubic container/box with open sides and internal structural reinforcements, featuring a mesh-like or lattice framework inside and appearing designed as an enclosure or framework structure with geometric face panels.
def model_22430_c6f08b03_0029():
    """Model: FlareNut v2 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1536506163, perimeter: 2.3962848199
            with BuildLine():
                Line((-0.1378481503, -0.23876), (-0.2756963005, 0))
                Line((0.1378481503, -0.23876), (-0.1378481503, -0.23876))
                Line((0.2756963005, 0), (0.1378481503, -0.23876))
                Line((0.1378481503, 0.23876), (0.2756963005, 0))
                Line((-0.1378481503, 0.23876), (0.1378481503, 0.23876))
                Line((-0.2756963005, 0), (-0.1378481503, 0.23876))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.39624
        extrude(amount=0.39624)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0924589137, perimeter: 2.0507688524
            with BuildLine():
                CenterArc((0, 0), 0.20828, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_21557_53eafe15_0024": {"func": model_21557_53eafe15_0024, "volume": 6.4852507237, "area": 28.3796724893},
    "model_21557_53eafe15_0027": {"func": model_21557_53eafe15_0027, "volume": 2.3050283801, "area": 12.9496588633},
    "model_21557_53eafe15_0031": {"func": model_21557_53eafe15_0031, "volume": 10.379676981, "area": 69.7414551036},
    "model_21557_53eafe15_0036": {"func": model_21557_53eafe15_0036, "volume": 3.5578816744, "area": 19.2733682024},
    "model_21557_53eafe15_0052": {"func": model_21557_53eafe15_0052, "volume": 2.6182417037, "area": 14.530586198},
    "model_21636_f65686bc_0006": {"func": model_21636_f65686bc_0006, "volume": 2.4049092516, "area": 11.3363444553},
    "model_21638_0a984848_0001": {"func": model_21638_0a984848_0001, "volume": 813.3821693828, "area": 1021.719466503},
    "model_21638_0a984848_0007": {"func": model_21638_0a984848_0007, "volume": 11.9042433199, "area": 43.1931495541},
    "model_21638_0a984848_0010": {"func": model_21638_0a984848_0010, "volume": 2.7269024233, "area": 12.1893794959},
    "model_21644_aa203dc5_0007": {"func": model_21644_aa203dc5_0007, "volume": 38.7489664843, "area": 128.1418731882},
    "model_21644_aa203dc5_0009": {"func": model_21644_aa203dc5_0009, "volume": 8.291448411, "area": 46.605527016},
    "model_21644_aa203dc5_0016": {"func": model_21644_aa203dc5_0016, "volume": 26.9636075146, "area": 80.9636075146},
    "model_21646_a2dd0d00_0002": {"func": model_21646_a2dd0d00_0002, "volume": 61.0216670115, "area": 269.5463776605},
    "model_21646_a2dd0d00_0005": {"func": model_21646_a2dd0d00_0005, "volume": 58.8431303776, "area": 258.7816190293},
    "model_21646_a2dd0d00_0025": {"func": model_21646_a2dd0d00_0025, "volume": 19.7880023441, "area": 91.3238972863},
    "model_21646_a2dd0d00_0027": {"func": model_21646_a2dd0d00_0027, "volume": 31.8223868506, "area": 161.6543553739},
    "model_21646_a2dd0d00_0041": {"func": model_21646_a2dd0d00_0041, "volume": 18.2441401077, "area": 59.9053801727},
    "model_21646_a2dd0d00_0060": {"func": model_21646_a2dd0d00_0060, "volume": 75.9475863499, "area": 255.7411508871},
    "model_21646_a2dd0d00_0064": {"func": model_21646_a2dd0d00_0064, "volume": 36.6029156033, "area": 165.440050567},
    "model_21646_a2dd0d00_0065": {"func": model_21646_a2dd0d00_0065, "volume": 30.0344521632, "area": 133.2605164268},
    "model_21646_a2dd0d00_0072": {"func": model_21646_a2dd0d00_0072, "volume": 25.2286792677, "area": 122.7715920039},
    "model_21680_360ba5c7_0002": {"func": model_21680_360ba5c7_0002, "volume": 4.403919863, "area": 20.4584190561},
    "model_21680_360ba5c7_0017": {"func": model_21680_360ba5c7_0017, "volume": 2.25376368, "area": 11.4288917786},
    "model_21697_06656699_0001": {"func": model_21697_06656699_0001, "volume": 3.219679101, "area": 13.2116374562},
    "model_21702_3390d14a_0007": {"func": model_21702_3390d14a_0007, "volume": 0.2915128086, "area": 3.1497072578},
    "model_21703_42d28e69_0011": {"func": model_21703_42d28e69_0011, "volume": 4.5247394423, "area": 15.2012243729},
    "model_21707_c15f2c00_0018": {"func": model_21707_c15f2c00_0018, "volume": 554.6477284754, "area": 403.9142626616},
    "model_21732_adaf1650_0007": {"func": model_21732_adaf1650_0007, "volume": 2.9146310904, "area": 23.7144866308},
    "model_21734_7cf58bd0_0011": {"func": model_21734_7cf58bd0_0011, "volume": 13.7145929852, "area": 64.6811500823},
    "model_21736_fc59650e_0011": {"func": model_21736_fc59650e_0011, "volume": 0.9801769079, "area": 13.0690254389},
    "model_21773_01f6bc23_0019": {"func": model_21773_01f6bc23_0019, "volume": 28.5683574146, "area": 227.3634895539},
    "model_21800_040f0143_0000": {"func": model_21800_040f0143_0000, "volume": 148.0731394743, "area": 210.1345574485},
    "model_21803_8a36dcda_0010": {"func": model_21803_8a36dcda_0010, "volume": 12.5763717598, "area": 58.5991148575},
    "model_21803_8a36dcda_0033": {"func": model_21803_8a36dcda_0033, "volume": 0.2110885567, "area": 5.6741252673},
    "model_21822_7d3db422_0006": {"func": model_21822_7d3db422_0006, "volume": 26.059750412, "area": 64.0483820711},
    "model_21822_7d3db422_0011": {"func": model_21822_7d3db422_0011, "volume": 1.0197317588, "area": 9.1741232174},
    "model_21822_7d3db422_0015": {"func": model_21822_7d3db422_0015, "volume": 9.0875688403, "area": 368.0632206506},
    "model_21822_7d3db422_0016": {"func": model_21822_7d3db422_0016, "volume": 119.485, "area": 426.39},
    "model_21822_7d3db422_0017": {"func": model_21822_7d3db422_0017, "volume": 10.5463015326, "area": 48.1528952566},
    "model_21822_7d3db422_0018": {"func": model_21822_7d3db422_0018, "volume": 178.6156369816, "area": 315.7624170183},
    "model_21822_7d3db422_0019": {"func": model_21822_7d3db422_0019, "volume": 4.8840001338, "area": 23.1199999797},
    "model_21822_7d3db422_0021": {"func": model_21822_7d3db422_0021, "volume": 7.9525442967, "area": 60.295423188},
    "model_21822_7d3db422_0034": {"func": model_21822_7d3db422_0034, "volume": 1.39457525, "area": 10.8284956179},
    "model_21847_b2de7eb8_0003": {"func": model_21847_b2de7eb8_0003, "volume": 2.0123467344, "area": 82.0137890837},
    "model_21847_b2de7eb8_0004": {"func": model_21847_b2de7eb8_0004, "volume": 0.5090796327, "area": 6.0107963268},
    "model_21847_b2de7eb8_0005": {"func": model_21847_b2de7eb8_0005, "volume": 1.2000620623, "area": 27.4860389478},
    "model_21847_b2de7eb8_0008": {"func": model_21847_b2de7eb8_0008, "volume": 0.4500331476, "area": 4.162610266},
    "model_21847_b2de7eb8_0011": {"func": model_21847_b2de7eb8_0011, "volume": 1.2251482803, "area": 28.0192277766},
    "model_21847_b2de7eb8_0014": {"func": model_21847_b2de7eb8_0014, "volume": 4.971999968, "area": 104.8400001627},
    "model_21847_b2de7eb8_0015": {"func": model_21847_b2de7eb8_0015, "volume": 2.0046739241, "area": 82.7812149812},
    "model_21852_6cf9a734_0007": {"func": model_21852_6cf9a734_0007, "volume": 8.5066475078, "area": 299.8925077209},
    "model_21852_6cf9a734_0016": {"func": model_21852_6cf9a734_0016, "volume": 1.1546283306, "area": 8.3702742736},
    "model_21859_35124f79_0000": {"func": model_21859_35124f79_0000, "volume": 2023.1856689118, "area": 2058.9369933097},
    "model_21865_c190b734_0000": {"func": model_21865_c190b734_0000, "volume": 8700.3614839197, "area": 5333.3399366294},
    "model_21881_f3bee5e5_0005": {"func": model_21881_f3bee5e5_0005, "volume": 137.7139274292, "area": 215.3037452762},
    "model_21893_0500d043_0026": {"func": model_21893_0500d043_0026, "volume": 0.0142775472, "area": 0.5626790728},
    "model_21893_0500d043_0038": {"func": model_21893_0500d043_0038, "volume": 14.503, "area": 48.7},
    "model_21893_0500d043_0041": {"func": model_21893_0500d043_0041, "volume": 11.9228112966, "area": 66.3967454318},
    "model_21894_93f0d052_0001": {"func": model_21894_93f0d052_0001, "volume": 11.3097335529, "area": 57.4911455607},
    "model_21894_93f0d052_0016": {"func": model_21894_93f0d052_0016, "volume": 1.0210176124, "area": 8.560839981},
    "model_21899_d55d6c08_0011": {"func": model_21899_d55d6c08_0011, "volume": 2.6394053193, "area": 14.9257344211},
    "model_21899_d55d6c08_0012": {"func": model_21899_d55d6c08_0012, "volume": 3.4314578685, "area": 17.7900908338},
    "model_21899_d55d6c08_0024": {"func": model_21899_d55d6c08_0024, "volume": 0.8558666254, "area": 9.3406752815},
    "model_21900_760d2078_0000": {"func": model_21900_760d2078_0000, "volume": 21.954562, "area": 63.661},
    "model_21900_760d2078_0002": {"func": model_21900_760d2078_0002, "volume": 183.8679611912, "area": 661.9992050531},
    "model_21900_760d2078_0003": {"func": model_21900_760d2078_0003, "volume": 0.0713355831, "area": 1.9362868915},
    "model_21900_760d2078_0005": {"func": model_21900_760d2078_0005, "volume": 0.5086091244, "area": 3.9906080682},
    "model_21900_760d2078_0015": {"func": model_21900_760d2078_0015, "volume": 0.5600096406, "area": 6.326},
    "model_21908_385686ec_0011": {"func": model_21908_385686ec_0011, "volume": 0.4382521752, "area": 5.6077428867},
    "model_21908_385686ec_0027": {"func": model_21908_385686ec_0027, "volume": 0.3785619148, "area": 3.754203221},
    "model_21908_385686ec_0028": {"func": model_21908_385686ec_0028, "volume": 0.0956216504, "area": 1.7945621261},
    "model_21918_976c2754_0012": {"func": model_21918_976c2754_0012, "volume": 0.7859790148, "area": 6.921117457},
    "model_21923_41fa6eda_0009": {"func": model_21923_41fa6eda_0009, "volume": 483.648, "area": 551.28},
    "model_21941_1a683ec2_0009": {"func": model_21941_1a683ec2_0009, "volume": 60.9626054429, "area": 158.3676856675},
    "model_21941_1a683ec2_0014": {"func": model_21941_1a683ec2_0014, "volume": 536.1, "area": 1098.9668204745},
    "model_21941_1a683ec2_0022": {"func": model_21941_1a683ec2_0022, "volume": 7.916813487, "area": 84.4460105285},
    "model_21979_29f59427_0004": {"func": model_21979_29f59427_0004, "volume": 491.61192, "area": 883.8692},
    "model_22003_c3e3616f_0013": {"func": model_22003_c3e3616f_0013, "volume": 89.5944693667, "area": 210.7577425852},
    "model_22003_c3e3616f_0014": {"func": model_22003_c3e3616f_0014, "volume": 132.9093771177, "area": 285.9269549772},
    "model_22010_95d37f0e_0007": {"func": model_22010_95d37f0e_0007, "volume": 3.7699111843, "area": 20.106192983},
    "model_22011_0832eefe_0006": {"func": model_22011_0832eefe_0006, "volume": 994.7168146928, "area": 842.1327412287},
    "model_22011_0832eefe_0013": {"func": model_22011_0832eefe_0013, "volume": 4.108163882, "area": 18.5526857167},
    "model_22016_c1658896_0000": {"func": model_22016_c1658896_0000, "volume": 192.3921138103, "area": 275.5308944444},
    "model_22016_c1658896_0007": {"func": model_22016_c1658896_0007, "volume": 12.6233292949, "area": 33.8208361451},
    "model_22016_c1658896_0011": {"func": model_22016_c1658896_0011, "volume": 16.4191753569, "area": 53.9304115674},
    "model_22019_0ef07114_0001": {"func": model_22019_0ef07114_0001, "volume": 0.25062359, "area": 14.1734700767},
    "model_22040_6461a147_0000": {"func": model_22040_6461a147_0000, "volume": 39.3521750031, "area": 129.957218565},
    "model_22047_5a090f16_0000": {"func": model_22047_5a090f16_0000, "volume": 349.1281945742, "area": 388.9299824648},
    "model_22110_0bc70e9f_0003": {"func": model_22110_0bc70e9f_0003, "volume": 3.0971327412, "area": 25.5313274123},
    "model_22124_6f71410e_0001": {"func": model_22124_6f71410e_0001, "volume": 1.6358527289, "area": 12.9344374419},
    "model_22124_6f71410e_0004": {"func": model_22124_6f71410e_0004, "volume": 8.1798805229, "area": 44.9208056176},
    "model_22131_6b4b60f8_0000": {"func": model_22131_6b4b60f8_0000, "volume": 0.5437723941, "area": 4.8702905011},
    "model_22198_327974c6_0008": {"func": model_22198_327974c6_0008, "volume": 1249.2146018366, "area": 1228.1415926536},
    "model_22201_473a3a65_0004": {"func": model_22201_473a3a65_0004, "volume": 47.2102817475, "area": 88.7953966024},
    "model_22202_c9c16395_0008": {"func": model_22202_c9c16395_0008, "volume": 0.1444405639, "area": 2.7482290261},
    "model_22205_f48b96b3_0006": {"func": model_22205_f48b96b3_0006, "volume": 21.3188477473, "area": 55.7946855278},
    "model_22205_f48b96b3_0008": {"func": model_22205_f48b96b3_0008, "volume": 5.9638785177, "area": 23.2527640067},
    "model_22205_f48b96b3_0012": {"func": model_22205_f48b96b3_0012, "volume": 21.9997879549, "area": 57.3968977811},
    "model_22206_703c82ed_0005": {"func": model_22206_703c82ed_0005, "volume": 0.2211126134, "area": 2.7896974844},
    "model_22216_4b032400_0000": {"func": model_22216_4b032400_0000, "volume": 16.9055522321, "area": 88.9304544582},
    "model_22225_a3ce4d29_0003": {"func": model_22225_a3ce4d29_0003, "volume": 2.6241058989, "area": 22.8368615545},
    "model_22225_a3ce4d29_0011": {"func": model_22225_a3ce4d29_0011, "volume": 2.56047875, "area": 13.306425},
    "model_22225_a3ce4d29_0013": {"func": model_22225_a3ce4d29_0013, "volume": 24.9340854543, "area": 80.3375131773},
    "model_22228_1c82530b_0004": {"func": model_22228_1c82530b_0004, "volume": 0.0001884721, "area": 0.0270114913},
    "model_22228_1c82530b_0011": {"func": model_22228_1c82530b_0011, "volume": 0.0002170583, "area": 0.0584753476},
    "model_22240_d2a6a35c_0001": {"func": model_22240_d2a6a35c_0001, "volume": 0.8240818763, "area": 15.3407352937},
    "model_22240_d2a6a35c_0004": {"func": model_22240_d2a6a35c_0004, "volume": 0.070166398, "area": 5.7649841141},
    "model_22247_1484e60d_0002": {"func": model_22247_1484e60d_0002, "volume": 562.4220563215, "area": 464.9480375477},
    "model_22276_69c5036b_0007": {"func": model_22276_69c5036b_0007, "volume": 77.9890951476, "area": 143.652465678},
    "model_22276_69c5036b_0008": {"func": model_22276_69c5036b_0008, "volume": 339.0061216562, "area": 530.8034947505},
    "model_22276_69c5036b_0010": {"func": model_22276_69c5036b_0010, "volume": 20.3371658162, "area": 64.7543282466},
    "model_22305_5b45cdb3_0001": {"func": model_22305_5b45cdb3_0001, "volume": 0.1798876063, "area": 7.9232789433},
    "model_22305_5b45cdb3_0003": {"func": model_22305_5b45cdb3_0003, "volume": 0.2857964474, "area": 12.8018578949},
    "model_22320_e9f9e6ae_0010": {"func": model_22320_e9f9e6ae_0010, "volume": 19.2526721054, "area": 42.3716802635},
    "model_22323_aa6edb8b_0005": {"func": model_22323_aa6edb8b_0005, "volume": 13.8041581199, "area": 31.8557495074},
    "model_22340_ec24cd79_0011": {"func": model_22340_ec24cd79_0011, "volume": 44.6243862603, "area": 80.6927378045},
    "model_22340_ec24cd79_0020": {"func": model_22340_ec24cd79_0020, "volume": 21.9997879549, "area": 57.3968977811},
    "model_22340_ec24cd79_0022": {"func": model_22340_ec24cd79_0022, "volume": 21.3188477473, "area": 55.7946855278},
    "model_22341_0f9c52ed_0006": {"func": model_22341_0f9c52ed_0006, "volume": 0.8484535048, "area": 6.7547589576},
    "model_22342_274ed8a6_0004": {"func": model_22342_274ed8a6_0004, "volume": 1.1949992039, "area": 7.1122651463},
    "model_22357_e2f7b060_0013": {"func": model_22357_e2f7b060_0013, "volume": 1.5728691303, "area": 14.0600030305},
    "model_22369_481ab478_0002": {"func": model_22369_481ab478_0002, "volume": 0.1496451393, "area": 2.7021290413},
    "model_22369_481ab478_0016": {"func": model_22369_481ab478_0016, "volume": 0.2148188762, "area": 2.9426215627},
    "model_22369_481ab478_0028": {"func": model_22369_481ab478_0028, "volume": 0.1033440263, "area": 2.6908345658},
    "model_22391_023436bc_0000": {"func": model_22391_023436bc_0000, "volume": 24.6066449141, "area": 55.4557573838},
    "model_22395_7f99d894_0001": {"func": model_22395_7f99d894_0001, "volume": 0.2614899906, "area": 5.6217017503},
    "model_22395_7f99d894_0002": {"func": model_22395_7f99d894_0002, "volume": 22.9479241901, "area": 74.1042450666},
    "model_22404_66db7dd7_0001": {"func": model_22404_66db7dd7_0001, "volume": 2.3114978286, "area": 32.7876340602},
    "model_22430_c6f08b03_0029": {"func": model_22430_c6f08b03_0029, "volume": 0.0315268151, "area": 1.4366862847},
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
