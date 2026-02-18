"""Batch 013 - passing/01_2ops
172 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_41902_43d78d0f_0001():
    """Model: Peg support beam v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.5464703842, perimeter: 38.3461632635
            with BuildLine():
                Line((0.9024165263, -4.8601058888), (0.9024165263, 10.6973941112))
                Line((0.9024165263, 10.6973941112), (-3.5684002096, 10.6973941112))
                Line((-3.5684002096, 10.6973941112), (-3.5684002096, -2.6196825921))
                Line((0.9024165263, -4.8601058888), (-3.5684002096, -2.6196825921))
            make_face()
        # OneSide extrude, distance=45.72
        extrude(amount=45.72)
    return part.part


def model_41902_43d78d0f_0006():
    """Model: Front Sup Leg v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 122.5804, perimeter: 101.6
            with BuildLine():
                Line((1.7085600544, 44.599636337), (1.7085600544, -3.660363663))
                Line((-0.8314399456, 44.599636337), (1.7085600544, 44.599636337))
                Line((-0.8314399456, -3.660363663), (-0.8314399456, 44.599636337))
                Line((1.7085600544, -3.660363663), (-0.8314399456, -3.660363663))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


def model_41902_43d78d0f_0023():
    """Model: seat pegs v1 (7)"""
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
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.8205753829, perimeter: 16.2625903303
            with BuildLine():
                Line((-2.081793411, 0.1816329822), (4.268206589, 0.1816329822))
                Line((4.268206589, 0.1816329822), (4.268206589, 1.9596329822))
                _nurbs_edge([(4.268206589, 1.9596329822), (4.141206589, 1.9692656285), (3.887206589, 1.9876897069), (3.506206589, 2.0128022584), (2.998206589, 2.0411548252), (2.363206589, 2.0674637786), (1.728206589, 2.0838248806), (1.093206589, 2.0894263108), (0.458206589, 2.0838248806), (-0.176793411, 2.0674637786), (-0.811793411, 2.0411548252), (-1.319793411, 2.0128022584), (-1.700793411, 1.9876897069), (-1.954793411, 1.9692656285), (-2.081793411, 1.9596329822)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.081793411, 0.1816329822), (-2.081793411, 1.9596329822))
            make_face()
        # OneSide extrude, distance=48.26
        extrude(amount=48.26)
    return part.part


def model_41902_43d78d0f_0024():
    """Model: BackLeg support v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 537.0076231995, perimeter: 139.3554166241
            with BuildLine():
                Line((9.0455804643, 3.0067529363), (0.2235482857, 5.54679184))
                Line((0.2235482857, 5.54679184), (0.2235482857, -56.36570816))
                Line((0.2235482857, -56.36570816), (9.1135482857, -56.36570816))
                Line((9.1135482857, -56.36570816), (9.0455804643, 3.0067529363))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_41907_7bcecdb1_0003():
    """Model: Bottle Opener"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5927506104, perimeter: 11.0817288289
            with BuildLine():
                Line((-0.5, 0), (-0.5, 3.0000000447))
                CenterArc((0, 0), 0.5, 180, 180.008694405)
                CenterArc((1.9554849527, -0.0311017489), 1.4558188446, 158.603920227, 20.1689471972)
                CenterArc((-0.82396555, 1.304793127), 1.6356557946, -29.4741514197, 36.3284378914)
                CenterArc((0.7500000112, 1.502172683), 0.050047183, -2.4881205009, 184.9762410018)
                CenterArc((0.3500000052, 1.4500000216), 0.3535533959, 171.8698976458, 196.2602047083)
                CenterArc((-2.750000041, 2.2500000335), 2.8504386052, -15.2551187031, 30.5102374061)
                Line((-0.5, 3.0000000447), (0, 3.0000000447))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_41907_7bcecdb1_0006():
    """Model: Phillips Screwdriver"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3498957532, perimeter: 11.822764801
            with BuildLine():
                Line((0.25, 4), (-0.25, 4))
                Line((-0.25, 4), (-0.25, 0.4330127019))
                CenterArc((0, 0), 0.5, 120, 300)
                Line((0.25, 4), (0.25, 0.4330127019))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


def model_41907_7bcecdb1_0008():
    """Model: Flashlight"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3291371368, perimeter: 10.0557519189
            with BuildLine():
                Line((-0.1, 2.5), (-0.1, 2.3))
                Line((-0.1, 2.5), (-0.6, 2.5))
                Line((-0.6, 0), (-0.6, 2.5))
                CenterArc((0, 0), 0.6, 180, 180)
                Line((0.6, 0), (0.6, 2.5))
                Line((0.6, 2.5), (0.1, 2.5))
                Line((0.1, 2.3), (0.1, 2.5))
                Line((-0.1, 2.3), (0.1, 2.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_41907_7bcecdb1_0011():
    """Model: Can Opener"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8061528709, perimeter: 12.0303009227
            with BuildLine():
                CenterArc((0.3019651398, 1.0318679961), 0.9285987343, 149.7265624495, 66.4781173302)
                CenterArc((-0.5571829503, 0.3605526507), 0.1647771893, -27.1291395631, 75.3192428963)
                CenterArc((0, 0), 0.5, 145.1919245251, 214.8080754749)
                Line((0.5, 0), (0.5, 3))
                Line((0.5, 3), (-0.5000000075, 3))
                Line((-0.5000000075, 3), (-0.4999999702, 2.0000000298))
                Line((-0.4999999702, 2.0000000298), (0.0000000298, 2.0000000298))
                Line((0.0000000298, 2.0000000298), (0.0000000298, 1.3000000194))
                CenterArc((-0.2500000037, 1.3000000194), 0.2500000335, 139.2226492641, 220.7773507359)
                CenterArc((-0.2500000037, 1.3000000194), 0.2500000335, 138.8359483438, 0.3867009203)
                CenterArc((-0.4660442051, 1.4876105054), 0.0361454561, -39.6332738974, 199.5877436616)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_41912_72d5af56_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3075687168, perimeter: 5.5498876633
            with BuildLine():
                Line((0, 0), (1.2869770424, 0))
                Line((0.6434885212, 2.0320000648), (1.2869770424, 0))
                Line((0.6434885212, 2.0320000648), (0, 0))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254)
    return part.part


def model_41912_7334aba9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5339188038, perimeter: 18.5013478094
            with BuildLine():
                Line((1.7136290379, -7.1377786377), (-0.0023125988, -8.783307505))
                Line((0, 0), (1.7136290379, -7.1377786377))
                Line((-0.0023125988, -8.783307505), (0, 0))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_41912_73d5e58c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9651306871, perimeter: 3.8939338973
            with BuildLine():
                Line((-0.2539993656, -0.0005676993), (-0.2539993656, 1.0154323007))
                CenterArc((0.1270006344, 0.053823848), 0.3848628852, -171.8753541576, 163.7507083153)
                Line((0.5080006344, 1.0154323007), (0.5080006344, -0.0005676993))
                Line((-0.2539993656, 1.0154323007), (0.5080006344, 1.0154323007))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254)
    return part.part


def model_41912_a2872c24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.673529747, perimeter: 15.0048964701
            with BuildLine():
                Line((0, 0), (2.2855993805, 1.0176144073))
                Line((3.5593490151, 5.8419727216), (2.2855993805, 1.0176144073))
                Line((-0.2525249861, 2.2873427091), (3.5593490151, 5.8419727216))
                Line((0, 0), (-0.2525249861, 2.2873427091))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_41912_e5724931_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.4523025625, perimeter: 12.4615008199
            with BuildLine():
                Line((0, 0), (0.5065834705, 1.7783750903))
                Line((0, 0), (2.0303734727, -0.5090746139))
                Line((4.824020052, 2.5396556471), (2.0303734727, -0.5090746139))
                Line((0.5065834705, 1.7783750903), (4.824020052, 2.5396556471))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_41912_fd149787_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 80.8073429558, perimeter: 62.762880714
            with BuildLine():
                Line((0, 15.7696273674), (1.7148089969, 8.6326709146))
                Line((1.7148089969, 8.6326709146), (0, 6.9861050303))
                Line((0, 6.9861050303), (0.0012064777, 1.4889192377))
                Line((0, 0.9776128061), (0.0012064777, 1.4889192377))
                Line((0, 0.9776128061), (0, 0))
                Line((9.5472770272, 3.4749246562), (0, 0))
                Line((9.5472770272, 3.4749246562), (12.8126380844, 7.3664304272))
                Line((12.8126380844, 7.3664304272), (7.8066480125, 6.5024492931))
                CenterArc((7.6852589679, 7.2057891322), 0.7137382079, 166.519413443, 113.272767835)
                Line((8.5351546299, 13.6650471144), (6.9911849881, 7.3721728453))
                Line((3.8161849881, 9.416067764), (8.5351546299, 13.6650471144))
                CenterArc((3.0848070882, 10.2283452127), 1.0930271205, -165.5659871745, 117.5659871745)
                Line((2.0262809761, 9.9558919945), (0, 17.3545311952))
                Line((0, 17.3545311952), (0, 15.7696273674))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_41917_f0c40fa1_0000():
    """Model: Back Wheel Pin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_41917_f0c40fa1_0002():
    """Model: Front Wheel Rubber v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_41917_f0c40fa1_0003():
    """Model: Back Wheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1884955592, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_41917_f0c40fa1_0006():
    """Model: Front Wheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7775441818, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_41917_f0c40fa1_0007():
    """Model: Wheel Pin v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_41919_d2473a88_0003():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # TwoSides extrude, along=2, against=-10
        extrude(amount=2)
        extrude(sk.sketch, amount=-10)
    return part.part


def model_41924_ac7400c0_0004():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.4787217752), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((-0.0454054745, 0.4006067619), (0.1313712208, 0.2238300666))
                Line((-0.2221821698, 0.2238300666), (-0.0454054745, 0.4006067619))
                Line((-0.0454054745, 0.0470533713), (-0.2221821698, 0.2238300666))
                Line((0.1313712208, 0.2238300666), (-0.0454054745, 0.0470533713))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_41941_79d46bb4_0001():
    """Model: game board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1451.609956398, perimeter: 152.3999977112
            with BuildLine():
                Line((12.6999998093, -12.6999998093), (-25.3999996185, -12.6999998093))
                Line((12.6999998093, 25.3999996185), (12.6999998093, -12.6999998093))
                Line((-25.3999996185, 25.3999996185), (12.6999998093, 25.3999996185))
                Line((-25.3999996185, -12.6999998093), (-25.3999996185, 25.3999996185))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_41941_79d46bb4_0005():
    """Model: iron handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7767801704, perimeter: 6.826341442
            with BuildLine():
                Line((-12.7812263207, 0.254), (-12.7812263207, 0.8831969113))
                Line((-12.7812263207, 0.254), (-12.5732833166, 0.254))
                Line((-12.5730004013, 1.1430000365), (-12.5732833166, 0.254))
                Line((-14.4678751312, 1.1430000365), (-12.5730004013, 1.1430000365))
                Line((-14.4678751312, 0.254), (-14.4678751312, 1.1430000365))
                Line((-14.4678751312, 0.254), (-14.2235196806, 0.254))
                Line((-14.2240004539, 0.8831969113), (-14.2235196806, 0.254))
                Line((-12.7812263207, 0.8831969113), (-14.2240004539, 0.8831969113))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


def model_41941_79d46bb4_0006():
    """Model: M"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.6817607889, perimeter: 38.8684870731
            with BuildLine():
                Line((3.7752132024, -2.5399999619), (4.826000154, -7.6200002432))
                Line((3.7752132024, -2.5399999619), (2.5399999619, -2.5399999619))
                Line((3.8099999428, -10.1599998474), (2.5399999619, -2.5399999619))
                Line((3.8099999428, -10.1599998474), (5.0799999237, -10.1599998474))
                Line((6.3499999046, -8.8899998665), (5.0799999237, -10.1599998474))
                Line((7.6199998856, -10.1599998474), (6.3499999046, -8.8899998665))
                Line((7.6199998856, -10.1599998474), (8.8899998665, -10.1599998474))
                Line((10.1599998474, -2.5399999619), (8.8899998665, -10.1599998474))
                Line((10.1599998474, -2.5399999619), (8.7645803585, -2.5399999619))
                Line((7.8740002513, -7.6200002432), (8.7645803585, -2.5399999619))
                Line((6.3500002027, -6.0960001945), (7.8740002513, -7.6200002432))
                Line((4.826000154, -7.6200002432), (6.3500002027, -6.0960001945))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


def model_41941_79d46bb4_0008():
    """Model: dog"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.169844775, perimeter: 13.6158486359
            with BuildLine():
                Line((1.5240000486, 3.3020001054), (1.3970000446, 2.5400000811))
                Line((1.3970000446, 2.5400000811), (1.3970000446, 2.1590000689))
                Line((2.1625567559, 2.1590000689), (1.3970000446, 2.1590000689))
                Line((2.1625567559, 2.5922009803), (2.1625567559, 2.1590000689))
                Line((2.413000077, 2.7940000892), (2.1625567559, 2.5922009803))
                Line((3.363472814, 2.7940000892), (2.413000077, 2.7940000892))
                Line((3.363472814, 2.7940000892), (3.5560001135, 2.6670000851))
                Line((3.5560001135, 2.1376826181), (3.5560001135, 2.6670000851))
                Line((4.2303273213, 2.1376826181), (3.5560001135, 2.1376826181))
                Line((4.2303273213, 3.3401506847), (4.2303273213, 2.1376826181))
                Line((4.344992909, 3.7157793341), (4.2303273213, 3.3401506847))
                Line((4.5907095923, 3.7790042769), (4.344992909, 3.7157793341))
                Line((4.7978257842, 3.7157793341), (4.5907095923, 3.7790042769))
                Line((4.9089850436, 3.5476894522), (4.7978257842, 3.7157793341))
                Line((5.0692844372, 4.0728081551), (4.9089850436, 3.5476894522))
                Line((4.9612444757, 4.2284237362), (5.0692844372, 4.0728081551))
                Line((4.3317270758, 4.4205922056), (4.9612444757, 4.2284237362))
                Line((4.0636273733, 4.826000154), (4.3317270758, 4.4205922056))
                Line((4.0636273733, 4.4205922056), (4.0636273733, 4.826000154))
                Line((3.6817884032, 3.7544050662), (4.0636273733, 4.4205922056))
                Line((3.1555769806, 3.5864652505), (3.6817884032, 3.7544050662))
                Line((1.6440841592, 3.662252437), (3.1555769806, 3.5864652505))
                Line((1.3970000446, 4.0225047686), (1.6440841592, 3.662252437))
                Line((1.5240000486, 3.3020001054), (1.3970000446, 4.0225047686))
            make_face()
        # OneSide extrude, distance=1.397
        extrude(amount=1.397)
    return part.part


def model_41942_29c07f06_0005():
    """Model: bike seat"""
    with BuildPart() as part:
        # Sketch6 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.090264773, 0.1193267967, -0.0954129364), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 204.1897904078, perimeter: 69.7446189294
            with BuildLine():
                CenterArc((-94.8373075082, -17.8813054638), 6.8832284383, 16.5560585082, 152.92547066)
                CenterArc((-99.638478703, -16.9898599306), 2, 169.4815291682, 37.5491028167)
                Line((-101.4200060637, -17.8987935162), (-101.0179637872, -18.6868041333))
                Line((-101.0179637872, -18.6868041333), (-101.4515403593, -19.744112747))
                CenterArc((-99.6010857217, -20.5029392318), 2, 157.7026577201, 39.7034245428)
                CenterArc((-94.8373075082, -19.0095062486), 6.9923866981, -162.593917737, 140.7869827131)
                CenterArc((-86.488408178, -22.35), 2, 90, 68.1930649761)
                Line((-76.5, -20.35), (-86.488408178, -20.35))
                CenterArc((-76.5, -18.85), 1.5, -90, 180)
                Line((-76.5, -17.35), (-86.3223653395, -17.35))
                CenterArc((-86.3223653395, -15.35), 2, -163.4439414918, 73.4439414918)
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


def model_41958_acdbb913_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 114.996008687, perimeter: 67.627088707
            with BuildLine():
                Line((7, 80), (1.5000000224, 80))
                Line((2.5, 110), (7, 80))
                Line((0.9000000134, 110), (2.5, 110))
                Line((0.9000000134, 81.20000121), (0.9000000134, 110))
                CenterArc((0.0071428481, 80.0035726126), 1.4928614491, -0.1371164214, 53.4042896625)
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_41970_24ba0c1b_0003():
    """Model: Keychain Loop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3435904707, perimeter: 5.9652426002
            with BuildLine():
                CenterArc((0.6, 0.2500000037), 0.5, -149.9999995071, 299.9999990141)
                Line((0.1669873003, 0.5000000075), (0, 0.5000000075))
                Line((0, 0.5000000075), (0, 0))
                Line((0, 0), (0.1669873003, 0))
            make_face()
            with BuildLine():
                CenterArc((0.6, 0.2500000037), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_41970_24ba0c1b_0004():
    """Model: Corkscrew"""
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
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_41970_24ba0c1b_0005():
    """Model: Scissor Main Blade"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3051129429, perimeter: 23.9783865806
            with BuildLine():
                Line((2.8291796434, 0.5000000075), (0, 0.5000000075))
                CenterArc((0, 0), 0.5000000075, 90, 180)
                Line((0, -0.5000000075), (1.0000000224, -0.5000000075))
                CenterArc((1.0000000224, -0.0000000075), 0.5, -90, 66.4218220807)
                Line((1.3000000194, -0.200000003), (1.4582575938, -0.200000003))
                CenterArc((1.2000000179, -0.200000003), 0.1000000015, 90, 270)
                Line((1.4898979721, -0.1000000015), (1.2000000179, -0.1000000015))
                CenterArc((1.0000000224, -0.0000000075), 0.5, -11.5369583357, 11.5369583357)
                Line((1.5000000224, -0.0000000075), (4.0000000596, -0.0000000075))
                CenterArc((4.5000000596, -0.0000000075), 0.5, 180, 90)
                Line((8.0000001267, -0.5000000075), (4.5000000596, -0.5000000075))
                CenterArc((8.0000001267, -0.0000000075), 0.5, -90, 90)
                Line((4.5000000671, 0.0000000075), (8.5000001267, -0.0000000075))
                CenterArc((4.0000000671, 0.0000000075), 0.5, 0, 75.3364155717)
                CenterArc((4.1772002549, 0.6772001946), 0.2, -165.3364159484, 60.6728315201)
                CenterArc((3.5000000522, 0.5000000075), 0.5000000149, 14.6635840516, 148.734866713)
                CenterArc((2.8291796434, 0.7000000075), 0.2, -90, 73.3984507646)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3000000641, -0.1000000015), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_41973_0e5cd44c_0008():
    """Model: Support rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.1180410861, perimeter: 15.1682507323
            with BuildLine():
                Line((10.7102758844, 6.8082682726), (12, 6.8082682726))
                Line((10.7102758844, 0.513867022), (10.7102758844, 6.8082682726))
                Line((12, 0.513867022), (10.7102758844, 0.513867022))
                Line((12, 6.8082682726), (12, 0.513867022))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_41973_0e5cd44c_0010():
    """Model: Circuit board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0997826681, 0.0198798385, 0), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 49.4728660985, perimeter: 37.2069891892
            with BuildLine():
                Line((1, 6), (8.9000001326, 6))
                Line((1, -0.5000000075), (1, 6))
                Line((8.9000001326, -0.5000000075), (1, -0.5000000075))
                Line((8.9000001326, 6), (8.9000001326, -0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((3.4249361885, 2.9801201615), 0.4683685249, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.508783578, 2.9801201615), 0.4347582296, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.9002173319, 2.9801201615), 0.4348870868, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_41978_2d035a32_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0005067075, perimeter: 0.0797964534
            Circle(0.0127)
        # OneSide extrude, distance=83
        extrude(amount=83)
    return part.part


def model_41978_48e2a5bb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0011400918, perimeter: 0.1196946801
            Circle(0.01905)
        # OneSide extrude, distance=83
        extrude(amount=83)
    return part.part


def model_41978_9d21376f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.012667687, perimeter: 0.398982267
            Circle(0.0635)
        # OneSide extrude, distance=82.5
        extrude(amount=82.5)
    return part.part


def model_41978_b9f032be_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 9
            with BuildLine():
                Line((0.5, -4), (0, -4))
                Line((0.5, 0), (0.5, -4))
                Line((0, 0), (0.5, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_41982_f75ceb8f_0008():
    """Model: chest holders v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((-1.0000000149, 1.5000000224), (0, 1.5))
                Line((-5, 1.5), (-1.0000000149, 1.5000000224))
                Line((-5, 0.5), (-5, 1.5))
                Line((-1.0000704922, 0.500000005), (-5, 0.5))
                Line((0, 0.5), (-1.0000704922, 0.500000005))
                Line((0, 1.5), (0, 0.5))
            make_face()
            # Profile area: 0.2146018653, perimeter: 3.5707964024
            with BuildLine():
                Line((0, 1.5), (0, 2.5000000373))
                CenterArc((-1.0000000149, 2.5000000373), 1.0000000149, -90, 90)
                Line((-1.0000000149, 1.5000000224), (0, 1.5))
            make_face()
            # Profile area: 0.2146018355, perimeter: 3.5709373272
            with BuildLine():
                CenterArc((-1.0000000149, -0.5000000075), 1.0000000149, 0, 90.0040380534)
                Line((0, 0.5), (0, -0.5000000075))
                Line((0, 0.5), (-1.0000704922, 0.500000005))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_41986_26275a06_0000():
    """Model: Lamp 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.7162924857, -0.2379967173), x_dir=(1, 0, 0), z_dir=(0, -0.996183484, 0.0872838254))):
            # Profile area: 0.3816015946, perimeter: 2.9065044847
            with BuildLine():
                CenterArc((0, 3.2504019282), 0.3625845559, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 3.2504019282), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_41986_26275a06_0001():
    """Model: Magazine"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2, perimeter: 4.4
            with BuildLine():
                Line((-4, 2.1), (-4, 0.9))
                Line((-4, 0.9), (-3, 0.9))
                Line((-3, 0.9), (-3, 2.1))
                Line((-3, 2.1), (-4, 2.1))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_41986_26275a06_0009():
    """Model: Tabletop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75.1038035934, perimeter: 31.6872635817
            Ellipse(6, 3.984380529)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_41998_654ac923_0006():
    """Model: Clamp Piece v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2864593742, perimeter: 18.0000369885
            with BuildLine():
                Line((-1.9997852576, -0.0293073969), (-3.24980912, -0.0293073969))
                CenterArc((0, 0), 2, -0.8396251249, 181.6792502499)
                Line((1.9997852576, -0.0293073969), (3.24980912, -0.0293073969))
                Line((3.24980912, -0.0293073969), (3.24980912, 0.2706926031))
                Line((3.24980912, 0.2706926031), (2.23365743, 0.2706926031))
                CenterArc((0, 0), 2.25, 6.9098682812, 166.1802634375)
                Line((-3.24980912, 0.2706926031), (-2.23365743, 0.2706926031))
                Line((-3.24980912, -0.0293073969), (-3.24980912, 0.2706926031))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_41998_654ac923_0008():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # Symmetric extrude, each_side=70
        extrude(amount=70, both=True)
    return part.part


def model_42004_549eeccf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0410433058, perimeter: 0.7181680806
            with Locations((-1.2700000405, 1.2700000405)):
                Circle(0.1143)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


def model_42005_128e5c59_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.9999997318, perimeter: 25.0000001267
            with BuildLine():
                Line((1.0000000149, 0.5000000075), (1.0000000149, 0.0000000075))
                Line((1.0000000149, 0.0000000075), (2.5000000075, 0.0000000075))
                Line((2.5000000075, 0.0000000075), (2.5, 3))
                Line((2.5, 3), (-2.5, 3))
                Line((-2.5, 3), (-2.5, 0))
                Line((-2.5, 0), (-1.0000000149, 0))
                Line((-1.0000000149, 0), (-1.0000000149, 0.5000000075))
                Line((-1.0000000149, 0.5000000075), (-2.0000000298, 0.5000000075))
                Line((-2.0000000298, 0.5000000075), (-2.0000000298, 2.5000000373))
                Line((-2.0000000298, 2.5000000373), (2.0000000298, 2.5000000373))
                Line((2.0000000298, 2.5000000373), (2.0000000298, 0.5000000075))
                Line((2.0000000298, 0.5000000075), (1.0000000149, 0.5000000075))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)
    return part.part


def model_42005_166cd78a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.4238884172, perimeter: 38.6512694142
            with BuildLine():
                Line((-5.0000000801, 4.8872984112), (-5.0000000328, 1.9999999672))
                CenterArc((-5.1000000801, 4.8872984096), 0.1, 0.0000009392, 104.4775109735)
                CenterArc((-5.000000082, 4.5000000745), 0.5, 104.4775119126, 75.5224880874)
                Line((-5.500000082, 1.9999999925), (-5.500000082, 4.5000000745))
                CenterArc((-3.000000082, 1.9999999925), 2.5, -180, 90)
                Line((3, -0.5000000075), (-3.000000082, -0.5000000075))
                CenterArc((3, 1.9999999925), 2.5, -90, 90)
                Line((5.5, 4.5), (5.5, 1.9999999925))
                CenterArc((5, 4.5), 0.5, 0, 90)
                Line((5, 2), (5, 5))
                CenterArc((3, 2), 2, -90, 90)
                Line((-3.0000000328, 0), (3, 0))
                CenterArc((-3.0000000328, 2), 2, -179.9999990608, 89.9999990608)
            make_face()
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)
    return part.part


def model_42005_bb4162aa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


def model_42013_3c6f187f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.5700377578, perimeter: 7.1400755155
            with BuildLine():
                Line((-0.999241143, -1), (0.999241143, -1))
                Line((0.9999997118, -0.000759145), (0.999241143, -1))
                CenterArc((0, 0), 1, -0.0434958068, 180.0869916135)
                Line((-0.999241143, -1), (-0.9999997118, -0.000759145))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_42013_6092fa24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            Circle(0.3000000045)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_42013_b9cc3868_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0503311748, perimeter: 64.4026493986
            with BuildLine():
                CenterArc((0, 0), 5.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_42143_51b31600_0005():
    """Model: Number Pad"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 242.43048288, perimeter: 62.2808
            with BuildLine():
                Line((-33.4050663841, 4.2494757704), (-33.4050663841, -11.2953242296))
                Line((-33.4050663841, -11.2953242296), (-17.8094663841, -11.2953242296))
                Line((-17.8094663841, -11.2953242296), (-17.8094663841, 4.2494757704))
                Line((-17.8094663841, 4.2494757704), (-33.4050663841, 4.2494757704))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508)
    return part.part


def model_42143_51b31600_0008():
    """Model: End Cap (Key Cylinder)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((0.6895256056, 0.6571948357)):
                Circle(1.27)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


def model_42329_df7f540f_0021():
    """Model: Main Arm plate 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2011001677, perimeter: 14.1057121357
            with BuildLine():
                Line((0, 0.2758), (3.611, 0.2758))
                CenterArc((0, 0), 0.2758, 90, 180)
                Line((0, -0.2758), (5, -0.2758))
                CenterArc((5, 0), 0.2758, -90, 176.0888126675)
                CenterArc((5.813518904, 3.5422841844), 3.3623911534, -121.343448545, 17.6721396323)
                CenterArc((3.960573244, 0.4999235731), 0.1998224432, 58.656551455, 118.481683446)
                Line((3.761, 0.4899471461), (3.761, 0.5099))
                Line((3.761, 0.4258), (3.761, 0.4899471461))
                CenterArc((3.611, 0.4258), 0.15, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((3.5, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.960573244, 0.4999235731), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_42329_df7f540f_0058():
    """Model: Main Arm plate 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3413434656, perimeter: 14.1092159742
            with BuildLine():
                Line((1.3864254832, 0.699516111), (3.5530025398, 0.3174901202))
                CenterArc((1.2996013944, 0.2071122345), 0.5, 80, 30.0243024164)
                Line((-0.0719761858, 0.2394147629), (1.1283920494, 0.6768859675))
                CenterArc((0, 0), 0.25, 106.7325575595, 163.2674424405)
                Line((0, -0.25), (1, -0.25))
                CenterArc((1, -0.05), 0.2, -90, 72.4008244233)
                Line((1.1906390037, -0.1104712351), (1.1966569559, -0.0864148553))
                Line((1.1966569559, -0.0864148553), (1.2373141445, 0.0761096598))
                CenterArc((1.3841945811, 0.038160433), 0.1517036799, 80.5916655128, 84.9217308367)
                Line((1.4089935015, 0.1878234546), (3.8398760219, -0.2408067207))
                CenterArc((3.9349419801, 0.2500725553), 0.5, -100.9604827874, 10.9713429429)
                Line((5.0087367528, -0.2499274358), (3.9350367528, -0.2499274358))
                CenterArc((5.0087367528, 0.0300725642), 0.28, -90, 159.9979663241)
                Line((4.0248988799, 0.6861300414), (5.1045117319, 0.2931830988))
                CenterArc((3.9548701813, 0.4987908267), 0.2, 69.5039079736, 105.9213234183)
                Line((3.7555073615, 0.4189497041), (3.7555073615, 0.5147428195))
                CenterArc((3.6101956365, 0.4561586086), 0.15, -112.4134444956, 98.0507395411)
            make_face()
            with BuildLine():
                CenterArc((5.0087367528, 0.0300725642), 0.055, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.9548701813, 0.4987908267), 0.055, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -0.05), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_42329_df7f540f_0064():
    """Model: Pin retainer ring (14)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0165998124, perimeter: 1.2789070554
            with BuildLine():
                CenterArc((-0.055, -0.0996), 0.02, -180, 90)
                Line((-0.045, -0.1196), (-0.055, -0.1196))
                CenterArc((-0.045, -0.0996), 0.02, -90, 90)
                Line((-0.025, -0.0996), (-0.025, -0.078))
                CenterArc((-0.0451840683, -0.0780478543), 0.020184125, 0.1358419323, 59.4061165625)
                CenterArc((0, 0), 0.07, -60.0447995899, 300.0895991798)
                CenterArc((0.0451840683, -0.0780478543), 0.020184125, 120.4580415052, 59.4061165625)
                Line((0.025, -0.0996), (0.025, -0.078))
                CenterArc((0.045, -0.0996), 0.02, -180, 90)
                Line((0.055, -0.1196), (0.045, -0.1196))
                CenterArc((0.055, -0.0996), 0.02, -90, 90)
                Line((0.075, -0.0996), (0.075, -0.0733))
                CenterArc((0.095, -0.0733), 0.02, 143.8979189821, 36.1020810179)
                CenterArc((0.095, -0.0733), 0.02, 140.7960375697, 3.1018814124)
                CenterArc((0, 0), 0.1, -37.3428699476, 254.6857398952)
                CenterArc((-0.095, -0.0733), 0.02, 36.1020810179, 3.1018814124)
                CenterArc((-0.095, -0.0733), 0.02, 0, 36.1020810179)
                Line((-0.075, -0.0996), (-0.075, -0.0733))
            make_face()
            with BuildLine():
                CenterArc((-0.05, -0.0996), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.05, -0.0996), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_42329_df7f540f_0069():
    """Model: Spacer 10mm (7) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0505796417, perimeter: 1.4451326207
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_42329_df7f540f_0073():
    """Model: Dust Seal (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0301592895, perimeter: 1.5079644737
            with BuildLine():
                CenterArc((0, 0), 0.14, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


def model_42329_df7f540f_0074():
    """Model: O-ring Sealant (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0333794219, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_42329_df7f540f_0077():
    """Model: Piston Seal  (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0452389342, perimeter: 2.2619467106
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_42333_53c85dac_0007():
    """Model: float"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0298154605, perimeter: 5.9151632035
            with BuildLine():
                Line((0, 0), (0, 2.1651))
                Line((0, 2.1651), (-0.6250105339, 2.1651))
                Line((-0.6250105339, 2.1651), (-1.2500210678, 1.08255))
                Line((-1.2500210678, 1.08255), (-0.6250105339, 0))
                Line((-0.6250105339, 0), (0, 0))
            make_face()
            # Profile area: 2.0298154605, perimeter: 5.9151632035
            with BuildLine():
                Line((0, 0), (0.6250105339, 0))
                Line((0.6250105339, 0), (1.2500210678, 1.08255))
                Line((1.2500210678, 1.08255), (0.6250105339, 2.1651))
                Line((0.6250105339, 2.1651), (0, 2.1651))
                Line((0, 0), (0, 2.1651))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_42333_53c85dac_0008():
    """Model: Base_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4157889852, perimeter: 8.5369662697
            with BuildLine():
                Line((1.7763, 1.5993), (0.7233, 1.5993))
                CenterArc((0.7233, 1.9993), 0.4, 180, 90)
                Line((0, 1.9993), (0.3233, 1.9993))
                Line((0, 0), (0, 1.9993))
                Line((0, 0), (2.3821778359, 1.4906751685))
                CenterArc((2.0639, 1.9993), 0.6, -57.9632527445, 57.9632527445)
                Line((2.1763, 1.9993), (2.6639, 1.9993))
                CenterArc((1.7763, 1.9993), 0.4, -90, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_42333_53c85dac_0023():
    """Model: pin1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.308624099, perimeter: 2.0685063198
            with BuildLine():
                Line((0.2798, 0), (-0.2102, 0))
                CenterArc((0.0348, -0.245), 0.3464823228, 135, 90)
                Line((0.2798, -0.49), (-0.2102, -0.49))
                CenterArc((0.0348, -0.245), 0.3464823228, -45, 90)
            make_face()
        # OneSide extrude, distance=3.01
        extrude(amount=3.01)
    return part.part


def model_42333_53c85dac_0041():
    """Model: Gear_Small_1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0000990891, perimeter: 0.0455693245
            with BuildLine():
                CenterArc((0, 0), 0.0656, 90, 6.7147001221)
                Line((0, 0.0656), (0, 0.0824))
                Line((-0.0032, 0.0824), (0, 0.0824))
                CenterArc((0.0541, 0.0583465272), 0.0621438618, 157.2282430346, 16.4864239608)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_42333_53c85dac_0044():
    """Model: Ring_1 (1) (1) (1) (1) (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_42429_df14cc7f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.3579070269, perimeter: 39.8902470553
            with BuildLine():
                CenterArc((0, 0), 3.33375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.01498, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.79248
        extrude(amount=0.79248)
    return part.part


def model_42536_905aec30_0016():
    """Model: Nut v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7143702752, perimeter: 8.0558367897
            with BuildLine():
                Line((0.8000000119, -0.4618802222), (0.8000000119, 0.4618802222))
                Line((0.8000000119, 0.4618802222), (0, 0.9237604445))
                Line((0, 0.9237604445), (-0.8000000119, 0.4618802222))
                Line((-0.8000000119, 0.4618802222), (-0.8000000119, -0.4618802222))
                Line((-0.8000000119, -0.4618802222), (0, -0.9237604445))
                Line((0, -0.9237604445), (0.8000000119, -0.4618802222))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_42573_a34062d9_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 110.2503488683, perimeter: 37.2215897597
            with Locations((15, 12.5)):
                Circle(5.924)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_42586_517832f9_0005():
    """Model: WheelBearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3338434887, perimeter: 19.9491133503
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_42586_517832f9_0013():
    """Model: HingePin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0324292787, perimeter: 0.6383716272
            Circle(0.1016)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_42586_517832f9_0019():
    """Model: HingePin2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=1.524
        extrude(amount=1.524)
    return part.part


def model_42586_517832f9_0024():
    """Model: HingePin3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)
    return part.part


def model_42586_517832f9_0026():
    """Model: HandlePin (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107319666, perimeter: 3.191858136
            Circle(0.508)
        # OneSide extrude, distance=1.778
        extrude(amount=1.778)
    return part.part


def model_42601_bfe96b47_0002():
    """Model: Connector v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8544236023, perimeter: 92.3628240155
            with BuildLine():
                CenterArc((0, 0), 7.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 7.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.8
        extrude(amount=7.8)
    return part.part


def model_42601_bfe96b47_0009():
    """Model: Tail Fin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 667.2645372309, perimeter: 123.6357302803
            with BuildLine():
                Line((2.2, 0), (-2.2, 0))
                Line((-21.1433683216, -25.1634984031), (-2.2, 0))
                CenterArc((-18.9735, -26.797), 2.716, 143.0271495342, 151.9651913211)
                CenterArc((0, -67.50000679), 42.192, 65.0076591447, 49.9846817105)
                CenterArc((18.9735, -26.797), 2.716, -114.9923408553, 151.9651913211)
                Line((21.1433683216, -25.1634984031), (2.2, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -12.84), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -3.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_42601_bfe96b47_0010():
    """Model: Stalk Connector v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.626281859, perimeter: 52.0876061965
            with BuildLine():
                CenterArc((0, 0), 4.445, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.845, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=75
        extrude(amount=75)
    return part.part


def model_42811_d7f97f6b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)
    return part.part


def model_43009_6aa4e085_0018():
    """Model: parallel key 1- 5x5x15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6963495408, perimeter: 3.5707963268
            with BuildLine():
                Line((0.75, -0.6774320221), (0.75, -1.6774320221))
                CenterArc((1, -1.6774320221), 0.25, 180, 180)
                Line((1.25, -0.6774320221), (1.25, -1.6774320221))
                CenterArc((1, -0.6774320221), 0.25, 0, 180)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_43009_6aa4e085_0028():
    """Model: washer M8  (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_43010_31eceafd_0004():
    """Model: Handle v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45.4588178557, perimeter: 49.1623100074
            with BuildLine():
                CenterArc((0, -10.044), 15.044, 41.8853011, 96.2293978)
                Line((-7.8, 0), (-11.2, 0))
                CenterArc((0, -8.64), 11.64, 47.9249779492, 84.1500441017)
                Line((7.8, 0), (11.2, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_43301_c87013f5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.0629910246, perimeter: 24.9936492362
            with BuildLine():
                Line((-2.6456184788, 3.8728092774), (-4, 3.5))
                Line((-4, 3.5), (-2.5, 3))
                Line((-2.5, 3), (-2.5, 2))
                Line((-2.5, 2), (-4, 1.5))
                Line((-4, 1.5), (-2.8913259181, 1.1304419727))
                Line((-2.8913259181, 1.1304419727), (-1.7774836251, 1.501722737))
                Line((-1.7774836251, 1.501722737), (-1.5, 2))
                Line((-1.5, 2), (2, 2))
                Line((2, 2), (3.0910688797, 1.3160823549))
                Line((3.0910688797, 1.3160823549), (4, 2))
                Line((4, 2), (2.5455344399, 2.543980274))
                Line((2.5455344399, 2.543980274), (2.5455344399, 3.0000000447))
                Line((2.5455344399, 3.0000000447), (4.0000000596, 3.5000000522))
                Line((4.0000000596, 3.5000000522), (3.0000000447, 4.0000000596))
                Line((3.0000000447, 4.0000000596), (2.0000000298, 3.4000000507))
                Line((2.0000000298, 3.4000000507), (-1.7000000253, 3.4000000507))
                Line((-1.7000000253, 3.4000000507), (-2.6456184788, 3.8728092774))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_43441_e1ab0873_0001():
    """Model: crank end v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_43529_4804941b_0031():
    """Model: Solid27_tubo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_43529_4804941b_0032():
    """Model: Solid31_cilindro plano"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.8298642142, perimeter: 30.1592894745
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 2), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -2), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_43529_4804941b_0046():
    """Model: Solid66_arandela (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2050364021, perimeter: 7.1942471767
            with BuildLine():
                CenterArc((0, 0), 0.74, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.405, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_43529_4804941b_0048():
    """Model: Solid40_pieza U"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.64, perimeter: 35.2
            with BuildLine():
                Line((-3.3, -2.5), (-3.3, 2.1))
                Line((-3.3, 2.1), (3.3, 2.1))
                Line((3.3, -2.5), (3.3, 2.1))
                Line((4, -2.5), (3.3, -2.5))
                Line((4, 2.5), (4, -2.5))
                Line((-4, 2.5), (4, 2.5))
                Line((-4, -2.5), (-4, 2.5))
                Line((-3.3, -2.5), (-4, -2.5))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


def model_43529_4804941b_0049():
    """Model: Solid37_placa cuadrada"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49, perimeter: 28
            with BuildLine():
                Line((-3.5, 3.5), (3.5, 3.5))
                Line((-3.5, -3.5), (-3.5, 3.5))
                Line((3.5, -3.5), (-3.5, -3.5))
                Line((3.5, 3.5), (3.5, -3.5))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_43529_4804941b_0053():
    """Model: Solid38_placa rectangular"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 172.6588505205, perimeter: 121.1898126663
            with BuildLine():
                Line((-8, 6.5), (-6, 8.5))
                Line((-8, -6.5), (-8, 6.5))
                Line((-8, -6.5), (-6, -8.5))
                Line((-6, -8.5), (6, -8.5))
                Line((8, -6.5), (6, -8.5))
                Line((8, -6.5), (8, 6.5))
                Line((8, 6.5), (6, 8.5))
                Line((6, 8.5), (-6, 8.5))
            make_face()
            with BuildLine():
                CenterArc((5.5000174763, -5.8437458921), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.5000174763, -5.8437458921), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5000174763, 5.8437458921), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.5000174763, 5.8437458921), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4, 5), (4, -5))
                Line((4, -5), (-4, -5))
                Line((-4, -5), (-4, 5))
                Line((-4, 5), (4, 5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_43529_4804941b_0054():
    """Model: Solid42_Placa cuadrada esquina chaflan"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 139.115, perimeter: 46.9071067812
            with BuildLine():
                Line((-5.9, -5.9), (5.4, -5.9))
                Line((5.9, -5.4), (5.4, -5.9))
                Line((5.9, 5.9), (5.9, -5.4))
                Line((-5.9, 5.9), (5.9, 5.9))
                Line((-5.9, -5.9), (-5.9, 5.9))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_43562_004c6cea_0018():
    """Model: tube 30x800 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.759291886, perimeter: 17.5929188601
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


def model_43562_004c6cea_0020():
    """Model: leg v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1378455892, perimeter: 5.7409287967
            with BuildLine():
                Line((-1, 0), (-0.525, 0))
                CenterArc((0, 0), 0.525, 0, 180)
                Line((0.525, 0), (1, 0))
                CenterArc((0, 0), 1, 0, 180)
            make_face()
            # Profile area: 24.1792036732, perimeter: 37.1760345073
            with BuildLine():
                Line((-1, 0), (-1, -2))
                Line((-1, -2), (-13.5, -2))
                Line((-13.5, -2), (-13.5, -3))
                Line((1, -4), (-13.5, -3))
                Line((1, 0), (1, -4))
                CenterArc((0, 0), 1, -180, 180)
            make_face()
            # Profile area: 1.1378455892, perimeter: 5.7409287967
            with BuildLine():
                CenterArc((0, 0), 1, -180, 180)
                Line((0.525, 0), (1, 0))
                CenterArc((0, 0), 0.525, -180, 180)
                Line((-1, 0), (-0.525, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_43628_a95b7e66_0011():
    """Model: 02B_rotor (core plate aligner) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


def model_43777_5e0613a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.5093521281, perimeter: 2.529961979
            with Locations((0.5, 2.5)):
                Circle(0.4026559548)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


def model_43866_908e0b9a_0000():
    """Model: blaszka1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_43928_6ca53538_0006():
    """Model: Drag adjustment lever v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.73
        extrude(amount=0.73)
    return part.part


def model_43928_6ca53538_0007():
    """Model: Locking Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 45 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2600483828, perimeter: 10.5501426016
            with BuildLine():
                Line((-2.4504054183, 0.8219), (-1.9154054183, 0.8219))
                CenterArc((-1.9154054183, 0.9219), 0.1, -90, 90)
                Line((-1.8154054183, 1.871), (-1.8154054183, 0.9219))
                CenterArc((-2.0154054183, 1.871), 0.2, 0, 137.1279345896)
                CenterArc((0, 0), 2.95, 137.1279345896, 70.6585347394)
                CenterArc((-2.4904054183, -1.3122903081), 0.135, -152.213530671, 152.213530671)
                CenterArc((-2.2204054183, -1.3122903081), 0.135, -0.0428776508, 180.0428776508)
                Line((-2.0854054561, -1.3123913361), (-2.0854054162, -1.4130760845))
                CenterArc((-1.9504054183, -1.4131), 0.135, 179.9898499663, 180.0101500336)
                Line((-1.8154054183, -0.8531640496), (-1.8154054183, -1.4131))
                CenterArc((-1.9154054183, -0.8531641467), 0.1, 0.0000556387, 71.9999980845)
                Line((-2.2539054183, -0.6380326071), (-1.884503808, -0.7580584661))
                CenterArc((-2.3199054183, -0.3045), 0.34, 90, 191.1931836057)
                Line((-2.3199054183, 0.0355), (-2.2744796051, 0.0355))
                CenterArc((-2.2744795147, 0.1355), 0.1, -90.000051756, 89.999997722)
                Line((-2.1744795147, 0.1354999057), (-2.1744795147, 0.4519))
                CenterArc((-2.2744795147, 0.4519), 0.1, 0, 90)
                Line((-2.4504054183, 0.5519), (-2.2744795147, 0.5519))
                CenterArc((-2.4504054183, 0.6869), 0.135, 90, 180)
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


def model_43928_6ca53538_0017():
    """Model: Winding Assembly Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 33 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30.2970483123, perimeter: 33.6778732465
            with BuildLine():
                CenterArc((0, 0), 3.19, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 2.64), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -1.5), 0.215, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -2.43), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.4, -1.39), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.9, -1.8), 0.09, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7924, 0.1647), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.53, 1.27), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7924, -0.1647), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4, -1.39), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.79, 2.06), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, 2.75), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.125
        extrude(amount=0.125)
    return part.part


def model_43931_bb001c04_0000():
    """Model: Propeler 3 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 16964.6003293849, perimeter: 1130.9733552923
            with BuildLine():
                CenterArc((0, 0), 105, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=76, against=-141
        extrude(amount=76)
        extrude(sk.sketch, amount=-141)
    return part.part


def model_43931_bb001c04_0004():
    """Model: propeler 1 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3472.9577967355, perimeter: 418.4538582729
            with BuildLine():
                CenterArc((0, 0), 41.599, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=17.5
        extrude(amount=17.5, both=True)
    return part.part


def model_43931_bb001c04_0005():
    """Model: ventilator v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3133.9239034003, perimeter: 410.172620038
            with BuildLine():
                CenterArc((0, 0), 40.281, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)
    return part.part


def model_43931_bb001c04_0006():
    """Model: Propeler v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12836.7550062229, perimeter: 896.2649681426
            with BuildLine():
                CenterArc((0, 0), 85.645, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 57, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=22.5
        extrude(amount=22.5, both=True)
    return part.part


def model_43933_3b763a09_0006():
    """Model: 9 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_43934_912ff891_0005():
    """Model: Lower Base Bearing Holder v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0986725877, perimeter: 5.5566370614
            with BuildLine():
                Line((-0.4, 0.375), (-0.9, 0.375))
                Line((-0.9, 0.375), (-0.9, -0.375))
                Line((-0.9, -0.375), (0.9, -0.375))
                Line((0.9, -0.375), (0.9, 0.375))
                Line((0.9, 0.375), (0.4, 0.375))
                CenterArc((0, 0.375), 0.4, 180, 180)
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)
    return part.part


def model_43938_418421a7_0005():
    """Model: shaft2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 15.9105337705, perimeter: 14.1399315427
            Circle(2.25044)
        # TwoSides extrude, along=11.22426, against=-20.77466
        extrude(amount=11.22426)
        extrude(sk.sketch, amount=-20.77466)
    return part.part


def model_43938_418421a7_0007():
    """Model: Key v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.911786499, perimeter: 14.1520555674
            with BuildLine():
                Line((0, 0.20066), (0, 0))
                Line((0, 0), (6.44906, 0))
                Line((6.44906, 0), (6.44906, 0.59944))
                Line((6.44906, 0.59944), (6.31952, 0.72898))
                Line((6.31952, 0.72898), (5.99948, 0.72898))
                Line((5.99948, 0.72898), (5.99948, 0.3302))
                Line((5.99948, 0.3302), (0, 0.20066))
            make_face()
        # Symmetric extrude, each_side=0.59944
        extrude(amount=0.59944, both=True)
    return part.part


def model_44030_17bd5ec9_0001():
    """Model: Рельсы"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 81.5697205131, perimeter: 68.4616457247
            with BuildLine():
                CenterArc((2.7138313773, -0.5065155732), 5.1495805233, 103.6160849671, 12.9866038655)
                Line((1.5015430436, 4.4983357294), (2.4112002811, 4.7771029297))
                Line((2.4112002811, 4.7771029297), (2.2918720731, 7.0709881323))
                CenterArc((0.3814793011, 6.1087177094), 2.1390570142, 26.7345291347, 64.0496505541)
                Line((0.3522039738, 8.2475743819), (-1.2559111559, 8.2489063497))
                Line((-2.8640268372, 8.2489063497), (-1.2559111559, 8.2489063497))
                CenterArc((-2.8950737236, 6.110074659), 2.1390570142, 89.1683634377, 64.0496505541)
                Line((-4.9258969554, 4.7801415105), (-4.8046688123, 7.0739270893))
                Line((-4.0164709269, 4.5006209563), (-4.9258969554, 4.7801415105))
                CenterArc((-5.232904256, -0.5032245171), 5.1495805233, 63.349854294, 12.9866038655)
                CenterArc((-4.7037313061, 2.4944664348), 2.3970909051, 2.7335722465, 39.2935026572)
                Line((-2.1193322867, -1.3713463308), (-2.3093680468, 2.608787867))
                Line((-2.2163440672, -4.7090053541), (-2.1193322867, -1.3713463308))
                CenterArc((-5.5058383347, -4.6133935214), 3.2908834921, -56.6591201914, 54.9942403856)
                Line((-8.6671889485, -8.6234953161), (-3.6971061877, -7.3626483621))
                Line((-8.6671889485, -9.7817151925), (-8.6671889485, -8.6234953161))
                Line((-1.2633783461, -9.7817151925), (-8.6671889485, -9.7817151925))
                Line((-1.2633783461, -9.7817151925), (6.1404297165, -9.7878476104))
                Line((6.1404297165, -9.7878476104), (6.1413890452, -8.6296281313))
                Line((6.1413890452, -8.6296281313), (1.1723523219, -7.3646649965))
                CenterArc((2.9833609974, -4.6169092331), 3.2908834921, -178.3825770676, 54.9942403856)
                Line((-0.306211335, -4.7097964153), (-0.4004585707, -1.3720581841))
                Line((-0.4004585707, -1.3720581841), (-0.2071262158, 2.6079172459))
                CenterArc((2.1871415322, 2.491612653), 2.3970909051, 137.9254682229, 39.2935026572)
            make_face()
        # Symmetric extrude, each_side=50
        extrude(amount=50, both=True)
    return part.part


def model_44104_2333396f_0000():
    """Model: Filament"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 206.119894002, perimeter: 50.8938009882
            Circle(8.1)
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)
    return part.part


def model_44206_ff45fbf0_0007():
    """Model: barra"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_44206_ff45fbf0_0011():
    """Model: V-link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0042411863, perimeter: 0.3666867265
            with BuildLine():
                Line((0, 0), (-0.0839288803, -0.0322172787))
                CenterArc((-0.075185262, -0.0556481027), 0.0250090859, 110.4639318583, 186.8238528378)
                Line((0, -0.045), (-0.0637195942, -0.0778740524))
                Line((0, 0), (0, -0.045))
            make_face()
            with BuildLine():
                CenterArc((-0.0750858446, -0.0553805556), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0042411863, perimeter: 0.3666867265
            with BuildLine():
                Line((0, 0), (0, -0.045))
                Line((0, -0.045), (0.0637195942, -0.0778740524))
                CenterArc((0.075185262, -0.0556481027), 0.0250090859, -117.2877846961, 186.8238528378)
                Line((0, 0), (0.0839288803, -0.0322172787))
            make_face()
            with BuildLine():
                CenterArc((0.0750858446, -0.0553805556), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


def model_44391_f921a9b0_0000():
    """Model: Sklo"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 257.7, perimeter: 346.6
            with BuildLine():
                Line((155, 5), (155, 3.5))
                Line((155, 3.5), (203.1, 3.5))
                Line((203.1, 3.5), (203.1, -69.1))
                Line((203.1, -69.1), (155, -69.1))
                Line((155, -70.6), (155, -69.1))
                Line((204.6, -70.6), (155, -70.6))
                Line((204.6, 5), (204.6, -70.6))
                Line((155, 5), (204.6, 5))
            make_face()
        # OneSide extrude, distance=51.4
        extrude(amount=51.4)
    return part.part


def model_44519_90af0df6_0009():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-71.6461186016, 10.9523851363)):
                Circle(0.75)
        # Symmetric extrude, each_side=14
        extrude(amount=14, both=True)
    return part.part


def model_44519_90af0df6_0010():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1520539662, perimeter: 12.0816512161
            with BuildLine():
                Line((-53.9363386161, 24.3858948137), (-53.9363386161, 25.6141051863))
                Line((-53.9363386161, 25.6141051863), (-55, 26.2282103726))
                Line((-55, 26.2282103726), (-56.0636613839, 25.6141051863))
                Line((-56.0636613839, 25.6141051863), (-56.0636613839, 24.3858948137))
                Line((-56.0636613839, 24.3858948137), (-55, 23.7717896274))
                Line((-55, 23.7717896274), (-53.9363386161, 24.3858948137))
            make_face()
            with BuildLine():
                CenterArc((-55, 25), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_44519_90af0df6_0011():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3744421982, perimeter: 10.9955696999
            with BuildLine():
                CenterArc((-50, 25), 0.9999992698, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-50, 25), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)
    return part.part


def model_44519_90af0df6_0013():
    """Model: Component22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.6458333333, perimeter: 30.0057549589
            with BuildLine():
                Line((25, -96), (25, -100))
                Line((25, -100), (30, -100))
                Line((30, -100), (30, -96))
                Line((30, -96), (25, -96))
            make_face()
            with BuildLine():
                Line((29, -97), (27.75, -97.4166666667))
                Line((26.5, -99.5), (29, -97))
                Line((28, -97.5), (26.5, -99.5))
                Line((26.5, -98), (28, -97.5))
                Line((28, -96.5), (26.5, -98))
                Line((27.75, -97.4166666667), (28, -96.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((30, -100), (30, -96))
                CenterArc((30, -98), 2, -90, 180)
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((25, -98), 2, 90, 180)
                Line((25, -96), (25, -100))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_44519_90af0df6_0015():
    """Model: Component21"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3633685403, perimeter: 5.9773716601
            with BuildLine():
                Line((-39.5000001584, 49.7113259503), (-39.5000010188, 50.2886755398))
                Line((-39.5000010188, 50.2886755398), (-40.0000008603, 50.5773495895))
                Line((-40.0000008603, 50.5773495895), (-40.4999998416, 50.2886740497))
                Line((-40.4999998416, 50.2886740497), (-40.4999989812, 49.7113244602))
                Line((-40.4999989812, 49.7113244602), (-39.9999991397, 49.4226504105))
                Line((-39.9999991397, 49.4226504105), (-39.5000001584, 49.7113259503))
            make_face()
            with BuildLine():
                CenterArc((-40, 50), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_44522_a7c79550_0000():
    """Model: Component28"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.9255565338, perimeter: 37.5797503433
            with BuildLine():
                CenterArc((0, 0), 0.4472136022, 89.3624432973, 181.2751134054)
                Line((0.0049762504, -0.4471859154), (15.5, -0.4471859154))
                CenterArc((15.5, 0), 0.4471859154, -90, 180)
                Line((0.0049762504, 0.4471859154), (15.5, 0.4471859154))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((15.5, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_44522_a7c79550_0001():
    """Model: Component27"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.5, perimeter: 25
            with BuildLine():
                Line((12.5, 12.5), (7.5, 12.5))
                Line((12.5, 20), (12.5, 12.5))
                Line((7.5, 20), (12.5, 20))
                Line((7.5, 12.5), (7.5, 20))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_44522_a7c79550_0002():
    """Model: Component30"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=21.7
        extrude(amount=21.7)
    return part.part


def model_44522_a7c79550_0003():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0.7000000104, 1.0000000149), 0.5, -158.8975456955, 137.795091391)
                CenterArc((0.7000000104, 1.0000000149), 0.5, -21.1024543045, 222.204908609)
            make_face()
        # OneSide extrude, distance=-29
        extrude(amount=-29)
    return part.part


def model_44522_a7c79550_0006():
    """Model: Component32"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0664604382, perimeter: 20.9684642776
            with BuildLine():
                CenterArc((7.5, 12.5), 0.35, 88.1614270499, 183.6771459003)
                Line((7.5112292756, 12.1501801844), (15.0000002235, 12.1501801844))
                CenterArc((15.0000002235, 12.5), 0.3498198156, -90, 180)
                Line((7.5112292756, 12.8498198156), (15.0000002235, 12.8498198156))
            make_face()
            with BuildLine():
                CenterArc((15.0000002235, 12.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.5, 12.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


def model_44533_35550b4f_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.5907007373, -2.701487282)):
                Circle(0.2)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True)
    return part.part


def model_44741_f386a08f_0002():
    """Model: Roll_mot_shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.3534291735, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=2, against=-0.1
        extrude(amount=2)
        extrude(sk.sketch, amount=-0.1)
    return part.part


def model_44920_70dd4b80_0002():
    """Model: woodAccent"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9500765233, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)
    return part.part


def model_44996_b3e9c266_0001():
    """Model: Dowel Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0670751144, perimeter: 7.9796455948
            Circle(1.2700000405)
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


def model_44996_b3e9c266_0002():
    """Model: Short 2x4 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 261.2898, perimeter: 144.78
            with BuildLine():
                Line((68.58, -3.81), (0, -3.81))
                Line((68.58, 0), (68.58, -3.81))
                Line((0, 0), (68.58, 0))
                Line((0, -3.81), (0, 0))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


def model_44996_b3e9c266_0006():
    """Model: 1ftx2inx4in v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 145.161, perimeter: 83.82
            with BuildLine():
                Line((38.1, -3.81), (0, -3.81))
                Line((38.1, 0), (38.1, -3.81))
                Line((0, 0), (38.1, 0))
                Line((0, -3.81), (0, 0))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


def model_44996_b3e9c266_0009():
    """Model: 15"x1"x3" v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72.5805, perimeter: 80.01
            with BuildLine():
                Line((38.1, -1.905), (0, -1.905))
                Line((38.1, 0), (38.1, -1.905))
                Line((0, 0), (38.1, 0))
                Line((0, -1.905), (0, 0))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_44996_b3e9c266_0010():
    """Model: Top Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2348.3824, perimeter: 203.2
            with BuildLine():
                Line((35.56, -66.04), (0, -66.04))
                Line((35.56, 0), (35.56, -66.04))
                Line((0, 0), (35.56, 0))
                Line((0, -66.04), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_44996_b3e9c266_0012():
    """Model: 2ftx1inx3in v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 116.1288, perimeter: 125.73
            with BuildLine():
                Line((60.96, -1.905), (0, -1.905))
                Line((60.96, 0), (60.96, -1.905))
                Line((0, 0), (60.96, 0))
                Line((0, -1.905), (0, 0))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_44996_b3e9c266_0013():
    """Model: 1ftx1inx3in v0 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.0644, perimeter: 64.77
            with BuildLine():
                Line((30.48, -1.905), (0, -1.905))
                Line((30.48, 0), (30.48, -1.905))
                Line((0, 0), (30.48, 0))
                Line((0, -1.905), (0, 0))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_44996_b3e9c266_0016():
    """Model: Base Plate v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1858.0608, perimeter: 182.88
            with BuildLine():
                Line((60.96, -30.48), (0, -30.48))
                Line((60.96, 0), (60.96, -30.48))
                Line((0, 0), (60.96, 0))
                Line((0, -30.48), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_44998_b4e41716_0005():
    """Model: Component25"""
    with BuildPart() as part:
        # Sketch32 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0775, perimeter: 1.75
            with BuildLine():
                Line((-2.4788970953, 0.5104713671), (-2.3788970953, 0.5104713671))
                Line((-2.4788970953, -0.2645286329), (-2.4788970953, 0.5104713671))
                Line((-2.3788970953, -0.2645286329), (-2.4788970953, -0.2645286329))
                Line((-2.3788970953, 0.5104713671), (-2.3788970953, -0.2645286329))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_45007_990d2758_0000():
    """Model: 10. Tornillo 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((12.5, 6)):
                Circle(0.3)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_45007_990d2758_0002():
    """Model: 1. Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_45235_14713966_0003():
    """Model: Head Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1564136928, perimeter: 3.1326867836
            with BuildLine():
                Line((-0.1613116652, -0.2794), (0.1613116652, -0.2794))
                Line((0.1613116652, -0.2794), (0.3226233304, 0))
                Line((0.3226233304, 0), (0.1613116652, 0.2794))
                Line((0.1613116652, 0.2794), (-0.1613116652, 0.2794))
                Line((-0.1613116652, 0.2794), (-0.3226233304, 0))
                Line((-0.3226233304, 0), (-0.1613116652, -0.2794))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


def model_45241_7a955ec1_0007():
    """Model: lead (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0015, perimeter: 0.16
            with BuildLine():
                Line((0.11, -0.015), (0.06, -0.015))
                Line((0.11, 0.015), (0.11, -0.015))
                Line((0.06, 0.015), (0.11, 0.015))
                Line((0.06, -0.015), (0.06, 0.015))
            make_face()
        # OneSide extrude, distance=0.015
        extrude(amount=0.015)
    return part.part


def model_45241_7a955ec1_0011():
    """Model: lead (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.00125, perimeter: 0.15
            with BuildLine():
                Line((0.16, -0.0125), (0.11, -0.0125))
                Line((0.16, 0.0125), (0.16, -0.0125))
                Line((0.11, 0.0125), (0.16, 0.0125))
                Line((0.11, -0.0125), (0.11, 0.0125))
            make_face()
        # OneSide extrude, distance=0.015
        extrude(amount=0.015)
    return part.part


def model_45303_48d14b32_0009():
    """Model: hinge (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.6105082033, perimeter: 16.0221225333
            with BuildLine():
                CenterArc((-25, -25), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-25, -25), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_45303_48d14b32_0014():
    """Model: profile for join arms"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((51.5, -32.5), (50, -32.5))
                Line((51.5, -22.5), (51.5, -32.5))
                Line((50, -22.5), (51.5, -22.5))
                Line((50, -32.5), (50, -22.5))
            make_face()
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((58.5, -32.5), (57, -32.5))
                Line((58.5, -22.5), (58.5, -32.5))
                Line((57, -22.5), (58.5, -22.5))
                Line((57, -32.5), (57, -22.5))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_45307_b9b4bca0_0002():
    """Model: lead"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.00125, perimeter: 0.15
            with BuildLine():
                Line((0.16, -0.0375), (0.11, -0.0375))
                Line((0.16, -0.0125), (0.16, -0.0375))
                Line((0.11, -0.0125), (0.16, -0.0125))
                Line((0.11, -0.0375), (0.11, -0.0125))
            make_face()
        # OneSide extrude, distance=0.015
        extrude(amount=0.015)
    return part.part


def model_45307_b9b4bca0_0003():
    """Model: Component39"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0771725666, perimeter: 1.0884955592
            with BuildLine():
                Line((0.13, -0.125), (-0.13, -0.125))
                CenterArc((0.16, -0.125), 0.03, 90, 90)
                Line((0.16, 0.095), (0.16, -0.095))
                CenterArc((0.16, 0.125), 0.03, 180, 90)
                Line((-0.13, 0.125), (0.13, 0.125))
                CenterArc((-0.16, 0.125), 0.03, -90, 90)
                Line((-0.16, -0.095), (-0.16, 0.095))
                CenterArc((-0.16, -0.125), 0.03, 0, 90)
            make_face()
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


def model_45307_b9b4bca0_0007():
    """Model: Component41"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.06), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0474785398, perimeter: 0.8714159265
            with BuildLine():
                CenterArc((0.12, -0.09), 0.005, -90, 90)
                Line((0.125, -0.09), (0.125, 0.09))
                CenterArc((0.12, 0.09), 0.005, 0, 90)
                Line((0.12, 0.095), (-0.12, 0.095))
                CenterArc((-0.12, 0.09), 0.005, 90, 90)
                Line((-0.125, 0.09), (-0.125, -0.09))
                CenterArc((-0.12, -0.09), 0.005, 180, 90)
                Line((-0.12, -0.095), (0.12, -0.095))
            make_face()
        # TwoSides extrude (symmetric), distance=0.01
        extrude(amount=0.01, both=True)
    return part.part


def model_45307_b9b4bca0_0008():
    """Model: Component46"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on Plane1 construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0016203522, perimeter: 0.2460469607
            with BuildLine():
                Line((0.2112550324, -0.015), (0.2163121119, -0.0728026835))
                Line((0.2312550324, -0.0714953474), (0.2163121119, -0.0728026835))
                Line((0.2312550324, -0.0714953474), (0.225, 0))
                Line((0.225, 0), (0.175, 0))
                Line((0.175, -0.015), (0.175, 0))
                Line((0.175, -0.015), (0.2112550324, -0.015))
            make_face()
        # OneSide extrude, distance=0.055
        extrude(amount=0.055)
    return part.part


def model_45331_7b9dc63f_0000():
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
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 63.926502179, perimeter: 41.3293316208
            with BuildLine():
                Line((-10, 0), (8, 0))
                Line((8, 0), (8, 3))
                _nurbs_edge([(-10, 1.5), (-9.8225904968, 1.6182730022), (-9.4581343108, 1.833901913), (-8.8825398859, 2.0946033398), (-8.0600114225, 2.3310219731), (-6.9557624447, 2.5193689481), (-5.7951806476, 2.6914181188), (-4.5980261348, 2.9251893256), (-3.3791734756, 3.2519296258), (-2.1472427145, 3.6504059051), (-0.9066803894, 4.0690165987), (0.3411436541, 4.4396324648), (1.5965652184, 4.6931006928), (2.8602643458, 4.7763024918), (4.1323735561, 4.661520385), (5.4128309751, 4.3364249048), (6.4437200972, 3.9065367684), (7.2204750341, 3.4897127233), (7.7398945212, 3.1701795436), (8, 3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-10, 0), (-10, 1.5))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9)
    return part.part


def model_45359_1768ab3f_0016():
    """Model: Linkage Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


def model_45359_1768ab3f_0030():
    """Model: Piston Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=8.4
        extrude(amount=8.4)
    return part.part


def model_45359_1768ab3f_0035():
    """Model: Piston Suport Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=10.5
        extrude(amount=10.5)
    return part.part


def model_45359_1768ab3f_0036():
    """Model: Beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3231456506, perimeter: 8.733627577
            with BuildLine():
                CenterArc((0, 0), 1.19, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_45359_1768ab3f_0045():
    """Model: Eccentric Strap Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=16
        extrude(amount=16)
    return part.part


def model_45360_cb4bac3f_0002():
    """Model: Brazo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 172.9001655874, perimeter: 111.1393797974
            with BuildLine():
                CenterArc((-23.25, 0), 1.75, 180, 90)
                Line((25, -1.75), (-23.25, -1.75))
                Line((25, 0), (25, -1.75))
                Line((25, 0), (22.5, 0))
                CenterArc((22, 0), 0.5, 0, 360)
                Line((25, 1.75), (25, 0))
                Line((-23.25, 1.75), (25, 1.75))
                CenterArc((-23.25, 0), 1.75, 90, 90)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_45360_cb4bac3f_0003():
    """Model: Lamina superior"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 69.780702757, perimeter: 52.0032698797
            with BuildLine():
                Line((-4.4998182986, -2.5), (-2.8636182986, -2.5))
                CenterArc((-3.6819354947, 47.4933031212), 50, -89.0622356995, 13.1636356839)
                Line((8.5, 2), (8.5, -1))
                CenterArc((8, 2), 0.5, 0, 90)
                Line((8, 2.5), (-6.5, 2.5))
                CenterArc((-6.5, 0.5), 2, 90, 180)
                CenterArc((-6.2414505997, -3.48321764), 2, 29.4463795994, 67.9813024346)
            make_face()
            with BuildLine():
                CenterArc((7.2999834901, 1.499957313), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2, 0.5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.5, 0.5), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_45360_cb4bac3f_0014():
    """Model: Lamina fija"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.0979705148, perimeter: 35.4627960133
            with BuildLine():
                Line((-6, 1.55), (6, 1.55))
                Line((-6, -1.55), (-6, 1.55))
                Line((6, -1.55), (-6, -1.55))
                Line((6, 1.55), (6, -1.55))
            make_face()
            with BuildLine():
                CenterArc((-2.7499735429, -0.3000606262), 0.4188, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7499735429, -0.3000606262), 0.4188, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_45360_cb4bac3f_0017():
    """Model: arandela articulacion (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0159289474, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_45360_cb4bac3f_0023():
    """Model: arandela torno eje (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5945792559, perimeter: 12.252211349
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_45419_9ab20637_0000():
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
        # OneSide extrude, distance=-25.4
        extrude(amount=-25.4)
    return part.part


def model_45466_5f662bcb_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Tile -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 929.0304, perimeter: 121.92
            with BuildLine():
                Line((15.24, -15.24), (-15.24, -15.24))
                Line((15.24, 15.24), (15.24, -15.24))
                Line((-15.24, 15.24), (15.24, 15.24))
                Line((-15.24, -15.24), (-15.24, 15.24))
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


def model_45468_eaf0dc99_0005():
    """Model: Figure v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


def model_45546_26041647_0001():
    """Model: wheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 60.3831787285, perimeter: 80.5109049713
            with BuildLine():
                CenterArc((0, 0), 7.1568542495, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.6568542495, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)
    return part.part


def model_45557_957c3482_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4208732399, perimeter: 4.3691667718
            with BuildLine():
                CenterArc((-0.4910024406, -0.0808959944), 0.1290969705, -42.8981337218, 261.5191194761)
                Line((-0.3964305092, -0.168771916), (0.4521783511, -0.168771916))
                CenterArc((0.5498880059, -0.0807277035), 0.1315255107, -38.1984033772, 260.2197840021)
                CenterArc((0.4772344213, 0.086183818), 0.3043144768, -54.6617788497, 62.9121666393)
                CenterArc((0.5491064798, -0.8124487409), 0.9697975601, 76.3238465211, 20.1556023169)
                CenterArc((0.0650986414, -0.4790052843), 0.7330777769, 59.2725821774, 66.9232962473)
                CenterArc((-0.4469175882, -0.088164684), 0.2157760216, 68.4952286173, 22.937320645)
                CenterArc((-0.3919014707, -0.5412166479), 0.6714835061, 95.1616385661, 33.8956195553)
                CenterArc((-0.5401216286, 0.0137500531), 0.2769190967, -173.0415608569, 32.2957754304)
                Line((-0.5918648595, -0.1614739087), (-0.7545528515, -0.1614739087))
            make_face()
            # Profile area: 0.0523578705, perimeter: 0.8111401885
            with BuildLine():
                CenterArc((-0.4910024406, -0.0808959944), 0.1290969705, -42.8981337218, 261.5191194761)
                CenterArc((-0.4910024406, -0.0808959944), 0.1290969705, -141.3790142458, 98.4808805239)
            make_face()
            # Profile area: 0.0543462856, perimeter: 0.8263991565
            with BuildLine():
                CenterArc((0.5498880059, -0.0807277035), 0.1315255107, -137.9786193752, 99.7802159979)
                CenterArc((0.5498880059, -0.0807277035), 0.1315255107, -38.1984033772, 260.2197840021)
            make_face()
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True)
    return part.part


def model_45581_2408ef88_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Grundriss -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 168.7183929684, perimeter: 76.2922345288
            with BuildLine():
                Line((0, 0), (6, 0))
                Line((6, 0), (10.2717451706, 24.2262707241))
                Line((10.2717451706, 24.2262707241), (0, 24.2262707241))
                Line((0, 24.2262707241), (0.125667198, 22.2265395542))
                Line((3.125667198, 22.2265395542), (0.125667198, 22.2265395542))
                Line((0, 4.5), (3.125667198, 22.2265395542))
                Line((0, 0), (0, 4.5))
            make_face()
            with BuildLine():
                CenterArc((0.3, 0.3), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7482701106, 0.3), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3, 4.5), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.4888434296, 4.5), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.1639497464, 14), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9797343003, 14), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.4104984967, 22.114266975), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.9142190928, 23.9262707241), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3637946889, 23.2205284188), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((0.3, 0.3)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((5.7482701106, 0.3)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((0.3, 4.5)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((6.4888434296, 4.5)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((8.1639497464, 14)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((1.9797343003, 14)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((3.4104984967, 22.114266975)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((9.9142190928, 23.9262707241)):
                Circle(0.14)
            # Profile area: 0.061575216, perimeter: 0.879645943
            with Locations((0.3637946889, 23.2205284188)):
                Circle(0.14)
        # OneSide extrude, distance=27
        extrude(amount=27)
    return part.part


def model_45680_5b1610e8_0000():
    """Model: sf40-40-2s-2F"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 91 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0128475343, perimeter: 50.1771209103
            with BuildLine():
                CenterArc((-1.8, 1.8), 0.2, 90, 90)
                Line((-2, 1.8), (-2, 1.3))
                Line((-2, 1.3), (-1.8, 1.3))
                Line((-1.8, 1.3), (-1.8, 1.6))
                Line((-1.8, 1.6), (-1.7, 1.6))
                Line((-1.7, 1.6), (-1.4, 1.3))
                Line((-1.4, 1.0224701299), (-1.4, 1.3))
                Line((-1.3775298701, 1), (-1.4, 1.0224701299))
                Line((-1.4, 0.9775298701), (-1.3775298701, 1))
                Line((-1.4, 0.7), (-1.4, 0.9775298701))
                Line((-1.4, 0.7), (-1.7, 0.4))
                Line((-1.7, 0.4), (-1.8, 0.4))
                Line((-1.8, 0.4), (-1.8, 0.7))
                Line((-1.8, 0.7), (-2, 0.7))
                Line((-2, 0.7), (-2, -0.7))
                Line((-2, -0.7), (-1.8, -0.7))
                Line((-1.8, -0.7), (-1.8, -0.4))
                Line((-1.8, -0.4), (-1.7, -0.4))
                Line((-1.4, -0.7), (-1.7, -0.4))
                Line((-1.4, -0.9775298701), (-1.4, -0.7))
                Line((-1.3775298701, -1), (-1.4, -0.9775298701))
                Line((-1.4, -1.0224701299), (-1.3775298701, -1))
                Line((-1.4, -1.3), (-1.4, -1.0224701299))
                Line((-1.4, -1.3), (-1.7, -1.6))
                Line((-1.7, -1.6), (-1.8, -1.6))
                Line((-1.8, -1.6), (-1.8, -1.3))
                Line((-1.8, -1.3), (-2, -1.3))
                Line((-2, -1.8), (-2, -1.3))
                CenterArc((-1.8, -1.8), 0.2, 180, 90)
                Line((-1.3, -2), (-1.8, -2))
                Line((-1.3, -2), (-1.3, -1.8))
                Line((-1.3, -1.8), (-1.6, -1.8))
                Line((-1.6, -1.8), (-1.6, -1.7))
                Line((-1.3, -1.4), (-1.6, -1.7))
                Line((-1.0224701299, -1.4), (-1.3, -1.4))
                Line((-1, -1.3775298701), (-1.0224701299, -1.4))
                Line((-0.9775298701, -1.4), (-1, -1.3775298701))
                Line((-0.7, -1.4), (-0.9775298701, -1.4))
                Line((-0.7, -1.4), (-0.4, -1.7))
                Line((-0.4, -1.7), (-0.4, -1.8))
                Line((-0.4, -1.8), (-0.7, -1.8))
                Line((-0.7, -1.8), (-0.7, -2))
                Line((-0.7, -2), (0.7, -2))
                Line((0.7, -2), (0.7, -1.8))
                Line((0.7, -1.8), (0.4, -1.8))
                Line((0.4, -1.8), (0.4, -1.7))
                Line((0.7, -1.4), (0.4, -1.7))
                Line((0.9775298701, -1.4), (0.7, -1.4))
                Line((1, -1.3775298701), (0.9775298701, -1.4))
                Line((1.0224701299, -1.4), (1, -1.3775298701))
                Line((1.3, -1.4), (1.0224701299, -1.4))
                Line((1.3, -1.4), (1.6, -1.7))
                Line((1.6, -1.7), (1.6, -1.8))
                Line((1.6, -1.8), (1.3, -1.8))
                Line((1.3, -1.8), (1.3, -2))
                Line((1.8, -2), (1.3, -2))
                CenterArc((1.8, -1.8), 0.2, -90, 90)
                Line((2, 1.8), (2, -1.8))
                CenterArc((1.8, 1.8), 0.2, 0, 90)
                Line((-1.8, 2), (1.8, 2))
            make_face()
            with BuildLine():
                CenterArc((1, 1), 0.4, 20.4873151147, 49.0253697706)
                CenterArc((1.175, 1.4683748499), 0.1, 180, 69.5126848853)
                Line((1.075, 1.7), (1.075, 1.4683748499))
                CenterArc((1.175, 1.7), 0.1, 90, 90)
                Line((1.175, 1.8), (1.7, 1.8))
                CenterArc((1.7, 1.7), 0.1, 0, 90)
                Line((1.8, 1.7), (1.8, 1.175))
                CenterArc((1.7, 1.175), 0.1, -90, 90)
                Line((1.4683748499, 1.075), (1.7, 1.075))
                CenterArc((1.4683748499, 1.175), 0.1, -159.5126848853, 69.5126848853)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.8093285293, -0.9119977827), (0.6, -0.8153846154))
                Line((0.6, -1.3), (0.6, -0.8153846154))
                Line((0.6, -1.3), (0.3, -1.6))
                Line((0.3, -1.6), (0.2, -1.6))
                Line((0.2, -1.6), (0.2, -1.8))
                Line((0.2, -1.8), (-0.2, -1.8))
                Line((-0.2, -1.6), (-0.2, -1.8))
                Line((-0.2, -1.6), (-0.3, -1.6))
                Line((-0.6, -1.3), (-0.3, -1.6))
                Line((-0.6, -0.8451007223), (-0.6, -1.3))
                Line((-0.8041706836, -0.9241654509), (-0.6, -0.8451007223))
                CenterArc((-1, -1), 0.21, 67.4528223324, 313.7159822363)
                Line((-0.9194767537, -0.8060515357), (-0.8339285714, -0.6))
                Line((-1.3, -0.6), (-0.8339285714, -0.6))
                Line((-1.3, -0.6), (-1.6, -0.3))
                Line((-1.6, -0.3), (-1.6, -0.2))
                Line((-1.6, -0.2), (-1.8, -0.2))
                Line((-1.8, 0.2), (-1.8, -0.2))
                Line((-1.6, 0.2), (-1.8, 0.2))
                Line((-1.6, 0.3), (-1.6, 0.2))
                Line((-1.3, 0.6), (-1.6, 0.3))
                Line((-0.8153846154, 0.6), (-1.3, 0.6))
                Line((-0.9119977827, 0.8093285293), (-0.8153846154, 0.6))
                CenterArc((-1, 1), 0.21, -27.2654056457, 322.0405462145)
                Line((-0.8133322607, 0.9037962833), (-0.6, 0.793850363))
                Line((-0.6, 1.7), (-0.6, 0.793850363))
                CenterArc((-0.5, 1.7), 0.1, 90, 90)
                Line((-0.5, 1.8), (0.825, 1.8))
                CenterArc((0.825, 1.7), 0.1, 0, 90)
                Line((0.925, 1.4683748499), (0.925, 1.7))
                CenterArc((0.825, 1.4683748499), 0.1, -69.5126848853, 69.5126848853)
                CenterArc((1, 1), 0.4, 110.4873151147, 94.2878254541)
                Line((0.8093285293, 0.9119977827), (0.6368162462, 0.832376729))
                CenterArc((1, 1), 0.21, -107.1027289691, 311.8778695379)
                Line((0.9382419717, 0.7992864082), (0.8823656605, 0.6176883965))
                CenterArc((1, 1), 0.4, -107.1027289691, 86.6154138543)
                CenterArc((1.4683748499, 0.825), 0.1, 90, 69.5126848853)
                Line((1.7, 0.925), (1.4683748499, 0.925))
                CenterArc((1.7, 0.825), 0.1, 0, 90)
                Line((1.8, 0.825), (1.8, -0.5))
                CenterArc((1.7, -0.5), 0.1, -90, 90)
                Line((0.7714285714, -0.6), (1.7, -0.6))
                Line((0.8958108229, -0.8176689402), (0.7714285714, -0.6))
                CenterArc((1, -1), 0.21, 155.2248594312, 324.5200218658)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.8, -1.6), (1.7, -1.6))
                Line((1.4, -1.3), (1.7, -1.6))
                Line((1.4, -0.85), (1.4, -1.3))
                CenterArc((1.5, -0.85), 0.1, 90, 90)
                Line((1.7, -0.75), (1.5, -0.75))
                CenterArc((1.7, -0.85), 0.1, 0, 90)
                Line((1.8, -0.85), (1.8, -1.6))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.3, 1.4), (-1.6, 1.7))
                Line((-1.6, 1.7), (-1.6, 1.8))
                Line((-1.6, 1.8), (-0.8, 1.8))
                CenterArc((-0.8, 1.7), 0.1, 0, 90)
                Line((-0.7, 1.5), (-0.7, 1.7))
                CenterArc((-0.8, 1.5), 0.1, -90, 90)
                Line((-1.3, 1.4), (-0.8, 1.4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0001():
    """Model: sf20-20-2F"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 48 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9286617881, perimeter: 18.2673887466
            with BuildLine():
                CenterArc((-0.8, 0.8), 0.2, 90, 90)
                Line((-1, 0.8), (-1, 0.3))
                Line((-1, 0.3), (-0.8, 0.3))
                Line((-0.8, 0.3), (-0.8, 0.6))
                Line((-0.8, 0.6), (-0.7, 0.6))
                Line((-0.7, 0.6), (-0.4, 0.3))
                Line((-0.4, 0.0224701299), (-0.4, 0.3))
                Line((-0.3775298701, 0), (-0.4, 0.0224701299))
                Line((-0.4, -0.0224701299), (-0.3775298701, 0))
                Line((-0.4, -0.3), (-0.4, -0.0224701299))
                Line((-0.4, -0.3), (-0.7, -0.6))
                Line((-0.7, -0.6), (-0.8, -0.6))
                Line((-0.8, -0.6), (-0.8, -0.3))
                Line((-0.8, -0.3), (-1, -0.3))
                Line((-1, -0.3), (-1, -0.8))
                CenterArc((-0.8, -0.8), 0.2, 180, 90)
                Line((-0.8, -1), (-0.3, -1))
                Line((-0.3, -1), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.6, -0.8))
                Line((-0.6, -0.8), (-0.6, -0.7))
                Line((-0.3, -0.4), (-0.6, -0.7))
                Line((-0.0224701299, -0.4), (-0.3, -0.4))
                Line((0, -0.3775298701), (-0.0224701299, -0.4))
                Line((0.0224701299, -0.4), (0, -0.3775298701))
                Line((0.0224701299, -0.4), (0.3, -0.4))
                Line((0.3, -0.4), (0.6, -0.7))
                Line((0.6, -0.7), (0.6, -0.8))
                Line((0.6, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, -1))
                Line((0.8, -1), (0.3, -1))
                CenterArc((0.8, -0.8), 0.2, -90, 90)
                Line((1, 0.8), (1, -0.8))
                CenterArc((0.8, 0.8), 0.2, 0, 90)
                Line((-0.8, 1), (0.8, 1))
            make_face()
            with BuildLine():
                Line((0.8, 0.7), (0.8, -0.6))
                Line((0.8, -0.6), (0.7, -0.6))
                Line((0.4, -0.3), (0.7, -0.6))
                Line((0.4, -0.0224701299), (0.4, -0.3))
                Line((0.3775298701, 0), (0.4, -0.0224701299))
                Line((0.4, 0.0224701299), (0.3775298701, 0))
                Line((0.4, 0.2), (0.4, 0.0224701299))
                CenterArc((0.2, 0.2), 0.2, 0, 90)
                Line((0.0224701299, 0.4), (0.2, 0.4))
                Line((0, 0.3775298701), (0.0224701299, 0.4))
                Line((-0.0224701299, 0.4), (0, 0.3775298701))
                Line((-0.3, 0.4), (-0.0224701299, 0.4))
                Line((-0.3, 0.4), (-0.6, 0.7))
                Line((-0.6, 0.7), (-0.6, 0.8))
                Line((-0.6, 0.8), (0.7, 0.8))
                CenterArc((0.7, 0.7), 0.1, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0002():
    """Model: sf20-20-R"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 41 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7354951659, perimeter: 16.9039317066
            with BuildLine():
                CenterArc((0.8, 0.8), 0.2, 0, 90)
                Line((0.3, 1), (0.8, 1))
                CenterArc((0.3, -0.3), 1.3, 90, 90)
                Line((-1, -0.3), (-1, -0.8))
                CenterArc((-0.8, -0.8), 0.2, 180, 90)
                Line((-0.8, -1), (-0.3, -1))
                Line((-0.3, -1), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.6069779884, -0.8))
                Line((-0.6069779884, -0.8), (-0.6069779884, -0.7032979731))
                Line((-0.3004751417, -0.4), (-0.6069779884, -0.7032979731))
                Line((-0.0224701299, -0.4), (-0.3004751417, -0.4))
                Line((0, -0.3775298701), (-0.0224701299, -0.4))
                Line((0.0224701299, -0.4), (0, -0.3775298701))
                Line((0.0224701299, -0.4), (0.2995248583, -0.4))
                Line((0.2995248583, -0.4), (0.6028228314, -0.7032979731))
                Line((0.6028228314, -0.7032979731), (0.6028228314, -0.8))
                Line((0.6028228314, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, -1))
                Line((0.8, -1), (0.3, -1))
                CenterArc((0.8, -0.8), 0.2, -90, 90)
                Line((1, -0.3), (1, -0.8))
                Line((0.8, -0.3), (1, -0.3))
                Line((0.8, -0.3), (0.8, -0.6))
                Line((0.8, -0.6), (0.7, -0.6))
                Line((0.4, -0.3), (0.7, -0.6))
                Line((0.4, -0.0224701299), (0.4, -0.3))
                Line((0.3775298701, 0), (0.4, -0.0224701299))
                Line((0.4, 0.0224701299), (0.3775298701, 0))
                Line((0.4, 0.3), (0.4, 0.0224701299))
                Line((0.4, 0.3), (0.7, 0.6))
                Line((0.7, 0.6), (0.8, 0.6))
                Line((0.8, 0.6), (0.8, 0.3))
                Line((0.8, 0.3), (1, 0.3))
                Line((1, 0.8), (1, 0.3))
            make_face()
            with BuildLine():
                Line((-0.1544943143, 0.0579353679), (-0.3089886286, 0.1158707357))
                CenterArc((0, 0), 0.33, 159.4439547804, 54.1545490804)
                Line((-0.274868778, -0.1826120338), (-0.7, -0.6032979731))
                Line((-0.7, -0.6032979731), (-0.8, -0.6032979731))
                Line((-0.8, -0.6032979731), (-0.8, -0.3))
                CenterArc((0.3, -0.3), 1.1, 90, 90)
                Line((0.3, 0.8), (0.6, 0.8))
                Line((0.6, 0.8), (0.6, 0.7))
                Line((0.1779254264, 0.2779254264), (0.6, 0.7))
                CenterArc((0, 0), 0.33, 57.3729838575, 53.1830613621)
                Line((-0.0579353679, 0.1544943143), (-0.1158707357, 0.3089886286))
                CenterArc((0, 0), 0.165, 159.4439547804, 311.1120904392)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0004():
    """Model: sf20-40-1F"""
    with BuildPart() as part:
        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 78 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.3551396806, perimeter: 32.4895217061
            with BuildLine():
                Line((-1, 2.8), (-1, -0.8))
                CenterArc((-0.8, -0.8), 0.2, 180, 90)
                Line((-0.3, -1), (-0.8, -1))
                Line((-0.3, -1), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.6, -0.8))
                Line((-0.6, -0.8), (-0.6, -0.7))
                Line((-0.3, -0.4), (-0.6, -0.7))
                Line((-0.0224701299, -0.4), (-0.3, -0.4))
                Line((0, -0.3775298701), (-0.0224701299, -0.4))
                Line((0.0224701299, -0.4), (0, -0.3775298701))
                Line((0.3, -0.4), (0.0224701299, -0.4))
                Line((0.3, -0.4), (0.6, -0.7))
                Line((0.6, -0.7), (0.6, -0.8))
                Line((0.6, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, -1))
                Line((0.8, -1), (0.3, -1))
                CenterArc((0.8, -0.8), 0.2, -90, 90)
                Line((1, -0.3), (1, -0.8))
                Line((1, -0.3), (0.8, -0.3))
                Line((0.8, -0.3), (0.8, -0.6))
                Line((0.8, -0.6), (0.7, -0.6))
                Line((0.4, -0.3), (0.7, -0.6))
                Line((0.4, -0.0224701299), (0.4, -0.3))
                Line((0.3775298701, 0), (0.4, -0.0224701299))
                Line((0.4, 0.0224701299), (0.3775298701, 0))
                Line((0.4, 0.3), (0.4, 0.0224701299))
                Line((0.4, 0.3), (0.7, 0.6))
                Line((0.7, 0.6), (0.8, 0.6))
                Line((0.8, 0.6), (0.8, 0.3))
                Line((0.8, 0.3), (1, 0.3))
                Line((1, 0.3), (1, 1.7))
                Line((0.8, 1.7), (1, 1.7))
                Line((0.8, 1.4), (0.8, 1.7))
                Line((0.7, 1.4), (0.8, 1.4))
                Line((0.4, 1.7), (0.7, 1.4))
                Line((0.4, 1.7), (0.4, 1.9775298701))
                Line((0.4, 1.9775298701), (0.3775298701, 2))
                Line((0.3775298701, 2), (0.4, 2.0224701299))
                Line((0.4, 2.0224701299), (0.4, 2.3))
                Line((0.4, 2.3), (0.7, 2.6))
                Line((0.8, 2.6), (0.7, 2.6))
                Line((0.8, 2.3), (0.8, 2.6))
                Line((1, 2.3), (0.8, 2.3))
                Line((1, 2.3), (1, 2.8))
                CenterArc((0.8, 2.8), 0.2, 0, 90)
                Line((0.8, 3), (0.3, 3))
                Line((0.3, 2.8), (0.3, 3))
                Line((0.6, 2.8), (0.3, 2.8))
                Line((0.6, 2.7), (0.6, 2.8))
                Line((0.3, 2.4), (0.6, 2.7))
                Line((0.3, 2.4), (0.0224701299, 2.4))
                Line((0.0224701299, 2.4), (0, 2.3775298701))
                Line((0, 2.3775298701), (-0.0224701299, 2.4))
                Line((-0.0224701299, 2.4), (-0.3, 2.4))
                Line((-0.3, 2.4), (-0.6, 2.7))
                Line((-0.6, 2.8), (-0.6, 2.7))
                Line((-0.3, 2.8), (-0.6, 2.8))
                Line((-0.3, 3), (-0.3, 2.8))
                Line((-0.3, 3), (-0.8, 3))
                CenterArc((-0.8, 2.8), 0.2, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.3, 1.6), (-0.7, 1.6))
                Line((0.3, 1.6), (0.6, 1.3))
                Line((0.6, 1.2), (0.6, 1.3))
                Line((0.6, 1.2), (0.8, 1.2))
                Line((0.8, 1.2), (0.8, 0.8))
                Line((0.8, 0.8), (0.6, 0.8))
                Line((0.6, 0.8), (0.6, 0.7))
                Line((0.3, 0.4), (0.6, 0.7))
                Line((-0.7, 0.4), (0.3, 0.4))
                CenterArc((-0.7, 0.5), 0.1, 180, 90)
                Line((-0.8, 0.5), (-0.8, 1.5))
                CenterArc((-0.7, 1.5), 0.1, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4, 2.3), (-0.4, 1.7))
                Line((-0.4, 1.7), (-0.7, 1.7))
                CenterArc((-0.7, 1.8), 0.1, -180, 90)
                Line((-0.8, 2.6), (-0.8, 1.8))
                Line((-0.7, 2.6), (-0.8, 2.6))
                Line((-0.4, 2.3), (-0.7, 2.6))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4, 0.3), (-0.7, 0.3))
                Line((-0.4, 0.3), (-0.4, -0.3))
                Line((-0.4, -0.3), (-0.7, -0.6))
                Line((-0.7, -0.6), (-0.8, -0.6))
                Line((-0.8, -0.6), (-0.8, 0.2))
                CenterArc((-0.7, 0.2), 0.1, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0005():
    """Model: sf20-20-2H"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 53 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9650998432, perimeter: 19.044677986
            with BuildLine():
                Line((-0.4, -0.3), (-0.7, -0.6))
                Line((-0.7, -0.6), (-0.8, -0.6))
                Line((-0.8, -0.6), (-0.8, -0.3))
                Line((-0.8, -0.3), (-1, -0.3))
                Line((-1, -0.3), (-1, -0.8))
                CenterArc((-0.8, -0.8), 0.2, 180, 90)
                Line((-0.8, -1), (0.8, -1))
                CenterArc((0.8, -0.8), 0.2, -90, 90)
                Line((1, -0.3), (1, -0.8))
                Line((0.8, -0.3), (1, -0.3))
                Line((0.8, -0.3), (0.8, -0.6))
                Line((0.8, -0.6), (0.7, -0.6))
                Line((0.4, -0.3), (0.7, -0.6))
                Line((0.4, -0.0224701299), (0.4, -0.3))
                Line((0.3775298701, 0), (0.4, -0.0224701299))
                Line((0.4, 0.0224701299), (0.3775298701, 0))
                Line((0.4, 0.3), (0.4, 0.0224701299))
                Line((0.4, 0.3), (0.7, 0.6))
                Line((0.7, 0.6), (0.8, 0.6))
                Line((0.8, 0.6), (0.8, 0.3))
                Line((0.8, 0.3), (1, 0.3))
                Line((1, 0.8), (1, 0.3))
                CenterArc((0.8, 0.8), 0.2, 0, 90)
                Line((-0.8, 1), (0.8, 1))
                CenterArc((-0.8, 0.8), 0.2, 90, 90)
                Line((-1, 0.8), (-1, 0.3))
                Line((-1, 0.3), (-0.8, 0.3))
                Line((-0.8, 0.3), (-0.8, 0.6))
                Line((-0.8, 0.6), (-0.7, 0.6))
                Line((-0.7, 0.6), (-0.4, 0.3))
                Line((-0.4, 0.0224701299), (-0.4, 0.3))
                Line((-0.3775298701, 0), (-0.4, 0.0224701299))
                Line((-0.4, -0.0224701299), (-0.3775298701, 0))
                Line((-0.4, -0.3), (-0.4, -0.0224701299))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.3, 0.8), (0.6, 0.8))
                Line((0.6, 0.8), (0.6, 0.7))
                Line((0.3, 0.4), (0.6, 0.7))
                Line((0.0224701299, 0.4), (0.3, 0.4))
                Line((0, 0.3775298701), (0.0224701299, 0.4))
                Line((-0.0224701299, 0.4), (0, 0.3775298701))
                Line((-0.3, 0.4), (-0.0224701299, 0.4))
                Line((-0.3, 0.4), (-0.6, 0.7))
                Line((-0.6, 0.7), (-0.6, 0.8))
                Line((-0.6, 0.8), (-0.3, 0.8))
                Line((-0.3, 0.8), (-0.3, 0.85))
                Line((0.3, 0.85), (-0.3, 0.85))
                Line((0.3, 0.85), (0.3, 0.8))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.0224701299, -0.4), (0.3, -0.4))
                Line((0.3, -0.4), (0.6, -0.7))
                Line((0.6, -0.7), (0.6, -0.8))
                Line((0.6, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, -0.85))
                Line((0.3, -0.85), (-0.3, -0.85))
                Line((-0.3, -0.85), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.6, -0.8))
                Line((-0.6, -0.8), (-0.6, -0.7))
                Line((-0.3, -0.4), (-0.6, -0.7))
                Line((-0.0224701299, -0.4), (-0.3, -0.4))
                Line((0, -0.3775298701), (-0.0224701299, -0.4))
                Line((0.0224701299, -0.4), (0, -0.3775298701))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0006():
    """Model: sf20-20-3F"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0550998432, perimeter: 19.944677986
            with BuildLine():
                Line((-1, 0.8), (-1, -0.8))
                CenterArc((-0.8, -0.8), 0.2, 180, 90)
                Line((-0.8, -1), (0.8, -1))
                CenterArc((0.8, -0.8), 0.2, -90, 90)
                Line((1, -0.8), (1, 0.8))
                CenterArc((0.8, 0.8), 0.2, 0, 90)
                Line((0.3, 1), (0.8, 1))
                Line((0.3, 1), (0.3, 0.8))
                Line((0.3, 0.8), (0.6, 0.8))
                Line((0.6, 0.8), (0.6, 0.7))
                Line((0.3, 0.4), (0.6, 0.7))
                Line((0.0224701299, 0.4), (0.3, 0.4))
                Line((0, 0.3775298701), (0.0224701299, 0.4))
                Line((-0.0224701299, 0.4), (0, 0.3775298701))
                Line((-0.3, 0.4), (-0.0224701299, 0.4))
                Line((-0.3, 0.4), (-0.6, 0.7))
                Line((-0.6, 0.7), (-0.6, 0.8))
                Line((-0.6, 0.8), (-0.3, 0.8))
                Line((-0.3, 0.8), (-0.3, 1))
                Line((-0.8, 1), (-0.3, 1))
                CenterArc((-0.8, 0.8), 0.2, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.4, 0.3), (0.7, 0.6))
                Line((0.7, 0.6), (0.8, 0.6))
                Line((0.8, 0.6), (0.8, 0.3))
                Line((0.8, 0.3), (0.85, 0.3))
                Line((0.85, 0.3), (0.85, -0.3))
                Line((0.8, -0.3), (0.85, -0.3))
                Line((0.8, -0.3), (0.8, -0.6))
                Line((0.8, -0.6), (0.7, -0.6))
                Line((0.4, -0.3), (0.7, -0.6))
                Line((0.4, -0.0224701299), (0.4, -0.3))
                Line((0.3775298701, 0), (0.4, -0.0224701299))
                Line((0.4, 0.0224701299), (0.3775298701, 0))
                Line((0.4, 0.3), (0.4, 0.0224701299))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.8, 0.3), (-0.8, 0.6))
                Line((-0.8, 0.6), (-0.7, 0.6))
                Line((-0.7, 0.6), (-0.4, 0.3))
                Line((-0.4, 0.0224701299), (-0.4, 0.3))
                Line((-0.3775298701, 0), (-0.4, 0.0224701299))
                Line((-0.4, -0.0224701299), (-0.3775298701, 0))
                Line((-0.4, -0.3), (-0.4, -0.0224701299))
                Line((-0.4, -0.3), (-0.7, -0.6))
                Line((-0.7, -0.6), (-0.8, -0.6))
                Line((-0.8, -0.6), (-0.8, -0.3))
                Line((-0.8, -0.3), (-0.85, -0.3))
                Line((-0.85, 0.3), (-0.85, -0.3))
                Line((-0.85, 0.3), (-0.8, 0.3))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.0224701299, -0.4), (0.3, -0.4))
                Line((0.3, -0.4), (0.6, -0.7))
                Line((0.6, -0.7), (0.6, -0.8))
                Line((0.6, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, -0.85))
                Line((0.3, -0.85), (-0.3, -0.85))
                Line((-0.3, -0.85), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.6, -0.8))
                Line((-0.6, -0.8), (-0.6, -0.7))
                Line((-0.3, -0.4), (-0.6, -0.7))
                Line((-0.0224701299, -0.4), (-0.3, -0.4))
                Line((0, -0.3775298701), (-0.0224701299, -0.4))
                Line((0.0224701299, -0.4), (0, -0.3775298701))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0007():
    """Model: sf40-40-2s-1F"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 57 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.1954926972, perimeter: 50.9305981418
            with BuildLine():
                Line((1.8, 1.6), (1.8, 1.3))
                Line((1.8, 1.3), (2, 1.3))
                Line((2, 1.8), (2, 1.3))
                CenterArc((1.8, 1.8), 0.2, 0, 90)
                Line((-1.8, 2), (1.8, 2))
                CenterArc((-1.8, 1.8), 0.2, 90, 90)
                Line((-2, 1.8), (-2, 1.3))
                Line((-2, 1.3), (-1.8, 1.3))
                Line((-1.8, 1.3), (-1.8, 1.6))
                Line((-1.8, 1.6), (-1.7, 1.6))
                Line((-1.7, 1.6), (-1.4, 1.3))
                Line((-1.4, 1.0224701299), (-1.4, 1.3))
                Line((-1.3775298701, 1), (-1.4, 1.0224701299))
                Line((-1.4, 0.9775298701), (-1.3775298701, 1))
                Line((-1.4, 0.7), (-1.4, 0.9775298701))
                Line((-1.4, 0.7), (-1.7, 0.4))
                Line((-1.7, 0.4), (-1.8, 0.4))
                Line((-1.8, 0.4), (-1.8, 0.7))
                Line((-1.8, 0.7), (-2, 0.7))
                Line((-2, 0.7), (-2, -0.7))
                Line((-2, -0.7), (-1.8, -0.7))
                Line((-1.8, -0.7), (-1.8, -0.4))
                Line((-1.8, -0.4), (-1.7, -0.4))
                Line((-1.4, -0.7), (-1.7, -0.4))
                Line((-1.4, -0.9775298701), (-1.4, -0.7))
                Line((-1.3775298701, -1), (-1.4, -0.9775298701))
                Line((-1.4, -1.0224701299), (-1.3775298701, -1))
                Line((-1.4, -1.3), (-1.4, -1.0224701299))
                Line((-1.4, -1.3), (-1.7, -1.6))
                Line((-1.7, -1.6), (-1.8, -1.6))
                Line((-1.8, -1.6), (-1.8, -1.3))
                Line((-1.8, -1.3), (-2, -1.3))
                Line((-2, -1.8), (-2, -1.3))
                CenterArc((-1.8, -1.8), 0.2, 180, 90)
                Line((-1.3, -2), (-1.8, -2))
                Line((-1.3, -2), (-1.3, -1.8))
                Line((-1.3, -1.8), (-1.6, -1.8))
                Line((-1.6, -1.8), (-1.6, -1.7))
                Line((-1.3, -1.4), (-1.6, -1.7))
                Line((-1.0224701299, -1.4), (-1.3, -1.4))
                Line((-1, -1.3775298701), (-1.0224701299, -1.4))
                Line((-0.9775298701, -1.4), (-1, -1.3775298701))
                Line((-0.7, -1.4), (-0.9775298701, -1.4))
                Line((-0.7, -1.4), (-0.4, -1.7))
                Line((-0.4, -1.7), (-0.4, -1.8))
                Line((-0.4, -1.8), (-0.7, -1.8))
                Line((-0.7, -1.8), (-0.7, -2))
                Line((-0.7, -2), (0.7, -2))
                Line((0.7, -2), (0.7, -1.8))
                Line((0.7, -1.8), (0.4, -1.8))
                Line((0.4, -1.8), (0.4, -1.7))
                Line((0.7, -1.4), (0.4, -1.7))
                Line((0.9775298701, -1.4), (0.7, -1.4))
                Line((1, -1.3775298701), (0.9775298701, -1.4))
                Line((1.0224701299, -1.4), (1, -1.3775298701))
                Line((1.3, -1.4), (1.0224701299, -1.4))
                Line((1.3, -1.4), (1.6, -1.7))
                Line((1.6, -1.7), (1.6, -1.8))
                Line((1.6, -1.8), (1.3, -1.8))
                Line((1.3, -1.8), (1.3, -2))
                Line((1.8, -2), (1.3, -2))
                CenterArc((1.8, -1.8), 0.2, -90, 90)
                Line((2, -1.3), (2, -1.8))
                Line((2, -1.3), (1.8, -1.3))
                Line((1.8, -1.3), (1.8, -1.6))
                Line((1.8, -1.6), (1.7, -1.6))
                Line((1.4, -1.3), (1.7, -1.6))
                Line((1.4, -1.0224701299), (1.4, -1.3))
                Line((1.3775298701, -1), (1.4, -1.0224701299))
                Line((1.4, -0.9775298701), (1.3775298701, -1))
                Line((1.4, -0.7), (1.4, -0.9775298701))
                Line((1.4, -0.7), (1.7, -0.4))
                Line((1.7, -0.4), (1.8, -0.4))
                Line((1.8, -0.4), (1.8, -0.7))
                Line((1.8, -0.7), (2, -0.7))
                Line((2, 0.7), (2, -0.7))
                Line((1.8, 0.7), (2, 0.7))
                Line((1.8, 0.7), (1.8, 0.4))
                Line((1.8, 0.4), (1.7, 0.4))
                Line((1.4, 0.7), (1.7, 0.4))
                Line((1.4, 0.9775298701), (1.4, 0.7))
                Line((1.3775298701, 1), (1.4, 0.9775298701))
                Line((1.4, 1.0224701299), (1.3775298701, 1))
                Line((1.4, 1.3), (1.4, 1.0224701299))
                Line((1.7, 1.6), (1.4, 1.3))
                Line((1.7, 1.6), (1.8, 1.6))
            make_face()
            with BuildLine():
                Line((0.7, 1.8), (1.6, 1.8))
                Line((1.6, 1.8), (1.6, 1.7))
                Line((1.3, 1.4), (1.6, 1.7))
                Line((0.8, 1.4), (1.3, 1.4))
                CenterArc((0.8, 1.5), 0.1, 180, 90)
                Line((0.7, 1.5), (0.7, 1.8))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.3, 1.4), (-1.6, 1.7))
                Line((-1.6, 1.7), (-1.6, 1.8))
                Line((-1.6, 1.8), (-0.7, 1.8))
                Line((-0.7, 1.5), (-0.7, 1.8))
                CenterArc((-0.8, 1.5), 0.1, -90, 90)
                Line((-1.3, 1.4), (-0.8, 1.4))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.6, -0.3), (-1.6, -0.2))
                Line((-1.6, -0.2), (-1.8, -0.2))
                Line((-1.8, 0.2), (-1.8, -0.2))
                Line((-1.6, 0.2), (-1.8, 0.2))
                Line((-1.6, 0.3), (-1.6, 0.2))
                Line((-1.3, 0.6), (-1.6, 0.3))
                Line((-0.9, 0.6), (-1.3, 0.6))
                CenterArc((-0.9, 0.9), 0.3, -90, 90)
                Line((-0.6, 1.8), (-0.6, 0.9))
                Line((-0.6, 1.8), (0.6, 1.8))
                Line((0.6, 1.8), (0.6, 0.9))
                CenterArc((0.9, 0.9), 0.3, 180, 90)
                Line((1.3, 0.6), (0.9, 0.6))
                Line((1.3, 0.6), (1.6, 0.3))
                Line((1.6, 0.3), (1.6, 0.2))
                Line((1.6, 0.2), (1.8, 0.2))
                Line((1.8, 0.2), (1.8, -0.2))
                Line((1.6, -0.2), (1.8, -0.2))
                Line((1.6, -0.2), (1.6, -0.3))
                Line((1.3, -0.6), (1.6, -0.3))
                Line((0.9, -0.6), (1.3, -0.6))
                CenterArc((0.9, -0.9), 0.3, 90, 90)
                Line((0.6, -1.3), (0.6, -0.9))
                Line((0.6, -1.3), (0.3, -1.6))
                Line((0.3, -1.6), (0.2, -1.6))
                Line((0.2, -1.6), (0.2, -1.8))
                Line((0.2, -1.8), (-0.2, -1.8))
                Line((-0.2, -1.6), (-0.2, -1.8))
                Line((-0.2, -1.6), (-0.3, -1.6))
                Line((-0.6, -1.3), (-0.3, -1.6))
                Line((-0.6, -0.9), (-0.6, -1.3))
                CenterArc((-0.9, -0.9), 0.3, 0, 90)
                Line((-1.3, -0.6), (-0.9, -0.6))
                Line((-1.3, -0.6), (-1.6, -0.3))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, -1), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -1), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 1), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 1), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0008():
    """Model: sf25-25"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7850998432, perimeter: 17.244677986
            with BuildLine():
                Line((-0.3, 0.4), (-0.6, 0.7))
                Line((-0.6, 0.7), (-0.6, 0.8))
                Line((-0.6, 0.8), (-0.3, 0.8))
                Line((-0.3, 0.8), (-0.3, 1))
                Line((-0.8, 1), (-0.3, 1))
                CenterArc((-0.8, 0.8), 0.2, 90, 90)
                Line((-1, 0.8), (-1, 0.3))
                Line((-1, 0.3), (-0.8, 0.3))
                Line((-0.8, 0.3), (-0.8, 0.6))
                Line((-0.8, 0.6), (-0.7, 0.6))
                Line((-0.7, 0.6), (-0.4, 0.3))
                Line((-0.4, 0.0224701299), (-0.4, 0.3))
                Line((-0.3775298701, 0), (-0.4, 0.0224701299))
                Line((-0.4, -0.0224701299), (-0.3775298701, 0))
                Line((-0.4, -0.3), (-0.4, -0.0224701299))
                Line((-0.4, -0.3), (-0.7, -0.6))
                Line((-0.7, -0.6), (-0.8, -0.6))
                Line((-0.8, -0.6), (-0.8, -0.3))
                Line((-0.8, -0.3), (-1, -0.3))
                Line((-1, -0.3), (-1, -0.8))
                CenterArc((-0.8, -0.8), 0.2, 180, 90)
                Line((-0.8, -1), (-0.3, -1))
                Line((-0.3, -1), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.6, -0.8))
                Line((-0.6, -0.8), (-0.6, -0.7))
                Line((-0.3, -0.4), (-0.6, -0.7))
                Line((-0.0224701299, -0.4), (-0.3, -0.4))
                Line((0, -0.3775298701), (-0.0224701299, -0.4))
                Line((0.0224701299, -0.4), (0, -0.3775298701))
                Line((0.0224701299, -0.4), (0.3, -0.4))
                Line((0.3, -0.4), (0.6, -0.7))
                Line((0.6, -0.7), (0.6, -0.8))
                Line((0.6, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (0.3, -1))
                Line((0.8, -1), (0.3, -1))
                CenterArc((0.8, -0.8), 0.2, -90, 90)
                Line((1, -0.3), (1, -0.8))
                Line((0.8, -0.3), (1, -0.3))
                Line((0.8, -0.3), (0.8, -0.6))
                Line((0.8, -0.6), (0.7, -0.6))
                Line((0.4, -0.3), (0.7, -0.6))
                Line((0.4, -0.0224701299), (0.4, -0.3))
                Line((0.3775298701, 0), (0.4, -0.0224701299))
                Line((0.4, 0.0224701299), (0.3775298701, 0))
                Line((0.4, 0.3), (0.4, 0.0224701299))
                Line((0.4, 0.3), (0.7, 0.6))
                Line((0.7, 0.6), (0.8, 0.6))
                Line((0.8, 0.6), (0.8, 0.3))
                Line((0.8, 0.3), (1, 0.3))
                Line((1, 0.8), (1, 0.3))
                CenterArc((0.8, 0.8), 0.2, 0, 90)
                Line((0.3, 1), (0.8, 1))
                Line((0.3, 1), (0.3, 0.8))
                Line((0.3, 0.8), (0.6, 0.8))
                Line((0.6, 0.8), (0.6, 0.7))
                Line((0.3, 0.4), (0.6, 0.7))
                Line((0.0224701299, 0.4), (0.3, 0.4))
                Line((0, 0.3775298701), (0.0224701299, 0.4))
                Line((-0.0224701299, 0.4), (0, 0.3775298701))
                Line((-0.3, 0.4), (-0.0224701299, 0.4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0012():
    """Model: sf20-80-SS"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 71 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.8873197005, perimeter: 91.3914207584
            with BuildLine():
                Line((-1.3, 7.4), (-1.6, 7.7))
                Line((-1.6, 7.7), (-1.6, 7.8))
                Line((-1.6, 7.8), (-1.3, 7.8))
                Line((-1.3, 7.8), (-1.3, 8))
                Line((-1.8, 8), (-1.3, 8))
                CenterArc((-1.8, 7.8), 0.2, 90, 90)
                Line((-2, 7.3), (-2, 7.8))
                Line((-2, 7.3), (-1.8, 7.3))
                Line((-1.8, 7.3), (-1.8, 7.6))
                Line((-1.8, 7.6), (-1.7, 7.6))
                Line((-1.4, 7.3), (-1.7, 7.6))
                Line((-1.4, 7.0224701299), (-1.4, 7.3))
                Line((-1.3775298701, 7), (-1.4, 7.0224701299))
                Line((-1.4, 6.9775298701), (-1.3775298701, 7))
                Line((-1.4, 6.7), (-1.4, 6.9775298701))
                Line((-1.4, 6.7), (-1.7, 6.4))
                Line((-1.7, 6.4), (-1.8, 6.4))
                Line((-1.8, 6.4), (-1.8, 6.7))
                Line((-1.8, 6.7), (-2, 6.7))
                Line((-2, 5.3), (-2, 6.7))
                Line((-2, 5.3), (-1.8, 5.3))
                Line((-1.8, 5.3), (-1.8, 5.6))
                Line((-1.8, 5.6), (-1.7, 5.6))
                Line((-1.4, 5.3), (-1.7, 5.6))
                Line((-1.4, 5.0224701299), (-1.4, 5.3))
                Line((-1.3775298701, 5), (-1.4, 5.0224701299))
                Line((-1.4, 4.9775298701), (-1.3775298701, 5))
                Line((-1.4, 4.7), (-1.4, 4.9775298701))
                Line((-1.4, 4.7), (-1.7, 4.4))
                Line((-1.7, 4.4), (-1.8, 4.4))
                Line((-1.8, 4.4), (-1.8, 4.7))
                Line((-1.8, 4.7), (-2, 4.7))
                Line((-2, 3.3), (-2, 4.7))
                Line((-2, 3.3), (-1.8, 3.3))
                Line((-1.8, 3.3), (-1.8, 3.6))
                Line((-1.8, 3.6), (-1.7, 3.6))
                Line((-1.4, 3.3), (-1.7, 3.6))
                Line((-1.4, 3.0224701299), (-1.4, 3.3))
                Line((-1.3775298701, 3), (-1.4, 3.0224701299))
                Line((-1.4, 2.9775298701), (-1.3775298701, 3))
                Line((-1.4, 2.7), (-1.4, 2.9775298701))
                Line((-1.4, 2.7), (-1.7, 2.4))
                Line((-1.7, 2.4), (-1.8, 2.4))
                Line((-1.8, 2.4), (-1.8, 2.7))
                Line((-1.8, 2.7), (-2, 2.7))
                Line((-2, 1.3), (-2, 2.7))
                Line((-2, 1.3), (-1.8, 1.3))
                Line((-1.8, 1.3), (-1.8, 1.6))
                Line((-1.8, 1.6), (-1.7, 1.6))
                Line((-1.4, 1.3), (-1.7, 1.6))
                Line((-1.4, 1.0224701299), (-1.4, 1.3))
                Line((-1.3775298701, 1), (-1.4, 1.0224701299))
                Line((-1.4, 0.9775298701), (-1.3775298701, 1))
                Line((-1.4, 0.7), (-1.4, 0.9775298701))
                Line((-1.4, 0.7), (-1.7, 0.4))
                Line((-1.7, 0.4), (-1.8, 0.4))
                Line((-1.8, 0.4), (-1.8, 0.7))
                Line((-1.8, 0.7), (-2, 0.7))
                Line((-2, 0.2), (-2, 0.7))
                CenterArc((-1.8, 0.2), 0.2, 180, 90)
                Line((-1.3, 0), (-1.8, 0))
                Line((-1.3, 0), (-1.3, 0.2))
                Line((-1.3, 0.2), (-1.6, 0.2))
                Line((-1.6, 0.2), (-1.6, 0.3))
                Line((-1.3, 0.6), (-1.6, 0.3))
                Line((-1.0224701299, 0.6), (-1.3, 0.6))
                Line((-1, 0.6224701299), (-1.0224701299, 0.6))
                Line((-0.9775298701, 0.6), (-1, 0.6224701299))
                Line((-0.7, 0.6), (-0.9775298701, 0.6))
                Line((-0.7, 0.6), (-0.4, 0.3))
                Line((-0.4, 0.3), (-0.4, 0.2))
                Line((-0.4, 0.2), (-0.7, 0.2))
                Line((-0.7, 0.2), (-0.7, 0))
                Line((-0.7, 0), (0.7, 0))
                Line((0.7, 0), (0.7, 0.2))
                Line((0.7, 0.2), (0.4, 0.2))
                Line((0.4, 0.2), (0.4, 0.3))
                Line((0.7, 0.6), (0.4, 0.3))
                Line((0.9775298701, 0.6), (0.7, 0.6))
                Line((1, 0.6224701299), (0.9775298701, 0.6))
                Line((1.0224701299, 0.6), (1, 0.6224701299))
                Line((1.3, 0.6), (1.0224701299, 0.6))
                Line((1.3, 0.6), (1.6, 0.3))
                Line((1.6, 0.3), (1.6, 0.2))
                Line((1.6, 0.2), (1.3, 0.2))
                Line((1.3, 0.2), (1.3, 0))
                Line((1.8, 0), (1.3, 0))
                CenterArc((1.8, 0.2), 0.2, -90, 90)
                Line((2, 0.7), (2, 0.2))
                Line((2, 0.7), (1.8, 0.7))
                Line((1.8, 0.7), (1.8, 0.4))
                Line((1.8, 0.4), (1.7, 0.4))
                Line((1.4, 0.7), (1.7, 0.4))
                Line((1.4, 0.9775298701), (1.4, 0.7))
                Line((1.3775298701, 1), (1.4, 0.9775298701))
                Line((1.4, 1.0224701299), (1.3775298701, 1))
                Line((1.4, 1.3), (1.4, 1.0224701299))
                Line((1.4, 1.3), (1.7, 1.6))
                Line((1.7, 1.6), (1.8, 1.6))
                Line((1.8, 1.6), (1.8, 1.3))
                Line((1.8, 1.3), (2, 1.3))
                Line((2, 2.7), (2, 1.3))
                Line((2, 2.7), (1.8, 2.7))
                Line((1.8, 2.7), (1.8, 2.4))
                Line((1.8, 2.4), (1.7, 2.4))
                Line((1.4, 2.7), (1.7, 2.4))
                Line((1.4, 2.9775298701), (1.4, 2.7))
                Line((1.3775298701, 3), (1.4, 2.9775298701))
                Line((1.4, 3.0224701299), (1.3775298701, 3))
                Line((1.4, 3.3), (1.4, 3.0224701299))
                Line((1.4, 3.3), (1.7, 3.6))
                Line((1.7, 3.6), (1.8, 3.6))
                Line((1.8, 3.6), (1.8, 3.3))
                Line((1.8, 3.3), (2, 3.3))
                Line((2, 4.7), (2, 3.3))
                Line((2, 4.7), (1.8, 4.7))
                Line((1.8, 4.7), (1.8, 4.4))
                Line((1.8, 4.4), (1.7, 4.4))
                Line((1.4, 4.7), (1.7, 4.4))
                Line((1.4, 4.9775298701), (1.4, 4.7))
                Line((1.3775298701, 5), (1.4, 4.9775298701))
                Line((1.4, 5.0224701299), (1.3775298701, 5))
                Line((1.4, 5.3), (1.4, 5.0224701299))
                Line((1.4, 5.3), (1.7, 5.6))
                Line((1.7, 5.6), (1.8, 5.6))
                Line((1.8, 5.6), (1.8, 5.3))
                Line((1.8, 5.3), (2, 5.3))
                Line((2, 6.7), (2, 5.3))
                Line((2, 6.7), (1.8, 6.7))
                Line((1.8, 6.7), (1.8, 6.4))
                Line((1.8, 6.4), (1.7, 6.4))
                Line((1.4, 6.7), (1.7, 6.4))
                Line((1.4, 6.9775298701), (1.4, 6.7))
                Line((1.3775298701, 7), (1.4, 6.9775298701))
                Line((1.4, 7.0224701299), (1.3775298701, 7))
                Line((1.4, 7.3), (1.4, 7.0224701299))
                Line((1.4, 7.3), (1.7, 7.6))
                Line((1.7, 7.6), (1.8, 7.6))
                Line((1.8, 7.6), (1.8, 7.3))
                Line((1.8, 7.3), (2, 7.3))
                Line((2, 7.8), (2, 7.3))
                CenterArc((1.8, 7.8), 0.2, 0, 90)
                Line((1.3, 8), (1.8, 8))
                Line((1.3, 8), (1.3, 7.8))
                Line((1.3, 7.8), (1.6, 7.8))
                Line((1.6, 7.8), (1.6, 7.7))
                Line((1.3, 7.4), (1.6, 7.7))
                Line((1.0224701299, 7.4), (1.3, 7.4))
                Line((1, 7.3775298701), (1.0224701299, 7.4))
                Line((0.9775298701, 7.4), (1, 7.3775298701))
                Line((0.7, 7.4), (0.9775298701, 7.4))
                Line((0.7, 7.4), (0.4, 7.7))
                Line((0.4, 7.7), (0.4, 7.8))
                Line((0.4, 7.8), (0.7, 7.8))
                Line((0.7, 7.8), (0.7, 8))
                Line((0.7, 8), (-0.7, 8))
                Line((-0.7, 8), (-0.7, 7.8))
                Line((-0.7, 7.8), (-0.4, 7.8))
                Line((-0.4, 7.8), (-0.4, 7.7))
                Line((-0.7, 7.4), (-0.4, 7.7))
                Line((-0.9775298701, 7.4), (-0.7, 7.4))
                Line((-1, 7.3775298701), (-0.9775298701, 7.4))
                Line((-1.0224701299, 7.4), (-1, 7.3775298701))
                Line((-1.3, 7.4), (-1.0224701299, 7.4))
            make_face()
            with BuildLine():
                Line((-0.7184788543, 4.5953133531), (-0.576412611, 4.5953133531))
                Line((-0.576412611, 5.3), (-0.576412611, 4.5953133531))
                Line((-0.576412611, 5.3), (0.6, 5.3))
                Line((0.6, 5.3), (0.6, 4.5953133531))
                Line((0.6, 4.5953133531), (0.7184788543, 4.5953133531))
                Line((0.8800764575, 4.8276099076), (0.7184788543, 4.5953133531))
                CenterArc((1, 5), 0.21, -64.7938620278, 299.9693728709)
                Line((1.6, 4.3), (1.0894340065, 4.8099958988))
                Line((1.6, 4.3), (1.6, 4.2))
                Line((1.6, 4.2), (1.8, 4.2))
                Line((1.8, 4.2), (1.8, 3.8))
                Line((1.6, 3.8), (1.8, 3.8))
                Line((1.6, 3.8), (1.6, 3.7))
                Line((1.0898213145, 3.1898213145), (1.6, 3.7))
                CenterArc((1, 3), 0.21, 124.4266141512, 300.2503988751)
                Line((0.8812764556, 3.1732187057), (0.725841285, 3.4))
                Line((0.6, 3.4), (0.725841285, 3.4))
                Line((0.6, 3.4), (0.6, 2.7))
                Line((-0.6, 2.7), (0.6, 2.7))
                Line((-0.6, 3.4), (-0.6, 2.7))
                Line((-0.7217391304, 3.4), (-0.6, 3.4))
                Line((-0.8800764575, 3.1723900924), (-0.7217391304, 3.4))
                CenterArc((-1, 3), 0.21, 115.3229869737, 299.8525238694)
                Line((-1.6, 3.7), (-1.0898213145, 3.1898213145))
                Line((-1.6, 3.7), (-1.6, 3.8))
                Line((-1.6, 3.8), (-1.8, 3.8))
                Line((-1.8, 4.2), (-1.8, 3.8))
                Line((-1.6, 4.2), (-1.8, 4.2))
                Line((-1.6, 4.2), (-1.6, 4.3))
                Line((-1.3046866469, 4.5953133531), (-1.6, 4.3))
                Line((-1.3046866469, 4.5953133531), (-1.0899841707, 4.8102558327))
                CenterArc((-1, 5), 0.21, -55.175510843, 299.8033572774)
                Line((-0.8800764575, 4.8276099076), (-0.7184788543, 4.5953133531))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.3, 6.6), (-0.8, 6.6))
                CenterArc((-0.8, 6.8), 0.2, -90, 90)
                Line((-0.6, 7.3), (-0.6, 6.8))
                Line((-0.6, 7.3), (-0.3, 7.6))
                Line((-0.3, 7.6), (-0.2, 7.6))
                Line((-0.2, 7.6), (-0.2, 7.8))
                Line((-0.2, 7.8), (0.2, 7.8))
                Line((0.2, 7.6), (0.2, 7.8))
                Line((0.2, 7.6), (0.3, 7.6))
                Line((0.6, 7.3), (0.3, 7.6))
                Line((0.6, 7.3), (0.6, 6.8))
                CenterArc((0.8, 6.8), 0.2, -180, 90)
                Line((0.8, 6.6), (1.3, 6.6))
                Line((1.3, 6.6), (1.6, 6.3))
                Line((1.6, 6.3), (1.6, 6.2))
                Line((1.6, 6.2), (1.8, 6.2))
                Line((1.8, 6.2), (1.8, 5.8))
                Line((1.6, 5.8), (1.8, 5.8))
                Line((1.6, 5.8), (1.6, 5.7))
                Line((1.3, 5.4), (1.6, 5.7))
                Line((1.3, 5.4), (-1.3, 5.4))
                Line((-1.3, 5.4), (-1.6, 5.7))
                Line((-1.6, 5.7), (-1.6, 5.8))
                Line((-1.6, 5.8), (-1.8, 5.8))
                Line((-1.8, 6.2), (-1.8, 5.8))
                Line((-1.6, 6.2), (-1.8, 6.2))
                Line((-1.6, 6.2), (-1.6, 6.3))
                Line((-1.3, 6.6), (-1.6, 6.3))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.6, 2.2), (-1.6, 2.3))
                Line((-1.3, 2.6), (-1.6, 2.3))
                Line((-1.3, 2.6), (1.3, 2.6))
                Line((1.3, 2.6), (1.6, 2.3))
                Line((1.6, 2.3), (1.6, 2.2))
                Line((1.6, 2.2), (1.8, 2.2))
                Line((1.8, 2.2), (1.8, 1.8))
                Line((1.8, 1.8), (1.6, 1.8))
                Line((1.6, 1.8), (1.6, 1.7))
                Line((1.3, 1.4), (1.6, 1.7))
                Line((0.8, 1.4), (1.3, 1.4))
                CenterArc((0.8, 1.2), 0.2, 90, 90)
                Line((0.6, 1.2), (0.6, 0.7))
                Line((0.6, 0.7), (0.3, 0.4))
                Line((0.3, 0.4), (0.2, 0.4))
                Line((0.2, 0.4), (0.2, 0.2))
                Line((0.2, 0.2), (-0.2, 0.2))
                Line((-0.2, 0.4), (-0.2, 0.2))
                Line((-0.2, 0.4), (-0.2912405147, 0.4))
                Line((-0.576412611, 0.6894132703), (-0.2912405147, 0.4))
                Line((-0.576412611, 1.2), (-0.576412611, 0.6894132703))
                CenterArc((-0.776412611, 1.2), 0.2, 0, 90)
                Line((-1.3, 1.4), (-0.776412611, 1.4))
                Line((-1.3, 1.4), (-1.6, 1.7))
                Line((-1.6, 1.7), (-1.6, 1.8))
                Line((-1.6, 1.8), (-1.8, 1.8))
                Line((-1.8, 2.2), (-1.8, 1.8))
                Line((-1.6, 2.2), (-1.8, 2.2))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 7), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 7), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 1), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 1), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45680_5b1610e8_0013():
    """Model: sf20-40-40"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2518569594, perimeter: 42.6625322496
            with BuildLine():
                Line((-0.2, 1.7), (-0.2, 1.4))
                Line((-0.2, 1.4), (-0.3, 1.4))
                Line((-0.6, 1.7), (-0.3, 1.4))
                Line((-0.6, 1.9775298701), (-0.6, 1.7))
                Line((-0.6224701299, 2), (-0.6, 1.9775298701))
                Line((-0.6, 2.0224701299), (-0.6224701299, 2))
                Line((-0.6, 2.3), (-0.6, 2.0224701299))
                Line((-0.6, 2.3), (-0.3, 2.6))
                Line((-0.3, 2.6), (-0.2, 2.6))
                Line((-0.2, 2.6), (-0.2, 2.3))
                Line((-0.2, 2.3), (0, 2.3))
                Line((0, 2.8), (0, 2.3))
                CenterArc((-0.2, 2.8), 0.2, 0, 90)
                Line((-0.7, 3), (-0.2, 3))
                Line((-0.7, 3), (-0.7, 2.8))
                Line((-0.7, 2.8), (-0.4, 2.8))
                Line((-0.4, 2.8), (-0.4, 2.7))
                Line((-0.7, 2.4), (-0.4, 2.7))
                Line((-0.9775298701, 2.4), (-0.7, 2.4))
                Line((-1, 2.3775298701), (-0.9775298701, 2.4))
                Line((-1.0224701299, 2.4), (-1, 2.3775298701))
                Line((-1.3, 2.4), (-1.0224701299, 2.4))
                Line((-1.3, 2.4), (-1.6, 2.7))
                Line((-1.6, 2.7), (-1.6, 2.8))
                Line((-1.6, 2.8), (-1.3, 2.8))
                Line((-1.3, 2.8), (-1.3, 3))
                Line((-1.8, 3), (-1.3, 3))
                CenterArc((-1.8, 2.8), 0.2, 90, 90)
                Line((-2, 2.8), (-2, 2.3))
                Line((-2, 2.3), (-1.8, 2.3))
                Line((-1.8, 2.3), (-1.8, 2.6))
                Line((-1.8, 2.6), (-1.7, 2.6))
                Line((-1.7, 2.6), (-1.4, 2.3))
                Line((-1.4, 2.0224701299), (-1.4, 2.3))
                Line((-1.3775298701, 2), (-1.4, 2.0224701299))
                Line((-1.4, 1.9775298701), (-1.3775298701, 2))
                Line((-1.4, 1.7), (-1.4, 1.9775298701))
                Line((-1.4, 1.7), (-1.7, 1.4))
                Line((-1.7, 1.4), (-1.8, 1.4))
                Line((-1.8, 1.4), (-1.8, 1.7))
                Line((-1.8, 1.7), (-2, 1.7))
                Line((-2, 1.7), (-2, 0.3))
                Line((-2, 0.3), (-1.8, 0.3))
                Line((-1.8, 0.3), (-1.8, 0.6))
                Line((-1.8, 0.6), (-1.7, 0.6))
                Line((-1.7, 0.6), (-1.4, 0.3))
                Line((-1.4, 0.0224701299), (-1.4, 0.3))
                Line((-1.3775298701, 0), (-1.4, 0.0224701299))
                Line((-1.4, -0.0224701299), (-1.3775298701, 0))
                Line((-1.4, -0.3), (-1.4, -0.0224701299))
                Line((-1.4, -0.3), (-1.7, -0.6))
                Line((-1.7, -0.6), (-1.8, -0.6))
                Line((-1.8, -0.6), (-1.8, -0.3))
                Line((-1.8, -0.3), (-2, -0.3))
                Line((-2, -0.3), (-2, -0.8))
                CenterArc((-1.8, -0.8), 0.2, 180, 90)
                Line((-1.8, -1), (-1.3, -1))
                Line((-1.3, -1), (-1.3, -0.8))
                Line((-1.3, -0.8), (-1.6, -0.8))
                Line((-1.6, -0.8), (-1.6, -0.7))
                Line((-1.3, -0.4), (-1.6, -0.7))
                Line((-1.0224701299, -0.4), (-1.3, -0.4))
                Line((-1, -0.3775298701), (-1.0224701299, -0.4))
                Line((-0.9775298701, -0.4), (-1, -0.3775298701))
                Line((-0.9775298701, -0.4), (-0.7, -0.4))
                Line((-0.7, -0.4), (-0.4, -0.7))
                Line((-0.4, -0.7), (-0.4, -0.8))
                Line((-0.4, -0.8), (-0.7, -0.8))
                Line((-0.7, -0.8), (-0.7, -1))
                Line((-0.7, -1), (0.7, -1))
                Line((0.7, -1), (0.7, -0.8))
                Line((0.7, -0.8), (0.4, -0.8))
                Line((0.4, -0.8), (0.4, -0.7))
                Line((0.7, -0.4), (0.4, -0.7))
                Line((0.9775298701, -0.4), (0.7, -0.4))
                Line((1, -0.3775298701), (0.9775298701, -0.4))
                Line((1.0224701299, -0.4), (1, -0.3775298701))
                Line((1.0224701299, -0.4), (1.3, -0.4))
                Line((1.3, -0.4), (1.6, -0.7))
                Line((1.6, -0.7), (1.6, -0.8))
                Line((1.6, -0.8), (1.3, -0.8))
                Line((1.3, -0.8), (1.3, -1))
                Line((1.8, -1), (1.3, -1))
                CenterArc((1.8, -0.8), 0.2, -90, 90)
                Line((2, -0.3), (2, -0.8))
                Line((1.8, -0.3), (2, -0.3))
                Line((1.8, -0.3), (1.8, -0.6))
                Line((1.8, -0.6), (1.7, -0.6))
                Line((1.4, -0.3), (1.7, -0.6))
                Line((1.4, -0.0224701299), (1.4, -0.3))
                Line((1.3775298701, 0), (1.4, -0.0224701299))
                Line((1.4, 0.0224701299), (1.3775298701, 0))
                Line((1.4, 0.3), (1.4, 0.0224701299))
                Line((1.4, 0.3), (1.7, 0.6))
                Line((1.7, 0.6), (1.8, 0.6))
                Line((1.8, 0.6), (1.8, 0.3))
                Line((1.8, 0.3), (2, 0.3))
                Line((2, 0.8), (2, 0.3))
                CenterArc((1.8, 0.8), 0.2, 0, 90)
                Line((1.3, 1), (1.8, 1))
                Line((1.3, 1), (1.3, 0.8))
                Line((1.3, 0.8), (1.6, 0.8))
                Line((1.6, 0.8), (1.6, 0.7))
                Line((1.3, 0.4), (1.6, 0.7))
                Line((1.0224701299, 0.4), (1.3, 0.4))
                Line((1, 0.3775298701), (1.0224701299, 0.4))
                Line((0.9775298701, 0.4), (1, 0.3775298701))
                Line((0.7, 0.4), (0.9775298701, 0.4))
                Line((0.7, 0.4), (0.4, 0.7))
                Line((0.4, 0.7), (0.4, 0.8))
                Line((0.4, 0.8), (0.7, 0.8))
                Line((0.7, 0.8), (0.7, 1))
                Line((0.1, 1), (0.7, 1))
                CenterArc((0.1, 1.1), 0.1, 180, 90)
                Line((0, 1.7), (0, 1.1))
                Line((-0.2, 1.7), (0, 1.7))
            make_face()
            with BuildLine():
                Line((-1.21, 0), (-1.21, 0.31))
                Line((-1.6, 0.7), (-1.21, 0.31))
                Line((-1.6, 0.7), (-1.6, 0.8))
                Line((-1.6, 0.8), (-1.8, 0.8))
                Line((-1.8, 1.2), (-1.8, 0.8))
                Line((-1.6, 1.2), (-1.8, 1.2))
                Line((-1.6, 1.2), (-1.6, 1.3))
                Line((-1.3, 1.6), (-1.6, 1.3))
                Line((-1.0224701299, 1.6), (-1.3, 1.6))
                Line((-1, 1.6224701299), (-1.0224701299, 1.6))
                Line((-0.9775298701, 1.6), (-1, 1.6224701299))
                Line((-0.9775298701, 1.6), (-0.7, 1.6))
                Line((-0.7, 1.6), (0.6, 0.3))
                Line((0.6, 0.3), (0.6, -0.3))
                Line((0.6, -0.3), (0.3, -0.6))
                Line((0.3, -0.6), (0.2, -0.6))
                Line((0.2, -0.6), (0.2, -0.8))
                Line((-0.2, -0.8), (0.2, -0.8))
                Line((-0.2, -0.6), (-0.2, -0.8))
                Line((-0.2, -0.6), (-0.3, -0.6))
                Line((-0.69, -0.21), (-0.3, -0.6))
                Line((-1, -0.21), (-0.69, -0.21))
                CenterArc((-1, 0), 0.21, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 2), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-100
        extrude(amount=-100)
    return part.part


def model_45796_4455d9eb_0005():
    """Model: 1.5in pipe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4820682164, perimeter: 27.848962237
            with BuildLine():
                CenterArc((-30.2751247712, -37.0609285992), 2.413, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-30.2751247712, -37.0609285992), 2.0193, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=40.64
        extrude(amount=40.64)
    return part.part


def model_45797_78875e5a_0001():
    """Model: top support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 311.9819626045, perimeter: 119.7396453401
            with BuildLine():
                Line((-23.6893212158, 21.9600329141), (-73.2193212158, 21.9600329141))
                Line((-23.6893212158, 28.3100329141), (-23.6893212158, 21.9600329141))
                Line((-73.2193212158, 28.3100329141), (-23.6893212158, 28.3100329141))
                Line((-73.2193212158, 21.9600329141), (-73.2193212158, 28.3100329141))
            make_face()
            with BuildLine():
                CenterArc((-26.2293212158, 25.7700329141), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-70.6793212158, 25.7700329141), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_45797_78875e5a_0002():
    """Model: 2.5x.25x19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 273.2723626045, perimeter: 115.9296453401
            with BuildLine():
                Line((69.2149989891, 55.2449991226), (69.2149989891, 60.9599991226))
                Line((69.2149989891, 60.9599991226), (20.9549989891, 60.9599991226))
                Line((20.9549989891, 60.9599991226), (20.9549989891, 55.2449991226))
                Line((20.9549989891, 55.2449991226), (69.2149989891, 55.2449991226))
            make_face()
            with BuildLine():
                CenterArc((67.3099989891, 58.4199991226), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.8599989891, 58.4199991226), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_45797_78875e5a_0005():
    """Model: 2in pipe"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.34936635, perimeter: 35.285991694
            with BuildLine():
                CenterArc((-58.4199991226, -35.5599994659), 3.01625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-58.4199991226, -35.5599994659), 2.59969, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=45.72
        extrude(amount=45.72)
    return part.part


MODELS = {
    "model_41902_43d78d0f_0001": {"func": model_41902_43d78d0f_0001, "volume": 2951.064625967, "area": 1882.2795251745},
    "model_41902_43d78d0f_0006": {"func": model_41902_43d78d0f_0006, "volume": 1089.739756, "area": 1148.3848},
    "model_41902_43d78d0f_0023": {"func": model_41902_43d78d0f_0023, "volume": 570.4609670891, "area": 808.4737602692},
    "model_41902_43d78d0f_0024": {"func": model_41902_43d78d0f_0024, "volume": 1363.9993629267, "area": 1427.9780046241},
    "model_41907_7bcecdb1_0003": {"func": model_41907_7bcecdb1_0003, "volume": 0.5185501221, "area": 7.4018469865},
    "model_41907_7bcecdb1_0006": {"func": model_41907_7bcecdb1_0006, "volume": 1.1749478766, "area": 10.6111739069},
    "model_41907_7bcecdb1_0008": {"func": model_41907_7bcecdb1_0008, "volume": 0.6658274274, "area": 8.6694246574},
    "model_41907_7bcecdb1_0011": {"func": model_41907_7bcecdb1_0011, "volume": 0.5612305742, "area": 8.0183659263},
    "model_41912_72d5af56_0000": {"func": model_41912_72d5af56_0000, "volume": 0.0332122454, "area": 2.7561045802},
    "model_41912_7334aba9_0000": {"func": model_41912_7334aba9_0000, "volume": 3.8272307523, "area": 24.4665222948},
    "model_41912_73d5e58c_0000": {"func": model_41912_73d5e58c_0000, "volume": 0.0245143195, "area": 2.0291672952},
    "model_41912_a2872c24_0000": {"func": model_41912_a2872c24_0000, "volume": 4.9141531115, "area": 26.9695469008},
    "model_41912_e5724931_0000": {"func": model_41912_e5724931_0000, "volume": 3.7857697017, "area": 21.2350475415},
    "model_41912_fd149787_0000": {"func": model_41912_fd149787_0000, "volume": 41.0501302216, "area": 193.4982293144},
    "model_41917_f0c40fa1_0000": {"func": model_41917_f0c40fa1_0000, "volume": 0.0031415927, "area": 0.1413716694},
    "model_41917_f0c40fa1_0002": {"func": model_41917_f0c40fa1_0002, "volume": 0.0981747704, "area": 2.7488935719},
    "model_41917_f0c40fa1_0003": {"func": model_41917_f0c40fa1_0003, "volume": 0.0188495559, "area": 0.5654866776},
    "model_41917_f0c40fa1_0006": {"func": model_41917_f0c40fa1_0006, "volume": 0.0777544182, "area": 1.9006635554},
    "model_41917_f0c40fa1_0007": {"func": model_41917_f0c40fa1_0007, "volume": 0.0039269908, "area": 0.1727875959},
    "model_41919_d2473a88_0003": {"func": model_41919_d2473a88_0003, "volume": 21.2057504117, "area": 60.0829594999},
    "model_41924_ac7400c0_0004": {"func": model_41924_ac7400c0_0004, "volume": 0.0625, "area": 1.125},
    "model_41941_79d46bb4_0001": {"func": model_41941_79d46bb4_0001, "volume": 921.7723223127, "area": 2999.9939113426},
    "model_41941_79d46bb4_0005": {"func": model_41941_79d46bb4_0005, "volume": 0.1973021633, "area": 3.287451067},
    "model_41941_79d46bb4_0006": {"func": model_41941_79d46bb4_0006, "volume": 7.2851672404, "area": 67.2361172944},
    "model_41941_79d46bb4_0008": {"func": model_41941_79d46bb4_0008, "volume": 5.8252731507, "area": 27.3610300944},
    "model_41942_29c07f06_0005": {"func": model_41942_29c07f06_0005, "volume": 530.8934550603, "area": 589.715590032},
    "model_41958_acdbb913_0000": {"func": model_41958_acdbb913_0000, "volume": 45.9984034748, "area": 257.0428528568},
    "model_41970_24ba0c1b_0003": {"func": model_41970_24ba0c1b_0003, "volume": 0.0687180941, "area": 1.8802294614},
    "model_41970_24ba0c1b_0004": {"func": model_41970_24ba0c1b_0004, "volume": 0.0612610567, "area": 1.4294246574},
    "model_41970_24ba0c1b_0005": {"func": model_41970_24ba0c1b_0005, "volume": 1.0610225882, "area": 15.405903202},
    "model_41973_0e5cd44c_0008": {"func": model_41973_0e5cd44c_0008, "volume": 8.1180410861, "area": 31.4043329044},
    "model_41973_0e5cd44c_0010": {"func": model_41973_0e5cd44c_0010, "volume": 14.8418598295, "area": 110.1078289537},
    "model_41978_2d035a32_0000": {"func": model_41978_2d035a32_0000, "volume": 0.0420567208, "area": 6.6241190473},
    "model_41978_48e2a5bb_0000": {"func": model_41978_48e2a5bb_0000, "volume": 0.0946276217, "area": 9.9369386321},
    "model_41978_9d21376f_0000": {"func": model_41978_9d21376f_0000, "volume": 1.0450841756, "area": 32.9413724019},
    "model_41978_b9f032be_0000": {"func": model_41978_b9f032be_0000, "volume": 1.4, "area": 10.3},
    "model_41982_f75ceb8f_0008": {"func": model_41982_f75ceb8f_0008, "volume": 5.429203727, "area": 26.0000001171},
    "model_41986_26275a06_0000": {"func": model_41986_26275a06_0000, "volume": 0.3052812757, "area": 3.0884067769},
    "model_41986_26275a06_0001": {"func": model_41986_26275a06_0001, "volume": 0.06, "area": 2.62},
    "model_41986_26275a06_0009": {"func": model_41986_26275a06_0009, "volume": 60.0830428747, "area": 175.5574180521},
    "model_41998_654ac923_0006": {"func": model_41998_654ac923_0006, "volume": 6.8593781226, "area": 58.5730297139},
    "model_41998_654ac923_0008": {"func": model_41998_654ac923_0008, "volume": 1759.2918860103, "area": 1784.424627239},
    "model_42004_549eeccf_0000": {"func": model_42004_549eeccf_0000, "volume": 0.3127499902, "area": 5.5545273859},
    "model_42005_128e5c59_0000": {"func": model_42005_128e5c59_0000, "volume": 2.9999998603, "area": 24.4999995269},
    "model_42005_166cd78a_0000": {"func": model_42005_166cd78a_0000, "volume": 282.716652515, "area": 1178.3858592612},
    "model_42005_bb4162aa_0000": {"func": model_42005_bb4162aa_0000, "volume": 1.0053096491, "area": 10.3044239038},
    "model_42013_3c6f187f_0000": {"func": model_42013_3c6f187f_0000, "volume": 1.0710113273, "area": 9.2820981702},
    "model_42013_6092fa24_0000": {"func": model_42013_6092fa24_0000, "volume": 1.4137167362, "area": 9.9902647957},
    "model_42013_b9cc3868_0000": {"func": model_42013_b9cc3868_0000, "volume": 8.0503311748, "area": 80.5033117482},
    "model_42143_51b31600_0005": {"func": model_42143_51b31600_0005, "volume": 123.154685303, "area": 516.49961216},
    "model_42143_51b31600_0008": {"func": model_42143_51b31600_0008, "volume": 25.7407399382, "area": 50.6707479097},
    "model_42329_df7f540f_0021": {"func": model_42329_df7f540f_0021, "volume": 0.3201100168, "area": 7.8127715489},
    "model_42329_df7f540f_0058": {"func": model_42329_df7f540f_0058, "volume": 0.3341344323, "area": 8.0936085285},
    "model_42329_df7f540f_0064": {"func": model_42329_df7f540f_0064, "volume": 0.0003319962, "area": 0.0587777659},
    "model_42329_df7f540f_0069": {"func": model_42329_df7f540f_0069, "volume": 0.0050579642, "area": 0.2456725455},
    "model_42329_df7f540f_0073": {"func": model_42329_df7f540f_0073, "volume": 0.0009047787, "area": 0.1055575132},
    "model_42329_df7f540f_0074": {"func": model_42329_df7f540f_0074, "volume": 0.0006675884, "area": 0.120165919},
    "model_42329_df7f540f_0077": {"func": model_42329_df7f540f_0077, "volume": 0.0045238934, "area": 0.3166725395},
    "model_42333_53c85dac_0007": {"func": model_42333_53c85dac_0007, "volume": 12.1788927627, "area": 30.6196410626},
    "model_42333_53c85dac_0008": {"func": model_42333_53c85dac_0008, "volume": 0.483157797, "area": 6.5389712243},
    "model_42333_53c85dac_0023": {"func": model_42333_53c85dac_0023, "volume": 0.9289585381, "area": 6.8434522208},
    "model_42333_53c85dac_0041": {"func": model_42333_53c85dac_0041, "volume": 0.0000019818, "area": 0.0011095648},
    "model_42333_53c85dac_0044": {"func": model_42333_53c85dac_0044, "volume": 0.1005309649, "area": 2.0106192983},
    "model_42429_df14cc7f_0000": {"func": model_42429_df14cc7f_0000, "volume": 5.0385141607, "area": 44.3280370401},
    "model_42536_905aec30_0016": {"func": model_42536_905aec30_0016, "volume": 0.8571851376, "area": 7.4566589452},
    "model_42573_a34062d9_0000": {"func": model_42573_a34062d9_0000, "volume": 55.1251744342, "area": 239.1114926165},
    "model_42586_517832f9_0005": {"func": model_42586_517832f9_0005, "volume": 8.0439812307, "area": 38.0030609323},
    "model_42586_517832f9_0013": {"func": model_42586_517832f9_0013, "volume": 0.2059259195, "area": 4.1185183901},
    "model_42586_517832f9_0019": {"func": model_42586_517832f9_0019, "volume": 0.3088888793, "area": 2.8375618829},
    "model_42586_517832f9_0024": {"func": model_42586_517832f9_0024, "volume": 0.1544444396, "area": 1.6214639331},
    "model_42586_517832f9_0026": {"func": model_42586_517832f9_0026, "volume": 1.4414814365, "area": 7.296587699},
    "model_42601_bfe96b47_0002": {"func": model_42601_bfe96b47_0002, "volume": 108.0645040982, "area": 748.1388745259},
    "model_42601_bfe96b47_0009": {"func": model_42601_bfe96b47_0009, "volume": 200.1793611693, "area": 1371.619793546},
    "model_42601_bfe96b47_0010": {"func": model_42601_bfe96b47_0010, "volume": 1171.9711394217, "area": 3937.8230284568},
    "model_42811_d7f97f6b_0000": {"func": model_42811_d7f97f6b_0000, "volume": 0.7476990516, "area": 15.3938040026},
    "model_43009_6aa4e085_0018": {"func": model_43009_6aa4e085_0018, "volume": 0.3481747704, "area": 3.1780972451},
    "model_43009_6aa4e085_0028": {"func": model_43009_6aa4e085_0028, "volume": 0.1237002107, "area": 2.638937829},
    "model_43010_31eceafd_0004": {"func": model_43010_31eceafd_0004, "volume": 181.8352714229, "area": 287.566875741},
    "model_43301_c87013f5_0000": {"func": model_43301_c87013f5_0000, "volume": 11.0629910246, "area": 47.1196312854},
    "model_43441_e1ab0873_0001": {"func": model_43441_e1ab0873_0001, "volume": 0.6283185307, "area": 7.5398223686},
    "model_43529_4804941b_0031": {"func": model_43529_4804941b_0031, "volume": 20.106192983, "area": 54.286721054},
    "model_43529_4804941b_0032": {"func": model_43529_4804941b_0032, "volume": 35.8298642142, "area": 101.8190179028},
    "model_43529_4804941b_0046": {"func": model_43529_4804941b_0046, "volume": 0.2410072804, "area": 3.8489222395},
    "model_43529_4804941b_0048": {"func": model_43529_4804941b_0048, "volume": 115.68, "area": 441.68},
    "model_43529_4804941b_0049": {"func": model_43529_4804941b_0049, "volume": 29.4, "area": 114.8},
    "model_43529_4804941b_0053": {"func": model_43529_4804941b_0053, "volume": 172.6588505205, "area": 466.5075137073},
    "model_43529_4804941b_0054": {"func": model_43529_4804941b_0054, "volume": 83.469, "area": 306.3742640687},
    "model_43562_004c6cea_0018": {"func": model_43562_004c6cea_0018, "volume": 140.7433508808, "area": 1410.9520925802},
    "model_43562_004c6cea_0020": {"func": model_43562_004c6cea_0020, "volume": 26.4548948516, "area": 93.3844964969},
    "model_43628_a95b7e66_0011": {"func": model_43628_a95b7e66_0011, "volume": 0.0636172512, "area": 1.7318029503},
    "model_43777_5e0613a3_0000": {"func": model_43777_5e0613a3_0000, "volume": 0.3056112769, "area": 2.5366814436},
    "model_43866_908e0b9a_0000": {"func": model_43866_908e0b9a_0000, "volume": 0.0078539816, "area": 0.471238898},
    "model_43928_6ca53538_0006": {"func": model_43928_6ca53538_0006, "volume": 1.8576237361, "area": 9.2174328456},
    "model_43928_6ca53538_0007": {"func": model_43928_6ca53538_0007, "volume": 0.0678014515, "area": 4.8366010436},
    "model_43928_6ca53538_0017": {"func": model_43928_6ca53538_0017, "volume": 3.787131039, "area": 64.8038307805},
    "model_43931_bb001c04_0000": {"func": model_43931_bb001c04_0000, "volume": 3681318.2714765212, "area": 279350.4187572044},
    "model_43931_bb001c04_0004": {"func": model_43931_bb001c04_0004, "volume": 121553.5228857441, "area": 21591.800633021},
    "model_43931_bb001c04_0005": {"func": model_43931_bb001c04_0005, "volume": 94017.717102008, "area": 18573.0264079403},
    "model_43931_bb001c04_0006": {"func": model_43931_bb001c04_0006, "volume": 577653.9752800284, "area": 66005.4335788641},
    "model_43933_3b763a09_0006": {"func": model_43933_3b763a09_0006, "volume": 2.7488935719, "area": 18.8495559215},
    "model_43934_912ff891_0005": {"func": model_43934_912ff891_0005, "volume": 1.7578761403, "area": 11.0879644737},
    "model_43938_418421a7_0005": {"func": model_43938_418421a7_0005, "volume": 509.1198972784, "area": 484.2836057809},
    "model_43938_418421a7_0007": {"func": model_43938_418421a7_0007, "volume": 2.2920025979, "area": 20.7901893767},
    "model_44030_17bd5ec9_0001": {"func": model_44030_17bd5ec9_0001, "volume": 8156.9720513076, "area": 7009.3040134993},
    "model_44104_2333396f_0000": {"func": model_44104_2333396f_0000, "volume": 1752.0190990172, "area": 844.8370964034},
    "model_44206_ff45fbf0_0007": {"func": model_44206_ff45fbf0_0007, "volume": 0.0003436117, "area": 0.0559596191},
    "model_44206_ff45fbf0_0011": {"func": model_44206_ff45fbf0_0011, "volume": 0.0002120593, "area": 0.0330490816},
    "model_44391_f921a9b0_0000": {"func": model_44391_f921a9b0_0000, "volume": 13245.78, "area": 18330.64},
    "model_44519_90af0df6_0009": {"func": model_44519_90af0df6_0009, "volume": 49.480084294, "area": 135.4811831861},
    "model_44519_90af0df6_0010": {"func": model_44519_90af0df6_0010, "volume": 2.1520539662, "area": 16.3857591485},
    "model_44519_90af0df6_0011": {"func": model_44519_90af0df6_0011, "volume": 0.4123326595, "area": 6.0475553064},
    "model_44519_90af0df6_0013": {"func": model_44519_90af0df6_0013, "volume": 62.4244078954, "area": 131.5686590419},
    "model_44519_90af0df6_0015": {"func": model_44519_90af0df6_0015, "volume": 0.1453474161, "area": 3.1176857446},
    "model_44522_a7c79550_0000": {"func": model_44522_a7c79550_0000, "volume": 13.9255565338, "area": 65.4308634109},
    "model_44522_a7c79550_0001": {"func": model_44522_a7c79550_0001, "volume": 15, "area": 85},
    "model_44522_a7c79550_0002": {"func": model_44522_a7c79550_0002, "volume": 6.1355304525, "area": 41.4690230274},
    "model_44522_a7c79550_0003": {"func": model_44522_a7c79550_0003, "volume": 22.7765467385, "area": 92.6769832809},
    "model_44522_a7c79550_0006": {"func": model_44522_a7c79550_0006, "volume": 3.0398762629, "area": 22.713999443},
    "model_44533_35550b4f_0000": {"func": model_44533_35550b4f_0000, "volume": 1.5079644737, "area": 15.3309721495},
    "model_44741_f386a08f_0002": {"func": model_44741_f386a08f_0002, "volume": 0.7422012644, "area": 10.6028752059},
    "model_44920_70dd4b80_0002": {"func": model_44920_70dd4b80_0002, "volume": 0.7239583108, "area": 6.4605203585},
    "model_44996_b3e9c266_0001": {"func": model_44996_b3e9c266_0001, "volume": 308.8888989738, "area": 496.5733456868},
    "model_44996_b3e9c266_0002": {"func": model_44996_b3e9c266_0002, "volume": 2322.866322, "area": 1809.6738},
    "model_44996_b3e9c266_0006": {"func": model_44996_b3e9c266_0006, "volume": 1290.48129, "area": 1035.4818},
    "model_44996_b3e9c266_0009": {"func": model_44996_b3e9c266_0009, "volume": 460.886175, "area": 653.2245},
    "model_44996_b3e9c266_0010": {"func": model_44996_b3e9c266_0010, "volume": 2982.445648, "area": 4954.8288},
    "model_44996_b3e9c266_0012": {"func": model_44996_b3e9c266_0012, "volume": 737.41788, "area": 1030.6431},
    "model_44996_b3e9c266_0013": {"func": model_44996_b3e9c266_0013, "volume": 368.70894, "area": 527.4183},
    "model_44996_b3e9c266_0016": {"func": model_44996_b3e9c266_0016, "volume": 2359.737216, "area": 3948.3792},
    "model_44998_b4e41716_0005": {"func": model_44998_b4e41716_0005, "volume": 0.00775, "area": 0.33},
    "model_45007_990d2758_0000": {"func": model_45007_990d2758_0000, "volume": 0.3392920066, "area": 2.8274333882},
    "model_45007_990d2758_0002": {"func": model_45007_990d2758_0002, "volume": 471.2388980385, "area": 722.5663103257},
    "model_45235_14713966_0003": {"func": model_45235_14713966_0003, "volume": 0.039729078, "area": 1.1085298286},
    "model_45241_7a955ec1_0007": {"func": model_45241_7a955ec1_0007, "volume": 0.0000225, "area": 0.0054},
    "model_45241_7a955ec1_0011": {"func": model_45241_7a955ec1_0011, "volume": 0.00001875, "area": 0.00475},
    "model_45303_48d14b32_0009": {"func": model_45303_48d14b32_0009, "volume": 38.0525410166, "area": 95.3316290732},
    "model_45303_48d14b32_0014": {"func": model_45303_48d14b32_0014, "volume": 900, "area": 1440},
    "model_45307_b9b4bca0_0002": {"func": model_45307_b9b4bca0_0002, "volume": 0.00001875, "area": 0.00475},
    "model_45307_b9b4bca0_0003": {"func": model_45307_b9b4bca0_0003, "volume": 0.0030869027, "area": 0.1978849556},
    "model_45307_b9b4bca0_0007": {"func": model_45307_b9b4bca0_0007, "volume": 0.0009495708, "area": 0.1123853982},
    "model_45307_b9b4bca0_0008": {"func": model_45307_b9b4bca0_0008, "volume": 0.0000891194, "area": 0.0167732873},
    "model_45331_7b9dc63f_0000": {"func": model_45331_7b9dc63f_0000, "volume": 575.3383870432, "area": 499.8169310492},
    "model_45359_1768ab3f_0016": {"func": model_45359_1768ab3f_0016, "volume": 0.2764601535, "area": 3.0159289474},
    "model_45359_1768ab3f_0030": {"func": model_45359_1768ab3f_0030, "volume": 1.0555751316, "area": 10.8070787283},
    "model_45359_1768ab3f_0035": {"func": model_45359_1768ab3f_0035, "volume": 1.3194689145, "area": 13.4460165574},
    "model_45359_1768ab3f_0036": {"func": model_45359_1768ab3f_0036, "volume": 5.1877747807, "area": 19.1266443936},
    "model_45359_1768ab3f_0045": {"func": model_45359_1768ab3f_0045, "volume": 2.0106192983, "area": 20.3575203953},
    "model_45360_cb4bac3f_0002": {"func": model_45360_cb4bac3f_0002, "volume": 121.0301159112, "area": 421.847897033},
    "model_45360_cb4bac3f_0003": {"func": model_45360_cb4bac3f_0003, "volume": 55.8245622056, "area": 181.1640214177},
    "model_45360_cb4bac3f_0014": {"func": model_45360_cb4bac3f_0014, "volume": 28.8783764119, "area": 100.5661778403},
    "model_45360_cb4bac3f_0017": {"func": model_45360_cb4bac3f_0017, "volume": 0.6031857895, "area": 8.0424771932},
    "model_45360_cb4bac3f_0023": {"func": model_45360_cb4bac3f_0023, "volume": 1.3783737768, "area": 12.8648219165},
    "model_45419_9ab20637_0000": {"func": model_45419_9ab20637_0000, "volume": 5019.4442879398, "area": 8299.868507617},
    "model_45466_5f662bcb_0001": {"func": model_45466_5f662bcb_0001, "volume": 884.901456, "area": 1974.1896},
    "model_45468_eaf0dc99_0005": {"func": model_45468_eaf0dc99_0005, "volume": 68.7223392973, "area": 94.2477796077},
    "model_45546_26041647_0001": {"func": model_45546_26041647_0001, "volume": 90.5747680927, "area": 241.5327149139},
    "model_45557_957c3482_0000": {"func": model_45557_957c3482_0000, "volume": 0.3693041772, "area": 3.5986165486},
    "model_45581_2408ef88_0000": {"func": model_45581_2408ef88_0000, "volume": 4570.3593876381, "area": 2184.6815079512},
    "model_45680_5b1610e8_0000": {"func": model_45680_5b1610e8_0000, "volume": 501.2847534296, "area": 5027.7377860938},
    "model_45680_5b1610e8_0001": {"func": model_45680_5b1610e8_0001, "volume": 192.8661788073, "area": 1830.5961982411},
    "model_45680_5b1610e8_0002": {"func": model_45680_5b1610e8_0002, "volume": 173.5495165897, "area": 1693.8641609963},
    "model_45680_5b1610e8_0004": {"func": model_45680_5b1610e8_0004, "volume": 335.5139680612, "area": 3255.6624499721},
    "model_45680_5b1610e8_0005": {"func": model_45680_5b1610e8_0005, "volume": 196.5099843171, "area": 1908.3979982899},
    "model_45680_5b1610e8_0006": {"func": model_45680_5b1610e8_0006, "volume": 205.5099843171, "area": 1998.5779982899},
    "model_45680_5b1610e8_0007": {"func": model_45680_5b1610e8_0007, "volume": 519.5492697181, "area": 5103.4507995756},
    "model_45680_5b1610e8_0008": {"func": model_45680_5b1610e8_0008, "volume": 178.5099843171, "area": 1728.0379982899},
    "model_45680_5b1610e8_0012": {"func": model_45680_5b1610e8_0012, "volume": 888.7319700495, "area": 9156.9167152379},
    "model_45680_5b1610e8_0013": {"func": model_45680_5b1610e8_0013, "volume": 425.1856959357, "area": 4274.7569388746},
    "model_45796_4455d9eb_0005": {"func": model_45796_4455d9eb_0005, "volume": 222.7912523127, "area": 1142.7459617449},
    "model_45797_78875e5a_0001": {"func": model_45797_78875e5a_0001, "volume": 198.1085462539, "area": 699.9986},
    "model_45797_78875e5a_0002": {"func": model_45797_78875e5a_0002, "volume": 173.5279502539, "area": 620.16005},
    "model_45797_78875e5a_0005": {"func": model_45797_78875e5a_0005, "volume": 336.0130295232, "area": 1627.9742729498},
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
