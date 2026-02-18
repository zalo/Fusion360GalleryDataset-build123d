"""Batch 012 - passing/03_4to5ops
114 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a curved interlocking roof tile with a wavy profile, featuring three rounded peaks and valleys designed for overlap installation, with textured surface details for weather protection and grip.
def model_45285_dc1f2b6f_0004():
    """Model: paddle 1 v1 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.1619046198, perimeter: 23.3034972734
            with BuildLine():
                Line((-2, 12), (-2, 3.4898440169))
                CenterArc((-3, 12), 1, 0, 180)
                Line((-4, 12), (-4, 3.4898440169))
                CenterArc((-3, 3.4898440169), 1, 180, 180)
            make_face()
            # Profile area: 39.6277736948, perimeter: 26.2896338935
            with BuildLine():
                CenterArc((0, 10.5006532619), 2.4996080975, 36.8579184393, 106.2841631213)
                Line((-2, 12), (-2, 3.4898440169))
                CenterArc((-0.003776424, 4.9822911689), 2.4924500129, -143.2169138205, 106.7247744997)
                Line((2, 12), (2, 3.5))
            make_face()
            # Profile area: 20.1415926536, perimeter: 23.2831853072
            with BuildLine():
                CenterArc((3, 12), 1, 0, 180)
                Line((2, 12), (2, 3.5))
                CenterArc((3, 3.5), 1, 180, 180)
                Line((4, 12), (4, 3.5))
            make_face()
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Intersect)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6636751633, perimeter: 7.1420043961
            with BuildLine():
                CenterArc((-3, -0.8512494074), 1.8512494074, 90, 32.6956023474)
                Line((-4, 0.7066736871), (-4, -0.774298472))
                CenterArc((-3, 1.3281658501), 2.3281658501, -115.4372710677, 25.4372710677)
                CenterArc((-3, 1.3281658501), 2.3281658501, -90, 25.4372710677)
                Line((-2, 0.7066736871), (-2, -0.774298472))
                CenterArc((-3, -0.8512494074), 1.8512494074, 57.3043976526, 32.6956023474)
            make_face()
            # Profile area: 3.7115289365, perimeter: 7.1230477609
            with BuildLine():
                CenterArc((3, -1.0553706886), 2.0553706886, 89.9999996347, 29.1127788446)
                Line((2, 0.7403321453), (2, -0.6901523266))
                CenterArc((3, 0.4962824726), 1.5516531612, -130.1262434778, 80.2524869555)
                Line((4, 0.7403321453), (4, -0.6901523266))
                CenterArc((3, -1.0553706886), 2.0553706886, 60.8872215207, 29.1127781139)
            make_face()
            # Profile area: 7.2793310326, perimeter: 11.0108307028
            with BuildLine():
                CenterArc((0.059706848, -6.3721100492), 7.3723518286, 90.4640293732, 15.7593306505)
                Line((-2, 0.7066736871), (-2, -0.774298472))
                CenterArc((-0.1543742295, 6.6061608702), 7.6077272944, -104.0399765612, 12.8772641528)
                Line((-0.308748459, -1), (0, -1))
                CenterArc((-0.1543742295, 6.6061608702), 7.6077272944, -88.8372875916, 15.2875181504)
                Line((2, 0.7403321453), (2, -0.6901523266))
                CenterArc((0.059706848, -6.3721100492), 7.3723518286, 74.7408610181, 14.7951096088)
                Line((0.1194136961, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=17.5
        extrude(amount=17.5, mode=Mode.INTERSECT)
    return part.part


# Description: This is a cylindrical bushing or sleeve with a stepped diameter design, featuring a larger bottom section and a smaller top section with a flange or lip at the transition, and a hollow interior bore running through its length.
def model_45359_1768ab3f_0012():
    """Model: Valve Linkage Rod D4-L46 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.22, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a solid dark body and a blue-tinted perforated top cap, featuring a slightly tapered or rounded upper end.
def model_45359_1768ab3f_0013():
    """Model: Valve Linkage Stud (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical connector or coupler with a threaded end cap on top and vertical ribbed or fluted detailing along its body, designed for secure fastening or joining applications.
def model_45359_1768ab3f_0017():
    """Model: Intel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3521725365, perimeter: 3.7070793312
            with BuildLine():
                CenterArc((0, 0), 0.39, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or connector with a hollow bore, featuring two radial flanges or mounting tabs protruding from opposite sides of the barrel, designed for structural support or assembly mounting.
def model_45359_1768ab3f_0029():
    """Model: Plain Bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8482300165, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered design, featuring a uniform circular cross-section and smooth surfaces along its length.
def model_45359_1768ab3f_0042():
    """Model: Crankshaft Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                Line((0.2236067977, -0.2), (-0.2236067977, -0.2))
                CenterArc((0, 0), 0.3, -138.1896851042, 96.3793702084)
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ring-shaped mechanical component with an overall torus-like form featuring a rectangular slot or opening on one side and textured surface patterns on the inner and outer surfaces, likely designed as a clamp, retaining ring, or engagement interface component.
def model_45359_1768ab3f_0046():
    """Model: Eccentric Strap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2001935622, perimeter: 2.9034599304
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1621, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.167698931, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular boat hull or kayak shell with an elongated, tapered form featuring internal structural ribs and crossbeams, designed for lightweight water vessel construction.
def model_45360_cb4bac3f_0012():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.8453542077, perimeter: 42.5965680241
            with BuildLine():
                Line((-6, 0), (-6, 2))
                Line((-6, 0), (-4.4, 0))
                CenterArc((-3.75, 0), 0.65, 0, 360)
                Line((-6, -2), (-6, 0))
                Line((-5.5, -2.5), (-6, -2))
                Line((5.5, -2.5), (-5.5, -2.5))
                Line((5.5, -2.5), (6, -2))
                Line((6, 2), (6, -2))
                Line((5.5, 2.5), (6, 2))
                Line((5.5, 2.5), (-5.5, 2.5))
                Line((-5.5, 2.5), (-6, 2))
            make_face()
            with BuildLine():
                CenterArc((3.75, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.25, perimeter: 12.9
            with BuildLine():
                Line((0.725, 2.5), (0.725, -2.5))
                Line((-0.725, 2.5), (0.725, 2.5))
                Line((-0.725, -2.5), (-0.725, 2.5))
                Line((0.725, -2.5), (-0.725, -2.5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer or mallet consisting of a cylindrical dark gray handle with a large polygonal (roughly cubic or octagonal) blue-gray head mounted at the top, typical of a striking tool used for driving or impact work.
def model_45360_cb4bac3f_0026():
    """Model: tornillo articulacion (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((-1, 0.5773502692), (-1, -0.5773502692))
                Line((-1, -0.5773502692), (0, -1.1547005384))
                Line((0, -1.1547005384), (1, -0.5773502692))
                Line((1, -0.5773502692), (1, 0.5773502692))
                Line((1, 0.5773502692), (0, 1.1547005384))
                Line((0, 1.1547005384), (-1, 0.5773502692))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a curved cylindrical band or sleeve with a longitudinal slot running along its length, featuring a twisted or helical surface pattern and an open rectangular aperture on one side.
def model_45422_51de0379_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 81.7554450966, perimeter: 52.6382801862
            with BuildLine():
                Line((-11.4451995672, 21.2429825323), (-8.3541867592, 6.8325834064))
                Line((-8.3541867592, 6.8325834064), (0, 0))
                Line((0, 0), (-2.5399999619, 10.1599998474))
                Line((-2.5399999619, 10.1599998474), (-7.6199998856, 13.9699997902))
                Line((-7.6199998856, 13.9699997902), (-7.6199998856, 20.3199996948))
                Line((-7.6199998856, 20.3199996948), (-11.4451995672, 21.2429825323))
            make_face()
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a cylindrical sleeve or collar with a slot cut through its side wall, allowing it to flex or compress radially.
def model_45423_34ff78aa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-25.4
        extrude(amount=-25.4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 99.9997979168, perimeter: 54.1256983339
            with BuildLine():
                Line((-2.5399999619, 10.1599998474), (0, 24.13))
                Line((-5.0799999237, 5.0799999237), (-2.5399999619, 10.1599998474))
                Line((0, 0), (-5.0799999237, 5.0799999237))
                Line((0, 0), (5.0799999237, 5.0799999237))
                Line((5.0799999237, 5.0799999237), (2.5399999619, 10.1599998474))
                Line((2.5399999619, 10.1599998474), (0, 24.13))
            make_face()
        # OneSide extrude, distance=-20.32
        extrude(amount=-20.32)
    return part.part


# Description: This is a cylindrical sleeve or band with a rectangular slot cut through one side, featuring fine linear surface texturing and a hollow tubular form.
def model_45427_4036cb2f_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.8928616646, perimeter: 52.4159114616
            with BuildLine():
                Line((0, 0), (15.7860203006, 18.2498893988))
                _nurbs_edge([(0, 0), (0.4247850763, -0.0885806481), (1.2374134962, -0.2454170384), (2.3455302255, -0.4196965322), (3.6010786679, -0.5299600484), (4.8030810963, -0.4655299432), (5.6481633501, -0.2043160887), (6.159464049, 0.2415654022), (6.3781558276, 0.8504959203), (6.3672234761, 1.5893617913), (6.2195501102, 2.4092635845), (6.0515877144, 3.2489139761), (5.9799735168, 4.0471212982), (6.1013814285, 4.7535640032), (6.4734297636, 5.3389655316), (7.0889862199, 5.8088779727), (7.8743462747, 6.2044363743), (8.7223499249, 6.5840470152), (9.5165002651, 7.0099869415), (10.1591936543, 7.5327341713), (10.596918657, 8.176991781), (10.8505447854, 8.9248030229), (10.9921293462, 9.7293491687), (11.1173484, 10.531239437), (11.3185715233, 11.2744897625), (11.6601877335, 11.9210886882), (12.146458293, 12.4701854296), (12.7321319063, 12.9509354085), (13.3473071136, 13.4065894949), (13.9179399621, 13.8812244612), (14.3869134156, 14.4062050926), (14.7380793587, 14.9845897823), (14.9873062704, 15.5978253949), (15.1673771954, 16.2166302869), (15.3162066874, 16.809547622), (15.4612644384, 17.3543066694), (15.5844524717, 17.7434350861), (15.6828996617, 18.0074568886), (15.7512010674, 18.1711351377), (15.7860203006, 18.2498893988)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a central axial slot, featuring a hollow toroidal (donut-like) shape with a rectangular opening running through its length for alignment or assembly purposes.
def model_45429_70a5f94e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=12.7
        extrude(amount=12.7, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 69.0573383091, perimeter: 69.8104651243
            with BuildLine():
                Line((12.379687499, 10.8758088439), (23.5472622566, 5.2709904398))
                Line((5.5286961126, -2.7747598198), (12.379687499, 10.8758088439))
                Line((0, 0), (5.5286961126, -2.7747598198))
                Line((5.225077251, -6.1300376775), (0, 0))
                Line((10.1599998474, -2.5399999619), (5.225077251, -6.1300376775))
                CenterArc((12.6999998093, 0.9525130514), 4.3184773884, 90, 143.972728575)
                Line((23.5472622566, 5.2709904398), (12.6999998093, 5.2709904398))
            make_face()
        # Symmetric extrude, each_side=12.7
        extrude(amount=12.7, both=True)
    return part.part


# Description: This is a ring or bushing with a rounded, torus-like overall shape featuring a central elongated oval slot or opening that cuts through the body.
def model_45430_2b0c8a5a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 83.5444041987, perimeter: 51.3621923052
            with BuildLine():
                Line((-9.9281273337, 21.9929349484), (-9.9281273337, 10.9964674742))
                CenterArc((1.1258208021, 10.9964674742), 11.0539481358, 180, 84.1544124073)
                Line((0, 0), (-9.9281273337, 21.9929349484))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a toroidal (donut-shaped) bearing or spacer ring with a large central void and internal rectangular slot features, characterized by its curved, smooth outer surface and hollow geometric design.
def model_45434_ab3cf909_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.4775895337, perimeter: 51.545953189
            with BuildLine():
                Line((10.1599998474, 12.6999998093), (18.141223096, 15.9107801374))
                Line((8.7614176911, 7.5828249965), (10.1599998474, 12.6999998093))
                Line((2.5399999619, 5.0799999237), (8.7614176911, 7.5828249965))
                Line((0, 0), (2.5399999619, 5.0799999237))
                Line((3.5977149843, 3.4196345092), (0, 0))
                Line((11.678159723, 6.6703308251), (3.5977149843, 3.4196345092))
                Line((12.6268458508, 10.1414124029), (11.678159723, 6.6703308251))
                Line((18.141223096, 15.9107801374), (12.6268458508, 10.1414124029))
            make_face()
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)
    return part.part


# Description: This is a flat bar or shaft with a circular hole or pin joint at one end, featuring a simple linear body with a slight angular orientation, commonly used as a lever arm, linkage, or mounting bracket in mechanical assemblies.
def model_45468_eaf0dc99_0006():
    """Model: Power v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.25, perimeter: 6
            with BuildLine():
                Line((0, 2.5), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (0.5, 2.5))
                Line((0.5, 2.5), (0, 2.5))
            make_face()
        # OneSide extrude, distance=75
        extrude(amount=75)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 9.3041760125, perimeter: 11.6460502619
            with BuildLine():
                CenterArc((2.5, 1.25), 2, 141.3178125465, 77.364374907)
                Line((0.9387505004, 0), (4.0612494996, 0))
                CenterArc((2.5, 1.25), 2, -38.6821874535, 77.364374907)
                Line((4.0612494996, 2.5), (0.9387505004, 2.5))
            make_face()
            # Profile area: 1.6310973009, perimeter: 6.7051581746
            with BuildLine():
                CenterArc((2.5, 1.25), 2, -141.3178125465, 102.635625093)
                Line((0.9387505004, 0), (4.0612494996, 0))
            make_face()
            # Profile area: 1.6310973009, perimeter: 6.7051581746
            with BuildLine():
                Line((4.0612494996, 2.5), (0.9387505004, 2.5))
                CenterArc((2.5, 1.25), 2, 38.6821874535, 102.635625093)
            make_face()
        # TwoSides extrude, along=0.5, against=-1
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical pulley or wheel with a rounded cube-like body, featuring a central axial hole and a recessed groove or flange around its circumference for belt or cable engagement.
def model_45551_7a11fc5b_0003():
    """Model: Tyre"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 71.9948316448, perimeter: 38.7979326579
            with BuildLine():
                Line((0, 0), (4.8296291314, 1.2940952255))
                Line((0, 0), (3.5355339059, 3.5355339059))
                CenterArc((0, 0), 5, 45, 330)
            make_face()
            # Profile area: 6.544984695, perimeter: 12.617993878
            with BuildLine():
                CenterArc((0, 0), 5, 15, 30)
                Line((0, 0), (3.5355339059, 3.5355339059))
                Line((0, 0), (4.8296291314, 1.2940952255))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch6 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-42
        extrude(amount=-42, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-chamber rectangular bracket or frame connector with two parallel open-sided box sections joined together, featuring reinforced corners and flanged edges for structural support and fastening.
def model_45593_25a4e479_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.75, perimeter: 12
            with BuildLine():
                Line((-1.5, 2.5), (-1.5, -3))
                Line((-1.5, -3), (-1, -3))
                Line((-1, -3), (-1, 2.5))
                Line((-1, 2.5), (-1.5, 2.5))
            make_face()
            # Profile area: 2.75, perimeter: 12
            with BuildLine():
                Line((1, 2.5), (1.5, 2.5))
                Line((1, -3), (1, 2.5))
                Line((1.5, -3), (1, -3))
                Line((1.5, 2.5), (1.5, -3))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.3873228961, perimeter: 11.4420352248
            with BuildLine():
                Line((0.7, -2), (-2.5, -2))
                CenterArc((0.7, -0.7), 1.3, -90, 90)
                Line((2, -0.5), (2, -0.7))
                Line((-2.5, -0.5), (2, -0.5))
                Line((-2.5, -2), (-2.5, -0.5))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an angle iron or L-shaped structural steel channel with a long, uniform cross-section featuring two perpendicular flanges (one dark top surface and one lighter blue side surface) that meet at a right angle.
def model_45797_78875e5a_0003():
    """Model: base support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.6118859375, perimeter: 20.32
            with BuildLine():
                Line((25.3711593553, 13.623545184), (25.3711593553, 18.227295184))
                Line((20.7674093553, 13.623545184), (25.3711593553, 13.623545184))
                Line((20.7674093553, 13.147295184), (20.7674093553, 13.623545184))
                Line((25.8474093553, 13.147295184), (20.7674093553, 13.147295184))
                Line((25.8474093553, 18.227295184), (25.8474093553, 13.147295184))
                Line((25.3711593553, 18.227295184), (25.8474093553, 18.227295184))
            make_face()
        # OneSide extrude, distance=49.53
        extrude(amount=49.53)
    return part.part


# Description: This is a rounded, bulbous connector or coupling with a large spherical main body and a smaller cylindrical or tapered neck extension, featuring a mesh-textured surface on one side that suggests internal geometric complexity or reinforcement.
def model_45798_b573e9da_0001():
    """Model: arm pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2.0000000298, 3.0000000447)):
                Circle(0.4)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433622, perimeter: 5.6548668233
            with BuildLine():
                CenterArc((2.0000000298, 3.0000000447), 0.5000000075, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.0000000298, 3.0000000447), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2.0000000298, 3.0000000447)):
                Circle(0.4)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a connecting link or clevis pin with an elongated cylindrical body and rounded ends, featuring two small holes at each end for securing pins or fasteners.
def model_45798_b573e9da_0003():
    """Model: Piston arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.2690268613, perimeter: 17.7699115162
            with BuildLine():
                CenterArc((-6.0000000894, 1.5000000224), 0.6000000089, -0.0000021344, 180.0000021344)
                Line((-5.4000000805, 8.5000001267), (-5.4000000805, 1.5))
                CenterArc((-6.0000000894, 8.5000001267), 0.6000000089, 180, 180)
                Line((-6.6000000983, 8.5000001267), (-6.6000000983, 1.5))
            make_face()
            # Profile area: 1.130973389, perimeter: 3.7699112405
            with BuildLine():
                CenterArc((-6.0000000894, 8.5000001267), 0.6000000089, 180, 180)
                CenterArc((-6.0000000894, 8.5000001267), 0.6000000089, 0, 180)
            make_face()
            # Profile area: 1.130973389, perimeter: 3.7699112181
            with BuildLine():
                CenterArc((-6.0000000894, 1.5000000224), 0.6000000089, -179.9999978656, 179.9999957311)
                CenterArc((-6.0000000894, 1.5000000224), 0.6000000089, -0.0000021344, 180.0000021344)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.515299735, perimeter: 2.5446900494
            with Locations((-6.0000000894, 8.5000001267)):
                Circle(0.405)
            # Profile area: 0.515299735, perimeter: 2.5446900494
            with Locations((-6.0000000894, 1.5000000224)):
                Circle(0.405)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling component with two perpendicular barrel sections featuring opposing rectangular windows or apertures, dark ribbed/textured outer surfaces, and blue interior walls, designed to join or align two components at a 90-degree angle.
def model_45912_c3b84cd3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.4304996605, perimeter: 89.5366609421
            with BuildLine():
                Line((0.3995970315, -0.9871431274), (5.5, -3))
                CenterArc((6.40625, 0), 3.1338935946, -106.8086916262, 213.6173832524)
                Line((0.5206815891, 0.9780708099), (5.5, 3))
                CenterArc((-0.0516043326, 3.2508748656), 2.343746883, -103.4264330292, 27.5595555559)
                Line((-7, 2.5), (-0.5958145366, 0.9711852584))
                CenterArc((-7, 0), 2.5, 90, 180)
                Line((-7, -2.5), (-0.4400589102, -0.9843859532))
                CenterArc((-0.0229402772, -1.8108526326), 0.9257619166, 62.8435898281, 53.9365379434)
            make_face()
            with BuildLine():
                Line((-7.0341985396, 2.1997341794), (-0.6654735354, 0.6793846006))
                CenterArc((-0.0516043326, 3.2508748656), 2.643746883, -103.4264330292, 28.0258932105)
                Line((0.6147791435, 0.692490484), (5.5997004565, 2.716694819))
                CenterArc((6.40625, 0), 2.8338935946, -106.5645896332, 213.100023856)
                Line((0.5224602789, -0.7131138159), (5.5983181494, -2.7162840482))
                CenterArc((-0.0229402772, -1.8108526326), 1.2257619166, 63.5799754597, 51.3898450699)
                Line((-7.0331260805, -2.199750591), (-0.5403844209, -0.6996623545))
                CenterArc((-7, 0), 2.2, 90.8906867749, 178.2465603485)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.7473329834, perimeter: 38.7867895588
            with BuildLine():
                CenterArc((-0.0516043326, 3.2508748656), 2.343746883, -103.4264330292, 27.5595555559)
                Line((5.5, 3), (0.5206815891, 0.9780708099))
                Line((7.8470961399, 3.9530746591), (5.5, 3))
                CenterArc((7.7906615983, 4.0920535874), 0.15, -67.8996280899, 180)
                Line((7.7342270567, 4.2310325157), (0.4278353766, 1.2641592626))
                CenterArc((-0.0516043326, 3.2508748656), 2.043746883, -103.4264330292, 26.9938061158)
                Line((-0.5261555379, 1.2629859162), (-7.8787087567, 3.018196132))
                CenterArc((-8.7816100647, -0.7640459371), 3.8885197494, 76.5735669708, 20.1218485706)
                Line((-9.2349775179, 3.0979540362), (-10.3357716307, 2.9687297413))
                CenterArc((-10.3182829403, 2.8197527441), 0.15, 96.6954155414, 180)
                Line((-9.2000001371, 2.8000000417), (-10.3007942499, 2.6707757468))
                CenterArc((-8.7816100647, -0.7640459371), 3.5885197494, 76.5735669708, 20.1218485706)
                Line((-7, 2.5), (-7.9483677554, 2.7263954742))
                Line((-0.5958145366, 0.9711852584), (-7, 2.5))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical roller or shaft with a textured dark gray body and blue hexagonal end caps on both ends, featuring a smooth cylindrical profile suitable for rotational or mechanical applications.
def model_45922_26941172_0001():
    """Model: screw fixing the wheels 12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((55, 60)):
                Circle(0.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4616784181, perimeter: 7.2985145918
            with BuildLine():
                Line((55.1793165279, 59.3307873411), (55.6692134271, 59.820686339))
                Line((55.6692134271, 59.820686339), (55.4898968992, 60.4898989979))
                Line((55.4898968992, 60.4898989979), (54.8206834721, 60.6692126589))
                Line((54.8206834721, 60.6692126589), (54.3307865729, 60.179313661))
                Line((54.3307865729, 60.179313661), (54.5101031008, 59.5101010021))
                Line((54.5101031008, 59.5101010021), (55.1793165279, 59.3307873411))
            make_face()
            with BuildLine():
                CenterArc((55, 60), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((55, 60)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or adapter with a cubic mounting base, featuring a hollow cylindrical tube extending from a solid rectangular block with a slotted opening on top for component insertion or alignment.
def model_45922_26941172_0004():
    """Model: screw on the handle 16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((62.5, 27.5)):
                Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4316268703, perimeter: 8.6841552378
            with BuildLine():
                Line((62.5155391861, 26.576370276), (63.3076563977, 27.0516424679))
                Line((63.3076563977, 27.0516424679), (63.2921172116, 27.9752721919))
                Line((63.2921172116, 27.9752721919), (62.4844608139, 28.423629724))
                Line((62.4844608139, 28.423629724), (61.6923436023, 27.9483575321))
                Line((61.6923436023, 27.9483575321), (61.7078827884, 27.0247278081))
                Line((61.7078827884, 27.0247278081), (62.5155391861, 26.576370276))
            make_face()
            with BuildLine():
                CenterArc((62.5, 27.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((62.5, 27.5)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or coupling with a smooth, hollow tubular body featuring internal ribbed or threaded surface patterns visible on the interior walls.
def model_45922_26941172_0005():
    """Model: rubber grips 10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4790928797, perimeter: 19.1637151869
            with BuildLine():
                CenterArc((56, 60), 1.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((56, 60), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-56, 60)):
                Circle(1.5)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a long, slender hexagonal or chamfered prism with a tapered wedge-like profile, featuring a gradually narrowing cross-section from one end to the other, commonly used as a shim, wedge, or structural support element.
def model_46016_d699e580_0002():
    """Model: Neck"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96, perimeter: 56
            with BuildLine():
                Line((-2, -12), (-2, 12))
                Line((2, -12), (-2, -12))
                Line((2, 12), (2, -12))
                Line((-2, 12), (2, 12))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a shoe sole or footwear component featuring an elongated, curved anatomical shape with a textured upper surface, a blue accent stripe or panel on the mid-foot area, and a contoured underside designed for ergonomic comfort and grip.
def model_46016_d699e580_0005():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 153.9379534222, perimeter: 43.9822952944
            with BuildLine():
                CenterArc((-0.0542156132, -35.9991133893), 10, 89.3521638708, 0.9302043403)
                CenterArc((0, -19), 7, -89.518294692, 358.6711214659)
            make_face()
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.2347399239, perimeter: 22.8778010212
            with BuildLine():
                CenterArc((71.833499628, -50.2558780473), 71.3430632371, 148.4105565663, 7.8895952489)
                CenterArc((6.8545375821, -9.9433385482), 5.1332675712, -102.9165180598, 67.9620851048)
                CenterArc((0, -19), 7, -21.626356201, 57.0094261086)
            make_face()
            # Profile area: 7.6754693684, perimeter: 19.2288591547
            with BuildLine():
                CenterArc((-11.7371074082, -25.2338449798), 6.304734504, -26.219250147, 51.3383791)
                CenterArc((-0.0542156132, -35.9991133893), 10, 90.2823682111, 36.7800824089)
                CenterArc((0, -19), 7, -149.4552875455, 58.6081143195)
            make_face()
            # Profile area: 314.1591787553, perimeter: 62.8318549277
            with BuildLine():
                CenterArc((-0.0542156132, -35.9991133893), 10, 90.2823682111, 36.7800824089)
                CenterArc((-0.0542156132, -35.9991133893), 10, 127.0624506201, 284.6168278268)
                CenterArc((-0.0542156132, -35.9991133893), 10, 51.6792784468, 37.672885424)
                CenterArc((0, -19), 7, -90.8471732261, 1.3288785341)
            make_face()
            # Profile area: 8.6635507838, perimeter: 20.7258808586
            with BuildLine():
                CenterArc((-0.0542156132, -35.9991133893), 10, 51.6792784468, 37.672885424)
                CenterArc((13.5793277405, -25.2893233251), 7.9656928119, 155.6331825447, 45.4409487436)
                CenterArc((0, -19), 7, -89.518294692, 64.1154295537)
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a curved clip or hook-shaped fastener with a primary elongated curved arm extending upward and a secondary lower flange or retention feature, designed to grip, hold, or mount components.
def model_46086_371b5052_0005():
    """Model: Can Opener v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.3419310961, perimeter: 10.8652245465
            with BuildLine():
                CenterArc((0.9540607687, 1.8690175947), 0.3, 176.3654699283, 3.6345300717)
                Line((0.654664157, 2.65), (0.654664157, 1.8880351894))
                Line((1.25, 3.7), (0.654664157, 2.65))
                CenterArc((1.25, 2.4490384615), 1.2509615385, 90, 87.7533945718)
                Line((0, 2.4980769231), (0, 2.4))
                Line((0, 2.4), (0, 0))
                Line((0, 0), (1.0439475063, 0))
                Line((1.4, 1.9), (1.0439475063, 0))
                CenterArc((1.15, 1.9), 0.25, 0, 65.402376747)
                Line((1.2540607687, 1.8690175947), (1.2540607687, 2.1273133441))
                CenterArc((0.9540607687, 1.8690175947), 0.3, -176.3654699283, 176.3654699283)
                CenterArc((0.9540607687, 1.8690175947), 0.3, 180, 3.6345300717)
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.28, perimeter: 2.3
            with BuildLine():
                Line((0.35, 0.8), (0, 0.8))
                Line((0, 0.8), (0, 0))
                Line((0, 0), (0.35, 0))
                Line((0.35, 0), (0.35, 0.8))
            make_face()
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.65, 0.4)):
                Circle(0.1)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polyhedron or truncated geometric solid featuring an irregular multi-faceted shape with predominantly angular faces, including triangular and pentagonal surfaces, with some internal geometric divisions and linear detailing across its surfaces.
def model_47894_f13353fd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3155591188, perimeter: 7.4004435942
            with BuildLine():
                Line((1.977534059, -2), (1.977534059, -4.1777558561))
                Line((1.977534059, -4.1777558561), (3.5, -4.1777558561))
                Line((3.5, -4.1777558561), (3.5, -2))
                Line((3.5, -2), (1.977534059, -2))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8731695205, perimeter: 3.3124872533
            with Locations((-3.1731759439, 0.8000809156)):
                Circle(0.5271987203)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tank or pressure vessel with a rounded capsule shape, featuring two end caps with central dome structures, internal horizontal ribbing for structural reinforcement, and symmetrical curved sidewalls.
def model_47994_ef70ce54_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6809590572, perimeter: 8.406901941
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.588, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.15
        extrude(amount=1.15, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3566567275, perimeter: 10.1371721097
            with BuildLine():
                Line((0.4531175328, 0.782391527), (-0.4510121716, 0.7836070578))
                Line((-0.4510121716, 0.7836070578), (-0.9041297045, 0.0012155309))
                Line((-0.9041297045, 0.0012155309), (-0.4531175328, -0.782391527))
                Line((-0.4531175328, -0.782391527), (0.4510121716, -0.7836070578))
                Line((0.4510121716, -0.7836070578), (0.9041297045, -0.0012155309))
                Line((0.9041297045, -0.0012155309), (0.4531175328, 0.782391527))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical dowel pin or shaft with a tapered or pointed end on one side and a flat or rounded end on the other, featuring a smooth cylindrical body.
def model_48224_53cae924_0009():
    """Model: cylinder1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=40
        extrude(amount=40)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.4323931621, perimeter: 34.1658425176
            with BuildLine():
                Line((-4.5, 0), (4.5, 0))
                Line((2.8708286934, 5.3708286934), (4.5, 0))
                CenterArc((0, 4.5), 3, 16.8744942979, 146.2510114041)
                Line((-4.5, 0), (-2.8708286934, 5.3708286934))
            make_face()
            with BuildLine():
                CenterArc((0, 4.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a seatpost tube, a cylindrical metal component with a tapered or slightly textured upper end, designed to insert into a bicycle frame and support the saddle.
def model_48224_53cae924_0010():
    """Model: cylinder1 pt2 v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.8584073464, perimeter: 27.6683501143
            with BuildLine():
                Line((1.5, 6.5), (2.5, 4))
                Line((1.5, 6.5), (-1.5, 6.5))
                Line((-2.5, 4), (-1.5, 6.5))
                Line((-2.5, 4), (-2.5, 0))
                Line((-2.5, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 4))
            make_face()
            with BuildLine():
                CenterArc((0, 4), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 4)):
                Circle(1)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 4)):
                Circle(1)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or rod with a tapered end, featuring a uniform diameter along most of its length that gradually reduces to a point at one end.
def model_48224_53cae924_0011():
    """Model: cylinder2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=200
        extrude(amount=200)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.9863055267, perimeter: 40.1998217323
            with BuildLine():
                Line((-4.5, 0), (4.5, 0))
                Line((3.428083908, 5.2058616858), (4.5, 0))
                CenterArc((0, 4.5), 3.5, 11.6349119792, 156.7301760416)
                Line((-4.5, 0), (-3.428083908, 5.2058616858))
            make_face()
            with BuildLine():
                CenterArc((0, 4.5), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or tube with a knurled or textured surface, featuring a slightly tapered end at the top and a uniform diameter along its length.
def model_48224_53cae924_0017():
    """Model: frame2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8703271841, perimeter: 25.1542058242
            with BuildLine():
                Line((40.55, 0), (40.55, -7.1917029919))
                CenterArc((40.3, -7.1917029919), 0.25, -90, 90)
                Line((40.3, -7.4417029919), (36.6463477841, -7.4417029919))
                Line((36.6463477841, -7.4417029919), (36.6463477841, -8.1917029919))
                Line((40.3, -8.1917029919), (36.6463477841, -8.1917029919))
                CenterArc((40.3, -7.1917029919), 1, -90, 90)
                Line((41.3, 0), (41.3, -7.1917029919))
                Line((40.55, 0), (41.3, 0))
            make_face()
            # Profile area: 8.8703271841, perimeter: 25.1542058242
            with BuildLine():
                Line((40.55, 7.1917029919), (40.55, 0))
                Line((40.55, 0), (41.3, 0))
                Line((41.3, 7.1917029919), (41.3, 0))
                CenterArc((40.3, 7.1917029919), 1, 0, 90)
                Line((40.3, 8.1917029919), (36.6463477841, 8.1917029919))
                Line((36.6463477841, 8.1917029919), (36.6463477841, 7.4417029919))
                Line((40.3, 7.4417029919), (36.6463477841, 7.4417029919))
                CenterArc((40.3, 7.1917029919), 0.25, 0, 90)
            make_face()
        # OneSide extrude, distance=280
        extrude(amount=280)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.25, perimeter: 12.5
            with BuildLine():
                Line((41.3, 5.9417029919), (41.3, 7.1917029919))
                Line((46.3, 5.9417029919), (41.3, 5.9417029919))
                Line((46.3, 7.1917029919), (46.3, 5.9417029919))
                Line((41.3, 7.1917029919), (46.3, 7.1917029919))
            make_face()
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or tube with a diagonal or slightly angled orientation, featuring a hollow center channel or slot running along its length and rounded ends, appearing to be a structural or mechanical component such as a shaft, guide rod, or conduit.
def model_48224_53cae924_0018():
    """Model: frame1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.8270378758, perimeter: 59.7054343355
            with BuildLine():
                Line((47.55, 8.6050176532), (47.55, -8.6050176532))
                CenterArc((47.3, -8.6050176532), 0.25, -90, 90)
                Line((47.3, -8.8550176532), (42.3354067735, -8.8550176532))
                Line((42.3354067735, -8.8550176532), (42.3354067735, -9.6050176532))
                Line((47.3, -9.6050176532), (42.3354067735, -9.6050176532))
                CenterArc((47.3, -8.6050176532), 1, -90, 90)
                Line((48.3, 8.6050176532), (48.3, -8.6050176532))
                CenterArc((47.3, 8.6050176532), 1, 0, 90)
                Line((42.3354067735, 9.6050176532), (47.3, 9.6050176532))
                Line((42.3354067735, 9.6050176532), (42.3354067735, 8.8550176532))
                Line((42.3354067735, 8.8550176532), (47.3, 8.8550176532))
                CenterArc((47.3, 8.6050176532), 0.25, 0, 90)
            make_face()
        # OneSide extrude, distance=280
        extrude(amount=280)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.6050176532), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 90, perimeter: 49
            with BuildLine():
                Line((46.8354067735, 280), (46.8354067735, 260))
                Line((42.3354067735, 280), (46.8354067735, 280))
                Line((42.3354067735, 260), (42.3354067735, 280))
                Line((46.8354067735, 260), (42.3354067735, 260))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular tray or pan with a flat base, slightly raised flanged edges, and rounded corners, featuring a grid of small holes or perforations across its surface for drainage or ventilation purposes.
def model_48332_fb679f90_0001():
    """Model: pedal rubber"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 31.5707963268, perimeter: 23.1415926536
            with BuildLine():
                CenterArc((-19, 3.5), 1, 0, 90)
                Line((-19, 4.5), (-25, 4.5))
                CenterArc((-25, 3.5), 1, 90, 90)
                Line((-26, 3.5), (-26, 0.5))
                Line((-26, 0.5), (-18, 0.5))
                Line((-18, 0.5), (-18, 3.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 43 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.3, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.8, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.3, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.8, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.3, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-22.8, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-22.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-22.8, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.3, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.05, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.8, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.05, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.3, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.8, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.05, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.3, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.3378539867, perimeter: 6.9141585482
            with BuildLine():
                CenterArc((-21.9999995192, 0.8500000119), 0.05, -179.9999861576, 179.9990604221)
                Line((-21.9500003271, 4.1500000626), (-21.9500003271, 0.8500000119))
                CenterArc((-22.0000003271, 4.1500000626), 0.05, 0, 180.0000017076)
                Line((-22.0499995192, 0.8499999998), (-22.0500003165, 4.1500000505))
            make_face()
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-21.2, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.7, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.2, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.7, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.2, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.7, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.95, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.95, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.95, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-21.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-21.2, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.7, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.2, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.7, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.2, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.7, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 43 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.3, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.8, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.3, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.8, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.3, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-22.8, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-22.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.05, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-22.8, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.3, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.05, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-23.8, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.3, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.05, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.55, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-25.3, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-24.8, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.3378539867, perimeter: 6.9141585482
            with BuildLine():
                CenterArc((-21.9999995192, 0.8500000119), 0.05, -179.9999861576, 179.9990604221)
                Line((-21.9500003271, 4.1500000626), (-21.9500003271, 0.8500000119))
                CenterArc((-22.0000003271, 4.1500000626), 0.05, 0, 180.0000017076)
                Line((-22.0499995192, 0.8499999998), (-22.0500003165, 4.1500000505))
            make_face()
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-21.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.95, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.95, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.95, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.45, 2.5)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.7, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.2, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.7, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.2, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.7, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-21.2, 1.3)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-21.2, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.7, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-20.2, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.7, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-19.2, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
            # Profile area: 0.1963495584, perimeter: 2.1446057395
            with Locations((-18.7, 3.7)):
                Ellipse(0.5000000447, 0.125, rotation=90)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or pin with a slightly tapered or beveled end, featuring a smooth, elongated shaft with a dark finish.
def model_48724_70685a9d_0008():
    """Model: table leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((72, 3), (72, -3))
                Line((72, -3), (78, -3))
                Line((78, -3), (78, 3))
                Line((78, 3), (72, 3))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 100, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-75, 0)):
                Circle(2)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a boat hull or watercraft component featuring an asymmetrical angular design with a main curved cavity, protruding flanges on the sides, and what appears to be mounting slots or openings, designed for hydrodynamic water flow.
def model_48907_25974aa4_0000():
    """Model: bottom hook v1"""
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
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6323485502, perimeter: 10.1679725106
            with BuildLine():
                Line((-1.375, -1.1), (0, 0))
                Line((0, 0), (0, 1.5))
                Line((0, 1.5), (-1.5, 1.5))
                Line((-1.5, 1.5), (-1.5, 1.2))
                Line((-1.5, 1.2), (-0.5000000075, 1.2))
                Line((-0.5000000075, 1.2), (-0.5000000075, 0.6000000089))
                _nurbs_edge([(-0.5000000075, 0.6000000089), (-0.5000000075, 0.5331381333), (-0.5175114839, 0.4119239605), (-0.5962658685, 0.2675976763), (-0.7917650218, 0.1398078438), (-1.1365335544, 0.0517888926), (-1.4616183295, 0.0165704381), (-1.7240418302, 0.0034508643), (-1.9067244797, 0.0002291267), (-2.0000000298, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.0000000298, 0), (-2.0000000298, -1.1))
                Line((-2.0000000298, -1.1), (-1.375, -1.1))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.0000000298, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1.25, -0.3), (1.25, -0.8))
                Line((0.25, -0.3), (1.25, -0.3))
                Line((0.25, -0.8), (0.25, -0.3))
                Line((1.25, -0.8), (0.25, -0.8))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((2.25, -0.8), (3.25, -0.8))
                Line((3.25, -0.3), (3.25, -0.8))
                Line((2.25, -0.3), (3.25, -0.3))
                Line((2.25, -0.3), (2.25, -0.8))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.0000000298, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.275, perimeter: 2.7
            with BuildLine():
                Line((0.25, -0.8), (0.25, -1.1))
                Line((0.25, -0.8), (0.25, -0.3))
                Line((0.25, -0.3), (0.25, 0))
                Line((0, 0), (0.25, 0))
                Line((0, -1.1), (0, 0))
                Line((0.25, -1.1), (0, -1.1))
            make_face()
            # Profile area: 0.3, perimeter: 2.6
            with BuildLine():
                Line((1.25, -1.1), (1.25, -0.8))
                Line((1.25, -0.8), (0.25, -0.8))
                Line((0.25, -0.8), (0.25, -1.1))
                Line((0.25, -1.1), (1.25, -1.1))
            make_face()
            # Profile area: 0.3, perimeter: 2.6
            with BuildLine():
                Line((0.25, -0.3), (0.25, 0))
                Line((0.25, -0.3), (1.25, -0.3))
                Line((1.25, 0), (1.25, -0.3))
                Line((0.25, 0), (1.25, 0))
            make_face()
            # Profile area: 0.3, perimeter: 2.6
            with BuildLine():
                Line((2.25, 0), (2.25, -0.3))
                Line((2.25, -0.3), (3.25, -0.3))
                Line((3.25, 0), (3.25, -0.3))
                Line((3.25, 0), (2.25, 0))
            make_face()
            # Profile area: 0.275, perimeter: 2.7
            with BuildLine():
                Line((3.25, 0), (3.25, -0.3))
                Line((3.25, -0.3), (3.25, -0.8))
                Line((3.25, -0.8), (3.25, -1.1))
                Line((3.25, -1.1), (3.5, -1.1))
                Line((3.5, -1.1), (3.5, 0))
                Line((3.5, 0), (3.25, 0))
            make_face()
            # Profile area: 0.3, perimeter: 2.6
            with BuildLine():
                Line((3.25, -0.8), (3.25, -1.1))
                Line((2.25, -0.8), (3.25, -0.8))
                Line((2.25, -1.1), (2.25, -0.8))
                Line((3.25, -1.1), (2.25, -1.1))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue/navy rectangular trim panel or fascia component with a slightly curved profile, featuring a central slot or channel running along its length and tapered ends, typical of an automotive or appliance trim piece.
def model_48917_591188ed_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0104320256, perimeter: 0.504320256
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 4.9809253219)
                Line((0.4981118292, 0.0434120444), (0.6973565609, 0.0607768622))
                CenterArc((0, 0), 0.5, 0, 4.9809253219)
                Line((0.5, 0), (0.7, 0))
            make_face()
            # Profile area: 0.0218166156, perimeter: 1.0872664626
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 4.9809253219)
                CenterArc((0, 0), 0.5, 4.9809253219, 5.0190746781)
                Line((0, 0), (0.4924038765, 0.0868240888))
                Line((0, 0), (0.5, 0))
            make_face()
            # Profile area: 0.0054070329, perimeter: 0.3027798904
            with BuildLine():
                Line((0.7, 0), (0.8, 0))
                CenterArc((0, 0), 0.8, 0, 2.4881088601)
                CenterArc((0.711155314, -0.0975506762), 0.1589277037, 56.3388451059, 38.642080216)
                CenterArc((0, 0), 0.7, 0, 4.9809253219)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with an oval or elliptical cross-section, featuring a solid dark band around the lower portion and an open lattice or mesh structure in the upper section, commonly used as a filter, ventilation component, or structural support element.
def model_49016_cd1b47bf_0000():
    """Model: MISKA v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.5724529597, perimeter: 23.6667269195
            Circle(3.766676576)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical filter or strainer component with an open top and a mesh or perforated surface on the upper portion, featuring curved walls and a solid base, designed for fluid or air filtration applications.
def model_49017_b6231068_0006():
    """Model: sruba v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0501669183, perimeter: 1.2051799872
            with BuildLine():
                Line((1.5, 0), (1.5, -0.1000000015))
                Line((1, 0), (1.5, 0))
                CenterArc((0, 0), 1, -5.7391705631, 5.7391705631)
                Line((1.5, -0.1000000015), (0.994987437, -0.1000000015))
            make_face()
            # Profile area: 0.0201669197, perimeter: 0.605180023
            with BuildLine():
                CenterArc((0, 0), 1, -180, 5.7391705631)
                Line((-1.2000000179, 0), (-1, 0))
                Line((-1.2000000179, -0.1000000015), (-1.2000000179, 0))
                Line((-0.994987437, -0.1000000015), (-1.2000000179, -0.1000000015))
            make_face()
            # Profile area: 0.1996661678, perimeter: 4.1903097192
            with BuildLine():
                Line((-1, 0), (1, 0))
                CenterArc((0, 0), 1, -180, 5.7391705631)
                Line((0.994987437, -0.1000000015), (-0.994987437, -0.1000000015))
                CenterArc((0, 0), 1, -5.7391705631, 5.7391705631)
            make_face()
            # Profile area: 0.0501669183, perimeter: 1.2051799872
            with BuildLine():
                Line((1.5, 0.1000000015), (1.5, 0))
                Line((0.994987437, 0.1000000015), (1.5, 0.1000000015))
                CenterArc((0, 0), 1, 0, 5.7391705631)
                Line((1, 0), (1.5, 0))
            make_face()
            # Profile area: 0.1996661678, perimeter: 4.1903097192
            with BuildLine():
                CenterArc((0, 0), 1, 0, 5.7391705631)
                Line((-0.994987437, 0.1000000015), (0.994987437, 0.1000000015))
                CenterArc((0, 0), 1, 174.2608294369, 5.7391705631)
                Line((-1, 0), (1, 0))
            make_face()
            # Profile area: 0.0201669197, perimeter: 0.605180023
            with BuildLine():
                Line((-1.2000000179, 0), (-1, 0))
                CenterArc((0, 0), 1, 174.2608294369, 5.7391705631)
                Line((-1.2000000179, 0.1000000015), (-0.994987437, 0.1000000015))
                Line((-1.2000000179, 0), (-1.2000000179, 0.1000000015))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a disc brake rotor with an oval or elliptical shape, featuring a central mounting hub, radial cooling fins on the top surface, and a solid friction ring with curved ventilation slots around its perimeter.
def model_49017_b6231068_0011():
    """Model: guzik v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a thin, triangular or wedge-shaped plate with a tapered profile, featuring a flat upper surface and angled lower edge, with subtle internal geometry suggested by the visible edge lines.
def model_49019_748c9a9f_0009():
    """Model: podstawa v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 316.6276328978, perimeter: 77.073803271
            with BuildLine():
                Line((0.1455664002, -10.747871599), (3.0323177461, -10.747871599))
                Line((13.8564064606, 8), (3.0323177461, -10.747871599))
                Line((13.8564064606, 8), (-13.8564064606, 8))
                Line((-13.8564064606, 8), (-3.0323177461, -10.747871599))
                Line((0.1455664002, -10.747871599), (-3.0323177461, -10.747871599))
            make_face()
            # Profile area: 8.7092437906, perimeter: 14.533652439
            with BuildLine():
                Line((0.1455664002, -10.747871599), (-3.0323177461, -10.747871599))
                Line((-3.0323177461, -10.747871599), (0, -16))
                Line((0, -16), (0.1455664002, -15.747871599))
                Line((0.1455664002, -15.747871599), (0.1455664002, -10.747871599))
            make_face()
            # Profile area: 7.2168783649, perimeter: 13.6602540378
            with BuildLine():
                Line((0.1455664002, -15.747871599), (0.1455664002, -10.747871599))
                Line((0.1455664002, -15.747871599), (3.0323177461, -10.747871599))
                Line((0.1455664002, -10.747871599), (3.0323177461, -10.747871599))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical rod or pipe with a slight taper, featuring rounded ends and a uniform dark gray finish.
def model_49019_748c9a9f_0011():
    """Model: rura v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a hollow interior, featuring a solid base and meshed or latticed sides that allow for fluid or air passage.
def model_49019_748c9a9f_0013():
    """Model: CYBUCH v7"""
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0367255757, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a slender cylindrical rod or pin with a tapered pointed tip at one end and a rounded opposite end, featuring a smooth elongated body typical of a stylus, pen, or similar precision instrument.
def model_49024_b7f02205_0017():
    """Model: smigielko v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65.5759885085, perimeter: 71.4030918922
            with BuildLine():
                Line((4.9896156366, -1), (34, -1))
                CenterArc((34, 0), 1, -90, 180)
                Line((3, 1), (34, 1))
                Line((0, 0), (3, 1))
                Line((4.9896156366, -1), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.6904374488, perimeter: 12.2196572877
            with BuildLine():
                Line((0.668912499, -1.3361625656), (-1.5847128204, -1.3361625656))
                Line((0.668912499, 2.5200407588), (0.668912499, -1.3361625656))
                Line((-1.5847128204, 2.5200407588), (0.668912499, 2.5200407588))
                Line((-1.5847128204, -1.3361625656), (-1.5847128204, 2.5200407588))
            make_face()
        # Symmetric extrude, each_side=-3
        extrude(amount=-3, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a socket head cap screw or fastener with a cylindrical shaft and a broad, circular flanged base designed for secure mounting and load distribution.
def model_49145_4a5b250e_0009():
    """Model: Srubka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4064435496, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.046211275, perimeter: 2.2995574288
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.0499999993, 0.1500000022), (0.0500000007, 0.1500000022))
                Line((0.0500000007, 0.1500000022), (0.0500000007, 0.0500000007))
                Line((0.0500000007, 0.0500000007), (0.1500000022, 0.0500000007))
                Line((0.1500000022, 0.0500000007), (0.1500000022, -0.0499999993))
                Line((0.1500000022, -0.0499999993), (0.0500000007, -0.0499999993))
                Line((0.0500000007, -0.0499999993), (0.0500000007, -0.1499999978))
                Line((0.0500000007, -0.1499999978), (-0.0499999993, -0.1499999978))
                Line((-0.0499999993, -0.1499999978), (-0.0499999993, -0.0499999993))
                Line((-0.0499999993, -0.0499999993), (-0.1499999978, -0.0499999993))
                Line((-0.1499999978, -0.0499999993), (-0.1499999978, 0.0500000007))
                Line((-0.1499999978, 0.0500000007), (-0.0499999993, 0.0500000007))
                Line((-0.0499999993, 0.0500000007), (-0.0499999993, 0.1500000022))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0100000001, perimeter: 0.400000003
            with BuildLine():
                Line((-0.0499999993, 0.0500000007), (-0.0499999993, 0.1500000022))
                Line((-0.0499999993, 0.0500000007), (0.0500000007, 0.0500000007))
                Line((0.0500000007, 0.1500000022), (0.0500000007, 0.0500000007))
                Line((-0.0499999993, 0.1500000022), (0.0500000007, 0.1500000022))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((-0.0499999993, -0.0499999993), (-0.0499999993, 0.0500000007))
                Line((0.0500000007, -0.0499999993), (-0.0499999993, -0.0499999993))
                Line((0.0500000007, 0.0500000007), (0.0500000007, -0.0499999993))
                Line((-0.0499999993, 0.0500000007), (0.0500000007, 0.0500000007))
            make_face()
            # Profile area: 0.0099999999, perimeter: 0.399999997
            with BuildLine():
                Line((-0.1499999978, 0.0500000007), (-0.0499999993, 0.0500000007))
                Line((-0.1499999978, -0.0499999993), (-0.1499999978, 0.0500000007))
                Line((-0.0499999993, -0.0499999993), (-0.1499999978, -0.0499999993))
                Line((-0.0499999993, -0.0499999993), (-0.0499999993, 0.0500000007))
            make_face()
            # Profile area: 0.0099999999, perimeter: 0.399999997
            with BuildLine():
                Line((0.0500000007, -0.0499999993), (-0.0499999993, -0.0499999993))
                Line((-0.0499999993, -0.1499999978), (-0.0499999993, -0.0499999993))
                Line((0.0500000007, -0.1499999978), (-0.0499999993, -0.1499999978))
                Line((0.0500000007, -0.0499999993), (0.0500000007, -0.1499999978))
            make_face()
            # Profile area: 0.0100000001, perimeter: 0.400000003
            with BuildLine():
                Line((0.0500000007, 0.0500000007), (0.0500000007, -0.0499999993))
                Line((0.1500000022, -0.0499999993), (0.0500000007, -0.0499999993))
                Line((0.1500000022, 0.0500000007), (0.1500000022, -0.0499999993))
                Line((0.0500000007, 0.0500000007), (0.1500000022, 0.0500000007))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0100000001, perimeter: 0.400000003
            with BuildLine():
                Line((-0.0499999993, 0.0500000007), (-0.0499999993, 0.1500000022))
                Line((-0.0499999993, 0.0500000007), (0.0500000007, 0.0500000007))
                Line((0.0500000007, 0.1500000022), (0.0500000007, 0.0500000007))
                Line((-0.0499999993, 0.1500000022), (0.0500000007, 0.1500000022))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((-0.0499999993, -0.0499999993), (-0.0499999993, 0.0500000007))
                Line((0.0500000007, -0.0499999993), (-0.0499999993, -0.0499999993))
                Line((0.0500000007, 0.0500000007), (0.0500000007, -0.0499999993))
                Line((-0.0499999993, 0.0500000007), (0.0500000007, 0.0500000007))
            make_face()
            # Profile area: 0.0099999999, perimeter: 0.399999997
            with BuildLine():
                Line((0.0500000007, -0.0499999993), (-0.0499999993, -0.0499999993))
                Line((-0.0499999993, -0.1499999978), (-0.0499999993, -0.0499999993))
                Line((0.0500000007, -0.1499999978), (-0.0499999993, -0.1499999978))
                Line((0.0500000007, -0.0499999993), (0.0500000007, -0.1499999978))
            make_face()
            # Profile area: 0.0099999999, perimeter: 0.399999997
            with BuildLine():
                Line((-0.1499999978, 0.0500000007), (-0.0499999993, 0.0500000007))
                Line((-0.1499999978, -0.0499999993), (-0.1499999978, 0.0500000007))
                Line((-0.0499999993, -0.0499999993), (-0.1499999978, -0.0499999993))
                Line((-0.0499999993, -0.0499999993), (-0.0499999993, 0.0500000007))
            make_face()
            # Profile area: 0.0100000001, perimeter: 0.400000003
            with BuildLine():
                Line((0.0500000007, 0.0500000007), (0.0500000007, -0.0499999993))
                Line((0.1500000022, -0.0499999993), (0.0500000007, -0.0499999993))
                Line((0.1500000022, 0.0500000007), (0.1500000022, -0.0499999993))
                Line((0.0500000007, 0.0500000007), (0.1500000022, 0.0500000007))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal bracket or mounting frame with a U-shaped channel design featuring three cylindrical mounting posts or bosses positioned at the corners (top-left, top-right, and bottom-left) for fastening or alignment purposes.
def model_49215_5368e45e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.617309496, perimeter: 14.2708231455
            with BuildLine():
                Line((0, 3.234216533), (0, 0))
                Line((0, 0), (3.9011950398, 0))
                Line((3.9011950398, 0), (3.9011950398, 3.234216533))
                Line((3.9011950398, 3.234216533), (0, 3.234216533))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1103031602, perimeter: 1.1773318952
            with Locations((-3.5376382182, 0.316440879)):
                Circle(0.1873781908)
            # Profile area: 0.1248847219, perimeter: 1.2527360853
            with Locations((-0.5, 0.316440879)):
                Circle(0.1993791404)
            # Profile area: 0.1168739837, perimeter: 1.2118918243
            with Locations((-0.5, 3)):
                Circle(0.1928785743)
            # Profile area: 0.1021867639, perimeter: 1.1331887519
            with Locations((-3.5, 3)):
                Circle(0.1803525913)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a socket head cap screw or hex bolt featuring a cylindrical shaft with a hexagonal or multi-faceted head on top, commonly used for fastening applications.
def model_49330_c6744767_0011():
    """Model: screw 16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((25, -40)):
                Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6696758629, perimeter: 5.0348979419
            with BuildLine():
                Line((-25.0371578344, 40.5761533031), (-25.5175423142, 40.255897023))
                Line((-25.5175423142, 40.255897023), (-25.4803844798, 39.6797437199))
                Line((-25.4803844798, 39.6797437199), (-24.9628421656, 39.4238466969))
                Line((-24.9628421656, 39.4238466969), (-24.4824576858, 39.744102977))
                Line((-24.4824576858, 39.744102977), (-24.5196155202, 40.3202562801))
                Line((-24.5196155202, 40.3202562801), (-25.0371578344, 40.5761533031))
            make_face()
            with BuildLine():
                CenterArc((-25, 40), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-25, 40)):
                Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or tube with fine longitudinal grooves or ridges running along its entire length, featuring a hollow bore through the center.
def model_49400_c5be6ea9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9452431127, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((2, 2), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2, 2), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a pyramidal or wedge-shaped enclosure with a triangular cross-section, featuring internal structural ribbing and bracing, two mounting holes on opposite sides, and an open or latticed top surface designed for ventilation or component access.
def model_49412_1f199584_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 149.0515496022, perimeter: 79.0176968209
            with BuildLine():
                Line((-8, -5), (8, -5))
                Line((8, -5), (8, 5))
                Line((-8, 5), (8, 5))
                Line((-8, 5), (-8, -5))
            make_face()
            with BuildLine():
                CenterArc((-6.4, 3.4), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.4, -3.4), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, -2.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 2.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5654866776, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5654866776, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((2.5, -2.5), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5, -2.5), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trapezoidal enclosure or duct component with a tapered box shape featuring internal structural ribs, open side panels, and internal cross-bracing for reinforcement.
def model_49503_e42c01c0_0002():
    """Model: Pedal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.7588821059, perimeter: 42.7725847007
            with BuildLine():
                Line((-0.0004504082, -2.4998123811), (-4.999999993, -2.4327009087))
                Line((-4.999999993, -2.4327009087), (-4.999999993, -8.4998123642))
                Line((0.000000007, -8.4998123642), (-4.999999993, -8.4998123642))
                Line((-0.0004504082, -2.4998123811), (0.000000007, -8.4998123642))
            make_face()
            with BuildLine():
                Line((-0.4926378414, -3.3303614435), (-0.4923019087, -7.830361431))
                Line((-0.4923019087, -7.830361431), (-1.5315771814, -7.230439013))
                CenterArc((-1.3208427011, -6.8653732514), 0.4215234648, -179.995722772, 60)
                Line((-1.7425580122, -4.2955047837), (-1.7423661648, -6.8654047189))
                CenterArc((-1.3210345486, -4.2954733163), 0.4215234648, 120.004277228, 60)
                Line((-0.4926378414, -3.3303614435), (-1.531823532, -3.9304390222))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.5077480473, -3.3305113109), (-3.4685175628, -3.9305113109))
                CenterArc((-3.6792792952, -4.2955613398), 0.4215234648, 0, 60)
                Line((-3.2577558303, -4.2955613398), (-3.2577558303, -6.8654612821))
                CenterArc((-3.6792792952, -6.8654612821), 0.4215234648, -60, 60)
                Line((-4.5077480473, -7.8305113109), (-3.4685175628, -7.2305113109))
                Line((-4.5077480473, -3.3305113109), (-4.5077480473, -7.8305113109))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.999999993, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.1, perimeter: 5.8
            with BuildLine():
                Line((7.2529713011, -0.7036990757), (5.7529713011, -0.7036990757))
                Line((7.2529713011, 0.6963009243), (7.2529713011, -0.7036990757))
                Line((5.7529713011, 0.6963009243), (7.2529713011, 0.6963009243))
                Line((5.7529713011, -0.7036990757), (5.7529713011, 0.6963009243))
            make_face()
            # Profile area: 2.1, perimeter: 5.8
            with BuildLine():
                Line((5.4529713011, -0.7), (3.9529713011, -0.7))
                Line((5.4529713011, 0.7), (5.4529713011, -0.7))
                Line((3.9529713011, 0.7), (5.4529713011, 0.7))
                Line((3.9529713011, -0.7), (3.9529713011, 0.7))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hex bolt or cap screw consisting of a hexagonal head (blue) attached to a cylindrical shaft (dark gray) with a threaded or textured surface.
def model_49503_e42c01c0_0005():
    """Model: pedals screw"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8059223083, perimeter: 6.2353829072
            with BuildLine():
                Line((-0.910988398, -0.5001001286), (-0.0223947832, -1.0389891596))
                Line((-0.0223947832, -1.0389891596), (0.8885936148, -0.5388890309))
                Line((0.8885936148, -0.5388890309), (0.910988398, 0.5001001286))
                Line((0.910988398, 0.5001001286), (0.0223947832, 1.0389891596))
                Line((0.0223947832, 1.0389891596), (-0.8885936148, 0.5388890309))
                Line((-0.8885936148, 0.5388890309), (-0.910988398, -0.5001001286))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7539822369, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a hex bolt or fastener with a polygonal (hexagonal) head and a long cylindrical threaded shaft extending from it.
def model_49562_6df35938_0000():
    """Model: V joint bolt 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4156921938, perimeter: 2.4
            with BuildLine():
                Line((0.2, -0.3464101615), (0.4, 0))
                Line((0.4, 0), (0.2, 0.3464101615))
                Line((0.2, 0.3464101615), (-0.2, 0.3464101615))
                Line((-0.2, 0.3464101615), (-0.4, 0))
                Line((-0.4, 0), (-0.2, -0.3464101615))
                Line((-0.2, -0.3464101615), (0.2, -0.3464101615))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


# Description: This is a wing or fin assembly featuring a swept aerodynamic shape with a curved leading edge, a latticed or truss-like internal structure (shown in blue), dark composite end caps, and a streamlined profile designed for fluid dynamics performance.
def model_49562_6df35938_0007():
    """Model: V Joint"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6666820518, perimeter: 15.2999966806
            with BuildLine():
                Line((0.1500810693, -1.6678039954), (0.8777295457, -2.4938678768))
                CenterArc((1.252925819, -2.1633716491), 0.5, -138.6243929328, 168.7018512647)
                Line((0.432674337, 0.2505851662), (1.6856001495, -1.9127864866))
                CenterArc((0, 0), 0.5000000075, 30.0774583318, 120.0000003415)
                Line((-0.4333502898, 0.2494143817), (-1.6804221798, -1.9173370348))
                CenterArc((-1.2470718965, -2.1667514128), 0.5, 150.0774586734, 168.8927145783)
                Line((-0.1508710301, -1.6687121219), (-0.8698879214, -2.4949773243))
                CenterArc((0.0000025599, -1.8000024865), 0.2, 41.3756070672, 97.5945661845)
            make_face()
            with BuildLine():
                CenterArc((1.252925819, -2.1633716491), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2470718965, -2.1667514128), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.9)):
                Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a hollow tubular body, featuring two opposing circular holes or openings on each end and horizontal ribbed or grooved surface detailing along its length.
def model_49600_4c47092d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.5769333168, perimeter: 20.541182735
            with Locations((0, -0.2692307692)):
                Circle(3.2692307692)
        # OneSide extrude, distance=14.5
        extrude(amount=14.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 21.2433531878, perimeter: 16.3386611829
            with Locations((0, -0.2692307692)):
                Circle(2.6003786908)
        # OneSide extrude, distance=-23
        extrude(amount=-23, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (doughnut-shaped) stator or rotor component with a large central circular opening and a ribbed or laminated construction featuring radial fins or slots distributed around its circumference.
def model_49613_1b97c07b_0003():
    """Model: light controle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 5), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0197330767, perimeter: 0.5922011154
            with BuildLine():
                Line((-0.100335983, 6.1499999548), (-0.100335983, 6.2459665688))
                Line((0.099664017, 6.1499999548), (-0.100335983, 6.1499999548))
                Line((0.099664017, 6.2460204989), (0.099664017, 6.1499999548))
                CenterArc((0, 5), 1.25, 85.4268839422, 9.1771318059)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical tube or sleeve with rounded ends (capsule shape), featuring a circular hole or opening on one end and a smooth, hollow interior designed for fluid or component passage.
def model_49613_1b97c07b_0010():
    """Model: rubber"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((-12.5, 20), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-12.5, 20), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((12.5, 20), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, 20), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((12.5, 20)):
                Circle(2.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or support component featuring an angular, L-shaped structure with multiple planar surfaces and triangulated facets, combining a vertical flange with a horizontal base and internal geometric complexity.
def model_49695_28e7f7e5_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 90, perimeter: 38
            with BuildLine():
                Line((0, 1), (-10, 1))
                Line((0, 10), (0, 1))
                Line((-10, 10), (0, 10))
                Line((-10, 1), (-10, 10))
            make_face()
        # OneSide extrude, distance=16
        extrude(amount=16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 64.3153800761, perimeter: 32.6682450771
            with BuildLine():
                Line((7, 10), (6.0165209973, 4.0991259837))
                Line((6.0165209973, 4.0991259837), (16, 2.4352128166))
                Line((16, 2.4352128166), (16, 10))
                Line((16, 10), (7, 10))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular disc or plate with a flat, slightly beveled or rounded edge rim, featuring a smooth, flat primary surface tilted at an angle in 3D space.
def model_49703_b92021be_0015():
    """Model: Gear 79"""
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
            # Profile area: 1213.977496359, perimeter: 123.5123116808
            with BuildLine():
                CenterArc((0, 0), 19.6575949367, 1.2417405924, 357.5165188152)
                CenterArc((0, 0), 19.6575949367, -1.2417405924, 2.4834811848)
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.9091322852, perimeter: 3.7792872487
            with BuildLine():
                Line((19.6529785745, 0.4259951254), (19.9869003812, 0.4332331662))
                CenterArc((0, 0), 19.6575949367, -1.2417405924, 2.4834811848)
                Line((19.6529785745, -0.4259951254), (19.9869003812, -0.4332331662))
                _nurbs_edge([(19.9869003812, -0.4332331662), (20.0174146324, -0.432317329), (20.0785879652, -0.4304813078), (20.170143991, -0.4210336243), (20.2617838433, -0.4091387685), (20.3534594925, -0.3944662757), (20.445165338, -0.3775581574), (20.5368921821, -0.3585761032), (20.628622103, -0.3376578577), (20.7203843265, -0.3150549382), (20.7813485066, -0.2986260132), (20.8118977591, -0.2903934515)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0915550279, 0.1835446052, 0.2759538342, 0.3687813049, 0.462026557, 0.5556893805, 0.649769661, 0.7442673284, 0.8391823362, 0.8391823362, 0.8391823362, 0.8391823362], 3)
                CenterArc((0.0043661666, 0), 20.809557884, -0.7995777384, 1.5991554769)
                _nurbs_edge([(19.9869003812, 0.4332331662), (20.0174146324, 0.432317329), (20.0785879652, 0.4304813078), (20.170143991, 0.4210336243), (20.2617838433, 0.4091387685), (20.3534594925, 0.3944662757), (20.445165338, 0.3775581574), (20.5368921821, 0.3585761032), (20.628622103, 0.3376578577), (20.7203843265, 0.3150549382), (20.7813485066, 0.2986260132), (20.8118977591, 0.2903934515)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0915550279, 0.1835446052, 0.2759538342, 0.3687813049, 0.462026557, 0.5556893805, 0.649769661, 0.7442673284, 0.8391823362, 0.8391823362, 0.8391823362, 0.8391823362], 3)
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical knob or dial with a textured grip surface on the curved body and a flat face featuring a small pointer or index mark, designed for manual rotation and tactile control.
def model_49703_b92021be_0016():
    """Model: Shaft1"""
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
            # Profile area: 35.9127839561, perimeter: 21.2436661851
            with BuildLine():
                CenterArc((0, 0), 3.3810344828, 3.6133191992, 352.7733616016)
                CenterArc((0, 0), 3.3810344828, -3.6133191992, 7.2266383984)
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2187696068, perimeter: 1.836653539
            with BuildLine():
                Line((3.374313341, 0.2130813234), (3.5312656964, 0.2229925594))
                CenterArc((0, 0), 3.3810344828, -3.6133191992, 7.2266383984)
                Line((3.374313341, -0.2130813234), (3.5312656964, -0.2229925594))
                _nurbs_edge([(3.5312656964, -0.2229925594), (3.5468032595, -0.2226145086), (3.5780877856, -0.2218533121), (3.6248633967, -0.2148960959), (3.6717964682, -0.2057426503), (3.7188121219, -0.1940644622), (3.7658772843, -0.1803095915), (3.8129621321, -0.1645946247), (3.8600231228, -0.147020708), (3.9070886376, -0.1277927757), (3.938126967, -0.1136966675), (3.953737396, -0.1066071656)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0465844731, 0.0937967656, 0.1416147825, 0.1900362111, 0.2390601876, 0.2886862459, 0.3389140797, 0.3897434616, 0.441174209, 0.441174209, 0.441174209, 0.441174209], 3)
                CenterArc((-0.0054568304, 0), 3.9606292442, -1.5424009896, 3.0848019792)
                _nurbs_edge([(3.5312656964, 0.2229925594), (3.5468032595, 0.2226145086), (3.5780877856, 0.2218533121), (3.6248633967, 0.2148960959), (3.6717964682, 0.2057426503), (3.7188121219, 0.1940644622), (3.7658772843, 0.1803095915), (3.8129621321, 0.1645946247), (3.8600231228, 0.147020708), (3.9070886376, 0.1277927757), (3.938126967, 0.1136966675), (3.953737396, 0.1066071656)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0465844731, 0.0937967656, 0.1416147825, 0.1900362111, 0.2390601876, 0.2886862459, 0.3389140797, 0.3897434616, 0.441174209, 0.441174209, 0.441174209, 0.441174209], 3)
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or tube with an open top end and a slight taper, featuring a textured or ribbed exterior surface and a blue-tinted interior visible at the opening.
def model_49909_13b120dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 278.5398163397, perimeter: 71.4159265359
            with BuildLine():
                CenterArc((-10, 0), 5, 90, 180)
                Line((-10, -5), (10, -5))
                CenterArc((10, 0), 5, -90, 180)
                Line((-10, 5), (10, 5))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a handheld fan featuring a circular mesh head with dual concentric grilles, mounted on a cylindrical handle below, with an overall teardrop-like profile when viewed from the side.
def model_50001_e86a6698_0003():
    """Model: Headlight"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.8597231867, perimeter: 13.1853522473
            with BuildLine():
                CenterArc((1.27, 7.6199998856), 3.8099999428, -109.4712209387, 38.9424418774)
                Line((0, 4.0278974978), (0, 0))
                Line((0, 0), (2.54, 0))
                Line((2.54, 0), (2.54, 4.0278974978))
            make_face()
            # Profile area: 42.5601949356, perimeter: 25.9935834136
            with BuildLine():
                Line((2.54, 4.0278974978), (2.54, 5.08))
                CenterArc((1.27, 7.6199998856), 3.8099999428, -70.5287790613, 321.0575581226)
                Line((0, 5.08), (0, 4.0278974978))
                Line((2.54, 5.08), (0, 5.08))
            make_face()
            # Profile area: 3.0434768133, perimeter: 7.233762256
            with BuildLine():
                Line((2.54, 5.08), (0, 5.08))
                Line((0, 5.08), (0, 4.0278974978))
                CenterArc((1.27, 7.6199998856), 3.8099999428, -109.4712209387, 38.9424418774)
                Line((2.54, 4.0278974978), (2.54, 5.08))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((1.27, 7.6199998856)):
                Circle(2.54)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or connector with a rounded head on one end and a slightly tapered or stepped cylindrical shaft, featuring a smooth finish typical of a screw, bolt, or similar mechanical component.
def model_50001_e86a6698_0007():
    """Model: Bumper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.62), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25.3353739549, perimeter: 39.8982267006
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a stepped cylindrical connector or adapter featuring a large flanged head on one end and a smaller diameter shaft on the other, with a central axial hole running through the entire length.
def model_50001_e86a6698_0011():
    """Model: Coupler"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 60.8048974917, perimeter: 47.8778720407
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)
    return part.part


# Description: This is a spiral or helical pump impeller featuring a curved, twisted cylindrical body with axial flow channels and a flat mounting base with radial fins or blades for anchoring to a shaft or housing.
def model_50036_7766eac1_0006():
    """Model: large sleeve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 73.4657082647, perimeter: 48.4247779608
            with BuildLine():
                Line((82, -2.75), (68, -2.75))
                Line((82, 2.75), (82, -2.75))
                Line((68, 2.75), (82, 2.75))
                Line((68, -2.75), (68, 2.75))
            make_face()
            with BuildLine():
                CenterArc((80, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((70, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.9185991623, perimeter: 40.3328413877
            with BuildLine():
                Line((75, 1), (72.4504902432, 1))
                CenterArc((75, 3.75), 2.75, 0, 360)
                Line((77.5495097568, 1), (75, 1))
                CenterArc((75, 3.75), 3.75, -47.1665719339, 274.3331438679)
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.ADD)
    return part.part


# Description: This is a bent sheet metal bracket or handle with a rectangular tubular cross-section, featuring two vertical legs connected by an angled top section, with cylindrical mounting holes or bushings at each end.
def model_50214_683032e0_0001():
    """Model: mount transformer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2000013575, perimeter: 32.4000001818
            with BuildLine():
                Line((33.5, 1), (34.7000005171, 1))
                Line((34.7000005171, 1), (34.7000005171, 4.0000000596))
                Line((34.7000005171, 4.0000000596), (42.3000006303, 4.0000000596))
                Line((42.3000006303, 4.0000000596), (42.3000006303, 1))
                Line((42.3000006303, 1), (43.5, 1))
                Line((43.5, 1), (43.5, 1.2))
                Line((43.5, 1.2), (42.5000006333, 1.2))
                Line((42.5000006333, 1.2), (42.5000006333, 4.2000000626))
                Line((34.5, 4.2), (42.5000006333, 4.2000000626))
                Line((34.5, 1.2), (34.5, 4.2))
                Line((33.5, 1.2), (34.5, 1.2))
                Line((33.5, 1), (33.5, 1.2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5, -43.0000003166)):
                Circle(0.1)
            # Profile area: 0.0536503183, perimeter: 1.7853994733
            with BuildLine():
                CenterArc((-0.5000000075, -34.0000005066), 0.5000005066, 0, 90)
                Line((0.0000004992, -34.0000005066), (0, -33.5))
                Line((0, -33.5), (-0.5000000075, -33.5))
            make_face()
            # Profile area: 0.0536503108, perimeter: 1.7853994584
            with BuildLine():
                Line((-1, -33.5), (-1.0000005141, -34.0000005066))
                CenterArc((-0.5000000075, -34.0000005066), 0.5000005066, 90, 90)
                Line((-0.5000000075, -33.5), (-1, -33.5))
            make_face()
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5000000075, -34.0000005066)):
                Circle(0.1)
            # Profile area: 0.0536505495, perimeter: 1.7853967012
            with BuildLine():
                Line((-0.9999996834, -43.0000006407), (-1, -43.5))
                Line((-0.5, -43.5), (-1, -43.5))
                CenterArc((-0.5, -43.0000003166), 0.4999996834, -179.9999628608, 89.9999628608)
            make_face()
            # Profile area: 0.2406360325, perimeter: 4.3506501621
            with BuildLine():
                Line((-1.1500000171, -43.0000006407), (-1.1210102394, -43.5448377002))
                Line((-1.1210102394, -43.5448377002), (0.0783102164, -43.5727288736))
                Line((0.0783102164, -43.5727288736), (0.1117796245, -43.0167648173))
                Line((0.1117796245, -43.0167648173), (-0.0000003166, -43.0000006407))
                CenterArc((-0.5, -43.0000003166), 0.4999996834, -90, 89.9999628608)
                Line((-0.5, -43.5), (-1, -43.5))
                Line((-0.9999996834, -43.0000006407), (-1, -43.5))
                Line((-0.9999996834, -43.0000006407), (-1.1500000171, -43.0000006407))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or pentagonal prism-shaped enclosure or container with a slanted top face, featuring internal geometric subdivisions and appearing to be a hollow structural component with multiple planar faces and internal ribbing or support structures.
def model_50214_683032e0_0002():
    """Model: interior upper housing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 51, perimeter: 29
            with BuildLine():
                Line((-17, 0), (-17, 8.5))
                Line((-17, 8.5), (-23, 8.5))
                Line((-23, 8.5), (-23, 0))
                Line((-17, 0), (-23, 0))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-20.000000298, 8.2500001229)):
                Circle(0.1)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-21.8000003248, 1.3000000194)):
                Circle(0.1000000015)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-18.2000003248, 1.3000000194)):
                Circle(0.1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal duct/box component with a dark body and blue reinforced flanges, featuring multiple openings/ports on the sides and angled top surfaces for airflow management, likely used as an HVAC or ventilation duct fitting.
def model_50214_683032e0_0004():
    """Model: transformer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.7364170368, perimeter: 31.5090553088
            with BuildLine():
                Line((25.7545276544, 0.5), (25, 0.5))
                Line((25, 0.5), (25, 0))
                Line((25, 0), (31, 0))
                Line((31, 0), (31, 0.5))
                Line((26, 0.5), (31, 0.5))
                Line((26, 0.5), (26, 3.5))
                Line((31, 3.5), (26, 3.5))
                Line((31, 3.5), (31, 4))
                Line((31, 4), (25, 4))
                Line((25, 4), (25, 3.5))
                Line((25.7545276544, 3.5), (25, 3.5))
                Line((25.7545276544, 0.5), (25.7545276544, 3.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.2942129505, perimeter: 9.1376399266
            with BuildLine():
                CenterArc((1.5, -30), 1.5, 0, 180)
                CenterArc((1.5, -30), 1.5, 180, 41.8103148958)
                Line((0.3819660113, -31), (2.6180339887, -31))
                CenterArc((1.5, -30), 1.5, -41.8103148958, 41.8103148958)
            make_face()
            # Profile area: 0.77437052, perimeter: 4.7592739892
            with BuildLine():
                Line((0.3819660113, -31), (2.6180339887, -31))
                CenterArc((1.5, -30), 1.5, -138.1896851042, 96.3793702084)
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                Line((3, -26), (0, -26))
                CenterArc((1.5, -26), 1.5, 0, 180)
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                CenterArc((1.5, -26), 1.5, 180, 180)
                Line((3, -26), (0, -26))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupler with two dark-colored tubular ends separated by a central blue-striped section, featuring a circular aperture or slot running through the middle for alignment or passage purposes.
def model_50214_683032e0_0007():
    """Model: strut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3672640872, perimeter: 16.1956555828
            with BuildLine():
                CenterArc((54, 0), 0.5, 179.9999347473, 246.4217857952)
                Line((54.2000008076, 0.458257217), (54.2000008076, 0.2236060754))
                CenterArc((54, 0), 0.3, 131.8101094774, 276.3793686805)
                Line((53.8000008017, 0.4582579194), (53.8000008017, 0.2236075148))
                Line((53.8014501128, 0.5563990194), (53.8000008017, 0.4582579194))
                Line((53.5000007182, 0.6306299449), (53.8014501128, 0.5563990194))
                CenterArc((52.0000002824, -2.23041272), 3.2304127349, 62.3326721728, 55.3346399094)
                Line((50.200000748, 0.5567564609), (50.5000006327, 0.6306303571))
                Line((50.200000748, 0.5567564609), (50.200000748, 0.2236061287))
                CenterArc((50, 0), 0.3, 131.8101247501, 276.3793686806)
                Line((49.8000007421, 0.4582578934), (49.8000007421, 0.2236074615))
                CenterArc((50, 0), 0.5, 113.5780856965, 246.4218568161)
                Line((50.5000005017, 0.4999998936), (50.5, -0.0000005017))
                CenterArc((51.99999737, -2.2795482144), 3.15846138, 61.6461323643, 56.707604766)
                Line((53.5000005694, 0.4999964769), (53.5, 0.0000005694))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6141848493, perimeter: 3.82644591
            with BuildLine():
                Line((51.1339752717, -4), (52.8660260793, -4))
                CenterArc((52.0000006755, -4.5), 1, 30, 120)
            make_face()
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((52.0000006755, -2)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((52.0000006755, 0.5)):
                Circle(1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved pipe elbow or duct connector featuring a tubular body with an approximately 90-degree bend, a circular flange on the outer curve, and textured surface details suggesting internal ribbing or reinforcement.
def model_50315_0f1419bf_0007():
    """Model: 2in1 Screwdriver Mini"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2848086268, perimeter: 2.427237803
            with BuildLine():
                Line((0.0437256247, -1.9013710572), (0.1668817364, -1.9875950786))
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, -34.9994517296, 90.0154160223)
                Line((-0.4614918235, -2.098487657), (0.0559593172, -1.3590524255))
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, -124.9840357073, 41.769291196)
                Line((-0.1494513174, -2.1768632836), (0.0437256247, -1.9013710572))
            make_face()
            # Profile area: 0.235601448, perimeter: 2.2412620365
            with BuildLine():
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, -124.9840357073, 41.769291196)
                Line((-0.8908788075, -2.7120796252), (-0.4614918235, -2.098487657))
                Line((-0.8908788075, -2.7120796252), (-0.6452689862, -2.8839555066))
                Line((-0.6452689862, -2.8839555066), (-0.1494513174, -2.1768632836))
            make_face()
            # Profile area: 1.166389618, perimeter: 6.5956212644
            with BuildLine():
                CenterArc((0.006018021, -1.3721930573), 0.6360792268, -75.3508812861, 109.8178097641)
                Line((0.3304355207, -1.0120348005), (0.5304354382, -1.0122164535))
                Line((0.3304355207, 0.1879651995), (0.3304355207, -1.0120348005))
                Line((-0.2751364658, 0.1879651995), (0.3304355207, 0.1879651995))
                Line((-0.2754672287, -1.0119493644), (-0.2751364658, 0.1879651995))
                CenterArc((-1.2266357872, -1.0116871696), 0.9511685946, -17.1672788524, 17.1514849612)
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, 55.0159642927, 49.7587427317)
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, -34.9994517296, 90.0154160223)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2349573184, perimeter: 2.237936612
            with BuildLine():
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, -166.4996682876, 41.5156325803)
                Line((-0.6415513124, -1.8341157006), (-1.1364886017, -2.5402037627))
                Line((-1.1364886017, -2.5402037627), (-0.8908788075, -2.7120796252))
                Line((-0.8908788075, -2.7120796252), (-0.4614918235, -2.098487657))
            make_face()
            # Profile area: 0.2539726651, perimeter: 2.2555172085
            with BuildLine():
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, 55.0159642927, 49.7587427317)
                CenterArc((-1.2266357872, -1.0116871696), 0.9511685946, -35.0287993182, 17.8615204658)
                Line((-0.4477584127, -1.5576466286), (-0.6415513124, -1.8341157006))
                CenterArc((-0.2027662532, -1.7287700413), 0.4512538489, -166.4996682876, 41.5156325803)
                Line((-0.4614918235, -2.098487657), (0.0559593172, -1.3590524255))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a cylindrical filter component with a perforated or mesh surface design, featuring rounded end caps and a hollow tubular body for fluid or air filtration applications.
def model_50379_ebec8fae_0000():
    """Model: crusher"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 29.6898913534, perimeter: 24.9363916879
            with BuildLine():
                CenterArc((-20.3199996948, 5.0799999237), 3.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20.3199996948, 5.0799999237), 0.79375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=13.335
        extrude(amount=13.335)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13.335), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0507074955, perimeter: 1.0539216087
            with BuildLine():
                Line((-20.5231996804, 8.1281080645), (-20.5231676467, 8.2484929067))
                Line((-20.1167996948, 8.1279999237), (-20.5231996804, 8.1281080645))
                Line((-20.1167996948, 8.2484908516), (-20.1167996948, 8.1279999237))
                CenterArc((-20.3199996948, 5.0799999237), 3.175, 86.330562195, 7.3382960842)
            make_face()
        # OneSide extrude, distance=-15.24
        extrude(amount=-15.24, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or barrel component with a rounded rectangular profile, featuring a central circular opening or bore on the left end and horizontal linear grooves or flutes running along its length.
def model_50382_cb85058c_0004():
    """Model: Front Wheel v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 3.4871678455, perimeter: 23.2477856366
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=3.5, against=-0.3
        extrude(amount=3.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box or enclosure with a trapezoidal top face, featuring angled side walls and internal geometric subdivisions or reinforcement ribs visible through the semi-transparent surfaces.
def model_50409_4a322fbf_0001():
    """Model: R0402_B"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 33 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0006826208, perimeter: 0.1259710891
            with BuildLine():
                CenterArc((0.33, 0), 0.3, 175.2198081528, 9.5603836944)
                Line((0.0310434814, -0.025), (0.044, -0.025))
                Line((0.044, -0.025), (0.044, 0.025))
                Line((0.044, 0.025), (0.0310434814, 0.025))
            make_face()
            # Profile area: 0.0002892699, perimeter: 0.1077079632
            with BuildLine():
                Line((0.044, -0.025), (0.044, 0.025))
                Line((0.044, -0.025), (0.045, -0.025))
                CenterArc((0.045, -0.02), 0.005, -89.9999999217, 89.9999999217)
                Line((0.05, -0.02), (0.05, 0.02))
                CenterArc((0.0449999999, 0.02), 0.0050000001, 0, 90.0000000783)
                Line((0.0449999999, 0.025), (0.044, 0.025))
            make_face()
        # OneSide extrude, distance=0.035
        extrude(amount=0.035)
    return part.part


# Description: This is a rectangular enclosure or housing box with a sloped/angled top cover and a recessed front panel featuring a mesh or perforated surface for ventilation or component access.
def model_50409_4a322fbf_0010():
    """Model: C0402-NO"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0003406485, perimeter: 0.1590997568
            with BuildLine():
                Line((0.0312531407, -0.025), (0.045, -0.025))
                CenterArc((0.045, -0.02), 0.005, -89.9999999515, 89.9999999515)
                Line((0.05, -0.02), (0.05, 0.02))
                CenterArc((0.045, 0.02), 0.005, 0, 90.0000000485)
                Line((0.045, 0.025), (0.0312531407, 0.025))
                CenterArc((0.28, 0), 0.25, 174.2608295227, 0.46049438)
                Line((0.044, 0.023), (0.0310602483, 0.023))
                Line((0.044, -0.023), (0.044, 0.023))
                Line((0.0310602483, -0.023), (0.044, -0.023))
                CenterArc((0.28, 0), 0.25, -174.7213238966, 0.4604943739)
            make_face()
            # Profile area: 0.0006277567, perimeter: 0.1179446425
            with BuildLine():
                Line((0.0310602483, -0.023), (0.044, -0.023))
                Line((0.044, -0.023), (0.044, 0.023))
                Line((0.044, 0.023), (0.0310602483, 0.023))
                CenterArc((0.28, 0), 0.25, 174.7213239028, 10.5573522006)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a hexagonal or polygonal box-like container with an open top, featuring multiple faceted surfaces, internal structural ribbing or bracing, and a complex geometric design with both convex and concave surfaces.
def model_50479_a1f097b3_0002():
    """Model: Hood v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((0, 0), (0, 1))
                Line((0, 1), (-2.5, 1))
                Line((-2.5, 1), (-2.5, 0))
                Line((0, 0), (-2.5, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((-1.5, 1.5), (0, 1.5))
                Line((-1.5, 0), (-1.5, 1.5))
                Line((-1.5, 0), (0, 0))
                Line((0, 1.5), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bent pipe or elbow connector with a angular L-shaped configuration, consisting of two cylindrical sections joined at approximately a 90-degree angle, designed to redirect fluid or gas flow in piping systems.
def model_50479_a1f097b3_0010():
    """Model: Front Landing Gear v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a flat, rectangular panel or tray with a parallelogram-like shape, featuring internal cross-bracing or ribbed support structure visible through the top surface.
def model_50585_06c574f3_0010():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300, perimeter: 70
            with BuildLine():
                Line((17.9999999702, -13.4999999776), (-2.0000000298, -13.4999999776))
                Line((17.9999999702, 1.5000000224), (17.9999999702, -13.4999999776))
                Line((-2.0000000298, 1.5000000224), (17.9999999702, 1.5000000224))
                Line((-2.0000000298, -13.4999999776), (-2.0000000298, 1.5000000224))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-0.9999999702, 5.9999999776)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-14.9999999702, 5.9999999776)):
                Circle(0.5)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a coated carbide drill bit or end mill with a tapered, elongated hexagonal or multi-faceted body, featuring a pointed tip for precision drilling or cutting operations, and a dark protective coating for enhanced durability and heat resistance.
def model_50681_eb7a9f92_0012():
    """Model: Lower Strap v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.2500006042, perimeter: 31.6094717545
            with BuildLine():
                Line((0, 0), (0, -4))
                Line((0, -4), (0.3000000045, -13.5000002012))
                Line((2.3000000343, -13.5000002012), (0.3000000045, -13.5000002012))
                Line((2.6, -4), (2.3000000343, -13.5000002012))
                Line((2.6, 0), (2.6, -4))
                Line((0, 0), (2.6, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 32 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 8.2000001222), (-1.4000000209, 8.2000001222))
                Line((-1.1000000164, 8.3000001237), (-1.1000000164, 8.2000001222))
                Line((-1.4000000209, 8.3000001237), (-1.1000000164, 8.3000001237))
                Line((-1.4000000209, 8.2000001222), (-1.4000000209, 8.3000001237))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 8.8000001311), (-1.1000000164, 8.9000001326))
                Line((-1.1000000164, 8.9000001326), (-1.4000000209, 8.9000001326))
                Line((-1.4000000209, 8.9000001326), (-1.4000000209, 8.8000001311))
                Line((-1.4000000209, 8.8000001311), (-1.1000000164, 8.8000001311))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 9.4000001401), (-1.4000000209, 9.4000001401))
                Line((-1.1000000164, 9.5000001416), (-1.1000000164, 9.4000001401))
                Line((-1.4000000209, 9.5000001416), (-1.1000000164, 9.5000001416))
                Line((-1.4000000209, 9.4000001401), (-1.4000000209, 9.5000001416))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 10.000000149), (-1.1000000164, 10.1000001505))
                Line((-1.1000000164, 10.1000001505), (-1.4000000209, 10.1000001505))
                Line((-1.4000000209, 10.1000001505), (-1.4000000209, 10.000000149))
                Line((-1.4000000209, 10.000000149), (-1.1000000164, 10.000000149))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 10.600000158), (-1.4000000209, 10.600000158))
                Line((-1.1000000164, 10.7000001594), (-1.1000000164, 10.600000158))
                Line((-1.4000000209, 10.7000001594), (-1.1000000164, 10.7000001594))
                Line((-1.4000000209, 10.600000158), (-1.4000000209, 10.7000001594))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 11.2000001669), (-1.1000000164, 11.3000001684))
                Line((-1.1000000164, 11.3000001684), (-1.4000000209, 11.3000001684))
                Line((-1.4000000209, 11.3000001684), (-1.4000000209, 11.2000001669))
                Line((-1.4000000209, 11.2000001669), (-1.1000000164, 11.2000001669))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-1.1000000164, 11.8000001758), (-1.4000000209, 11.8000001758))
                Line((-1.1000000164, 11.9000001773), (-1.1000000164, 11.8000001758))
                Line((-1.4000000209, 11.9000001773), (-1.1000000164, 11.9000001773))
                Line((-1.4000000209, 11.8000001758), (-1.4000000209, 11.9000001773))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bent tubular bracket or handle with two cylindrical end caps, featuring an angular Z-shaped profile with a hollow rectangular cross-section and blue-highlighted edges.
def model_50681_eb7a9f92_0013():
    """Model: Chrome Buckle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.093983266, perimeter: 1.8842902836
            with BuildLine():
                Line((-0.0484260123, 0.1940487602), (-0.0101624535, 0.1997416445))
                CenterArc((0, 0), 0.2, 104.0122924844, 177.2958901142)
                Line((0.1153556736, -0.1633801352), (0.0392172374, -0.196117333))
                CenterArc((0, 0), 0.2, -54.7757322486, 147.6883149701)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.249977528, perimeter: 3.2825521233
            with BuildLine():
                CenterArc((0, 0), 0.2, -54.7757322486, 147.6883149701)
                Line((0.7480571005, 0.1086621183), (0.1153556736, -0.1633801352))
                CenterArc((1.1628113282, -0.8559512398), 1.05, 90, 23.266225175)
                Line((1.3527378097, 0.1940487602), (1.1628113282, 0.1940487602))
                CenterArc((1.3527378097, 0.2190487602), 0.025, -90, 160.2243412506)
                Line((1.2926135398, 0.2672327671), (1.3611962639, 0.242574375))
                CenterArc((0.9373584607, -0.7208430542), 1.05, 70.2243412506, 28.2380963524)
                Line((-0.0101624535, 0.1997416445), (0.7828394181, 0.3177251263))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.415000072, perimeter: 6.7000000998
            with BuildLine():
                Line((0.8500000127, -2.4500000365), (-0.200000003, -2.4500000365))
                Line((0.8500000127, -0.1500000022), (0.8500000127, -2.4500000365))
                Line((-0.200000003, -0.1500000022), (0.8500000127, -0.1500000022))
                Line((-0.200000003, -2.4500000365), (-0.200000003, -0.1500000022))
            make_face()
        # TwoSides extrude, along=2.2, against=-0.7
        extrude(amount=2.2, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered shaft or spindle with an elongated cylindrical body that gradually narrows toward one end and features a small flange or shoulder at the opposite end.
def model_50777_2934de55_0000():
    """Model: Second Hand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((0, 0), 0.1, 177.6927365278, 184.7305964224)
                CenterArc((0, 0), 0.1, 2.4233329502, 175.2694035776)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2154269234, perimeter: 4.8248725291
            with BuildLine():
                Line((-0.0024542874, 2.4230360135), (0.0951832388, 0.1159316654))
                Line((-0.0954178971, 0.115738606), (-0.0024542874, 2.4230360135))
                CenterArc((0, 0), 0.15, 50.6130180545, 78.8900333691)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0113752209, perimeter: 0.7360432392
            with BuildLine():
                CenterArc((0, 0), 0.1, 2.4233329502, 175.2694035776)
                Line((0.0951832388, 0.1159316654), (0.0999105694, 0.004228253))
                CenterArc((0, 0), 0.15, 50.6130180545, 78.8900333691)
                Line((-0.09991893, 0.0040258462), (-0.0954178971, 0.115738606))
            make_face()
            # Profile area: 0.0278946873, perimeter: 1.2819666831
            with BuildLine():
                Line((-0.09991893, 0.0040258462), (-0.0954178971, 0.115738606))
                CenterArc((0, 0), 0.15, 129.5030514236, 281.1099666309)
                Line((0.0951832388, 0.1159316654), (0.0999105694, 0.004228253))
                CenterArc((0, 0), 0.1, 177.6927365278, 184.7305964224)
            make_face()
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((0, 0), 0.1, 177.6927365278, 184.7305964224)
                CenterArc((0, 0), 0.1, 2.4233329502, 175.2694035776)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a streamlined, oval-shaped disc or deflector component featuring a central elongated slot, radial structural ribs for reinforcement, and curved aerodynamic surfaces with a blue mesh texture indicating a lightweight or composite construction.
def model_50777_2934de55_0016():
    """Model: Watch Face v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.6743897705, perimeter: 21.9793801141
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 2), 0.2481269912, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -1.5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1934184468, perimeter: 1.5590278657
            with Locations((0, 2)):
                Circle(0.2481269912)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2400000072, perimeter: 2.0000000298
            with BuildLine():
                Line((-2.0000000298, 0.200000003), (-2.0000000298, -0.200000003))
                Line((-2.0000000298, -0.200000003), (-1.4000000209, -0.200000003))
                Line((-1.4000000209, -0.200000003), (-1.4000000209, 0.200000003))
                Line((-1.4000000209, 0.200000003), (-2.0000000298, 0.200000003))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved, slightly tapered body and rounded ends, featuring a smooth, hollow interior design suitable for housing or connecting components.
def model_50785_223bc784_0002():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4261.40989921, perimeter: 231.4097148634
            Circle(36.83)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 148.211937636, perimeter: 466.8092523969
            with BuildLine():
                CenterArc((0, 0), 37.465, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 36.83, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=120.65
        extrude(amount=120.65, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 150.7454750315, perimeter: 474.788897737
            with BuildLine():
                CenterArc((0, 0), 38.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 37.465, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=121.92
        extrude(amount=121.92, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal aerospace or mechanical component featuring a central hub with four radial arms or struts extending outward, likely serving as a structural support frame or mounting bracket with internal bracing elements.
def model_50821_9dfe2ba3_0007():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3875, perimeter: 18.0332447311
            with BuildLine():
                Line((0, -4.4), (3, -4.4))
                Line((3, -4.4), (3, -4.3))
                Line((2, -2.2), (3, -4.3))
                Line((0, -2.2), (2, -2.2))
                Line((0, -2.2), (0, -4.4))
            make_face()
            with BuildLine():
                Line((0.1, -4.3), (0.1, -2.45))
                Line((0.1, -2.45), (1.9, -2.45))
                Line((1.9, -2.45), (2.8, -4.3))
                Line((0.1, -4.3), (2.8, -4.3))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.3875, perimeter: 18.0332447311
            with BuildLine():
                Line((2, -2.2), (3, -0.1))
                Line((3, 0), (3, -0.1))
                Line((0, 0), (3, 0))
                Line((0, 0), (0, -2.2))
                Line((0, -2.2), (2, -2.2))
            make_face()
            with BuildLine():
                Line((0.1, -0.1), (0.1, -1.95))
                Line((0.1, -0.1), (2.8, -0.1))
                Line((1.9, -1.95), (2.8, -0.1))
                Line((0.1, -1.95), (1.9, -1.95))
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1.5
        extrude(amount=1.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3875, perimeter: 18.0332447311
            with BuildLine():
                Line((0, -4.4), (3, -4.4))
                Line((3, -4.4), (3, -4.3))
                Line((2, -2.2), (3, -4.3))
                Line((0, -2.2), (2, -2.2))
                Line((0, -2.2), (0, -4.4))
            make_face()
            with BuildLine():
                Line((0.1, -4.3), (0.1, -2.45))
                Line((0.1, -2.45), (1.9, -2.45))
                Line((1.9, -2.45), (2.8, -4.3))
                Line((0.1, -4.3), (2.8, -4.3))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.3875, perimeter: 18.0332447311
            with BuildLine():
                Line((2, -2.2), (3, -0.1))
                Line((3, 0), (3, -0.1))
                Line((0, 0), (3, 0))
                Line((0, 0), (0, -2.2))
                Line((0, -2.2), (2, -2.2))
            make_face()
            with BuildLine():
                Line((0.1, -0.1), (0.1, -1.95))
                Line((0.1, -0.1), (2.8, -0.1))
                Line((1.9, -1.95), (2.8, -0.1))
                Line((0.1, -1.95), (1.9, -1.95))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.1625, perimeter: 8.4073040611
            with BuildLine():
                Line((0.1, -4.3), (2.8, -4.3))
                Line((1.9, -2.45), (2.8, -4.3))
                Line((0.1, -2.45), (1.9, -2.45))
                Line((0.1, -4.3), (0.1, -2.45))
            make_face()
            # Profile area: 4.1625, perimeter: 8.4073040611
            with BuildLine():
                Line((0.1, -1.95), (1.9, -1.95))
                Line((1.9, -1.95), (2.8, -0.1))
                Line((0.1, -0.1), (2.8, -0.1))
                Line((0.1, -0.1), (0.1, -1.95))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2.2, 0)):
                Circle(0.4)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parabolic satellite dish antenna featuring an elliptical reflector surface with radial support ribs, a reinforced rim flange, and an integrated feed support structure for receiving or transmitting electromagnetic signals.
def model_50897_3be92e2f_0015():
    """Model: Front Wheel Hub v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.3197531067, perimeter: 21.9440246853
            Circle(3.4925)
        # OneSide extrude, distance=0.4445
        extrude(amount=0.4445)
    return part.part


# Description: This is a cylindrical tube or sleeve with a longitudinal slot running along its length and rolled/flanged edges at both ends.
def model_50897_3be92e2f_0028():
    """Model: Foot Pegs v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4543643519, perimeter: 30.921125693
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.38125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # Symmetric extrude, each_side=5.334
        extrude(amount=5.334, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or barrel component with a dark blue/navy finish, featuring a flat rectangular body that tapers into a rounded cylindrical end, with visible internal structural details and what appears to be a ribbed or threaded circular opening.
def model_50914_67b32535_0005():
    """Model: cpart6 v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24.8165568752, perimeter: 21.7354260359
            with BuildLine():
                Line((1.3863966938, 1.6163900617), (-3.6489819086, 6.4789986549))
                CenterArc((-4.8174566202, 5.2690076701), 1.6820854125, 46, 188)
                Line((-0.427024356, 0), (-5.8061616188, 3.9081719854))
                Line((-0.427024356, 0), (0.0300843892, 0))
                Line((0.0300843892, 0), (1.3863966938, 1.6163900617))
            make_face()
            # Profile area: 0.0471564308, perimeter: 1.0774673006
            with BuildLine():
                Line((-0.427024356, 0), (0.0300843892, 0))
                Line((-0.1430426582, -0.2063247806), (-0.427024356, 0))
                Line((-0.1430426582, -0.2063247806), (0.0300843892, 0))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.3664545004, perimeter: 16.6361717207
            with BuildLine():
                Line((0, 0), (1.7320508076, 1))
                Line((1.7320508076, 1), (-3.00519889, 4.9750244741))
                CenterArc((-3.6092216636, 4.2551781637), 0.9396926208, 50, 180)
                Line((0, 0), (-4.2132444372, 3.5353318533))
            make_face()
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered hexagonal prism (coffin/casket shape) with a hinged or removable lid, featuring a narrower shoulder section that widens slightly toward the foot end, typical of a burial casket design.
def model_50947_49287c16_0001():
    """Model: Socket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4348205389, perimeter: 14.661897765
            with BuildLine():
                Line((2.5399999619, 0.2890510031), (-2.5399999619, 0.2890510031))
                Line((2.5399999619, 2.5399999619), (2.5399999619, 0.2890510031))
                Line((-2.5399999619, 2.5399999619), (2.5399999619, 2.5399999619))
                Line((-2.5399999619, 0.2890510031), (-2.5399999619, 2.5399999619))
            make_face()
        # OneSide extrude, distance=-13.97
        extrude(amount=-13.97)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -13.97), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.32258, perimeter: 3.048
            with BuildLine():
                Line((-1.2699999809, 1.9049999809), (-1.2699999809, 0.6349999809))
                Line((-1.2699999809, 0.6349999809), (-1.0159999809, 0.6349999809))
                Line((-1.0159999809, 0.6349999809), (-1.0159999809, 1.9049999809))
                Line((-1.0159999809, 1.9049999809), (-1.2699999809, 1.9049999809))
            make_face()
            # Profile area: 0.32258, perimeter: 3.048
            with BuildLine():
                Line((0.9239291176, 1.9508929372), (0.9239291176, 0.6808929372))
                Line((0.9239291176, 0.6808929372), (1.1779291176, 0.6808929372))
                Line((1.1779291176, 0.6808929372), (1.1779291176, 1.9508929372))
                Line((1.1779291176, 1.9508929372), (0.9239291176, 1.9508929372))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular boat or hull-shaped container with a trapezoidal top surface, featuring internal ribbed or webbed structural supports and what appears to be internal compartments or dividers.
def model_51022_47816098_0000():
    """Model: lower part fix"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((-5, 2.5), (0, 2.5))
                Line((-5, 0), (-5, 2.5))
                Line((0, 0), (-5, 0))
                Line((0, 2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((2.5, 0), 1.25, 0, 180)
                Line((1.25, 0), (3.75, 0))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, tapered channel or tray with a curved top surface, angled side walls, and a central longitudinal groove or slot running the full length, featuring a narrower bottom section designed to mount or guide components.
def model_51022_47816098_0003():
    """Model: upper part fix"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.0228539613, perimeter: 11.7898410752
            with BuildLine():
                Line((5, 0), (5, 0.8))
                CenterArc((2.5, -4.1083333333), 5.5083333333, 63.0085334384, 53.9829331232)
                Line((0, 0), (0, 0.8))
                Line((5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.2723450247, perimeter: 4.6274333882
            with BuildLine():
                CenterArc((-2.5, 0), 0.9, 0, 180)
                Line((-3.4, 0), (-1.6, 0))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered or textured top end, featuring a simple hollow tubular form tilted at an angle.
def model_51345_4b292361_0006():
    """Model: Grip v1"""
    with BuildPart() as part:
        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7530749408, perimeter: 20.4281132299
            with BuildLine():
                EllipticalCenterArc((0, 0), 1.8528745684, 1.1000000164, 0, 360, -180)
            make_face()
            with BuildLine():
                Line((0.3, -0.25), (0.3, -1))
                Line((0.3, -1), (-0.3, -1))
                Line((-0.3, -1), (-0.3, -0.25))
                Line((-1.75, -0.25), (-0.3, -0.25))
                Line((-1.75, 0.25), (-1.75, -0.25))
                Line((-0.3, 0.25), (-1.75, 0.25))
                Line((-0.3, 0.25), (-0.3, 1))
                Line((-0.3, 1), (0.3, 1))
                Line((0.3, 1), (0.3, 0.25))
                Line((1.75, 0.25), (0.3, 0.25))
                Line((1.75, -0.25), (1.75, 0.25))
                Line((0.3, -0.25), (1.75, -0.25))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.7530749408, perimeter: 20.4281132299
            with BuildLine():
                EllipticalCenterArc((0, 0), 1.8528745684, 1.1000000164, 0, 360, 0)
            make_face()
            with BuildLine():
                Line((0.3, 1), (0.3, 0.25))
                Line((0.3, 0.25), (1.75, 0.25))
                Line((1.75, 0.25), (1.75, -0.25))
                Line((1.75, -0.25), (0.3, -0.25))
                Line((0.3, -0.25), (0.3, -1))
                Line((0.3, -1), (-0.3, -1))
                Line((-0.3, -1), (-0.3, -0.25))
                Line((-0.3, -0.25), (-1.75, -0.25))
                Line((-1.75, -0.25), (-1.75, 0.25))
                Line((-1.75, 0.25), (-0.3, 0.25))
                Line((-0.3, 0.25), (-0.3, 1))
                Line((-0.3, 1), (0.3, 1))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.65, perimeter: 11
            with BuildLine():
                Line((-0.3, 1), (0.3, 1))
                Line((-0.3, 0.25), (-0.3, 1))
                Line((-1.75, 0.25), (-0.3, 0.25))
                Line((-1.75, -0.25), (-1.75, 0.25))
                Line((-0.3, -0.25), (-1.75, -0.25))
                Line((-0.3, -1), (-0.3, -0.25))
                Line((0.3, -1), (-0.3, -1))
                Line((0.3, -0.25), (0.3, -1))
                Line((1.75, -0.25), (0.3, -0.25))
                Line((1.75, 0.25), (1.75, -0.25))
                Line((0.3, 0.25), (1.75, 0.25))
                Line((0.3, 1), (0.3, 0.25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow core, featuring a rounded hemispherical dome on one end and a flat base on the opposite end, with a mesh or lattice pattern visible on its upper surface.
def model_51509_fd5fcb9c_0003():
    """Model: Engine-008"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.851020977, perimeter: 17.4195657775
            with BuildLine():
                CenterArc((-6.8580002189, -33.7820010781), 2.29616, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6.8580002189, -33.7820010781), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=3.175
        extrude(amount=3.175, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.175), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.0860591982, perimeter: 6.1602862026
            with BuildLine():
                CenterArc((6.8580002189, -33.7820010781), 0.50419, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.8580002189, -33.7820010781), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.127, trim=-0.07366
        extrude(amount=-0.127, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.07366, mode=Mode.ADD)
    return part.part


# Description: This is a torus or ring-shaped component with a smooth, curved profile featuring a central axial hole and radial fins or blade-like extensions around its circumference, suggesting an aerodynamic or fluid-dynamic application such as a turbine impeller or cooling fan.
def model_51559_4293c0e0_0003():
    """Model: distanziale v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.5301944847, perimeter: 41.154863762
            with BuildLine():
                CenterArc((0, 0), 4.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2594023781, perimeter: 26.0752190248
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a mesh-reinforced elastic band or belt with an oval/elliptical toroidal shape, featuring a solid dark core material wrapped with a blue mesh or fabric reinforcement layer on its outer surface.
def model_51559_4293c0e0_0004():
    """Model: ghiera1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.8123883775, perimeter: 29.5309709437
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3241504118, perimeter: 2.3942790473
            with BuildLine():
                Line((-0.4082724528, -2.7195245181), (-0.4082724528, -2.3452531236))
                CenterArc((0, 0), 2.75, -98.5378488618, 17.1846273325)
                Line((0.4134420184, -2.3452531236), (0.4134420184, -2.7187434041))
                Line((-0.4082724528, -2.3452531236), (0.4134420184, -2.3452531236))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth, uniform circular cross-section and rounded ends, featuring a slight taper or chamfer at both the top and bottom edges.
def model_51559_4293c0e0_0007():
    """Model: cilindro v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7255526112, perimeter: 8.4823001647
            Circle(1.35)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.316924582, perimeter: 18.5353966562
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue rectangular duct or channel component with a trapezoidal cross-section, featuring an oval hole through its center and internal ribbing or bracing for structural support.
def model_51585_b695905b_0009():
    """Model: Seal_Walls"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 64, perimeter: 128
            with BuildLine():
                Line((-1, 11), (21, 11))
                Line((-1, -1), (-1, 11))
                Line((21, -1), (-1, -1))
                Line((21, 11), (21, -1))
            make_face()
            with BuildLine():
                Line((0, 0), (0, 10))
                Line((0, 10), (20, 10))
                Line((20, 10), (20, 0))
                Line((20, 0), (0, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.6
        extrude(amount=6.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((10, -3.375)):
                Circle(2.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve component with an elongated oval opening or slot running along its length, featuring a solid base section and a mesh/lattice upper portion.
def model_51586_2ad96f8c_0001():
    """Model: Macro Lens v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8384126711, perimeter: 9.5818575782
            with BuildLine():
                CenterArc((0, 0), 0.8500000127, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6749999849, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2042035134, perimeter: 8.1681407168
            with BuildLine():
                CenterArc((0, 0), 0.6749999849, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.624999986, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344278, perimeter: 6.5973444251
            with BuildLine():
                CenterArc((0, 0), 0.624999986, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4249999905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a flat parallelogram plate or panel with a slight 3D depth, featuring a uniform thickness and beveled or chamfered edges along its perimeter.
def model_51593_174d44c2_0006():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 464.5152, perimeter: 86.36
            with BuildLine():
                Line((20.32, -22.86), (0, -22.86))
                Line((20.32, 0), (20.32, -22.86))
                Line((0, 0), (20.32, 0))
                Line((0, -22.86), (0, 0))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a VR headset or virtual reality goggle featuring a curved front face with mesh ventilation panels on the sides, dual cylindrical eye pieces extending forward, and an adjustable head strap structure in the back.
def model_51601_2616f89b_0006():
    """Model: plug v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2671458676, perimeter: 10.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.75, -90, 180)
                Line((0, 0.75), (-3, 0.75))
                CenterArc((-3, 0), 0.75, 90, 180)
                Line((-3, -0.75), (0, -0.75))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-3, 0)):
                Circle(0.2)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a curved structural bracket or support beam with two cylindrical end caps connected by a flat base platform, featuring internal ribbed reinforcement and a gentle upward curve along its length.
def model_51602_42da13f0_0007():
    """Model: Clipper v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1840044843, perimeter: 2.665916849
            with BuildLine():
                Line((0, 0.1599999964), (-0.3210527358, 0.2242105463))
                CenterArc((-0.5760037219, -1.05054433), 1.3, 78.6900670569, 33.1113424295)
                Line((-1.0588116012, 0.1564753682), (-1.0794702247, 0.1482119188))
                CenterArc((-1.0701854578, 0.1250000015), 0.025, 111.8014094864, 158.1985905136)
                Line((-1.0701854578, 0.1000000015), (-0.980824646, 0.1000000015))
                CenterArc((-0.980824646, -1.3999999985), 1.5, 68.79208289, 21.20791711)
                Line((-0.4381945538, -0.0015892638), (-0.0578805419, -0.1491638084))
                CenterArc((0, 0), 0.1599999964, 90, 158.79208289)
            make_face()
            # Profile area: 0.0725707867, perimeter: 1.319468892
            with BuildLine():
                CenterArc((0, 0), 0.1599999964, 90, 158.79208289)
                CenterArc((0, 0), 0.1599999964, -111.20791711, 201.20791711)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.2800000381, perimeter: 4.8000000715
            with BuildLine():
                Line((1.8000000268, -0.1000000015), (1.8000000268, 0.7000000104))
                Line((1.8000000268, 0.7000000104), (0.200000003, 0.7000000104))
                Line((0.200000003, 0.7000000104), (0.200000003, -0.1000000015))
                Line((1.8000000268, -0.1000000015), (0.200000003, -0.1000000015))
            make_face()
            # Profile area: 1.2800000381, perimeter: 4.8000000715
            with BuildLine():
                Line((1.8000000268, -0.1000000015), (0.200000003, -0.1000000015))
                Line((0.200000003, -0.1000000015), (0.200000003, -0.9000000134))
                Line((0.200000003, -0.9000000134), (1.8000000268, -0.9000000134))
                Line((1.8000000268, -0.9000000134), (1.8000000268, -0.1000000015))
            make_face()
        # TwoSides extrude, along=1.6, against=-1.5
        extrude(amount=1.6, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a disc or wheel-shaped component with an elongated elliptical/oval profile featuring radial ribs or fins extending from a central hub, commonly used in automotive or mechanical applications for structural rigidity and weight reduction.
def model_51602_42da13f0_0016():
    """Model: Watch Face Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.01, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1200000036, perimeter: 1.4000000209
            with BuildLine():
                Line((-1.6000000238, 0.1000000015), (-1.2000000179, 0.1000000015))
                Line((-1.6000000238, -0.200000003), (-1.6000000238, 0.1000000015))
                Line((-1.2000000179, -0.200000003), (-1.6000000238, -0.200000003))
                Line((-1.2000000179, 0.1000000015), (-1.2000000179, -0.200000003))
            make_face()
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with two flanged ends and a mesh or perforated central section, designed to join or transition between two circular components while allowing flow or visibility through its hollow center.
def model_51606_b72fa3d6_0007():
    """Model: Handle Pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4940398439, perimeter: 5.1867695729
            with BuildLine():
                CenterArc((0, 0), 0.5080000162, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.079375
        extrude(amount=0.079375, mode=Mode.ADD)
    return part.part


# Description: This is a curved rectangular panel or shroud with a pronounced cylindrical cutout in the center and horizontal ribbing or striations across its surface, likely designed as a ventilation cover or decorative component.
def model_51606_b72fa3d6_0023():
    """Model: Height Lock Plastic Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0561313471, perimeter: 2.6594927452
            with BuildLine():
                CenterArc((-0.9807821165, 0.635), 1.1684, -32.9207345281, 65.8414690562)
                Line((0, 1.190625), (0, 1.27))
                CenterArc((-1.0278323888, 0.635), 1.1684, -28.3947417411, 56.7894834823)
                Line((0, 0), (0, 0.079375))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.3175, 0.635)):
                Circle(0.15875)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with rounded rectangular ends, featuring a hollow central bore and smooth curved surfaces throughout.
def model_51674_a70c1c6c_0002():
    """Model: Button v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            Circle(0.275)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flashlight or torch assembly consisting of a cylindrical barrel with a polygonal reflector head featuring a mesh lens, designed to direct and focus light output.
def model_51723_ab02be01_0000():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 4.0594940802, perimeter: 7.5
            with BuildLine():
                Line((0.625, 1.0825317547), (1.25, 0))
                Line((-0.625, 1.0825317547), (0.625, 1.0825317547))
                Line((-1.25, 0), (-0.625, 1.0825317547))
                Line((-0.625, -1.0825317547), (-1.25, 0))
                Line((0.625, -1.0825317547), (-0.625, -1.0825317547))
                Line((1.25, 0), (0.625, -1.0825317547))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)
    return part.part


# Description: This is a hammer or mallet with a cylindrical handle and a large hemispherical striking head, designed for impact applications.
def model_51731_22e19a47_0033():
    """Model: sruba  duza10 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.43
        extrude(amount=1.43)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.43), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6597344573, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.32
        extrude(amount=0.32, mode=Mode.ADD)
    return part.part


# Description: This is a complex 3D bracket or mounting component featuring a trapezoidal overall shape with two large oval/elliptical cutout holes through its center, reinforced ribs on the sides, and flanged edges for fastening or assembly purposes.
def model_51736_e8b2b138_0006():
    """Model: Counter Blade v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.25, perimeter: 2.9236067977
            with BuildLine():
                Line((1, -0.3), (0, -0.3))
                Line((1.2, -0.2), (1, -0.3))
                Line((0.7, -0.2), (1.2, -0.2))
                Line((0.7, 0), (0.7, -0.2))
                Line((0, 0), (0.7, 0))
                Line((0, -0.3), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.32, 0.5)):
                Circle(0.3)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mobile device holder with a central rectangular blue mounting plate featuring adjustment slots, four black rubber grip pads positioned at the corners, and a dark frame structure designed to securely clamp and stabilize a smartphone or tablet.
def model_51736_e8b2b138_0007():
    """Model: Anvil v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9893807017, perimeter: 15.6265482457
            with BuildLine():
                CenterArc((4.5, 4), 0.8, 180, 90)
                Line((3.7, 4), (0.8, 4))
                CenterArc((0, 4), 0.8, -90, 90)
                Line((0, 3.2), (0, 0.8))
                CenterArc((0, 0), 0.8, 0, 90)
                Line((0.8, 0), (3.7, 0))
                CenterArc((4.5, 0), 0.8, 90, 90)
                Line((4.5, 0.8), (4.5, 3.2))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1178097245, perimeter: 2.5561944902
            with BuildLine():
                Line((0, 0.8), (0, 0.7))
                CenterArc((0, 0), 0.7, 0, 90)
                Line((0.7, 0), (0.8, 0))
                CenterArc((0, 0), 0.8, 0, 90)
            make_face()
            # Profile area: 0.3534291735, perimeter: 7.2685834706
            with BuildLine():
                CenterArc((0, 0), 0.8, 90, 270)
                Line((0.7, 0), (0.8, 0))
                CenterArc((0, 0), 0.7, 90, 270)
                Line((0, 0.8), (0, 0.7))
            make_face()
            # Profile area: 0.1178097245, perimeter: 2.5561944902
            with BuildLine():
                Line((3.7, 0), (3.8, 0))
                CenterArc((4.5, 0), 0.7, 90, 90)
                Line((4.5, 0.7), (4.5, 0.8))
                CenterArc((4.5, 0), 0.8, 90, 90)
            make_face()
            # Profile area: 0.3534291735, perimeter: 7.2685834706
            with BuildLine():
                CenterArc((4.5, 0), 0.8, -180, 270)
                Line((4.5, 0.7), (4.5, 0.8))
                CenterArc((4.5, 0), 0.7, -180, 270)
                Line((3.7, 0), (3.8, 0))
            make_face()
            # Profile area: 0.3534291735, perimeter: 7.2685834706
            with BuildLine():
                Line((4.5, 3.2), (4.5, 3.3))
                CenterArc((4.5, 4), 0.8, -90, 270)
                Line((3.8, 4), (3.7, 4))
                CenterArc((4.5, 4), 0.7, -90, 270)
            make_face()
            # Profile area: 0.1178097245, perimeter: 2.5561944902
            with BuildLine():
                CenterArc((4.5, 4), 0.7, 180, 90)
                Line((3.8, 4), (3.7, 4))
                CenterArc((4.5, 4), 0.8, 180, 90)
                Line((4.5, 3.2), (4.5, 3.3))
            make_face()
            # Profile area: 0.1178097245, perimeter: 2.5561944902
            with BuildLine():
                Line((0.8, 4), (0.7, 4))
                CenterArc((0, 4), 0.7, -90, 90)
                Line((0, 3.3), (0, 3.2))
                CenterArc((0, 4), 0.8, -90, 90)
            make_face()
            # Profile area: 0.3534291735, perimeter: 7.2685834706
            with BuildLine():
                CenterArc((0, 4), 0.8, 0, 270)
                Line((0, 3.3), (0, 3.2))
                CenterArc((0, 4), 0.7, 0, 270)
                Line((0.8, 4), (0.7, 4))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9056622572, perimeter: 5.5801987049
            with BuildLine():
                CenterArc((0, 0), 0.7, 90, 270)
                Line((0.325, 0), (0.7, 0))
                CenterArc((0, 0), 0.325, 90, 270)
                Line((0, 0.7), (0, 0.325))
            make_face()
            # Profile area: 0.3018874191, perimeter: 2.360066235
            with BuildLine():
                Line((0, 0.7), (0, 0.325))
                CenterArc((0, 0), 0.325, 0, 90)
                Line((0.325, 0), (0.7, 0))
                CenterArc((0, 0), 0.7, 0, 90)
            make_face()
            # Profile area: 0.9056622572, perimeter: 5.5801987049
            with BuildLine():
                CenterArc((4.5, 0), 0.7, -180, 270)
                Line((4.5, 0.325), (4.5, 0.7))
                CenterArc((4.5, 0), 0.325, -180, 270)
                Line((3.8, 0), (4.175, 0))
            make_face()
            # Profile area: 0.3018874191, perimeter: 2.360066235
            with BuildLine():
                Line((3.8, 0), (4.175, 0))
                CenterArc((4.5, 0), 0.325, 90, 90)
                Line((4.5, 0.325), (4.5, 0.7))
                CenterArc((4.5, 0), 0.7, 90, 90)
            make_face()
            # Profile area: 0.3018874191, perimeter: 2.360066235
            with BuildLine():
                CenterArc((4.5, 4), 0.325, 180, 90)
                Line((4.175, 4), (3.8, 4))
                CenterArc((4.5, 4), 0.7, 180, 90)
                Line((4.5, 3.3), (4.5, 3.675))
            make_face()
            # Profile area: 0.9056622572, perimeter: 5.5801987049
            with BuildLine():
                Line((4.5, 3.3), (4.5, 3.675))
                CenterArc((4.5, 4), 0.7, -90, 270)
                Line((4.175, 4), (3.8, 4))
                CenterArc((4.5, 4), 0.325, -90, 270)
            make_face()
            # Profile area: 0.3018874191, perimeter: 2.360066235
            with BuildLine():
                Line((0.7, 4), (0.325, 4))
                CenterArc((0, 4), 0.325, -90, 90)
                Line((0, 3.675), (0, 3.3))
                CenterArc((0, 4), 0.7, -90, 90)
            make_face()
            # Profile area: 0.9056622572, perimeter: 5.5801987049
            with BuildLine():
                CenterArc((0, 4), 0.7, 0, 270)
                Line((0, 3.675), (0, 3.3))
                CenterArc((0, 4), 0.325, 0, 270)
                Line((0.7, 4), (0.325, 4))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a curved duct or airflow component featuring a sharp 90-degree bend with triangulated mesh reinforcement sections, smooth curved surfaces, and open passages designed for air or fluid flow through an industrial ventilation or HVAC system.
def model_51736_e8b2b138_0014():
    """Model: Stroking jaw v5"""
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
        # Sketch has 27 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.5195201107, perimeter: 18.7748077541
            with BuildLine():
                Line((0, 4.9899392994), (-2.5, 4.9899392994))
                _nurbs_edge([(-5.7, 1.5), (-5.7, 1.5766993177), (-5.6901987486, 1.7208218867), (-5.6460922202, 1.9091768577), (-5.5341867422, 2.1091709811), (-5.3382317574, 2.299603807), (-5.1269480693, 2.4628942826), (-4.9391269027, 2.6301833507), (-4.8026691833, 2.8243819141), (-4.7221510261, 3.0505087309), (-4.6817435315, 3.2979937114), (-4.6555411027, 3.5487564334), (-4.6154877427, 3.783435156), (-4.5398225764, 3.9880112234), (-4.4223825617, 4.1611624002), (-4.2680836845, 4.3101899831), (-4.0865861708, 4.4454045024), (-3.8872809871, 4.5756672594), (-3.6725104076, 4.7022508539), (-3.4370313674, 4.8186465792), (-3.1718391248, 4.9145411656), (-2.9276993885, 4.9657160904), (-2.7227820874, 4.9855351469), (-2.5759620666, 4.9899392994), (-2.5, 4.9899392994)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-5.7, 0.4899392994), (-5.7, 1.5))
                Line((-4.3, 0.4899392994), (-5.7, 0.4899392994))
                Line((-4.3, 0.4899392994), (-4.8, 0.9899392994))
                Line((-4.8, 0.9899392994), (-3.6452994616, 2.9899392994))
                Line((-3.6452994616, 2.9899392994), (0, 2.9899392994))
                Line((0, 2.9899392994), (0, 4.9899392994))
            make_face()
            # Profile area: 11.5195201107, perimeter: 18.7748077541
            with BuildLine():
                Line((4.3, 0.4899392994), (5.7, 0.4899392994))
                Line((5.7, 0.4899392994), (5.7, 1.5))
                _nurbs_edge([(5.7, 1.5), (5.7, 1.5766993177), (5.6901987486, 1.7208218867), (5.6460922202, 1.9091768577), (5.5341867422, 2.1091709811), (5.3382317574, 2.299603807), (5.1269480693, 2.4628942826), (4.9391269027, 2.6301833507), (4.8026691833, 2.8243819141), (4.7221510261, 3.0505087309), (4.6817435315, 3.2979937114), (4.6555411027, 3.5487564334), (4.6154877427, 3.783435156), (4.5398225764, 3.9880112234), (4.4223825617, 4.1611624002), (4.2680836845, 4.3101899831), (4.0865861708, 4.4454045024), (3.8872809871, 4.5756672594), (3.6725104076, 4.7022508539), (3.4370313674, 4.8186465792), (3.1718391248, 4.9145411656), (2.9276993885, 4.9657160904), (2.7227820874, 4.9855351469), (2.5759620666, 4.9899392994), (2.5, 4.9899392994)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 4.9899392994), (2.5, 4.9899392994))
                Line((0, 2.9899392994), (0, 4.9899392994))
                Line((3.6452994616, 2.9899392994), (0, 2.9899392994))
                Line((4.8, 0.9899392994), (3.6452994616, 2.9899392994))
                Line((4.3, 0.4899392994), (4.8, 0.9899392994))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a angled bracket or mounting arm with a bent L-shape, featuring a textured/ribbed lower section and a smooth upper extension, designed to support or position components at an offset angle.
def model_51747_3d58eae0_0004():
    """Model: Side handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1.5, 5.5), (1.5, 4.5))
                Line((1.5, 4.5), (2, 4.5))
                Line((2, 4.5), (2, 5.5))
                Line((1.5, 5.5), (2, 5.5))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0, 0), (0, 1))
                Line((0, 0), (0.5, 0))
                Line((0.5, 1), (0.5, 0))
                Line((0, 1), (0.5, 1))
            make_face()
            # Profile area: 1.7910429119, perimeter: 10.7057858766
            with BuildLine():
                CenterArc((-6, 5.5), 7.5, -36.8698976458, 36.8698976458)
                Line((0, 1), (0.5, 1))
                CenterArc((-4.9119048967, 5.2166667632), 6.8606846016, -37.9238142223, 31.0873583027)
                CenterArc((2, 4.4000000283), 0.0999999717, 90, 89.9999786556)
                Line((1.5, 4.5), (2, 4.5))
                Line((1.5, 5.5), (1.5, 4.5))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((5, 0)):
                Circle(0.3000000045)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform diameter and slightly tapered or rounded ends, displayed at an angle.
def model_51775_49ef614a_0008():
    """Model: teleskop2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flanged shaft or coupling component featuring a large circular flanged disk on one end connected to a cylindrical shaft body, with parallel slots or grooves running along the shaft portion.
def model_51775_49ef614a_0011():
    """Model: sruba_gora"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a hollow tubular body, featuring rounded ends and what appears to be shallow slots or grooves running along its length.
def model_51775_49ef614a_0019():
    """Model: szklo_zarowki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal duct connector/coupling with a tapered, funnel-like shape featuring mesh or perforated panels on the upper portion and solid walls on the lower section, designed to transition between different duct sizes.
def model_51775_49ef614a_0020():
    """Model: Obudowa_gorna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72.7118067861, perimeter: 31.9317115881
            with BuildLine():
                CenterArc((2.9993404099, 0.0544767871), 1.5, -4.7636416907, 6.1510172566)
                CenterArc((0.75, 0), 3.75, 1.3873755659, 177.2252488683)
                CenterArc((-1.4993404099, 0.0544767871), 1.5, 178.6126244341, 6.1510172566)
                Line((-2.9941590473, -0.0700914326), (-2.5017271209, -5.9792745495))
                CenterArc((-0.8583832773, -5.8583066929), 1.6477900991, -175.7900048466, 80.8597272434)
                Line((-1, -7.5), (2.5, -7.5))
                CenterArc((2.3583832773, -5.8583066929), 1.6477900991, -85.0697223968, 80.8597272434)
                Line((4.4941590473, -0.0700914326), (4.0017271209, -5.9792745495))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1.7502, 6.7000000998)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.2502, 6.7000000998)):
                Circle(0.4)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_45285_dc1f2b6f_0004": {"func": model_45285_dc1f2b6f_0004, "volume": 146.7771652098, "area": 228.2988785559},
    "model_45359_1768ab3f_0012": {"func": model_45359_1768ab3f_0012, "volume": 0.0333008821, "area": 0.6031857895},
    "model_45359_1768ab3f_0013": {"func": model_45359_1768ab3f_0013, "volume": 0.081681409, "area": 1.0681415022},
    "model_45359_1768ab3f_0017": {"func": model_45359_1768ab3f_0017, "volume": 0.3663097034, "area": 4.9769110818},
    "model_45359_1768ab3f_0029": {"func": model_45359_1768ab3f_0029, "volume": 0.8340928495, "area": 8.7650435035},
    "model_45359_1768ab3f_0042": {"func": model_45359_1768ab3f_0042, "volume": 1.8130518457, "area": 12.7717559412},
    "model_45359_1768ab3f_0046": {"func": model_45359_1768ab3f_0046, "volume": 1.3829511667, "area": 14.2039370727},
    "model_45360_cb4bac3f_0012": {"func": model_45360_cb4bac3f_0012, "volume": 44.7512833662, "area": 147.1979628347},
    "model_45360_cb4bac3f_0026": {"func": model_45360_cb4bac3f_0026, "volume": 4.4346554593, "area": 20.5099031292},
    "model_45422_51de0379_0000": {"func": model_45422_51de0379_0000, "volume": 6057.7384406667, "area": 9131.885556175},
    "model_45423_34ff78aa_0000": {"func": model_45423_34ff78aa_0000, "volume": 7051.4401816091, "area": 9599.7022935949},
    "model_45427_4036cb2f_0000": {"func": model_45427_4036cb2f_0000, "volume": 6114.2743856835, "area": 9593.8815097708},
    "model_45429_70a5f94e_0000": {"func": model_45429_70a5f94e_0000, "volume": 6773.5006809903, "area": 10211.1689983934},
    "model_45430_2b0c8a5a_0000": {"func": model_45430_2b0c8a5a_0000, "volume": 5231.6470746044, "area": 8597.4172844696},
    "model_45434_ab3cf909_0000": {"func": model_45434_ab3cf909_0000, "volume": 6225.3750620965, "area": 9704.0908976859},
    "model_45468_eaf0dc99_0006": {"func": model_45468_eaf0dc99_0006, "volume": 107.9474679153, "area": 472.0509199943},
    "model_45551_7a11fc5b_0003": {"func": model_45551_7a11fc5b_0003, "volume": 441.7864669111, "area": 382.8816046563},
    "model_45593_25a4e479_0000": {"func": model_45593_25a4e479_0000, "volume": 7.3626771039, "area": 56.8927436403},
    "model_45797_78875e5a_0003": {"func": model_45797_78875e5a_0003, "volume": 228.4267104844, "area": 1015.673371875},
    "model_45798_b573e9da_0001": {"func": model_45798_b573e9da_0001, "volume": 0.2796017485, "area": 2.8902652928},
    "model_45798_b573e9da_0003": {"func": model_45798_b573e9da_0003, "volume": 3.4001496677, "area": 26.1444649578},
    "model_45912_c3b84cd3_0000": {"func": model_45912_c3b84cd3_0000, "volume": 147.6753281681, "area": 842.9570819015},
    "model_45922_26941172_0001": {"func": model_45922_26941172_0001, "volume": 4.5505291077, "area": 20.2805773999},
    "model_45922_26941172_0004": {"func": model_45922_26941172_0004, "volume": 2.2866097619, "area": 11.9177203399},
    "model_45922_26941172_0005": {"func": model_45922_26941172_0005, "volume": 3.1023227454, "area": 109.9714508389},
    "model_46016_d699e580_0002": {"func": model_46016_d699e580_0002, "volume": 96, "area": 248},
    "model_46016_d699e580_0005": {"func": model_46016_d699e580_0005, "volume": 1978.6835690148, "area": 1388.3043977761},
    "model_46086_371b5052_0005": {"func": model_46086_371b5052_0005, "volume": 0.4848824271, "area": 7.8999972315},
    "model_47894_f13353fd_0000": {"func": model_47894_f13353fd_0000, "volume": 5.4099234384, "area": 19.3880272555},
    "model_47994_ef70ce54_0000": {"func": model_47994_ef70ce54_0000, "volume": 1.7088685226, "area": 21.6960636933},
    "model_48224_53cae924_0009": {"func": model_48224_53cae924_0009, "volume": 3232.4574399139, "area": 1536.9131654748},
    "model_48224_53cae924_0010": {"func": model_48224_53cae924_0010, "volume": 727.7433086787, "area": 774.9500750927},
    "model_48224_53cae924_0011": {"func": model_48224_53cae924_0011, "volume": 15845.9221845292, "area": 6598.8370161096},
    "model_48224_53cae924_0017": {"func": model_48224_53cae924_0017, "volume": 5592.3832230783, "area": 14714.3365702784},
    "model_48224_53cae924_0018": {"func": model_48224_53cae924_0018, "volume": 6044.0706052283, "area": 16581.1756896937},
    "model_48332_fb679f90_0001": {"func": model_48332_fb679f90_0001, "volume": 16.5653117486, "area": 83.5533067266},
    "model_48724_70685a9d_0008": {"func": model_48724_70685a9d_0008, "volume": 3618.8495559215, "area": 2490.8495559215},
    "model_48907_25974aa4_0000": {"func": model_48907_25974aa4_0000, "volume": 18.3382199681, "area": 75.7526006673},
    "model_48917_591188ed_0000": {"func": model_48917_591188ed_0000, "volume": 0.0018827837, "area": 0.1595976532},
    "model_49016_cd1b47bf_0000": {"func": model_49016_cd1b47bf_0000, "volume": 146.4745430999, "area": 298.6608661262},
    "model_49017_b6231068_0006": {"func": model_49017_b6231068_0006, "volume": 2.4334076557, "area": 12.0255895644},
    "model_49017_b6231068_0011": {"func": model_49017_b6231068_0011, "volume": 0.7814711756, "area": 6.6444684698},
    "model_49019_748c9a9f_0009": {"func": model_49019_748c9a9f_0009, "volume": 665.1075101064, "area": 831.3843876331},
    "model_49019_748c9a9f_0011": {"func": model_49019_748c9a9f_0011, "volume": 14.7262155637, "area": 119.7732199181},
    "model_49019_748c9a9f_0013": {"func": model_49019_748c9a9f_0013, "volume": 1.2440706908, "area": 10.3672557568},
    "model_49024_b7f02205_0017": {"func": model_49024_b7f02205_0017, "volume": 32.7282885025, "area": 166.0995608762},
    "model_49145_4a5b250e_0009": {"func": model_49145_4a5b250e_0009, "volume": 0.1115334525, "area": 2.2955529126},
    "model_49215_5368e45e_0000": {"func": model_49215_5368e45e_0000, "volume": 5.728296743, "area": 38.1056710853},
    "model_49330_c6744767_0011": {"func": model_49330_c6744767_0011, "volume": 0.6525067028, "area": 5.9128739457},
    "model_49400_c5be6ea9_0000": {"func": model_49400_c5be6ea9_0000, "volume": 11.780972451, "area": 100.1382658332},
    "model_49412_1f199584_0000": {"func": model_49412_1f199584_0000, "volume": 297.3114178558, "area": 457.8977847322},
    "model_49503_e42c01c0_0002": {"func": model_49503_e42c01c0_0002, "volume": 35.2985296188, "area": 115.8185392428},
    "model_49503_e42c01c0_0005": {"func": model_49503_e42c01c0_0005, "volume": 5.0678690188, "area": 34.4666946296},
    "model_49562_6df35938_0000": {"func": model_49562_6df35938_0000, "volume": 0.3093331098, "area": 3.5733310982},
    "model_49562_6df35938_0007": {"func": model_49562_6df35938_0007, "volume": 0.6295000583, "area": 13.4916823024},
    "model_49600_4c47092d_0000": {"func": model_49600_4c47092d_0000, "volume": 178.8369118713, "area": 559.4248970677},
    "model_49613_1b97c07b_0003": {"func": model_49613_1b97c07b_0003, "volume": 1.7474127909, "area": 17.8237657236},
    "model_49613_1b97c07b_0010": {"func": model_49613_1b97c07b_0010, "volume": 132.7322896142, "area": 287.4557278035},
    "model_49695_28e7f7e5_0001": {"func": model_49695_28e7f7e5_0001, "volume": 796.8461992392, "area": 654.7559469505},
    "model_49703_b92021be_0015": {"func": model_49703_b92021be_0015, "volume": 2794.2417140402, "area": 2718.624464005},
    "model_49703_b92021be_0016": {"func": model_49703_b92021be_0016, "volume": 97.5555482079, "area": 132.2771521952},
    "model_49909_13b120dd_0000": {"func": model_49909_13b120dd_0000, "volume": 13926.9908169872, "area": 4127.8759594744},
    "model_50001_e86a6698_0003": {"func": model_50001_e86a6698_0003, "volume": 96.1792515064, "area": 171.7654592594},
    "model_50001_e86a6698_0007": {"func": model_50001_e86a6698_0007, "volume": 270.2777693506, "area": 273.6220387126},
    "model_50001_e86a6698_0011": {"func": model_50001_e86a6698_0011, "volume": 566.2962786394, "area": 445.9025816058},
    "model_50036_7766eac1_0006": {"func": model_50036_7766eac1_0006, "volume": 166.5180036574, "area": 394.9348057979},
    "model_50214_683032e0_0001": {"func": model_50214_683032e0_0001, "volume": 3.1445146507, "area": 38.3247817207},
    "model_50214_683032e0_0002": {"func": model_50214_683032e0_0002, "volume": 152.9528761097, "area": 189.9424778008},
    "model_50214_683032e0_0004": {"func": model_50214_683032e0_0004, "volume": 60.4214017175, "area": 124.5773741962},
    "model_50214_683032e0_0007": {"func": model_50214_683032e0_0007, "volume": 4.9363162832, "area": 59.5389618326},
    "model_50315_0f1419bf_0007": {"func": model_50315_0f1419bf_0007, "volume": 0.4351459352, "area": 6.1396933717},
    "model_50379_ebec8fae_0000": {"func": model_50379_ebec8fae_0000, "volume": 395.2385167453, "area": 395.0139511227},
    "model_50382_cb85058c_0004": {"func": model_50382_cb85058c_0004, "volume": 17.1530958886, "area": 114.9822911214},
    "model_50409_4a322fbf_0001": {"func": model_50409_4a322fbf_0001, "volume": 0.0000340162, "area": 0.0066225482},
    "model_50409_4a322fbf_0010": {"func": model_50409_4a322fbf_0010, "volume": 0.0000484203, "area": 0.00860108},
    "model_50479_a1f097b3_0002": {"func": model_50479_a1f097b3_0002, "volume": 4.325, "area": 19},
    "model_50479_a1f097b3_0010": {"func": model_50479_a1f097b3_0010, "volume": 0.5585672545, "area": 5.3945194558},
    "model_50585_06c574f3_0010": {"func": model_50585_06c574f3_0010, "volume": 447.6438055098, "area": 711.2831853072},
    "model_50681_eb7a9f92_0012": {"func": model_50681_eb7a9f92_0012, "volume": 16.020000299, "area": 82.684737115},
    "model_50681_eb7a9f92_0013": {"func": model_50681_eb7a9f92_0013, "volume": 0.2460468742, "area": 5.4348939853},
    "model_50777_2934de55_0000": {"func": model_50777_2934de55_0000, "volume": 0.0388214519, "area": 1.2647334565},
    "model_50777_2934de55_0016": {"func": model_50777_2934de55_0016, "volume": 1.7821226657, "area": 37.6535544347},
    "model_50785_223bc784_0002": {"func": model_50785_223bc784_0002, "volume": 38966.6538776251, "area": 66378.6797617722},
    "model_50821_9dfe2ba3_0007": {"func": model_50821_9dfe2ba3_0007, "volume": 16.1473451754, "area": 104.098134387},
    "model_50897_3be92e2f_0015": {"func": model_50897_3be92e2f_0015, "volume": 17.0331302559, "area": 86.3936251861},
    "model_50897_3be92e2f_0028": {"func": model_50897_3be92e2f_0028, "volume": 33.1664388562, "area": 425.3891939424},
    "model_50914_67b32535_0005": {"func": model_50914_67b32535_0005, "volume": 16.6273386226, "area": 103.7171462434},
    "model_50947_49287c16_0001": {"func": model_50947_49287c16_0001, "volume": 158.9250897285, "area": 235.4382728547},
    "model_51022_47816098_0000": {"func": model_51022_47816098_0000, "volume": 80.3650459151, "area": 151.5071880147},
    "model_51022_47816098_0003": {"func": model_51022_47816098_0003, "volume": 47.5050893662, "area": 137.6737625077},
    "model_51345_4b292361_0006": {"func": model_51345_4b292361_0006, "volume": 40.732286878, "area": 221.8013387955},
    "model_51509_fd5fcb9c_0003": {"func": model_51509_fd5fcb9c_0003, "volume": 100.6493928066, "area": 142.4977669918},
    "model_51559_4293c0e0_0003": {"func": model_51559_4293c0e0_0003, "volume": 19.6184607235, "area": 147.4820671228},
    "model_51559_4293c0e0_0004": {"func": model_51559_4293c0e0_0004, "volume": 11.6503131716, "area": 53.5280843213},
    "model_51559_4293c0e0_0007": {"func": model_51559_4293c0e0_0007, "volume": 36.4715345137, "area": 291.5712141797},
    "model_51585_b695905b_0009": {"func": model_51585_b695905b_0009, "volume": 402.7650459151, "area": 949.2380550981},
    "model_51586_2ad96f8c_0001": {"func": model_51586_2ad96f8c_0001, "volume": 0.5464408323, "area": 7.9757185326},
    "model_51593_174d44c2_0006": {"func": model_51593_174d44c2_0006, "volume": 325.16064, "area": 989.4824},
    "model_51601_2616f89b_0006": {"func": model_51601_2616f89b_0006, "volume": 6.6441369917, "area": 27.0165919281},
    "model_51602_42da13f0_0007": {"func": model_51602_42da13f0_0007, "volume": 0.1267216178, "area": 3.0985166048},
    "model_51602_42da13f0_0016": {"func": model_51602_42da13f0_0016, "volume": 0.1244637061, "area": 25.0324049279},
    "model_51606_b72fa3d6_0007": {"func": model_51606_b72fa3d6_0007, "volume": 0.2654513847, "area": 3.141586482},
    "model_51606_b72fa3d6_0023": {"func": model_51606_b72fa3d6_0023, "volume": 0.0319182944, "area": 1.6892571814},
    "model_51674_a70c1c6c_0002": {"func": model_51674_a70c1c6c_0002, "volume": 0.1211476667, "area": 2.3876104167},
    "model_51723_ab02be01_0000": {"func": model_51723_ab02be01_0000, "volume": 9.734578324, "area": 33.329606253},
    "model_51731_22e19a47_0033": {"func": model_51731_22e19a47_0033, "volume": 0.4310265121, "area": 4.3730969738},
    "model_51736_e8b2b138_0006": {"func": model_51736_e8b2b138_0006, "volume": 0.1651769984, "area": 3.4236067977},
    "model_51736_e8b2b138_0007": {"func": model_51736_e8b2b138_0007, "volume": 11.5021459581, "area": 66.7230510286},
    "model_51736_e8b2b138_0014": {"func": model_51736_e8b2b138_0014, "volume": 138.234219173, "area": 247.3757871003},
    "model_51747_3d58eae0_0004": {"func": model_51747_3d58eae0_0004, "volume": 3.6392729536, "area": 23.942738561},
    "model_51775_49ef614a_0008": {"func": model_51775_49ef614a_0008, "volume": 1.4686945656, "area": 52.9201282497},
    "model_51775_49ef614a_0011": {"func": model_51775_49ef614a_0011, "volume": 0.0691150384, "area": 1.2095131716},
    "model_51775_49ef614a_0019": {"func": model_51775_49ef614a_0019, "volume": 1.9854865571, "area": 20.6088478075},
    "model_51775_49ef614a_0020": {"func": model_51775_49ef614a_0020, "volume": 253.9886689269, "area": 259.6978782533},
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
