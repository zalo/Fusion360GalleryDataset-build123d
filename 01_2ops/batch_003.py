"""Batch 003 - passing/01_2ops
148 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_128996_b5ff8312_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=1.05
        extrude(amount=1.05)
    return part.part


def model_128996_b8d06bf2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_128996_bc7c82e0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7815999463, perimeter: 22.4181266827
            with BuildLine():
                CenterArc((0, 0), 1.2000000179, 0, 180)
                CenterArc((-6.3250001721, -1.5000000305), 5.3400024974, -16.313851593, 32.627703869)
                CenterArc((0, -3), 1.2, 180, 180)
                CenterArc((6.3250001721, -1.5000000305), 5.3400024974, 163.686147724, 32.627703869)
            make_face()
            with BuildLine():
                CenterArc((0, -3), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_128996_be3a6361_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2)
    return part.part


def model_128996_ccc5fb94_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=12.3
        extrude(amount=12.3)
    return part.part


def model_128996_ce71b660_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.7871660368, perimeter: 165.2477735788
            with BuildLine():
                CenterArc((0, 0), 13.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_128996_d895c690_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=9.3
        extrude(amount=9.3)
    return part.part


def model_128996_de0fca55_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9845130209, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_128996_decf48a5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5634954085, perimeter: 27.253981634
            with BuildLine():
                Line((0, 0), (0, -0.5))
                Line((0, -0.5), (4.6, -0.5))
                CenterArc((4.6, 1), 1.5, -90, 180)
                Line((4.6, 2.5), (0, 2.5))
                Line((0, 2), (0, 2.5))
                Line((4.6, 2), (0, 2))
                CenterArc((4.6, 1), 1, -90, 180)
                Line((0, 0), (4.6, 0))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_128996_e660b876_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


def model_129696_aac1f710_0000():
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
        # Sketch has 26 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3652743229, perimeter: 52.2482534706
            with BuildLine():
                Line((-1.7207720223, 2.1769350917), (-1.720772022, 1.9328871852))
                _nurbs_edge([(-1.7207720223, 2.1769350917), (-1.6845253836, 2.1793555087), (-1.6111555688, 2.1871686519), (-1.5029639808, 2.2074904418), (-1.3665948796, 2.2503134229), (-1.2179852753, 2.3256986971), (-1.0984724725, 2.4193826988), (-1.0150962829, 2.527029729), (-0.9705199588, 2.646195811), (-0.9663544154, 2.7496386242), (-0.9807669625, 2.8315102939), (-0.9981125634, 2.8879842014), (-1.0087197073, 2.9166943495)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4693103842, 0.4693103842, 0.4693103842, 0.4693103842, 0.4693103842, 0.4693103842, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.0087197073, 2.9166943495), (-2.957318457, 2.9166943495))
                _nurbs_edge([(-2.957318457, 2.9166943495), (-2.9280202113, 2.8724475719), (-2.8684780562, 2.7871271286), (-2.7763278325, 2.6686657573), (-2.6477456202, 2.5298946027), (-2.4775083409, 2.3892129783), (-2.2982515828, 2.2823148807), (-2.1457467524, 2.2233343531), (-2.0282413466, 2.195298691), (-1.9484649792, 2.183734516), (-1.9070595594, 2.1796741733), (-1.9040218356, 2.1793867145)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4052783728, 0.4052783728, 0.4052783728, 0.4052783728, 0.4052783728, 0.4052783728], 5)
                Line((-1.9040218356, 2.1793867145), (-1.9040218236, 1.9488299912))
                _nurbs_edge([(-3.3020001054, 2.7940000892), (-3.2808917665, 2.7564255011), (-3.2358406665, 2.6829807767), (-3.1597608337, 2.5779270183), (-3.0411903019, 2.4481565463), (-2.8642426629, 2.3038164907), (-2.6593183035, 2.1786851155), (-2.4290364508, 2.074813766), (-2.2260461619, 2.0100642621), (-2.0682556478, 1.9742070379), (-1.9616364696, 1.9565238924), (-1.9069761153, 1.9492196079), (-1.9040218236, 1.9488299912)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.4704763229, 0.4704763229, 0.4704763229, 0.4704763229, 0.4704763229, 0.4704763229], 5)
                Line((-4.0640001297, 2.5400000811), (-3.3020001054, 2.7940000892))
                Line((-4.0640001297, -1.0160000324), (-4.0640001297, 2.5400000811))
                _nurbs_edge([(0.4455964125, 0.4181505737), (0.3883598862, 0.4270220896), (0.2579913671, 0.44616574), (0.055339826, 0.4720553791), (-0.2181588642, 0.4983208911), (-0.5605751601, 0.5144975764), (-0.9153004667, 0.5097364363), (-1.267204967, 0.4796475911), (-1.6170954658, 0.4202318826), (-1.965821111, 0.3276537029), (-2.3141642222, 0.1987503686), (-2.662708388, 0.031882969), (-3.011802959, -0.1729855939), (-3.3616406906, -0.4151282015), (-3.6421678517, -0.6378325363), (-3.8529389595, -0.8207731989), (-3.99361878, -0.9497542934), (-4.0640001297, -1.0160000324)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1480161485, 0.1480161485, 0.1480161485, 0.1480161485, 0.1480161485, 0.1480161485, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((0.4455964125, 0.4181505737), (0.4455964117, 0.2096687702))
                _nurbs_edge([(0.4455964117, 0.2096687702), (0.4167822446, 0.2138563101), (0.3189744276, 0.2272582783), (0.1494100838, 0.2458386328), (-0.0969442362, 0.2617791697), (-0.4262312288, 0.2632983997), (-0.8090837518, 0.2393854134), (-1.1959952065, 0.1895366538), (-1.5786605484, 0.1134702028), (-1.9474743837, 0.0108343446), (-2.2920769046, -0.1188809007), (-2.6019375308, -0.2763897333), (-2.8669244546, -0.4627442672), (-3.0779062039, -0.6791862564), (-3.2273597905, -0.9257181103), (-3.3100583988, -1.1997316588), (-3.323680134, -1.4947581766), (-3.2697577699, -1.7986536324), (-3.1527981887, -2.0952422601), (-2.9788993769, -2.3669700412), (-2.7546249762, -2.5970942998), (-2.4857130896, -2.7723155244), (-2.176159499, -2.8845436297), (-1.8286223198, -2.9293580018), (-1.5214331789, -2.909880789), (-1.2749559225, -2.8640504143), (-1.1035070976, -2.8196568788), (-1.0160000324, -2.7940000892)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1031698372, 0.1031698372, 0.1031698372, 0.1031698372, 0.1031698372, 0.1031698372, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.0160000324, -2.7940000892), (-1.0518063749, -2.7602413712), (-1.1204307596, -2.6911380864), (-1.2144024768, -2.5827255719), (-1.3216948822, -2.4286218861), (-1.4251458816, -2.2203528459), (-1.4967015305, -1.9977082934), (-1.5344910305, -1.7635347747), (-1.5359282479, -1.5229460953), (-1.4977198636, -1.2839020027), (-1.416829397, -1.0557352865), (-1.2914386044, -0.847796569), (-1.1219386542, -0.6680837294), (-0.9120654765, -0.5217687258), (-0.6698580528, -0.4099101743), (-0.4060006722, -0.3306978605), (-0.1324625258, -0.280417491), (0.1389833391, -0.2544804981), (0.3478512717, -0.2494994726), (0.4959439781, -0.2532266299), (0.5906263014, -0.2587791311), (0.6374759493, -0.2623553806), (0.6389043368, -0.2624652071)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.8515736743, 0.8515736743, 0.8515736743, 0.8515736743, 0.8515736743, 0.8515736743], 5)
                Line((0.6389043368, -0.2624652071), (0.6389043372, -0.6072178606))
                _nurbs_edge([(0.6389043372, -0.6072178606), (0.6144524322, -0.60772411), (0.5613056047, -0.6094577785), (0.4802069492, -0.6143593208), (0.3725543133, -0.6262679983), (0.2408986758, -0.6528287381), (0.1104245138, -0.6970182105), (-0.0132271872, -0.7629033737), (-0.1283567141, -0.8547358741), (-0.2330333856, -0.9748970525), (-0.3251462201, -1.1227777859), (-0.4024548793, -1.2931850063), (-0.4626767755, -1.4772133332), (-0.5035966842, -1.6638793665), (-0.5231813846, -1.8414165944), (-0.519727355, -1.9987492731), (-0.4919945422, -2.1267519128), (-0.4394498179, -2.220025807), (-0.3775629967, -2.2650919818), (-0.3200712364, -2.2820624181), (-0.2768408565, -2.2859288047), (-0.2540000081, -2.286000073)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1577540641, 0.1577540641, 0.1577540641, 0.1577540641, 0.1577540641, 0.1577540641, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.2540000081, -2.286000073), (-0.2468973357, -2.2618712128), (-0.23089839, -2.2152276218), (-0.2015190617, -2.1501046451), (-0.1515074857, -2.0730290363), (-0.0707331906, -1.993358786), (0.0280331178, -1.9308612017), (0.1436074959, -1.8859437133), (0.2732229933, -1.8586498329), (0.4122382188, -1.8485012052), (0.5550458579, -1.8547497044), (0.6956935601, -1.8764976757), (0.8286092899, -1.9128056883), (0.9492311211, -1.9627519922), (1.0548743315, -2.0254490417), (1.1443463179, -2.1001227041), (1.2027484591, -2.1689723197), (1.239208749, -2.2255707759), (1.2602761754, -2.2654921307), (1.2700000405, -2.286000073)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(1.2700000405, -2.286000073), (1.3076541851, -2.2734622208), (1.3819199407, -2.2477244426), (1.4901911678, -2.2071316764), (1.628193411, -2.1489693754), (1.7893536903, -2.0690632858), (1.9380701249, -1.9812545757), (2.0731808762, -1.8848054048), (2.1938107302, -1.7791599574), (2.300159921, -1.6644453947), (2.3931541036, -1.5412495657), (2.4576644117, -1.4364152844), (2.5008288623, -1.3544756386), (2.5273233108, -1.2984000892), (2.5400000811, -1.2700000405)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((2.5400000811, -1.2700000405), (2.3420801697, -1.1068987444))
                Line((2.3420801697, -1.1068987444), (2.5126357685, -0.688236726))
                _nurbs_edge([(2.5126357685, -0.688236726), (2.5075460984, -0.6994992591), (2.4910760134, -0.7343626987), (2.4610052362, -0.7898509058), (2.4131226071, -0.8603051277), (2.3411586348, -0.9371455414), (2.2474717454, -1.0046091613), (2.141489421, -1.0530424674), (2.0250801483, -1.082340205), (1.9016072766, -1.0930440342), (1.7753058651, -1.0860900403), (1.6507171479, -1.0626190755), (1.5321173748, -1.023832493), (1.4229704174, -0.9708900376), (1.3252653491, -0.9048477192), (1.2398907572, -0.8265811318), (1.1816253814, -0.7547024737), (1.1435161152, -0.6957543467), (1.120576381, -0.6542321943), (1.1097231226, -0.6329152648)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0356372602, 0.0356372602, 0.0356372602, 0.0356372602, 0.0356372602, 0.0356372602, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(1.1097231226, -0.6329152648), (1.0790205225, -0.6292257793), (1.0263528286, -0.623414743), (0.9740796754, -0.6185435343), (0.9222024423, -0.6146153263), (0.8707294784, -0.6116581179), (0.8492048454, -0.6105915263)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.0861436723, 0.0861436723, 0.0861436723, 0.0861436723, 0.0861436723, 0.0861436723], 5)
                Line((0.8492048061, -0.2860627207), (0.8492048454, -0.6105915263))
                _nurbs_edge([(0.8492048061, -0.2860627207), (0.8895537685, -0.2921473566), (0.9681367, -0.3056514179), (1.0417353554, -0.3216789769), (1.1103065115, -0.3401645442), (1.1738695468, -0.3610976548), (1.2045198185, -0.372224351)], [1, 1, 1, 1, 1, 1, 1], [0.9004107336, 0.9004107336, 0.9004107336, 0.9004107336, 0.9004107336, 0.9004107336, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((1.2700000405, 0), (1.2045198185, -0.372224351))
                _nurbs_edge([(1.2700000405, 0), (1.2106915968, 0.0225185985), (1.0902791632, 0.0651379155), (0.9652885742, 0.1032222511), (0.8366398289, 0.1363806803), (0.7043667823, 0.1645798065), (0.6367987276, 0.1775260246), (0.6357396382, 0.1777285956)], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.080636824, 0.080636824, 0.080636824, 0.080636824, 0.080636824, 0.080636824], 5)
                Line((0.6357396429, 0.3866571497), (0.6357396382, 0.1777285956))
                _nurbs_edge([(1.2700000405, 0.2540000081), (1.1948856588, 0.2721177867), (1.0672471945, 0.3017187523), (0.9401621663, 0.3291662276), (0.8136339901, 0.3544467859), (0.687667684, 0.3775130097), (0.6357396429, 0.3866571497)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.113571974, 0.113571974, 0.113571974, 0.113571974, 0.113571974, 0.113571974], 5)
                _nurbs_edge([(2.8386385801, -0.1622283244), (2.8519661458, -0.1331904915), (2.8756291015, -0.0756346846), (2.9021467897, 0.0091396276), (2.9194215905, 0.1190290496), (2.9103554117, 0.2506632161), (2.8704840609, 0.3753054931), (2.8005740094, 0.4906478097), (2.7032367672, 0.5928766458), (2.5827119633, 0.6769850109), (2.4439253603, 0.7376017364), (2.2918639407, 0.7697102396), (2.1309016418, 0.7694827099), (1.9641711738, 0.7352194256), (1.7937661763, 0.6666582363), (1.6209617484, 0.5643563092), (1.4813254765, 0.4562235226), (1.3759233441, 0.3606858843), (1.3053574436, 0.2906237099), (1.2700000405, 0.2540000081)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((3.0480000973, 0.2789263011), (2.8386385801, -0.1622283244))
                Line((3.4190197922, 0.2789263011), (3.0480000973, 0.2789263011))
                Line((3.9842173629, 1.469878325), (3.4190197922, 0.2789263011))
                _nurbs_edge([(1.3575724266, 2.5258827728), (1.4138971894, 2.5137561327), (1.5262157735, 2.488717934), (1.6937008571, 2.4488059551), (1.9149957783, 2.3908024991), (2.1880217289, 2.3097771004), (2.4571332247, 2.2194674953), (2.7220097536, 2.1191135007), (2.9824744079, 2.0082955318), (3.2386993389, 1.8874218923), (3.4910034495, 1.7572489486), (3.6899669052, 1.6462802779), (3.8376724697, 1.559455727), (3.9354796081, 1.499999642), (3.9842173629, 1.469878325)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((1.9531448289, 2.5258827728), (1.3575724266, 2.5258827728))
                Line((0.7620000243, 2.9210000932), (1.9531448289, 2.5258827728))
                Line((-0.7620000243, 2.9210000932), (0.7620000243, 2.9210000932))
                _nurbs_edge([(-1.720772022, 1.9328871852), (-1.709195083, 1.9324215711), (-1.6470989146, 1.9304072449), (-1.5361835216, 1.931572627), (-1.3819207472, 1.9465147825), (-1.1983365285, 1.993129931), (-1.0186182108, 2.090724839), (-0.8824331014, 2.2318720918), (-0.7922603576, 2.4162142896), (-0.7572729502, 2.5975067104), (-0.7516684905, 2.752073099), (-0.7570384964, 2.8633234302), (-0.7620000243, 2.9210000932)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5181054138, 0.5181054138, 0.5181054138, 0.5181054138, 0.5181054138, 0.5181054138, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_129699_881b4b3a_0002():
    """Model: Outer Race"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9975803495, perimeter: 12.5679414107
            with BuildLine():
                CenterArc((0, 0), 1.0795, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.92075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_129854_5b7bfc38_0002():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 48.7139289629, perimeter: 25.9807621135
            with BuildLine():
                Line((3.75, -2.1650635095), (3.75, 2.1650635095))
                Line((3.75, 2.1650635095), (0, 4.3301270189))
                Line((0, 4.3301270189), (-3.75, 2.1650635095))
                Line((-3.75, 2.1650635095), (-3.75, -2.1650635095))
                Line((-3.75, -2.1650635095), (0, -4.3301270189))
                Line((0, -4.3301270189), (3.75, -2.1650635095))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_129941_4f0a8032_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 158.87065, perimeter: 130.81
            with BuildLine():
                Line((12.7, -25.4), (0, -25.4))
                Line((12.7, 0), (12.7, -25.4))
                Line((0, 0), (12.7, 0))
                Line((0, -25.4), (0, 0))
            make_face()
            with BuildLine():
                Line((10.795, -5.08), (1.905, -5.08))
                Line((10.795, -23.495), (10.795, -5.08))
                Line((1.905, -23.495), (10.795, -23.495))
                Line((1.905, -5.08), (1.905, -23.495))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)
    return part.part


def model_130459_57e34211_0000():
    """Model: wood table v2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2400, perimeter: 200
            with BuildLine():
                Line((72.6425453308, -46.6257295128), (12.6425453308, -46.6257295128))
                Line((72.6425453308, -6.6257295128), (72.6425453308, -46.6257295128))
                Line((12.6425453308, -6.6257295128), (72.6425453308, -6.6257295128))
                Line((12.6425453308, -46.6257295128), (12.6425453308, -6.6257295128))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_130540_e8c5e51b_0004():
    """Model: Clip Cutoff 180718 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8398952986, perimeter: 4.8450518782
            with BuildLine():
                CenterArc((-0.5, -0.25), 0.6, 24.6243183522, 310.7513632957)
                Line((-0.5, -0.5), (0.0454356057, -0.5))
                Line((-0.5, 0), (-0.5, -0.5))
                Line((0.0454356057, 0), (-0.5, 0))
            make_face()
            # Profile area: 0.4589219433, perimeter: 2.9248593061
            with BuildLine():
                CenterArc((-0.5, -0.25), 0.6, -24.6243183522, 49.2486367043)
                Line((0.0454356057, -0.5), (1, -0.5))
                Line((1, -0.5), (1, 0))
                Line((1, 0), (0.0454356057, 0))
            make_face()
            # Profile area: 0.2910780567, perimeter: 2.106601729
            with BuildLine():
                Line((0.0454356057, 0), (-0.5, 0))
                Line((-0.5, 0), (-0.5, -0.5))
                Line((-0.5, -0.5), (0.0454356057, -0.5))
                CenterArc((-0.5, -0.25), 0.6, -24.6243183522, 49.2486367043)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_130604_4f758677_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.72860322, perimeter: 55.6381376267
            with BuildLine():
                CenterArc((0, 0), 2, 0, 180)
                Line((-2, 0), (-2, -4))
                CenterArc((-2.5, -4), 0.5, -90, 90)
                Line((-2.5, -4.5), (-8.1109127035, -4.5))
                CenterArc((-8.1109127035, -2.5), 2, -135, 45)
                Line((-9.5251262658, -3.9142135624), (-12.4393398282, -1))
                Line((-12.4393398282, -1), (-13.5, -2.0606601718))
                Line((-13.5, -2.0606601718), (-10.5857864376, -4.9748737342))
                CenterArc((-8.1109127035, -2.5), 3.5, -135, 45)
                Line((-8.1109127035, -6), (0, -6))
                Line((0, -6), (6.5, -6))
                Line((6.5, -6), (6.5, -4.5))
                Line((6.5, -4.5), (2.5, -4.5))
                CenterArc((2.5, -4), 0.5, 180, 90)
                Line((2, -4), (2, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=5
        extrude(amount=2.5, both=True)
    return part.part


def model_130605_c596617d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 175.469383848, perimeter: 109.430638586
            with BuildLine():
                Line((11, 0), (8, 2))
                Line((8, 2), (4, 3.5))
                Line((4, 3.5), (0, 4))
                Line((-4, 3.5), (0, 4))
                Line((-8, 2), (-4, 3.5))
                Line((-11, 0), (-8, 2))
                CenterArc((0, 0), 11, 180, 74.1733798681)
                CenterArc((0, -10.5830052443), 3, 90, 90)
                CenterArc((0, -10.5830052443), 3, 0, 90)
                CenterArc((0, 0), 11, -74.1733798681, 74.1733798681)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0, -2.5830052443), (-7, -2.5830052443))
                Line((0, -2.5830052443), (7, -2.5830052443))
                Line((7, -2.5830052443), (7, -6.5830052443))
                Line((7, -6.5830052443), (2, -6.5830052443))
                CenterArc((0, -6.5830052443), 2, 0, 90)
                CenterArc((0, -6.5830052443), 2, 90, 90)
                Line((-7, -6.5830052443), (-2, -6.5830052443))
                Line((-7, -2.5830052443), (-7, -6.5830052443))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=3
        extrude(amount=1.5, both=True)
    return part.part


def model_130664_090d6ddd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 32 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.5474293303, perimeter: 44.3495565244
            with BuildLine():
                Line((0, 7.4), (0, 0))
                Line((0, 0), (6.6, 0))
                Line((6.6, 0), (6.6, 7.4))
                Line((6.6, 7.4), (0, 7.4))
            make_face()
            with BuildLine():
                CenterArc((3.3, 6.5), 0.255, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3, 0.89), 0.255, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 3.7), 0.255, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.6, 3.7), 0.255, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.1, 2.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.1, 1.65), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.15, 2.05), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.15, 3.2), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.55, 4.9999901688), (2.75, 4.9999901688))
                Line((4.55, 4.4999901688), (4.55, 4.9999901688))
                Line((4.55, 3.9999901688), (4.55, 4.4999901688))
                Line((2.75, 3.9999901688), (4.55, 3.9999901688))
                CenterArc((2.75, 4.4999901688), 0.5, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_130679_7a357a9c_0006():
    """Model: Component196"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.2000013046, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 82.386536556, perimeter: 36.7992470848
            with BuildLine():
                Line((-5.3499058964, 9.149905953), (5.3499058979, 9.149905953))
                Line((-5.3499058964, 1.4500942049), (-5.3499058964, 9.149905953))
                Line((5.3499058979, 1.4500942049), (-5.3499058964, 1.4500942049))
                Line((5.3499058979, 9.149905953), (5.3499058979, 1.4500942049))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_130679_7a357a9c_0008():
    """Model: Component209"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.3000004298, perimeter: 14.9999998972
            with BuildLine():
                Line((7.2000001073, 26.4000002474), (7.2000001073, 27.5000004098))
                Line((7.5000001118, 27.5000004098), (7.2000001073, 27.5000004098))
                Line((7.5000001118, 27.5000004098), (7.5000001118, 28.5000004247))
                Line((7.5000001118, 28.5000004247), (7.2000001073, 28.5000004247))
                Line((7.2000001073, 28.5000004247), (7.2000001073, 29.4000003189))
                Line((3.3000000492, 29.4000003189), (7.2000001073, 29.4000003189))
                Line((3.3000000492, 28.5000004247), (3.3000000492, 29.4000003189))
                Line((3.3000000492, 28.5000004247), (3, 28.5))
                Line((3.0000000447, 27.5000004098), (3, 28.5))
                Line((3.3000000492, 27.5000004098), (3.0000000447, 27.5000004098))
                Line((3.3000000492, 26.4000002474), (3.3000000492, 27.5000004098))
                Line((7.2000001073, 26.4000002474), (3.3000000492, 26.4000002474))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_130714_8b4a9662_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 89.350001405, perimeter: 75.434331815
            with BuildLine():
                Line((20.7788489942, 35.1771659075), (20.7788489942, 0))
                Line((20.7788489942, 0), (23.3188489942, 0))
                Line((23.3188489942, 0), (23.3188489942, 35.1771659075))
                Line((23.3188489942, 35.1771659075), (20.7788489942, 35.1771659075))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


def model_130719_e4764a36_0007():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((9, -1), (10, -1))
                Line((9, -2), (9, -1))
                Line((10, -2), (9, -2))
                Line((10, -1), (10, -2))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


def model_130757_2772bec8_0001():
    """Model: Wires"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on Profile plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.18), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-0.1200000026, -0.0000047854)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.1199999973, 0)):
                Circle(0.025)
        # TwoSides extrude, along=0.01, against=-0.88
        extrude(amount=0.01)
        extrude(sk.sketch, amount=-0.88)
    return part.part


def model_130757_3a6352fd_0006():
    """Model: Pin Inputs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.165), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.52, perimeter: 4.66
            with BuildLine():
                Line((-3.2075, -2.26979305), (-3.2075, -2.51979305))
                Line((-3.2075, -2.51979305), (-1.1275, -2.51979305))
                Line((-1.1275, -2.51979305), (-1.1275, -2.26979305))
                Line((-1.1275, -2.26979305), (-3.2075, -2.26979305))
            make_face()
            # Profile area: 0.6475, perimeter: 5.68
            with BuildLine():
                Line((-1.0275, -2.26979305), (-1.0275, -2.51979305))
                Line((-1.0275, -2.51979305), (1.5625, -2.51979305))
                Line((1.5625, -2.51979305), (1.5625, -2.26979305))
                Line((1.5625, -2.26979305), (-1.0275, -2.26979305))
            make_face()
            # Profile area: 0.3925, perimeter: 3.64
            with BuildLine():
                Line((-3.2125, 2.55479305), (-3.2125, 2.30479305))
                Line((-3.2125, 2.30479305), (-1.6425, 2.30479305))
                Line((-1.6425, 2.30479305), (-1.6425, 2.55479305))
                Line((-1.6425, 2.55479305), (-3.2125, 2.55479305))
            make_face()
            # Profile area: 0.52, perimeter: 4.66
            with BuildLine():
                Line((-1.4575, 2.55479305), (-1.4575, 2.30479305))
                Line((-1.4575, 2.30479305), (0.6225, 2.30479305))
                Line((0.6225, 2.30479305), (0.6225, 2.55479305))
                Line((0.6225, 2.55479305), (-1.4575, 2.55479305))
            make_face()
        # OneSide extrude, distance=0.855
        extrude(amount=0.855)
    return part.part


def model_130757_3a6352fd_0008():
    """Model: PCB"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 61 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 35.805457589, perimeter: 27.9765407099
            with BuildLine():
                CenterArc((-3.2525, 2.61479305), 0.05, 90, 90)
                Line((-3.3025, -2.61479305), (-3.3025, 2.61479305))
                CenterArc((-3.2525, -2.61479305), 0.05, -180, 90)
                Line((3.2525, -2.66479305), (-3.2525, -2.66479305))
                CenterArc((3.2525, -2.61479305), 0.05, -90, 90)
                Line((3.3025, -2.41479305), (3.3025, -2.61479305))
                Line((3.3025, -2.41479305), (3.5675, -2.17979305))
                Line((3.5675, 1.12520695), (3.5675, -2.17979305))
                Line((3.5675, 1.12520695), (3.3025, 1.36020695))
                Line((3.3025, 2.51479305), (3.3025, 1.36020695))
                Line((3.3025, 2.51479305), (3.1525, 2.66479305))
                Line((-3.2525, 2.66479305), (3.1525, 2.66479305))
            make_face()
            with BuildLine():
                CenterArc((3.3175, 0.88020695), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3175, -1.90979305), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.9125, -2.41479305), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7775, 2.41479305), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.165
        extrude(amount=0.165)
    return part.part


def model_130757_8bbd9729_0000():
    """Model: Button"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.28), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0989798035, perimeter: 1.115265392
            Circle(0.1775)
        # OneSide extrude, distance=0.135
        extrude(amount=0.135)
    return part.part


def model_130757_95d3cd06_0001():
    """Model: Pins"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((-0.095, -0.155), (-0.095, -0.095))
                Line((-0.095, -0.095), (-0.155, -0.095))
                Line((-0.155, -0.095), (-0.155, -0.155))
                Line((-0.155, -0.155), (-0.095, -0.155))
            make_face()
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((-0.095, 0.095), (-0.155, 0.095))
                Line((-0.095, 0.155), (-0.095, 0.095))
                Line((-0.155, 0.155), (-0.095, 0.155))
                Line((-0.155, 0.095), (-0.155, 0.155))
            make_face()
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((0.095, 0.155), (0.095, 0.095))
                Line((0.095, 0.095), (0.155, 0.095))
                Line((0.155, 0.095), (0.155, 0.155))
                Line((0.155, 0.155), (0.095, 0.155))
            make_face()
            # Profile area: 0.0036, perimeter: 0.24
            with BuildLine():
                Line((0.155, -0.095), (0.155, -0.155))
                Line((0.095, -0.095), (0.155, -0.095))
                Line((0.095, -0.155), (0.095, -0.095))
                Line((0.155, -0.155), (0.095, -0.155))
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35)
    return part.part


def model_130757_b2c47f8d_0003():
    """Model: Broadcom Block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.135), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.96, perimeter: 5.6
            with BuildLine():
                Line((0.85, 0.33), (2.25, 0.33))
                Line((0.85, -1.07), (0.85, 0.33))
                Line((2.25, -1.07), (0.85, -1.07))
                Line((2.25, 0.33), (2.25, -1.07))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_130757_b2c47f8d_0004():
    """Model: L1 & L2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.135), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.132, perimeter: 1.338634244
            with BuildLine():
                Line((3.135, 1.27), (3.345, 1.27))
                Line((3.06, 1.19), (3.135, 1.27))
                Line((3.06, 0.95), (3.06, 1.19))
                Line((3.135, 0.87), (3.06, 0.95))
                Line((3.345, 0.87), (3.135, 0.87))
                Line((3.42, 0.95), (3.345, 0.87))
                Line((3.42, 1.19), (3.42, 0.95))
                Line((3.345, 1.27), (3.42, 1.19))
            make_face()
            # Profile area: 0.132, perimeter: 1.338634244
            with BuildLine():
                Line((3.63, 2.02), (3.705, 2.1))
                Line((3.63, 1.78), (3.63, 2.02))
                Line((3.705, 1.7), (3.63, 1.78))
                Line((3.915, 1.7), (3.705, 1.7))
                Line((3.99, 1.78), (3.915, 1.7))
                Line((3.99, 2.02), (3.99, 1.78))
                Line((3.915, 2.1), (3.99, 2.02))
                Line((3.705, 2.1), (3.915, 2.1))
            make_face()
        # OneSide extrude, distance=0.175
        extrude(amount=0.175)
    return part.part


def model_130757_c4798e9b_0001():
    """Model: Back Piece"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 37 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0290351874, perimeter: 6.6435396656
            with BuildLine():
                Line((-0.435, -0.385), (-0.435, -0.95))
                Line((0.435, -0.95), (-0.435, -0.95))
                Line((0.435, -0.385), (0.435, -0.95))
                Line((0.52, -0.385), (0.435, -0.385))
                Line((0.52, -0.005), (0.52, -0.385))
                CenterArc((0.52, 0.06), 0.065, 90, 180)
                Line((0.52, 0.275), (0.52, 0.125))
                Line((-0.52, 0.275), (0.52, 0.275))
                Line((-0.52, 0.125), (-0.52, 0.275))
                CenterArc((-0.52, 0.06), 0.065, -90, 180)
                Line((-0.52, -0.385), (-0.52, -0.005))
                Line((-0.435, -0.385), (-0.52, -0.385))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.18, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.13, -0.335), (-0.13, -0.335))
                CenterArc((0.13, -0.385), 0.05, -90, 180)
                Line((-0.13, -0.435), (0.13, -0.435))
                CenterArc((-0.13, -0.385), 0.05, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.13
        extrude(amount=0.13)
    return part.part


def model_130850_227be64a_0001():
    """Model: uchwyt_1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5434758941, perimeter: 4.8851765763
            with BuildLine():
                CenterArc((-2.5, -2), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, -2), 0.2775, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_130996_b842b511_0003():
    """Model: Z Linear Rail"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9890522722, perimeter: 7.6591791044
            with BuildLine():
                CenterArc((-50.4382040958, -0.5976764922), 0.05, -180, 45.0000000001)
                Line((-50.4545389296, -0.6520523366), (-50.4735594349, -0.6330318313))
                CenterArc((-50.4191835905, -0.6166969975), 0.05, -134.9999999999, 34.2884054678)
                CenterArc((-50.4662075508, -0.8652885242), 0.203, 10.7115945268, 68.5768109464)
                CenterArc((-50.2176160241, -0.8182645639), 0.05, -169.2884054682, 34.2884054682)
                Line((-50.2112761569, -0.8953151092), (-50.2529713632, -0.853619903))
                Line((-48.7651320347, -0.8953151092), (-50.2112761569, -0.8953151092))
                Line((-48.7234368285, -0.853619903), (-48.7651320347, -0.8953151092))
                CenterArc((-48.7587921675, -0.8182645639), 0.05, -45, 34.2884054682)
                CenterArc((-48.5102006408, -0.8652885242), 0.203, 100.7115945268, 68.5768109464)
                CenterArc((-48.5572246011, -0.6166969975), 0.05, -79.2884054679, 34.2884054675)
                Line((-48.5028487568, -0.6330318313), (-48.5218692621, -0.6520523366))
                CenterArc((-48.5382040958, -0.5976764922), 0.05, -45, 45)
                Line((-48.4882040958, -0.4919537262), (-48.4882040958, -0.5976764922))
                CenterArc((-48.5382040958, -0.4919537262), 0.05, 0, 45.0000000023)
                Line((-48.5206697564, -0.4387773874), (-48.5028487568, -0.4565983871))
                CenterArc((-48.5560250955, -0.4741327265), 0.05, 45.0000000024, 34.564744487)
                CenterArc((-48.5102006408, -0.2253172942), 0.203, -169.5647444872, 69.1294889789)
                CenterArc((-48.7590160731, -0.2711417489), 0.05, 10.435255517, 34.564744485)
                Line((-48.7989147739, -0.16053237), (-48.723660734, -0.2357864099))
                CenterArc((-48.7282040958, -0.0898216919), 0.1, 180, 45.0000000024)
                Line((-48.8282040958, 0.0661914734), (-48.8282040958, -0.0898216919))
                CenterArc((-48.7282040958, 0.0661914734), 0.1, 134.9999999989, 45.0000000011)
                Line((-48.5174934177, 0.4183235078), (-48.7989147739, 0.1369021516))
                CenterArc((-48.5882040958, 0.4890341859), 0.1, -45.000000001, 45.000000001)
                Line((-48.4882040958, 0.7546848908), (-48.4882040958, 0.4890341859))
                Line((-48.5882040958, 0.8546848908), (-48.4882040958, 0.7546848908))
                Line((-50.3882040958, 0.8546848908), (-48.5882040958, 0.8546848908))
                Line((-50.4882040958, 0.7546848908), (-50.3882040958, 0.8546848908))
                Line((-50.4882040958, 0.4890341859), (-50.4882040958, 0.7546848908))
                CenterArc((-50.3882040958, 0.4890341859), 0.1, -180, 45.000000001)
                Line((-50.1774934177, 0.1369021516), (-50.4589147739, 0.4183235078))
                CenterArc((-50.2482040958, 0.0661914734), 0.1, 0, 45.0000000011)
                Line((-50.1482040958, -0.0898216919), (-50.1482040958, 0.0661914734))
                CenterArc((-50.2482040958, -0.0898216919), 0.1, -45.0000000023, 45.0000000023)
                Line((-50.2527474576, -0.2357864099), (-50.1774934177, -0.16053237))
                CenterArc((-50.2173921185, -0.2711417489), 0.05, 134.9999999977, 34.564744487)
                CenterArc((-50.4662075508, -0.2253172942), 0.203, -79.5647444921, 69.1294889789)
                CenterArc((-50.4203830961, -0.4741327265), 0.05, 100.4352555124, 34.5647444851)
                Line((-50.4735594349, -0.4565983871), (-50.4557384352, -0.4387773874))
                CenterArc((-50.4382040958, -0.4919537262), 0.05, 134.9999999976, 45.0000000024)
                Line((-50.4882040958, -0.5976764922), (-50.4882040958, -0.4919537262))
            make_face()
        # OneSide extrude, distance=44.7
        extrude(amount=44.7)
    return part.part


def model_130996_b842b511_0015():
    """Model: Parametric HGR20R Hiwin Rail v3 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9890522722, perimeter: 7.6591791044
            with BuildLine():
                CenterArc((-50.4382040958, -0.5976764922), 0.05, -180, 45.0000000001)
                Line((-50.4545389296, -0.6520523366), (-50.4735594349, -0.6330318313))
                CenterArc((-50.4191835905, -0.6166969975), 0.05, -134.9999999999, 34.2884054678)
                CenterArc((-50.4662075508, -0.8652885242), 0.203, 10.7115945268, 68.5768109464)
                CenterArc((-50.2176160241, -0.8182645639), 0.05, -169.2884054682, 34.2884054682)
                Line((-50.2112761569, -0.8953151092), (-50.2529713632, -0.853619903))
                Line((-48.7651320347, -0.8953151092), (-50.2112761569, -0.8953151092))
                Line((-48.7234368285, -0.853619903), (-48.7651320347, -0.8953151092))
                CenterArc((-48.7587921675, -0.8182645639), 0.05, -45, 34.2884054682)
                CenterArc((-48.5102006408, -0.8652885242), 0.203, 100.7115945268, 68.5768109464)
                CenterArc((-48.5572246011, -0.6166969975), 0.05, -79.2884054679, 34.2884054675)
                Line((-48.5028487568, -0.6330318313), (-48.5218692621, -0.6520523366))
                CenterArc((-48.5382040958, -0.5976764922), 0.05, -45, 45)
                Line((-48.4882040958, -0.4919537262), (-48.4882040958, -0.5976764922))
                CenterArc((-48.5382040958, -0.4919537262), 0.05, 0, 45.0000000023)
                Line((-48.5206697564, -0.4387773874), (-48.5028487568, -0.4565983871))
                CenterArc((-48.5560250955, -0.4741327265), 0.05, 45.0000000024, 34.564744487)
                CenterArc((-48.5102006408, -0.2253172942), 0.203, -169.5647444872, 69.1294889789)
                CenterArc((-48.7590160731, -0.2711417489), 0.05, 10.435255517, 34.564744485)
                Line((-48.7989147739, -0.16053237), (-48.723660734, -0.2357864099))
                CenterArc((-48.7282040958, -0.0898216919), 0.1, 180, 45.0000000024)
                Line((-48.8282040958, 0.0661914734), (-48.8282040958, -0.0898216919))
                CenterArc((-48.7282040958, 0.0661914734), 0.1, 134.9999999989, 45.0000000011)
                Line((-48.5174934177, 0.4183235078), (-48.7989147739, 0.1369021516))
                CenterArc((-48.5882040958, 0.4890341859), 0.1, -45.000000001, 45.000000001)
                Line((-48.4882040958, 0.7546848908), (-48.4882040958, 0.4890341859))
                Line((-48.5882040958, 0.8546848908), (-48.4882040958, 0.7546848908))
                Line((-50.3882040958, 0.8546848908), (-48.5882040958, 0.8546848908))
                Line((-50.4882040958, 0.7546848908), (-50.3882040958, 0.8546848908))
                Line((-50.4882040958, 0.4890341859), (-50.4882040958, 0.7546848908))
                CenterArc((-50.3882040958, 0.4890341859), 0.1, -180, 45.000000001)
                Line((-50.1774934177, 0.1369021516), (-50.4589147739, 0.4183235078))
                CenterArc((-50.2482040958, 0.0661914734), 0.1, 0, 45.0000000011)
                Line((-50.1482040958, -0.0898216919), (-50.1482040958, 0.0661914734))
                CenterArc((-50.2482040958, -0.0898216919), 0.1, -45.0000000023, 45.0000000023)
                Line((-50.2527474576, -0.2357864099), (-50.1774934177, -0.16053237))
                CenterArc((-50.2173921185, -0.2711417489), 0.05, 134.9999999977, 34.564744487)
                CenterArc((-50.4662075508, -0.2253172942), 0.203, -79.5647444921, 69.1294889789)
                CenterArc((-50.4203830961, -0.4741327265), 0.05, 100.4352555124, 34.5647444851)
                Line((-50.4735594349, -0.4565983871), (-50.4557384352, -0.4387773874))
                CenterArc((-50.4382040958, -0.4919537262), 0.05, 134.9999999976, 45.0000000024)
                Line((-50.4882040958, -0.5976764922), (-50.4882040958, -0.4919537262))
            make_face()
        # OneSide extrude, distance=156.5
        extrude(amount=156.5)
    return part.part


def model_131014_17cad022_0004():
    """Model: Cart v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.209675, perimeter: 4.445
            with BuildLine():
                Line((1.27, -0.9525), (0, -0.9525))
                Line((1.27, 0), (1.27, -0.9525))
                Line((0, 0), (1.27, 0))
                Line((0, -0.9525), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_131065_c82633e9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.585, perimeter: 8.1
            with BuildLine():
                Line((0, 0.15), (0, 0))
                Line((0, 0), (3.9, 0))
                Line((3.9, 0), (3.9, 0.15))
                Line((3.9, 0.15), (0, 0.15))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


def model_131066_7943a19c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.335, perimeter: 18.1
            with BuildLine():
                Line((0, 8.9), (0, 0))
                Line((0, 0), (0.15, 0))
                Line((0.15, 0), (0.15, 8.9))
                Line((0.15, 8.9), (0, 8.9))
            make_face()
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)
    return part.part


def model_131067_b78691f2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> 押し出し3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.54, perimeter: 25
            with BuildLine():
                Line((0, 8.6), (0, 0))
                Line((0, 0), (3.9, 0))
                Line((3.9, 0), (3.9, 8.6))
                Line((3.9, 8.6), (0, 8.6))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_131156_d1bee956_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 138.6150481491, perimeter: 111.2643849701
            with BuildLine():
                Line((-8.5021409833, -4.2826856), (8.4978547511, -4.2912011266))
                CenterArc((8.5, -0.0085274218), 4.2826742421, -90.0287002244, 180.0574004489)
                Line((-8.5021409833, 4.2656307564), (8.4978547511, 4.274146283))
                CenterArc((-8.5, -0.0085274218), 4.2741587145, 90.0287002244, 179.9425995511)
            make_face()
            with BuildLine():
                CenterArc((8.5, -0.0085274218), 2.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.5, -0.0085274218), 2.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6, -0.0085274218), 1.9, -90, 180)
                Line((-1.6, -1.9085274218), (1.6, -1.9085274218))
                CenterArc((-1.6, -0.0085274218), 1.9, 90, 180)
                Line((1.6, 1.8914725782), (-1.6, 1.8914725782))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_131355_3bb5668a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 98 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 117.424573306, perimeter: 45.4625523708
            with BuildLine():
                Line((-8.3017247877, 336.1824824896), (-8.3017247877, 344.1198329707))
                Line((6.4922009166, 336.1824824896), (-8.3017247877, 336.1824824896))
                Line((6.4922009166, 344.1198329707), (6.4922009166, 336.1824824896))
                Line((-8.3017247877, 344.1198329707), (6.4922009166, 344.1198329707))
            make_face()
            # Profile area: 117.424573306, perimeter: 45.4625523708
            with BuildLine():
                Line((-8.3017247877, 344.1198329707), (6.4922009166, 344.1198329707))
                Line((6.4922009166, 352.0571834517), (6.4922009166, 344.1198329707))
                Line((-8.3017247877, 352.0571834517), (6.4922009166, 352.0571834517))
                Line((-8.3017247877, 344.1198329707), (-8.3017247877, 352.0571834517))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_131425_0b7b5ce2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 964.8119222937, perimeter: 428.8052987972
            with BuildLine():
                CenterArc((-25, -12.5), 12.5, 180, 90)
                Line((25, -25), (-25, -25))
                CenterArc((25, -12.5), 12.5, -90, 90)
                Line((37.5, 12.5), (37.5, -12.5))
                CenterArc((25, 12.5), 12.5, 0, 90)
                Line((-25, 25), (25, 25))
                CenterArc((-25, 12.5), 12.5, 90, 90)
                Line((-37.5, -12.5), (-37.5, 12.5))
            make_face()
            with BuildLine():
                Line((-25, 20.5), (25, 20.5))
                CenterArc((25, 12.5), 8, 0, 90)
                Line((33, 12.5), (33, -12.5))
                CenterArc((25, -12.5), 8, -90, 90)
                Line((25, -20.5), (-25, -20.5))
                CenterArc((-25, -12.5), 8, 180, 90)
                Line((-33, -12.5), (-33, 12.5))
                CenterArc((-25, 12.5), 8, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_131463_e4a55cfe_0003():
    """Model: Side Panel v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.625, perimeter: 52.7
            with BuildLine():
                Line((23.85, -2.5), (0, -2.5))
                Line((23.85, 0), (23.85, -2.5))
                Line((0, 0), (23.85, 0))
                Line((0, -2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_131463_e4a55cfe_0004():
    """Model: Display Mockup Glass v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 454.5115926536, perimeter: 85.1831853072
            with BuildLine():
                CenterArc((1, -1), 1, 90, 90)
                Line((0, -24.8), (0, -1))
                CenterArc((1, -24.8), 1, 180, 90)
                Line((16.65, -25.8), (1, -25.8))
                CenterArc((16.65, -24.8), 1, -90, 90)
                Line((17.65, -1), (17.65, -24.8))
                CenterArc((16.65, -1), 1, 0, 90)
                Line((1, 0), (16.65, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_131463_e4a55cfe_0008():
    """Model: Cable Cover v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 150.875, perimeter: 52.5
            with BuildLine():
                Line((17.75, -8.5), (0, -8.5))
                Line((17.75, 0), (17.75, -8.5))
                Line((0, 0), (17.75, 0))
                Line((0, -8.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_131528_0743cfc4_0001():
    """Model: side2 v1"""
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
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9098948489, perimeter: 33.4324305395
            with BuildLine():
                _nurbs_edge([(3.5, 0.4083009887), (3.4755665527, 0.3966108857), (3.4272764779, 0.3739873406), (3.3565717431, 0.342322014), (3.2657637595, 0.3046461086), (3.1578232317, 0.2651353175), (3.0548126717, 0.2331902112), (2.9554007537, 0.2087409681), (2.8573896133, 0.1916335561), (2.7573311702, 0.1816183782), (2.6508542126, 0.1782606255), (2.5339595361, 0.1807355939), (2.4040300651, 0.1876672386), (2.2610565068, 0.1969116892), (2.1085623204, 0.2054417451), (1.9552224096, 0.2089814751), (1.8136684956, 0.2026751144), (1.6975412877, 0.1823917766), (1.6190230652, 0.1458801463), (1.5862822067, 0.0939072406), (1.6006659334, 0.0316198258), (1.6547914231, -0.0307897705), (1.7365957317, -0.082223723), (1.832457241, -0.1138938134), (1.9311056028, -0.1236607266), (2.0257381656, -0.1174100525), (2.11291942, -0.1049293078), (2.1921827031, -0.0969120045), (2.2653523876, -0.1016663912), (2.3360305611, -0.1215564751), (2.4085762751, -0.1542181892), (2.487018611, -0.194456961), (2.5740489915, -0.2358327054), (2.6698273105, -0.2725063324), (2.7725244948, -0.2994135451), (2.8790922302, -0.3122323661), (2.9859591016, -0.3074285591), (3.0897248085, -0.2822661465), (3.1879326497, -0.2348544617), (3.2789903554, -0.1640055855), (3.3619594099, -0.0690687538), (3.4215073072, 0.0263649657), (3.4622686082, 0.1089177943), (3.4877114639, 0.1688269444), (3.5000000522, 0.200000003)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5, 0.4083009887), (3.5, 0.75))
                _nurbs_edge([(3.5, 0.75), (3.4862622227, 0.7422124196), (3.4573875519, 0.7267508212), (3.4098780258, 0.7038990704), (3.3381165228, 0.6741134839), (3.2347368868, 0.6381577211), (3.1189786252, 0.6038790662), (2.9935733769, 0.5720567866), (2.8633857006, 0.544011998), (2.7342185073, 0.5213393028), (2.6113453071, 0.5055753537), (2.4981376635, 0.4978876416), (2.3946332688, 0.4987491082), (2.2960926209, 0.5076075258), (2.1951301923, 0.5231936955), (2.0839277961, 0.543833506), (1.9562380277, 0.5677335586), (1.8099132965, 0.593314916), (1.6465991635, 0.6192640553), (1.4704853237, 0.6444898913), (1.2874183062, 0.6681136708), (1.1038606456, 0.6894482904), (0.9259996011, 0.7079835593), (0.7586231759, 0.723375302), (0.6046879962, 0.7354236352), (0.4658835609, 0.7440322749), (0.3675279147, 0.7481463654), (0.3009712226, 0.7496764945), (0.2597959315, 0.7500070817), (0.2400072617, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.2400072617, 0.75), (0.2653796346, 0.7388989688), (0.3147581051, 0.7177200127), (0.3847270691, 0.6890208704), (0.4698154693, 0.6568981642), (0.5627809768, 0.6268454455), (0.6432250092, 0.6064451485), (0.712960649, 0.5947618817), (0.7749997024, 0.590223468), (0.8340187373, 0.5904042839), (0.896235228, 0.5919982682), (0.9670970666, 0.5915199786), (1.0491706155, 0.5859185956), (1.1402135451, 0.5731789297), (1.2304643355, 0.553052642), (1.3056864804, 0.5268166265), (1.3519022914, 0.4967951478), (1.3590852375, 0.4659530193), (1.326388376, 0.4374922356), (1.2627400249, 0.4143218891), (1.1811242538, 0.3982235305), (1.0947797923, 0.3892324541), (1.0118079285, 0.3845921108), (0.9351386096, 0.379792592), (0.8643739915, 0.3703962859), (0.7970396426, 0.3536478474), (0.7300420159, 0.3300867893), (0.6611226199, 0.3054121024), (0.5889156389, 0.288109212), (0.5128641326, 0.2865793875), (0.4331781669, 0.3066597909), (0.350806896, 0.3484827395), (0.267310754, 0.4051961125), (0.1844462607, 0.4662401729), (0.1038201729, 0.5196696569), (0.026490993, 0.5549790894), (-0.0473508908, 0.5654154509), (-0.118883462, 0.5512738949), (-0.1903870483, 0.5191669426), (-0.2645521407, 0.479049586), (-0.3438949515, 0.4418539702), (-0.4301817871, 0.4170691114), (-0.5237123365, 0.4098544437), (-0.6234215674, 0.4210825569), (-0.7273354637, 0.4486594663), (-0.8329041023, 0.4884083322), (-0.9373960555, 0.5351591207), (-1.0382372141, 0.5836739592), (-1.1334436591, 0.629819304), (-1.2217420847, 0.670941197), (-1.3023701474, 0.7054303045), (-1.3604452079, 0.7270911233), (-1.4003355218, 0.7398863099), (-1.425300899, 0.7468841588), (-1.4373765406, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.4373765406, 0.75), (-1.4375557371, 0.7453849078), (-1.4365473152, 0.7359377065), (-1.4309345989, 0.7211158727), (-1.4152367661, 0.7000494721), (-1.3824275858, 0.6715860734), (-1.3379958022, 0.6411355908), (-1.2852682042, 0.6090040605), (-1.2295311229, 0.5756972356), (-1.1770054034, 0.5418945853), (-1.1340574414, 0.5084375023), (-1.1063334192, 0.4763107796), (-1.0978874419, 0.4466326886), (-1.1104053723, 0.4206276883), (-1.143440231, 0.3994486664), (-1.1945533666, 0.3840149678), (-1.2594560357, 0.374835443), (-1.3327625812, 0.3720394562), (-1.4087763965, 0.375414466), (-1.4822554821, 0.3844389419), (-1.5491966046, 0.3983140232), (-1.6075956377, 0.4159950107), (-1.6582877431, 0.4362164964), (-1.7040522258, 0.4576435645), (-1.7486525566, 0.4790272886), (-1.7958990321, 0.4993605132), (-1.8487232072, 0.5180304712), (-1.9081914779, 0.5349859903), (-1.9738771136, 0.5506139461), (-2.0442996557, 0.5656017034), (-2.1173294371, 0.5808077313), (-2.1906091643, 0.5971276154), (-2.2619486812, 0.6153682013), (-2.3297767838, 0.636102696), (-2.3930791526, 0.6596971663), (-2.4512631819, 0.6863613181), (-2.4934938464, 0.7102238568), (-2.5227035788, 0.7295549417), (-2.5410834358, 0.7430788875), (-2.550000038, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-2.550000038, 0.75), (-2.5574929846, 0.7398489007), (-2.5701779074, 0.7200814334), (-2.5823022011, 0.6920344697), (-2.5846382885, 0.6578524288), (-2.5652854377, 0.6203516923), (-2.5262766663, 0.5876218011), (-2.4730022965, 0.5587158192), (-2.4147945753, 0.5319747278), (-2.3628589172, 0.5056265834), (-2.3278643831, 0.4784874846), (-2.3177955466, 0.4505673714), (-2.3353531976, 0.4238662025), (-2.3764900696, 0.4026689768), (-2.4334706211, 0.391845701), (-2.4972495932, 0.3954354092), (-2.5600532886, 0.4151501323), (-2.6179955564, 0.4487992766), (-2.6702654268, 0.4914592953), (-2.7181627334, 0.5367457238), (-2.7641920561, 0.5780614993), (-2.8111830882, 0.6097826801), (-2.8613118508, 0.6286372583), (-2.9154529754, 0.6345131274), (-2.9736161169, 0.629396056), (-3.0351914351, 0.6166417924), (-3.0992644435, 0.6001303106), (-3.1648969038, 0.5834797005), (-3.2314222507, 0.5692312196), (-3.2983977955, 0.5590435217), (-3.365558886, 0.5538822087), (-3.4193305615, 0.5541405193), (-3.4596636136, 0.5568614235), (-3.4865542203, 0.5597965142), (-3.5, 0.5615443483)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.5, 0.5615443483), (-3.5, 0))
                _nurbs_edge([(-3.5, 0), (-3.4873973996, 0.025338118), (-3.4615849338, 0.0727804237), (-3.4210443601, 0.134241728), (-3.3633434938, 0.1967692229), (-3.2851924675, 0.2430841759), (-3.2012260311, 0.2593859901), (-3.1118694243, 0.2493896553), (-3.0179121194, 0.2196813726), (-2.9202965197, 0.1790536356), (-2.8196781804, 0.1367494747), (-2.7160297632, 0.1009947745), (-2.6082772501, 0.0774986183), (-2.4937800256, 0.0677235428), (-2.3693523691, 0.0697228083), (-2.2325376968, 0.0793813184), (-2.0827684575, 0.0914916175), (-1.9226434385, 0.1009174887), (-1.7590227805, 0.1036601371), (-1.6046031829, 0.0981245707), (-1.4751451564, 0.0846197286), (-1.3861159851, 0.0646165712), (-1.3494671674, 0.0400854029), (-1.3705066371, 0.0128307636), (-1.4442590983, -0.0162459647), (-1.5585076053, -0.046757414), (-1.6976220332, -0.0782960852), (-1.8458819175, -0.1100015634), (-1.9914797601, -0.1399690378), (-2.1286955221, -0.1650969168), (-2.2559272392, -0.1819541146), (-2.3745808829, -0.1874232336), (-2.4875887239, -0.1794764279), (-2.5981982366, -0.1578012268), (-2.7083936645, -0.1247406286), (-2.818511359, -0.0851226444), (-2.9278833213, -0.0451217781), (-3.0352034774, -0.0113657152), (-3.1389779732, 0.0099878125), (-3.2380017165, 0.0143250489), (-3.331605868, -0.0009679217), (-3.401886566, -0.0299374325), (-3.451965783, -0.0612458734), (-3.4841833771, -0.0863728679), (-3.5000000522, -0.1000000015)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.5000000522, -0.1000000015), (-3.5, -0.6165341183))
                _nurbs_edge([(-1.8318892104, -0.75), (-1.8324993978, -0.7373125494), (-1.8318173596, -0.7132767917), (-1.8250871235, -0.6812405217), (-1.8046869636, -0.6465689661), (-1.760704563, -0.6161615396), (-1.70003512, -0.5971911138), (-1.6263811665, -0.5865817994), (-1.5459581116, -0.5791920054), (-1.4664266016, -0.5692309817), (-1.395910202, -0.5515566523), (-1.3419603472, -0.5230961908), (-1.31059669, -0.4840460116), (-1.3051653416, -0.4396364615), (-1.3265223787, -0.3979222771), (-1.3734811987, -0.3670537506), (-1.4431435086, -0.3522108832), (-1.531327502, -0.3547542006), (-1.6330275615, -0.3733985686), (-1.7428659858, -0.4047997322), (-1.8555374534, -0.4443633716), (-1.9662722379, -0.4869702869), (-2.0712539403, -0.5276894092), (-2.168159096, -0.5626083301), (-2.2561301688, -0.5890227469), (-2.3354829081, -0.6053190943), (-2.4075014188, -0.6109550117), (-2.4742058336, -0.6064145034), (-2.5381264402, -0.5931558137), (-2.602101337, -0.5736260676), (-2.6689607027, -0.5509870991), (-2.7411341381, -0.528645857), (-2.8202743686, -0.5098404815), (-2.906882663, -0.497212621), (-2.9999010268, -0.4923612887), (-3.0963910752, -0.4954640571), (-3.192173249, -0.5056750123), (-3.282390844, -0.5214602473), (-3.3620933783, -0.5409505001), (-3.4268239997, -0.5622907751), (-3.4690375887, -0.5820389027), (-3.489304466, -0.597179063), (-3.4971808398, -0.6078494445), (-3.4994916977, -0.6142602036), (-3.5, -0.6165341183)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 0.9888390667, 0.9888390667, 0.9888390667, 0.9888390667, 0.9888390667, 0.9888390667], 5)
                _nurbs_edge([(-0.1531436683, -0.75), (-0.1508900914, -0.736513527), (-0.1459304135, -0.7105508837), (-0.1371332805, -0.6746377221), (-0.1226861529, -0.6328222002), (-0.1000060225, -0.5901394308), (-0.0724637894, -0.5554127962), (-0.0395854591, -0.5252985674), (-0.0006316717, -0.4942502314), (0.0444374794, -0.4566367235), (0.0939823301, -0.40884399), (0.143803731, -0.3512259665), (0.1859455767, -0.2905628829), (0.2109845663, -0.236926043), (0.2108944905, -0.1996513108), (0.1814668612, -0.1839669985), (0.1255481163, -0.1864804845), (0.0512099692, -0.1976986522), (-0.0313198628, -0.2062769823), (-0.1122108767, -0.202539903), (-0.1849824871, -0.1826027653), (-0.2487566738, -0.1514038157), (-0.3061848075, -0.11893404), (-0.3617643136, -0.0970565025), (-0.4201316116, -0.0963416843), (-0.484094098, -0.1223474764), (-0.5536986623, -0.1739738902), (-0.6272996762, -0.2457950657), (-0.7021811618, -0.3295011974), (-0.7753457006, -0.4156686839), (-0.8442446877, -0.4954124928), (-0.9074995232, -0.5620168205), (-0.9657256329, -0.6127757426), (-1.0210633222, -0.6481898925), (-1.0765677018, -0.6708742536), (-1.1356468598, -0.6845690465), (-1.201497623, -0.6931397988), (-1.2765000532, -0.6995159951), (-1.3623034551, -0.7057615178), (-1.4599736705, -0.7132479394), (-1.5701149484, -0.7227875684), (-1.6684226776, -0.7323822109), (-1.7479168874, -0.7407398092), (-1.8034719494, -0.7468273092), (-1.8318892104, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(1.3145814558, -0.75), (1.3406294064, -0.7467967707), (1.3897710024, -0.7391031459), (1.4546205934, -0.7237013898), (1.5233365538, -0.6954312407), (1.5798760779, -0.6476402337), (1.6079662245, -0.588785047), (1.609636223, -0.5217796203), (1.5883750713, -0.451456228), (1.5497640899, -0.3854323849), (1.5006620146, -0.3326320187), (1.4477658003, -0.3007848106), (1.3963951457, -0.2942944683), (1.3491317752, -0.3118345352), (1.304638804, -0.3443116037), (1.2593524706, -0.3789275408), (1.2090786986, -0.4030634546), (1.1505441765, -0.4080180709), (1.0831645562, -0.3933601826), (1.0085040385, -0.3649500625), (0.9294364545, -0.3321607546), (0.84939968, -0.3053204538), (0.7716644645, -0.2932682997), (0.6984798069, -0.3003825232), (0.6306679314, -0.3254276808), (0.5680703328, -0.36381484), (0.5098019245, -0.409105233), (0.4545730224, -0.4547667492), (0.4009885993, -0.4959030273), (0.3478277423, -0.530753917), (0.294029663, -0.5597162875), (0.238709444, -0.5845820802), (0.1811610445, -0.6077434362), (0.1208721641, -0.6313196123), (0.0575177468, -0.6566425633), (-0.0090866956, -0.6845226127), (-0.0650353193, -0.7091809758), (-0.1085041027, -0.7290547081), (-0.1381523097, -0.7429161766), (-0.1531436683, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                Line((1.3145814558, -0.75), (1.4474709617, -0.75))
                _nurbs_edge([(2.4178759013, -0.75), (2.4279695417, -0.7477047954), (2.4481351465, -0.7428018341), (2.4783185139, -0.7345097411), (2.5184328596, -0.7215757773), (2.5679180538, -0.7024296106), (2.6154249314, -0.680782886), (2.6583050707, -0.6576143785), (2.692141461, -0.6345743193), (2.7102688024, -0.614170596), (2.7064752515, -0.5987210549), (2.6777035125, -0.5893064794), (2.6268372535, -0.5846901899), (2.5607134943, -0.5821316816), (2.4881246314, -0.5782059809), (2.4177453973, -0.569651077), (2.3563101246, -0.5541224527), (2.3061477073, -0.5311897196), (2.2649889176, -0.5024795053), (2.2282150417, -0.4708887065), (2.1905288174, -0.4400376218), (2.1476756034, -0.4136597846), (2.0985780089, -0.3949498886), (2.0457164631, -0.3861902614), (1.9932474812, -0.3887712213), (1.9456419614, -0.4030920234), (1.9062587598, -0.4285320192), (1.8755865946, -0.4633141234), (1.8513194433, -0.504744717), (1.8295283525, -0.5496590583), (1.8055010927, -0.5948080256), (1.7746772864, -0.6372506457), (1.7336367623, -0.6747894938), (1.680028748, -0.705903363), (1.6148773604, -0.7287173186), (1.5524104958, -0.7409984039), (1.5002817911, -0.7468115941), (1.4641662812, -0.7492015689), (1.4474709617, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.966067172, 0.966067172, 0.966067172, 0.966067172, 0.966067172, 0.966067172], 5)
                _nurbs_edge([(3.5, -0.2315151421), (3.4881342741, -0.2519510953), (3.4643476883, -0.291695802), (3.4285024005, -0.3479313302), (3.3803755213, -0.416099221), (3.3196147457, -0.489716914), (3.2581369344, -0.5515409188), (3.1957287929, -0.6016064146), (3.1320558381, -0.6403713025), (3.0666196056, -0.6690599994), (2.9987964316, -0.6895576362), (2.9279370154, -0.7039958443), (2.8534505109, -0.7144734377), (2.7749134915, -0.7227313944), (2.6921628623, -0.7298985554), (2.6051900137, -0.7366477625), (2.5322921296, -0.7419773859), (2.4757900113, -0.7459847925), (2.4373150814, -0.7486608533), (2.4178759013, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5, -0.2315151421), (3.5000000522, 0.200000003))
            make_face()
            # Profile area: 0.0001292932, perimeter: 0.2658219101
            with BuildLine():
                _nurbs_edge([(1.4474709617, -0.75), (1.4436144273, -0.7501844335), (1.4190347358, -0.7512595941), (1.3933706213, -0.7517514319), (1.3666210304, -0.7516591), (1.3387868139, -0.750983057), (1.3145814558, -0.75)], [1, 1, 1, 1, 1, 1, 1], [0.966067172, 0.966067172, 0.966067172, 0.966067172, 0.966067172, 0.966067172, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                Line((1.3145814558, -0.75), (1.4474709617, -0.75))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_131528_0743cfc4_0002():
    """Model: side4 v1"""
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
        # Sketch2 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8918757304, perimeter: 34.878032587
            with BuildLine():
                _nurbs_edge([(-3.5, -0.7070769185), (-3.4865782812, -0.7081522637), (-3.4599121799, -0.7100596552), (-3.4204450272, -0.7121908521), (-3.3688868108, -0.7135718247), (-3.3061920281, -0.7128850047), (-3.2451816756, -0.7098560307), (-3.1857114797, -0.7046346015), (-3.1275425838, -0.6974718751), (-3.070298871, -0.6887595688), (-3.0135014732, -0.6790158216), (-2.9567269531, -0.6687837), (-2.8997412026, -0.6585495271), (-2.8426345242, -0.6486540612), (-2.785977846, -0.6392043382), (-2.7309103102, -0.6299914435), (-2.6787352373, -0.6204884675), (-2.630545697, -0.609827857), (-2.5868785346, -0.5968100928), (-2.5472604579, -0.5798413055), (-2.5101018343, -0.5570825824), (-2.4734932747, -0.5271318545), (-2.4358452329, -0.4896236471), (-2.3965589165, -0.4458259645), (-2.3567688222, -0.3993417407), (-2.3184665972, -0.3548597494), (-2.2835021405, -0.316761571), (-2.2526298529, -0.2877810576), (-2.2245335883, -0.2676384261), (-2.1948560609, -0.2516780113), (-2.158084313, -0.2332959534), (-2.1094897069, -0.2064366687), (-2.0469570968, -0.1679475269), (-1.9731038659, -0.1203013308), (-1.8940515441, -0.0700573892), (-1.8178130631, -0.025829772), (-1.7528562912, 0.0035141556), (-1.7065187791, 0.0108602301), (-1.6836629703, -0.0074867984), (-1.6847773407, -0.0493450658), (-1.7062810786, -0.1073518968), (-1.7423394516, -0.1718045771), (-1.7862893561, -0.2329809255), (-1.8320883086, -0.2834131608), (-1.8760858514, -0.3208279035), (-1.9172031955, -0.3479942616), (-1.9559216255, -0.3702894744), (-1.9936089425, -0.3938927291), (-2.0317449092, -0.4238318889), (-2.0710971933, -0.4618083091), (-2.1117770739, -0.5067090407), (-2.1534701696, -0.5556273924), (-2.1956101917, -0.6047302229), (-2.2375626324, -0.6501194885), (-2.2788367616, -0.6888616172), (-2.319154677, -0.719284457), (-2.3505298112, -0.7362868219), (-2.3735466699, -0.7447937524), (-2.3886625943, -0.748578917), (-2.3961634007, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0181818182, 0.0363636364, 0.0545454545, 0.0727272727, 0.0909090909, 0.1090909091, 0.1272727273, 0.1454545455, 0.1636363636, 0.1818181818, 0.2, 0.2181818182, 0.2363636364, 0.2545454545, 0.2727272727, 0.2909090909, 0.3090909091, 0.3272727273, 0.3454545455, 0.3636363636, 0.3818181818, 0.4, 0.4181818182, 0.4363636364, 0.4545454545, 0.4727272727, 0.4909090909, 0.5090909091, 0.5272727273, 0.5454545455, 0.5636363636, 0.5818181818, 0.6, 0.6181818182, 0.6363636364, 0.6545454545, 0.6727272727, 0.6909090909, 0.7090909091, 0.7272727273, 0.7454545455, 0.7636363636, 0.7818181818, 0.8, 0.8181818182, 0.8363636364, 0.8545454545, 0.8727272727, 0.8909090909, 0.9090909091, 0.9272727273, 0.9454545455, 0.9636363636, 0.9818181818, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.2199643238, -0.75), (-2.3961634007, -0.75))
                _nurbs_edge([(-2.2199643238, -0.75), (-2.2196024462, -0.7499541579), (-2.2054383186, -0.7481447081), (-2.1795313765, -0.7436595072), (-2.1467567835, -0.7342978899), (-2.1139498201, -0.7167280721), (-2.0862760721, -0.6873995251), (-2.0634075487, -0.6521580445), (-2.0343266855, -0.6131856425), (-1.9888931451, -0.5726444476), (-1.9204571768, -0.5322431561), (-1.8296299156, -0.4926192582), (-1.7231110803, -0.4534901749), (-1.6109106415, -0.4140516451), (-1.5041404037, -0.3732903537), (-1.4125290581, -0.330334591), (-1.3421669873, -0.2847797764), (-1.2928602856, -0.2370489354), (-1.2564151969, -0.1886780433), (-1.2210458887, -0.1420632892), (-1.1753242128, -0.1002775476), (-1.1119029787, -0.0668441196), (-1.0323517994, -0.0455812008), (-0.9456456292, -0.0401261524), (-0.864315982, -0.0533560813), (-0.8013008006, -0.0868119227), (-0.7667157024, -0.1401691795), (-0.7641109774, -0.2105287585), (-0.7914254832, -0.293009046), (-0.8429232972, -0.3815942382), (-0.9108028125, -0.46990634), (-0.9868378866, -0.5519581326), (-1.0642103103, -0.6230278632), (-1.138561508, -0.6801151524), (-1.2065782648, -0.721045718), (-1.2554481538, -0.7407784539), (-1.2887550918, -0.7482043593), (-1.3093796235, -0.7499213842), (-1.319100066, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0563951924, 0.0563951924, 0.0563951924, 0.0563951924, 0.0563951924, 0.0563951924, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 0.9985917666, 0.9985917666, 0.9985917666, 0.9985917666, 0.9985917666, 0.9985917666], 5)
                Line((-1.2479649106, -0.75), (-1.319100066, -0.75))
                _nurbs_edge([(-1.2479649106, -0.75), (-1.2474730581, -0.7499886632), (-1.2319492164, -0.749624725), (-1.2016029485, -0.7485324786), (-1.1569503708, -0.7458000039), (-1.0988643997, -0.7399884465), (-1.0293408619, -0.7293092616), (-0.9630827095, -0.7153486035), (-0.9013549466, -0.6984340753), (-0.8460861217, -0.679081273), (-0.7998710895, -0.6579876612), (-0.7648243657, -0.6356180849), (-0.7415750117, -0.6118418246), (-0.7281606729, -0.5855304872), (-0.7190801087, -0.5542268142), (-0.7076297321, -0.5158033396), (-0.6878590052, -0.4697913838), (-0.6571408518, -0.4193429547), (-0.6160322177, -0.3703161538), (-0.5669346658, -0.3291097274), (-0.5131114627, -0.3008060155), (-0.4576297245, -0.2873876738), (-0.4021578796, -0.285386024), (-0.3470519683, -0.2874081101), (-0.2918292149, -0.2847826549), (-0.2355083183, -0.2698362056), (-0.1770008688, -0.2382935027), (-0.1154873304, -0.1917215278), (-0.0504937711, -0.1359575039), (0.0180407748, -0.0794036691), (0.08969739, -0.0314139241), (0.1634958057, -0.0005749011), (0.237846666, 0.0068016539), (0.3104141513, -0.0113022302), (0.3783077717, -0.0524530246), (0.4386011328, -0.1114181835), (0.4887493743, -0.1812929699), (0.5270744067, -0.2548783929), (0.5531658311, -0.3258476006), (0.5684641545, -0.3902507356), (0.5762786124, -0.4470221118), (0.5809193764, -0.4969307859), (0.5870106895, -0.5418716503), (0.5987938479, -0.584079993), (0.6192826105, -0.6252422147), (0.6502064399, -0.6663180337), (0.6839831851, -0.6995067951), (0.7145168967, -0.7246538205), (0.737182866, -0.7415323187), (0.7490933682, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0214952657, 0.0214952657, 0.0214952657, 0.0214952657, 0.0214952657, 0.0214952657, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.7490933682, -0.75), (0.7525649402, -0.7390315395), (0.7584429198, -0.7182711789), (0.764065381, -0.6906582605), (0.7651559333, -0.6609235412), (0.7565743153, -0.6342151805), (0.7401723465, -0.6141695515), (0.7205822584, -0.5924576318), (0.704128591, -0.5581789614), (0.6967524272, -0.5024473207), (0.7022622374, -0.4223240295), (0.7205675877, -0.3247269325), (0.7488971407, -0.2228286492), (0.7828455322, -0.1328694738), (0.8174712436, -0.0708447447), (0.8483744871, -0.0492230279), (0.872767112, -0.0736951586), (0.8906017765, -0.1397039744), (0.9038882014, -0.2353762609), (0.9159463666, -0.3446865271), (0.9307048976, -0.4504352591), (0.951955291, -0.5374488937), (0.9826952311, -0.5953240168), (1.0242546733, -0.6223097512), (1.0762961291, -0.6245965521), (1.1374123486, -0.6124454237), (1.2055337169, -0.5973363702), (1.2784215999, -0.5885891609), (1.3540851262, -0.5905499108), (1.4307643604, -0.6038707857), (1.5069428157, -0.6264797083), (1.5813504206, -0.6546525872), (1.6529714814, -0.6840213406), (1.721053145, -0.7106231647), (1.7816167582, -0.730716413), (1.8263839495, -0.7417836297), (1.8575005219, -0.747076441), (1.8765459813, -0.7492781203), (1.8844470095, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9636329193, 0.9636329193, 0.9636329193, 0.9636329193, 0.9636329193, 0.9636329193], 5)
                Line((1.9500000291, -0.75), (1.8844470095, -0.75))
                _nurbs_edge([(2.252348771, -0.75), (2.3021888477, -0.7238039781), (2.3963974776, -0.6736244261), (2.5212959213, -0.6049925492), (2.6549539092, -0.5267761487), (2.7675665145, -0.4510058961), (2.8271383536, -0.3965972148), (2.8368692224, -0.3621274212), (2.8023730657, -0.3451088063), (2.7324860485, -0.3416463193), (2.6396422924, -0.3462440136), (2.5373255523, -0.3526784597), (2.4376869676, -0.3547784528), (2.3493814624, -0.3472001844), (2.2746001782, -0.3263032442), (2.209395196, -0.2905985099), (2.1467065889, -0.2409064958), (2.0784719641, -0.180529232), (1.9983745759, -0.1156218235), (1.9034270503, -0.0548619116), (1.7935345617, -0.0075862512), (1.6714644433, 0.0176940025), (1.54272095, 0.015036454), (1.4153643083, -0.0175248983), (1.3001562391, -0.0757997483), (1.2091233156, -0.1506578177), (1.1533800754, -0.2308632851), (1.1410779621, -0.3054801497), (1.1755139941, -0.3662410761), (1.2525568787, -0.4104830357), (1.3619406426, -0.4405233083), (1.4898556065, -0.4618107822), (1.6211487463, -0.4814634185), (1.7415310161, -0.5067463483), (1.840124475, -0.5433652147), (1.910745637, -0.5945410241), (1.9424134399, -0.6484107261), (1.9517904392, -0.6962976977), (1.9516603445, -0.7315454235), (1.9500000291, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                Line((2.4067831347, -0.75), (2.252348771, -0.75))
                _nurbs_edge([(3.5, -0.6000000611), (3.4867422633, -0.5838149926), (3.4606098146, -0.5535867796), (3.4225603271, -0.5146704365), (3.3741418018, -0.4757256036), (3.317349798, -0.4488209155), (3.263711945, -0.4432734666), (3.2119508062, -0.4574913624), (3.159681402, -0.4878050777), (3.1037341389, -0.5290117393), (3.0407597715, -0.5754300289), (2.9676866945, -0.6216524131), (2.8823946642, -0.6635741267), (2.7838660854, -0.6986800553), (2.6721684213, -0.7254221495), (2.5721960193, -0.7397359537), (2.4914597864, -0.7464267931), (2.4352477497, -0.7491055021), (2.4067831347, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9320874582, 0.9320874582, 0.9320874582, 0.9320874582, 0.9320874582, 0.9320874582], 5)
                Line((3.5, 0), (3.5, -0.6000000611))
                _nurbs_edge([(3.5, 0.3067165037), (3.485421827, 0.3149741345), (3.455465362, 0.3306012719), (3.4081302995, 0.3513776216), (3.3402036931, 0.373736667), (3.2473653239, 0.3926442971), (3.1470029144, 0.4022398922), (3.0400283785, 0.4020940641), (2.9280676742, 0.3915813134), (2.813649025, 0.3698867957), (2.7001798874, 0.3364762369), (2.5919311536, 0.2915087608), (2.494065018, 0.236333034), (2.4125675114, 0.1738502171), (2.354434822, 0.1092353902), (2.3269883553, 0.0495022261), (2.3358990832, 0.0014010435), (2.383631123, -0.0301657659), (2.4673651785, -0.0442171447), (2.5801965062, -0.0429345388), (2.7127542542, -0.0305424704), (2.8546693515, -0.0123203602), (2.9959934517, 0.0063652967), (3.1288416798, 0.0211623957), (3.2482676803, 0.0293469257), (3.3513909283, 0.0293229714), (3.4198040415, 0.0221562932), (3.4630351982, 0.0126718693), (3.4882752089, 0.0045275313), (3.5, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5, 0.6956190617), (3.5, 0.3067165037))
                _nurbs_edge([(3.5, 0.6956190617), (3.4900404181, 0.6996540387), (3.4692117863, 0.7071491613), (3.4352405109, 0.7166673867), (3.3844782776, 0.7259028848), (3.3120938362, 0.7317511465), (3.2314080515, 0.7321505317), (3.1437833305, 0.7276553801), (3.0515233652, 0.7192165124), (2.9582837043, 0.7083633894), (2.8684743273, 0.6969220382), (2.7862544658, 0.6865447969), (2.7146694015, 0.6783062861), (2.6546969728, 0.6722559661), (2.6043713576, 0.66701069), (2.5577001658, 0.6592400425), (2.5067851165, 0.6448791084), (2.4443015918, 0.6205492869), (2.3655946373, 0.5847471876), (2.2715598357, 0.5395271165), (2.1689453917, 0.4905571835), (2.0676308522, 0.4452628062), (1.9787432074, 0.4115018711), (1.912384067, 0.3959827318), (1.8756621706, 0.402892835), (1.8702267397, 0.4321577599), (1.8910579484, 0.4786414121), (1.9298152318, 0.5347905089), (1.9771902006, 0.5925137546), (2.0261376903, 0.6457621281), (2.0726616188, 0.691123482), (2.106308946, 0.7197300298), (2.1292499842, 0.7366329936), (2.1435246815, 0.7458810508), (2.15040728, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(2.15040728, 0.75), (2.1331701429, 0.7490246777), (2.0993449807, 0.7468918558), (2.0505545636, 0.7431460924), (1.9893985444, 0.7370577863), (1.9194691108, 0.7276148438), (1.856082766, 0.7163199934), (1.7992678887, 0.7031416856), (1.7490561575, 0.6880322872), (1.7054613753, 0.6709282797), (1.6685163093, 0.6517404704), (1.6380561666, 0.6303848611), (1.6132668927, 0.6068406791), (1.5923875099, 0.5812032707), (1.5721423197, 0.5537332569), (1.5481326784, 0.5249378717), (1.5161078858, 0.4957027616), (1.4728956971, 0.4673799956), (1.4176880696, 0.441965363), (1.3524601478, 0.4220021552), (1.2809221963, 0.4099932959), (1.2078026003, 0.4079274049), (1.137998906, 0.4167479671), (1.075795389, 0.4358653624), (1.0240302773, 0.462593168), (0.9833397116, 0.4917553158), (0.9524407896, 0.5173113421), (0.9283090635, 0.5339491339), (0.9064645812, 0.5384993569), (0.8810194151, 0.5319063295), (0.8458007052, 0.5185683517), (0.7961739644, 0.5041832861), (0.7304346469, 0.4942191657), (0.6519000771, 0.4917647101), (0.5686849604, 0.4970724418), (0.4912308541, 0.5086508032), (0.4305004299, 0.5239186037), (0.3958051361, 0.5400641303), (0.3930133392, 0.5547438624), (0.4220207366, 0.5670264427), (0.4767908859, 0.5775268536), (0.5477496083, 0.5878076561), (0.6235422063, 0.5999794564), (0.6929890918, 0.6162342371), (0.7470818621, 0.6383795436), (0.7805915252, 0.6674558641), (0.788847082, 0.6966735091), (0.7842365793, 0.7220074107), (0.7763650089, 0.7404159345), (0.7712297942, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.7712297942, 0.75), (0.7562011133, 0.7443795441), (0.726527767, 0.7336875014), (0.6831698001, 0.7192960628), (0.6276655793, 0.7034039249), (0.5621021527, 0.6889248975), (0.5002494296, 0.6794710921), (0.4418784411, 0.6742990535), (0.3865870458, 0.6721328893), (0.33376274, 0.6710565751), (0.2825095142, 0.6682923892), (0.2317902348, 0.6606656127), (0.1806222388, 0.6452401311), (0.1282668322, 0.6199328575), (0.0743955884, 0.5840601661), (0.0193334036, 0.5391162549), (-0.035980038, 0.4887031267), (-0.0903420739, 0.4375197981), (-0.1425515822, 0.390610325), (-0.1917155135, 0.3524990729), (-0.2375230681, 0.3263954801), (-0.2805726509, 0.3133103228), (-0.3225791008, 0.3113506236), (-0.3653063598, 0.3170900543), (-0.4094816407, 0.3268849282), (-0.45391352, 0.3380432573), (-0.4940234023, 0.3504636915), (-0.5230059924, 0.3661158465), (-0.5344801789, 0.3872922839), (-0.5246934036, 0.4152336246), (-0.494889938, 0.4486152033), (-0.4496773439, 0.4845439907), (-0.3954630905, 0.5195076268), (-0.338893522, 0.5503246412), (-0.2852492559, 0.575127674), (-0.2369872686, 0.5942429035), (-0.1945463567, 0.6094639665), (-0.1570309422, 0.6234071857), (-0.1229043051, 0.6388721891), (-0.0907440078, 0.6581274745), (-0.0597468745, 0.6824633973), (-0.0355439594, 0.7065155252), (-0.0176658113, 0.7272214195), (-0.0058683698, 0.7422097533), (0, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0, 0.75), (-0.0201637467, 0.7495359716), (-0.0599115435, 0.7477846833), (-0.11779415, 0.742688065), (-0.1914864744, 0.7309441857), (-0.2777966283, 0.7081524003), (-0.3583721617, 0.6777452919), (-0.4334039485, 0.6407905467), (-0.5032561659, 0.5991337241), (-0.5685218692, 0.5556272826), (-0.6300784452, 0.5143208377), (-0.6890298579, 0.4793991084), (-0.7466598461, 0.4541132551), (-0.8043711665, 0.4397901587), (-0.8636597972, 0.4346049547), (-0.925995221, 0.4329900372), (-0.9923064989, 0.4281591354), (-1.0624555623, 0.4143747146), (-1.1348309943, 0.3890039834), (-1.2055811395, 0.3554460044), (-1.2691409716, 0.3227855674), (-1.3201983308, 0.3018098459), (-1.3552344902, 0.3020808008), (-1.3743479792, 0.3284136592), (-1.382704723, 0.3780326462), (-1.3883431136, 0.4435801873), (-1.4003408506, 0.5155797909), (-1.4266934999, 0.5852905477), (-1.4728023796, 0.6467628022), (-1.5421693981, 0.6960645256), (-1.6265046309, 0.7271656712), (-1.7075225044, 0.7420270707), (-1.7730440328, 0.7478374559), (-1.8147055015, 0.7496087783), (-1.8280786371, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 0.9819508248, 0.9819508248, 0.9819508248, 0.9819508248, 0.9819508248, 0.9819508248], 5)
                Line((-1.9108861257, 0.75), (-1.8280786371, 0.75))
                _nurbs_edge([(-1.9108861257, 0.75), (-1.9078751297, 0.7411872217), (-1.9006202137, 0.7236701003), (-1.886038813, 0.6977197243), (-1.859193556, 0.663770497), (-1.8139988806, 0.6224649127), (-1.7593879649, 0.5824202124), (-1.6997966203, 0.5438915811), (-1.6428455409, 0.5073005152), (-1.5995219835, 0.4732778954), (-1.5805285381, 0.4427499129), (-1.5934814326, 0.4169915904), (-1.6391138666, 0.39775245), (-1.7100107351, 0.3871622555), (-1.7944362156, 0.3871766279), (-1.8790811387, 0.3991187614), (-1.9522394313, 0.4231782552), (-2.0067819195, 0.4579271825), (-2.0432966817, 0.4998089322), (-2.0676496782, 0.5441388397), (-2.0883903664, 0.5861818285), (-2.114408664, 0.6220897275), (-2.1520517639, 0.6501692961), (-2.2044422507, 0.6708115403), (-2.2722813816, 0.6855369627), (-2.3542001808, 0.6962750894), (-2.4472874046, 0.7046252447), (-2.547531599, 0.7109413234), (-2.6502998298, 0.7142339588), (-2.7508012452, 0.7128450579), (-2.8445625906, 0.7049106023), (-2.9278848839, 0.6888944333), (-2.998345009, 0.6641264978), (-3.0552048119, 0.6312639791), (-3.100063245, 0.5929871691), (-3.1366043946, 0.5537922535), (-3.1695384869, 0.5189739624), (-3.2037972982, 0.4938621309), (-3.2435770721, 0.4829050022), (-3.2915920512, 0.4889609415), (-3.3494556916, 0.513707129), (-3.4042447857, 0.5490845057), (-3.4502238406, 0.5844820519), (-3.4830463138, 0.6120160682), (-3.5, 0.6267669966)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.5, 0.1428166557), (-3.5, 0.6267669966))
                _nurbs_edge([(-3.5, 0.1428166557), (-3.4816015608, 0.1277663844), (-3.4458680351, 0.1002644842), (-3.3954581885, 0.0668078266), (-3.3346341826, 0.0378172742), (-3.2686100033, 0.0271135435), (-3.2104803818, 0.0401229719), (-3.1560322396, 0.0730503323), (-3.0978629463, 0.1191546682), (-3.0272645289, 0.1698571256), (-2.9367589908, 0.216310978), (-2.8225075005, 0.2508480462), (-2.6865952942, 0.2683913754), (-2.5399520374, 0.2681432307), (-2.3992750188, 0.2525677055), (-2.2831360809, 0.2260004299), (-2.2083100493, 0.1933835091), (-2.1861969948, 0.1590169798), (-2.2186948722, 0.1251622984), (-2.295629556, 0.0911164515), (-2.4001254734, 0.0546756432), (-2.5130785237, 0.0133344594), (-2.6175650081, -0.0345317768), (-2.7041902411, -0.0881967856), (-2.7728513805, -0.1441994328), (-2.8291077085, -0.1975888226), (-2.8818155654, -0.2427971119), (-2.9404586758, -0.2745868268), (-3.012182657, -0.2891442519), (-3.1014792548, -0.2841030021), (-3.2109878543, -0.2581268788), (-3.3157266953, -0.2201448117), (-3.4040654659, -0.1819319771), (-3.4672984013, -0.1521419559), (-3.5, -0.1361682355)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.5, -0.7070769185), (-3.5, -0.1361682355))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_131528_0743cfc4_0007():
    """Model: side3 v1"""
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
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0000045236, perimeter: 0.1149060419
            with BuildLine():
                _nurbs_edge([(-2.1650339508, 0.75), (-2.176298277, 0.7500944835), (-2.1876757117, 0.7501417255), (-2.1991662541, 0.7501417246), (-2.2107698995, 0.7500944828), (-2.222486648, 0.75)], [1, 1, 1, 1, 1, 1], [0.992940092, 0.992940092, 0.992940092, 0.992940092, 0.992940092, 0.992940092, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.222486648, 0.75), (-2.1650339508, 0.75))
            make_face()
            # Profile area: 0.0000009783, perimeter: 0.0671140094
            with BuildLine():
                _nurbs_edge([(-1.4909526129, -0.75), (-1.4975970446, -0.7500349836), (-1.5042749542, -0.750052475), (-1.5109863405, -0.7500524747), (-1.517731203, -0.750034983), (-1.5245095416, -0.75)], [1, 1, 1, 1, 1, 1], [0.9950191555, 0.9950191555, 0.9950191555, 0.9950191555, 0.9950191555, 0.9950191555, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.4909526129, -0.75), (-1.5245095416, -0.75))
            make_face()
            # Profile area: 5.6253597579, perimeter: 30.9376314112
            with BuildLine():
                Line((-3.5, -0.5990122608), (-3.5, 0.159770398))
                _nurbs_edge([(-2.6467499287, -0.75), (-2.6378606349, -0.740156185), (-2.6206421306, -0.7211739879), (-2.5964949291, -0.6948170488), (-2.5676598336, -0.6639100814), (-2.5368343269, -0.6322143749), (-2.5099989747, -0.6070486666), (-2.4847611802, -0.587586545), (-2.4569021727, -0.5723861378), (-2.4211623785, -0.5594602524), (-2.3730525013, -0.5465161448), (-2.3102092646, -0.5311465068), (-2.2343077568, -0.5110318972), (-2.150518029, -0.4841889537), (-2.0661520329, -0.4492438148), (-1.989586131, -0.4056965282), (-1.929067323, -0.3541973905), (-1.8915841834, -0.296810414), (-1.8816723734, -0.2373152675), (-1.9003363444, -0.1814191075), (-1.9457873504, -0.1354750952), (-2.0140784303, -0.1052779131), (-2.0997684568, -0.094837586), (-2.1965690289, -0.1051373871), (-2.2979888848, -0.1329440063), (-2.3977778306, -0.1722253041), (-2.4903703417, -0.2154816827), (-2.5713444899, -0.2551308143), (-2.6378477219, -0.2848053157), (-2.6891126093, -0.3008354699), (-2.72677647, -0.3033215083), (-2.7557087921, -0.2982489102), (-2.7825663832, -0.2949179286), (-2.813522302, -0.3016548182), (-2.8517665827, -0.3210825533), (-2.8968450421, -0.3490764488), (-2.9463799809, -0.3785039438), (-2.9971712211, -0.4017281192), (-3.0465170298, -0.4135394802), (-3.0935185969, -0.4141033855), (-3.1386438028, -0.4074900549), (-3.1831436579, -0.3998285261), (-3.2285634946, -0.3977317256), (-3.2761256366, -0.4063087296), (-3.326603884, -0.428815918), (-3.3804665175, -0.4672106105), (-3.4264420446, -0.5113804966), (-3.4625782003, -0.5522055382), (-3.4874036213, -0.5828403253), (-3.5, -0.5990122608)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.5245095416, -0.75), (-1.5182297439, -0.734359375), (-1.5051736145, -0.7046667407), (-1.4840998168, -0.6648936207), (-1.4530198323, -0.6214022585), (-1.4092383931, -0.5826198691), (-1.3606635914, -0.5583918654), (-1.3075896966, -0.5465981342), (-1.2505256123, -0.5436559895), (-1.1902489318, -0.544105243), (-1.1280046911, -0.5417763674), (-1.0656994674, -0.5309764494), (-1.00611769, -0.507708641), (-0.9530891771, -0.4707919037), (-0.9117942109, -0.423273085), (-0.8877090539, -0.3710809168), (-0.885261645, -0.3211946209), (-0.906742613, -0.280124694), (-0.9507316094, -0.2519396002), (-1.0120870118, -0.2376756974), (-1.0838078718, -0.2363989042), (-1.1584684501, -0.2458596692), (-1.2297026763, -0.2632666067), (-1.2939579433, -0.2861040549), (-1.3511607645, -0.3125981363), (-1.4032740049, -0.3414563422), (-1.4533163654, -0.3717696099), (-1.5042231294, -0.4028526492), (-1.5577240588, -0.4341061339), (-1.6133598244, -0.4648854082), (-1.6693850365, -0.4945699104), (-1.723516688, -0.5226153606), (-1.7737471755, -0.5486136156), (-1.8191116902, -0.5723479928), (-1.8605285704, -0.5938560121), (-1.900133283, -0.6133480644), (-1.9405244143, -0.6311175757), (-1.9840854014, -0.6474592738), (-2.0321685906, -0.662572547), (-2.0852144981, -0.6765679402), (-2.1430686519, -0.6894954894), (-2.2052245756, -0.7013650835), (-2.2711043877, -0.7121707438), (-2.3402987682, -0.7219112297), (-2.4125267777, -0.7305877187), (-2.4876157989, -0.7382031024), (-2.5499024884, -0.7434492041), (-2.5978480541, -0.7469090656), (-2.6303582265, -0.7490048244), (-2.6467499287, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.4909526129, -0.75), (-1.5245095416, -0.75))
                _nurbs_edge([(0.0692390437, -0.75), (0.0822881047, -0.7439275605), (0.1093509646, -0.7316988875), (0.1528394871, -0.7131045014), (0.2166171491, -0.6878087788), (0.3056305012, -0.6552863229), (0.4027933897, -0.6216716661), (0.5057892695, -0.5865903064), (0.6107079719, -0.5494163377), (0.7116672507, -0.509219738), (0.8003120735, -0.4646754992), (0.8675259587, -0.4146851034), (0.9052846539, -0.3590466815), (0.9084500932, -0.2991032266), (0.8766236683, -0.238420636), (0.8159223098, -0.1834180912), (0.7364176754, -0.1415387), (0.6496011238, -0.1194078298), (0.5659472622, -0.1210980095), (0.4922017307, -0.1461000267), (0.4294762702, -0.1881241006), (0.3752139391, -0.2378041725), (0.3246742416, -0.2849752912), (0.2724992002, -0.3208990384), (0.2144762507, -0.3410318143), (0.1482454726, -0.3454256235), (0.0730553624, -0.337038225), (-0.010210765, -0.3206533876), (-0.0991021744, -0.3015403928), (-0.1896548825, -0.2842794586), (-0.277267097, -0.272661238), (-0.357509793, -0.269556992), (-0.4269963864, -0.2767856446), (-0.4841516162, -0.2950013516), (-0.5302345748, -0.323508134), (-0.5686053891, -0.3605839636), (-0.6036288387, -0.4039098076), (-0.6396692133, -0.4509714864), (-0.6801538442, -0.4994392442), (-0.7277681331, -0.5471953774), (-0.7845440057, -0.592397549), (-0.8519850336, -0.633524014), (-0.9311788014, -0.6694408862), (-1.0228726859, -0.6993589673), (-1.1275350485, -0.7227665334), (-1.2401357326, -0.7386270768), (-1.3386583465, -0.7462222914), (-1.4162265074, -0.7491219853), (-1.4679526668, -0.749878903), (-1.4909526129, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 0.9950191555, 0.9950191555, 0.9950191555, 0.9950191555, 0.9950191555, 0.9950191555], 5)
                _nurbs_edge([(3.5, -0.699951799), (3.4873119191, -0.6930087162), (3.4625239115, -0.6795803391), (3.4271058725, -0.6608108167), (3.3834176126, -0.6385364692), (3.3340945104, -0.6149399918), (3.2882827124, -0.5945939801), (3.2422511534, -0.5753856402), (3.1902107167, -0.5540761285), (3.1264923561, -0.5278292969), (3.0471546949, -0.4953313859), (2.9522052749, -0.4583906576), (2.846308023, -0.4223055616), (2.736577254, -0.3938269917), (2.6310408798, -0.3796859425), (2.5367515095, -0.384791015), (2.4582556747, -0.4108037946), (2.3953812822, -0.4539366559), (2.3433748475, -0.5054752924), (2.2953383932, -0.5549985733), (2.243965645, -0.5927505341), (2.1837008157, -0.6125873576), (2.1123051747, -0.6140152988), (2.0299684038, -0.6002774862), (1.9387208632, -0.5768930746), (1.8417524728, -0.5501336532), (1.7427457893, -0.5252914088), (1.6453367399, -0.5060055742), (1.5527274946, -0.4946264623), (1.467246814, -0.4922844382), (1.3899454, -0.4990763198), (1.3201309958, -0.5141906859), (1.2550363761, -0.5360701397), (1.1906106941, -0.5627013582), (1.122230815, -0.5919043243), (1.045393661, -0.6216017376), (0.9565325599, -0.6501433468), (0.8530747514, -0.6763234245), (0.7332258965, -0.6992895839), (0.5958488471, -0.7184889705), (0.440307123, -0.7336004099), (0.3011231453, -0.7422992376), (0.1884138505, -0.7468977124), (0.1095797431, -0.7491083984), (0.0692390437, -0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5000000522, -0.3000000045), (3.5, -0.699951799))
                _nurbs_edge([(3.5, 0.2632511524), (3.485456793, 0.2512066317), (3.4554922879, 0.2287900179), (3.4079112185, 0.2001824673), (3.3391972656, 0.1720811252), (3.244667245, 0.1533349223), (3.1419988461, 0.1498040747), (3.0322129814, 0.1591187837), (2.9170673778, 0.1772127838), (2.799155828, 0.1980920326), (2.6813236295, 0.2151299277), (2.5661858032, 0.2221397672), (2.4555658902, 0.2146080194), (2.3500564882, 0.1906943344), (2.2483019532, 0.1527574159), (2.1472395787, 0.1070784951), (2.0434487339, 0.0615055531), (1.9341887697, 0.0236808607), (1.8186092033, -0.0010431203), (1.6987885899, -0.0113849243), (1.5811287859, -0.0125225576), (1.4748641651, -0.0135450065), (1.3901032314, -0.024088128), (1.3360492962, -0.0513073789), (1.3191174344, -0.0965957929), (1.3411623334, -0.1526898995), (1.3999848739, -0.2081776326), (1.4897037998, -0.2519047956), (1.6012688772, -0.2769663752), (1.7241522885, -0.2799671135), (1.8478947626, -0.2606997414), (1.9637953819, -0.2216921693), (2.0663377459, -0.1677809619), (2.1552588021, -0.1057837857), (2.2348544513, -0.0436576664), (2.3117547631, 0.0106179021), (2.3931011074, 0.0501242325), (2.4847303246, 0.0699872994), (2.5889298689, 0.0687005087), (2.7043377155, 0.0479635544), (2.8272413505, 0.0115714538), (2.95243175, -0.035390079), (3.0742631785, -0.0874956757), (3.1875565041, -0.139806011), (3.2887399275, -0.1889028686), (3.3757479943, -0.2327914598), (3.4331987376, -0.2629363643), (3.4693104977, -0.2826092289), (3.4902865903, -0.2944204111), (3.5000000522, -0.3000000045)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5, 0.75), (3.5, 0.2632511524))
                _nurbs_edge([(3.5, 0.75), (3.4843904546, 0.7460781688), (3.4534207887, 0.7379218732), (3.4077146273, 0.7247494514), (3.3482712013, 0.7053084532), (3.2763076868, 0.6780430908), (3.2061856938, 0.6483488128), (3.1369073169, 0.6172948519), (3.0667513156, 0.5867353972), (2.9932431922, 0.5593155332), (2.9137715669, 0.5376716018), (2.8261086515, 0.5237446098), (2.7289462877, 0.5180878436), (2.6224870046, 0.519070828), (2.5088524311, 0.52240804), (2.3914108171, 0.5225555598), (2.2742371923, 0.5138958439), (2.1615395539, 0.4919569743), (2.0570737179, 0.4547262181), (1.9636256594, 0.4036939023), (1.8822971548, 0.3456414697), (1.8126211467, 0.2913168165), (1.7531828842, 0.2522413283), (1.7021005899, 0.237965286), (1.6575168425, 0.2534041983), (1.6181942093, 0.2954057469), (1.5832154059, 0.35507011), (1.5514518451, 0.4215117631), (1.5211218224, 0.4850576891), (1.4892784255, 0.5408202389), (1.4523252689, 0.5874650216), (1.4065672857, 0.6258416399), (1.3487394386, 0.6576936529), (1.2765704962, 0.6842991189), (1.1886164598, 0.7065124479), (1.0840686161, 0.7248595976), (0.9868747611, 0.7366620064), (0.9063222711, 0.7439416194), (0.8492219923, 0.7480968469), (0.8198221973, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.8198221973, 0.75), (0.8287883077, 0.744849792), (0.8474770691, 0.7341838094), (0.8777797936, 0.7170881424), (0.9227311616, 0.6920965072), (0.9860400012, 0.6572655107), (1.0550089242, 0.6190955912), (1.1266358562, 0.578125773), (1.1958648496, 0.5352825226), (1.2549532008, 0.4919992597), (1.295307713, 0.4499887412), (1.3095869482, 0.4109823676), (1.2934850253, 0.3765081512), (1.2482411953, 0.3475863972), (1.1799611859, 0.3247873653), (1.0974069575, 0.3084603188), (1.0102637826, 0.2989128212), (0.927293577, 0.2965923906), (0.8543518069, 0.3023094344), (0.7944667232, 0.3169422874), (0.748210705, 0.341045176), (0.7139667689, 0.374523104), (0.6881705092, 0.4161882267), (0.6657045565, 0.4636332188), (0.6407556795, 0.5138553288), (0.6075356393, 0.5637034535), (0.5611330069, 0.6104408358), (0.4980759055, 0.652112218), (0.4159906631, 0.6873575477), (0.3134196063, 0.7153199121), (0.1895875799, 0.7355218548), (0.0732779914, 0.7453123354), (-0.0236626089, 0.7490540601), (-0.0925966868, 0.7499509526), (-0.1281404808, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.1281404808, 0.75), (-0.1141692943, 0.7417218458), (-0.0865112634, 0.7256877183), (-0.0458772085, 0.7032030264), (0.0065943304, 0.6763584988), (0.0693859885, 0.6478806105), (0.1295263188, 0.6240283055), (0.1873252003, 0.6038713976), (0.2432848018, 0.585872869), (0.2982202972, 0.5676447149), (0.3527909748, 0.5464237415), (0.4068271728, 0.5197727065), (0.4587878487, 0.4861699912), (0.5050147297, 0.4457306153), (0.5395192581, 0.4006224414), (0.5561120786, 0.3542621156), (0.5500553254, 0.3106959416), (0.5201931863, 0.2738984903), (0.4699891906, 0.2471439787), (0.4054317057, 0.2325000454), (0.3334813861, 0.2302972515), (0.2603169654, 0.238612376), (0.1896443743, 0.252718803), (0.1231711219, 0.2665756669), (0.0611197383, 0.2743285291), (0.0027250899, 0.2718261372), (-0.0532709537, 0.2580854127), (-0.1081068196, 0.2369175239), (-0.1629290516, 0.2150049332), (-0.2187426161, 0.1996812209), (-0.2763581423, 0.1970171361), (-0.3363271037, 0.2093095314), (-0.3989301861, 0.23457152), (-0.4642300551, 0.2683292377), (-0.5321078314, 0.3048434608), (-0.6023035376, 0.3385033279), (-0.6744596248, 0.365283344), (-0.7481465084, 0.3837481242), (-0.8228156833, 0.3943070592), (-0.8977694671, 0.3987668527), (-0.972113567, 0.3997603581), (-1.044740238, 0.4002536072), (-1.1142384398, 0.4029625887), (-1.1791101575, 0.4100815521), (-1.2381652363, 0.423200197), (-1.2908803444, 0.4431534414), (-1.3377351624, 0.4699184639), (-1.380661528, 0.5024346126), (-1.4226882715, 0.5388676209), (-1.4673595314, 0.5769962267), (-1.5182630784, 0.6145352463), (-1.5784392293, 0.6495340777), (-1.6500948631, 0.6805731312), (-1.734799351, 0.7066375005), (-1.8335696295, 0.7270649316), (-1.9381895252, 0.7403465602), (-2.0298645579, 0.7466951607), (-2.1012730587, 0.7491500723), (-2.1472885606, 0.7498511543), (-2.1650339508, 0.75)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0181818182, 0.0363636364, 0.0545454545, 0.0727272727, 0.0909090909, 0.1090909091, 0.1272727273, 0.1454545455, 0.1636363636, 0.1818181818, 0.2, 0.2181818182, 0.2363636364, 0.2545454545, 0.2727272727, 0.2909090909, 0.3090909091, 0.3272727273, 0.3454545455, 0.3636363636, 0.3818181818, 0.4, 0.4181818182, 0.4363636364, 0.4545454545, 0.4727272727, 0.4909090909, 0.5090909091, 0.5272727273, 0.5454545455, 0.5636363636, 0.5818181818, 0.6, 0.6181818182, 0.6363636364, 0.6545454545, 0.6727272727, 0.6909090909, 0.7090909091, 0.7272727273, 0.7454545455, 0.7636363636, 0.7818181818, 0.8, 0.8181818182, 0.8363636364, 0.8545454545, 0.8727272727, 0.8909090909, 0.9090909091, 0.9272727273, 0.9454545455, 0.9636363636, 0.9818181818, 0.992940092, 0.992940092, 0.992940092, 0.992940092, 0.992940092, 0.992940092], 5)
                Line((-2.222486648, 0.75), (-2.1650339508, 0.75))
                _nurbs_edge([(-2.222486648, 0.75), (-2.2304238932, 0.7391157507), (-2.2439673692, 0.7183590828), (-2.2572899066, 0.6902593021), (-2.2610535044, 0.6588706057), (-2.2428780833, 0.6294828622), (-2.2032367198, 0.6090934489), (-2.1451594146, 0.5958799967), (-2.0733289568, 0.5871027933), (-1.9934652775, 0.5796513354), (-1.9118894781, 0.5704478296), (-1.8350131147, 0.5569317712), (-1.7688705017, 0.5374576572), (-1.7186071674, 0.5118653318), (-1.6880723712, 0.4814468515), (-1.6794490704, 0.4483175657), (-1.6929465448, 0.4149853227), (-1.7262746714, 0.3837644593), (-1.7751652666, 0.3566507029), (-1.8344176937, 0.3353981383), (-1.898752808, 0.3215264194), (-1.9637946141, 0.3163706609), (-2.0268537902, 0.321068433), (-2.0865501835, 0.3361828641), (-2.142556894, 0.3613688169), (-2.195299968, 0.3950024046), (-2.2456840571, 0.4338609896), (-2.294798169, 0.472670695), (-2.3437834017, 0.5051845641), (-2.3937159776, 0.5254192261), (-2.4454847757, 0.5288355079), (-2.4996707545, 0.5135455889), (-2.5564242342, 0.4815208124), (-2.6155668141, 0.4374320943), (-2.6766924289, 0.3874939965), (-2.739268101, 0.3383098857), (-2.8027334919, 0.2957293244), (-2.8666023596, 0.2636755187), (-2.9305586135, 0.2430461959), (-2.9944196427, 0.232513951), (-3.0581054538, 0.2292366231), (-3.1216051626, 0.2296183645), (-3.1849467845, 0.2299930966), (-3.2481611031, 0.2274692853), (-3.3112665842, 0.2201978689), (-3.3742752852, 0.2070615721), (-3.4246095139, 0.1914309991), (-3.4623202719, 0.1767499864), (-3.4874430457, 0.1656491787), (-3.5, 0.159770398)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_131557_45be02b8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1827.1573433705, perimeter: 201.5108466705
            with BuildLine():
                Line((25.5, 10), (-25.5, 10))
                Line((-25.5, 10), (-25.5, -40))
                Line((-25.5, -40), (1.7, -47.2882180341))
                Line((1.7, -47.2882180341), (4.3, -37.5848859344))
                CenterArc((29.1597156911, -25.030323586), 27.85, 124.2141636248, 82.5803574505)
                Line((25.5, 0), (13.5, -2))
                Line((25.5, 10), (25.5, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_131569_5e471769_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 137.773297529, perimeter: 167.0812800718
            with BuildLine():
                CenterArc((11.6567474485, 6.587503894), 3.7130443539, -103.7364627666, 242.7235666454)
                CenterArc((-2.5458244001, 14.8502629913), 12.8032586104, -33.3115990781, 6.2433003632)
                CenterArc((-2.5458244001, 14.8502629913), 12.8032586104, -66.7338494876, 33.4222504095)
                CenterArc((0.5005049054, 9.280422202), 6.5106164446, -116.377652922, 44.3693524314)
                CenterArc((3.0112224654, 12.5269327403), 10.5654529601, -150.6848874538, 29.9270065404)
                CenterArc((-9.8929587321, 6.3405158576), 3.828314565, 15.3504413762, 250.5733673742)
                CenterArc((-12.0232544196, -10.4981297346), 13.15194209, 48.8749831985, 33.0028256163)
                CenterArc((-5.6715343566, -2.9640126006), 3.303526285, 4.0934134085, 41.8210424076)
                CenterArc((-23.8010589488, -3.4481256045), 21.4367159601, -10.017062169, 11.9416381107)
                CenterArc((-8.5481238605, -5.6985829394), 6.040674059, -26.0929780384, 11.92767043)
                CenterArc((-8.5481238605, -5.6985829394), 6.040674059, -30.1234393461, 4.0304613077)
                CenterArc((-0.0289732524, -10.2489543588), 3.6275375593, 155.2488366909, 236.3376489274)
                CenterArc((5.9137332815, -6.2356483949), 3.5500850048, -148.4669118765, 4.9987362849)
                CenterArc((5.9137332815, -6.2356483949), 3.5500850048, -165.2095184773, 16.7426066009)
                CenterArc((5.9137332815, -6.2356483949), 3.5500850048, -170.0667236337, 4.8572051563)
                CenterArc((24.2460194414, -2.2178187865), 22.3148131905, -177.5893214501, 9.5649444441)
                CenterArc((5.9872115694, -4.047141082), 4.1333704334, 130.6757643024, 36.8796809023)
                CenterArc((18.0958723042, -20.2251814476), 24.3332142834, 107.5090667674, 19.9600045364)
            make_face()
            with BuildLine():
                CenterArc((-0.0289732524, -10.2489543588), 2.8042864252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.8929587321, 6.3405158576), 3.0454649546, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.6567474485, 6.587503894), 2.8254101006, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 2.0795826282, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.274
        extrude(amount=1.274)
    return part.part


def model_131586_eff7d729_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1590.4312808798, perimeter: 141.3716694115
            with Locations((0, -70)):
                Circle(22.5)
        # OneSide extrude, distance=70
        extrude(amount=70)
    return part.part


def model_131863_d8b2c0a3_0002():
    """Model: Top Light"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2000, perimeter: 240
            with BuildLine():
                Line((3.7003075412, -25.7199729379), (-16.2996924588, -25.7199729379))
                Line((3.7003075412, 74.2800270621), (3.7003075412, -25.7199729379))
                Line((-16.2996924588, 74.2800270621), (3.7003075412, 74.2800270621))
                Line((-16.2996924588, -25.7199729379), (-16.2996924588, 74.2800270621))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_131863_d8b2c0a3_0005():
    """Model: Extension Slide Rail"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.2821642391, perimeter: 7.1917536522
            with BuildLine():
                Line((0.49, 0.6737540456), (0, 0.7601542661))
                Line((0.49, 1.3262459544), (0.49, 0.6737540456))
                Line((-0.01, 1.2380824641), (0.49, 1.3262459544))
                Line((-0.01, 2.0000000298), (-0.01, 1.2380824641))
                Line((-1.01, 2.0000000298), (-0.01, 2.0000000298))
                Line((-1.01, 1.2380824641), (-1.01, 2.0000000298))
                Line((-1.01, 0), (-1.01, 1.2380824641))
                Line((-0.01, 0), (-1.01, 0))
                Line((-0.01, 0.7619175359), (-0.01, 0))
                Line((0, 0.7601542661), (-0.01, 0.7619175359))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


def model_131882_5b95e1ad_0010():
    """Model: RUEDA v5 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.4350474524, perimeter: 9.6799392528
            with BuildLine():
                CenterArc((0, 0), 0.95, -135, 10)
                Line((-0.5448976145, -0.7781944421), (-0.5977528415, -0.9234129848))
                CenterArc((0, 0), 1.1, -122.9161896914, 25.8323793829)
                Line((-0.0827979556, -0.9463849632), (-0.1356531826, -1.0916035059))
                CenterArc((0, 0), 0.95, -95, 10)
                Line((0.0827979556, -0.9463849632), (0.1356531826, -1.0916035059))
                CenterArc((0, 0), 1.1, -82.9161896914, 25.8323793829)
                Line((0.5448976145, -0.7781944421), (0.5977528415, -0.9234129848))
                CenterArc((0, 0), 0.95, -55, 10)
                Line((0.6717514421, -0.6717514421), (0.805585575, -0.7490206148))
                CenterArc((0, 0), 1.1, -42.9161896914, 25.8323793829)
                Line((0.917629535, -0.2458780928), (1.0514636678, -0.3231472655))
                CenterArc((0, 0), 0.95, -15, 10)
                Line((0.9463849632, -0.0827979556), (1.0985755238, -0.0559626536))
                CenterArc((0, 0), 1.1, -2.9161896914, 25.8323793829)
                Line((0.8609923977, 0.4014873487), (1.0131829583, 0.4283226507))
                CenterArc((0, 0), 0.95, 25, 10)
                Line((0.7781944421, 0.5448976145), (0.8775297756, 0.6632808552))
                CenterArc((0, 0), 1.1, 37.0838103086, 25.8323793829)
                Line((0.4014873487, 0.8609923977), (0.5008226822, 0.9793756383))
                CenterArc((0, 0), 0.95, 65, 10)
                Line((0.2458780928, 0.917629535), (0.2458780928, 1.0721678803))
                CenterArc((0, 0), 1.1, 77.0838103086, 25.8323793829)
                Line((-0.2458780928, 0.917629535), (-0.2458780928, 1.0721678803))
                CenterArc((0, 0), 0.95, 105, 10)
                Line((-0.4014873487, 0.8609923977), (-0.5008226822, 0.9793756383))
                CenterArc((0, 0), 1.1, 117.0838103086, 25.8323793829)
                Line((-0.7781944421, 0.5448976145), (-0.8775297756, 0.6632808552))
                CenterArc((0, 0), 0.95, 145, 10)
                Line((-0.8609923977, 0.4014873487), (-1.0131829583, 0.4283226507))
                CenterArc((0, 0), 1.1, 157.0838103086, 25.8323793829)
                Line((-0.9463849632, -0.0827979556), (-1.0985755238, -0.0559626536))
                CenterArc((0, 0), 0.95, -175, 10)
                Line((-0.917629535, -0.2458780928), (-1.0514636678, -0.3231472655))
                CenterArc((0, 0), 1.1, -162.9161896914, 25.8323793829)
                Line((-0.6717514421, -0.6717514421), (-0.805585575, -0.7490206148))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 75, 30)
                CenterArc((0, 0), 0.15, 105, 330)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_131894_4af6c952_0001():
    """Model: ASIENTO"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1600, perimeter: 160
            with BuildLine():
                Line((-20, 20), (20, 20))
                Line((-20, -20), (-20, 20))
                Line((20, -20), (-20, -20))
                Line((20, 20), (20, -20))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_131958_e7821102_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (2, 0))
                Line((2, 0), (2, 2))
                Line((2, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_132030_c99db4e7_0000():
    """Model: Doggy walker"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000054, -0.0000000034, 3.993414034), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8001932995, perimeter: 8.4208229652
            with BuildLine():
                Line((1.4500000054, 4.1499999966), (-1.4499999946, 4.1499999966))
                Line((1.4500000054, 5.4604114792), (1.4500000054, 4.1499999966))
                Line((1.4500000054, 5.4604114792), (-1.4499999946, 5.4604114792))
                Line((-1.4499999946, 5.4604114792), (-1.4499999946, 4.1499999966))
            make_face()
            # Profile area: 4.6462779043, perimeter: 11.6251254827
            with BuildLine():
                Line((-1.4558323699, 7.0567303627), (1.4500000054, 7.0567303627))
                Line((-1.4558323699, 4.1499999966), (-1.4558323699, 7.0567303627))
                Line((-1.4499999946, 4.1499999966), (-1.4558323699, 4.1499999966))
                Line((-1.4499999946, 5.4604114792), (-1.4499999946, 4.1499999966))
                Line((1.4500000054, 5.4604114792), (-1.4499999946, 5.4604114792))
                Line((1.4500000054, 7.0567303627), (1.4500000054, 5.4604114792))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_132148_a107f53e_0000():
    """Model: Table in glass"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9398.780669118, perimeter: 713.1544153813
            with BuildLine():
                Line((-75, 45), (75, 45))
                Line((-75, -45), (-75, 45))
                Line((75, -45), (-75, -45))
                Line((75, 45), (75, -45))
            make_face()
            with BuildLine():
                Line((-15, -35), (14.1421356237, -35.3553390593))
                Line((-35.3553390593, -14.1421356237), (-15, -35))
                Line((-35, 15), (-35.3553390593, -14.1421356237))
                Line((-14.1421356237, 35.3553390593), (-35, 15))
                Line((15, 35), (-14.1421356237, 35.3553390593))
                Line((35.3553390593, 14.1421356237), (15, 35))
                Line((35, -15), (35.3553390593, 14.1421356237))
                Line((14.1421356237, -35.3553390593), (35, -15))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((-22.6778042491, -22.1314314009), (-0.3863439461, -31.6849143879))
                Line((-22.6778042491, -22.1314314009), (-13.5106652082, -31.5248854857))
                Line((-13.5106652082, -31.5248854857), (-0.3863439461, -31.6849143879))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((-31.6849143879, 0.3863439461), (-22.6778042491, -22.1314314009))
                Line((-31.6849143879, 0.3863439461), (-31.8449432901, -12.737977316))
                Line((-31.8449432901, -12.737977316), (-22.6778042491, -22.1314314009))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((-22.1314314009, 22.6778042491), (-31.6849143879, 0.3863439461))
                Line((-22.1314314009, 22.6778042491), (-31.5248854857, 13.5106652082))
                Line((-31.5248854857, 13.5106652082), (-31.6849143879, 0.3863439461))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((0.3863439461, 31.6849143879), (-22.1314314009, 22.6778042491))
                Line((0.3863439461, 31.6849143879), (-12.737977316, 31.8449432901))
                Line((-12.737977316, 31.8449432901), (-22.1314314009, 22.6778042491))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((13.5106652082, 31.5248854857), (0.3863439461, 31.6849143879))
                Line((22.6778042491, 22.1314314009), (0.3863439461, 31.6849143879))
                Line((22.6778042491, 22.1314314009), (13.5106652082, 31.5248854857))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((31.6849143879, -0.3863439461), (22.6778042491, 22.1314314009))
                Line((31.6849143879, -0.3863439461), (31.8449432901, 12.737977316))
                Line((31.8449432901, 12.737977316), (22.6778042491, 22.1314314009))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((22.1314314009, -22.6778042491), (31.6849143879, -0.3863439461))
                Line((22.1314314009, -22.6778042491), (31.5248854857, -13.5106652082))
                Line((31.5248854857, -13.5106652082), (31.6849143879, -0.3863439461))
            make_face()
            # Profile area: 60.9078509865, perimeter: 50.5029800001
            with BuildLine():
                Line((-0.3863439461, -31.6849143879), (22.1314314009, -22.6778042491))
                Line((-0.3863439461, -31.6849143879), (12.737977316, -31.8449432901))
                Line((12.737977316, -31.8449432901), (22.1314314009, -22.6778042491))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((-10.1561139877, -23.6975993045), (9.5752760949, -23.9381902372))
                Line((-10.1561139877, -23.6975993045), (-0.34024696, -27.9043994592))
                Line((-0.34024696, -27.9043994592), (9.5752760949, -23.9381902372))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((-23.9381902372, -9.5752760949), (-10.1561139877, -23.6975993045))
                Line((-23.9381902372, -9.5752760949), (-19.9719810153, -19.4907991498))
                Line((-19.9719810153, -19.4907991498), (-10.1561139877, -23.6975993045))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((-23.6975993045, 10.1561139877), (-23.9381902372, -9.5752760949))
                Line((-23.6975993045, 10.1561139877), (-27.9043994592, 0.34024696))
                Line((-27.9043994592, 0.34024696), (-23.9381902372, -9.5752760949))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((-9.5752760949, 23.9381902372), (-23.6975993045, 10.1561139877))
                Line((-9.5752760949, 23.9381902372), (-19.4907991498, 19.9719810153))
                Line((-19.4907991498, 19.9719810153), (-23.6975993045, 10.1561139877))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((0.34024696, 27.9043994592), (-9.5752760949, 23.9381902372))
                Line((10.1561139877, 23.6975993045), (-9.5752760949, 23.9381902372))
                Line((10.1561139877, 23.6975993045), (0.34024696, 27.9043994592))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((23.9381902372, 9.5752760949), (10.1561139877, 23.6975993045))
                Line((23.9381902372, 9.5752760949), (19.9719810153, 19.4907991498))
                Line((19.9719810153, 19.4907991498), (10.1561139877, 23.6975993045))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((23.6975993045, -10.1561139877), (23.9381902372, 9.5752760949))
                Line((23.6975993045, -10.1561139877), (27.9043994592, -0.34024696))
                Line((27.9043994592, -0.34024696), (23.9381902372, 9.5752760949))
            make_face()
            # Profile area: 40.322203124, perimeter: 41.0915471477
            with BuildLine():
                Line((9.5752760949, -23.9381902372), (23.6975993045, -10.1561139877))
                Line((9.5752760949, -23.9381902372), (19.4907991498, -19.9719810153))
                Line((19.4907991498, -19.9719810153), (23.6975993045, -10.1561139877))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((20.3251544059, -0.2478308845), (14.5472974081, 14.1968116101))
                Line((20.3251544059, -0.2478308845), (20.4278093195, 8.1711237278))
                Line((20.4278093195, 8.1711237278), (14.5472974081, 14.1968116101))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((14.1968116101, -14.5472974081), (20.3251544059, -0.2478308845))
                Line((14.1968116101, -14.5472974081), (20.2224994924, -8.6667854967))
                Line((20.2224994924, -8.6667854967), (20.3251544059, -0.2478308845))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((-0.2478308845, -20.3251544059), (14.1968116101, -14.5472974081))
                Line((-0.2478308845, -20.3251544059), (8.1711237278, -20.4278093195))
                Line((8.1711237278, -20.4278093195), (14.1968116101, -14.5472974081))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((8.6667854967, 20.2224994924), (0.2478308845, 20.3251544059))
                Line((14.5472974081, 14.1968116101), (0.2478308845, 20.3251544059))
                Line((14.5472974081, 14.1968116101), (8.6667854967, 20.2224994924))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((0.2478308845, 20.3251544059), (-14.1968116101, 14.5472974081))
                Line((0.2478308845, 20.3251544059), (-8.1711237278, 20.4278093195))
                Line((-8.1711237278, 20.4278093195), (-14.1968116101, 14.5472974081))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((-14.1968116101, 14.5472974081), (-20.3251544059, 0.2478308845))
                Line((-14.1968116101, 14.5472974081), (-20.2224994924, 8.6667854967))
                Line((-20.2224994924, 8.6667854967), (-20.3251544059, 0.2478308845))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((-20.3251544059, 0.2478308845), (-14.5472974081, -14.1968116101))
                Line((-20.3251544059, 0.2478308845), (-20.4278093195, -8.1711237278))
                Line((-20.4278093195, -8.1711237278), (-14.5472974081, -14.1968116101))
            make_face()
            # Profile area: 25.0631646735, perimeter: 32.3965169637
            with BuildLine():
                Line((-14.5472974081, -14.1968116101), (-0.2478308845, -20.3251544059))
                Line((-14.5472974081, -14.1968116101), (-8.6667854967, -20.2224994924))
                Line((-8.6667854967, -20.2224994924), (-0.2478308845, -20.3251544059))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((5.6772227303, -14.1930568258), (14.0504094182, -6.0216040364))
                Line((5.6772227303, -14.1930568258), (11.5561793591, -11.8414741742))
                Line((11.5561793591, -11.8414741742), (14.0504094182, -6.0216040364))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((-6.0216040364, -14.0504094182), (5.6772227303, -14.1930568258))
                Line((-6.0216040364, -14.0504094182), (-0.2017338985, -16.5446394773))
                Line((-0.2017338985, -16.5446394773), (5.6772227303, -14.1930568258))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((-14.1930568258, -5.6772227303), (-6.0216040364, -14.0504094182))
                Line((-14.1930568258, -5.6772227303), (-11.8414741742, -11.5561793591))
                Line((-11.8414741742, -11.5561793591), (-6.0216040364, -14.0504094182))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((11.8414741742, 11.5561793591), (6.0216040364, 14.0504094182))
                Line((14.1930568258, 5.6772227303), (6.0216040364, 14.0504094182))
                Line((14.1930568258, 5.6772227303), (11.8414741742, 11.5561793591))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((14.0504094182, -6.0216040364), (14.1930568258, 5.6772227303))
                Line((14.0504094182, -6.0216040364), (16.5446394773, -0.2017338985))
                Line((16.5446394773, -0.2017338985), (14.1930568258, 5.6772227303))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((-5.6772227303, 14.1930568258), (-14.0504094182, 6.0216040364))
                Line((-5.6772227303, 14.1930568258), (-11.5561793591, 11.8414741742))
                Line((-11.5561793591, 11.8414741742), (-14.0504094182, 6.0216040364))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((6.0216040364, 14.0504094182), (-5.6772227303, 14.1930568258))
                Line((6.0216040364, 14.0504094182), (0.2017338985, 16.5446394773))
                Line((0.2017338985, 16.5446394773), (-5.6772227303, 14.1930568258))
            make_face()
            # Profile area: 14.1746879949, perimeter: 24.3633565422
            with BuildLine():
                Line((-14.0504094182, 6.0216040364), (-14.1930568258, -5.6772227303))
                Line((-14.0504094182, 6.0216040364), (-16.5446394773, 0.2017338985))
                Line((-16.5446394773, 0.2017338985), (-14.1930568258, -5.6772227303))
            make_face()
            # Profile area: 374.4234913465, perimeter: 70.4480036763
            with BuildLine():
                Line((4.5322755454, 10.575309606), (-4.2730703632, 10.682675908))
                Line((-4.2730703632, 10.682675908), (-10.575309606, 4.5322755454))
                Line((-10.575309606, 4.5322755454), (-10.682675908, -4.2730703632))
                Line((-10.682675908, -4.2730703632), (-4.5322755454, -10.575309606))
                Line((-4.5322755454, -10.575309606), (4.2730703632, -10.682675908))
                Line((4.2730703632, -10.682675908), (10.575309606, -4.5322755454))
                Line((10.575309606, -4.5322755454), (10.682675908, 4.2730703632))
                Line((10.682675908, 4.2730703632), (4.5322755454, 10.575309606))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5)
    return part.part


def model_132321_74af461c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7944257522, perimeter: 11.6578292113
            with BuildLine():
                CenterArc((5.1619172949, 3.3900605339), 0.5, 28.0144761829, 120)
                Line((4.0661873123, 2.5794613976), (4.7378263165, 3.6549130249))
                CenterArc((4.4902782908, 2.3146089066), 0.5, 148.0144761829, 120)
                Line((5.7401427265, 1.7709784742), (4.4729547946, 1.8149091003))
                CenterArc((5.7574662227, 2.2706782805), 0.5, -91.9855238171, 120)
                Line((5.6033317696, 3.6249078493), (6.1988806974, 2.5055255959))
            make_face()
            with BuildLine():
                CenterArc((5.1619172949, 3.3900605339), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7574662227, 2.2706782805), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.4902782908, 2.3146089066), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_132430_321b9be8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.6036731188, perimeter: 23.9389360204
            Circle(3.81)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_132444_13a66007_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.6692174436, perimeter: 19.9491133503
            Circle(3.175)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


def model_132461_14abd2d0_0000():
    """Model: F#4 Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=10.541
        extrude(amount=10.541)
    return part.part


def model_132461_14abd2d0_0001():
    """Model: D4 Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=9.39292
        extrude(amount=9.39292)
    return part.part


def model_132461_14abd2d0_0002():
    """Model: E4 Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=9.95172
        extrude(amount=9.95172)
    return part.part


def model_132461_14abd2d0_0003():
    """Model: D#4 Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=9.66724
        extrude(amount=9.66724)
    return part.part


def model_132461_14abd2d0_0004():
    """Model: C5 key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=12.53744
        extrude(amount=12.53744)
    return part.part


def model_132461_14abd2d0_0005():
    """Model: F4 Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=10.24128
        extrude(amount=10.24128)
    return part.part


def model_132461_14abd2d0_0006():
    """Model: G4 Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7625791443, perimeter: 3.5255200486
            with BuildLine():
                Line((0, 1.00076), (0, 0))
                Line((0, 0), (0.7620000243, 0))
                Line((0.7620000243, 0), (0.7620000243, 1.00076))
                Line((0.7620000243, 1.00076), (0, 1.00076))
            make_face()
        # OneSide extrude, distance=10.85088
        extrude(amount=10.85088)
    return part.part


def model_132527_404df1cf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Four AMERiCANO plates final -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 18.4714733821, perimeter: 61.687375021
            with BuildLine():
                CenterArc((5.3117853682, 5.3563949294), 0.5, -33.13575247, 176.282262643)
                Line((4.9116994735, 5.6562803689), (4.7526125478, 5.6562348111))
                CenterArc((4.7525552737, 5.8562348029), 0.2, 179.9999999974, 90.0164078214)
                Line((4.5525552737, 5.8562348029), (4.5525552737, 6.4561202793))
                CenterArc((4.3525552737, 6.4561202793), 0.2, -0.0000000026, 90.016407824)
                Line((1.8131289345, 6.6553930708), (4.3524979996, 6.6561202711))
                CenterArc((1.8131862085, 6.455393079), 0.2, 90.0164078188, 89.9835921786)
                Line((1.6131862085, 5.8552785062), (1.6131862085, 6.455393079))
                CenterArc((1.4131862085, 5.8552785062), 0.2, -89.9835921812, 89.9835921786)
                Line((1.2523940507, 5.6552324519), (1.4132434826, 5.6552785144))
                CenterArc((0.8524799783, 5.355117916), 0.5, 36.8863054647, 176.2820122651)
                Line((1.2075851777, 3.8978958607), (0.4339464953, 5.0815676946))
                CenterArc((0.03023172, 3.12838682), 1.4065224236, -33.0837756737, 66.2520934086)
                Line((0.4368280461, 1.1758037673), (1.2087193349, 2.3606158454))
                CenterArc((0.8557647069, 0.9028714053), 0.5, 146.9162243273, 156.2718259076)
                Line((1.1294590538, 0.484432157), (2.3130048383, 1.2585703191))
                CenterArc((3.0834390005, 0.0806874168), 1.407471822, 56.8370896499, 66.3509605886)
                Line((5.0372416068, 0.4852894736), (3.8533562643, 1.258908252))
                CenterArc((5.3107523272, 0.9038487714), 0.5, -123.1629103553, 156.2720762785)
                Line((4.9571238132, 2.3614794892), (5.7295679987, 1.1769667557))
                CenterArc((6.1355133492, 3.1299306162), 1.4068116551, 146.864247531, 66.2449183912)
                Line((5.7304742616, 5.0830826345), (4.9574805189, 3.89892846))
            make_face()
            with BuildLine():
                CenterArc((4.6097096873, 1.6055423126), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5564993946, 1.6048724781), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5542497316, 4.6541515672), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3117853682, 5.3563949294), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0829284794, 6.3562347826), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3107523272, 0.9038487714), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0815115692, 6.3562347825), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8524799783, 5.355117916), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8557647069, 0.9028714053), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.082927551, 6.3562347824), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3327698812, 3.8806388874), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.3131532192, 2.3330686828), (3.6546938024, 1.992064603))
                CenterArc((3.5840387271, 1.9212983658), 0.1, -105.2149803437, 150.2600167773)
                CenterArc((3.0834390005, 0.0806874168), 1.807471822, 74.7850196595, 30.4629723621)
                CenterArc((2.5817788659, 1.9210096335), 0.1, 134.9839413312, 150.2640506881)
                Line((2.852491394, 2.3329521912), (2.5110880091, 1.9917401274))
                CenterArc((3.0828806145, 2.1024337891), 0.3259109183, 45.0450364336, 89.9389048976)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0827698812, 3.1306388873), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8327698811, 2.3806388873), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2776513169, 2.8894881385), (1.9388593634, 2.5508860427))
                CenterArc((1.8681685066, 2.6216165366), 0.1, 164.5849874551, 150.3989538749)
                CenterArc((0.03023172, 3.12838682), 1.8065224236, -15.4150125499, 30.800621238)
                CenterArc((1.8684283361, 3.6342138182), 0.1, 45.0450364336, 150.3405722461)
                Line((1.9390834114, 3.7049800555), (2.277530548, 3.3670645631))
                CenterArc((2.0390572069, 3.1282160307), 0.3375176378, -45.0160586701, 90.0610951036)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0827698812, 3.1306388873), 0.7, -2.1926702616, 4.1713585773)
                CenterArc((4.1010218649, 3.1287374576), 0.3197340378, 134.9839413351, 40.3390132212)
                Line((4.2261472152, 3.7058382207), (3.8749991341, 3.3548869217))
                CenterArc((4.296838072, 3.6351077268), 0.1, -15.3629647804, 150.3469061116)
                CenterArc((6.1355133492, 3.1299306162), 1.8068116551, 164.6370352201, 30.813282876)
                CenterArc((4.2976104031, 2.621950844), 0.1, -134.9549635664, 150.4052816629)
                Line((3.8751135398, 2.9024737098), (4.2269553278, 2.5511846067))
                CenterArc((4.1010218649, 3.1287374576), 0.3197340378, -175.5369365021, 40.5819729357)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.6104172021, 4.6550267633), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.4319087883, 6.0562347825), (4.0525552737, 6.0562347824))
                CenterArc((4.0525552737, 5.8562347824), 0.2, 1.2458524312, 88.7541475688)
                CenterArc((4.0525552737, 5.8649317878), 0.2, -45.0000000013, 43.7541475649)
                Line((4.1939766299, 5.7235104316), (3.8679550819, 5.3974888836))
                CenterArc((3.0818956182, 6.1835483476), 1.1116559547, -68.7937137308, 23.7937137183)
                CenterArc((3.4323184944, 5.3403732952), 0.2, -179.9544947042, 104.9334771543)
                Line((3.2319088513, 5.8560759391), (3.2323185575, 5.3402144518))
                CenterArc((3.4319087883, 5.8562347825), 0.2, 90, 90.0455052907)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2962864914, 5.3970388045), (1.9718458733, 5.7211079943))
                CenterArc((2.1131862085, 5.8626103251), 0.2, -179.0867321366, 44.1195477822)
                CenterArc((2.1131862085, 5.8562347826), 0.2, 89.9999999949, 89.0867321366)
                Line((2.1131862085, 6.0562347826), (2.7319085675, 6.0562347826))
                CenterArc((2.7319085675, 5.8562347826), 0.2, 0.0455052958, 89.9544947042)
                Line((2.9323182781, 5.3404471648), (2.9319085044, 5.856393626))
                CenterArc((2.7323183412, 5.3402883214), 0.2, -105.6069315526, 105.6524368484)
                CenterArc((3.0818956182, 6.1835483476), 1.1116559547, -134.9671843752, 23.6907403092)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3327698811, 2.3806388874), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8327698812, 3.8806388873), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0818956182, 6.1835483476), 1.7116559547, -111.4586915032, 0.1822474063)
                Line((2.4607901793, 4.5885580214), (2.5170892685, 4.5697843004))
                CenterArc((2.7323183412, 5.3402883214), 0.8, -105.6069315689, 41.5583728542)
                CenterArc((3.4323184944, 5.3403732952), 0.8, -115.9375308793, 40.9165133094)
                Line((3.7010475492, 4.5877986826), (3.6390902554, 4.567556733))
                CenterArc((3.0818956182, 6.1835483476), 1.7116559547, -68.7937137597, 0.2761103665)
                CenterArc((3.7453518387, 4.4977479023), 0.1, -45.0160586688, 156.4984552789)
                Line((3.2237884026, 3.8350950126), (3.8160426955, 4.4270174084))
                CenterArc((3.082406689, 3.9765560003), 0.2, -134.9549635664, 89.9389048964)
                Line((2.9410965384, 3.8350235258), (2.348481849, 4.4267073161))
                CenterArc((2.4191369242, 4.4974735534), 0.1, 68.5413085545, 156.503727879)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.2542523709, perimeter: 82.2651747746
            with BuildLine():
                CenterArc((7.2784187395, 5.662038248), 0.5, 36.8863054647, 196.2860679213)
                Line((6.9787139286, 5.2618170262), (6.9787694493, 5.1865621646))
                CenterArc((7.0087086425, 4.7375592195), 0.45, 93.8147943371, 89.5601214558)
                Line((6.559489079, 4.7110680181), (6.5597772401, 2.1685527037))
                CenterArc((7.0087086424, 2.1375592195), 0.45, 176.0506604173, 90.4638165794)
                Line((6.9813502904, 1.6883916332), (6.9814084424, 1.6095702979))
                CenterArc((7.2817034682, 1.2097917373), 0.5, 126.9121686777, 196.2305036213)
                Line((7.6817692746, 0.9098794993), (7.7587086529, 0.9098963788))
                CenterArc((8.2087086421, 0.9099951029), 0.45, -179.9874300592, 90.0000000051)
                Line((8.2088073662, 0.4599951137), (10.8088073662, 0.4605655198))
                CenterArc((10.8087086421, 0.910565509), 0.45, -89.9874300541, 90)
                Line((11.2587086313, 0.9106642331), (11.3367569142, 0.9106813559))
                CenterArc((11.7366910885, 1.2107691034), 0.5, -143.1175324082, 196.2343414953)
                Line((12.0368019209, 1.6884370002), (12.0367838849, 1.6106994893))
                CenterArc((12.0087086424, 2.1375592193), 0.45, -86.4207251081, 86.4207251072)
                Line((12.4587086424, 2.1375592193), (12.4587086425, 4.7375592193))
                CenterArc((12.0087086425, 4.7375592193), 0.45, 0, 86.3171785478)
                Line((12.0376313168, 5.2632456687), (12.0376135411, 5.186629934))
                CenterArc((11.7377241294, 5.6633152613), 0.5, -53.1433956212, 196.4332458235)
                Line((11.2587086425, 5.9621988464), (11.3368892475, 5.9621988464))
                CenterArc((10.8087086425, 5.9621988464), 0.45, 0, 90)
                Line((8.2087086425, 6.4121988464), (10.8087086425, 6.4121988464))
                CenterArc((8.2087086425, 5.9621988464), 0.45, 90, 90.002934214)
                Line((7.678332812, 5.9621527838), (7.7587086431, 5.9621758011))
            make_face()
            with BuildLine():
                CenterArc((11.0356484485, 1.9124626446), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.0363559633, 4.9619470953), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.9801884928, 4.9610718992), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.9824381558, 1.9117928101), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.7366910885, 1.2107691034), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.2784187395, 5.662038248), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.2817034682, 1.2097917373), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.7377241294, 5.6633152613), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((11.8587086424, 2.1384119628), (11.8587086425, 4.7375592193))
                CenterArc((12.0087086425, 4.7375592193), 0.15, 0, 179.9999999974)
                Line((12.1587086424, 2.1384119628), (12.1587086425, 4.7375592193))
                CenterArc((12.0087086424, 2.1384119628), 0.15, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((8.2087086425, 6.1121988464), (10.8087086425, 6.1121988464))
                CenterArc((10.8087086425, 5.9621988464), 0.15, -90, 180)
                Line((10.8087086425, 5.8121988464), (8.2087086425, 5.8121988464))
                CenterArc((8.2087086425, 5.9621988464), 0.15, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((8.208675734, 1.0599950993), (10.808675734, 1.0605655054))
                CenterArc((10.8087086421, 0.910565509), 0.15, -89.9874300567, 180.0000000051)
                Line((10.8087415501, 0.7605655126), (8.2087415501, 0.7599951065))
                CenterArc((8.2087086421, 0.9099951029), 0.15, 90.0125699459, 179.9999999974)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.0087086425, 4.7375592195), 0.15, 0, 179.9999999923)
                Line((7.1587086424, 2.1375592195), (7.1587086425, 4.7375592195))
                CenterArc((7.0087086424, 2.1375592195), 0.15, 180, 180)
                Line((6.8587086425, 4.7375592195), (6.8587086424, 2.1375592195))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.5808141016, 2.4153837419), (7.5793091626, 4.4552355152))
                CenterArc((7.7793091082, 4.4553830689), 0.2, 45.0450364336, 134.9972345983)
                Line((7.9206192587, 4.5969155435), (8.9423860031, 3.5767538247))
                CenterArc((8.8010758526, 3.4352213501), 0.2, -45.0160586688, 90.0610951036)
                Line((8.9424575662, 3.2937603623), (7.9221957608, 2.2740703078))
                CenterArc((7.7808140472, 2.4155312956), 0.2, -179.9577289682, 134.9416702981)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.0746622551, 3.5770401532), (11.096062386, 4.5978678954))
                CenterArc((11.2374440996, 4.4564069076), 0.2, -0.0132932671, 134.9972346021)
                Line((11.4374440942, 4.4563605054), (11.4369972599, 2.5304442789))
                Line((11.4369972599, 2.5304442789), (11.4369972599, 2.4162296219))
                CenterArc((11.2369972599, 2.416229622), 0.2, -134.9549635664, 134.9549635587)
                Line((11.0956871094, 2.2746971474), (10.0747338181, 3.2940466909))
                CenterArc((10.2160439686, 3.4355791654), 0.2, 134.9839413312, 90.0610950985)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.6711743073, 5.0215083371), (9.6497629072, 4.0006693321))
                CenterArc((9.5083811936, 4.1421303199), 0.2, -134.9549635703, 89.9389049015)
                Line((9.3670710431, 4.0005978454), (8.3452119997, 5.0208517181))
                CenterArc((8.4865221503, 5.1623841926), 0.2, 90.0164078188, 135.0286286109)
                Line((8.4864648762, 5.3623841844), (10.5297353197, 5.3629693167))
                CenterArc((10.5297925938, 5.1629693249), 0.2, -45.0160586688, 135.0324664876)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.528550531, 1.5105040604), (8.4895978981, 1.5100567408))
                CenterArc((8.4895540207, 1.710056736), 0.2, 134.9839413351, 135.0286286083)
                Line((8.3481723071, 1.8515177238), (9.367356914, 2.8701311834))
                CenterArc((9.5087386276, 2.7286701956), 0.2, 45.0450364336, 89.9389048976)
                Line((9.6500487782, 2.8702026702), (10.6698168042, 1.8520365301))
                CenterArc((10.5285066536, 1.7105040556), 0.2, -89.9874300567, 135.0324664902)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 12.4645953974, perimeter: 46.7976747289
            with BuildLine():
                Line((13.7558064371, 0.4523105281), (14.4613062084, 0.913766522))
                CenterArc((14.7350005554, 0.4953272738), 0.5, 32.0765900121, 91.1114602367)
                CenterArc((15.7094403711, 1.1060375533), 0.65, -147.9234099896, 115.8781779634)
                CenterArc((16.6842142828, 0.4958606763), 0.5, 56.8370896601, 91.1176783212)
                Line((17.6635889901, 0.4531678447), (16.9577250031, 0.9144199743))
                CenterArc((17.9370997105, 0.8717271425), 0.5, -123.1629103553, 156.2720762785)
                Line((17.5834711965, 2.3293578603), (18.355915382, 1.1448451268))
                CenterArc((18.7618607325, 3.0978089873), 1.4068116551, 146.864247531, 66.2449183912)
                Line((18.3568216449, 5.0509610056), (17.5838279022, 3.8668068311))
                CenterArc((17.9381327515, 5.3242733004), 0.5, -33.135752469, 176.282262642)
                Line((17.5380468567, 5.62415874), (17.378959931, 5.6241131822))
                CenterArc((17.378902657, 5.824113174), 0.2, 179.9999999974, 90.0164078188)
                Line((17.178902657, 5.824113174), (17.178902657, 6.2239413681))
                CenterArc((16.778902657, 6.2239413681), 0.4, 0, 90.0164078214)
                Line((14.6394190436, 6.6233286996), (16.7787881088, 6.6239413517))
                CenterArc((14.6395335918, 6.223328716), 0.4, 90.0164078214, 89.9835921786)
                Line((14.2395335918, 5.8231568773), (14.2395335918, 6.223328716))
                CenterArc((14.0395335918, 5.8231568773), 0.2, -89.9835921837, 89.9835921837)
                Line((13.878741434, 5.623110823), (14.0395908659, 5.6231568855))
                CenterArc((13.4788273616, 5.3229962871), 0.5, 36.8863054657, 176.2820122641)
                Line((13.833932561, 3.8657742318), (13.0602938785, 5.0494460657))
                CenterArc((12.6565791033, 3.0962651911), 1.4065224236, -33.0837756737, 66.2520934086)
                Line((13.0631754294, 1.1436821384), (13.8350667182, 2.3284942165))
                CenterArc((13.4821120902, 0.8707497764), 0.5, 146.9162243315, 156.2718259034)
            make_face()
            with BuildLine():
                CenterArc((13.4821120902, 0.8707497764), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((13.4788273616, 5.3229962871), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.9370997105, 0.8717271425), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.9381327515, 5.3242733004), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((14.0365863153, 5.1231560046), (14.039734051, 5.123156906))
                CenterArc((14.0395335918, 5.8231568773), 0.7, -89.9835921879, 89.9835921824)
                Line((14.7395335918, 5.8231568772), (14.7395335918, 5.9234146148))
                CenterArc((14.9395335918, 5.9234146148), 0.2, 90.0164078214, 89.983592176)
                Line((14.9394763177, 6.1234146066), (16.4788453829, 6.1238554364))
                CenterArc((16.478902657, 5.9238554446), 0.2, 0, 90.0164078188)
                Line((16.678902657, 5.9238554446), (16.678902657, 5.824113174))
                CenterArc((17.378902657, 5.824113174), 0.7, 180, 90.016407806)
                Line((17.3791031161, 5.1241132027), (17.3804877454, 5.1241135992))
                Line((17.3804877454, 5.1241135992), (17.3804936988, 5.1241094315))
                CenterArc((17.3791695235, 4.8922205039), 0.2318927083, -33.1357524587, 122.8085749877)
                Line((17.5733513263, 4.7654622474), (17.1651390087, 4.1401191259))
                CenterArc((18.7618607325, 3.0978089873), 1.9068116551, 146.8642475313, 66.2449183764)
                CenterArc((16.9424280393, 1.8673217885), 0.2916763604, 25.8500946573, 14.5181426131)
                CenterArc((16.9424280393, 1.8673217885), 0.2916763604, -115.8813314803, 141.7314261376)
                Line((16.8151087807, 1.6049005516), (16.7532143679, 1.645345921))
                CenterArc((15.7097863837, 0.0485657879), 1.907471822, 56.8370896515, 66.3509605837)
                CenterArc((14.4936132851, 1.8840882187), 0.2946457447, -59.3494425141, 5.0749855185)
                CenterArc((14.4936132851, 1.8840882187), 0.2946457447, 149.4213477876, 151.2292096984)
                CenterArc((14.4936132851, 1.8840882187), 0.2946457447, 144.4111008727, 5.0102469149)
                CenterArc((12.6565791033, 3.0962651911), 1.9065224236, -33.0837756785, 66.252093409)
                Line((14.252466044, 4.139324453), (13.844890917, 4.762916847))
                CenterArc((14.039800732, 4.8903083825), 0.232848533, 90.7986004091, 122.3697173352)
                Line((14.0365553461, 5.1231342977), (14.0365863153, 5.1231560046))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((15.7094403711, 1.1060375533), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 20.2452408214, perimeter: 53.3801781607
            with BuildLine():
                Line((19.5174134298, 1.7197367036), (19.1006493216, 1.07788402))
                CenterArc((19.5194837668, 0.8047948267), 0.5, 146.8947727182, 156.2718259076)
                Line((19.7930214303, 0.3862531363), (20.5002127879, 0.8484376118))
                CenterArc((20.7737504515, 0.4298959214), 0.5, 32.0156918803, 91.1509067594)
                CenterArc((21.7488388241, 1.0395701505), 0.65, -147.9843081213, 115.5187373453)
                Line((22.2992692124, 0.6938442653), (22.2972530272, 0.6906548859))
                CenterArc((22.7226772035, 0.4279012768), 0.5, 56.8156380511, 91.0513904719)
                Line((23.7008040305, 0.3856473743), (22.9963446137, 0.8463581427))
                CenterArc((23.9744714408, 0.8041042401), 0.5, -123.1843619608, 156.272076274)
                Line((23.9750263263, 1.7191338672), (24.3933893386, 1.0770654001))
                Line((23.9766166349, 4.3416200718), (23.9750263263, 1.7191338672))
                Line((24.3957580559, 4.9831806658), (23.9766166349, 4.3416200718))
                CenterArc((23.9771715203, 5.2566496992), 0.5, -33.157204079, 176.2822626471)
                Line((23.5771979311, 5.5566849103), (23.4181109995, 5.5566989148))
                CenterArc((23.4181286057, 5.7566989141), 0.2, 179.9785483884, 90.0164078214)
                Line((23.2182783158, 6.1566019604), (23.2181286197, 5.7567737943))
                CenterArc((22.8182783439, 6.1567517209), 0.4, -0.0214516116, 90.0164078214)
                Line((20.6789444116, 6.5569400496), (22.8183135562, 6.5567517193))
                CenterArc((20.6789091993, 6.1569400511), 0.4, 89.9949562098, 89.9835921837)
                Line((20.2787594025, 5.756918001), (20.2789092273, 6.1570898116))
                CenterArc((20.0787594165, 5.7569928812), 0.2, -90.0050437928, 89.9835921811)
                Line((19.9178923725, 5.5570070417), (20.0787418103, 5.556992882))
                CenterArc((19.5178659648, 5.2570422552), 0.5, 36.8648538556, 176.2820122651)
                Line((19.518198425, 4.3421003229), (19.0992300936, 4.9836487524))
                Line((19.518198425, 4.3421003229), (19.5174134298, 1.7197367036))
            make_face()
            with BuildLine():
                CenterArc((21.7488388241, 1.0395701505), 0.37, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((21.7471733237, 3.0295694535), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((21.7471733237, 3.0295694535), 1, 56.4994487566, 66.9871770386)
                Line((21.1954310023, 3.8635840881), (20.9193523052, 4.1394355927))
                CenterArc((21.1313970011, 4.3516549296), 0.3, 89.9949601565, 135.0286246641)
                Line((21.1314233896, 4.6516549285), (22.363338736, 4.6515465669))
                CenterArc((22.3633123474, 4.3515465681), 0.3, -45.0375102778, 135.0324704344)
                Line((22.5753054582, 4.139275701), (22.2991183318, 3.8634499653))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((20.7305308543, 3.7626489434), (20.9127047411, 3.5806249723))
                CenterArc((21.7471733237, 3.0295694535), 1, 146.5605438615, 66.8649868236)
                Line((20.9125708345, 2.4787167645), (20.7308575048, 2.2972412064))
                CenterArc((20.518864394, 2.5095120734), 0.3, -179.9791805772, 134.9416702994)
                Line((20.2188644138, 2.5094030632), (20.2184861782, 3.5503205963))
                CenterArc((20.5184861584, 3.5504296065), 0.3, 45.0235848245, 134.9972345983)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((22.7634604703, 2.296844994), (22.5816419062, 2.4785139347))
                CenterArc((21.7471733237, 3.0295694535), 1, -33.4394561427, 66.864986832)
                Line((22.5817758128, 3.5804221426), (22.7641434618, 3.7625511637))
                CenterArc((22.9761365726, 3.5502802967), 0.3, -0.0347448761, 134.9972346021)
                Line((23.2761365174, 3.5500983729), (23.275505111, 2.5088824072))
                CenterArc((22.9755051662, 2.5090643309), 0.3, -134.9764151755, 134.9416702994)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((20.7788717662, 6.2569400508), (22.7182931494, 6.2569400508))
                CenterArc((22.7182931494, 6.0569400508), 0.2, 0.0085074072, 89.9914925928)
                Line((22.9182931472, 6.0569697472), (22.9183398901, 5.7421648225))
                CenterArc((23.4181286057, 5.7566989141), 0.5, -179.9984806642, 1.6641995131)
                CenterArc((22.7181285797, 5.7567605356), 0.2, -90.0050437928, 89.9835921869)
                Line((22.7181109735, 5.5567605364), (20.7787418363, 5.5569312605))
                CenterArc((20.7787594425, 5.7569312597), 0.2, -179.9640242538, 89.958980461)
                CenterArc((20.0787594165, 5.7569928812), 0.5, -1.7112884029, 1.6898367972)
                Line((20.5788717802, 6.057014931), (20.5785364144, 5.7420612929))
                CenterArc((20.7788717662, 6.0569400508), 0.2, 90, 89.9785483884)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((19.5194837668, 0.8047948267), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((19.5178659648, 5.2570422552), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((23.9744714408, 0.8041042401), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((23.9771715203, 5.2566496992), 0.19, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)
    return part.part


def model_132569_1cbfed5b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((18, 10.3923048454), (15.8349364905, 11.6423048454))
                CenterArc((16.9174682453, 11.0173048454), 1.25, -30, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((16.9174682453, 11.0173048454), 1.25, 150, 180)
                Line((18, 10.3923048454), (15.8349364905, 11.6423048454))
            make_face()
            # Profile area: 51.4828222963, perimeter: 52.4297153521
            with BuildLine():
                Line((0, 0), (10.556624327, 0))
                CenterArc((10.556624327, 2.5), 2.5, -90, 60)
                Line((12.7216878365, 1.25), (18, 10.3923048454))
                CenterArc((16.9174682453, 11.0173048454), 1.25, 150, 180)
                Line((15.8349364905, 11.6423048454), (11.2783121635, 3.75))
                CenterArc((9.1132486541, 5), 2.5, -90, 60)
                Line((9.1132486541, 2.5), (0, 2.5))
                CenterArc((0, 1.25), 1.25, -90, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((0, 2.5), (0, 0))
                CenterArc((0, 1.25), 1.25, 90, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((0, 1.25), 1.25, -90, 180)
                Line((0, 2.5), (0, 0))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)
    return part.part


def model_132601_ae380b60_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 466.1281, perimeter: 86.36
            with BuildLine():
                Line((21.59, -21.59), (0, -21.59))
                Line((21.59, 0), (21.59, -21.59))
                Line((0, 0), (21.59, 0))
                Line((0, -21.59), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_132643_03c61ba8_0000():
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
        # HoldBar -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 71.7088304441, perimeter: 80.488248256
            with BuildLine():
                Line((4.1868246, 19.037837), (4.1868246, 29.0327539))
                Line((4.1868246, 29.0327539), (1.0131681, 29.0327539))
                Line((1.0131681, 29.0327539), (1.0131681, 1.0131716))
                Line((1.0131681, 1.0131716), (4.1868246, 1.0131716))
                Line((4.1868246, 1.0131716), (4.1868246, 11.0080625))
                Line((4.1868246, 11.0080625), (2.2080627, 11.0080625))
                Line((2.2080627, 11.0080625), (2.2080627, 19.037837))
                Line((2.2080627, 19.037837), (4.1868246, 19.037837))
            make_face()
            with BuildLine():
                _nurbs_edge([(3.7875916, 19.5459), (3.7875916, 19.47888), (3.7518368, 19.4169509), (3.6937958, 19.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 19.3834409), (3.6357548, 19.3499309), (3.5642452, 19.3499309), (3.5062042, 19.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 19.3834409), (3.4481632, 19.4169509), (3.4124084, 19.47888), (3.4124084, 19.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.4124084, 19.5459), (3.4124084, 19.61292), (3.4481632, 19.6748491), (3.5062042, 19.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 19.7083591), (3.5642452, 19.7418691), (3.6357548, 19.7418691), (3.6937958, 19.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 19.7083591), (3.7518368, 19.6748491), (3.7875916, 19.61292), (3.7875916, 19.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.7875916, 28.5459), (3.7875916, 28.47888), (3.7518368, 28.4169509), (3.6937958, 28.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 28.3834409), (3.6357548, 28.3499309), (3.5642452, 28.3499309), (3.5062042, 28.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 28.3834409), (3.4481632, 28.4169509), (3.4124084, 28.47888), (3.4124084, 28.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.4124084, 28.5459), (3.4124084, 28.61292), (3.4481632, 28.6748491), (3.5062042, 28.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 28.7083591), (3.5642452, 28.7418691), (3.6357548, 28.7418691), (3.6937958, 28.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 28.7083591), (3.7518368, 28.6748491), (3.7875916, 28.61292), (3.7875916, 28.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.5062042, 10.3375409), (3.4481632, 10.3710509), (3.4124084, 10.43298), (3.4124084, 10.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.4124084, 10.5), (3.4124084, 10.56702), (3.4481632, 10.6289491), (3.5062042, 10.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 10.6624591), (3.5642452, 10.6959691), (3.6357548, 10.6959691), (3.6937958, 10.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 10.6624591), (3.7518368, 10.6289491), (3.7875916, 10.56702), (3.7875916, 10.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.7875916, 10.5), (3.7875916, 10.43298), (3.7518368, 10.3710509), (3.6937958, 10.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 10.3375409), (3.6357548, 10.3040309), (3.5642452, 10.3040309), (3.5062042, 10.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.4124084, 10.5), (1.4124084, 10.56702), (1.4481632, 10.6289491), (1.5062042, 10.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 10.6624591), (1.5642452, 10.6959691), (1.6357548, 10.6959691), (1.6937958, 10.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 10.6624591), (1.7518368, 10.6289491), (1.7875916, 10.56702), (1.7875916, 10.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.7875916, 10.5), (1.7875916, 10.43298), (1.7518368, 10.3710509), (1.6937958, 10.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 10.3375409), (1.6357548, 10.3040309), (1.5642452, 10.3040309), (1.5062042, 10.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 10.3375409), (1.4481632, 10.3710509), (1.4124084, 10.43298), (1.4124084, 10.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.6937958, 4.3375409), (3.6357548, 4.3040309), (3.5642452, 4.3040309), (3.5062042, 4.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 4.3375409), (3.4481632, 4.3710509), (3.4124084, 4.43298), (3.4124084, 4.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.4124084, 4.5), (3.4124084, 4.56702), (3.4481632, 4.6289491), (3.5062042, 4.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 4.6624591), (3.5642452, 4.6959691), (3.6357548, 4.6959691), (3.6937958, 4.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 4.6624591), (3.7518368, 4.6289491), (3.7875916, 4.56702), (3.7875916, 4.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.7875916, 4.5), (3.7875916, 4.43298), (3.7518368, 4.3710509), (3.6937958, 4.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.7875916, 1.5), (3.7875916, 1.43298), (3.7518368, 1.3710509), (3.6937958, 1.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 1.3375409), (3.6357548, 1.3040309), (3.5642452, 1.3040309), (3.5062042, 1.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 1.3375409), (3.4481632, 1.3710509), (3.4124084, 1.43298), (3.4124084, 1.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.4124084, 1.5), (3.4124084, 1.56702), (3.4481632, 1.6289491), (3.5062042, 1.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 1.6624591), (3.5642452, 1.6959691), (3.6357548, 1.6959691), (3.6937958, 1.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 1.6624591), (3.7518368, 1.6289491), (3.7875916, 1.56702), (3.7875916, 1.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.5062042, 4.3375409), (1.4481632, 4.3710509), (1.4124084, 4.43298), (1.4124084, 4.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.4124084, 4.5), (1.4124084, 4.56702), (1.4481632, 4.6289491), (1.5062042, 4.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 4.6624591), (1.5642452, 4.6959691), (1.6357548, 4.6959691), (1.6937958, 4.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 4.6624591), (1.7518368, 4.6289491), (1.7875916, 4.56702), (1.7875916, 4.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.7875916, 4.5), (1.7875916, 4.43298), (1.7518368, 4.3710509), (1.6937958, 4.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 4.3375409), (1.6357548, 4.3040309), (1.5642452, 4.3040309), (1.5062042, 4.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.4124084, 19.5459), (1.4124084, 19.61292), (1.4481632, 19.6748491), (1.5062042, 19.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 19.7083591), (1.5642452, 19.7418691), (1.6357548, 19.7418691), (1.6937958, 19.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 19.7083591), (1.7518368, 19.6748491), (1.7875916, 19.61292), (1.7875916, 19.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.7875916, 19.5459), (1.7875916, 19.47888), (1.7518368, 19.4169509), (1.6937958, 19.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 19.3834409), (1.6357548, 19.3499309), (1.5642452, 19.3499309), (1.5062042, 19.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 19.3834409), (1.4481632, 19.4169509), (1.4124084, 19.47888), (1.4124084, 19.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.7875916, 1.5), (1.7875916, 1.43298), (1.7518368, 1.3710509), (1.6937958, 1.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 1.3375409), (1.6357548, 1.3040309), (1.5642452, 1.3040309), (1.5062042, 1.3375409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 1.3375409), (1.4481632, 1.3710509), (1.4124084, 1.43298), (1.4124084, 1.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.4124084, 1.5), (1.4124084, 1.56702), (1.4481632, 1.6289491), (1.5062042, 1.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 1.6624591), (1.5642452, 1.6959691), (1.6357548, 1.6959691), (1.6937958, 1.6624591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 1.6624591), (1.7518368, 1.6289491), (1.7875916, 1.56702), (1.7875916, 1.5)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.5062042, 25.3834409), (1.4481632, 25.4169509), (1.4124084, 25.47888), (1.4124084, 25.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.4124084, 25.5459), (1.4124084, 25.61292), (1.4481632, 25.6748491), (1.5062042, 25.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 25.7083591), (1.5642452, 25.7418691), (1.6357548, 25.7418691), (1.6937958, 25.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 25.7083591), (1.7518368, 25.6748491), (1.7875916, 25.61292), (1.7875916, 25.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.7875916, 25.5459), (1.7875916, 25.47888), (1.7518368, 25.4169509), (1.6937958, 25.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 25.3834409), (1.6357548, 25.3499309), (1.5642452, 25.3499309), (1.5062042, 25.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(1.7875916, 28.5459), (1.7875916, 28.47888), (1.7518368, 28.4169509), (1.6937958, 28.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 28.3834409), (1.6357548, 28.3499309), (1.5642452, 28.3499309), (1.5062042, 28.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 28.3834409), (1.4481632, 28.4169509), (1.4124084, 28.47888), (1.4124084, 28.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.4124084, 28.5459), (1.4124084, 28.61292), (1.4481632, 28.6748491), (1.5062042, 28.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.5062042, 28.7083591), (1.5642452, 28.7418691), (1.6357548, 28.7418691), (1.6937958, 28.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.6937958, 28.7083591), (1.7518368, 28.6748491), (1.7875916, 28.61292), (1.7875916, 28.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.6937958, 25.7083591), (3.7518368, 25.6748491), (3.7875916, 25.61292), (3.7875916, 25.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.7875916, 25.5459), (3.7875916, 25.47888), (3.7518368, 25.4169509), (3.6937958, 25.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6937958, 25.3834409), (3.6357548, 25.3499309), (3.5642452, 25.3499309), (3.5062042, 25.3834409)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 25.3834409), (3.4481632, 25.4169509), (3.4124084, 25.47888), (3.4124084, 25.5459)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.4124084, 25.5459), (3.4124084, 25.61292), (3.4481632, 25.6748491), (3.5062042, 25.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5062042, 25.7083591), (3.5642452, 25.7418691), (3.6357548, 25.7418691), (3.6937958, 25.7083591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_132735_7fc55abd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 56 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((21.3, 44.3049611318), (31.0293743169, 41.9942739179))
                Line((31.0293743169, 42.689312786), (31.0293743169, 41.9942739179))
                Line((21.3, 45), (31.0293743169, 42.689312786))
                Line((21.3, 44.3049611318), (21.3, 45))
            make_face()
            # Profile area: 38.6490315175, perimeter: 51.7618274075
            with BuildLine():
                Line((4.4769547976, -1.9973819936), (21.3, -0.6950388682))
                Line((21.3, 0), (21.3, -0.6950388682))
                Line((21.3, 0), (21.0000003129, 0))
                Line((21.0000003129, 0), (18.8, 0))
                Line((0, 0), (18.8, 0))
                Line((0, 0), (0, -6))
                Line((0, -6), (1.031516563, -6))
                CenterArc((4.7659403177, -5.7303586363), 3.7441457297, 94.4266798833, 89.7031534453)
            make_face()
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((21.3, -0.6950388682), (31.0293743169, -3.0057260821))
                Line((31.0293743169, -2.310687214), (31.0293743169, -3.0057260821))
                Line((21.3, 0), (31.0293743169, -2.310687214))
                Line((21.3, 0), (21.3, -0.6950388682))
            make_face()
            # Profile area: 0.048436885, perimeter: 0.8656712588
            with BuildLine():
                CenterArc((21.0499995202, 0), 0.2500004798, 0, 53.129956871)
                Line((21.2000003159, 0.200000003), (21.1000003144, 0.200000003))
                CenterArc((21.2262729705, 0.0118636731), 0.2265834555, 123.868578067, 59.1327415119)
                Line((21.3, 0), (21.0000003129, 0))
            make_face()
            # Profile area: 0.048436885, perimeter: 0.8656712588
            with BuildLine():
                Line((21.2000003159, 40.200000003), (21.1000003144, 40.200000003))
                CenterArc((21.2262729705, 40.0118636731), 0.2265834555, 123.868578067, 59.1327415119)
                Line((21.0000003129, 40), (21.3, 40))
                CenterArc((21.0499995202, 40), 0.2500004798, 0, 53.129956871)
            make_face()
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((21.3, 40), (21.3, 39.3049611318))
                Line((21.3, 39.3049611318), (31.0293743169, 36.9942739179))
                Line((31.0293743169, 37.689312786), (31.0293743169, 36.9942739179))
                Line((21.3, 40), (31.0293743169, 37.689312786))
            make_face()
            # Profile area: 29.9013512647, perimeter: 52.2754081468
            with BuildLine():
                Line((21.0000003129, 40), (21.3, 40))
                Line((18.8, 40), (21.0000003129, 40))
                Line((0, 40), (18.8, 40))
                Line((0, 40), (0, 34))
                Line((0, 34), (1.0190883101, 34))
                CenterArc((5.421321824, 34.4278612938), 4.422976961, 91.631717436, 93.9195306461)
                Line((5.2953775892, 38.8490447606), (21.3, 39.3049611318))
                Line((21.3, 40), (21.3, 39.3049611318))
            make_face()
            # Profile area: 0.048436885, perimeter: 0.8656712588
            with BuildLine():
                CenterArc((21.0499995202, 20), 0.2500004798, 0, 53.129956871)
                Line((21.2000003159, 20.200000003), (21.1000003144, 20.200000003))
                CenterArc((21.2262729705, 20.0118636731), 0.2265834555, 123.868578067, 59.1327415119)
                Line((21.3, 20), (21.0000003129, 20))
            make_face()
            # Profile area: 33.7681956516, perimeter: 52.0674697409
            with BuildLine():
                Line((21.3, 20), (21.0000003129, 20))
                Line((21.0000003129, 20), (18.8, 20))
                Line((0, 20), (18.8, 20))
                Line((0, 20), (0, 14))
                Line((0, 14), (1.0190883101, 14))
                CenterArc((5.0507752238, 14.4154667176), 4.0530373751, 92.9281641694, 92.9554175397)
                Line((4.8437304222, 18.4632123141), (21.3, 19.3049611318))
                Line((21.3, 20), (21.3, 19.3049611318))
            make_face()
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((21.3, 20), (21.3, 19.3049611318))
                Line((21.3, 19.3049611318), (31.0293743169, 16.9942739179))
                Line((31.0293743169, 17.689312786), (31.0293743169, 16.9942739179))
                Line((21.3, 20), (31.0293743169, 17.689312786))
            make_face()
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((21.3, 30), (21.3, 29.3049611318))
                Line((21.3, 29.3049611318), (31.0293743169, 26.9942739179))
                Line((31.0293743169, 27.689312786), (31.0293743169, 26.9942739179))
                Line((21.3, 30), (31.0293743169, 27.689312786))
            make_face()
            # Profile area: 0.048436885, perimeter: 0.8656712588
            with BuildLine():
                CenterArc((21.0499995202, 30), 0.2500004798, 0, 53.129956871)
                Line((21.2000003159, 30.200000003), (21.1000003144, 30.200000003))
                CenterArc((21.2262729705, 30.0118636731), 0.2265834555, 123.868578067, 59.1327415119)
                Line((21.0000003129, 30), (21.3, 30))
            make_face()
            # Profile area: 29.9013512647, perimeter: 52.2754081468
            with BuildLine():
                Line((21.0000003129, 30), (21.3, 30))
                Line((18.8, 30), (21.0000003129, 30))
                Line((0, 30), (18.8, 30))
                Line((0, 30), (0, 24))
                Line((0, 24), (1.0190883101, 24))
                CenterArc((5.421321824, 24.4278612938), 4.422976961, 91.631717436, 93.9195306461)
                Line((5.2953775892, 28.8490447606), (21.3, 29.3049611318))
                Line((21.3, 30), (21.3, 29.3049611318))
            make_face()
            # Profile area: 33.7681956516, perimeter: 52.0674697409
            with BuildLine():
                Line((4.8437304222, 8.4632123141), (21.3, 9.3049611318))
                Line((21.3, 10), (21.3, 9.3049611318))
                Line((21.3, 10), (21.0000003129, 10))
                Line((21.0000003129, 10), (18.8, 10))
                Line((0, 10), (18.8, 10))
                Line((0, 10), (0, 4))
                Line((0, 4), (1.0190883101, 4))
                CenterArc((5.0507752238, 4.4154667176), 4.0530373751, 92.9281641694, 92.9554175397)
            make_face()
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((21.3, 9.3049611318), (31.0293743169, 6.9942739179))
                Line((31.0293743169, 7.689312786), (31.0293743169, 6.9942739179))
                Line((21.3, 10), (31.0293743169, 7.689312786))
                Line((21.3, 10), (21.3, 9.3049611318))
            make_face()
            # Profile area: 0.048436885, perimeter: 0.8656712588
            with BuildLine():
                CenterArc((21.0499995202, 10), 0.2500004798, 0, 53.129956871)
                Line((21.2000003159, 10.200000003), (21.1000003144, 10.200000003))
                CenterArc((21.2262729705, 10.0118636731), 0.2265834555, 123.868578067, 59.1327415119)
                Line((21.3, 10), (21.0000003129, 10))
            make_face()
            # Profile area: 6.7622933131, perimeter: 21.3900777363
            with BuildLine():
                Line((6.3, 44.3049611318), (16.0293743169, 41.9942739179))
                Line((16.0293743169, 42.689312786), (16.0293743169, 41.9942739179))
                Line((6.3, 45), (16.0293743169, 42.689312786))
                Line((6.3, 44.3049611318), (6.3, 45))
            make_face()
        # OneSide extrude, distance=0.846
        extrude(amount=0.846)
    return part.part


def model_132772_70a3e5dc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 57 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0447052222, perimeter: 16.547344264
            with BuildLine():
                Line((0.4539051583, 0.704484688), (-2.4059761059, 0.704484688))
                CenterArc((-2.4059761059, 0.6104607732), 0.0940239148, 90, 90.0000107114)
                Line((-2.5000000207, 0.6104607556), (-2.5000000176, 0.5940238972))
                CenterArc((-2.4059761028, 0.5940239148), 0.0940239148, -179.9999892886, 89.9999892886)
                Line((-0.3966620979, 0.5), (-2.4059761028, 0.5))
                CenterArc((-0.3966620979, 0.45), 0.05, 0, 90)
                Line((-0.3466620979, 0.3809976117), (-0.3466620979, 0.45))
                CenterArc((-0.3966620979, 0.3809976117), 0.05, -43.8460407842, 43.8460407842)
                CenterArc((0, 0), 0.5, 136.1539592158, 69.7953706321)
                CenterArc((-0.4046316179, -0.1969092527), 0.05, -154.0506701521, 93.8559381357)
                Line((-0.2927535633, -0.1904447163), (-0.3797789307, -0.2402952405))
                CenterArc((-0.3176062505, -0.1470587285), 0.05, -60.1947320164, 85.0399135972)
                CenterArc((0, 0), 0.3, -24.8451815808, 229.6903631617)
                CenterArc((0.3176062505, -0.1470587285), 0.05, 155.1548184192, 85.0399135972)
                Line((0.2927535633, -0.1904447163), (0.3797789307, -0.2402952405))
                CenterArc((0.4046316179, -0.1969092527), 0.05, -119.8052679836, 93.8559381357)
                CenterArc((0, 0), 0.5, -25.9493298479, 69.7953706321)
                CenterArc((0.3966620979, 0.3809976117), 0.05, 180, 43.8460407842)
                Line((0.3466620979, 0.3809976117), (0.3466620979, 0.45))
                CenterArc((0.3966620979, 0.45), 0.05, 90, 90)
                Line((0.3966620979, 0.5), (0.6261174738, 0.5))
                CenterArc((0.6261174738, 0.7), 0.2, -90, 90)
                Line((0.8261174738, 0.7), (0.8261174738, 0.704484688))
                Line((0.8261174738, 0.704484688), (0.8261174738, 1.0022740208))
                CenterArc((0.6261174738, 1.0022740208), 0.2, 0, 90)
                Line((0.6261174738, 1.2022740208), (-2.4059761225, 1.2022740208))
                CenterArc((-2.4059761225, 1.1082501061), 0.0940239148, 90, 90)
                Line((-2.5000000373, 1.1082501061), (-2.5000000373, 1.044484688))
                Line((-2.5000000373, 0.9785086028), (-2.5000000373, 1.044484688))
                CenterArc((-2.4059761225, 0.9785086028), 0.0940239148, -180, 90)
                Line((-0.0765498626, 0.884484688), (-2.4059761225, 0.884484688))
                CenterArc((-0.0765498626, 1.0450588803), 0.1605741924, -90, 52.092014261)
                CenterArc((0.2508312936, 0.7901263134), 0.2543583746, 90, 52.092014261)
                Line((0.4539051583, 1.044484688), (0.2508312936, 1.044484688))
                CenterArc((0.4539051583, 0.874484688), 0.17, -90, 180)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_132863_90d729e2_0003():
    """Model: Rol intern"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.4196999251, perimeter: 17.8726990174
            with Locations((3.2611927714, -3.1148414568)):
                Circle(2.844528395)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


def model_132863_90d729e2_0004():
    """Model: Glaasje"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.9475177503, perimeter: 10.0489905793
            with BuildLine():
                Line((4.8094196577, 0.190287405), (1.6939552371, 0.190287405))
                Line((4.8094196577, 2.099318274), (4.8094196577, 0.190287405))
                Line((1.6939552371, 2.099318274), (4.8094196577, 2.099318274))
                Line((1.6939552371, 0.190287405), (1.6939552371, 2.099318274))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_132867_9ee8378c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 232.2575930237, perimeter: 76.1999988556
            with BuildLine():
                Line((-25.3999996185, 5.0799999237), (5.0799999237, 5.0799999237))
                Line((-25.3999996185, 5.0799999237), (-25.3999996185, -2.5399999619))
                Line((-25.3999996185, -2.5399999619), (5.0799999237, -2.5399999619))
                Line((5.0799999237, 5.0799999237), (5.0799999237, -2.5399999619))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


def model_132946_aaef771a_0002():
    """Model: wall wall look"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(15.8000002354, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1798697738, perimeter: 1.7995490973
            with BuildLine():
                Line((-2.3000000343, 0.2997913523), (-1.700016838, 0.2997913523))
                Line((-2.3000000343, 0), (-2.3000000343, 0.2997913523))
                Line((-1.700016838, 0), (-2.3000000343, 0))
                Line((-1.700016838, 0), (-1.700016838, 0.2997913523))
            make_face()
            # Profile area: 0.5398755171, perimeter: 4.2003682921
            with BuildLine():
                Line((-1.700016838, 0.5997967232), (-3.4999869655, 0.5997967232))
                Line((-3.4999869655, 0.5997967232), (-3.4999869655, 0.2997913523))
                Line((-3.4999869655, 0.2997913523), (-2.9000000432, 0.2997913523))
                Line((-2.9000000432, 0.2997913523), (-2.9000000432, 0.3))
                Line((-2.3000000343, 0.3), (-2.9000000432, 0.3))
                Line((-2.3000000343, 0.2997913523), (-2.3000000343, 0.3))
                Line((-2.3000000343, 0.2997913523), (-1.700016838, 0.2997913523))
                Line((-1.700016838, 0.2997913523), (-1.700016838, 0.5997967232))
            make_face()
            # Profile area: 0.1800616874, perimeter: 5.9997370075
            with BuildLine():
                Line((-2.9000000432, 0), (-2.9000000432, 0.2997913523))
                Line((-3.4999869655, 0.2997913523), (-2.9000000432, 0.2997913523))
                Line((-3.4999869655, 0.5997967232), (-3.4999869655, 0.2997913523))
                Line((-1.700016838, 0.5997967232), (-3.4999869655, 0.5997967232))
                Line((-3.5000000522, 0.5999999999), (-1.700016838, 0.5997967232))
                Line((-3.5000000522, 0), (-3.5000000522, 0.5999999999))
                Line((-2.9000000432, 0), (-3.5000000522, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_132982_ee1eed2f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4005373554, perimeter: 3.7259288872
            with BuildLine():
                CenterArc((0, 0), 0.404, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.189, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.062
        extrude(amount=0.062)
    return part.part


def model_132996_c742ef84_0005():
    """Model: handle trial v1"""
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
            # Profile area: 13.5927782189, perimeter: 37.1468092122
            with BuildLine():
                _nurbs_edge([(2.1942412678, -2.6995701615), (1.0619581525, -1.9573609432), (0.7794095882, -2.2049580717), (0.2888456202, -2.1350816441)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.6668664487, -2.7279070139), (2.6238716571, -2.7081425953), (2.1942412678, -2.6995701615)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(3.1968797207, -3.2578938421), (3.0449296125, -3.1549709415), (2.6668664487, -2.7279070139)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(3.9500427278, -3.0068572028), (3.8663547643, -3.0068572028), (3.3724837065, -3.3768241231), (3.1968797207, -3.2578938421)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.4591012065, -3.3834122626), (4.2150233237, -3.3345966053), (4.0337306913, -3.0068572028), (3.9500427278, -3.0068572028)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.8440433915, -3.3107840649), (4.809197731, -3.3526411676), (4.7031790892, -3.4322279199), (4.4591012065, -3.3834122626)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.2419765472, -2.8587434642), (5.1234429232, -2.9005741231), (4.8788890521, -3.2689269622), (4.8440433915, -3.3107840649)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.8957092539, -2.9091994445), (5.6237176196, -2.9440979926), (5.3605101713, -2.8169128052), (5.2419765472, -2.8587434642)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.9766381073, -2.4489303811), (6.7883598709, -2.4489303811), (6.1677008883, -2.8743008963), (5.8957092539, -2.9091994445)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.1662844849, -2.3471980572), (8.0546036402, -2.4159632397), (7.1649163437, -2.4489303811), (6.9766381073, -2.4489303811)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(8.2737585449, -1.8979885578), (8.2779653295, -2.2784328747), (8.1662844849, -2.3471980572)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(8.0924130249, -1.3052159746), (8.1970287323, -1.3749600824), (8.2737585449, -1.8979885578)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(6.9068684642, -1.207584761), (7.1788600985, -1.3191595276), (7.9877973175, -1.2354718669), (8.0924130249, -1.3052159746)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.2792238776, -0.9007474661), (6.6348768298, -1.0960099943), (6.9068684642, -1.207584761)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                Line((5.93052948, -0.8031162524), (6.2792238776, -0.9007474661))
                Line((5.832924811, -0.6985264842), (5.93052948, -0.8031162524))
                Line((5.5400308673, -0.6636543798), (5.832924811, -0.6985264842))
                Line((5.0867203585, -0.4195762448), (5.5400308673, -0.6636543798))
                _nurbs_edge([(4.5149028714, -0.0360098059), (4.7659393088, -0.0290512639), (5.0867203585, -0.4195762448)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(3.7547550678, -0.1685131365), (4.2638664341, -0.0429683479), (4.5149028714, -0.0360098059)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(3.1968544881, -0.1685131365), (3.2944858027, -0.1406260558), (3.7547550678, -0.1685131365)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(2.5831798983, -0.5032375121), (2.6041084496, -0.5799666687), (3.0992231735, -0.1964002172), (3.1968544881, -0.1685131365)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.0531666263, -0.4892939591), (2.0740687339, -0.4962524633), (2.5622513469, -0.4265083555), (2.5831798983, -0.5032375121)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.9792228723, -0.9844352277), (1.5301382518, -0.8658753618), (2.0322645187, -0.482335455), (2.0531666263, -0.4892939591)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2006864593, -1.0668794243), (0.3725597751, -0.989541707), (0.4283074927, -1.1029950937), (0.9792228723, -0.9844352277)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.2888456202, -2.1350816441), (0.1491191708, -2.1151850065), (-0.1984110436, -1.2464785433), (0.2006864593, -1.0668794243)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(2.5637330071, -1.8230585384), (2.7304999193, -1.8776686176), (3.0105613534, -1.4535679094)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(2.2887516085, -1.5566760174), (2.3003666941, -1.623800776), (2.396966095, -1.7684484593), (2.5637330071, -1.8230585384)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.5859581121, -1.1301941562), (2.4490892458, -1.1521016328), (2.2771365229, -1.4895512589), (2.2887516085, -1.5566760174)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.0105613534, -1.4535679094), (2.9039078585, -1.0815637064), (2.5859581121, -1.1301941562)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(2.2157529958, -2.2231612968), (2.251021959, -2.1667520301), (2.2298552116, -2.1385475985)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(1.6551538364, -2.0045625194), (1.6903963558, -2.0539072545), (2.2157529958, -2.2231612968)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(1.7644532251, -1.8177138631), (1.7221197303, -1.8494373385), (1.619911317, -1.9552177842), (1.6551538364, -2.0045625194)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(1.9936353763, -1.8353351227), (1.80678672, -1.7859903876), (1.7644532251, -1.8177138631)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(2.2298552116, -2.1385475985), (2.2086884642, -2.110343167), (1.9936353763, -1.8353351227)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.2981635094, -2.7767228731), (3.3263679409, -2.7697114309), (3.5696525097, -2.4171275743), (3.5731713518, -2.3430708059)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.0407769267, -2.4523700937), (3.0619434722, -2.5122982025), (3.2699590778, -2.7837343152), (3.2981635094, -2.7767228731)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.0619436741, -2.0786196915), (3.0337392426, -2.1138886547), (3.0196103811, -2.3924419848), (3.0407769267, -2.4523700937)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.2840612936, -1.8776421738), (3.213549811, -1.8847065036), (3.0901481056, -2.0433507284), (3.0619436741, -2.0786196915)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.5731713518, -2.3430708059), (3.5766901938, -2.2690140375), (3.3545727762, -1.8705776421), (3.2840612936, -1.8776421738)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(3.9186908786, -1.8177138631), (3.9504145559, -1.7930280717), (4.3382671738, -1.3664140924), (4.3135549386, -1.1442963719)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.6154782009, -1.5074370575), (3.7318155766, -1.77188797), (3.8869672012, -1.8423996544), (3.9186908786, -1.8177138631)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(3.9292740504, -0.7952316602), (3.8305579344, -0.8375385094), (3.4991408253, -1.2429860441), (3.6154782009, -1.5074370575)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.3135549386, -1.1442963719), (4.289530646, -0.9281583818), (4.0279901663, -0.752924811), (3.9292740504, -0.7952316602)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(4.620313104, -2.8966055346), (4.7587167199, -2.8612043524), (5.1033363501, -2.5969385465), (5.1562267749, -2.529945906)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.1513656298, -2.5405028359), (4.1302255281, -2.6074954764), (4.3171008301, -2.9741813469), (4.620313104, -2.8966055346)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.3417597739, -1.9129111369), (4.1725057316, -2.4735101954), (4.1513656298, -2.5405028359)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(4.5639038372, -1.7542669121), (4.4828089809, -1.7683426841), (4.3417597739, -1.9129111369)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(5.1562267749, -2.529945906), (5.2091171996, -2.4629532655), (4.6450249354, -1.7401911402), (4.5639038372, -1.7542669121)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(5.8225794315, -1.7119336192), (5.8190605895, -1.6731458139), (5.3183631961, -1.1337132001), (5.219673322, -1.1266487694)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.3148968379, -2.110343167), (5.3747983011, -2.1385742442), (5.8260982736, -1.7507214244), (5.8225794315, -1.7119336192)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.8741804409, -1.384035453), (4.8177449322, -1.482751468), (5.2549953747, -2.0821120898), (5.3148968379, -2.110343167)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.219673322, -1.1266487694), (5.120983448, -1.1195843387), (4.9306163534, -1.2853193371), (4.8741804409, -1.384035453)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(4.6485437775, -0.9504097287), (4.7049530443, -0.932788469), (4.8459760094, -0.837591397), (4.8459760094, -0.7917391105)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(4.3735092894, -0.6930230955), (4.5921345107, -0.9680309884), (4.6485437775, -0.9504097287)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(4.3982215246, -0.5414168576), (4.3594335175, -0.5484812379), (4.3735092894, -0.6930230955)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(4.5568657494, -0.5414168576), (4.4370095317, -0.5343524774), (4.3982215246, -0.5414168576)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
                _nurbs_edge([(4.8459760094, -0.7917391105), (4.8459760094, -0.7458868241), (4.5568657494, -0.5414168576)], [1, 1, 1], [0, 0, 0, 1, 1, 1], 2)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                _nurbs_edge([(6.4840111192, -1.9804857429), (6.3797652213, -1.9795331605), (5.868484656, -2.332884291), (5.9447372691, -2.3514581331)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(6.6479735756, -2.0731427972), (6.6644042587, -2.0184798304), (6.521688083, -1.9808297141), (6.4840111192, -1.9804857429)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(5.9447372691, -2.3514581331), (6.0209898822, -2.3700319751), (6.6315432962, -2.1278320058), (6.6479735756, -2.0731427972)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_132996_c742ef84_0008():
    """Model: FIREPIT LEG 40x40x2.5 x 190mm height v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9914159265, perimeter: 15.8283185307
            with BuildLine():
                CenterArc((3.9, -0.1), 0.1, 0, 90)
                Line((0.1, 0), (3.9, 0))
                CenterArc((0.1, -0.1), 0.1, 90, 90)
                Line((0, -3.9), (0, -0.1))
                CenterArc((0.1, -3.9), 0.1, -180, 90)
                Line((3.9, -4), (0.1, -4))
                CenterArc((3.9, -3.9), 0.1, -90, 90)
                Line((4, -0.1), (4, -3.9))
            make_face()
        # OneSide extrude, distance=19
        extrude(amount=19)
    return part.part


def model_133073_013d4ebd_0001():
    """Model: Back Side v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1935.479941864, perimeter: 203.1999969482
            with BuildLine():
                Line((38.0999994278, 50.7999992371), (76.1999988556, 0))
                Line((0, 0), (38.0999994278, 50.7999992371))
                Line((76.1999988556, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133073_013d4ebd_0002():
    """Model: Front Side (Entrance) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1359.5462196146, perimeter: 243.0982230496
            with BuildLine():
                Line((0, 0), (25.3999996185, 0))
                Line((25.3999996185, 0), (25.3999996185, 12.6999998093))
                CenterArc((38.0999994278, 12.6999998093), 12.6999998093, 0, 180)
                Line((50.7999992371, 0), (50.7999992371, 12.6999998093))
                Line((76.1999988556, 0), (50.7999992371, 0))
                Line((38.0999994278, 50.7999992371), (76.1999988556, 0))
                Line((0, 0), (38.0999994278, 50.7999992371))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133073_013d4ebd_0016():
    """Model: Coumns v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.3510028886, perimeter: 77.8015433395
            with BuildLine():
                CenterArc((0, 0), 6.3500002027, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.0325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=63.5
        extrude(amount=63.5)
    return part.part


def model_133073_013d4ebd_0019():
    """Model: Sharpener v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2257999031, perimeter: 7.6199998856
            with BuildLine():
                Line((0, 1.2699999809), (0, 0))
                Line((0, 0), (2.5399999619, 0))
                Line((2.5399999619, 0), (2.5399999619, 1.2699999809))
                Line((2.5399999619, 1.2699999809), (0, 1.2699999809))
            make_face()
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


def model_133073_013d4ebd_0022():
    """Model: columnCover v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 126.67687786, perimeter: 39.8982279739
            Circle(6.3500002027)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133109_dbf8891f_0002():
    """Model: Thermolis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2318, perimeter: 198
            with BuildLine():
                Line((-5, -74), (-5, -13))
                Line((-5, -13), (-43, -13))
                Line((-43, -13), (-43, -74))
                Line((-43, -74), (-5, -74))
            make_face()
        # OneSide extrude, distance=34.5
        extrude(amount=34.5)
    return part.part


def model_133109_dbf8891f_0005():
    """Model: Plotr"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2580, perimeter: 232
            with BuildLine():
                Line((-160.3, -108), (-160.3, -22))
                Line((-160.3, -22), (-190.3, -22))
                Line((-190.3, -22), (-190.3, -108))
                Line((-190.3, -108), (-160.3, -108))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


def model_133131_e8fc0f93_0017():
    """Model: Top Side Pannel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2619.3496, perimeter: 215.9
            with BuildLine():
                Line((-2.54, 58.42), (-73.66, 58.42))
                Line((-2.54, 95.25), (-2.54, 58.42))
                Line((-73.66, 95.25), (-2.54, 95.25))
                Line((-73.66, 58.42), (-73.66, 95.25))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133131_e8fc0f93_0029():
    """Model: Side Pannel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3070.9616, perimeter: 228.6
            with BuildLine():
                Line((-2.54, 12.7), (-2.54, 55.88))
                Line((-2.54, 55.88), (-73.66, 55.88))
                Line((-73.66, 55.88), (-73.66, 12.7))
                Line((-73.66, 12.7), (-2.54, 12.7))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133131_e8fc0f93_0030():
    """Model: Side Shelves"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3477.4124, perimeter: 240.03
            with BuildLine():
                Line((51.435, -73.66), (2.54, -73.66))
                Line((51.435, -2.54), (51.435, -73.66))
                Line((2.54, -2.54), (51.435, -2.54))
                Line((2.54, -73.66), (2.54, -2.54))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133131_e8fc0f93_0031():
    """Model: Middle Shelf"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2579.0228007368, perimeter: 203.1998263976
            with BuildLine():
                Line((103.505, -5.0800868012), (103.505, -57.15))
                Line((53.975, -5.0800868012), (103.505, -5.0800868012))
                Line((53.975, -57.15), (53.975, -5.0800868012))
                Line((103.505, -57.15), (53.975, -57.15))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0000():
    """Model: Foam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 57.785, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8129.016, perimeter: 411.48
            with BuildLine():
                Line((-154.94, 71.12), (-2.54, 71.12))
                Line((-154.94, 17.78), (-154.94, 71.12))
                Line((-2.54, 17.78), (-154.94, 17.78))
                Line((-2.54, 71.12), (-2.54, 17.78))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_133402_47273d61_0001():
    """Model: 28" Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6129003088, perimeter: 5.0800004864
            with BuildLine():
                Line((2.54, 3.8100001216), (2.54, 2.54))
                Line((2.54, 2.54), (3.8100001216, 2.54))
                Line((3.8100001216, 2.54), (3.8100001216, 3.8100001216))
                Line((3.8100001216, 3.8100001216), (2.54, 3.8100001216))
            make_face()
        # OneSide extrude, distance=71.12
        extrude(amount=71.12)
    return part.part


def model_133402_47273d61_0002():
    """Model: 15" Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129001029, perimeter: 5.0800001621
            with BuildLine():
                Line((0, -15.2400004864), (-1.2700000405, -15.2400004864))
                Line((-1.2700000405, -15.2400004864), (-1.2700000405, -16.5100005269))
                Line((-1.2700000405, -16.5100005269), (0, -16.5100005269))
                Line((0, -15.2400004864), (0, -16.5100005269))
            make_face()
        # OneSide extrude, distance=35.56
        extrude(amount=35.56)
    return part.part


def model_133402_47273d61_0003():
    """Model: Side Shelves"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3296.7676, perimeter: 234.95
            with BuildLine():
                Line((48.895, -73.66), (2.54, -73.66))
                Line((48.895, -2.54), (48.895, -73.66))
                Line((2.54, -2.54), (48.895, -2.54))
                Line((2.54, -73.66), (2.54, -2.54))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0005():
    """Model: Middle Shelf"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2704.8290007368, perimeter: 208.2798263976
            with BuildLine():
                Line((103.505, -2.5400868012), (103.505, -57.15))
                Line((53.975, -2.5400868012), (103.505, -2.5400868012))
                Line((53.975, -57.15), (53.975, -2.5400868012))
                Line((103.505, -57.15), (53.975, -57.15))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0006():
    """Model: Foam Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8129.016, perimeter: 411.48
            with BuildLine():
                Line((154.94, -71.12), (2.54, -71.12))
                Line((154.94, -17.78), (154.94, -71.12))
                Line((2.54, -17.78), (154.94, -17.78))
                Line((2.54, -71.12), (2.54, -17.78))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0007():
    """Model: 21.5" Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((65.2456138926, 4.9045363469), (65.2456138926, 3.6345363469))
                Line((65.2456138926, 3.6345363469), (66.5156138926, 3.6345363469))
                Line((66.5156138926, 3.6345363469), (66.5156138926, 4.9045363469))
                Line((66.5156138926, 4.9045363469), (65.2456138926, 4.9045363469))
            make_face()
        # OneSide extrude, distance=54.61
        extrude(amount=54.61)
    return part.part


def model_133402_47273d61_0008():
    """Model: 1U"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.8171882494, perimeter: 19.8728469744
            with BuildLine():
                Line((1.2700000405, 5.8724800405), (1.2700000405, 1.2700000405))
                Line((1.2700000405, 1.2700000405), (2.8575000405, 1.2700000405))
                Line((2.8575000405, 1.2700000405), (2.8575000405, 5.8724800405))
                Line((2.8575000405, 5.8724800405), (1.2700000405, 5.8724800405))
            make_face()
            with BuildLine():
                CenterArc((2.0637500405, 5.0800000405), 0.39751, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0637500405, 3.4925000405), 0.39751, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0637500405, 1.9050000405), 0.39751, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_133402_47273d61_0009():
    """Model: Attachment"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.6951521607, perimeter: 72.0674484815
            with BuildLine():
                Line((-32.648190138, -29.8228561645), (-32.648190138, 6.0521180762))
                Line((-32.648190138, 6.0521180762), (-32.806940138, 6.0521180762))
                Line((-32.806940138, 6.0521180762), (-32.806940138, -29.8228561645))
                Line((-32.806940138, -29.8228561645), (-32.648190138, -29.8228561645))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


def model_133402_47273d61_0012():
    """Model: Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((48.895, -71.12), (51.435, -71.12))
                Line((48.895, -73.66), (48.895, -71.12))
                Line((51.435, -73.66), (48.895, -73.66))
                Line((51.435, -71.12), (51.435, -73.66))
            make_face()
        # OneSide extrude, distance=43.18
        extrude(amount=43.18)
    return part.part


def model_133402_47273d61_0013():
    """Model: 27" Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 174.1932, perimeter: 142.24
            with BuildLine():
                Line((0, -71.12), (0, -2.54))
                Line((0, -2.54), (-2.54, -2.54))
                Line((-2.54, -2.54), (-2.54, -71.12))
                Line((-2.54, -71.12), (0, -71.12))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_133402_47273d61_0014():
    """Model: VBar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((2.54, -2.54), (0, -2.54))
                Line((2.54, 0), (2.54, -2.54))
                Line((0, 0), (2.54, 0))
                Line((0, -2.54), (0, 0))
            make_face()
        # OneSide extrude, distance=97.79
        extrude(amount=97.79)
    return part.part


def model_133402_47273d61_0016():
    """Model: 28" Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180.6448, perimeter: 147.32
            with BuildLine():
                Line((2.54, -73.66), (0, -73.66))
                Line((2.54, -2.54), (2.54, -73.66))
                Line((0, -2.54), (2.54, -2.54))
                Line((0, -73.66), (0, -2.54))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_133402_47273d61_0017():
    """Model: Front Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 130.6449, perimeter: 107.95
            with BuildLine():
                Line((56.5149999237, -76.1999988937), (5.0799999237, -76.1999988937))
                Line((56.5149999237, -73.6599988937), (56.5149999237, -76.1999988937))
                Line((5.0799999237, -73.6599988937), (56.5149999237, -73.6599988937))
                Line((5.0799999237, -76.1999988937), (5.0799999237, -73.6599988937))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_133402_47273d61_0019():
    """Model: 60" Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 387.096, perimeter: 309.88
            with BuildLine():
                Line((154.94, -2.54), (2.54, -2.54))
                Line((154.94, 0), (154.94, -2.54))
                Line((2.54, 0), (154.94, 0))
                Line((2.54, -2.54), (2.54, 0))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_133402_47273d61_0021():
    """Model: 68" Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 438.7088, perimeter: 350.52
            with BuildLine():
                Line((0, 2.54), (0, 0))
                Line((0, 0), (172.72, 0))
                Line((172.72, 0), (172.72, 2.54))
                Line((172.72, 2.54), (0, 2.54))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_133402_47273d61_0023():
    """Model: 14.5" Brace"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129004118, perimeter: 5.0800006485
            with BuildLine():
                Line((3.8100001216, -6.3500002027), (2.54, -6.3500002027))
                Line((3.8100001216, -5.08), (3.8100001216, -6.3500002027))
                Line((2.54, -5.08), (3.8100001216, -5.08))
                Line((2.54, -6.3500002027), (2.54, -5.08))
            make_face()
        # OneSide extrude, distance=36.83
        extrude(amount=36.83)
    return part.part


def model_133402_47273d61_0024():
    """Model: Post"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.3548, perimeter: 20.32
            with BuildLine():
                Line((165.1, -5.08), (157.48, -5.08))
                Line((165.1, -2.54), (165.1, -5.08))
                Line((157.48, -2.54), (165.1, -2.54))
                Line((157.48, -5.08), (157.48, -2.54))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_133402_47273d61_0026():
    """Model: Pipe"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0670751144, perimeter: 7.9796455948
            with Locations((-1.2700000405, 59.690001905)):
                Circle(1.2700000405)
        # OneSide extrude, distance=66.04
        extrude(amount=66.04)
    return part.part


def model_133402_47273d61_0027():
    """Model: 25" Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6128963453, perimeter: 5.0799942446
            with BuildLine():
                Line((3.8100001216, 93.9800029993), (2.54, 93.9800029993))
                Line((3.8100001216, 95.25), (3.8100001216, 93.9800029993))
                Line((2.54, 95.25), (3.8100001216, 95.25))
                Line((2.54, 93.9800029993), (2.54, 95.25))
            make_face()
        # OneSide extrude, distance=63.5
        extrude(amount=63.5)
    return part.part


def model_133402_47273d61_0028():
    """Model: DoorVert"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 97.79, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4516004118, perimeter: 10.1600003242
            with BuildLine():
                Line((0, -2.5400000811), (0, 0))
                Line((0, 0), (-2.5400000811, 0))
                Line((-2.5400000811, 0), (-2.5400000811, -2.5400000811))
                Line((-2.5400000811, -2.5400000811), (0, -2.5400000811))
            make_face()
        # OneSide extrude, distance=81.28
        extrude(amount=81.28)
    return part.part


def model_133402_47273d61_0029():
    """Model: DoorHoriz"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.4516004118, perimeter: 10.1600003242
            with BuildLine():
                Line((0, 2.5400000811), (0, 0))
                Line((0, 0), (2.5400000811, 0))
                Line((2.5400000811, 0), (2.5400000811, 2.5400000811))
                Line((2.5400000811, 2.5400000811), (0, 2.5400000811))
            make_face()
        # OneSide extrude, distance=48.895
        extrude(amount=48.895)
    return part.part


def model_133402_47273d61_0030():
    """Model: HBrace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6129001029, perimeter: 5.0800001621
            with BuildLine():
                Line((1.2700000405, 1.2700000405), (1.2700000405, 0))
                Line((1.2700000405, 0), (2.5400000811, 0))
                Line((2.5400000811, 0), (2.5400000811, 1.2700000405))
                Line((2.5400000811, 1.2700000405), (1.2700000405, 1.2700000405))
            make_face()
        # OneSide extrude, distance=41.275
        extrude(amount=41.275)
    return part.part


def model_133402_47273d61_0031():
    """Model: Door Pannel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3725.7989920729, perimeter: 250.1899996758
            with BuildLine():
                Line((54.6100000811, 15.8750000811), (54.6100000811, 92.0749999189))
                Line((54.6100000811, 92.0749999189), (5.7150000811, 92.0749999189))
                Line((5.7150000811, 92.0749999189), (5.7150000811, 15.8750000811))
                Line((5.7150000811, 15.8750000811), (54.6100000811, 15.8750000811))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0032():
    """Model: Mid Back"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6128999516, perimeter: 5.0799999237
            with BuildLine():
                Line((5.0799999237, 8.8899998665), (3.8099999428, 8.8899998665))
                Line((5.0799999237, 10.1599998474), (5.0799999237, 8.8899998665))
                Line((3.8099999428, 10.1599998474), (5.0799999237, 10.1599998474))
                Line((3.8099999428, 8.8899998665), (3.8099999428, 10.1599998474))
            make_face()
        # OneSide extrude, distance=38.01872
        extrude(amount=38.01872)
    return part.part


def model_133402_47273d61_0033():
    """Model: Top Side Pannel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6593.5352, perimeter: 327.66
            with BuildLine():
                Line((-2.54, 2.54), (-73.66, 2.54))
                Line((-2.54, 95.25), (-2.54, 2.54))
                Line((-73.66, 95.25), (-2.54, 95.25))
                Line((-73.66, 2.54), (-73.66, 95.25))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0034():
    """Model: Back Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((98.425, 3.165570856), (100.965, 3.165570856))
                Line((98.425, 0.625570856), (98.425, 3.165570856))
                Line((100.965, 0.625570856), (98.425, 0.625570856))
                Line((100.965, 3.165570856), (100.965, 0.625570856))
            make_face()
        # OneSide extrude, distance=82.55
        extrude(amount=82.55)
    return part.part


def model_133402_47273d61_0036():
    """Model: Shelf Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-5.0799999046, 62.2299990463), (-6.3499999046, 62.2299990463))
                Line((-5.0799999046, 63.4999990463), (-5.0799999046, 62.2299990463))
                Line((-6.3499999046, 63.4999990463), (-5.0799999046, 63.4999990463))
                Line((-6.3499999046, 62.2299990463), (-6.3499999046, 63.4999990463))
            make_face()
        # OneSide extrude, distance=53.34
        extrude(amount=53.34)
    return part.part


def model_133402_47273d61_0037():
    """Model: Inside Pannel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2029.0282, perimeter: 180.34
            with BuildLine():
                Line((-13.97, 16.51), (-60.96, 16.51))
                Line((-13.97, 16.51), (-13.97, 59.69))
                Line((-13.97, 59.69), (-60.96, 59.69))
                Line((-60.96, 59.69), (-60.96, 55.88))
                Line((-60.96, 16.51), (-60.96, 55.88))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_133402_47273d61_0038():
    """Model: 17" Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129003088, perimeter: 5.0800004864
            with BuildLine():
                Line((165.1, -6.3500002027), (165.1, -5.08))
                Line((165.1, -5.08), (163.8299999595, -5.08))
                Line((163.8299999595, -5.08), (163.8299999595, -6.3500002027))
                Line((163.8299999595, -6.3500002027), (165.1, -6.3500002027))
            make_face()
        # OneSide extrude, distance=43.18
        extrude(amount=43.18)
    return part.part


def model_133564_b5340c41_0002():
    """Model: dr"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=10.5
        extrude(amount=10.5)
    return part.part


def model_133564_b5340c41_0005():
    """Model: regenerater"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000000013, -0.0000000111, 13.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.8694686131, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((-0.3735133095, -0.270475145), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.3735133095, -0.270475145), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4)
    return part.part


def model_133604_d1452929_0000():
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
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 60.2579960625, perimeter: 76.567089458
            with BuildLine():
                CenterArc((-9.0870976505, -1.1103090346), 0.9375600022, -71.5650511771, 88.637851825)
                _nurbs_edge([(-4.762510585, 2.1535469448), (-4.773399912, 2.1469798406), (-4.7960635662, 2.1333147791), (-4.8327140776, 2.1112246156), (-4.8868955056, 2.0785834687), (-4.9634135605, 2.0325002085), (-5.0484784062, 1.9812555454), (-5.1415762963, 1.9251065231), (-5.2417998138, 1.8645087247), (-5.3479076944, 1.8000985447), (-5.4584478703, 1.7326486402), (-5.571856939, 1.663032866), (-5.6865725553, 1.5921877628), (-5.8011312422, 1.5210759037), (-5.9142949501, 1.4506485897), (-6.0250474132, 1.3818090831), (-6.132527072, 1.315375694), (-6.2359845568, 1.2520446365), (-6.3347218598, 1.1923524984), (-6.4280599132, 1.136638261), (-6.5152435099, 1.0850046771), (-6.5956155288, 1.0372789095), (-6.6689552225, 0.9929713975), (-6.7357630558, 0.9512356762), (-6.7975813244, 0.9108230073), (-6.8572698964, 0.8700479729), (-6.9180809129, 0.8271194224), (-6.9828312281, 0.7804423264), (-7.0529285094, 0.7289621012), (-7.1277798438, 0.6723994378), (-7.2056421168, 0.6110583327), (-7.2842837474, 0.5457023123), (-7.3616516809, 0.4774013269), (-7.4366963837, 0.4074035), (-7.5094955806, 0.3369552584), (-7.580687027, 0.2670874047), (-7.6510736949, 0.1983949684), (-7.7212018751, 0.1308504864), (-7.7908454993, 0.0635215401), (-7.8589867782, -0.0053273306), (-7.9241747807, -0.0778543427), (-7.9847792784, -0.1563334326), (-8.0392694291, -0.2428387512), (-8.0865272131, -0.3388779382), (-8.1258399898, -0.445414639), (-8.1567928804, -0.563009469), (-8.1747157689, -0.6661371975), (-8.1842882917, -0.7486052585), (-8.1889515551, -0.8058586496), (-8.1908535799, -0.835054019)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-3.9889021538, 1.8333659576), (-3.9911552245, 1.8386598697), (-3.9957251756, 1.8491106405), (-4.0027715302, 1.8643756367), (-4.0125499216, 1.8839058046), (-4.0254134357, 1.9069440077), (-4.0389189725, 1.9286083697), (-4.0530663493, 1.9489067429), (-4.0678529663, 1.9678578461), (-4.0832713372, 1.9854959027), (-4.0993122195, 2.0018724707), (-4.1159750771, 2.0170540644), (-4.1332776445, 2.0311211293), (-4.1512639563, 2.0441661922), (-4.1700177001, 2.0562935081), (-4.1896578945, 2.0676148), (-4.2103011351, 2.0782378457), (-4.2320300559, 2.0882563588), (-4.2548612774, 2.0977399766), (-4.2787081667, 2.1067226799), (-4.3033610185, 2.1151963191), (-4.3285386294, 2.1231246299), (-4.353927625, 2.1304538892), (-4.3792283199, 2.1371251214), (-4.4041932591, 2.1430849909), (-4.4286804925, 2.1482989727), (-4.4526426317, 2.1527550532), (-4.4760851352, 2.1564625924), (-4.4990327995, 2.1594532134), (-4.5214967861, 2.1617801548), (-4.5434322945, 2.1635204639), (-4.564731979, 2.1647690557), (-4.5852758763, 2.1656207567), (-4.6049704367, 2.1661542294), (-4.6237868875, 2.1664171797), (-4.6418130342, 2.166405806), (-4.659239443, 2.1660705499), (-4.6763016779, 2.1653392543), (-4.6932387848, 2.1641339207), (-4.7102390554, 2.1623924903), (-4.7274107001, 2.1600808413), (-4.741328959, 2.1577623983), (-4.7518771935, 2.1557578928), (-4.7589580118, 2.1543035883), (-4.762510585, 2.1535469448)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-3.1035017534, 2.1625959828), 0.9446302338, -159.602696517, 181.3487226571)
                Line((-2.501139558, 3.2746413674), (-2.2260958927, 2.5125748883))
                _nurbs_edge([(1.0942457996, 5.7280961555), (1.0631738266, 5.7096082337), (1.000354021, 5.6720718862), (0.9040967555, 5.6140858299), (0.7716818898, 5.5333944958), (0.5992637699, 5.4268816887), (0.4197740233, 5.3148035586), (0.2330068897, 5.1974324911), (0.0387345515, 5.07534974), (-0.1632179656, 4.949486318), (-0.3727335255, 4.8209462006), (-0.5891935479, 4.6908803129), (-0.8112211117, 4.5603389548), (-1.0364706323, 4.430148573), (-1.2612584438, 4.3007400992), (-1.4808596554, 4.1721825472), (-1.6901041023, 4.04430691), (-1.8838777212, 3.9167969639), (-2.0576590501, 3.7892885869), (-2.2080930517, 3.6614670123), (-2.3335025796, 3.5331552974), (-2.4133387387, 3.4300471997), (-2.4616996187, 3.3524481087), (-2.4888425196, 3.3005967233), (-2.501139558, 3.2746413674)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(10.9474379952, 2.2467436592), (10.9352032553, 2.2800844879), (10.9098164742, 2.3474627439), (10.8689843472, 2.4506201421), (10.8090344621, 2.5923442019), (10.7249953823, 2.7760922421), (10.6321292177, 2.9652444383), (10.5309981808, 3.1574629598), (10.4226014345, 3.3486739501), (10.3081751775, 3.5339623167), (10.1888759021, 3.7089717076), (10.0655175225, 3.8710585362), (9.938251546, 4.0207322046), (9.8063713459, 4.1624453099), (9.6686778578, 4.3024247356), (9.5237752816, 4.4468599818), (9.3703832329, 4.6000314666), (9.2076686642, 4.7622577342), (9.0351858527, 4.9308492681), (8.8527770461, 5.1013566823), (8.6604849147, 5.268737704), (8.4584689683, 5.4284857445), (8.2469000587, 5.577957805), (8.0260280322, 5.7161771425), (7.796286988, 5.84328606), (7.5583943479, 5.9601137308), (7.3134398833, 6.0677178098), (7.0630128509, 6.1668919398), (6.8092109615, 6.2578348941), (6.5542667752, 6.3403522494), (6.3002523138, 6.4139632255), (6.0487288994, 6.4780461973), (5.8004739663, 6.531963169), (5.5550352308, 6.5752042175), (5.3110101702, 6.6074705819), (5.0667284507, 6.6287203094), (4.8208421305, 6.6392338052), (4.5728841124, 6.6396552716), (4.3240117132, 6.6310868008), (4.0770998617, 6.6150224611), (3.8356301229, 6.5929958828), (3.6028197813, 6.5662810244), (3.3807133695, 6.5355930911), (3.1691479363, 6.500736667), (2.9651988153, 6.460433841), (2.7643245348, 6.4127771737), (2.5612601314, 6.355591857), (2.3509396279, 6.2868053528), (2.1295740628, 6.2048828478), (1.8947230406, 6.1088504816), (1.6449285947, 5.9981401565), (1.4325810868, 5.8976230119), (1.2661860036, 5.8154834705), (1.1520873132, 5.7577250507), (1.0942457996, 5.7280961555)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1, 1, 1, 1, 1], 5)
                Line((12.5349585862, 2.8697252244), (10.9474379952, 2.2467436592))
                Line((11.6894200665, 5.0243793673), (12.5349585862, 2.8697252244))
                _nurbs_edge([(11.6894200665, 5.0243793673), (11.6805724257, 5.0427875875), (11.6628596065, 5.0797493729), (11.6362378286, 5.1356280826), (11.6006364613, 5.2110052533), (11.5558599867, 5.3066681639), (11.5105026342, 5.4037350564), (11.4639703727, 5.5021289284), (11.4152289906, 5.6017231831), (11.3630277317, 5.7023083314), (11.3062763202, 5.8035477211), (11.2443610287, 5.9049399521), (11.1775118006, 6.0057711768), (11.1070763401, 6.1050918608), (11.0348884179, 6.201940879), (10.9626748846, 6.2955628282), (10.8914964939, 6.3856067346), (10.8210604463, 6.4723828007), (10.7494395898, 6.5569400205), (10.674062128, 6.6405906527), (10.5925347275, 6.7245032391), (10.503428364, 6.8093215883), (10.4073343009, 6.8946417286), (10.3066338158, 6.9791520721), (10.2044644707, 7.0611848112), (10.1038876933, 7.139167256), (10.0070660925, 7.2120606112), (9.9142101872, 7.27993558), (9.8234575707, 7.3440058046), (9.7319453707, 7.4059722773), (9.6366035384, 7.467525191), (9.5350077994, 7.5298206881), (9.4263456901, 7.592867891), (9.3111993222, 7.6557724289), (9.1910623276, 7.7171654559), (9.067938763, 7.7755846552), (8.9439325729, 7.8298379113), (8.8207802385, 7.8794671467), (8.6996678419, 7.9247769979), (8.5812883885, 7.9665141344), (8.4658244209, 8.0056385505), (8.3529722986, 8.0430763542), (8.2419211102, 8.0794342217), (8.1314463754, 8.1148939187), (8.0201597998, 8.1493901485), (7.9067319602, 8.1827255321), (7.7901049553, 8.2146995331), (7.6697616233, 8.2452597035), (7.5457179524, 8.274506342), (7.4183568316, 8.3026101633), (7.2883084131, 8.3297545883), (7.156316844, 8.3560731749), (7.0230995645, 8.3815761389), (6.8892588425, 8.4061291025), (6.7552680057, 8.4295040742), (6.6214392093, 8.4514121621), (6.4878974335, 8.4715436891), (6.3545544483, 8.4896050524), (6.2210753793, 8.5053572248), (6.0870488404, 8.5186378774), (5.9521571795, 8.529381375), (5.8163625923, 8.5376430289), (5.6800506054, 8.543613828), (5.5442808401, 8.5476585265), (5.4106447067, 8.5502687886), (5.2807376895, 8.55193355), (5.1557170784, 8.5530271016), (5.0358652476, 8.5536999846), (4.9200534349, 8.5537445469), (4.8055471758, 8.5525456463), (4.6889349297, 8.5493100288), (4.5669023901, 8.5432576981), (4.4369965571, 8.533810104), (4.2985647197, 8.5208232588), (4.1530178421, 8.5046480184), (4.0030153258, 8.4859138478), (3.8519179284, 8.4653822863), (3.7031081817, 8.4437639287), (3.5594248674, 8.4215705481), (3.4224068378, 8.3989037877), (3.2921779789, 8.3754615301), (3.1679506553, 8.3507531828), (3.0483684561, 8.3242636752), (2.9318982095, 8.2956265087), (2.8172386527, 8.2648211823), (2.7036042575, 8.2322731753), (2.5905420556, 8.1986170446), (2.477821353, 8.1645055656), (2.3653059457, 8.1304212619), (2.2528072246, 8.0964375682), (2.1400429622, 8.0621816716), (2.0267395261, 8.0270602263), (1.9127024909, 7.9904268348), (1.797889766, 7.951755557), (1.6825095187, 7.9108555586), (1.5669848052, 7.867859918), (1.4518395196, 7.8230793701), (1.3376045538, 7.7768931262), (1.2247245329, 7.7296344712), (1.1134418541, 7.681453309), (1.0038028355, 7.6323154357), (0.8957290378, 7.5820759142), (0.7890695415, 7.5305306354), (0.6836579226, 7.4774735953), (0.5793753175, 7.4227602192), (0.4761522189, 7.3663066882), (0.3943926296, 7.3197180154), (0.3335281833, 7.2839685332), (0.2931541709, 7.2597764796), (0.2730177369, 7.2475906874)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0095238095, 0.019047619, 0.0285714286, 0.0380952381, 0.0476190476, 0.0571428571, 0.0666666667, 0.0761904762, 0.0857142857, 0.0952380952, 0.1047619048, 0.1142857143, 0.1238095238, 0.1333333333, 0.1428571429, 0.1523809524, 0.1619047619, 0.1714285714, 0.180952381, 0.1904761905, 0.2, 0.2095238095, 0.219047619, 0.2285714286, 0.2380952381, 0.2476190476, 0.2571428571, 0.2666666667, 0.2761904762, 0.2857142857, 0.2952380952, 0.3047619048, 0.3142857143, 0.3238095238, 0.3333333333, 0.3428571429, 0.3523809524, 0.3619047619, 0.3714285714, 0.380952381, 0.3904761905, 0.4, 0.4095238095, 0.419047619, 0.4285714286, 0.4380952381, 0.4476190476, 0.4571428571, 0.4666666667, 0.4761904762, 0.4857142857, 0.4952380952, 0.5047619048, 0.5142857143, 0.5238095238, 0.5333333333, 0.5428571429, 0.5523809524, 0.5619047619, 0.5714285714, 0.580952381, 0.5904761905, 0.6, 0.6095238095, 0.619047619, 0.6285714286, 0.6380952381, 0.6476190476, 0.6571428571, 0.6666666667, 0.6761904762, 0.6857142857, 0.6952380952, 0.7047619048, 0.7142857143, 0.7238095238, 0.7333333333, 0.7428571429, 0.7523809524, 0.7619047619, 0.7714285714, 0.780952381, 0.7904761905, 0.8, 0.8095238095, 0.819047619, 0.8285714286, 0.8380952381, 0.8476190476, 0.8571428571, 0.8666666667, 0.8761904762, 0.8857142857, 0.8952380952, 0.9047619048, 0.9142857143, 0.9238095238, 0.9333333333, 0.9428571429, 0.9523809524, 0.9619047619, 0.9714285714, 0.980952381, 0.9904761905, 1, 1, 1, 1, 1, 1], 5)
                Line((0.2730177369, 7.2475906874), (-7.4505839572, 2.8456761413))
                _nurbs_edge([(-7.4505839572, 2.8456761413), (-7.4714542547, 2.8345732193), (-7.5132438525, 2.812192738), (-7.5760752546, 2.7780981127), (-7.6601456967, 2.7315864549), (-7.7657156364, 2.6716928371), (-7.8717248539, 2.6100869127), (-7.9780769544, 2.5468898013), (-8.0846025224, 2.4823336322), (-8.1910311415, 2.4168149378), (-8.2969921144, 2.3508752461), (-8.4020376353, 2.2851249091), (-8.5056585698, 2.2201848463), (-8.6073030874, 2.15662207), (-8.7063944942, 2.0948849494), (-8.8023513487, 2.0352401291), (-8.8946166769, 1.9778183168), (-8.9826904872, 1.9226518586), (-9.0661641078, 1.8697109707), (-9.1447632247, 1.8189374472), (-9.218383962, 1.7702743685), (-9.2732948321, 1.7329933449), (-9.3122543077, 1.7059454976), (-9.3372429919, 1.6883176852), (-9.34949126, 1.6796048009)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-9.34949126, 1.6796048009), (-9.3677103631, 1.6704777953), (-9.4037533856, 1.6516688542), (-9.4566323739, 1.6217906652), (-9.5247622542, 1.5786173897), (-9.6059739148, 1.5191310764), (-9.6833027664, 1.454303953), (-9.7569200437, 1.3845451289), (-9.8271394321, 1.3105749464), (-9.8944727368, 1.2335396325), (-9.9595147593, 1.1547765109), (-10.0228138452, 1.0755499184), (-10.0847408489, 0.9967828415), (-10.1453742796, 0.918822912), (-10.2043353038, 0.8411013693), (-10.2609132387, 0.7624089564), (-10.3142765767, 0.6813519368), (-10.3636621897, 0.5967643113), (-10.4085574989, 0.5080983951), (-10.448931656, 0.4159355917), (-10.4851361451, 0.3216914183), (-10.5177207668, 0.2271158027), (-10.5472751316, 0.1338482178), (-10.5742741564, 0.0429917554), (-10.5988882149, -0.0454307422), (-10.6210181528, -0.13231275), (-10.6404093259, -0.219053571), (-10.6567377538, -0.3072374474), (-10.6697098358, -0.398269988), (-10.6791511216, -0.4930533222), (-10.684973561, -0.5921080981), (-10.6867138145, -0.6749605618), (-10.6863795336, -0.7391582277), (-10.6854293495, -0.7828698047), (-10.6847724245, -0.8049538777)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-10.6847724245, -0.8049538777), (-10.6864267352, -0.824637654), (-10.6893866989, -0.8649783261), (-10.6927806613, -0.9284087416), (-10.6952119341, -1.018826965), (-10.6947867818, -1.1414152474), (-10.6909978901, -1.2729753854), (-10.6840600662, -1.412286718), (-10.674353097, -1.5572385074), (-10.6624425619, -1.7047143861), (-10.6489407834, -1.8512626421), (-10.6343931493, -1.9936439456), (-10.6191454671, -2.1294673587), (-10.60323965, -2.2576989592), (-10.5862441766, -2.3794619709), (-10.5673347047, -2.4977235728), (-10.5455555629, -2.6161765544), (-10.520038972, -2.7383116858), (-10.490218016, -2.8665155732), (-10.4561034932, -3.0008942901), (-10.4182398697, -3.1394868134), (-10.3774830346, -3.279249797), (-10.3348338279, -3.4168052857), (-10.2912521827, -3.5492669008), (-10.247473437, -3.6750744069), (-10.2038414253, -3.7947118979), (-10.1603657114, -3.9100088451), (-10.1167590992, -4.0235551239), (-10.0724826185, -4.1380835181), (-10.0267833306, -4.255851712), (-9.9787426367, -4.3780685893), (-9.9274698871, -4.5050123765), (-9.8722810363, -4.6361030964), (-9.812895988, -4.7699827844), (-9.7496018986, -4.9046015121), (-9.683504124, -5.0372650177), (-9.6163778507, -5.1648631055), (-9.5503317693, -5.2841806384), (-9.4875231679, -5.3921930461), (-9.4298732563, -5.4863447844), (-9.3787309937, -5.5648962107), (-9.3435241451, -5.6146213456), (-9.3204208285, -5.6444283909), (-9.3064840551, -5.6609762992), (-9.2998820592, -5.6684193532)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
                Line((-8.8855927452, -5.5038121209), (-9.2998820592, -5.6684193532))
                _nurbs_edge([(-8.7906151455, -1.9997565496), (-8.8058347528, -2.0114465753), (-8.8349982062, -2.0343018022), (-8.8749166589, -2.067011537), (-8.9204691158, -2.1074607237), (-8.9649549222, -2.153631771), (-8.99803476, -2.1979002669), (-9.0220904711, -2.2457195367), (-9.0405274356, -2.3045908888), (-9.0566811802, -2.3812661613), (-9.0727392791, -2.4788916497), (-9.0893588343, -2.5961556442), (-9.1062297925, -2.729093709), (-9.1223786382, -2.8721653444), (-9.1365688277, -3.0195963727), (-9.1476653936, -3.1666328153), (-9.1549911892, -3.3107432262), (-9.1582276514, -3.4510648921), (-9.1573461105, -3.5879645594), (-9.1525304363, -3.7225653366), (-9.1441062774, -3.8562975468), (-9.1324691603, -3.990438836), (-9.1180158488, -4.1256715329), (-9.1011335001, -4.2622174112), (-9.082188013, -4.3999562103), (-9.0615130083, -4.5385475776), (-9.0393989409, -4.6775483496), (-9.0160819068, -4.8165328543), (-8.9917335023, -4.9552051462), (-8.9664717155, -5.0933712876), (-8.9403706687, -5.2309188889), (-8.9188506536, -5.3404195043), (-8.9023584247, -5.4222358207), (-8.891207348, -5.4766428794), (-8.8855927452, -5.5038121209)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((-3.1035017534, 2.1625959828), 0.484690189, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.0870976505, -1.1103090346), 0.4848978513, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.7629964168, 5.5943927198), 0.4839329181, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_133630_3d294c66_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1550147206, perimeter: 37.8832919653
            with BuildLine():
                Line((0, 0), (0.77, 0))
                Line((0.77, 0), (0.77, 5.5))
                Line((0.77, 5.5), (0, 5.5))
                Line((0, 5.5), (0, 1.088944443))
                Line((0, 1.088944443), (-4.7604013514, 5.8493457944))
                Line((-5.77, 5.8493457944), (-4.7604013514, 5.8493457944))
                Line((-5.77, 0), (-5.77, 5.8493457944))
                Line((-5, 0), (-5.77, 0))
                Line((-5, 5), (-5, 0))
                Line((0, 0), (-5, 5))
            make_face()
        # OneSide extrude, distance=7.012
        extrude(amount=7.012)
    return part.part


def model_133654_8bd3bccc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.7313686294, perimeter: 30.8364606199
            with BuildLine():
                CenterArc((10.461586913, 13.8849712751), 17.3849713272, -126.9960797257, 36.996088571)
                Line((12.3927692951, -3.5000000522), (10.4615895969, -3.5000000522))
                CenterArc((12.6000001878, -3.5000000522), 0.2072308926, 0, 180)
                Line((13, -3.5000000522), (12.8072310804, -3.5000000522))
                Line((13, -2.2849365401), (13, -3.5000000522))
                Line((13, 0), (13, -2.2849365401))
                Line((12.8735682654, 0), (13, 0))
                CenterArc((12.8000001907, 0), 0.0735680747, -180, 180)
                Line((12.6735682654, 0), (12.726432116, 0))
                CenterArc((12.6000001907, 0), 0.0735680747, -180, 180)
                Line((12.4735682654, 0), (12.526432116, 0))
                CenterArc((12.4000001907, 0), 0.0735680747, -180, 180)
                Line((12.2735682654, 0), (12.326432116, 0))
                CenterArc((12.2000001907, 0), 0.0735680747, -180, 180)
                Line((0, 0), (12.126432116, 0))
            make_face()
            # Profile area: 24.5658249895, perimeter: 32.7037760371
            with BuildLine():
                Line((13, 0), (13, -2.2849365401))
                CenterArc((15.4443204902, -12.5598291585), 10.5616343895, 76.6184924518, 26.7630150965)
                CenterArc((21.17118695, -20.998953063), 18.9997242733, 80.0511994908, 19.8976010184)
                CenterArc((24, -1.1875184408), 1.1875184408, -67.5371110359, 157.5371110359)
                Line((13, 0), (24, 0))
            make_face()
            with BuildLine():
                CenterArc((15.3924083038, -1.0368202018), 0.2452122297, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((19.5111922201, -1.0368202018), 0.2452122297, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((24, -1.1875184408), 0.2452122297, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_133710_00be7f31_0002():
    """Model: Lateral pieza exterior"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1160.4503940345, perimeter: 378.6516249707
            with BuildLine():
                Line((-28.6578435483, 26.7000237994), (-7.4252663289, -0.0207535691))
                Line((-7.4252663289, -0.0207535691), (-1.8748525255, 0.0331339435))
                Line((-1.8748525255, 0.0331339435), (-33.6340373663, 43.7615035675))
                CenterArc((-65.3180202465, 20.7499557455), 39.1587296055, 35.990277814, 51.726509891)
                Line((-68.8812890865, 60.0818676889), (-63.7579745945, 59.8775976612))
                CenterArc((-69.403982759, 46.9721418127), 13.1201418142, 87.716787705, 88.5858068942)
                Line((-85.5865794411, 0.0050650728), (-82.4968155169, 47.8182219497))
                Line((-85.5865794411, 0.0050650728), (-80.2264645145, 0.0050650728))
                Line((-80.2264645145, 0.0050650728), (-76.7926147029, 32.5231713085))
                CenterArc((-73.4336646519, 32.1684726088), 3.377625884, 87.1365468142, 86.8354681678)
                Line((-73.2649323635, 35.5418812746), (-42.9102673295, 34.0235914371))
                CenterArc((-43.8816507183, 14.6030455995), 19.4448241524, 38.4709791774, 48.6655676368)
            make_face()
            with BuildLine():
                Line((-75.8039630733, 41.8855722537), (-75.033034625, 49.1861632976))
                CenterArc((-67.2003621389, 48.3590480669), 7.8762223102, 88.1824993055, 85.7895156765)
                Line((-66.9505594654, 56.2313080032), (-64.5343094908, 56.1546355218))
                CenterArc((-65.4106992987, 28.5361625975), 27.6323742332, 38.4709791774, 49.7115201281)
                Line((-40.4756041224, 41.5724411246), (-43.7766678629, 45.7267643788))
                Line((-75.8039630733, 41.8855722537), (-40.4756041224, 41.5724411246))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_133768_6787114d_0021():
    """Model: D v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_133768_6787114d_0029():
    """Model: Part v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_133768_6787114d_0030():
    """Model: Shaft v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=2.55
        extrude(amount=2.55)
    return part.part


def model_133813_d9ccc7d4_0000():
    """Model: disc v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 28.2036480476, perimeter: 19.7920337176
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_133989_1aa964b4_0004():
    """Model: M3x15 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495467, perimeter: 1.5707963502
            Circle(0.2500000037)
        # OneSide extrude, distance=0.287
        extrude(amount=0.287)
    return part.part


def model_133989_b2a532b9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 102 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.1224563589, perimeter: 60.7672548389
            with BuildLine():
                Line((-2, 1.0000000149), (-1.0000000149, 1.0000000149))
                Line((-1.0000000149, 1.0000000149), (-1.0000000149, 0.8000000119))
                Line((-1.0000000149, 0.8000000119), (-2, 0.8000000119))
                Line((-2, 0.6000000089), (-2, 0.8000000119))
                Line((-2, 0.6000000089), (-1.2000000179, 0.6000000089))
                Line((-1.2000000179, 0.6000000089), (-1.2000000179, 0.400000006))
                Line((-1.2000000179, 0.400000006), (-2, 0.400000006))
                Line((-2, 0.200000003), (-2, 0.400000006))
                Line((-2, 0.200000003), (-1.4000000209, 0.200000003))
                Line((-1.4000000209, 0.200000003), (-1.4000000209, 0.1000000015))
                Line((-1.4000000209, 0.1000000015), (-2, 0.1000000015))
                Line((-2, -0.1000000015), (-2, 0.1000000015))
                Line((-1.4000000209, -0.1000000015), (-2, -0.1000000015))
                Line((-1.4000000209, -0.200000003), (-1.4000000209, -0.1000000015))
                Line((-2, -0.200000003), (-1.4000000209, -0.200000003))
                Line((-2, -0.400000006), (-2, -0.200000003))
                Line((-1.2000000179, -0.400000006), (-2, -0.400000006))
                Line((-1.2000000179, -0.6000000089), (-1.2000000179, -0.400000006))
                Line((-2, -0.6000000089), (-1.2000000179, -0.6000000089))
                Line((-2, -0.8000000119), (-2, -0.6000000089))
                Line((-1.0000000149, -0.8000000119), (-2, -0.8000000119))
                Line((-1.0000000149, -1.0000000149), (-1.0000000149, -0.8000000119))
                Line((-2, -1.0000000149), (-1.0000000149, -1.0000000149))
                Line((-2, -1.2000000179), (-2, -1.0000000149))
                Line((-0.7000000104, -1.2000000179), (-2, -1.2000000179))
                Line((-0.7000000104, -1.4002126807), (-0.7000000104, -1.2000000179))
                Line((-2, -1.4002126807), (-0.7000000104, -1.4002126807))
                Line((-2, -2), (-2, -1.4002126807))
                Line((-1.4000000209, -2), (-2, -2))
                Line((-1.4000000209, -2), (-1.4000000209, -1.7000000253))
                Line((-1.4000000209, -1.7000000253), (-1.2000000179, -1.7000000253))
                Line((-1.2000000179, -1.7000000253), (-1.2000000179, -2))
                Line((-1.0000000149, -2), (-1.2000000179, -2))
                Line((-1.0000000149, -2), (-1.0000000149, -1.7000000253))
                Line((-1.0000000149, -1.7000000253), (-0.8000000119, -1.7000000253))
                Line((-0.8000000119, -1.7000000253), (-0.8000000119, -2))
                Line((-0.6000000089, -2), (-0.8000000119, -2))
                Line((-0.6000000089, -2), (-0.6000000089, -1.7000000253))
                Line((-0.6000000089, -1.7000000253), (-0.400000006, -1.7000000253))
                Line((-0.400000006, -1.7000000253), (-0.400000006, -2))
                Line((-0.200000003, -2), (-0.400000006, -2))
                Line((-0.200000003, -2), (-0.200000003, -1.7000000253))
                Line((-0.200000003, -1.7000000253), (-0.1000000015, -1.7000000253))
                Line((-0.1000000015, -1.7000000253), (-0.1000000015, -2))
                Line((0.1000000015, -2), (-0.1000000015, -2))
                Line((0.1000000015, -1.7000000253), (0.1000000015, -2))
                Line((0.200000003, -1.7000000253), (0.1000000015, -1.7000000253))
                Line((0.200000003, -2), (0.200000003, -1.7000000253))
                Line((0.400000006, -2), (0.200000003, -2))
                Line((0.400000006, -1.7000000253), (0.400000006, -2))
                Line((0.6000000089, -1.7000000253), (0.400000006, -1.7000000253))
                Line((0.6000000089, -2), (0.6000000089, -1.7000000253))
                Line((0.8000000119, -2), (0.6000000089, -2))
                Line((0.8000000119, -1.7000000253), (0.8000000119, -2))
                Line((1.0000000149, -1.7000000253), (0.8000000119, -1.7000000253))
                Line((1.0000000149, -2), (1.0000000149, -1.7000000253))
                Line((1.2000000179, -2), (1.0000000149, -2))
                Line((1.2000000179, -1.7000000253), (1.2000000179, -2))
                Line((1.4000000209, -1.7000000253), (1.2000000179, -1.7000000253))
                Line((1.4000000209, -2), (1.4000000209, -1.7000000253))
                Line((2, -2), (1.4000000209, -2))
                Line((2, -1.4000000209), (2, -2))
                Line((2, -1.4000000209), (0.7000000104, -1.4000000209))
                Line((0.7000000104, -1.4000000209), (0.7000000104, -1.2000000179))
                Line((0.7000000104, -1.2000000179), (2, -1.2000000179))
                Line((2, -1.0000000149), (2, -1.2000000179))
                Line((2, -1.0000000149), (1.0000000149, -1.0000000149))
                Line((1.0000000149, -1.0000000149), (1.0000000149, -0.8000000119))
                Line((1.0000000149, -0.8000000119), (2, -0.8000000119))
                Line((2, -0.6000000089), (2, -0.8000000119))
                Line((2, -0.6000000089), (1.2000000179, -0.6000000089))
                Line((1.2000000179, -0.6000000089), (1.2000000179, -0.400000006))
                Line((1.2000000179, -0.400000006), (2, -0.400000006))
                Line((2, -0.200000003), (2, -0.400000006))
                Line((2, -0.200000003), (1.4000000209, -0.200000003))
                Line((1.4000000209, -0.200000003), (1.4000000209, -0.1000000015))
                Line((1.4000000209, -0.1000000015), (2, -0.1000000015))
                Line((2, 0.1000000015), (2, -0.1000000015))
                Line((1.4000000209, 0.1000000015), (2, 0.1000000015))
                Line((1.4000000209, 0.200000003), (1.4000000209, 0.1000000015))
                Line((2, 0.200000003), (1.4000000209, 0.200000003))
                Line((2, 0.400000006), (2, 0.200000003))
                Line((1.2000000179, 0.400000006), (2, 0.400000006))
                Line((1.2000000179, 0.6000000089), (1.2000000179, 0.400000006))
                Line((2, 0.6000000089), (1.2000000179, 0.6000000089))
                Line((2, 0.8000000119), (2, 0.6000000089))
                Line((1.0000000149, 0.8000000119), (2, 0.8000000119))
                Line((1.0000000149, 1.0000000149), (1.0000000149, 0.8000000119))
                Line((2, 1.0000000149), (1.0000000149, 1.0000000149))
                Line((2, 1.2000000179), (2, 1.0000000149))
                Line((0.7000000104, 1.2000000179), (2, 1.2000000179))
                Line((0.7000000104, 1.4000000209), (0.7000000104, 1.2000000179))
                Line((2, 1.4000000209), (0.7000000104, 1.4000000209))
                Line((2, 2), (2, 1.4000000209))
                Line((-2, 2), (2, 2))
                Line((-2, 1.3930138482), (-2, 2))
                Line((-2, 1.3930138482), (-0.7000000104, 1.3930138482))
                Line((-0.7000000104, 1.3930138482), (-0.7000000104, 1.2000000179))
                Line((-0.7000000104, 1.2000000179), (-2, 1.2000000179))
                Line((-2, 1.0000000149), (-2, 1.2000000179))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6000000238, 1.6000000238), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6000000238, 1.6000000238), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6000000238, -1.6000000238), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6000000238, -1.6000000238), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.25
        extrude(amount=5.25)
    return part.part


def model_133998_c71b3d55_0003():
    """Model: OutsideLegBlocks (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.8709, perimeter: 25.4
            with BuildLine():
                Line((-4.445, 1.905), (-4.445, -1.905))
                Line((-4.445, -1.905), (4.445, -1.905))
                Line((4.445, -1.905), (4.445, 1.905))
                Line((4.445, 1.905), (-4.445, 1.905))
            make_face()
        # OneSide extrude, distance=85.725
        extrude(amount=85.725)
    return part.part


def model_134013_9b4cfef2_0004():
    """Model: Rohr v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.086393798, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=16.2
        extrude(amount=16.2)
    return part.part


def model_134013_9b4cfef2_0007():
    """Model: Bild v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 256, perimeter: 64
            with BuildLine():
                Line((-8, 8), (8, 8))
                Line((-8, -8), (-8, 8))
                Line((8, -8), (-8, -8))
                Line((8, 8), (8, -8))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_134189_c08fdee5_0008():
    """Model: Energiekette_Endstück_Aussen v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7259115717, perimeter: 9.0399239845
            with BuildLine():
                CenterArc((2.8850000507, 0.5000000075), 0.5000000075, -90, 180)
                Line((2.8850000507, 1.0000000149), (1.8000000268, 1.0000000149))
                Line((1.8000000268, 1.0000000149), (0, 0.5000000075))
                Line((0, 0.5000000075), (0, 0))
                Line((0, 0), (2.8850000507, 0))
            make_face()
            with BuildLine():
                CenterArc((2.8850000507, 0.5000000075), 0.18, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.124
        extrude(amount=0.124)
    return part.part


def model_134189_c08fdee5_0010():
    """Model: Energiekette_Endstück_Innen v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.4887739322, perimeter: 7.0436400309
            with BuildLine():
                Line((-1.0000000149, 0.5000000075), (-1.0000000149, 0.3499999922))
                Line((-1.0000000149, 0.3499999922), (0.9799999781, 0.3499999922))
                Line((0.9799999781, 0.3499999922), (1.006250338, 0.3499999922))
                CenterArc((1.1040000194, 0.3430000075), 0.098, 175.9039651945, 144.090823457)
                Line((2.3000000343, 0.2799999937), (1.1790666449, 0.2799999937))
                Line((2.3000000343, 0.400000006), (2.3000000343, 0.2799999937))
                Line((1.3000000194, 0.400000006), (2.3000000343, 0.400000006))
                Line((1.3000000194, 0.5000000075), (1.3000000194, 0.400000006))
                Line((-1.0000000149, 0.5000000075), (1.3000000194, 0.5000000075))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


def model_134193_b8d974d8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.7441563281, perimeter: 43.4316805127
            with BuildLine():
                Line((-10, -5), (0, -5))
                Line((0, -5), (7.1396320077, -0.0011687344))
                Line((-2.8586987354, 0), (7.1396320077, -0.0011687344))
                Line((-10, -5), (-2.8586987354, 0))
            make_face()
            with BuildLine():
                Line((-2, -3.25), (-2, -1.75))
                Line((-2, -1.75), (-0.5, -1.75))
                Line((-0.5, -1.75), (-0.5, -3.25))
                Line((-0.5, -3.25), (-2, -3.25))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_134504_78fae2e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.2101482734, perimeter: 28.1738766654
            with BuildLine():
                Line((4.615, -2), (4.615, 1.1))
                Line((2.115, 2), (4.615, 1.1))
                Line((2.115, 2), (0.115, 2))
                Line((-4.615, 0.7), (0.115, 2))
                Line((-4.615, -2), (-4.615, 0.7))
                Line((4.615, -2), (-4.615, -2))
            make_face()
            with BuildLine():
                CenterArc((-0.385, 0), 0.285, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.145, 0), 0.285, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.97
        extrude(amount=0.97)
    return part.part


def model_134597_776fec5d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.25, perimeter: 12.2111025509
            with BuildLine():
                Line((2, 0), (0, 3))
                Line((0, 3), (-2, 0))
                Line((-2, 0), (-0.75, 0))
                Line((0, 1), (-0.75, 0))
                Line((0.75, 0), (0, 1))
                Line((0.75, 0), (2, 0))
            make_face()
            # Profile area: 0.75, perimeter: 4
            with BuildLine():
                Line((0.75, 0), (0, 1))
                Line((0, 1), (-0.75, 0))
                Line((-0.75, 0), (0.75, 0))
            make_face()
            # Profile area: 1.9856074491, perimeter: 5.9712148983
            with BuildLine():
                Line((-0.9856074491, -7), (1, -7))
                Line((-0.9856074491, -7), (-0.9856074491, -8))
                Line((-0.9856074491, -8), (1, -8))
                Line((1, -8), (1, -7))
            make_face()
            # Profile area: 19.2, perimeter: 19.8449987799
            with BuildLine():
                Line((-0.8, -3), (0.8, -3))
                Line((-0.8, -3), (-4, -7))
                Line((-4, -7), (-0.9856074491, -7))
                Line((-0.9856074491, -7), (1, -7))
                Line((1, -7), (4, -7))
                Line((4, -7), (0.8, -3))
            make_face()
            # Profile area: 0.8, perimeter: 4.161249695
            with BuildLine():
                Line((0.8, -3), (0, -2))
                Line((0, -2), (-0.8, -3))
                Line((-0.8, -3), (0.8, -3))
            make_face()
            # Profile area: 10.45, perimeter: 15.961249695
            with BuildLine():
                Line((-0.75, 0), (0.75, 0))
                Line((-0.75, 0), (-3, -3))
                Line((-3, -3), (-0.8, -3))
                Line((0, -2), (-0.8, -3))
                Line((0.8, -3), (0, -2))
                Line((0.8, -3), (3, -3))
                Line((3, -3), (0.75, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_134783_0a059b7d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.9781742838, perimeter: 572.3432252516
            with BuildLine():
                CenterArc((-75, 0), 3.2385, 115.6464037772, 128.7071924456)
                Line((-76.401674616, -2.9194503799), (-15.4514013552, -32.1826471293))
                CenterArc((0, 0), 35.6997, -115.6464037772, 231.2928075544)
                Line((-76.401674616, 2.9194503799), (-15.4514013552, 32.1826471293))
            make_face()
            with BuildLine():
                Line((-76.3412102208, 2.7935133047), (-15.39093696, 32.0567100541))
                CenterArc((0, 0), 35.56, -115.6464037772, 231.2928075544)
                Line((-76.3412102208, -2.7935133047), (-15.39093696, -32.0567100541))
                CenterArc((-75, 0), 3.0988, 115.6464037772, 128.7071924456)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_134862_699d5eed_0002():
    """Model: STAIRS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 65.9366190483, perimeter: 40.6845255468
            with BuildLine():
                Line((40.1326250034, 0), (40.1326250034, 0.1056049123))
                Line((40.1326250034, 0.1056049123), (40.1326250034, 0.2755223455))
                Line((40.1326250034, 0.2755223455), (40.1326250034, 2.7755223455))
                Line((40.1326250034, 2.7755223455), (37.6326250034, 2.7755223455))
                Line((37.6326250034, 2.7755223455), (37.6326250034, 5.2755223455))
                Line((37.6326250034, 5.2755223455), (35.1326250034, 5.2755223455))
                Line((35.1326250034, 5.2755223455), (35.1326250034, 7.7755223455))
                Line((35.1326250034, 7.7755223455), (32.6326250034, 7.7755223455))
                Line((32.6326250034, 7.7755223455), (32.6326250034, 10.2755223455))
                Line((32.6326250034, 10.2755223455), (30.1326250034, 10.2755223455))
                Line((30.1326250034, 10.2755223455), (30, 0))
                Line((30, 0), (40.1326250034, 0))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_134862_b757f2b8_0001():
    """Model: INSULATED PEX"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 49 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 33.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.8215219378, perimeter: 28.9606469031
            with BuildLine():
                Line((3, 4.0049695421), (16.9927993644, 4.0049695421))
                Line((3, 4.0049695421), (3.0000000447, 3.5000000522))
                Line((16.9927993644, 3.5349344214), (3.0000000447, 3.5000000522))
                Line((16.9927993644, 3.5349344214), (16.9927993644, 4.0049695421))
            make_face()
            # Profile area: 7.3896581757, perimeter: 29.0418074234
            with BuildLine():
                Line((3, 3.0236423848), (16.9927993644, 3.0236423848))
                Line((3, 3.0236423848), (3, 2.4955380374))
                Line((16.9927993644, 2.4955380374), (3, 2.4955380374))
                Line((16.9927993644, 2.4955380374), (16.9927993644, 3.0236423848))
            make_face()
            # Profile area: 7.6828088638, perimeter: 29.0837076437
            with BuildLine():
                Line((16.9927993644, 9), (3, 9))
                Line((3, 9), (3, 8.4509455425))
                Line((16.9927993644, 8.4509455425), (3, 8.4509455425))
                Line((16.9927993644, 8.4509455425), (16.9927993644, 9))
            make_face()
            # Profile area: 6.6241121831, perimeter: 28.932387432
            with BuildLine():
                Line((3, 8), (16.9927993644, 8))
                Line((3, 8), (3, 7.5266056483))
                Line((16.9927993644, 7.5266056483), (3, 7.5266056483))
                Line((16.9927993644, 7.5266056483), (16.9927993644, 8))
            make_face()
            # Profile area: 7.6347154541, perimeter: 29.0768336211
            with BuildLine():
                Line((3, 6), (16.9927993644, 6))
                Line((3, 6), (3, 5.4543825538))
                Line((16.9927993644, 5.4543825538), (3, 5.4543825538))
                Line((16.9927993644, 5.4543825538), (16.9927993644, 6))
            make_face()
            # Profile area: 7.3156510922, perimeter: 29.0312972015
            with BuildLine():
                Line((3, 2.0445725274), (16.9927993647, 2.0010583114))
                Line((3, 2.0445725274), (3, 1.5000000224))
                Line((16.992799364, 1.5000000028), (3, 1.5000000224))
                Line((16.992799364, 1.5000000028), (16.9927993647, 2.0010583114))
            make_face()
            # Profile area: 6.9192964128, perimeter: 28.9745783078
            with BuildLine():
                Line((3, 7), (16.9927993644, 7))
                Line((3, 7), (3, 6.5055102105))
                Line((16.9927993644, 6.5055102105), (3, 6.5055102105))
                Line((16.9927993644, 6.5055102105), (16.9927993644, 7))
            make_face()
            # Profile area: 19.3835543626, perimeter: 23.3835543626
            with BuildLine():
                Line((3, 2.0445725274), (3, 1.5000000224))
                Line((3, 2.4955380374), (3, 2.0445725274))
                Line((3, 3.0236423848), (3, 2.4955380374))
                Line((3.0000000447, 3.5000000522), (3, 3.0236423848))
                Line((3, 4.0049695421), (3.0000000447, 3.5000000522))
                Line((3, 4.5129146899), (3, 4.0049695421))
                Line((3, 4.999940318), (3, 4.5129146899))
                Line((3, 5.4543825538), (3, 4.999940318))
                Line((3, 6), (3, 5.4543825538))
                Line((3, 6.5055102105), (3, 6))
                Line((3, 7), (3, 6.5055102105))
                Line((3, 7.5266056483), (3, 7))
                Line((3, 8), (3, 7.5266056483))
                Line((3, 8.4509455425), (3, 8))
                Line((3, 9), (3, 8.4509455425))
                Line((3, 9), (3, 9.7917771813))
                Line((3, 9.7917771813), (1, 9.7917771813))
                Line((1, 9.7917771813), (1, 0.1))
                Line((2.4933785972, 0.1), (1, 0.1))
                Line((3, 0.1), (2.4933785972, 0.1))
                Line((3, 1.5000000224), (3, 0.1))
            make_face()
            # Profile area: 6.8148518988, perimeter: 28.9596499848
            with BuildLine():
                Line((3, 4.999940318), (16.9927993644, 4.999940318))
                Line((3, 4.999940318), (3, 4.5129146899))
                Line((16.9927993644, 4.5129146899), (3, 4.5129146899))
                Line((16.9927993644, 4.5129146899), (16.9927993644, 4.999940318))
            make_face()
            # Profile area: 15.0540047645, perimeter: 19.0144012688
            with BuildLine():
                Line((19, 1.5), (19, 9))
                Line((19, 9), (16.9927993644, 9))
                Line((16.9927993644, 8.4509455425), (16.9927993644, 9))
                Line((16.9927993644, 8), (16.9927993644, 8.4509455425))
                Line((16.9927993644, 7.5266056483), (16.9927993644, 8))
                Line((16.9927993644, 7), (16.9927993644, 7.5266056483))
                Line((16.9927993644, 6.5055102105), (16.9927993644, 7))
                Line((16.9927993644, 6), (16.9927993644, 6.5055102105))
                Line((16.9927993644, 5.4543825538), (16.9927993644, 6))
                Line((16.9927993644, 4.999940318), (16.9927993644, 5.4543825538))
                Line((16.9927993644, 4.5129146899), (16.9927993644, 4.999940318))
                Line((16.9927993644, 4.0049695421), (16.9927993644, 4.5129146899))
                Line((16.9927993644, 3.5349344214), (16.9927993644, 4.0049695421))
                Line((16.9927993644, 3.0236423848), (16.9927993644, 3.5349344214))
                Line((16.9927993644, 2.4955380374), (16.9927993644, 3.0236423848))
                Line((16.9927993647, 2.0010583114), (16.9927993644, 2.4955380374))
                Line((16.992799364, 1.5000000028), (16.9927993647, 2.0010583114))
                Line((19, 1.5), (16.992799364, 1.5000000028))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_135070_b300af8d_0013():
    """Model: pin1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.02
        extrude(amount=1.02)
    return part.part


def model_135070_b300af8d_0015():
    """Model: kol1 v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7246760035, perimeter: 5.1920666512
            with BuildLine():
                CenterArc((0, 0), 0.25, 90, 180)
                Line((0, -0.25), (1.1823166315, -0.25))
                CenterArc((1.1823166315, 0), 0.25, -90, 180)
                Line((1.1823166315, 0.25), (0, 0.25))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1823166315, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_135070_b300af8d_0017():
    """Model: l kol v7 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3238001087, perimeter: 8.971964721
            with BuildLine():
                Line((0.3328452354, 2.6998965723), (0.2250699433, 2.6999300752))
                CenterArc((0.225, 2.4749300861), 0.225, 89.982189086, 90.017810914)
                Line((0, 2.4749300861), (0, 2.5000000373))
                Line((0, 2.5000000373), (-0.2716776299, 0.739829677))
                CenterArc((-0.5820501914, 0.7877348593), 0.3140478203, -65.0407314907, 56.2665189079)
                Line((-0.4495302198, 0.503016594), (-1.1062236915, 0.1973635649))
                CenterArc((-1.0218289191, 0.0160419656), 0.2, 114.9592685093, 180.0000012074)
                Line((-0.9374341429, -0.165279632), (-0.0315507951, 0.2563569476))
                CenterArc((-0.1159455675, 0.437678547), 0.2, -65.0407314907, 56.2665189079)
                Line((0.0817138598, 0.4071703383), (0.3718707437, 2.2870658124))
                Line((0.3718707437, 2.2870658124), (0.4077752921, 2.5196875485))
                Line((0.4077752921, 2.5196875485), (0.5532719347, 2.5196875485))
                CenterArc((0.3327752921, 2.4748965831), 0.225, 11.4826364128, 78.4995526732)
            make_face()
            with BuildLine():
                CenterArc((-0.1159455675, 0.437678547), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.0218289191, 0.0160419656), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_135094_15befe88_0001():
    """Model: Micro USB Plug"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4914159265, perimeter: 2.8283185307
            with BuildLine():
                CenterArc((0.4, -0.15), 0.1, -90, 90)
                Line((0.5, 0.15), (0.5, -0.15))
                CenterArc((0.4, 0.15), 0.1, 0, 90)
                Line((-0.4, 0.25), (0.4, 0.25))
                CenterArc((-0.4, 0.15), 0.1, 90, 90)
                Line((-0.5, -0.15), (-0.5, 0.15))
                CenterArc((-0.4, -0.15), 0.1, 180, 90)
                Line((0.4, -0.25), (-0.4, -0.25))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


MODELS = {
    "model_128996_b5ff8312_0000": {"func": model_128996_b5ff8312_0000, "volume": 0.667981138, "area": 4.2411500823},
    "model_128996_b8d06bf2_0000": {"func": model_128996_b8d06bf2_0000, "volume": 17.0117242192, "area": 41.4847309907},
    "model_128996_bc7c82e0_0000": {"func": model_128996_bc7c82e0_0000, "volume": 9.3379199356, "area": 42.4649519119},
    "model_128996_be3a6361_0000": {"func": model_128996_be3a6361_0000, "volume": 0.6534512719, "area": 6.7858401318},
    "model_128996_ccc5fb94_0000": {"func": model_128996_ccc5fb94_0000, "volume": 7.8249219019, "area": 36.0497756999},
    "model_128996_ce71b660_0000": {"func": model_128996_ce71b660_0000, "volume": 39.6594656589, "area": 313.9707697998},
    "model_128996_d895c690_0000": {"func": model_128996_d895c690_0000, "volume": 1.8260507299, "area": 15.0011049209},
    "model_128996_de0fca55_0000": {"func": model_128996_de0fca55_0000, "volume": 2.3876104167, "area": 15.5194677087},
    "model_128996_decf48a5_0000": {"func": model_128996_decf48a5_0000, "volume": 7.8761944902, "area": 45.8317687778},
    "model_128996_e660b876_0000": {"func": model_128996_e660b876_0000, "volume": 0.3337942194, "area": 3.0630528373},
    "model_129696_aac1f710_0000": {"func": model_129696_aac1f710_0000, "volume": 34.7538833417, "area": 121.0857984213},
    "model_129699_881b4b3a_0002": {"func": model_129699_881b4b3a_0002, "volume": 0.6334635219, "area": 9.9758034947},
    "model_129854_5b7bfc38_0002": {"func": model_129854_5b7bfc38_0002, "volume": 14.6141786889, "area": 105.2220865598},
    "model_129941_4f0a8032_0000": {"func": model_129941_4f0a8032_0000, "volume": 403.531451, "area": 649.9987},
    "model_130459_57e34211_0000": {"func": model_130459_57e34211_0000, "volume": 12000, "area": 5800},
    "model_130540_e8c5e51b_0004": {"func": model_130540_e8c5e51b_0004, "volume": 0.7949476493, "area": 6.0114453248},
    "model_130604_4f758677_0000": {"func": model_130604_4f758677_0000, "volume": 278.6430161002, "area": 389.6478945737},
    "model_130605_c596617d_0000": {"func": model_130605_c596617d_0000, "volume": 526.408151544, "area": 679.2306834539},
    "model_130664_090d6ddd_0000": {"func": model_130664_090d6ddd_0000, "volume": 81.9853727945, "area": 170.9240604045},
    "model_130679_7a357a9c_0006": {"func": model_130679_7a357a9c_0006, "volume": 24.7159609668, "area": 175.8128472375},
    "model_130679_7a357a9c_0008": {"func": model_130679_7a357a9c_0008, "volume": 3.6900001289, "area": 29.1000008288},
    "model_130714_8b4a9662_0001": {"func": model_130714_8b4a9662_0001, "volume": 312.7250049175, "area": 442.7201641624},
    "model_130719_e4764a36_0007": {"func": model_130719_e4764a36_0007, "volume": 4.5, "area": 20},
    "model_130757_2772bec8_0001": {"func": model_130757_2772bec8_0001, "volume": 0.0034950218, "area": 0.2874557278},
    "model_130757_3a6352fd_0006": {"func": model_130757_3a6352fd_0006, "volume": 1.7784, "area": 20.0972},
    "model_130757_3a6352fd_0008": {"func": model_130757_3a6352fd_0008, "volume": 5.9079005022, "area": 76.2270443951},
    "model_130757_8bbd9729_0000": {"func": model_130757_8bbd9729_0000, "volume": 0.0133622735, "area": 0.348520435},
    "model_130757_95d3cd06_0001": {"func": model_130757_95d3cd06_0001, "volume": 0.00504, "area": 0.3648},
    "model_130757_b2c47f8d_0003": {"func": model_130757_b2c47f8d_0003, "volume": 0.196, "area": 4.48},
    "model_130757_b2c47f8d_0004": {"func": model_130757_b2c47f8d_0004, "volume": 0.0462, "area": 0.9965219854},
    "model_130757_c4798e9b_0001": {"func": model_130757_c4798e9b_0001, "volume": 0.1337745744, "area": 2.9217305314},
    "model_130850_227be64a_0001": {"func": model_130850_227be64a_0001, "volume": 0.5434758941, "area": 5.9721283646},
    "model_130996_b842b511_0003": {"func": model_130996_b842b511_0003, "volume": 133.6106365695, "area": 348.343410512},
    "model_130996_b842b511_0015": {"func": model_130996_b842b511_0015, "volume": 467.7866806069, "area": 1204.6396343861},
    "model_131014_17cad022_0004": {"func": model_131014_17cad022_0004, "volume": 1.53628725, "area": 8.0645},
    "model_131065_c82633e9_0000": {"func": model_131065_c82633e9_0000, "volume": 1.5795, "area": 23.04},
    "model_131066_7943a19c_0000": {"func": model_131066_7943a19c_0000, "volume": 3.8715, "area": 55.16},
    "model_131067_b78691f2_0000": {"func": model_131067_b78691f2_0000, "volume": 6.708, "area": 72.08},
    "model_131156_d1bee956_0000": {"func": model_131156_d1bee956_0000, "volume": 41.5845144447, "area": 310.6094117893},
    "model_131355_3bb5668a_0000": {"func": model_131355_3bb5668a_0000, "volume": 7045.4743983602, "area": 2309.8158932108},
    "model_131425_0b7b5ce2_0000": {"func": model_131425_0b7b5ce2_0000, "volume": 9648.1192229366, "area": 6217.6768325591},
    "model_131463_e4a55cfe_0003": {"func": model_131463_e4a55cfe_0003, "volume": 23.85, "area": 140.33},
    "model_131463_e4a55cfe_0004": {"func": model_131463_e4a55cfe_0004, "volume": 45.4511592654, "area": 917.5415038379},
    "model_131463_e4a55cfe_0008": {"func": model_131463_e4a55cfe_0008, "volume": 60.35, "area": 322.75},
    "model_131528_0743cfc4_0001": {"func": model_131528_0743cfc4_0001, "volume": 1.4775217078, "area": 20.1777563998},
    "model_131528_0743cfc4_0002": {"func": model_131528_0743cfc4_0002, "volume": 1.4729784625, "area": 20.5049236181},
    "model_131528_0743cfc4_0007": {"func": model_131528_0743cfc4_0007, "volume": 1.406342509, "area": 18.9851988451},
    "model_131557_45be02b8_0000": {"func": model_131557_45be02b8_0000, "volume": 913.5786716853, "area": 3755.0701100762},
    "model_131569_5e471769_0000": {"func": model_131569_5e471769_0000, "volume": 175.5231810519, "area": 488.4081458695},
    "model_131586_eff7d729_0000": {"func": model_131586_eff7d729_0000, "volume": 111330.1896615883, "area": 13076.8794205675},
    "model_131863_d8b2c0a3_0002": {"func": model_131863_d8b2c0a3_0002, "volume": 1000, "area": 4120},
    "model_131863_d8b2c0a3_0005": {"func": model_131863_d8b2c0a3_0005, "volume": 114.1082119527, "area": 364.152011088},
    "model_131882_5b95e1ad_0010": {"func": model_131882_5b95e1ad_0010, "volume": 1.0305142357, "area": 9.7740766806},
    "model_131894_4af6c952_0001": {"func": model_131894_4af6c952_0001, "volume": 2880, "area": 3488},
    "model_131958_e7821102_0000": {"func": model_131958_e7821102_0000, "volume": 80, "area": 168},
    "model_132030_c99db4e7_0000": {"func": model_132030_c99db4e7_0000, "volume": 4.2232356019, "area": 22.7055051491},
    "model_132148_a107f53e_0000": {"func": model_132148_a107f53e_0000, "volume": 38139.3159514356, "area": 28690.4265143998},
    "model_132321_74af461c_0000": {"func": model_132321_74af461c_0000, "volume": 1.3972128761, "area": 11.41776611},
    "model_132430_321b9be8_0000": {"func": model_132430_321b9be8_0000, "volume": 86.8749972913, "area": 136.8110193563},
    "model_132444_13a66007_0000": {"func": model_132444_13a66007_0000, "volume": 402.1990615336, "area": 316.6921744359},
    "model_132461_14abd2d0_0000": {"func": model_132461_14abd2d0_0000, "volume": 8.0383467605, "area": 38.6876651214},
    "model_132461_14abd2d0_0001": {"func": model_132461_14abd2d0_0001, "volume": 7.1628448964, "area": 34.6400860639},
    "model_132461_14abd2d0_0002": {"func": model_132461_14abd2d0_0002, "volume": 7.5889741223, "area": 36.6101466671},
    "model_132461_14abd2d0_0003": {"func": model_132461_14abd2d0_0003, "volume": 7.3720356073, "area": 35.6072067237},
    "model_132461_14abd2d0_0004": {"func": model_132461_14abd2d0_0004, "volume": 9.5607902674, "area": 45.7261543673},
    "model_132461_14abd2d0_0005": {"func": model_132461_14abd2d0_0005, "volume": 7.8097865393, "area": 37.6309962524},
    "model_132461_14abd2d0_0006": {"func": model_132461_14abd2d0_0006, "volume": 8.2746547857, "area": 39.780153274},
    "model_132527_404df1cf_0000": {"func": model_132527_404df1cf_0000, "volume": 15.4958237057, "area": 194.5798125345},
    "model_132569_1cbfed5b_0000": {"func": model_132569_1cbfed5b_0000, "volume": 766.253741735, "area": 777.972040579},
    "model_132601_ae380b60_0000": {"func": model_132601_ae380b60_0000, "volume": 591.982687, "area": 1041.9334},
    "model_132643_03c61ba8_0000": {"func": model_132643_03c61ba8_0000, "volume": 43.0252982665, "area": 191.7106098418},
    "model_132735_7fc55abd_0000": {"func": model_132735_7fc55abd_0000, "volume": 180.6771430702, "area": 769.3871849089},
    "model_132772_70a3e5dc_0000": {"func": model_132772_70a3e5dc_0000, "volume": 1.2268231333, "area": 14.0178170028},
    "model_132863_90d729e2_0003": {"func": model_132863_90d729e2_0003, "volume": 33.0456099027, "area": 74.0739085728},
    "model_132863_90d729e2_0004": {"func": model_132863_90d729e2_0004, "volume": 0.594751775, "area": 12.8999345585},
    "model_132867_9ee8378c_0000": {"func": model_132867_9ee8378c_0000, "volume": 1179.8685725603, "area": 851.6111802338},
    "model_132946_aaef771a_0002": {"func": model_132946_aaef771a_0002, "volume": 0.539884187, "area": 5.0394718544},
    "model_132982_ee1eed2f_0000": {"func": model_132982_ee1eed2f_0000, "volume": 0.024833316, "area": 1.0320823017},
    "model_132996_c742ef84_0005": {"func": model_132996_c742ef84_0005, "volume": 54.3711128755, "area": 175.7724669197},
    "model_132996_c742ef84_0008": {"func": model_132996_c742ef84_0008, "volume": 303.8369026042, "area": 332.7208839367},
    "model_133073_013d4ebd_0001": {"func": model_133073_013d4ebd_0001, "volume": 1229.0297630836, "area": 3999.9918817902},
    "model_133073_013d4ebd_0002": {"func": model_133073_013d4ebd_0002, "volume": 863.3118494553, "area": 2873.4598108657},
    "model_133073_013d4ebd_0016": {"func": model_133073_013d4ebd_0016, "volume": 784.2886834266, "area": 4965.1000078339},
    "model_133073_013d4ebd_0019": {"func": model_133073_013d4ebd_0019, "volume": 40.9676587695, "area": 103.2255983528},
    "model_133073_013d4ebd_0022": {"func": model_133073_013d4ebd_0022, "volume": 80.4398174411, "area": 278.6891304834},
    "model_133109_dbf8891f_0002": {"func": model_133109_dbf8891f_0002, "volume": 79971, "area": 11467},
    "model_133109_dbf8891f_0005": {"func": model_133109_dbf8891f_0005, "volume": 64500, "area": 10960},
    "model_133131_e8fc0f93_0017": {"func": model_133131_e8fc0f93_0017, "volume": 1663.286996, "area": 5375.7957},
    "model_133131_e8fc0f93_0029": {"func": model_133131_e8fc0f93_0029, "volume": 1950.060616, "area": 6287.0842},
    "model_133131_e8fc0f93_0030": {"func": model_133131_e8fc0f93_0030, "volume": 2208.156874, "area": 7107.24385},
    "model_133131_e8fc0f93_0031": {"func": model_133131_e8fc0f93_0031, "volume": 1637.6794784679, "area": 5287.0774912361},
    "model_133402_47273d61_0000": {"func": model_133402_47273d61_0000, "volume": 10323.85032, "area": 16780.6116},
    "model_133402_47273d61_0001": {"func": model_133402_47273d61_0001, "volume": 114.7094699652, "area": 364.5154352086},
    "model_133402_47273d61_0002": {"func": model_133402_47273d61_0002, "volume": 57.3547276609, "area": 183.8706059711},
    "model_133402_47273d61_0003": {"func": model_133402_47273d61_0003, "volume": 2093.447426, "area": 6742.72845},
    "model_133402_47273d61_0005": {"func": model_133402_47273d61_0005, "volume": 1717.5664154679, "area": 5541.9156912361},
    "model_133402_47273d61_0006": {"func": model_133402_47273d61_0006, "volume": 5161.92516, "area": 16519.3218},
    "model_133402_47273d61_0007": {"func": model_133402_47273d61_0007, "volume": 88.080469, "area": 280.6446},
    "model_133402_47273d61_0008": {"func": model_133402_47273d61_0008, "volume": 1.8469572692, "area": 17.9440054132},
    "model_133402_47273d61_0009": {"func": model_133402_47273d61_0009, "volume": 7.2328432441, "area": 102.9159638929},
    "model_133402_47273d61_0012": {"func": model_133402_47273d61_0012, "volume": 278.580088, "area": 451.612},
    "model_133402_47273d61_0013": {"func": model_133402_47273d61_0013, "volume": 442.450728, "area": 709.676},
    "model_133402_47273d61_0014": {"func": model_133402_47273d61_0014, "volume": 630.901964, "area": 1006.4496},
    "model_133402_47273d61_0016": {"func": model_133402_47273d61_0016, "volume": 458.837792, "area": 735.4824},
    "model_133402_47273d61_0017": {"func": model_133402_47273d61_0017, "volume": 331.838046, "area": 535.4828},
    "model_133402_47273d61_0019": {"func": model_133402_47273d61_0019, "volume": 983.22384, "area": 1561.2872},
    "model_133402_47273d61_0021": {"func": model_133402_47273d61_0021, "volume": 1114.320352, "area": 1767.7384},
    "model_133402_47273d61_0023": {"func": model_133402_47273d61_0023, "volume": 59.4031221665, "area": 190.3222247078},
    "model_133402_47273d61_0024": {"func": model_133402_47273d61_0024, "volume": 49.161192, "area": 90.3224},
    "model_133402_47273d61_0026": {"func": model_133402_47273d61_0026, "volume": 334.6296405549, "area": 537.1099453083},
    "model_133402_47273d61_0027": {"func": model_133402_47273d61_0027, "volume": 102.4189179269, "area": 325.8054272212},
    "model_133402_47273d61_0028": {"func": model_133402_47273d61_0028, "volume": 524.3860814708, "area": 838.7080271786},
    "model_133402_47273d61_0029": {"func": model_133402_47273d61_0029, "volume": 315.4510021348, "area": 509.6764166778},
    "model_133402_47273d61_0030": {"func": model_133402_47273d61_0030, "volume": 66.5724517492, "area": 212.9028068976},
    "model_133402_47273d61_0031": {"func": model_133402_47273d61_0031, "volume": 2365.8823599663, "area": 7610.4686339399},
    "model_133402_47273d61_0032": {"func": model_133402_47273d61_0032, "volume": 61.3203916461, "area": 196.3608946025},
    "model_133402_47273d61_0033": {"func": model_133402_47273d61_0033, "volume": 4186.894852, "area": 13395.1345},
    "model_133402_47273d61_0034": {"func": model_133402_47273d61_0034, "volume": 532.57958, "area": 851.6112},
    "model_133402_47273d61_0036": {"func": model_133402_47273d61_0036, "volume": 86.032086, "area": 274.193},
    "model_133402_47273d61_0037": {"func": model_133402_47273d61_0037, "volume": 1288.432907, "area": 4172.5723},
    "model_133402_47273d61_0038": {"func": model_133402_47273d61_0038, "volume": 69.645035336, "area": 222.5802216193},
    "model_133564_b5340c41_0002": {"func": model_133564_b5340c41_0002, "volume": 0.7422012644, "area": 10.0373885282},
    "model_133564_b5340c41_0005": {"func": model_133564_b5340c41_0005, "volume": 26.2951305105, "area": 114.9194592683},
    "model_133604_d1452929_0000": {"func": model_133604_d1452929_0000, "volume": 15.0645883304, "area": 139.6584736149},
    "model_133630_3d294c66_0000": {"func": model_133630_3d294c66_0000, "volume": 99.2549632211, "area": 293.9476727023},
    "model_133654_8bd3bccc_0000": {"func": model_133654_8bd3bccc_0000, "volume": 23.3188774476, "area": 140.1825326685},
    "model_133710_00be7f31_0002": {"func": model_133710_00be7f31_0002, "volume": 1740.6755910517, "area": 2888.8782255249},
    "model_133768_6787114d_0021": {"func": model_133768_6787114d_0021, "volume": 0.6283185307, "area": 7.5398223686},
    "model_133768_6787114d_0029": {"func": model_133768_6787114d_0029, "volume": 1.2566370614, "area": 8.7964594301},
    "model_133768_6787114d_0030": {"func": model_133768_6787114d_0030, "volume": 8.0110612667, "area": 22.3053078405},
    "model_133813_d9ccc7d4_0000": {"func": model_133813_d9ccc7d4_0000, "volume": 2.8203648048, "area": 58.386499467},
    "model_133989_1aa964b4_0004": {"func": model_133989_1aa964b4_0004, "volume": 0.0563523199, "area": 0.8435176459},
    "model_133989_b2a532b9_0000": {"func": model_133989_b2a532b9_0000, "volume": 47.8928958842, "area": 337.2730006222},
    "model_133998_c71b3d55_0003": {"func": model_133998_c71b3d55_0003, "volume": 2903.5829025, "area": 2245.1568},
    "model_134013_9b4cfef2_0004": {"func": model_134013_9b4cfef2_0004, "volume": 1.3995795272, "area": 56.1559686829},
    "model_134013_9b4cfef2_0007": {"func": model_134013_9b4cfef2_0007, "volume": 76.8, "area": 531.2},
    "model_134189_c08fdee5_0008": {"func": model_134189_c08fdee5_0008, "volume": 0.3380130349, "area": 6.5727737174},
    "model_134189_c08fdee5_0010": {"func": model_134189_c08fdee5_0010, "volume": 0.4887739322, "area": 8.0211878953},
    "model_134193_b8d974d8_0000": {"func": model_134193_b8d974d8_0000, "volume": 9.5488312656, "area": 104.1746487587},
    "model_134504_78fae2e5_0000": {"func": model_134504_78fae2e5_0000, "volume": 31.2438438252, "area": 91.7489569123},
    "model_134597_776fec5d_0000": {"func": model_134597_776fec5d_0000, "volume": 3.8435607449, "area": 81.0568250313},
    "model_134783_0a059b7d_0000": {"func": model_134783_0a059b7d_0000, "volume": 152.3168440214, "area": 2260.5840367763},
    "model_134862_699d5eed_0002": {"func": model_134862_699d5eed_0002, "volume": 1318.7323809663, "area": 945.563749032},
    "model_134862_b757f2b8_0001": {"func": model_134862_b757f2b8_0001, "volume": 13.7460262735, "area": 221.9963775669},
    "model_135070_b300af8d_0013": {"func": model_135070_b300af8d_0013, "volume": 0.0320442451, "area": 0.7037167544},
    "model_135070_b300af8d_0015": {"func": model_135070_b300af8d_0015, "volume": 0.0724676004, "area": 1.9685586721},
    "model_135070_b300af8d_0017": {"func": model_135070_b300af8d_0017, "volume": 0.1323800109, "area": 3.5447966895},
    "model_135094_15befe88_0001": {"func": model_135094_15befe88_0001, "volume": 0.7371238898, "area": 5.2253096491},
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
