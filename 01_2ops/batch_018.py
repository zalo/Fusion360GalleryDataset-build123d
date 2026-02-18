"""Batch 018 - passing/01_2ops
52 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical sleeve or band with vertical ribbed texture throughout its surface, featuring an open top and slightly tapered walls, commonly used as a protective cover, guide ring, or connector component.
def model_90205_97363b6d_0005():
    """Model: Pencil Clip v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a shallow, oval-shaped trampoline or mesh-topped platform with a dark rim/frame border and a blue diagonal mesh or lattice surface pattern, designed for elastic support or containment.
def model_90205_97363b6d_0008():
    """Model: Logo v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 2.1010048976
            Ellipse(0.5, 0.1)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a hexagonal or polygonal duct/enclosure component with a curved or tapering top surface, featuring multiple flat side panels and internal geometric complexity, likely designed as an air duct, exhaust manifold, or structural housing element.
def model_90205_97363b6d_0009():
    """Model: Clip Cap v3"""
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
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1023171486, perimeter: 1.3395490776
            with BuildLine():
                Line((0, 0.5), (0, 0))
                Line((0, 0), (0.1, 0))
                _nurbs_edge([(0.1, 0.5), (0.133699474, 0.4452383486), (0.1912629629, 0.3458605096), (0.2481283632, 0.2272027625), (0.273122617, 0.1214207121), (0.2479780199, 0.0473578445), (0.2001894865, 0.0166526299), (0.1538956785, 0.0044055777), (0.1186894748, 0.0007214496), (0.1, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((0.1, 0.5), (0, 0.5))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tubular shape and slightly rounded or chamfered ends, appearing to be a simple mechanical component used for structural support, alignment, or as a pin/dowel in assemblies.
def model_90205_97363b6d_0011():
    """Model: Metal Tip v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0051435726, perimeter: 0.5560618997
            with BuildLine():
                CenterArc((0, 0), 0.0535, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.035, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component with a circular central hole and a smooth, curved outer surface, featuring a mesh-like textured appearance typical of a CAD wireframe or surface model.
def model_90628_b8795213_0007():
    """Model: Magnet (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3030826212, perimeter: 9.2208829941
            with BuildLine():
                CenterArc((0, 0), 0.9835426753, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4840064329, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a mesh or perforated cylindrical band/ring with a curved, slightly tapered drum-like shape featuring ventilation holes or mesh openings distributed across its surface.
def model_90827_941c5cd3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 48 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 62.7446949673, perimeter: 61.5736749188
            with BuildLine():
                EllipticalCenterArc((0.5060800393, -0.6467720687), 4.8426866769, 4.7022927536, 0, 360, -43.8228784534)
            make_face()
            with BuildLine():
                EllipticalCenterArc((-1.826007613, -1.5593281066), 0.7395278325, 0.6270544509, 0, 360, -43.8228784534)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((2.6607262399, -0.6467720687), 0.9186610177, 0.6607262399, 0, 360, -90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-0.634615008, -2.8521158269), 1.2193790227, 0.3283582301, 0, 360, -20.6954507341)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((1.3172409619, -2.0409549043), 0.3430672613, 0.3090372435, 0, 360, -133.8228784534)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-1, 0), 0.3969678148, 0.2653809123, 0, 360, -170.758696412)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((0.2018946934, 1.4064790165), 0.7146110967, 0.6433039621, 0, 360, -43.8228784534)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-1.6333196966, 1.4064790165), 0.3163104799, 0.2999375837, 0, 360, -133.8228784534)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((0.9877068371, -0.5453769534), 0.4978826382, 0.4066484122, 0, 360, -43.8228784534)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((2.0270067691, 1.6141651937), 0.6761967173, 0.5323243554, 0, 360, -90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a mesh or perforated cylindrical container with a curved, bucket-like shape featuring ventilation holes across its surface and reinforced side panels or flanges.
def model_90830_03175f94_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 42 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.0870947629, perimeter: 102.1356210988
            with BuildLine():
                CenterArc((0, 0), 4.9707294914, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, 2), 0.5884724438, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -2), 0.9367181802, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 2), 0.3899621238, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3, -1), 1.2283158553, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3, 0), 0.5782800009, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4774209466, 0), 0.6658637796, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2465991383, -3.5939187923), 0.6458866545, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 3.355208319), 0.2665567296, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7584321357, 1.6311882341), 0.641515121, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 1), 0.4753585778, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, -2), 0.4164713427, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-4, 1), 0.5523618331, 0.4134372201, 0, 360, 27.6110241638)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((3, -2), 0.8745041484, 0.6508104289, 0, 360, 118.6368803574)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((1.9532732856, 3.5900591882), 0.5304677184, 0.3978507888, 0, 360, -90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-1.52129027, 3.5900591882), 0.6597429739, 0.3955470779, 0, 360, 53.5773639459)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-1.0173459375, -0.6536825591), 0.4748160766, 0.4243741747, 0, 360, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((1.8471797419, 0.4602996495), 0.3342615216, 0.2652338592, 0, 360, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((4.2077610888, 0.7255335088), 0.5026932584, 0.3442332419, 0, 360, -142.8756115959)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((0.9453846206, -3.5939187923), 0.9017951213, 0.4060812077, 0, 360, 0)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-3.1657401971, 2.1843197344), 0.3871055388, 0.2917572451, 0, 360, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a long, narrow rectangular bar or rail with a beveled or chamfered edge profile, featuring a slight curved or rounded top surface and appearing to be a guide rail, trim piece, or structural support element.
def model_90838_c2246452_0004():
    """Model: 25x75"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.75, perimeter: 20
            with BuildLine():
                Line((-330, 2.5), (-330, 0))
                Line((-330, 0), (-322.5, 0))
                Line((-322.5, 0), (-322.5, 2.5))
                Line((-322.5, 2.5), (-330, 2.5))
            make_face()
        # OneSide extrude, distance=160
        extrude(amount=160)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a smooth, gradually narrowing profile from a thicker end to a pointed or sharp tip, featuring a uniform dark finish.
def model_90838_c2246452_0005():
    """Model: carrier"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((17.5, 15), (12.5, 15))
                Line((12.5, 0), (12.5, 15))
                Line((12.5, 0), (17.5, 0))
                Line((17.5, 15), (17.5, 0))
            make_face()
        # OneSide extrude, distance=350
        extrude(amount=350)
    return part.part


# Description: This is a tapered cylindrical pin or shaft with a uniform dark finish, featuring a gradually narrowing conical shape from one end to the other, commonly used as a mechanical fastener or alignment component.
def model_90838_c2246452_0006():
    """Model: 50x30"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((393, 161), (393, 156))
                Line((393, 161), (390, 161))
                Line((390, 156), (390, 161))
                Line((393, 156), (390, 156))
            make_face()
        # OneSide extrude, distance=102.5
        extrude(amount=102.5)
    return part.part


# Description: This is a dark navy-colored sailboat or sail-shaped bracket featuring a tall triangular main surface with a smaller rectangular fin or stabilizer element protruding from its lower right corner.
def model_91009_9f8a5c0b_0001():
    """Model: pied1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 69.6383390113, perimeter: 46.5768192732
            with BuildLine():
                Line((-2.5187422484, 2.245110771), (-2.2278325939, 2.8858031756))
                Line((-2.2278325939, 2.8858031756), (-2.9171271529, 3.1987808862))
                Line((-2.9171271529, 3.1987808862), (-4.3693104795, 0.0005273627))
                Line((-4.3693104795, 0.0005273627), (5.9999783297, -0.0101758589))
                Line((6.0319436779, 14.9999659867), (5.9999783297, -0.0101758589))
                Line((-1.6082076501, 1.831677892), (6.0319436779, 14.9999659867))
                Line((-2.5187422484, 2.245110771), (-1.6082076501, 1.831677892))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a 3D triangular rocket or missile nosecone with a pointed apex and a curved, tapered body that transitions from a narrow top to a wider base.
def model_91089_e02eca20_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.4546628675, perimeter: 14.1844610224
            with BuildLine():
                Line((7.5906467905, 2.1301431669), (5.5125809159, 2.7848762507))
                Line((7.3059802324, 3.3257427113), (7.5906467905, 2.1301431669))
                Line((5.8826474415, 4.6921421905), (7.3059802324, 3.3257427113))
                Line((5.5410475717, 5.859275079), (5.8826474415, 4.6921421905))
                Line((4.1460438368, 7.0548746233), (5.5410475717, 5.859275079))
                Line((4.1460438368, 2.6755073979), (4.1460438368, 7.0548746233))
                Line((5.5125809159, 2.7848762507), (4.1460438368, 2.6755073979))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a flat parallelogram plate or panel with a shallow thickness, featuring a simple rectangular geometry with slightly angled edges and a clean, minimalist design suitable for structural or assembly applications.
def model_91185_8f6eaf98_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 62.8205081171, perimeter: 33.3841038226
            with BuildLine():
                Line((25, -17.5), (14.0394681378, -17.5))
                Line((25, -11.7684799509), (25, -17.5))
                Line((14.0394681378, -11.7684799509), (25, -11.7684799509))
                Line((14.0394681378, -17.5), (14.0394681378, -11.7684799509))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a parallelogram-based prism or wedge-shaped plate with a flat top surface, tapered sides, and a trapezoidal profile when viewed from the side, featuring clean edges and a uniform thickness.
def model_91417_853f437b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 117, perimeter: 44
            with BuildLine():
                Line((6.5, -4.5), (6.5, 4.5))
                Line((6.5, 4.5), (-6.5, 4.5))
                Line((-6.5, 4.5), (-6.5, -4.5))
                Line((-6.5, -4.5), (6.5, -4.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular block or prism with a long, narrow rectangular cross-section and parallel faces, featuring subtle edge details and surface indentations that suggest internal structure or reinforcement ribs along its length.
def model_91438_c1e57b51_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21, perimeter: 20
            with BuildLine():
                Line((-1.5, 3.5), (-1.5, -3.5))
                Line((-1.5, -3.5), (1.5, -3.5))
                Line((1.5, -3.5), (1.5, 3.5))
                Line((1.5, 3.5), (-1.5, 3.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical roller or idler pulley with a rounded hemispherical end cap, featuring a smooth curved surface and a flat circular base.
def model_91457_60e370fb_0001():
    """Model: tie rod 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # Symmetric extrude, each_side=3.5
        extrude(amount=3.5, both=True)
    return part.part


# Description: This is a rectangular parallelepiped or wedge-shaped structural component with a slanted profile, featuring flat parallel faces and beveled or angled edges, appearing to serve as a support bracket or reinforcement beam.
def model_91457_9b6cdf83_0002():
    """Model: cotter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8, perimeter: 4.8
            with BuildLine():
                Line((1, -0.2), (1, 0.2))
                Line((1, 0.2), (-1, 0.2))
                Line((-1, 0.2), (-1, -0.2))
                Line((-1, -0.2), (1, -0.2))
            make_face()
        # Symmetric extrude, each_side=2.4
        extrude(amount=2.4, both=True)
    return part.part


# Description: This is a turning tool holder or lathe tool insert with an elongated hexagonal cross-section, featuring a angled cutting head at one end and a tapered shank designed for tool post mounting.
def model_91457_c0320701_0003():
    """Model: key2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.47, perimeter: 18.8
            with BuildLine():
                Line((0, 0.9), (0, 0))
                Line((0, 0), (8.2, 0))
                Line((8.2, 0), (8.2, 1.2))
                Line((8.2, 1.2), (7.9, 1.2))
                Line((7.9, 1.2), (7.9, 0.9))
                Line((7.9, 0.9), (0, 0.9))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is an elongated hexagonal prism or column with a vertical slot or channel running along its length, featuring a tapered or beveled top end.
def model_91544_97fc5e8c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 500, perimeter: 120
            with BuildLine():
                Line((5, -25), (5, 25))
                Line((5, 25), (-5, 25))
                Line((-5, 25), (-5, -25))
                Line((-5, -25), (5, -25))
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)
    return part.part


# Description: This is a rectangular box or base platform with a sloped/angled top surface, featuring a trapezoidal profile when viewed from the side, with the top surface subdivided into multiple triangular facets, suggesting either a faceted design or internal structural ribbing.
def model_91572_e9d75fc1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60, perimeter: 32
            with BuildLine():
                Line((5, -3), (5, 3))
                Line((5, 3), (-5, 3))
                Line((-5, 3), (-5, -3))
                Line((-5, -3), (5, -3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal block with a tilted/angled top face, featuring clean planar surfaces and sharp edges throughout its geometry.
def model_91573_272066be_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 55, perimeter: 32
            with BuildLine():
                Line((2.5, -5.5), (2.5, 5.5))
                Line((2.5, 5.5), (-2.5, 5.5))
                Line((-2.5, 5.5), (-2.5, -5.5))
                Line((-2.5, -5.5), (2.5, -5.5))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is a long, tapered sheet metal channel or trough with a closed rectangular cross-section that narrows toward one end, featuring an internal reinforcing ridge or divider running along its length.
def model_91792_65f165a7_0000():
    """Model: Cap"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5977168189, perimeter: 6.3917931442
            with BuildLine():
                Line((3.5302754609, 10.3969558956), (3.4954131638, 10.7954337748))
                Line((0.5302754609, 10.3969558956), (3.4954131638, 10.7954337748))
                Line((3.5302754609, 10.3969558956), (0.5302754609, 10.3969558956))
            make_face()
        # Symmetric extrude, each_side=5.5
        extrude(amount=5.5, both=True)
    return part.part


# Description: This is a cylindrical component with a domed or hemispherical top end and a flat circular base, featuring a wireframe mesh pattern on the curved upper surface that suggests internal structure or a latticed design.
def model_92044_2d700e71_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.0706795195, perimeter: 24.320929339
            with Locations((3.8189117697, -0.6316451026)):
                Circle(3.8707961249)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a flat washer with a circular disc shape, featuring a large central hole and a slightly beveled or rounded edge, commonly used in fastening applications to distribute load and prevent surface damage.
def model_92286_aaa6cf84_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.6548667765, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: A flat, ring-shaped disc with a large central hole, featuring a uniform thickness and smooth outer and inner circular edges.
def model_92286_c1d7202a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1545353002, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved jaw or clamping component with an organic, tapered shape that widens from a narrow cylindrical neck on the left to a broader, flattened body on the right, featuring angular faceted surfaces and a hollow interior structure typical of a molded or cast part.
def model_92555_89522606_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.2010555133, perimeter: 18.5293275012
            with BuildLine():
                Line((-6, 2.5), (-7.4036018551, 1.5648119942))
                Line((-7.4036018551, 1.5648119942), (-7.4036018551, 0))
                Line((-7.4036018551, 0), (-6.5, -1))
                CenterArc((-1.5517628449, -11.5385415082), 11.64241848, 82.3405231928, 32.8112781395)
                Line((0, 0), (0, 1))
                CenterArc((-0.3350458582, 12.4098165674), 11.4147347682, -119.75447706, 31.4364671842)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular duct or channel component with a symmetrical double-chamber design, featuring two parallel vertical passages separated by an internal divider, angled side walls, and open top and bottom surfaces for airflow or fluid passage.
def model_92821_a5393771_0001():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1902681469, perimeter: 4.9054431915
            with BuildLine():
                Line((0.25, -0.24), (0, -0.24))
                Line((0.265, -0.29), (0.25, -0.24))
                Line((0.455, -0.29), (0.265, -0.29))
                Line((0.47, -0.24), (0.455, -0.29))
                Line((0.82, -0.24), (0.47, -0.24))
                Line((0.835, -0.29), (0.82, -0.24))
                Line((1.025, -0.29), (0.835, -0.29))
                Line((1.04, -0.24), (1.025, -0.29))
                Line((1.29, -0.24), (1.04, -0.24))
                Line((1.29, 0), (1.29, -0.24))
                Line((0.82, 0), (1.29, 0))
                Line((0.82, -0.22), (0.82, 0))
                Line((0.47, -0.22), (0.82, -0.22))
                Line((0.47, 0), (0.47, -0.22))
                Line((0, 0), (0.47, 0))
                Line((0, -0.24), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((0.94, -0.13), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.35, -0.13), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.58
        extrude(amount=0.58)
    return part.part


# Description: This is a conveyor belt or drive belt featuring an elongated oval/elliptical shape with two parallel longitudinal slots or grooves running along its length, designed for power transmission or tensioning applications.
def model_93178_46bda33d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2014697587, perimeter: 8.4279806096
            with BuildLine():
                CenterArc((0.164902479, 1.3431787001), 1.1025, -179.2452465738, 178.4904931475)
                Line((-1.2320968876, 1.3286559622), (-0.937501866, 1.3286559622))
                CenterArc((0.1679031124, 1.3286559622), 1.4, -180, 180)
                Line((1.2673068241, 1.3286559622), (1.5679031124, 1.3286559622))
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                CenterArc((0.1679031124, -1.6713440378), 1.4, 0, 180)
                Line((-0.9345968876, -1.6713440378), (-1.2320968876, -1.6713440378))
                CenterArc((0.1679031124, -1.6713440378), 1.1025, 0, 180)
                Line((1.5679031124, -1.6713440378), (1.2704031124, -1.6713440378))
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                Line((1.5679031124, -1.6713440378), (1.2704031124, -1.6713440378))
                CenterArc((0.1679031124, -1.6713440378), 1.1025, -180, 180)
                Line((-0.9345968876, -1.6713440378), (-1.2320968876, -1.6713440378))
                CenterArc((0.1679031124, -1.6713440378), 1.4, -180, 180)
            make_face()
            # Profile area: 2.242478399, perimeter: 14.7964594301
            with BuildLine():
                CenterArc((0.1679031124, 1.3286559622), 1.4, -180, 180)
                Line((-1.2320968876, -1.6713440378), (-1.2320968876, 1.3286559622))
                CenterArc((0.1679031124, -1.6713440378), 1.4, 0, 180)
                Line((1.5679031124, 1.3286559622), (1.5679031124, -1.6713440378))
            make_face()
            # Profile area: 1.1374263369, perimeter: 8.4860732412
            with BuildLine():
                Line((1.2673068241, 1.3286559622), (1.5679031124, 1.3286559622))
                CenterArc((0.1679031124, 1.3286559622), 1.4, 0, 180)
                Line((-1.2320968876, 1.3286559622), (-0.937501866, 1.3286559622))
                CenterArc((0.164902479, 1.3431787001), 1.1025, -0.7547534262, 181.5095068525)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a hexagonal or multi-faceted geometric solid with a complex polyhedral shape featuring flat faces of varying sizes and orientations, including darker and lighter shaded surfaces with visible edge wireframes, typical of an abstract or crystalline form.
def model_93717_70437f3e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 160.8, perimeter: 50.8
            with BuildLine():
                Line((-6, 6.7), (6, 6.7))
                Line((-6, -6.7), (-6, 6.7))
                Line((6, -6.7), (-6, -6.7))
                Line((6, 6.7), (6, -6.7))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a composite structural bracket or mount featuring a tall vertical rectangular tube with a horizontal flange base and angled support wings, designed to provide rigid support and multi-directional load distribution.
def model_93963_e78f0c67_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3221685665, perimeter: 4.4494308836
            with BuildLine():
                Line((-0.4544687569, 0.2), (-0.3544687569, 0.2))
                Line((-0.3544687569, 0.2), (-0.3544687569, 0))
                Line((0, 0), (-0.3544687569, 0))
                Line((0, 0), (-0.1685069418, 0.1685069418))
                CenterArc((0.021309035, 0.3583229186), 0.2684403288, 151.6451778786, 73.3548221214)
                Line((-0.2149247171, 0.4858134064), (-0.0012652877, 0.8817140697))
                Line((-0.0012652877, 0.8817140697), (0.0501801206, 0.9770399412))
                CenterArc((-0.0244478662, 1.0173151278), 0.0848022822, -28.3548221214, 90)
                Line((-0.0244478662, 1.0173151278), (0.0158273204, 1.0919431146))
                Line((-0.0244478662, 1.0173151278), (-0.0730707189, 1.0867935076))
                CenterArc((-0.0244478662, 1.0173151278), 0.0848022822, 124.9853708696, 26.659807009)
                Line((-0.1344359228, 0.9920698028), (-0.0990758529, 1.0575903143))
                Line((-0.1396568382, 0.9823956972), (-0.1344359228, 0.9920698028))
                Line((-0.3784086857, 0.5399999879), (-0.1396568382, 0.9823956972))
                CenterArc((-0.4162193602, 0.5791851682), 0.0544529656, -90.2020908304, 44.179373314)
                Line((-0.4913115923, 0.5249967265), (-0.4164114236, 0.5247325413))
                CenterArc((-0.4911875525, 0.5601637112), 0.0351672035, -145.0146291304, 54.8125383)
                Line((-0.6307901575, 0.6983107619), (-0.5199999884, 0.5399999879))
                Line((-0.6455959342, 0.669999985), (-0.6307901575, 0.6983107619))
                CenterArc((-0.6058729555, 0.649225933), 0.0448271823, 152.3916400196, 55.2167199608)
                Line((-0.5709998393, 0.4858134064), (-0.6455959342, 0.628451881))
                CenterArc((-0.792533832, 0.3699570725), 0.25, -45, 72.6083599804)
                Line((-0.8089375139, 0), (-0.6157571367, 0.1931803772))
                Line((-0.4544687569, 0), (-0.8089375139, 0))
                Line((-0.4544687569, 0.2), (-0.4544687569, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a blue molded plastic or composite component with a streamlined, boat-like shape featuring a curved upper surface, a hollow underside, and textured grip patterns on the raised end sections.
def model_93963_e78f0c67_0002():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1558622317, perimeter: 2.6535830048
            with BuildLine():
                Line((0, 0.2), (-0.0099999998, 0.2))
                CenterArc((-0.0099999998, -0.0209999946), 0.2209999946, 90, 84.5473792871)
                Line((-0.2299999949, 0), (-0.2199999951, 0))
                Line((-0.2199999951, 0), (-0.1199999973, 0))
                Line((-0.1199999973, 0), (-0.1099999975, 0))
                Line((-0.1099999975, 0), (0, 0))
                Line((0, 0), (0.1, 0))
                Line((0.1, 0), (0.2799999937, 0))
                Line((0.2799999937, 0), (0.2899999935, 0))
                Line((0.2899999935, 0), (0.3353247997, 0))
                Line((0.3353247997, 0), (0.6000000089, 0.0500000007))
                Line((0.6000000089, 0.0500000007), (0.9365325196, 0.0500000007))
                Line((0.9365325196, 0.0500000007), (0.9365325196, 0.2))
                Line((0.9365325196, 0.2), (0.9000000134, 0.2))
                CenterArc((0.9000000134, -0.7004715991), 0.9004715991, 90, 27.2587660473)
                Line((0.4875750828, 0.0999999978), (0.2399999946, 0.0999999978))
                CenterArc((0.2582459405, 0.1738908883), 0.0761103032, -153.2150102088, 49.3443871868)
                Line((0.179999996, 0.1599999964), (0.1903019754, 0.1395922606))
                CenterArc((0.1149999974, 0.1271875053), 0.0728124947, 26.7849897912, 63.2150102088)
                Line((0.1, 0.2), (0.1149999974, 0.2))
                Line((0, 0.2), (0.1, 0.2))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a tapered steel pry bar or wedge tool with a flat, elongated rectangular body that narrows to a sharp point at one end and has a blunt, flat end at the other for leverage applications.
def model_94410_d32e7520_0001():
    """Model: podeprena tyc SBR 20 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.1255068566, perimeter: 16.3144706376
            with BuildLine():
                Line((2.65, 1.77), (2.6447683485, 1.7812193129))
                CenterArc((2.25, 2.7), 1, -66.7484726648, 313.4969453296)
                Line((1.85, 1.77), (1.8552316515, 1.7812193129))
                Line((1.85, 1.77), (1.2577892741, 0.5))
                Line((0, 0.5), (1.2577892741, 0.5))
                Line((0, 0.5), (0, 0))
                Line((0, 0), (4.5, 0))
                Line((4.5, 0), (4.5, 0.5))
                Line((3.2422107259, 0.5), (4.5, 0.5))
                Line((2.65, 1.77), (3.2422107259, 0.5))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)
    return part.part


# Description: This is a complex mechanical bracket or housing component featuring an irregular polygonal body with internal ribbed/reinforcing structures, a large circular hole on one side, and angular flanges designed for structural support and assembly mounting.
def model_94410_d32e7520_0004():
    """Model: trapezova matice v domku TRMD 2004 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.8984073464, perimeter: 24.580241582
            with BuildLine():
                Line((1.45, 0.6), (2.05, 0))
                Line((3.35, 0), (2.05, 0))
                Line((3.95, 0.6), (3.35, 0))
                Line((5.4, 0.6), (3.95, 0.6))
                Line((5.4, 4.1), (5.4, 0.6))
                Line((0, 4.1), (5.4, 4.1))
                Line((0, 0.6), (0, 4.1))
                Line((1.45, 0.6), (0, 0.6))
            make_face()
            with BuildLine():
                CenterArc((2.7, 2), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a bracket or mounting component with a complex angular geometry featuring multiple planar faces, internal cutouts/slots, and a circular hole, designed for structural support or attachment purposes.
def model_94410_d32e7520_0005():
    """Model: kulickove pouzdro SME 20 v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.4829801548, perimeter: 22.3205037062
            with BuildLine():
                Line((4.8, 0), (4.8, 3.9))
                Line((0, 3.9), (4.8, 3.9))
                Line((0, 0), (0, 3.9))
                Line((1.284122187, 0), (0, 0))
                Line((1.9, 0.7339745962), (1.284122187, 0))
                CenterArc((2.4, 1.6), 1, -60, 300)
                Line((2.9, 0.7339745962), (3.515877813, 0))
                Line((4.8, 0), (3.515877813, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a torus-shaped (donut-like) component with a central hole and radial fin or blade-like features extending across its surface, appearing to be a turbine rotor, impeller, or similar rotating machinery part designed for fluid dynamics applications.
def model_95520_dd447a90_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 67.4493617686, perimeter: 49.5446498168
            with BuildLine():
                CenterArc((0, 0), 4.925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.0001644266, 4.4249999969), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.125853184, -3.1320387724), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.8321624117, -2.2125), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5441830163, 4.1468209284), 0.4102759221, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a boat hull or marine vessel component with a curved, tapered parallelogram shape featuring a hollow interior cavity and internal structural ribbing for reinforcement.
def model_96151_49bcd93d_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 662.81, perimeter: 98.913708499
            with BuildLine():
                Line((-10.95, 12.95), (-12.95, 10.95))
                Line((-12.95, -10.95), (-12.95, 10.95))
                Line((-10.95, -12.95), (-12.95, -10.95))
                Line((10.95, -12.95), (-10.95, -12.95))
                Line((12.95, -10.95), (10.95, -12.95))
                Line((12.95, 10.95), (12.95, -10.95))
                Line((10.95, 12.95), (12.95, 10.95))
                Line((-10.95, 12.95), (10.95, 12.95))
            make_face()
        # OneSide extrude, distance=3.3
        extrude(amount=3.3)
    return part.part


# Description: This is a curved shield or guard component with an overall rounded, oval/oblong shape featuring a smooth curved surface, a flat bottom edge, and what appears to be a small mounting hole or slot at the top.
def model_96175_a81ddef6_0001():
    """Model: Component5"""
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
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 71.9862486362, perimeter: 38.4805985753
            with BuildLine():
                CenterArc((-20.3525465902, -7.5658836706), 4.5, 12.653240761, 74.7994410564)
                Line((-20.1525465902, -3.070330312), (-20.1525465902, -6.7658836706))
                Line((-20.1525465902, -6.7658836706), (-20.5525465902, -6.7658836706))
                Line((-20.5525465902, -6.7658836706), (-20.5525465902, -3.070330312))
                CenterArc((-20.3525465902, -7.5658836706), 4.5, 92.5473181826, 74.7994410564)
                _nurbs_edge([(-24.7432579528, -6.5801586937), (-24.7673724868, -6.6642429825), (-24.8142871803, -6.8303031174), (-24.8807161072, -7.0730680222), (-24.9613695244, -7.3840520785), (-25.0487452686, -7.7514870437), (-25.1222795913, -8.0977845713), (-25.1814309509, -8.4236896481), (-25.2255393884, -8.7308445269), (-25.2538638754, -9.0221698688), (-25.2656175394, -9.3021559247), (-25.2598622465, -9.5757252233), (-25.2354149604, -9.8471311988), (-25.1907818273, -10.1189791607), (-25.1240544192, -10.3908538447), (-25.032997663, -10.6593176912), (-24.915337496, -10.9193546547), (-24.7690254293, -11.1654223861), (-24.5925257182, -11.3926118673), (-24.3851790034, -11.5979013649), (-24.1469445946, -11.7797877517), (-23.9318680227, -11.9061583859), (-23.7569416901, -11.990185185), (-23.6342958621, -12.0414440094), (-23.5714658813, -12.0658836706)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-20.3525465902, -12.0658836706), (-23.5714658813, -12.0658836706))
                Line((-20.3525465902, -12.0658836706), (-17.1336272991, -12.0658836706))
                _nurbs_edge([(-15.9618352276, -6.5801586937), (-15.9377206936, -6.6642429825), (-15.890806, -6.8303031174), (-15.8243770732, -7.0730680222), (-15.743723656, -7.3840520785), (-15.6563479118, -7.7514870437), (-15.5828135891, -8.0977845713), (-15.5236622295, -8.4236896481), (-15.4795537919, -8.7308445269), (-15.451229305, -9.0221698688), (-15.4394756409, -9.3021559247), (-15.4452309339, -9.5757252233), (-15.46967822, -9.8471311988), (-15.514311353, -10.1189791607), (-15.5810387612, -10.3908538447), (-15.6720955174, -10.6593176912), (-15.7897556844, -10.9193546547), (-15.9360677511, -11.1654223861), (-16.1125674622, -11.3926118673), (-16.319914177, -11.5979013649), (-16.5581485859, -11.7797877517), (-16.7732251577, -11.9061583859), (-16.9481514903, -11.990185185), (-17.0707973183, -12.0414440094), (-17.1336272991, -12.0658836706)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a curved bracket or clamp component with an organic, C-shaped profile featuring a central cutout and rounded edges, designed for securing or holding cylindrical objects.
def model_96270_e596d25c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.5141891284, perimeter: 15.0708624178
            with BuildLine():
                Line((3.1714816741, -0.9191887679), (3.1557147313, -0.9349557107))
                CenterArc((0, 0), 3.302, -16.163144509, 22.7228789779)
                Line((2.032, 1.6256), (3.2803827775, 0.3772172225))
                Line((0, 1.6256), (2.032, 1.6256))
                CenterArc((0, 0.8128), 0.8128, 90, 180)
                Line((0, 0), (1.3208, 0))
                CenterArc((1.8288, 0), 0.508, -11.9353906282, 191.9353906282)
                Line((3.1557147313, -0.9349557107), (2.3258177663, -0.1050587456))
            make_face()
            with BuildLine():
                CenterArc((0.381, 0.8128), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.143, 0.8128), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.762, 0.3048), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.762, 1.3208), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a curved bracket or connector component with a boomerang-like shape, featuring multiple angled facets and a hollow central opening, designed for structural support or assembly purposes.
def model_96271_dbd85c3b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.2295256959, perimeter: 16.1541441142
            with BuildLine():
                Line((0, 0), (0.5, 0))
                CenterArc((0.3084662568, 0.981486029), 1, -78.9576947563, 51.5339737279)
                CenterArc((2.4387657329, -0.1238755145), 1.4, 75, 77.5762789716)
                Line((4.4, 0.8), (2.801112396, 1.2284206423))
                Line((6, 0.8), (4.4, 0.8))
                Line((6, 0.8), (6.5, 1.3))
                Line((6.5, 1.3), (6.5, 1.7))
                Line((6.5, 1.7), (5.2225229077, 1.7))
                CenterArc((5.2225229077, 3.2), 1.5, -133.9455222888, 43.9455222888)
                CenterArc((3.4875876648, 1.4000000826), 1, 46.0544777112, 43.9630505928)
                Line((1.0000000184, 2.4000000358), (3.4872817382, 2.4000000358))
                Line((0, 1.4), (1.0000000184, 2.4000000358))
                Line((0, 0), (0, 1.4))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a trapezoidal structural bracket or frame component with a tapered box-like shape, featuring internal ribbing/bracing, hollow sections with blue-highlighted openings, and dark structural walls that provide rigidity while minimizing weight.
def model_97331_a482fa9b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 72 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 132.6363596452, perimeter: 96.1182285093
            with BuildLine():
                CenterArc((1, 9), 1, 90, 90)
                Line((0, 9), (0, 1))
                CenterArc((1, 1), 1, 180, 90)
                Line((1, 0), (14, 0))
                CenterArc((14, 1), 1, -90, 90)
                Line((15, 1), (15, 9))
                CenterArc((14, 9), 1, 0, 90)
                Line((14, 10), (1, 10))
            make_face()
            with BuildLine():
                Line((5.5, 7.87), (5.5, 1.63))
                CenterArc((5.37, 1.63), 0.13, -90, 90)
                Line((5.37, 1.5), (5.13, 1.5))
                CenterArc((5.13, 1.63), 0.13, 180, 90)
                Line((5, 1.63), (5, 7.87))
                CenterArc((5.13, 7.87), 0.13, 90, 90)
                Line((5.13, 8), (5.37, 8))
                CenterArc((5.37, 7.87), 0.13, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4, 1.63), (4, 7.87))
                CenterArc((4.13, 7.87), 0.13, 90, 90)
                Line((4.13, 8), (4.37, 8))
                CenterArc((4.37, 7.87), 0.13, 0, 90)
                Line((4.5, 7.87), (4.5, 1.63))
                CenterArc((4.37, 1.63), 0.13, -90, 90)
                Line((4.37, 1.5), (4.13, 1.5))
                CenterArc((4.13, 1.63), 0.13, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.0376301974, 2.2), (2.0376301974, 6.8))
                CenterArc((2.2376301974, 6.8), 0.2, 90, 90)
                Line((2.2376301974, 7), (2.4376301974, 7))
                CenterArc((2.4376301974, 6.8), 0.2, 0, 90)
                Line((2.6376301974, 6.8), (2.6376301974, 2.2))
                CenterArc((2.4376301974, 2.2), 0.2, -90, 90)
                Line((2.4376301974, 2), (2.2376301974, 2))
                CenterArc((2.2376301974, 2.2), 0.2, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.9712403574, 4.9920159017), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a dual-loop connector or link featuring an elongated figure-eight shape with two circular openings aligned vertically, connected by a narrow waisted section in the middle, with textured or patterned surfaces throughout.
def model_97342_27fcca0b_0001():
    """Model: SPINNER v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.8797954478, perimeter: 28.446599802
            with BuildLine():
                CenterArc((0, 0), 1.425, 152.2263450683, 235.5473098633)
                CenterArc((2.3225877415, 1.2231971154), 1.2, 149.3410330077, 58.432621924)
                CenterArc((0, 2.6), 1.5, -30.6589669923, 46.8332979226)
                CenterArc((0, 2.6), 1.5, 16.1743309302, 147.6513381395)
                CenterArc((0, 2.6), 1.5, 163.8256690698, 46.8332979225)
                CenterArc((-2.3225877415, 1.2231971154), 1.2, -27.7736549317, 58.432621924)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2.6), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.038657513, perimeter: 11.6156284444
            with BuildLine():
                CenterArc((0, 2.6), 1.5, 16.1743309302, 147.6513381395)
                CenterArc((0, 4.044968537), 1.769293376, -35.4878035094, 250.9756070189)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a closed bottom, open top, and textured mesh surface covering the curved walls, featuring rounded edges and a slightly tapered or beveled rim.
def model_97733_4ac743c3_0002():
    """Model: Brace"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 3.8003060932, perimeter: 11.9694680102
            with BuildLine():
                CenterArc((8, -2), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8, -2), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=2.145, against=-2.15
        extrude(amount=2.145)
        extrude(sk.sketch, amount=-2.15)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly textured or knurled surface, featuring a tapered or beveled top end and a smooth cylindrical body.
def model_97733_4ac743c3_0003():
    """Model: pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((6, -9)):
                Circle(0.6)
        # OneSide extrude, distance=5.3
        extrude(amount=5.3)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slightly beveled or chamfered edge on one side, featuring a simple geometric form without holes or protrusions.
def model_98198_e5b0d64a_0001():
    """Model: Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2477.4144, perimeter: 203.2
            with BuildLine():
                Line((60.96, -40.64), (0, -40.64))
                Line((60.96, 0), (60.96, -40.64))
                Line((0, 0), (60.96, 0))
                Line((0, -40.64), (0, 0))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: These are two identical tapered hexagonal or prismatic fasteners/pins with a pointed end, featuring a grooved or ridged surface along their length for grip or engagement purposes.
def model_98198_e5b0d64a_0002():
    """Model: Legs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 67.7418, perimeter: 74.93
            with BuildLine():
                Line((-7.3025, 40.64), (-9.2075, 40.64))
                Line((-9.2075, 5.08), (-9.2075, 40.64))
                Line((-7.3025, 5.08), (-9.2075, 5.08))
                Line((-7.3025, 40.64), (-7.3025, 5.08))
            make_face()
            # Profile area: 73.790175, perimeter: 81.28
            with BuildLine():
                Line((-7.3025, 79.375), (-7.3025, 40.64))
                Line((-9.2075, 79.375), (-7.3025, 79.375))
                Line((-9.2075, 40.64), (-9.2075, 79.375))
                Line((-7.3025, 40.64), (-9.2075, 40.64))
            make_face()
            # Profile area: 73.790175, perimeter: 81.28
            with BuildLine():
                Line((-9.525, 79.375), (-9.525, 40.64))
                Line((-11.43, 79.375), (-9.525, 79.375))
                Line((-11.43, 40.64), (-11.43, 79.375))
                Line((-9.525, 40.64), (-11.43, 40.64))
            make_face()
            # Profile area: 67.7418, perimeter: 74.93
            with BuildLine():
                Line((-9.525, 40.64), (-11.43, 40.64))
                Line((-11.43, 5.08), (-11.43, 40.64))
                Line((-9.525, 5.08), (-11.43, 5.08))
                Line((-9.525, 40.64), (-9.525, 5.08))
            make_face()
            # Profile area: 67.7418, perimeter: 74.93
            with BuildLine():
                Line((-51.435, 5.08), (-49.53, 5.08))
                Line((-49.53, 5.08), (-49.53, 40.64))
                Line((-49.53, 40.64), (-51.435, 40.64))
                Line((-51.435, 40.64), (-51.435, 5.08))
            make_face()
            # Profile area: 73.790175, perimeter: 81.28
            with BuildLine():
                Line((-49.53, 40.64), (-51.435, 40.64))
                Line((-49.53, 40.64), (-49.53, 79.375))
                Line((-49.53, 79.375), (-51.435, 79.375))
                Line((-51.435, 79.375), (-51.435, 40.64))
            make_face()
            # Profile area: 67.7418, perimeter: 74.93
            with BuildLine():
                Line((-51.7525, 40.64), (-53.6575, 40.64))
                Line((-53.6575, 40.64), (-53.6575, 5.08))
                Line((-53.6575, 5.08), (-51.7525, 5.08))
                Line((-51.7525, 5.08), (-51.7525, 40.64))
            make_face()
            # Profile area: 73.790175, perimeter: 81.28
            with BuildLine():
                Line((-51.7525, 40.64), (-51.7525, 79.375))
                Line((-51.7525, 79.375), (-53.6575, 79.375))
                Line((-53.6575, 79.375), (-53.6575, 40.64))
                Line((-51.7525, 40.64), (-53.6575, 40.64))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a gasket or seal ring with an elongated oval shape, featuring a hollow center and a textured or ribbed surface pattern on its outer edge.
def model_98492_f154c80b_0000():
    """Model: RINGS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 328.978841141, perimeter: 186.2748459084
            with BuildLine():
                CenterArc((0, 0), 16.589375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 13.0571875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a complex modular assembly composed of multiple interconnected hexagonal and cubic geometric forms with internal mesh structures, featuring angular faces, triangulated surfaces, and various sized cavities or openings throughout its irregular, crystalline-like overall shape.
def model_98701_7cd4ec8d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 33 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 83.4336293856, perimeter: 76.5663706144
            with BuildLine():
                Line((-2, -4), (-2, -6))
                Line((-2, -6), (0, -6))
                Line((0, -6), (0, -4))
                Line((2, -4), (0, -4))
                Line((2, -4), (2, -6))
                Line((2, -6), (4, -6))
                Line((4, -2), (4, -6))
                Line((6, -2), (4, -2))
                Line((6, 0), (6, -2))
                Line((4, 0), (6, 0))
                Line((4, 2), (4, 0))
                Line((6, 2), (4, 2))
                Line((6, 4), (6, 2))
                Line((2, 4), (6, 4))
                Line((2, 4), (2, 6))
                Line((2, 6), (0, 6))
                Line((0, 6), (0, 4))
                Line((-2, 4), (0, 4))
                Line((-2, 4), (-2, 6))
                Line((-2, 6), (-4, 6))
                Line((-4, 2), (-4, 6))
                Line((-6, 2), (-4, 2))
                Line((-6, 0), (-6, 2))
                Line((-4, 0), (-6, 0))
                Line((-4, -2), (-4, 0))
                Line((-6, -2), (-4, -2))
                Line((-6, -4), (-6, -2))
                Line((-2, -4), (-6, -4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a blue polymer or composite boat shoe/footwear featuring an elongated curved sole with a raised heel section, internal mesh or lattice structural ribbing visible through the translucent design, and a distinctive upturned toe box with angular geometric detailing.
def model_98960_e0dee877_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0080335336, perimeter: 0.5638381642
            with BuildLine():
                CenterArc((0, 0), 0.032, 90, 180)
                Line((0, -0.032), (0.08, -0.032))
                Line((0.08, -0.032), (0.124, 0.012))
                CenterArc((-0.0056883157, 0.0030032905), 0.13, 3.9683526325, 20.6187216632)
                Line((0.112524584, 0.0570931265), (0.0915676286, 0.0361361711))
                CenterArc((0.072, 0.032), 0.02, 180, 191.9353906283)
                Line((0, 0.032), (0.052, 0.032))
            make_face()
            with BuildLine():
                CenterArc((0.045, 0), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.015, 0), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.03, -0.02), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.03, 0.02), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a polyhedron-shaped solid body with an irregular geometric form featuring multiple angular faces, prominent faceted surfaces in dark navy and lighter blue tones, and a complex non-uniform structure without obvious holes, slots, or flanges.
def model_99167_f191105a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1083.2930659181, perimeter: 133.9257013426
            with BuildLine():
                Line((30.48, -12.7115193389), (22.8599996567, -43.1799993515))
                Line((30.48, -12.7115193389), (30.48, 0))
                Line((30.48, 0), (0, 0))
                Line((0, 0), (0, -12.6999998093))
                Line((0, -12.6999998093), (7.6606571084, -43.18))
                Line((7.6606571084, -43.18), (22.8599996567, -43.1799993515))
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


# Description: This is a long, slender rectangular beam or channel with a hollow interior cross-section, featuring angled end cuts and running the full length of the part.
def model_99282_f545b74d_0002():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 190), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 237.5, perimeter: 144.3502884254
            with BuildLine():
                Line((-50, 5), (-45, 5))
                Line((0, 50), (-45, 5))
                Line((0, 50), (0, 55))
                Line((-50, 5), (0, 55))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a ring-shaped connector or coupling with an overall oval/elliptical loop form featuring a flat rectangular flange or tab extending from one side and a textured grip surface on the inner circumference.
def model_99732_6f03d7fc_0000():
    """Model: 001.001.002.007"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49.1748913414, perimeter: 73.987495763
            with BuildLine():
                CenterArc((0, 0), 6, -126.8698976458, 253.7397952917)
                Line((-3.6, 4.8), (-10, 0))
                Line((-10, 0), (-3.6, -4.8))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a mounting bracket or clamp assembly with an oval-shaped opening, featuring a curved grip section and three rectangular mounting tabs or slots extending from the right side for fastening.
def model_99732_6f03d7fc_0002():
    """Model: 001.001.002.002"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 64.6982979743, perimeter: 91.1008003303
            with BuildLine():
                Line((4.8733971724, 3.5), (8, 3.5))
                CenterArc((0, 0), 6, 35.6853347127, 54.3146652873)
                Line((-9, 6), (0, 6))
                Line((-9, 6), (-5.5384615385, -2.3076923077))
                CenterArc((0, 0), 6, -157.380135052, 121.6948003393)
                Line((8, -3.5), (4.8733971724, -3.5))
                Line((8, -2.5), (8, -3.5))
                Line((5.5, -2.5), (8, -2.5))
                Line((5.5, -1.5), (5.5, -2.5))
                Line((8, -1.5), (5.5, -1.5))
                Line((8, 1.5), (8, -1.5))
                Line((5.5, 1.5), (8, 1.5))
                Line((5.5, 2.5), (5.5, 1.5))
                Line((8, 2.5), (5.5, 2.5))
                Line((8, 3.5), (8, 2.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


MODELS = {
    "model_90205_97363b6d_0005": {"func": model_90205_97363b6d_0005, "volume": 0.0824668072, "area": 3.6285395149},
    "model_90205_97363b6d_0008": {"func": model_90205_97363b6d_0008, "volume": 0.0078539816, "area": 0.4192095102},
    "model_90205_97363b6d_0009": {"func": model_90205_97363b6d_0009, "volume": 0.035810999, "area": 0.6734764676},
    "model_90205_97363b6d_0011": {"func": model_90205_97363b6d_0011, "volume": 0.0077153589, "area": 0.8443799947},
    "model_90628_b8795213_0007": {"func": model_90628_b8795213_0007, "volume": 1.1515413106, "area": 9.2166067394},
    "model_90827_941c5cd3_0000": {"func": model_90827_941c5cd3_0000, "volume": 188.2340849019, "area": 310.2104445037},
    "model_90830_03175f94_0000": {"func": model_90830_03175f94_0000, "volume": 247.891926433, "area": 569.7844970417},
    "model_90838_c2246452_0004": {"func": model_90838_c2246452_0004, "volume": 3000, "area": 3237.5},
    "model_90838_c2246452_0005": {"func": model_90838_c2246452_0005, "volume": 26250, "area": 14150},
    "model_90838_c2246452_0006": {"func": model_90838_c2246452_0006, "volume": 1537.5, "area": 1670},
    "model_91009_9f8a5c0b_0001": {"func": model_91009_9f8a5c0b_0001, "volume": 20.8915017034, "area": 153.2497238045},
    "model_91089_e02eca20_0000": {"func": model_91089_e02eca20_0000, "volume": 1.6909325735, "area": 19.7462179396},
    "model_91185_8f6eaf98_0000": {"func": model_91185_8f6eaf98_0000, "volume": 31.4102540585, "area": 142.3330681454},
    "model_91417_853f437b_0000": {"func": model_91417_853f437b_0000, "volume": 117, "area": 278},
    "model_91438_c1e57b51_0000": {"func": model_91438_c1e57b51_0000, "volume": 10.5, "area": 52},
    "model_91457_60e370fb_0001": {"func": model_91457_60e370fb_0001, "volume": 49.480084294, "area": 80.1106126665},
    "model_91457_9b6cdf83_0002": {"func": model_91457_9b6cdf83_0002, "volume": 3.84, "area": 24.64},
    "model_91457_c0320701_0003": {"func": model_91457_c0320701_0003, "volume": 10.458, "area": 41.26},
    "model_91544_97fc5e8c_0000": {"func": model_91544_97fc5e8c_0000, "volume": 5000, "area": 2200},
    "model_91572_e9d75fc1_0000": {"func": model_91572_e9d75fc1_0000, "volume": 120, "area": 184},
    "model_91573_272066be_0000": {"func": model_91573_272066be_0000, "volume": 165, "area": 206},
    "model_91792_65f165a7_0000": {"func": model_91792_65f165a7_0000, "volume": 6.5748850074, "area": 71.5051582234},
    "model_92044_2d700e71_0000": {"func": model_92044_2d700e71_0000, "volume": 235.3533975976, "area": 215.746005734},
    "model_92286_aaa6cf84_0000": {"func": model_92286_aaa6cf84_0000, "volume": 0.2827433388, "area": 11.8752202306},
    "model_92286_c1d7202a_0000": {"func": model_92286_c1d7202a_0000, "volume": 0.11545353, "area": 2.9688050576},
    "model_92555_89522606_0000": {"func": model_92555_89522606_0000, "volume": 13.2010555133, "area": 44.9314385278},
    "model_92821_a5393771_0001": {"func": model_92821_a5393771_0001, "volume": 0.1103555252, "area": 3.2256933449},
    "model_93178_46bda33d_0000": {"func": model_93178_46bda33d_0000, "volume": 4.8441894132, "area": 33.8961593032},
    "model_93717_70437f3e_0000": {"func": model_93717_70437f3e_0000, "volume": 2412, "area": 1083.6},
    "model_93963_e78f0c67_0001": {"func": model_93963_e78f0c67_0001, "volume": 0.0322168566, "area": 1.0892802213},
    "model_93963_e78f0c67_0002": {"func": model_93963_e78f0c67_0002, "volume": 0.0155862232, "area": 0.5770827638},
    "model_94410_d32e7520_0001": {"func": model_94410_d32e7520_0001, "volume": 712.5506856555, "area": 1645.6980774714},
    "model_94410_d32e7520_0004": {"func": model_94410_d32e7520_0004, "volume": 84.4920367321, "area": 156.698022603},
    "model_94410_d32e7520_0005": {"func": model_94410_d32e7520_0005, "volume": 72.414900774, "area": 140.5684788406},
    "model_95520_dd447a90_0000": {"func": model_95520_dd447a90_0000, "volume": 20.2348085306, "area": 149.7621184823},
    "model_96151_49bcd93d_0002": {"func": model_96151_49bcd93d_0002, "volume": 2187.273, "area": 1652.0352380466},
    "model_96175_a81ddef6_0001": {"func": model_96175_a81ddef6_0001, "volume": 28.7945032953, "area": 159.3647359862},
    "model_96270_e596d25c_0000": {"func": model_96270_e596d25c_0000, "volume": 1.4006040386, "area": 14.8563773108},
    "model_96271_dbd85c3b_0000": {"func": model_96271_dbd85c3b_0000, "volume": 8.2295256959, "area": 32.6131955059},
    "model_97331_a482fa9b_0000": {"func": model_97331_a482fa9b_0000, "volume": 397.9090789355, "area": 553.6274048181},
    "model_97342_27fcca0b_0001": {"func": model_97342_27fcca0b_0001, "volume": 8.3429170726, "area": 46.4687615035},
    "model_97733_4ac743c3_0002": {"func": model_97733_4ac743c3_0002, "volume": 16.3223146704, "area": 59.0094772902},
    "model_97733_4ac743c3_0003": {"func": model_97733_4ac743c3_0003, "volume": 5.994158783, "area": 22.2424759874},
    "model_98198_e5b0d64a_0001": {"func": model_98198_e5b0d64a_0001, "volume": 4719.474432, "area": 5341.9248},
    "model_98198_e5b0d64a_0002": {"func": model_98198_e5b0d64a_0002, "volume": 2156.947299, "area": 3454.8318},
    "model_98492_f154c80b_0000": {"func": model_98492_f154c80b_0000, "volume": 104.4507820623, "area": 717.0999458579},
    "model_98701_7cd4ec8d_0000": {"func": model_98701_7cd4ec8d_0000, "volume": 166.8672587713, "area": 320},
    "model_98960_e0dee877_0000": {"func": model_98960_e0dee877_0000, "volume": 0.0000803353, "area": 0.0217054489},
    "model_99167_f191105a_0000": {"func": model_99167_f191105a_0000, "volume": 22012.5149990441, "area": 4887.9563831173},
    "model_99282_f545b74d_0002": {"func": model_99282_f545b74d_0002, "volume": 1187.5, "area": 1196.7514421272},
    "model_99732_6f03d7fc_0000": {"func": model_99732_6f03d7fc_0000, "volume": 49.1748913414, "area": 172.3372784458},
    "model_99732_6f03d7fc_0002": {"func": model_99732_6f03d7fc_0002, "volume": 64.6982979743, "area": 220.4973962789},
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
