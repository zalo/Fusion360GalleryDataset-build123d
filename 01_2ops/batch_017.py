"""Batch 017 - passing/01_2ops
181 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a hexahedron-like solid body with an irregular, elongated shape featuring multiple faceted surfaces in dark and light blue tones, with angular edges and what appears to be internal geometric complexity or cavities visible through the transparent rendering.
def model_73091_ce795f51_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.5, perimeter: 31
            with BuildLine():
                Line((6.5, -2.5), (-4, -2.5))
                Line((6.5, 2.5), (6.5, -2.5))
                Line((-4, 2.5), (6.5, 2.5))
                Line((-4, -2.5), (-4, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a torus or donut-shaped ring featuring a smooth, curved elliptical cross-section with a textured surface pattern and a hollow center opening.
def model_73388_10a40b49_0000():
    """Model: Small_Comp_Washer_0.5_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.95, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0773208757, perimeter: 2.1359459871
            with BuildLine():
                CenterArc((-2.6334135433, -1.3514266888), 0.2061730082, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.6334135433, -1.3514266888), 0.1337733538, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.018
        extrude(amount=0.018)
    return part.part


# Description: This is a cylindrical bearing or bushing with a hollow center bore, featuring a ribbed or textured outer surface with radial fins/grooves that run along the length of the component.
def model_73388_10a40b49_0006():
    """Model: T3_Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.4715530573, perimeter: 4.9637163927
            with BuildLine():
                CenterArc((0, 0), 0.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.395, against=-0.055
        extrude(amount=0.395)
        extrude(sk.sketch, amount=-0.055)
    return part.part


# Description: This is a cylindrical filter or strainer component with a hollow core, featuring a mesh or perforated surface pattern on its outer walls and a large central bore, designed for fluid or air filtration applications.
def model_73388_10a40b49_0007():
    """Model: spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a solid torus (donut-shaped ring) with a textured mesh surface finish applied to its outer surfaces, featuring a uniform circular cross-section and a central hollow opening.
def model_73388_10a40b49_0009():
    """Model: 2M_Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4715530573, perimeter: 4.9637163927
            with BuildLine():
                CenterArc((0, 0), 0.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.24
        extrude(amount=0.24)
    return part.part


# Description: This is a torus-shaped ring with a circular cross-section, featuring a smooth outer surface and a hollow center, commonly used as a seal, gasket, or structural component.
def model_73388_10a40b49_0010():
    """Model: compression_washer_1.4m_2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5011900196, perimeter: 5.4119071083
            with BuildLine():
                CenterArc((0, 0), 0.5, 90.4596430435, 359.080713913)
                Line((0.0040110992, 0.4999839108), (0.003217109, 0.2999827499))
                CenterArc((0, 0), 0.3, 90.6509950088, 358.7345706465)
                Line((-0.0040110992, 0.4999839108), (-0.0034085286, 0.2999806359))
            make_face()
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore and multiple rectangular slots or cutouts evenly distributed around its outer surface, creating a mesh-like or perforated pattern.
def model_73388_10a40b49_0012():
    """Model: M5_Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.4715530573, perimeter: 4.9637163927
            with BuildLine():
                CenterArc((0, 0), 0.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.55, against=-0.055
        extrude(amount=0.55)
        extrude(sk.sketch, amount=-0.055)
    return part.part


# Description: This is a cylindrical bushing or spacer with a hollow central bore, featuring a rounded, domed top surface and a uniform tubular body design with a through-hole for shaft or fastener passage.
def model_73388_10a40b49_0020():
    """Model: 6M_Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4715530573, perimeter: 4.9637163927
            with BuildLine():
                CenterArc((0, 0), 0.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.64
        extrude(amount=0.64)
    return part.part


# Description: This is a washer or ring gasket – a flat, donut-shaped component with a large central hole and uniform thickness, characterized by its circular outer and inner edges.
def model_73388_10a40b49_0021():
    """Model: Washer_0.2_mm_4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4260785036, perimeter: 4.8694686131
            with BuildLine():
                CenterArc((0, 0), 0.475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


# Description: This is a friction ring or washer with a toroidal (donut) shape, featuring a smooth dark gray body with textured grip surfaces on the inner and outer edges for enhanced friction and traction.
def model_73388_10a40b49_0022():
    """Model: Washer_1_mm_2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4260785036, perimeter: 4.8694686131
            with BuildLine():
                CenterArc((0, 0), 0.475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore and a mesh or perforated pattern covering portions of its outer surface, featuring a solid flanged section on one end.
def model_73388_10a40b49_0024():
    """Model: Chain_Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4715530573, perimeter: 4.9637163927
            with BuildLine():
                CenterArc((0, 0), 0.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or bushing with a hollow circular center and textured surface finish, commonly used as a bearing, spacer, or sealing component in mechanical assemblies.
def model_73388_10a40b49_0028():
    """Model: T2_Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4715530573, perimeter: 4.9637163927
            with BuildLine():
                CenterArc((0, 0), 0.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.34
        extrude(amount=0.34)
    return part.part


# Description: This is a torus or ring-shaped seal/gasket featuring a uniform circular cross-section with a smooth, rounded outer surface and a continuous hollow center opening.
def model_74148_8ce0be94_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1362830044, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a long, slender hexagonal rod or shaft with a uniform cross-section and straight cylindrical geometry, featuring a slightly tapered or beveled end at the top.
def model_74667_3504f3e1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.8064, perimeter: 20.32
            with BuildLine():
                Line((5.08, -5.08), (0, -5.08))
                Line((5.08, 0), (5.08, -5.08))
                Line((0, 0), (5.08, 0))
                Line((0, -5.08), (0, 0))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


# Description: This is a parallelogram-shaped flat plate or sheet metal part with a diagonal internal line or fold, suggesting it may be a bent or two-faced planar component with a simple geometric form and no holes or additional features.
def model_74722_43175bd2_0000():
    """Model: Component22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 89.9617681939, perimeter: 38.1756551318
            with BuildLine():
                Line((8.3108499867, 6.584560672), (8.3108499867, -4.0197879758))
                Line((8.3108499867, -4.0197879758), (16.7943289049, -4.0197879758))
                Line((16.7943289049, -4.0197879758), (16.7943289049, 6.584560672))
                Line((16.7943289049, 6.584560672), (8.3108499867, 6.584560672))
            make_face()
        # OneSide extrude, distance=0.0751
        extrude(amount=0.0751)
    return part.part


# Description: This is an oval or elliptical disk/wheel with a ribbed or finned outer edge, featuring a smooth curved face with diagonal surface patterns and a hollow or recessed center section.
def model_74811_83a8fddf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Rueda Ppal -> Rueda Ppal (1) (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 201.0619298297, perimeter: 50.2654824574
            Circle(8)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


# Description: This is a tapered sleeve or ferrule with an elongated, cone-like shape that narrows from a wider cylindrical body to a pointed tip, featuring longitudinal ribbing or grooves along its length and a flat mounting base at the rear end.
def model_75032_945d0803_0001():
    """Model: perm_magnet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1805630378, perimeter: 2.7075071702
            with BuildLine():
                CenterArc((0, 0), 2.374, 57, 30)
                Line((0.1163951667, 2.2209520853), (0.1242455601, 2.3707465155))
                CenterArc((0, 0), 2.224, 57, 30)
                Line((1.2929730691, 1.9910039283), (1.2112772139, 1.8652033431))
            make_face()
        # TwoSides extrude, along=1.7, against=-1.05
        extrude(amount=1.7)
        extrude(sk.sketch, amount=-1.05)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a dark gray body and a blue textured top surface, featuring a hollow tubular design with rounded edges and a slightly tapered or curved profile.
def model_75646_4baf69b2_0010():
    """Model: ????? v1"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            Circle(2.4)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a hexagonal geometric solid with a large central elliptical void, featuring triangular faceted surfaces and linear surface patterns that create a complex, abstract architectural or decorative form.
def model_75646_4baf69b2_0011():
    """Model: ????? v2"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.1894362492, perimeter: 19.6386882466
            with BuildLine():
                Line((0, 3.5), (0, 1.75))
                CenterArc((0, 0), 1.75, -90, 180)
                Line((0, -1.75), (0, -3))
                Line((2.5, -3), (0, -3))
                Line((3.5, 1.5), (2.5, -3))
                Line((0, 3.5), (3.5, 1.5))
            make_face()
            # Profile area: 12.1894362492, perimeter: 19.6386882466
            with BuildLine():
                Line((-3.5, 1.5), (-2.5, -3))
                Line((-2.5, -3), (0, -3))
                Line((0, -1.75), (0, -3))
                CenterArc((0, 0), 1.75, 90, 180)
                Line((0, 3.5), (0, 1.75))
                Line((0, 3.5), (-3.5, 1.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)
    return part.part


# Description: This is a cylindrical barrel or sleeve with rounded ends, featuring a central longitudinal bore or hollow core, and what appears to be internal or external ribbed/textured surface details along its length.
def model_75646_4baf69b2_0012():
    """Model: ??????? v1"""
    with BuildPart() as part:
        # Sketch2 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-10
        extrude(amount=-10)
    return part.part


# Description: This is a modern lounge chair or chaise with a curved, sculptural frame featuring a high angled backrest and extended seat platform, constructed from a lattice or mesh structural framework in dark material with blue surface elements.
def model_75990_213a7354_0000():
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
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 238.6857769553, perimeter: 230.8194390353
            with BuildLine():
                _nurbs_edge([(33.1212319865, 13.5452677239), (32.6915849518, 13.2426857983), (31.823260409, 12.6207052531), (30.4936815909, 11.6372836757), (28.6663368324, 10.2244255706), (26.2915991311, 8.2880395682), (23.8318237086, 6.1864975911), (21.301386926, 3.9363418287), (18.7284299621, 1.5724616619), (16.1584462033, -0.8465377645), (13.6627538511, -3.2263787818), (11.3296061135, -5.4477933109), (9.2416851884, -7.394823414), (7.4578609877, -8.9774334443), (5.9901962771, -10.1598232304), (4.7846547747, -10.9843645827), (3.9064706825, -11.4872504059), (3.2190683727, -11.860477711), (2.7361895107, -12.1206204155), (2.4885915146, -12.253529672)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-26.2478765279, -3.9088806023), (-25.9375007321, -3.9110485914), (-25.3056072532, -3.9253171758), (-24.3243400326, -3.9765189516), (-22.9486552569, -4.1048097127), (-21.1160770406, -4.3665005725), (-19.1736616147, -4.7286018455), (-17.1315425398, -5.1858412784), (-15.0120530121, -5.7247339796), (-12.849731059, -6.3239774728), (-10.6841042375, -6.9607597678), (-8.5546399915, -7.6152756465), (-6.4948046393, -8.2759778282), (-4.5265376797, -8.9443750523), (-2.653364622, -9.6410439866), (-0.8667164116, -10.3976426465), (0.504518213, -11.078030523), (1.5062069522, -11.6430468157), (2.1629684434, -12.0457051286), (2.4885915146, -12.253529672)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-26.2478765279, -5.9088806023), (-26.2478765279, -3.9088806023))
                _nurbs_edge([(-26.2478765279, -5.9088806023), (-25.9485695691, -5.9125513581), (-25.339524487, -5.9288240021), (-24.3946624921, -5.9800270179), (-23.0718102655, -6.1022697565), (-21.3126705531, -6.3461013745), (-19.4514216863, -6.6799277466), (-17.4987307863, -7.0984943591), (-15.4772360817, -7.5890287992), (-13.4233641633, -8.130199163), (-11.3792847695, -8.6986419046), (-9.3870920148, -9.2737351954), (-7.4817557757, -9.8433667078), (-5.685240338, -10.4085682435), (-3.9971161398, -10.9912313699), (-2.400109609, -11.6276732365), (-1.1766112987, -12.2112466025), (-0.2798353802, -12.7053543489), (0.3100867386, -13.0617761855), (0.603066023, -13.2467416981)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.603066023, -13.2467416981), (0.1361101346, -13.4695103535), (-0.8012930629, -13.9031546372), (-2.2178717281, -14.5179441442), (-4.1245415666, -15.2667477441), (-6.5204473403, -16.0855157934), (-8.9066377787, -16.7868101505), (-11.2603659367, -17.3698981705), (-13.5623143003, -17.8349794344), (-15.8029633589, -18.1879157278), (-17.9809600855, -18.4382514467), (-19.6748267223, -18.5634765426), (-20.9192041645, -18.6179529762), (-21.7374086097, -18.6370232029), (-22.1436658314, -18.6422465349)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-22.1436658314, -18.6422465349), (-22.14090089, -20.6422446237))
                _nurbs_edge([(2.9023804813, -14.682023314), (2.709434001, -14.778765724), (1.8708247633, -15.1927910271), (0.3597106331, -15.8903741575), (-1.8635936784, -16.8032990947), (-4.8088286457, -17.8314172072), (-8.1969026389, -18.8074276219), (-11.4543801087, -19.5733581498), (-14.5114943541, -20.1380422025), (-17.331014897, -20.5087829319), (-19.383404643, -20.6546080355), (-20.8069791184, -20.6806853127), (-21.7047983427, -20.6612027768), (-22.14090089, -20.6422446237)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5849699378, 0.5849699378, 0.5849699378, 0.5849699378, 0.5849699378, 0.5849699378, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(2.9023804813, -14.682023314), (3.2419954395, -14.8982869976), (3.9283407957, -15.3199955478), (4.9792041527, -15.9201037685), (6.4189969291, -16.6571645966), (8.2605616268, -17.4825211093), (10.1151435728, -18.2226216437), (11.9534747677, -18.8880327749), (13.7505863261, -19.4883709736), (15.4930268183, -20.032813135), (17.1770095109, -20.529342746), (18.4779683117, -20.8928524373), (19.4287288352, -21.1480177476), (20.0516536731, -21.3104906893), (20.3603873558, -21.389817831)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((20.3603873558, -19.6254554639), (20.3603873558, -21.389817831))
                _nurbs_edge([(4.7528684256, -13.6957137705), (5.0989164181, -13.9113685732), (5.8080549909, -14.3314444556), (6.9228852003, -14.9278586449), (8.5006214953, -15.6571357579), (10.5607095703, -16.4654180125), (12.6221250188, -17.1770907236), (14.5878652269, -17.7974124785), (16.3628228473, -18.3298861831), (17.8653953853, -18.7767528186), (19.0468500254, -19.1411564575), (19.7305098912, -19.3710567559), (20.1001531618, -19.5107662975), (20.2840643067, -19.5896088966), (20.3603873558, -19.6254554639)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(34.6507153159, 11.7098877286), (34.2395606354, 11.4231438368), (33.4065891334, 10.8318261398), (32.125144975, 9.8913593328), (30.3521179197, 8.5296497148), (28.0285307237, 6.6466506235), (25.6029684154, 4.587364567), (23.0900629471, 2.3675818763), (20.5189625795, 0.0212235571), (17.9374541429, -2.3939785256), (15.42053521, -4.7850980621), (13.0664940254, -7.0280519789), (10.970929552, -8.9987895705), (9.207348019, -10.5963445127), (7.7999447459, -11.774812151), (6.706316974, -12.5640972585), (5.9575395693, -13.0121738063), (5.3755612208, -13.3426785287), (4.9643214944, -13.5758770409), (4.7528684256, -13.6957137705)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((33.1212319865, 13.5452677239), (34.6507153159, 11.7098877286))
            make_face()
        # OneSide extrude, distance=-34
        extrude(amount=-34)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal block with a slanted or beveled top surface, featuring a uniform extruded body with six vertical sides and a tapered upper face.
def model_76278_13dd168d_0006():
    """Model: qfn48 v2"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.001, perimeter: 0.14
            with BuildLine():
                Line((-0.03, -0.26), (-0.03, -0.31))
                Line((-0.03, -0.31), (-0.01, -0.31))
                Line((-0.01, -0.31), (-0.01, -0.26))
                Line((-0.01, -0.26), (-0.03, -0.26))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight 3D depth, featuring clean edges and a uniform rectangular form with a skewed geometry.
def model_76278_13dd168d_0007():
    """Model: mainproc"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.17, perimeter: 5.9
            with BuildLine():
                Line((-3.25, 0.9), (-1.85, 0.9))
                Line((-3.25, -0.65), (-3.25, 0.9))
                Line((-1.85, -0.65), (-3.25, -0.65))
                Line((-1.85, 0.9), (-1.85, -0.65))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with four corner mounting holes and internal cross-bracing or ribbing visible on its surface.
def model_76278_13dd168d_0008():
    """Model: pcb"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 79 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 48.3475026556, perimeter: 34.3398223702
            with BuildLine():
                Line((-3.85, 2.95), (-3.15, 2.95))
                CenterArc((-3.85, 2.65), 0.3, 90, 90)
                Line((-4.15, 2.25), (-4.15, 2.65))
                Line((-4.1, 2.25), (-4.15, 2.25))
                Line((-4.1, 1.9474399387), (-4.1, 2.25))
                Line((-4.15, 1.9474399387), (-4.1, 1.9474399387))
                Line((-4.15, -1.9474399387), (-4.15, 1.9474399387))
                Line((-4.1, -1.9474399387), (-4.15, -1.9474399387))
                Line((-4.1, -2.25), (-4.1, -1.9474399387))
                Line((-4.15, -2.25), (-4.1, -2.25))
                Line((-4.15, -2.65), (-4.15, -2.25))
                CenterArc((-3.85, -2.65), 0.3, 179.9999999999, 89.9999999998)
                Line((-3.15, -2.95), (-3.85, -2.95))
                Line((-3.15, -2.9), (-3.15, -2.95))
                Line((-2.85, -2.9), (-3.15, -2.9))
                Line((-2.85, -2.95), (-2.85, -2.9))
                Line((2.85, -2.95), (-2.85, -2.95))
                Line((2.85, -2.9), (2.85, -2.95))
                Line((3.15, -2.9), (2.85, -2.9))
                Line((3.15, -2.9500000002), (3.15, -2.9))
                Line((3.8500000006, -2.9500000003), (3.15, -2.9500000002))
                CenterArc((3.8500000006, -2.6500000003), 0.3, -90.0000000039, 90.0000000176)
                Line((4.1500000005, -2.25), (4.1500000006, -2.6500000002))
                Line((4.1, -2.25), (4.1500000005, -2.25))
                Line((4.1, -1.9413033044), (4.1, -2.25))
                Line((4.15, -1.9413033044), (4.1, -1.9413033044))
                Line((4.15, 1.9413033044), (4.15, -1.9413033044))
                Line((4.1, 1.9413033044), (4.15, 1.9413033044))
                Line((4.1, 2.25), (4.1, 1.9413033044))
                Line((4.15, 2.25), (4.1, 2.25))
                Line((4.15, 2.65), (4.15, 2.25))
                CenterArc((3.85, 2.65), 0.3, 0, 90)
                Line((3.15, 2.95), (3.85, 2.95))
                Line((3.15, 2.9), (3.15, 2.95))
                Line((2.85, 2.9), (3.15, 2.9))
                Line((2.85, 2.95), (2.85, 2.9))
                Line((-2.85, 2.95), (2.85, 2.95))
                Line((-2.85, 2.9), (-2.85, 2.95))
                Line((-3.15, 2.9), (-2.85, 2.9))
                Line((-3.15, 2.95), (-3.15, 2.9))
            make_face()
            with BuildLine():
                CenterArc((-1.311, 1.25), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8, -0.7500000003), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8, -2.6), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8, 2.6), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.8, -2.6), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.8, 2.6), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat, ring-shaped washer or spacer with a circular outer diameter, a central hole, and a textured or knurled surface on its edges for grip or identification purposes.
def model_76298_af8ea172_0018():
    """Model: Lock Screw Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8707202504, perimeter: 8.089601083
            with BuildLine():
                CenterArc((0, 0), 0.875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a curved blade or fin component with a rectangular base that tapers and curves upward, featuring a smooth aerodynamic profile with diagonal ribbing or reinforcement lines along its surface.
def model_76298_af8ea172_0025():
    """Model: Spring v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1347822088, perimeter: 5.491288351
            with BuildLine():
                Line((1.3030296452, 1.0918396145), (0.4525510431, 1.3723055612))
                CenterArc((0, 0), 1.445, 71.7487749034, 36.4991480773)
                Line((-1.3029667173, 1.0919147099), (-0.4524719525, 1.3723316407))
                Line((-1.3029667173, 1.0919147099), (-1.2873102483, 1.044429186))
                Line((-1.2873102483, 1.044429186), (-0.4368154836, 1.3248461168))
                CenterArc((0, 0), 1.395, 71.7487749034, 36.4991480773)
                Line((1.2873704396, 1.044354993), (0.4368918374, 1.3248209397))
                Line((1.3030296452, 1.0918396145), (1.2873704396, 1.044354993))
            make_face()
        # OneSide extrude, distance=0.51
        extrude(amount=0.51)
    return part.part


# Description: This is a wing or airfoil component with a tapered, streamlined shape featuring a pointed leading edge, internal ribbed/truss-like structure for weight reduction, and a flat base surface for mounting or assembly.
def model_76666_8c3d34c0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9, perimeter: 10.9286927533
            with BuildLine():
                Line((5, 7), (0.5, 4))
                Line((0.5, 4), (1.1, 4))
                Line((1.1, 4), (5, 7))
            make_face()
            # Profile area: 1.4605769231, perimeter: 9.7213527771
            with BuildLine():
                Line((2.3346153846, 3.1923076923), (1.5, 2))
                Line((1.5, 2), (1.5, -1.5))
                Line((2.3346153846, 3.1923076923), (1.5, -1.5))
            make_face()
            # Profile area: 2.8499998838, perimeter: 14.0000000298
            with BuildLine():
                Line((1.5, 2), (1.5, -1.5))
                Line((0, 2), (1.5, 2))
                Line((0, 2), (0, 1.7000000253))
                Line((0, 1.7000000253), (1.0000000149, 1.7000000253))
                Line((1.0000000149, 1.7000000253), (1.0000000149, -2.2000000328))
                Line((1.0000000149, -2.2000000328), (0, -2.2000000328))
                Line((0, -2.2000000328), (0, -2.5))
                Line((1.5, -2.5), (0, -2.5))
                Line((1.5, -1.5), (1.5, -2.5))
            make_face()
            # Profile area: 1.467256704, perimeter: 10.6652673271
            with BuildLine():
                Line((-1.5000000224, -2.0000000298), (-1.5, 2))
                Line((-1.5, 2), (-2.5000000373, -1.0000000149))
                Line((-2.5000000373, -1.0000000149), (-2.0000000186, -1.0000000149))
                Line((-2.0000000186, -1.0000000149), (-1.5000000224, -2.0000000298))
            make_face()
            with BuildLine():
                CenterArc((-1.9000000283, -0.6000000089), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.8499998838, perimeter: 14.0000000298
            with BuildLine():
                Line((0, -2.2000000328), (0, -2.5))
                Line((0, -2.2000000328), (-1.0000000149, -2.2000000328))
                Line((-1.0000000149, -2.2000000328), (-1.0000000149, 1.7000000253))
                Line((-1.0000000149, 1.7000000253), (0, 1.7000000253))
                Line((0, 2), (0, 1.7000000253))
                Line((-1.5, 2), (0, 2))
                Line((-1.5000000224, -2.0000000298), (-1.5, 2))
                Line((-1.5, -2.5), (-1.5000000224, -2.0000000298))
                Line((0, -2.5), (-1.5, -2.5))
            make_face()
            # Profile area: 5.538461572, perimeter: 25.8669643375
            with BuildLine():
                Line((5, 7), (3.25, 4.5))
                Line((1.1, 4), (5, 7))
                Line((-1.5, 2), (1.1, 4))
                Line((-1.5, 2), (0, 2))
                Line((0, 2), (1.5, 2))
                Line((2.3346153846, 3.1923076923), (1.5, 2))
                Line((3.25, 4.5), (2.3346153846, 3.1923076923))
            make_face()
            with BuildLine():
                Line((3.5, 5.5), (1.3000000194, 2.5000000373))
                Line((1.3000000194, 2.5000000373), (0.5, 3.1923076923))
                Line((3.5, 5.5), (0.5, 3.1923076923))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.475885108, perimeter: 12.0274335343
            with BuildLine():
                Line((-1.0000000149, 1.7000000253), (0, 1.7000000253))
                Line((-1.0000000149, -2.2000000328), (-1.0000000149, 1.7000000253))
                Line((0, -2.2000000328), (-1.0000000149, -2.2000000328))
                Line((0, -1.0000000104), (0, -2.2000000328))
                CenterArc((0, -0.7000000104), 0.3, 90, 180)
                Line((0, 1.7000000253), (0, -0.4000000104))
            make_face()
            with BuildLine():
                CenterArc((-0.5000000075, -1.5000000224), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.475885108, perimeter: 12.0274335343
            with BuildLine():
                Line((0, 1.7000000253), (0, -0.4000000104))
                CenterArc((0, -0.7000000104), 0.3, -90, 180)
                Line((0, -1.0000000104), (0, -2.2000000328))
                Line((1.0000000149, -2.2000000328), (0, -2.2000000328))
                Line((1.0000000149, 1.7000000253), (1.0000000149, -2.2000000328))
                Line((0, 1.7000000253), (1.0000000149, 1.7000000253))
            make_face()
            with BuildLine():
                CenterArc((0.5000000075, -1.5000000224), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.75, perimeter: 6.9647578646
            with BuildLine():
                Line((3.5, 4), (3.25, 4.5))
                Line((5, 7), (3.5, 4))
                Line((5, 7), (3.25, 4.5))
            make_face()
            # Profile area: 1.961538428, perimeter: 8.5630767962
            with BuildLine():
                Line((3.5, 5.5), (0.5, 3.1923076923))
                Line((1.3000000194, 2.5000000373), (0.5, 3.1923076923))
                Line((3.5, 5.5), (1.3000000194, 2.5000000373))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a flat, circular washer or spacer with a large central hole, featuring an annular (ring-shaped) body tilted in an isometric view.
def model_76880_9bb28e72_0001():
    """Model: board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.7264365479, perimeter: 19.1637151869
            with BuildLine():
                CenterArc((0, 0), 2.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)
    return part.part


# Description: This is a hexagonal or polygonal prism-like component with an irregular, asymmetrical shape featuring multiple flat faces at varying angles, creating a complex geometric form with no apparent holes, slots, or curves—primarily composed of planar surfaces that meet at sharp edges.
def model_77211_d46ae17d_0000():
    """Model: scaffalatura-bassa2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34, perimeter: 25
            with BuildLine():
                Line((0, 4), (0, 0))
                Line((0, 0), (8.5, 0))
                Line((8.5, 0), (8.5, 4))
                Line((8.5, 4), (0, 4))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a rectangular prism or box-shaped part with a faceted/pyramidal top surface, featuring a hollow or recessed interior visible on the left side, and clean vertical sides with a geometric, industrial design.
def model_77211_d46ae17d_0001():
    """Model: esagono"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7942916866, perimeter: 10.3923468804
            with BuildLine():
                Line((0.8702917489, 1.4975368245), (-0.8617590587, 1.5024631755))
                Line((-0.8617590587, 1.5024631755), (-1.7320508076, 0.004926351))
                Line((-1.7320508076, 0.004926351), (-0.8702917489, -1.4975368245))
                Line((-0.8702917489, -1.4975368245), (0.8617590587, -1.5024631755))
                Line((0.8617590587, -1.5024631755), (1.7320508076, -0.004926351))
                Line((1.7320508076, -0.004926351), (0.8702917489, 1.4975368245))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a rectangular base and angled top face, featuring internal diagonal reinforcement or structural geometry.
def model_77211_d46ae17d_0002():
    """Model: parallelepipedo1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (3, 0))
                Line((3, 0), (3, 3))
                Line((3, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped polyhedron with an irregular geometric form, featuring multiple planar faces in varying shades of blue and dark gray, suggesting a complex 3D solid with angled surfaces and possible internal geometry or cutouts.
def model_77211_d46ae17d_0003():
    """Model: pedana-ortofrutta2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72, perimeter: 36
            with BuildLine():
                Line((0, 6), (0, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (12, 6))
                Line((12, 6), (0, 6))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a sheet metal enclosure or housing with a trapezoidal/wedge-shaped profile, featuring angled side panels, a sloped top surface, and what appears to be an open or partially enclosed design with minimal features.
def model_77211_d46ae17d_0005():
    """Model: scaffalatura-bassa1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 51, perimeter: 40
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (17, 0))
                Line((17, 0), (17, 3))
                Line((17, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a pentagonal or wedge-shaped solid with angular faceted surfaces, featuring a trapezoidal top face and triangulated internal geometry, appearing to be a geometric structural component or bracket with no visible holes or slots.
def model_77211_d46ae17d_0007():
    """Model: vetrina"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 112.2, perimeter: 49.4
            with BuildLine():
                Line((0, 18.7), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 18.7))
                Line((6, 18.7), (0, 18.7))
            make_face()
        # OneSide extrude, distance=22.2
        extrude(amount=22.2)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal tube with a tapered or wedge-like top end, featuring parallel longitudinal edges and a slanted upper face that narrows toward one side.
def model_77211_d46ae17d_0008():
    """Model: frigorifero"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0, 6), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 6))
                Line((6, 6), (0, 6))
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22)
    return part.part


# Description: This is a rectangular flat panel or plate with a slightly curved or warped surface, featuring a central vertical seam or ridge line running along its length, tilted at an angle in 3D space.
def model_77211_d46ae17d_0011():
    """Model: specchio3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 72, perimeter: 36
            with BuildLine():
                Line((0, 12), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 12))
                Line((6, 12), (0, 12))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a hexagonal or wedge-shaped box/container with a sloped top surface, featuring a hollow interior cavity and angular faceted geometry with flat side panels and triangulated surface divisions.
def model_77211_d46ae17d_0012():
    """Model: pedana-ortofrutta-1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 108, perimeter: 42
            with BuildLine():
                Line((0, 9), (0, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (12, 9))
                Line((12, 9), (0, 9))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a rectangular prism or box-like component with a parallelogram-based extruded shape, featuring angled or skewed geometry and what appears to be a diagonal slot or cutout running along one of its faces.
def model_77211_d46ae17d_0014():
    """Model: scaffalatura-alta"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 22
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (8, 0))
                Line((8, 0), (8, 3))
                Line((8, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17)
    return part.part


# Description: This is a structural bracket or support arm with an elongated, angled tubular body featuring two parallel rails, a reinforcing triangular base flange at the bottom, and mounting holes at both ends.
def model_77306_fe3133f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 87.4298710116, perimeter: 103.1327211219
            with BuildLine():
                CenterArc((8.3939809578, 21.2128553164), 0.3, -14.0362434679, 106.05520866)
                CenterArc((8.4889687728, 21.2318528794), 0.3, 110.6008997559, 38.435343712)
                Line((8.0793408008, 21.1322347823), (8.2317208951, 21.386201606))
                CenterArc((7.8220929231, 21.2865835089), 0.3, -85.3732768285, 54.4095202964)
                Line((1.4397241675, 20.4690933586), (7.8462920693, 20.9875610995))
                CenterArc((1.2783965264, 22.4625760879), 2, -114.8325891035, 29.459312275)
                CenterArc((0, 19.7000002936), 1.0440306664, 65.1674108965, 98.1333449164)
                CenterArc((50.9189550035, 1.9556451293), 54.9652312253, 160.8351810185, 20.8953204173)
                CenterArc((-3.7213448117, 0.3048450143), 0.3, -178.2694985641, 88.2694985641)
                Line((-3.6000000536, 0.0048450143), (-3.7213448117, 0.0048450143))
                CenterArc((0.9279421852, -19.5809473343), 20.1023760496, 76.9215988655, 26.0956355312)
                CenterArc((5.4767908673, 0.3), 0.3, -90, 73.300755766)
                Line((5.7641387529, 0.2137956343), (5.7942329188, 0.3141095208))
                CenterArc((5.5068850333, 0.4003138864), 0.3, -16.699244234, 85.4577483593)
                Line((5.6155749436, 0.6799323826), (1.9100993785, 2.1202799002))
                CenterArc((2.6346987805, 3.984403208), 2, -171.6778624072, 60.4363665325)
                CenterArc((27.8300138232, 7.6699447203), 27.4634466704, 160.1429448016, 28.1791927912)
                CenterArc((4.4193549046, 16.0806454009), 2.5881443844, 110.8067910127, 48.419995978)
                Line((8.3535262867, 20.3443402448), (3.5000000522, 18.5000002757))
                CenterArc((8.2469609585, 20.624775319), 0.3, -69.1932089873, 55.1569655194)
                Line((8.6850237079, 21.1400946289), (8.5380037085, 20.5520146315))
            make_face()
            with BuildLine():
                CenterArc((0, 19.7000002936), 0.405, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.2000000477, 1.3000000194), 0.405, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((36.0391426282, 5.9659518315), 37.285450063, 162.9770646065, 20.0128672975)
                CenterArc((-1.6000000238, 4.0000000596), 0.405, -177.010068096, 179.9999987926)
                CenterArc((36.0391426282, 5.9659518315), 38.095450063, 162.9770646065, 20.0128672975)
                CenterArc((0, 17.0000002533), 0.405, -17.0229353935, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a bracket or support component with a rectangular body featuring an open U-shaped slot running vertically through its center, two flat flanges at the top, and diagonal ribbing or reinforcement structures on the inner surfaces for added strength.
def model_77397_df713db5_0004():
    """Model: Component E"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 93.003251074, perimeter: 47.4699572125
            with BuildLine():
                Line((4.0987803064, 4.5), (4.55, 4.5))
                Line((4.55, 4.5), (4.55, 8.9))
                Line((4.55, 8.9), (4.25, 8.9))
                Line((4.25, 8.9), (4.25, 10.9))
                Line((4.25, 10.9), (4.55, 10.9))
                Line((4.55, 10.9), (4.55, 16.9))
                Line((4.55, 16.9), (1, 16.9))
                Line((1, 16.9), (1, 16.6))
                Line((1, 16.6), (-1, 16.6))
                Line((-1, 16.6), (-1, 16.9))
                Line((-1, 16.9), (-4.55, 16.9))
                Line((-4.55, 16.9), (-4.55, 10.9))
                Line((-4.55, 10.9), (-4.25, 10.9))
                Line((-4.25, 10.9), (-4.25, 8.9))
                Line((-4.25, 8.9), (-4.55, 8.9))
                Line((-4.55, 8.9), (-4.55, 4.5))
                Line((-4.55, 4.5), (-4.0987803064, 4.5))
                CenterArc((0, 3.2), 4.3, 17.5973366081, 144.8053267838)
            make_face()
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)
    return part.part


# Description: This is a rounded hexagonal or cylindrical housing component with a flat top surface featuring a triangular cutout or opening, designed as an enclosure or connector shell with smoothly curved sides and a polygonal base.
def model_77686_b1e8a0fa_0002():
    """Model: Render Box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6056.6370614359, perimeter: 302.8318530718
            with BuildLine():
                CenterArc((40, 40), 40, 0, 90)
                Line((40, 80), (0, 80))
                Line((0, 80), (0, 0))
                Line((0, 0), (80, 0))
                Line((80, 0), (80, 40))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


# Description: This is a triangular or trapezoidal sheet metal component with a tapered wedge shape, featuring a flat base and sloped upper surface that converges to a point or edge, likely designed as an aerodynamic fairing, deflector, or structural bracket.
def model_78288_d264181d_0001():
    """Model: Light Sword Rendering-1 v9"""
    with BuildPart() as part:
        # 握把剖面草圖 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 62 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3273428445, perimeter: 3.6187027022
            with BuildLine():
                Line((12.5, 2.3346179987), (11.9748359791, 2.6621343014))
                Line((11.9748359791, 2.6621343014), (10.7954513404, 2.1510216166))
                Line((10.7954513404, 2.1510216166), (12.5, 2.3346179987))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a vertical mounting bracket or clamp with a U-shaped channel base, an upright arm, and a hook or grip feature at the top for securing or holding cylindrical objects or cables.
def model_78422_3d6c0e4e_0003():
    """Model: Component14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.6464784585, perimeter: 35.5220224794
            with BuildLine():
                Line((20.3838323172, 25.9757949368), (19.3838323172, 18.4757949368))
                Line((19.3838323172, 18.4757949368), (22.9838323172, 18.4757949368))
                Line((22.9838323172, 18.4757949368), (22.3132830901, 23.5049141401))
                CenterArc((22.065476115, 23.4718732101), 0.25, 7.5946433686, 270)
                Line((22.6516198847, 19.0757949368), (22.098517045, 23.2240662349))
                Line((19.7160447498, 19.0757949368), (22.6516198847, 19.0757949368))
                Line((20.6027114164, 25.7257949368), (19.7160447498, 19.0757949368))
                Line((20.6027114164, 25.7257949368), (21.7649532181, 25.7257949368))
                Line((21.7890929443, 25.5447469904), (21.7649532181, 25.7257949368))
                CenterArc((22.0368999194, 25.5777879204), 0.25, -172.4053566314, 270)
                Line((22.0038589894, 25.8255948956), (21.9838323172, 25.9757949368))
                Line((20.3838323172, 25.9757949368), (21.9838323172, 25.9757949368))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a flat parallelogram-shaped sheet metal or plate part with a slight 3D depth, featuring clean edges and a simple geometric form with no holes, slots, or additional features.
def model_78422_3d6c0e4e_0004():
    """Model: Wall"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8221.1194617631, perimeter: 614.3427492219
            with BuildLine():
                Line((-72.2933570176, 30), (-72.2933570176, 0.3798074232))
                Line((-72.2933570176, 0.3798074232), (205.2578250166, 0.3798074232))
                Line((205.2578250166, 0.3798074232), (205.2578250166, 30))
                Line((205.2578250166, 30), (-72.2933570176, 30))
            make_face()
        # OneSide extrude, distance=270
        extrude(amount=270)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring featuring a hollow center and a textured mesh or lattice pattern covering portions of its outer surface, with solid dark gray sections alternating around the circumference.
def model_78513_7ad0bd6a_0000():
    """Model: tire"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 57.6796411199, perimeter: 64.0884901332
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.65
        extrude(amount=1.65, both=True)
    return part.part


# Description: A hollow cylindrical sleeve with a smooth outer surface and internal bore, featuring grooved or textured bands along its length, designed for use as a spacer or bushing component.
def model_78513_7ad0bd6a_0005():
    """Model: bussing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9792033718, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


# Description: This is a satellite dish or parabolic reflector antenna featuring an elliptical dish surface with radial ribs for structural reinforcement and a peripheral rim flange.
def model_78600_3f295e84_0001():
    """Model: Bottom ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexagonal or octagonal prism-like polyhedron with a truncated or beveled top surface, featuring multiple angled faces and a roughly trapezoidal profile when viewed from the side.
def model_78603_4720dcb8_0006():
    """Model: Eraser"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.91, perimeter: 4
            with BuildLine():
                Line((-1.3, 0.7), (0, 0.7))
                Line((-1.3, 0), (-1.3, 0.7))
                Line((0, 0), (-1.3, 0))
                Line((0, 0.7), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a truncated polyhedron or chamfered rectangular block featuring a primarily rectangular base with beveled/faceted edges and corners, creating an angular, geometric form with multiple triangular and polygonal faces.
def model_78687_39a896db_0023():
    """Model: Bolt M5 v1 (8)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4243524479, perimeter: 2.4248711306
            with BuildLine():
                Line((0.35, -0.2020725942), (0.35, 0.2020725942))
                Line((0.35, 0.2020725942), (0, 0.4041451884))
                Line((0, 0.4041451884), (-0.35, 0.2020725942))
                Line((-0.35, 0.2020725942), (-0.35, -0.2020725942))
                Line((-0.35, -0.2020725942), (0, -0.4041451884))
                Line((0, -0.4041451884), (0.35, -0.2020725942))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a 3D CAD representation of a needle or stylus with a long, thin cylindrical shaft, a small spherical node or joint near the center, and a pointed tip at one end, resembling a sewing needle or drawing instrument.
def model_78773_06275eba_0009():
    """Model: arrow_3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0325731409, perimeter: 2.2349037819
            with BuildLine():
                CenterArc((0, 0), 0.14, 83.8493601721, 12.3012796559)
                Line((0.015, 0.1391941091), (0.015, 1.2265153077))
                CenterArc((0, 1.3), 0.075, -101.5369590328, 23.0739180656)
                Line((-0.015, 1.2265153077), (-0.015, 0.1391941091))
            make_face()
            # Profile area: 0.0265956576, perimeter: 0.6881534931
            with BuildLine():
                Line((0.015, -0.1391941091), (0.015, 0.1391941091))
                CenterArc((0, 0), 0.14, -83.8493601721, 167.6987203441)
            make_face()
            # Profile area: 0.0025883379, perimeter: 0.2242969625
            with BuildLine():
                CenterArc((0, 1.3), 0.075, -101.5369590328, 23.0739180656)
                Line((0.015, 1.2265153077), (0.015, 1.3))
                CenterArc((0, 1.3), 0.015, 0, 180)
                Line((-0.015, 1.3), (-0.015, 1.2265153077))
            make_face()
            # Profile area: 0.0083839008, perimeter: 0.6168918293
            with BuildLine():
                Line((-0.015, 0.1391941091), (-0.015, -0.1391941091))
                CenterArc((0, 0), 0.14, -96.1506398279, 12.3012796559)
                Line((0.015, -0.1391941091), (0.015, 0.1391941091))
                CenterArc((0, 0), 0.14, 83.8493601721, 12.3012796559)
            make_face()
            # Profile area: 0.0265956576, perimeter: 0.6881534931
            with BuildLine():
                CenterArc((0, 0), 0.14, 96.1506398279, 167.6987203441)
                Line((-0.015, 0.1391941091), (-0.015, -0.1391941091))
            make_face()
            # Profile area: 0.0251336695, perimeter: 0.9031431155
            with BuildLine():
                Line((-0.015, 1.3), (-0.015, 1.2265153077))
                CenterArc((0, 1.3), 0.015, 0, 180)
                Line((0.015, 1.2265153077), (0.015, 1.3))
                CenterArc((0, 1.3), 0.075, -78.4630409672, 96.6729978315)
                Line((0.071243832, 1.3234375), (0, 1.54))
                Line((0, 1.54), (-0.071243832, 1.3234375))
                CenterArc((0, 1.3), 0.075, 161.7900431357, 96.6729978315)
            make_face()
            # Profile area: 0.0666614788, perimeter: 4.4987933682
            with BuildLine():
                CenterArc((0, 0), 0.14, -96.1506398279, 12.3012796559)
                Line((-0.015, -0.1391941091), (-0.015, -2.35))
                CenterArc((0, -2.35), 0.015, 180, 180)
                Line((0.015, -2.35), (0.015, -0.1391941091))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a solar-powered ball mount or tracking device featuring a spherical dark base with two flat blue solar panel wings extending from opposite sides at an angle, designed for solar tracking or positioning applications.
def model_78863_d59be42e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.1805093565, perimeter: 36.2404093675
            with BuildLine():
                Line((0, 0), (0, -0.4))
                Line((0, -0.4), (3.5143444265, -0.4))
                Line((3.5143444265, -2.4000000358), (3.5143444265, -0.4))
                CenterArc((5.25, -2.4000000358), 1.7356555735, 180, 180)
                Line((6.9856555735, -2.4000000358), (6.9856555735, -0.4))
                Line((6.9856555735, -0.4), (10.5, -0.4))
                Line((10.5, 0), (10.5, -0.4))
                Line((0, 0), (10.5, 0))
            make_face()
            with BuildLine():
                CenterArc((5.25, -2.4000000358), 1.3462912887, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a lightweight tent or canopy structure with an A-frame peak design, featuring two angled fabric panels meeting at a ridge line and supported by a central pole, with open sides for entry and ventilation.
def model_78880_ed3c684d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0492870116, perimeter: 61.1857402311
            with BuildLine():
                Line((3.1117808279, 10.0146924689), (10.0819231921, 0.0573462344))
                CenterArc((2.9479344438, 9.9), 0.2, 34.9920201986, 55.0079798014)
                Line((-2.9479344438, 10.1), (2.9479344438, 10.1))
                CenterArc((-2.9479344438, 9.9), 0.2, 90, 55.0079798014)
                Line((-3.1117808279, 10.0146924689), (-10.0819231921, 0.0573462344))
                Line((-10.0819231921, 0.0573462344), (-10, 0))
                Line((-3.0298576359, 9.9573462344), (-10, 0))
                CenterArc((-2.9479344438, 9.9), 0.1, 90, 55.0079798014)
                Line((-2.9479344438, 10), (2.9479344438, 10))
                CenterArc((2.9479344438, 9.9), 0.1, 34.9920201985, 55.0079798016)
                Line((3.0298576359, 9.9573462344), (10, 0))
                Line((10.0819231921, 0.0573462344), (10, 0))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a flat, elongated elliptical disc or plate with a smooth, curved surface and a slight 3D depth, featuring no holes, slots, or additional features—a simple, minimalist oval component.
def model_78880_ed3c684d_0001():
    """Model: Glazen Schijf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((0, 8.4037797825)):
                Circle(7.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a curved duct or deflector component with a flat rectangular flange at the top and a large hemispherical or bulbous curved chamber below, featuring internal ribbing or structural reinforcement patterns.
def model_78970_755e6a93_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 29.9734812095, perimeter: 70.6680383676
            with BuildLine():
                Line((0, 0), (0, -0.5))
                Line((0, -0.5), (6.6095656957, -0.5))
                Line((6.6095656957, -4.5), (6.6095656957, -0.5))
                CenterArc((10, -4.5), 3.3904343043, 180, 180)
                Line((13.3904343043, -4.5), (13.3904343043, -0.5))
                Line((13.3904343043, -0.5), (20, -0.5))
                Line((20, 0), (20, -0.5))
                Line((0, 0), (20, 0))
            make_face()
            with BuildLine():
                CenterArc((10, -4.5), 2.8325670187, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


# Description: This is a rectangular channel or beam with a hollow elongated body, featuring two raised flanges or mounting points at each end and linear ribbing or grooves running along its length for structural reinforcement.
def model_79010_bf913e12_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.02435, perimeter: 21.154
            with BuildLine():
                Line((-0.1509677589, -2.407), (-0.4842834383, -2.407))
                Line((-0.1509677589, -1.8214717688), (-0.1509677589, -2.407))
                Line((-0.1509677589, -1.8214717688), (-0.3276075396, -1.8214717688))
                Line((-0.3276075396, -1.8214717688), (-0.3276075396, -1.5964717688))
                Line((-0.3276075396, -1.5964717688), (-0.1509677589, -1.5964717688))
                Line((-0.1509677589, -1.367), (-0.1509677589, -1.5964717688))
                Line((0.1490322411, -1.367), (-0.1509677589, -1.367))
                Line((0.1490322411, -1.5964717688), (0.1490322411, -1.367))
                Line((0.1490322411, -1.5964717688), (0.3223924604, -1.5964717688))
                Line((0.3223924604, -1.5964717688), (0.3223924604, -1.8214717688))
                Line((0.3223924604, -1.8214717688), (0.1490322411, -1.8214717688))
                Line((0.1490322411, -2.407), (0.1490322411, -1.8214717688))
                Line((0.5157165617, -2.407), (0.1490322411, -2.407))
                Line((0.5157165617, -2.707), (0.5157165617, -2.407))
                Line((1, -2.707), (0.5157165617, -2.707))
                Line((1, 2.5), (1, -2.707))
                Line((0.5, 2.5), (1, 2.5))
                Line((0.5, 2.5), (0.5, 2.2))
                Line((0.5, 2.2), (0.1667759221, 2.2))
                Line((0.1667759221, 2.2), (0.1667759221, 1.5930981401))
                Line((0.1667759221, 1.5930981401), (0.3154905767, 1.5930981401))
                Line((0.3154905767, 1.5930981401), (0.3154905767, 1.3680981401))
                Line((0.3154905767, 1.3680981401), (0.1667759221, 1.3680981401))
                Line((0.1667759221, 1.3680981401), (0.1667759221, 1.16))
                Line((0.1667759221, 1.16), (-0.1432240779, 1.16))
                Line((-0.1432240779, 1.16), (-0.1432240779, 1.3680981401))
                Line((-0.1432240779, 1.3680981401), (-0.3345094233, 1.3680981401))
                Line((-0.3345094233, 1.3680981401), (-0.3345094233, 1.5930981401))
                Line((-0.3345094233, 1.5930981401), (-0.1432240779, 1.5930981401))
                Line((-0.1432240779, 1.5930981401), (-0.1432240779, 2.2))
                Line((-0.1432240779, 2.2), (-0.5, 2.2))
                Line((-0.5, 2.2), (-0.5, 2.5))
                Line((-1, 2.5), (-0.5, 2.5))
                Line((-1, -2.707), (-1, 2.5))
                Line((-0.4842834383, -2.707), (-1, -2.707))
                Line((-0.4842834383, -2.407), (-0.4842834383, -2.707))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a solar-powered satellite or space probe featuring a rectangular solar panel array mounted on top of a cylindrical body with a protruding curved reflector or antenna dish on its side.
def model_79093_054c6005_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 419.7800885142, perimeter: 215.6247719319
            with BuildLine():
                Line((0, 0), (0, -3.2))
                Line((0, -3.2), (21.9, -3.2))
                Line((21.9, -13.2), (21.9, -3.2))
                CenterArc((32.5, -13.2), 10.6, 180, 180)
                Line((43.1, -13.2), (43.1, -3.2))
                Line((43.1, -3.2), (65, -3.2))
                Line((65, 0), (65, -3.2))
                Line((0, 0), (65, 0))
            make_face()
            with BuildLine():
                CenterArc((32.5, -13.2), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a cylindrical rod or tube with a rectangular slot or notch cut into its middle section, creating a distinctive stepped appearance along its length.
def model_79116_8392be69_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((8, -8), (0, -8))
                Line((8, 0), (8, -8))
                Line((0, 0), (8, 0))
                Line((0, -8), (0, 0))
            make_face()
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((220, -8), (212, -8))
                Line((220, 0), (220, -8))
                Line((212, 0), (220, 0))
                Line((212, -8), (212, 0))
            make_face()
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((220, -180), (212, -180))
                Line((220, -172), (220, -180))
                Line((212, -172), (220, -172))
                Line((212, -180), (212, -172))
            make_face()
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((8, -180), (0, -180))
                Line((8, -172), (8, -180))
                Line((0, -172), (8, -172))
                Line((0, -180), (0, -172))
            make_face()
        # OneSide extrude, distance=280
        extrude(amount=280)
    return part.part


# Description: A flat, elongated parallelogram-shaped plate or bar with a dark blue-gray color and slightly angled edges, featuring a simple, minimalist rectangular geometry with no visible holes or complex features.
def model_79116_8392be69_0002():
    """Model: bocni kryt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 180), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 160, perimeter: 56
            with BuildLine():
                Line((0, 60), (8, 60))
                Line((8, 60), (8, 80))
                Line((8, 80), (0, 80))
                Line((0, 80), (0, 60))
            make_face()
            # Profile area: 4240, perimeter: 464
            with BuildLine():
                Line((8, 60), (8, 80))
                Line((8, 60), (220, 60))
                Line((220, 60), (220, 80))
                Line((220, 80), (8, 80))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a hexagonal tapered punch or chisel with a uniform six-sided shaft that gradually narrows toward a pointed tip, commonly used for marking, punching, or cutting operations.
def model_79116_8392be69_0004():
    """Model: pricka 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((0, 60), (8, 60))
                Line((8, 60), (8, 68))
                Line((8, 68), (0, 68))
                Line((0, 68), (0, 60))
            make_face()
        # OneSide extrude, distance=164
        extrude(amount=164)
    return part.part


# Description: This is a triangular or arrow-shaped 3D solid featuring two connected planar faces that form a sharp pointed tip on the left and a wider trapezoidal base on the right, with clean edges and no holes or additional features.
def model_79120_688e7f03_0001():
    """Model: Desklight-elbow v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.0751983757, perimeter: 16.5950658396
            with BuildLine():
                Line((-0.829873563, -0.6), (4.35, -0.6))
                Line((4.35, -0.6), (4.35, 1.7399987274))
                Line((4.35, 1.7399987274), (0.6700462877, 3.9443792135))
                Line((-0.829873563, -0.6), (0.6700462877, 3.9443792135))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a simple right-angled triangular wedge or prism with a flat base, a vertical right edge, and a sloped hypotenuse, featuring no holes, slots, or additional features—just clean, planar surfaces.
def model_79120_688e7f03_0004():
    """Model: Desklight-top-suport v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.0646649396, perimeter: 15.8353829072
            with BuildLine():
                Line((7.2583208553, 1.931292599), (4.6190903708, 6.5025738911))
                Line((4.6190903708, 6.5025738911), (1.9798598862, 1.931292599))
                Line((1.9798598862, 1.931292599), (7.2583208553, 1.931292599))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a boxing glove with a rounded, padded mitt structure featuring a distinctive anatomical design, internal structural ribbing and support framework visible through semi-transparent surfaces, and a cuffed wrist closure area at the base.
def model_79211_141cf274_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 65.1514255279, perimeter: 53.4238004327
            with BuildLine():
                CenterArc((0, 0), 1, -180, 180)
                Line((-1, 0), (-2, 0))
                CenterArc((0, 0), 2, 180, 150)
                Line((7, -1), (1.7320508076, -1))
                CenterArc((7, 0), 1, -90, 90)
                CenterArc((0, 0), 8, 0, 90)
                CenterArc((0, 7), 1, 90, 90)
                Line((-1, 7), (-1, 1.7320508076))
                CenterArc((0, 0), 2, 120, 60)
                CenterArc((0, 0), 1, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((4.3, 5.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a parallelogram-shaped panel or plate with a flat base surface featuring internal cross-bracing or reinforcement ribs and diagonal support members for structural rigidity.
def model_79325_5f4654e1_0001():
    """Model: Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9309670845, 1.1841875692), x_dir=(1, 0, 0), z_dir=(0, 0.9271838546, 0.3746065934))):
            # Profile area: 5.7335203791, perimeter: 19.3283319027
            with BuildLine():
                Line((0.635, 9.8150531941), (0.635, 18.8442191455))
                Line((0.635, 18.8442191455), (0, 18.8442191455))
                Line((0, 18.8442191455), (0, 9.8150531941))
                Line((0.635, 9.8150531941), (0, 9.8150531941))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((-27.635, 24.3442191455), (-27, 24.3442191455))
                Line((-27.635, 24.3442191455), (-27.635, 21.3442191455))
                Line((-27, 21.3442191455), (-27.635, 21.3442191455))
                Line((-27, 21.3442191455), (-27, 24.3442191455))
            make_face()
            # Profile area: 5.7335203791, perimeter: 19.3283319027
            with BuildLine():
                Line((-27.635, 18.8442191455), (-27, 18.8442191455))
                Line((-27.635, 18.8442191455), (-27.635, 9.8150531941))
                Line((-27.635, 9.8150531941), (-27, 9.8150531941))
                Line((-27, 9.8150531941), (-27, 18.8442191455))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((-27, 7.3150531941), (-27.635, 7.3150531941))
                Line((-27.635, 7.3150531941), (-27.635, 4.3150531941))
                Line((-27, 4.3150531941), (-27.635, 4.3150531941))
                Line((-27, 4.3150531941), (-27, 7.3150531941))
            make_face()
            # Profile area: 16.0233327611, perimeter: 41.6583319027
            with BuildLine():
                Line((-27.635, 7.3150531941), (-27.635, 4.3150531941))
                Line((-27.635, 7.3150531941), (-27.635, 9.8150531941))
                Line((-27.635, 18.8442191455), (-27.635, 9.8150531941))
                Line((-27.635, 21.3442191455), (-27.635, 18.8442191455))
                Line((-27.635, 24.3442191455), (-27.635, 21.3442191455))
                Line((-28.435, 24.3442191455), (-27.635, 24.3442191455))
                Line((-28.435, 4.3150531941), (-28.435, 24.3442191455))
                Line((-27.635, 4.3150531941), (-28.435, 4.3150531941))
            make_face()
            # Profile area: 540.7874806868, perimeter: 94.0583319027
            with BuildLine():
                Line((0, 18.8442191455), (0, 21.3442191455))
                Line((0, 24.3442191455), (0, 21.3442191455))
                Line((-27, 24.3442191455), (0, 24.3442191455))
                Line((-27, 21.3442191455), (-27, 24.3442191455))
                Line((-27, 18.8442191455), (-27, 21.3442191455))
                Line((-27, 9.8150531941), (-27, 18.8442191455))
                Line((-27, 9.8150531941), (-27, 7.3150531941))
                Line((-27, 4.3150531941), (-27, 7.3150531941))
                Line((0, 4.3150531941), (-27, 4.3150531941))
                Line((0, 7.3150531941), (0, 4.3150531941))
                Line((0, 9.8150531941), (0, 7.3150531941))
                Line((0, 18.8442191455), (0, 9.8150531941))
            make_face()
            # Profile area: 16.0233327611, perimeter: 41.6583319027
            with BuildLine():
                Line((0.635, 7.3150531941), (0.635, 9.8150531941))
                Line((0.635, 4.3150531941), (0.635, 7.3150531941))
                Line((1.435, 4.3150531941), (0.635, 4.3150531941))
                Line((1.435, 24.3442191455), (1.435, 4.3150531941))
                Line((0.635, 24.3442191455), (1.435, 24.3442191455))
                Line((0.635, 21.3442191455), (0.635, 24.3442191455))
                Line((0.635, 21.3442191455), (0.635, 18.8442191455))
                Line((0.635, 9.8150531941), (0.635, 18.8442191455))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((0, 7.3150531941), (0.635, 7.3150531941))
                Line((0, 7.3150531941), (0, 4.3150531941))
                Line((0.635, 4.3150531941), (0, 4.3150531941))
                Line((0.635, 4.3150531941), (0.635, 7.3150531941))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((0, 24.3442191455), (0.635, 24.3442191455))
                Line((0, 24.3442191455), (0, 21.3442191455))
                Line((0, 21.3442191455), (0.635, 21.3442191455))
                Line((0.635, 21.3442191455), (0.635, 24.3442191455))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635)
    return part.part


# Description: This is a curved plastic or composite bracket or guard component with a rounded L-shaped profile, featuring a hollow cutout on the inner edge and a smooth, contoured exterior surface designed to fit around or protect an internal assembly.
def model_79338_5e0d79fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3202967656, perimeter: 14.5627094321
            with BuildLine():
                Line((0, 0.8128), (2.032, 0.8128))
                CenterArc((0, 0), 0.8128, 90, 180)
                Line((0, -0.8128), (1.3208, -0.8128))
                CenterArc((1.8288, -0.8128), 0.508, -11.9353906281, 191.9353906281)
                Line((2.3258177663, -0.9178587456), (2.9301903829, -1.5222313622))
                CenterArc((0, 0), 3.302, -27.4518375838, 19.9834952803)
                Line((2.032, 0.8128), (3.273988572, -0.429188572))
            make_face()
            with BuildLine():
                CenterArc((0.381, 0), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.762, -0.508), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.143, 0), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.762, 0.508), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.127
        extrude(amount=0.127, both=True)
    return part.part


# Description: This is a cylindrical connector or adapter housing with a curved/rounded rectangular body, featuring a protruding angular flange or guide element on one end and what appears to be internal cavity or slot details visible through semi-transparent surfaces.
def model_79423_62db5fc6_0020():
    """Model: 2-18-CON-ROD BIG END"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8417367153, perimeter: 5.4845130209
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 180)
                Line((-0.45, 0), (-0.45, -0.8))
                Line((-0.45, -0.8), (0.45, -0.8))
                Line((0.45, -0.8), (0.45, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.9
        extrude(amount=0.45, both=True)
    return part.part


# Description: This is a flat metal bracket or panel with a parallelogram shape, featuring multiple rectangular cutouts and slots distributed across its surface for mounting, ventilation, or component access.
def model_79424_5ac55435_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 43 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.6109226297, perimeter: 107.9855731415
            with BuildLine():
                Line((12.7, 0), (12.7, 7.96798))
                Line((12.7, 7.96798), (0, 7.96798))
                Line((0, 7.96798), (0, 0))
                Line((0, 0), (12.7, 0))
            make_face()
            with BuildLine():
                Line((9.9695001175, 2.794), (9.9695001175, 1.9974056672))
                Line((12.573, 2.794), (9.9695001175, 2.794))
                Line((12.573, 1.9974056672), (12.573, 2.794))
                Line((9.9695001175, 1.9974056672), (12.573, 1.9974056672))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((11.3411, 5.3593999352), (10.4140003324, 5.3593999352))
                Line((11.3411, 5.3593999352), (11.3411, 7.32028))
                Line((9.9568, 7.32028), (11.3411, 7.32028))
                Line((9.9568, 7.71398), (9.9568, 7.32028))
                Line((9.9568, 7.71398), (11.8145942601, 7.71398))
                Line((11.8145942601, 7.3405999383), (11.8145942601, 7.71398))
                Line((11.8145942601, 7.3405999383), (12.4206, 7.3405999383))
                Line((12.4206, 7.3405999383), (12.4206, 4.470399946))
                Line((12.4206, 4.470399946), (9.9695001175, 4.470399946))
                Line((9.9695001175, 4.470399946), (9.9695001175, 5.3594001699))
                Line((10.4140003324, 5.3593999352), (9.9695001175, 5.3594001699))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.8890000284, 1.1938), (0.0508, 1.1938))
                Line((0.0508, 2.3114), (0.0508, 1.1938))
                Line((0.8890000284, 2.3114), (0.0508, 2.3114))
                Line((0.8890000284, 1.1938), (0.8890000284, 2.3114))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.0508, 7.05358), (1.1811, 7.05358))
                Line((1.1811, 7.05358), (1.1811, 5.21208))
                Line((1.1811, 5.21208), (1.905, 5.2070001662))
                Line((1.905, 3.00228), (1.905, 5.2070001662))
                Line((0.0508, 3.00228), (1.905, 3.00228))
                Line((0.0508, 7.05358), (0.0508, 3.00228))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.1021, 7.84098), (9.4995998852, 7.84098))
                Line((9.4995998852, 7.84098), (9.4995998852, 7.15518))
                Line((9.4995998852, 7.15518), (4.1021, 7.15518))
                Line((4.1021, 7.84098), (4.1021, 7.15518))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((9.5250156411, 0.8253210638), (3.3145846423, 0.8253210638))
                Line((9.5250156411, 0.1270000041), (9.5250156411, 0.8253210638))
                Line((3.3145846423, 0.1270000041), (9.5250156411, 0.1270000041))
                Line((3.3145846423, 0.8253210638), (3.3145846423, 0.1270000041))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((12.2808589833, 7.5209349918), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((12.2808672964, 0.4469411397), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4193778415, 0.4471310474), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4194012685, 7.5208194638), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.29972
        extrude(amount=0.29972)
    return part.part


# Description: This is a dark triangular or wedge-shaped bracket or support component with a peaked top, a flat base, and reinforcing ribs or flanges along its edges for structural rigidity.
def model_79510_f27c9c97_0000():
    """Model: leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 181.9155960151, perimeter: 65.4997376244
            with BuildLine():
                Line((0, 5.5), (0, 0))
                Line((0, 0), (22.5, 0))
                Line((22.5, 0), (22.5, 12.5))
                Line((22.5, 12.5), (1.9296608098, 4.1890434928))
                Line((1.9296608098, 4.1890434928), (1.4, 5.5))
                Line((1.4, 5.5), (0, 5.5))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a trapezoidal profile, featuring internal diagonal bracing and horizontal reinforcement ribs that provide structural support across its surface.
def model_79510_f27c9c97_0001():
    """Model: top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9309670845, 1.1841875692), x_dir=(1, 0, 0), z_dir=(0, 0.9271838546, 0.3746065934))):
            # Profile area: 554.6085442574, perimeter: 95.0821143894
            with BuildLine():
                Line((0, 9.1583936602), (0, 18.6994508549))
                Line((0, 18.6994508549), (0, 21.1994508549))
                Line((0, 21.1994508549), (0, 24.1994508549))
                Line((-27, 24.1994508549), (0, 24.1994508549))
                Line((-27, 21.1994508549), (-27, 24.1994508549))
                Line((-27, 21.1994508549), (-27, 18.6994508549))
                Line((-27, 9.1583936602), (-27, 18.6994508549))
                Line((-27, 9.1583936602), (-27, 6.6583936602))
                Line((-27, 3.6583936602), (-27, 6.6583936602))
                Line((0, 3.6583936602), (-27, 3.6583936602))
                Line((0, 3.6583936602), (0, 6.6583936602))
                Line((0, 9.1583936602), (0, 6.6583936602))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((0, 3.6583936602), (0, 6.6583936602))
                Line((0.635, 3.6583936602), (0, 3.6583936602))
                Line((0.635, 3.6583936602), (0.635, 6.6583936602))
                Line((0, 6.6583936602), (0.635, 6.6583936602))
            make_face()
            # Profile area: 16.4328457558, perimeter: 42.6821143894
            with BuildLine():
                Line((0.635, 6.6583936602), (0.635, 9.1583936602))
                Line((0.635, 3.6583936602), (0.635, 6.6583936602))
                Line((1.435, 3.6583936602), (0.635, 3.6583936602))
                Line((1.435, 24.1994508549), (1.435, 3.6583936602))
                Line((0.635, 24.1994508549), (1.435, 24.1994508549))
                Line((0.635, 21.1994508549), (0.635, 24.1994508549))
                Line((0.635, 21.1994508549), (0.635, 18.6994508549))
                Line((0.635, 9.1583936602), (0.635, 18.6994508549))
            make_face()
            # Profile area: 6.0585713186, perimeter: 20.3521143894
            with BuildLine():
                Line((-27, 18.6994508549), (-27.635, 18.6994508549))
                Line((-27.635, 18.6994508549), (-27.635, 9.1583936602))
                Line((-27.635, 9.1583936602), (-27, 9.1583936602))
                Line((-27, 9.1583936602), (-27, 18.6994508549))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((-27.635, 24.1994508549), (-27, 24.1994508549))
                Line((-27.635, 24.1994508549), (-27.635, 21.1994508549))
                Line((-27.635, 21.1994508549), (-27, 21.1994508549))
                Line((-27, 21.1994508549), (-27, 24.1994508549))
            make_face()
            # Profile area: 16.4328457558, perimeter: 42.6821143894
            with BuildLine():
                Line((-27.635, 6.6583936602), (-27.635, 3.6583936602))
                Line((-27.635, 6.6583936602), (-27.635, 9.1583936602))
                Line((-27.635, 18.6994508549), (-27.635, 9.1583936602))
                Line((-27.635, 18.6994508549), (-27.635, 21.1994508549))
                Line((-27.635, 24.1994508549), (-27.635, 21.1994508549))
                Line((-28.435, 24.1994508549), (-27.635, 24.1994508549))
                Line((-28.435, 3.6583936602), (-28.435, 24.1994508549))
                Line((-27.635, 3.6583936602), (-28.435, 3.6583936602))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((-27, 6.6583936602), (-27.635, 6.6583936602))
                Line((-27.635, 6.6583936602), (-27.635, 3.6583936602))
                Line((-27, 3.6583936602), (-27.635, 3.6583936602))
                Line((-27, 3.6583936602), (-27, 6.6583936602))
            make_face()
            # Profile area: 1.905, perimeter: 7.27
            with BuildLine():
                Line((0, 21.1994508549), (0.635, 21.1994508549))
                Line((0.635, 21.1994508549), (0.635, 24.1994508549))
                Line((0, 24.1994508549), (0.635, 24.1994508549))
                Line((0, 21.1994508549), (0, 24.1994508549))
            make_face()
            # Profile area: 6.0585713186, perimeter: 20.3521143894
            with BuildLine():
                Line((0.635, 9.1583936602), (0, 9.1583936602))
                Line((0.635, 9.1583936602), (0.635, 18.6994508549))
                Line((0.635, 18.6994508549), (0, 18.6994508549))
                Line((0, 9.1583936602), (0, 18.6994508549))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635)
    return part.part


# Description: This is a cylindrical pressure vessel or pipe component with rounded end caps, featuring a smooth curved surface and internal geometric details visible through the mesh wireframe representation.
def model_79625_8be98a9f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a circular disc or flange with a large central hole, featuring multiple smaller holes distributed around its face for fastening purposes, and a textured or knurled outer edge.
def model_79678_786d163b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 137.4446785946, perimeter: 94.2477796077
            with BuildLine():
                CenterArc((0, 0), 7.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.9980430769, 0.1398763781), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0100411396, -4.9999899175), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.9980430769, 0.1398763781), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0100411396, 4.9999899175), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rectangular enclosure or mounting bracket with rounded corners, featuring horizontal slot openings on the front face and mounting holes positioned at the corners.
def model_79693_9396219b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.7742776726, perimeter: 27.047355355
            with BuildLine():
                CenterArc((1.5, 1), 1, 90, 90)
                Line((0.5, -0.1461529184), (0.5, 1))
                CenterArc((1.5, -0.1461529184), 1, -180, 90)
                Line((6.230668411, -1.1461529184), (1.5, -1.1461529184))
                CenterArc((6.230668411, -0.1461529184), 1, -90, 90)
                Line((7.230668411, 1), (7.230668411, -0.1461529184))
                CenterArc((6.230668411, 1), 1, 0, 90)
                Line((1.5, 2), (6.230668411, 2))
            make_face()
            with BuildLine():
                CenterArc((6.230668411, -0.1461529184), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, -0.1461529184), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.230668411, 1), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 1), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2033981153, -0.435980156), 0.0340699738, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a hexagonal ring or collar with a large central hole, featuring a twisted or tapered geometry with angled faces and a hollow core, likely designed as a structural connector or mounting component.
def model_79693_9396219b_0002():
    """Model: bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4811803295, perimeter: 5.6632165243
            with BuildLine():
                Line((-1.1732050982, -0.9690599068), (-0.8267949316, -1.430940129))
                Line((-0.8267949316, -1.430940129), (-0.2535898423, -1.3618802356))
                Line((-0.2535898423, -1.3618802356), (-0.0267949196, -0.8309401201))
                Line((-0.0267949196, -0.8309401201), (-0.3732050863, -0.3690598978))
                Line((-0.3732050863, -0.3690598978), (-0.9464101756, -0.4381197912))
                Line((-0.9464101756, -0.4381197912), (-1.1732050982, -0.9690599068))
            make_face()
            with BuildLine():
                CenterArc((-0.6000000089, -0.9000000134), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)
    return part.part


# Description: A hexagonal ring or frame featuring a central oval aperture with curved, inward-tapering sides and faceted external geometry, creating a hollow structural component with an organic, twisted appearance.
def model_79906_052c7eb4_0000():
    """Model: Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.8520002002, perimeter: 8.5918800934
            with BuildLine():
                Line((0.73, -0.4214656965), (0.73, 0.4214656965))
                Line((0.73, 0.4214656965), (0, 0.842931393))
                Line((0, 0.842931393), (-0.73, 0.4214656965))
                Line((-0.73, 0.4214656965), (-0.73, -0.4214656965))
                Line((-0.73, -0.4214656965), (0, -0.842931393))
                Line((0, -0.842931393), (0.73, -0.4214656965))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.24
        extrude(amount=0.24)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a uniform circular cross-section, featuring a textured or ribbed surface finish on its outer perimeter and a smooth central void.
def model_79906_052c7eb4_0001():
    """Model: Washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.6886371097, perimeter: 8.6079638708
            with BuildLine():
                CenterArc((0, 0), 0.765, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.605, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)
    return part.part


# Description: This is a cylindrical barrel or drum with a rounded top surface and a flat circular face, featuring a wireframe-textured curved side surface that suggests a ribbed or corrugated external pattern.
def model_79986_27ba3aa9_0000():
    """Model: cutting plier v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 123.603626396, perimeter: 39.4112798393
            Circle(6.2725)
        # TwoSides extrude (symmetric), distance=4.25
        extrude(amount=4.25, both=True)
    return part.part


# Description: This is a polyhedron or geometric solid featuring an irregular, faceted shape with multiple planar surfaces in varying shades of dark blue and gray, with no obvious holes, slots, or curves—appearing to be a complex multi-sided geometric form, possibly an architectural or abstract design element.
def model_80178_284e8e7a_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, 1), (1, 1))
                Line((-1, -1), (-1, 1))
                Line((1, -1), (-1, -1))
                Line((1, 1), (1, -1))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a dark blue/navy helmet or head-mounted device with an overall rounded, organic shape featuring a prominent curved visor or face opening on the front, textured mesh panels on the sides and top for ventilation, and a cylindrical attachment or connector protruding from the lower left side.
def model_80470_fca39d24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.7997171086, perimeter: 51.9328257016
            with BuildLine():
                CenterArc((7, 0), 1, -90, 90)
                CenterArc((0, 0), 8, 0, 90)
                CenterArc((0, 7), 1, 90, 90)
                Line((-1, 7), (-1, 1.5))
                CenterArc((0, 0), 1.8027756377, 123.690067526, 202.619864948)
                Line((1.5, -1), (7, -1))
            make_face()
            with BuildLine():
                CenterArc((7, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3, 5.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a welding helmet or protective headgear with an organic, curved ergonomic shape featuring a large viewing window/visor opening, ventilation mesh areas on the top and sides, and a chin guard section at the bottom.
def model_80473_92aeb455_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 67.015827883, perimeter: 53.0212461434
            with BuildLine():
                CenterArc((7, 0), 1, -90, 90)
                CenterArc((0, 0), 8, 0, 90)
                CenterArc((0, 7), 1, 90, 90)
                Line((-1, 7), (-1, 2))
                CenterArc((0, 0), 2.2360679775, 116.5650511771, 216.8698976458)
                Line((7, -1), (2, -1))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3, 5.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a stylus or pen-like tool with a long, slender cylindrical shaft and a small pointed or hook-shaped tip at the upper end, designed for precision input or marking applications.
def model_80490_5d5ba15f_0000():
    """Model: 卡钩"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1743982999, perimeter: 5.4227875428
            with BuildLine():
                Line((-0.080976915, 0.7000000104), (-0.0152645975, 0.7000000104))
                Line((-0.0152645975, 0.7000000104), (-0.0152645975, 3.2999999262))
                Line((-0.0152645975, 3.2999999262), (-0.0828795141, 3.2999999262))
                Line((-0.0828795141, 3.2999999262), (-0.1500000022, 3.2000000477))
                Line((-0.080976915, 3.2000000477), (-0.1500000022, 3.2000000477))
                Line((-0.080976915, 0.7000000104), (-0.080976915, 3.2000000477))
            make_face()
        # TwoSides extrude (symmetric), distance=0.03
        extrude(amount=0.03, both=True)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered design, featuring a smooth, elongated tubular shape with rounded ends.
def model_80490_5d5ba15f_0001():
    """Model: 笔杆"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-9
        extrude(amount=-9)
    return part.part


# Description: This is a tapered cylindrical pin or rod with a slightly curved or bent profile, featuring a gradual diameter reduction from one end to the other.
def model_80491_e73dabd5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.2869479333, perimeter: 69.0916253334
            with BuildLine():
                Line((-1, -9.6249083983), (-1, 12.2862138142))
                CenterArc((-0.5, -9.6249083983), 0.5, 180, 90)
                Line((0, -10.1249083983), (-0.5, -10.1249083983))
                Line((0, -10.1249083983), (0, 23.5))
                Line((0, 23.5), (-0.75, 23.5))
                CenterArc((-0.75, 23.25), 0.25, 90, 90)
                Line((-1, 18.3150926303), (-1, 23.25))
                CenterArc((0.5, 18.3150926303), 1.5, 180, 22.5388175933)
                CenterArc((-6.8856315459, 15.25), 6.4963958233, -23.2885208672, 45.8273384605)
                CenterArc((0, 12.2862138142), 1, 156.7114791328, 23.2885208672)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a triangular or wedge-shaped solid object with a trapezoidal profile, featuring internal diagonal bracing or reinforcement ribs that create a latticed structure for lightweight strength.
def model_80493_74f06ac0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50, perimeter: 34.1421356237
            with BuildLine():
                Line((5, 5), (-5, -5))
                Line((-5, -5), (5, -5))
                Line((5, -5), (5, 5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a uniform circular cross-section and a slight taper or chamfer at both extremities.
def model_80494_8a92342c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6648704379, perimeter: 2.9699569883
            with BuildLine():
                CenterArc((0, 0.591764981), 0.006, 46.7688008937, 86.4623982126)
                Line((-0.0041096637, 0.5961365555), (-0.2149358637, 0.3979414292))
                CenterArc((-0.2697313795, 0.4562290904), 0.08, -59.4076071262, 12.6388062325)
                CenterArc((0, 0), 0.45, 120.5923928738, 298.8152142523)
                CenterArc((0.2697313795, 0.4562290904), 0.08, -133.2311991063, 12.6388062325)
                Line((0.0041096637, 0.5961365555), (0.2149358637, 0.3979414292))
            make_face()
        # OneSide extrude, distance=14.3
        extrude(amount=14.3)
    return part.part


# Description: This is a composite geometric solid consisting of a rectangular prism (right side) joined to a triangular or wedge-shaped prism (left side), creating an asymmetrical polyhedron with flat faces and angled surfaces.
def model_80758_5dd10206_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.5502553065, perimeter: 41.9297034145
            with BuildLine():
                Line((4.3705966929, 6), (2.5363691291, 6))
                Line((2.5363691291, 6), (2.5363691291, -2.5012208364))
                Line((2.5363691291, -2.5012208364), (15, -2.5012208364))
                Line((15, -2.5012208364), (15, -1))
                Line((15, -1), (4.3705966929, -1))
                Line((4.3705966929, -1), (4.3705966929, 6))
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)
    return part.part


# Description: This is a hexagonal or polygonal housing/enclosure with a complex geometric structure featuring angled faceted surfaces, internal ribbing or reinforcement straps, and multiple planar faces in varying shades indicating different surface orientations and depth.
def model_80761_62bb3981_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 186.1587385212, perimeter: 52.853981634
            with BuildLine():
                CenterArc((6.25, -5), 1.25, -90, 90)
                Line((7.5, -5), (7.5, 5))
                CenterArc((6.25, 5), 1.25, 0, 90)
                Line((6.25, 6.25), (-6.25, 6.25))
                CenterArc((-6.25, 5), 1.25, 90, 90)
                Line((-7.5, 5), (-7.5, -5))
                CenterArc((-6.25, -5), 1.25, 180, 90)
                Line((-6.25, -6.25), (6.25, -6.25))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a wrench or spanner tool featuring an L-shaped design with a long cylindrical handle and a rectangular open jaw head at the top, designed for gripping and turning nuts or bolts.
def model_80766_9206dfb0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 45 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.4314159265, perimeter: 29.0849555922
            with BuildLine():
                CenterArc((1.55, -0.8), 0.2, -90, 90)
                Line((1.75, -0.8), (1.75, 0.8))
                CenterArc((1.55, 0.8), 0.2, 0, 90)
                Line((1.55, 1), (-1.55, 1))
                CenterArc((-1.55, 0.8), 0.2, 90, 90)
                Line((-1.75, -6), (-1.75, 0.8))
                Line((-1.45, -6), (-1.75, -6))
                Line((-1.45, -1.2), (-1.45, -6))
                CenterArc((-1.25, -1.2), 0.2, 90, 90)
                Line((-1.25, -1), (1.55, -1))
            make_face()
            with BuildLine():
                Line((-1.45, -0.6), (-1.45, 0.6))
                CenterArc((-1.35, 0.6), 0.1, 90, 90)
                Line((-1.35, 0.7), (1.35, 0.7))
                CenterArc((1.35, 0.6), 0.1, 0, 90)
                Line((1.45, 0.6), (1.45, -0.6))
                CenterArc((1.35, -0.6), 0.1, -90, 90)
                Line((1.35, -0.7), (-1.35, -0.7))
                CenterArc((-1.35, -0.6), 0.1, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a rectangular prism or block with a diagonal plane cut through it, creating an angled or chamfered surface that divides the solid into two distinct geometric sections with triangular and trapezoidal faces.
def model_80768_93483df3_0002():
    """Model: 便池"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((5, -5), (5, 5))
                Line((5, 5), (-5, 5))
                Line((-5, 5), (-5, -5))
                Line((-5, -5), (5, -5))
            make_face()
        # OneSide extrude, distance=-23.3
        extrude(amount=-23.3)
    return part.part


# Description: This is a 3D CAD part featuring a flat, rounded rectangular plate with a parallelogram-like shape, characterized by gentle curves at all corners and a slight trapezoidal skew.
def model_80769_6632d585_0000():
    """Model: 基板"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 98.0685834706, perimeter: 37.4247779608
            with BuildLine():
                CenterArc((3.5, -3.5), 1.5, -90, 90)
                Line((5, -3.5), (5, 3.5))
                CenterArc((3.5, 3.5), 1.5, 0, 90)
                Line((3.5, 5), (-3.5, 5))
                CenterArc((-3.5, 3.5), 1.5, 90, 90)
                Line((-5, 3.5), (-5, -3.5))
                CenterArc((-3.5, -3.5), 1.5, -180, 90)
                Line((-3.5, -5), (3.5, -5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: A flat, trapezoidal tray or shallow pan with a recessed blue surface, dark gray rim/flange, and internal diagonal reinforcement ribs, designed for containing or organizing contents.
def model_80911_b01bc2a7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 199.1415926536, perimeter: 58.2831853072
            with BuildLine():
                CenterArc((9, -4), 1, -90, 90)
                Line((10, -4), (10, 4))
                CenterArc((9, 4), 1, 0, 90)
                Line((9, 5), (-9, 5))
                CenterArc((-9, 4), 1, 90, 90)
                Line((-10, 4), (-10, -4))
                CenterArc((-9, -4), 1, -180, 90)
                Line((-9, -5), (9, -5))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9)
    return part.part


# Description: This is a rubber O-ring seal, characterized by its circular torus shape with a uniform cross-section, designed to create a watertight or airtight seal in mechanical applications.
def model_81123_41bb9143_0000():
    """Model: 22-BOILER GLADDING STRAP"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on Plane1 construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -29.0253690931, 7.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.5499996986, perimeter: 70.9999939711
            with BuildLine():
                CenterArc((0, -1.5746309069), 5.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -1.5746309069), 5.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a long, slender hexagonal or prismatic rod/bar with a tapered or beveled point at one end, featuring longitudinal grooves or flutes running along its length, commonly used as a tool bit, cutting tool, or indexable insert holder.
def model_81123_41bb9143_0001():
    """Model: 21-BOILER GLADDING PLANK"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on Plane1 construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -29.0253690931, 7.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2337705011, perimeter: 2.1584700075
            with BuildLine():
                Line((0.3785714286, -6.8610932092), (0.4, -7.1603269244))
                CenterArc((0, -1.5746309069), 5.3, -94.0960437582, 8.1920875163)
                Line((-0.3785714286, -6.8610932092), (-0.4, -7.1603269244))
                CenterArc((0, -1.5746309069), 5.6, -94.0960437582, 8.1920875163)
            make_face()
        # OneSide extrude, distance=6.6
        extrude(amount=6.6)
    return part.part


# Description: This is a cylindrical disc or wheel with a flat, circular face and a textured or ribbed edge/rim, resembling a pulley, gear wheel, or industrial drum component.
def model_81123_41bb9143_0009():
    """Model: 26-STEAM DELIVERY PIPE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.9022104447, perimeter: 16.9646003294
            Circle(2.7)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a blue and black composite drone or aerial vehicle frame featuring a streamlined body with four circular motor mounts at the corners, strut reinforcements throughout the structure, and an open central cavity design for component integration.
def model_81145_bdb0ac6a_0016():
    """Model: Oxcart X-main v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.6684475712, perimeter: 51.5123147706
            with BuildLine():
                CenterArc((-1.4000000238, -3.2000000507), 0.2, 180, 90)
                Line((1.4000000238, -3.4000000507), (-1.4000000238, -3.4000000507))
                CenterArc((1.4000000238, -3.2000000507), 0.2, -90, 90)
                Line((1.6000000238, -3.2000000507), (1.6000000238, -3.1435029081))
                CenterArc((1.8000000238, -3.1435029081), 0.2, 45, 135)
                Line((1.9414213801, -3.0020815519), (2.4088834765, -3.4695436483))
                CenterArc((2.9392135624, -2.9392135624), 0.75, -135, 180)
                Line((3.4695436483, -2.4088834765), (2.1692386438, -1.108578472))
                CenterArc((2.31066, -0.9671571157), 0.2, -180, 45)
                Line((2.11066, 0.9671571157), (2.11066, -0.9671571157))
                CenterArc((2.31066, 0.9671571157), 0.2, 135, 45)
                Line((3.4695436483, 2.4088834765), (2.1692386438, 1.108578472))
                CenterArc((2.9392135624, 2.9392135624), 0.75, -45, 179.9999987926)
                Line((1.9414213801, 3.0020815519), (2.4088834765, 3.4695436483))
                CenterArc((1.8000000238, 3.1435029081), 0.2, 180, 135)
                Line((1.6000000238, 3.2000000507), (1.6000000238, 3.1435029081))
                CenterArc((1.4000000238, 3.2000000507), 0.2, 0, 90)
                Line((-1.4000000238, 3.4000000507), (1.4000000238, 3.4000000507))
                CenterArc((-1.4000000238, 3.2000000507), 0.2, 90, 90)
                Line((-1.6000000238, 3.2000000507), (-1.6000000238, 3.1435029081))
                CenterArc((-1.8000000238, 3.1435029081), 0.2, -135, 135)
                Line((-1.9414213801, 3.0020815519), (-2.4088834765, 3.4695436483))
                CenterArc((-2.9392135624, 2.9392135624), 0.75, 45, 180)
                Line((-3.4695436483, 2.4088834765), (-2.1692386438, 1.108578472))
                CenterArc((-2.31066, 0.9671571157), 0.2, 0, 45)
                Line((-2.11066, -0.9671571157), (-2.11066, 0.9671571157))
                CenterArc((-2.31066, -0.9671571157), 0.2, -45, 45)
                Line((-3.4695436483, -2.4088834765), (-2.1692386438, -1.108578472))
                CenterArc((-2.9392135624, -2.9392135624), 0.75, 135, 180)
                Line((-1.9414213801, -3.0020815519), (-2.4088834765, -3.4695436483))
                CenterArc((-1.8000000238, -3.1435029081), 0.2, 0, 135)
                Line((-1.6000000238, -3.1435029081), (-1.6000000238, -3.2000000507))
            make_face()
            with BuildLine():
                CenterArc((-1.525, 1.525), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.525, 1.525), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.525, -1.525), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.525, -1.525), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.9392135624, 2.9392135624), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9392135624, 2.9392135624), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.9392135624, -2.9392135624), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9392135624, -2.9392135624), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9500000142, 2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9500000142, 2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9500000142, -2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9500000142, -2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5, -2.5250000507), (-0.5, -1.9250000507))
                CenterArc((-0.3, -1.9250000507), 0.2, 90, 90)
                Line((-0.3, -1.7250000507), (0.3, -1.7250000507))
                CenterArc((0.3, -1.9250000507), 0.2, 0, 90)
                Line((0.5, -1.9250000507), (0.5, -2.5250000507))
                CenterArc((0.3, -2.5250000507), 0.2, -90, 90)
                Line((0.3, -2.7250000507), (-0.3, -2.7250000507))
                CenterArc((-0.3, -2.5250000507), 0.2, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.3, 1.7250000507), (0.3, 1.7250000507))
                CenterArc((-0.3, 1.9250000507), 0.2, 180, 90)
                Line((-0.5, 2.5250000507), (-0.5, 1.9250000507))
                CenterArc((-0.3, 2.5250000507), 0.2, 90, 90)
                Line((0.3, 2.7250000507), (-0.3, 2.7250000507))
                CenterArc((0.3, 2.5250000507), 0.2, 0, 90)
                Line((0.5, 1.9250000507), (0.5, 2.5250000507))
                CenterArc((0.3, 1.9250000507), 0.2, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an elongated rectangular box or tray with a tapered, wedge-shaped top section featuring angled surfaces and internal diagonal ribbing or bracing for structural reinforcement.
def model_81145_bdb0ac6a_0017():
    """Model: Jeti Duplex EX R3 Receiver v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8, perimeter: 12.4
            with BuildLine():
                Line((1.1227426506, -1.9855680592), (-1.0772573494, -1.9855680592))
                Line((1.1227426506, 2.0144319408), (1.1227426506, -1.9855680592))
                Line((-1.0772573494, 2.0144319408), (1.1227426506, 2.0144319408))
                Line((-1.0772573494, -1.9855680592), (-1.0772573494, 2.0144319408))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform diameter, tapered slightly at one end, featuring a smooth, elongated tubular form with no holes or flanges.
def model_81145_bdb0ac6a_0023():
    """Model: Antenna Tube (60mm) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0313373867, perimeter: 1.7907078125
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a cylindrical rod or shaft with a simple, uniform round cross-section and tapered or slightly rounded ends, designed as a basic structural or mechanical component.
def model_81145_bdb0ac6a_0024():
    """Model: Antenna Tube (70mm) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0313373867, perimeter: 1.7907078125
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a dark-colored structural bracket or frame component with an organic, curved shape featuring multiple triangulated reinforcement ribs, two large circular cutout holes, and several smaller fastening holes throughout its design for lightweight strength and assembly purposes.
def model_81145_bdb0ac6a_0041():
    """Model: Oxcart X-side v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22.4071872061, perimeter: 53.7535624142
            with BuildLine():
                CenterArc((-0.9000000089, -0.3100000076), 0.2, -89.9999999526, 89.9999999526)
                Line((-0.7000000089, 0.2000000063), (-0.7000000089, -0.3100000076))
                CenterArc((-0.5000000089, 0.2000000063), 0.2, 90.0000001115, 89.9999998885)
                Line((-0.5000000093, 0.4000000063), (0.5000000099, 0.4000000083))
                CenterArc((0.5000000103, 0.2000000083), 0.2, 0, 90.0000001115)
                Line((0.7000000103, 0.2000000083), (0.7000000103, -0.3100000075))
                CenterArc((0.9000000103, -0.3100000075), 0.2, -180, 90)
                Line((0.9000000103, -0.5100000075), (2.3000000394, -0.5100000075))
                CenterArc((2.3000000394, -0.7100000075), 0.2, 0.0000006392, 89.9999993608)
                Line((2.5000000394, -0.7100000052), (2.5000000432, -1.0500000181))
                CenterArc((2.9500000432, -1.0500000104), 0.45, -179.9999990243, 179.9999991462)
                Line((3.4000000432, 0.800000018), (3.4000000432, -1.0500000095))
                CenterArc((2.9000000432, 0.800000018), 0.5, 0, 45)
                Line((-0.4464466205, 4.8535534629), (3.2535534338, 1.1535534086))
                CenterArc((-0.8000000164, 4.5000000671), 0.5000000075, 45, 45)
                CenterArc((-0.8980769409, 2.5000000373), 2.5019231142, 87.7533945718, 92.2466054282)
                CenterArc((-2.9000000477, 2.5000000373), 0.5000000075, 180, 45)
                Line((-3.2535534435, 2.1464466414), (-2.9778950814, 1.8707882792))
                CenterArc((-3.1193164376, 1.729366923), 0.2, -28.398450401, 73.398450401)
                CenterArc((-2.5035534324, 1.3964466302), 0.5, 151.601549599, 102.1001638892)
                CenterArc((-2.7000000358, 0.7245770506), 0.2, 0, 73.7017134882)
                Line((-2.5000000358, 0.5000000075), (-2.5000000358, 0.7245770506))
                CenterArc((-2.7000000358, 0.5000000075), 0.2, -90, 90)
                Line((-2.9500000484, 0.3000000075), (-2.7000000358, 0.3000000075))
                CenterArc((-2.9500000484, -0.1499999925), 0.45, 90, 90.0000002944)
                Line((-3.4000000432, -1.0500000104), (-3.4000000484, -0.1499999949))
                CenterArc((-2.9500000432, -1.0500000104), 0.45, 180, 180)
                Line((-2.5000000432, -1.0500000104), (-2.5000000432, -0.7100000083))
                CenterArc((-2.3000000432, -0.7100000083), 0.2, 90.0000000279, 89.9999999721)
                Line((-2.3000000433, -0.5100000083), (-0.9000000088, -0.5100000076))
            make_face()
            with BuildLine():
                CenterArc((-0.8000000164, 4.5000000671), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.2000000328, 1.5000000224), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.9500000432, -1.0500000104), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9500000432, -1.0500000104), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8000000164, 2.5000000373), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8000000164, 2.5000000373), 0.8000000164, -25.0000066701, 60)
                CenterArc((-0.0422843109, 3.0305581724), 0.1249999972, 35, 180)
                CenterArc((-0.8000000164, 2.5000000373), 1.0500000108, -25.000005082, 60)
                CenterArc((0.0383346596, 2.109078055), 0.1249999972, 155, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.5000000358, 0), (-1.6000000238, 0))
                CenterArc((-1.5500000231, 0), 0.0500000007, 0, 180)
                Line((-1.5000000224, 0), (-1.5000000224, -0.210000003))
                CenterArc((-1.5500000231, -0.210000003), 0.0500000007, 180, 180)
                Line((-2.5000000358, -0.210000003), (-1.6000000238, -0.210000003))
                CenterArc((-2.5500000365, -0.210000003), 0.0500000007, 180, 180)
                Line((-2.6000000402, 0), (-2.6000000373, -0.210000003))
                CenterArc((-2.550000038, 0), 0.0500000022, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.6000000238, 0), (2.5000000358, 0))
                CenterArc((2.5500000365, 0), 0.0500000007, 0, 180)
                Line((2.6000000373, 0), (2.6000000373, -0.210000003))
                CenterArc((2.5500000365, -0.210000003), 0.0500000007, 180, 180)
                Line((2.5000000358, -0.210000003), (1.6000000238, -0.210000003))
                CenterArc((1.5500000231, -0.210000003), 0.0500000007, 180, 180)
                Line((1.5000000224, 0), (1.5000000224, -0.210000003))
                CenterArc((1.5500000231, 0), 0.0500000007, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8000000164, 4.5000000671), 0.500000003, -129.7051388884, 23.1035895194)
                CenterArc((-1.0000000145, 3.8291796701), 0.2, 0.0000002846, 73.3984503464)
                Line((-0.8000000146, 3.4797959347), (-0.8000000145, 3.8291796711))
                CenterArc((-1.0000000146, 3.4797959347), 0.2, -78.4630410747, 78.463041074)
                CenterArc((-0.8000000164, 2.5000000373), 0.8, 101.5369589253, 66.9260820418)
                CenterArc((-1.7797959135, 2.7000000373), 0.2, -90, 78.4630409672)
                Line((-1.7797959135, 2.5000000373), (-2.3866318923, 2.5000000373))
                CenterArc((-2.3866318923, 2.7000000373), 0.2, 172.3519924042, 97.6480075958)
                CenterArc((-0.8972222358, 2.5000000373), 1.7027778029, 103.4665581089, 68.8854342953)
                CenterArc((-1.2471857943, 3.9614604824), 0.2, 50.2948611116, 53.1716969973)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5035534324, 1.3964466302), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5035534324, 1.3964466302), 0.5, -12.0760288028, 33.3125732989)
                CenterArc((-1.8510883607, 1.6500000373), 0.2, 90, 111.2365444961)
                Line((-1.8510883607, 1.8500000373), (-1.3267827182, 1.8500000373))
                CenterArc((-1.3267827182, 1.6500000373), 0.2, 58.2116686941, 31.7883313059)
                CenterArc((-0.8000000164, 2.5000000373), 0.8000000075, -121.7883313059, 20.2513723602)
                CenterArc((-1.0000000164, 1.5202041325), 0.2, 0, 78.4630410543)
                Line((-0.8000000164, 1.5202041325), (-0.8000000164, 1.250000006))
                CenterArc((-1.0000000164, 1.250000006), 0.2, -90, 90)
                Line((-1.8190438369, 1.050000006), (-1.0000000164, 1.050000006))
                CenterArc((-1.8190438369, 1.250000006), 0.2, 167.9239711972, 102.0760288028)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.8000000164, 2.5000000373), 1.7000000108, -41.1395113297, 24.9010319529)
                CenterArc((1.0242015858, 1.9686916942), 0.2, 45, 118.7615206232)
                Line((1.1656229421, 2.1101130504), (1.6414578369, 1.6342781556))
                CenterArc((1.5000364806, 1.4928567994), 0.2, 0.5846909011, 44.4153090989)
                CenterArc((2.2000000328, 1.5000000224), 0.5, -179.4153090989, 20.3401427702)
                CenterArc((1.5461651967, 1.2500000082), 0.2, -89.9999999461, 110.9248336175)
                Line((0.6309087741, 1.0500000073), (1.5461651969, 1.0500000082))
                CenterArc((0.6309087739, 1.2500000073), 0.2, 138.8604886703, 131.1395113836)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a modular truss or frame component with a segmented diagonal lattice structure, featuring multiple rectangular openings and a stepped, elongated profile that angles downward from left to right.
def model_81145_bdb0ac6a_0043():
    """Model: Oxcart X-top v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.848850014, perimeter: 41.5663710715
            with BuildLine():
                Line((1.4000000209, -0.7000000015), (1.7500000265, -0.7000000077))
                CenterArc((1.7500000283, -0.6000000086), 0.0999999991, -90.0000010245, 90.0000010245)
                Line((1.8500000283, 0.6000000164), (1.8500000274, -0.6000000086))
                CenterArc((1.7500000283, 0.6000000164), 0.1, 0, 90)
                Line((1.4000000209, 0.7000000194), (1.7500000283, 0.7000000164))
                CenterArc((1.4000000209, 0.7500000112), 0.0499999918, 90, 180)
                Line((1.4000000209, 0.800000003), (1.4000000209, 1.4000000142))
                CenterArc((1.4000000209, 1.4500000216), 0.0500000075, 90, 180)
                Line((1.4000000209, 1.5000000291), (1.6000000236, 1.5000000235))
                CenterArc((1.6000000247, 1.5500000235), 0.05, -90.0000012807, 90.0000011448)
                Line((1.6500000247, 1.5500000234), (1.6500000271, 2.550000038))
                CenterArc((1.6000000271, 2.5500000381), 0.05, -0.0000001358, 89.9999991398)
                Line((1.4000000212, 2.6000000454), (1.6000000279, 2.6000000381))
                CenterArc((1.4000000209, 2.6500000395), 0.049999994, 90.0000004044, 180)
                Line((1.4000000208, 3.3000000506), (1.4000000205, 2.7000000335))
                CenterArc((1.3000000208, 3.3000000507), 0.1, -0.0000000337, 90.0000000337)
                Line((-1.3000000209, 3.4000000507), (1.3000000208, 3.4000000507))
                CenterArc((-1.3000000209, 3.3000000507), 0.1, 90, 90)
                Line((-1.4000000209, 2.7000000402), (-1.4000000209, 3.3000000507))
                CenterArc((-1.4000000209, 2.6500000395), 0.0500000007, -90, 180)
                Line((-1.4000000209, 2.6000000387), (-1.600000025, 2.6000000391))
                CenterArc((-1.6000000246, 2.5500000391), 0.05, 90.0000004269, 89.9999995731)
                Line((-1.6500000246, 1.5500000235), (-1.6500000246, 2.5500000391))
                CenterArc((-1.6000000246, 1.5500000235), 0.05, -180, 90.0000012807)
                Line((-1.4000000209, 1.5000000224), (-1.6000000235, 1.5000000235))
                CenterArc((-1.4000000209, 1.4500000216), 0.0500000007, -90, 180)
                Line((-1.4000000209, 0.8000000119), (-1.4000000209, 1.4000000209))
                CenterArc((-1.4000000209, 0.7500000112), 0.0500000007, -90, 180)
                Line((-1.7500000284, 0.7000000164), (-1.4000000209, 0.7000000104))
                CenterArc((-1.7500000284, 0.6000000164), 0.1, 90, 89.999999939)
                Line((-1.8500000284, 0.6000000165), (-1.8500000297, -0.6000000026))
                CenterArc((-1.7500000297, -0.6000000027), 0.1, 179.999999939, 90.0000002317)
                Line((-1.7500000294, -0.7000000027), (-1.4000000209, -0.7000000104))
                CenterArc((-1.4000000209, -0.7500000112), 0.0500000007, -90, 180)
                Line((-1.4000000209, -1.4000000209), (-1.4000000209, -0.8000000119))
                CenterArc((-1.4000000209, -1.4500000216), 0.0500000007, -90, 180)
                Line((-1.4000000209, -1.5000000224), (-1.6000000253, -1.5000000291))
                CenterArc((-1.6000000253, -1.5500000291), 0.05, 90, 90.0000000388)
                Line((-1.6500000253, -1.5500000291), (-1.6500000246, -2.5500000379))
                CenterArc((-1.6000000246, -2.5500000379), 0.05, -179.9999999612, 89.9999992497)
                Line((-1.6000000252, -2.6000000379), (-1.4000000209, -2.6000000387))
                CenterArc((-1.4000000209, -2.6500000395), 0.0500000007, -90, 180)
                Line((-1.4000000209, -2.7000000402), (-1.4000000203, -3.3000000001))
                CenterArc((-1.3000000203, -3.3), 0.1, -179.9999999557, 89.9999999557)
                Line((-1.3000000203, -3.4), (1.3000000203, -3.4))
                CenterArc((1.3000000203, -3.3), 0.1, -90, 89.9999999557)
                Line((1.4000000206, -2.700000038), (1.4000000203, -3.3000000001))
                CenterArc((1.4000000209, -2.6500000395), 0.0499999985, 90.0000021344, 179.9999975852)
                Line((1.400000019, -2.600000041), (1.6000000257, -2.6000000391))
                CenterArc((1.6000000253, -2.5500000391), 0.05, -89.9999995731, 89.9999995731)
                Line((1.6500000253, -2.5500000391), (1.6500000253, -1.550000029))
                CenterArc((1.6000000253, -1.550000029), 0.05, 0, 90)
                Line((1.4000000191, -1.500000029), (1.6000000253, -1.500000029))
                CenterArc((1.4000000209, -1.4500000216), 0.0500000074, 90.0000020069, 179.9999959954)
                Line((1.4000000191, -1.4000000142), (1.4000000209, -0.8000000209))
                CenterArc((1.4000000209, -0.7500000112), 0.0500000097, 90, 180)
            make_face()
            with BuildLine():
                Line((1.45, -0.2999999985), (1.45, 0.300000006))
                CenterArc((1.55, 0.300000006), 0.1, 0, 180)
                Line((1.65, -0.2999999985), (1.65, 0.300000006))
                CenterArc((1.55, -0.2999999985), 0.1, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.45, 0.300000006), (-1.45, -0.2999999985))
                CenterArc((-1.55, -0.2999999985), 0.1, 180, 180)
                Line((-1.65, -0.2999999985), (-1.65, 0.300000006))
                CenterArc((-1.55, 0.300000006), 0.1, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9500000142, 2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9500000142, 2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9500000142, -2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9500000142, -2.950000044), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.300000006, -2.5500000402), (0.300000006, -2.5500000402))
                CenterArc((-0.300000006, -2.3500000402), 0.2, 180, 90)
                Line((-0.500000006, -1.7500000208), (-0.500000006, -2.3500000402))
                CenterArc((-0.300000006, -1.7500000209), 0.2, 90, 89.9999999927)
                Line((0.300000006, -1.5500000209), (-0.300000006, -1.5500000209))
                CenterArc((0.300000006, -1.7500000209), 0.2, 0.0000000073, 89.9999999927)
                Line((0.500000006, -2.3500000402), (0.500000006, -1.7500000208))
                CenterArc((0.300000006, -2.3500000402), 0.2, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.500000006, 0.2999999792), (-0.500000006, -0.3000000402))
                CenterArc((-0.300000006, 0.2999999791), 0.2, 90, 89.9999999695)
                Line((0.300000006, 0.4999999791), (-0.300000006, 0.4999999791))
                CenterArc((0.300000006, 0.2999999791), 0.2, 0.0000000305, 89.9999999695)
                Line((0.500000006, -0.3000000402), (0.500000006, 0.2999999792))
                CenterArc((0.300000006, -0.3000000402), 0.2, -90, 90)
                Line((-0.300000006, -0.5000000402), (0.300000006, -0.5000000402))
                CenterArc((-0.300000006, -0.3000000402), 0.2, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.300000006, 2.5499999791), (-0.300000006, 2.5499999791))
                CenterArc((0.300000006, 2.3499999791), 0.2, 0.0000000305, 89.9999999695)
                Line((0.500000006, 1.7499999598), (0.500000006, 2.3499999792))
                CenterArc((0.300000006, 1.7499999598), 0.2, -90, 90)
                Line((-0.300000006, 1.5499999598), (0.300000006, 1.5499999598))
                CenterArc((-0.300000006, 1.7499999598), 0.2, 180, 90)
                Line((-0.500000006, 2.3499999792), (-0.500000006, 1.7499999598))
                CenterArc((-0.300000006, 2.3499999791), 0.2, 90, 89.9999999695)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a rectangular box or container with a diagonal internal partition or divider running through its length, creating a compartmentalized structure with an angled separation between two internal sections.
def model_81145_bdb0ac6a_0049():
    """Model: Oxcart X-standoff v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6357079773, perimeter: 3.1141592985
            with BuildLine():
                Line((-0.350000006, 0.4000000039), (-0.350000006, -0.3999999921))
                Line((-0.350000006, -0.3999999921), (0.3500000067, -0.400000006))
                CenterArc((0.3500000067, -0.300000006), 0.1, -90, 90)
                Line((0.4500000067, 0.300000006), (0.4500000067, -0.300000006))
                CenterArc((0.3500000067, 0.300000006), 0.1, 0, 90)
                Line((-0.350000006, 0.4000000039), (0.3500000067, 0.400000006))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a curved, bear-head-shaped bracket or clamp with two large circular holes and a central slot, featuring a smooth, organic form with textured surfaces and a dark finish.
def model_81146_08caa784_0000():
    """Model: Clip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1376171163, perimeter: 2.368138184
            with BuildLine():
                Line((0.1229073869, -0.5841090517), (0.7814545706, -0.4455385001))
                CenterArc((0.687705, 0), 0.455295, -78.1172538893, 54.403271159)
                Line((0.9946540683, -0.1196541041), (1.1045569267, -0.1831065489))
                CenterArc((0.7619999908, 0), 0.26162, -137.2539163322, 110.0371356618)
                CenterArc((0, 0), 0.5969, -78.1172538893, 60.8100495809)
            make_face()
            # Profile area: 0.7201356485, perimeter: 7.3751667138
            with BuildLine():
                CenterArc((0, 0), 0.5969, 78.1172538893, 203.7654922215)
                CenterArc((0, 0), 0.5969, -78.1172538893, 60.8100495809)
                CenterArc((0.7619999908, 0), 0.26162, 31.7242976814, 191.0217859864)
                Line((0.984530874, 0.1375682754), (1.0958013825, 0.2018684711))
                CenterArc((0.687705, 0), 0.455295, 26.3197063976, 51.7975474917)
                Line((0.1229073869, 0.5841090517), (0.7814545706, 0.4455385001))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.403225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a curved, boomerang-shaped bracket or connector with a hollow central void, featuring multiple angled faces and flanges at each end for mounting or assembly purposes.
def model_81549_8d959744_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.468612906, perimeter: 16.1397683088
            with BuildLine():
                CenterArc((3.5, 1.4), 1, 39.9662130438, 50.0337869562)
                Line((3.5, 2.4), (1, 2.4))
                Line((1, 2.4), (0, 1.4))
                Line((0, 1.4), (0, 0))
                Line((0, 0), (0.5, 0))
                CenterArc((0.5, 1), 1, -90, 60.9217865104)
                CenterArc((2.5974970091, -0.1664074318), 1.4, 75, 75.9217865104)
                Line((2.9598436722, 1.185888725), (4.4, 0.8))
                Line((4.4, 0.8), (6, 0.8))
                Line((6, 0.8), (6.5, 1.3))
                Line((6.5, 1.3), (6.5, 1.7))
                Line((6.5, 1.7), (5, 1.7))
                CenterArc((5, 2.6571428571), 0.9571428571, -140.0337869562, 50.0337869562)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a robotic arm joint or connector featuring an angular, bent tubular structure with a cylindrical main body and cubic end pieces, designed to articulate or pivot at the central bend with internal ribbing for structural reinforcement.
def model_81549_b0ace035_0000():
    """Model: body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.0759820167, perimeter: 34.0641549326
            with BuildLine():
                Line((0, 1.4), (0, 8.75))
                Line((0, 8.75), (-1.41, 10.16))
                Line((-1.41, 10.16), (-5.0107222631, 10.16))
                Line((-5.0107222631, 10.16), (-5.0107222631, 8.25))
                Line((-2.535, 8.25), (-5.0107222631, 8.25))
                CenterArc((-2.535, 7.615), 0.635, 0, 90)
                Line((-1.9, 2.545), (-1.9, 7.615))
                CenterArc((-2.535, 2.545), 0.635, -130.8954455861, 130.8954455861)
                Line((-2.9507222631, 2.065), (-5.1707222631, 2.065))
                Line((-5.1707222631, 2.065), (-5.1707222631, 1.4))
                Line((-5.1707222631, 1.4), (-3.7707222631, 0))
                Line((-1.4, 0), (-3.7707222631, 0))
                Line((0, 1.4), (-1.4, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=2.22
        extrude(amount=1.11, both=True)
    return part.part


# Description: This is an elliptical or oval-shaped structural component with a thin, curved shell featuring radial ribbing or support struts running from the center toward the perimeter, creating a lightweight framework similar to a boat hull or aircraft fuselage section.
def model_81969_8bc864bd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.072
        extrude(amount=0.072)
    return part.part


# Description: This is a dark blue 3D bracket or channel part with a wide-open rectangular slot running vertically through its center, featuring two parallel flanges on the left and right sides that form an inverted "U" or arch-like shape.
def model_81969_8bc864bd_0003():
    """Model: log"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6667476013, perimeter: 4.4784684702
            with BuildLine():
                Line((0.7, -1.698), (0.5081355932, 0))
                Line((0.5081355932, 0), (0.2500000037, 0))
                Line((0.2500000037, 0), (0, 0))
                Line((0, 0), (0, -0.6000000089))
                Line((0, -0.6000000089), (0.2538424778, -0.6000000089))
                Line((0.2538424778, -0.6000000089), (0.4, -1.698))
                Line((0.7, -1.698), (0.4, -1.698))
            make_face()
            # Profile area: 0.6667476013, perimeter: 4.4784684702
            with BuildLine():
                Line((0, 0), (-0.2500000037, 0))
                Line((-0.2500000037, 0), (-0.5081355932, 0))
                Line((-0.7, -1.698), (-0.5081355932, 0))
                Line((-0.7, -1.698), (-0.4, -1.698))
                Line((-0.2538424778, -0.6000000089), (-0.4, -1.698))
                Line((0, -0.6000000089), (-0.2538424778, -0.6000000089))
                Line((0, 0), (0, -0.6000000089))
            make_face()
        # Symmetric extrude, each_side=0.036
        extrude(amount=0.036, both=True)
    return part.part


# Description: This is a curved metal bracket or corner brace with a horizontal arm and a vertical downward-bent section, featuring a simple L-shaped profile with sharp edges.
def model_81972_a6710ac4_0002():
    """Model: frame v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0024867318, perimeter: 21.255332795
            with BuildLine():
                Line((0, 2), (0, 1.5))
                Line((0, 1.5), (7.5, 1.5))
                CenterArc((7.5, 0), 1.5, 20.3297249668, 69.6702750332)
                Line((8.906563228, 0.5211332704), (9.5, 0))
                CenterArc((7.5, 0), 2, 0, 90)
                Line((0, 2), (7.5, 2))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical shaft or rod with dark end caps or connectors on both ends, featuring a long, slender blue-metallic body typical of a mechanical linkage, drive shaft, or connector component used in assemblies.
def model_81980_55748cd2_0000():
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2503756413, perimeter: 4.7390209257
            with BuildLine():
                _nurbs_edge([(-0.1625423372, 0.5820849094), (-0.1576995845, 0.5939906313), (-0.1490524115, 0.6172561912), (-0.1391966958, 0.650516889), (-0.1322937134, 0.6915847667), (-0.1339068313, 0.7373925444), (-0.1452054035, 0.7775330383), (-0.1650238219, 0.8117614268), (-0.1913277639, 0.83969389), (-0.2210632533, 0.8607944215), (-0.2497235389, 0.8743092818), (-0.272006794, 0.879405616), (-0.2835549621, 0.8755025333), (-0.2821845432, 0.8625261174), (-0.2698254923, 0.8412550995), (-0.2518713371, 0.81336395), (-0.2351023778, 0.781288313), (-0.2259849935, 0.7481661454), (-0.2289661855, 0.7177141178), (-0.2443742242, 0.694235018), (-0.2692606463, 0.6818055786), (-0.2991325813, 0.6831489245), (-0.3292494939, 0.6987695287), (-0.3563891876, 0.7255772622), (-0.379211158, 0.7573142995), (-0.3975159286, 0.7864368601), (-0.4118031449, 0.8056493952), (-0.4227507812, 0.8094211753), (-0.4306369581, 0.7959065359), (-0.4351391302, 0.7672474699), (-0.4356040529, 0.7279757241), (-0.4311986117, 0.6838836866), (-0.4210945174, 0.6408063211), (-0.4046733738, 0.6032163289), (-0.3815630544, 0.5739575036), (-0.3515590511, 0.554728242), (-0.3219780415, 0.548008767), (-0.2966510802, 0.547951397), (-0.2783722458, 0.550124265), (-0.2688842777, 0.5517634933)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.2688842777, 0.5517634933), (0.205003503, -0.6073731842))
                _nurbs_edge([(0.205003503, -0.6073731842), (0.1982232789, -0.6192007031), (0.1858784891, -0.6422136131), (0.1710083181, -0.6748065939), (0.1584848184, -0.7144060156), (0.1548669985, -0.757447539), (0.1627733641, -0.7939993923), (0.1811134002, -0.8240368722), (0.2079729763, -0.8475553933), (0.2404589403, -0.8645813467), (0.2743065842, -0.8751902155), (0.3044383707, -0.8794982926), (0.3261846365, -0.8776362331), (0.3363162184, -0.8697285736), (0.3341475625, -0.8558719715), (0.3226637704, -0.8361124042), (0.3070560782, -0.8108191442), (0.2931510827, -0.7811047983), (0.2859824297, -0.749164296), (0.288073892, -0.718814128), (0.2985525232, -0.6954422205), (0.314753721, -0.6840964832), (0.3333154115, -0.688022423), (0.3515927574, -0.7067577613), (0.3685582366, -0.7351727025), (0.3841243471, -0.7657386021), (0.3986943586, -0.7903459555), (0.4126590747, -0.8021635205), (0.4258433663, -0.7977892211), (0.4372111266, -0.7783100855), (0.4452756812, -0.7474822536), (0.4483737309, -0.7104706461), (0.4449872573, -0.6723992906), (0.4340597644, -0.6369273661), (0.4149239943, -0.6064466751), (0.3872087224, -0.5823695133), (0.358046654, -0.5687748037), (0.3322301731, -0.5618599263), (0.3132682245, -0.5587063169), (0.3033495092, -0.557493592)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                Line((0.3033495092, -0.557493592), (-0.1625423372, 0.5820849094))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a dark blue/gray metal sheet or panel component with a rectangular base shape, featuring a curved or angled upper edge and what appears to be a ventilation slot or cutout on the right side.
def model_81997_a224b06d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.127154127, perimeter: 23.0027061015
            with BuildLine():
                CenterArc((9.0698850673, 2.3098111295), 3.0915141705, -95, 31.5253612255)
                CenterArc((0, 0), 10.4604925096, -2.5, 5)
                CenterArc((9.0698850673, -2.3098111295), 3.0915141705, 63.4746387745, 31.5253612255)
                Line((8.8004418535, 0.7699388962), (8.664603468, 0.7580545774))
                CenterArc((8.6471723195, 0.957293517), 0.2, -173.6827396036, 88.6827396036)
                CenterArc((0, 0), 8.5, 6.3172603964, 2.6827396036)
                Line((0, 0), (8.3953508951, 1.3296929528))
                Line((0, 0), (8.3953508951, -1.3296929528))
                CenterArc((0, 0), 8.5, -9, 2.6827396036)
                CenterArc((8.6471723195, -0.957293517), 0.2, 85, 88.6827396036)
                Line((8.8004418535, -0.7699388962), (8.664603468, -0.7580545774))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a dark metal bracket or mounting clip with an elongated vertical body featuring two circular holes for fastening and a curved hook or eye at the top for attachment or suspension.
def model_82012_c533307b_0000():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 64.3002054444, perimeter: 61.7768719933
            with BuildLine():
                Line((4, -19), (4, 0.9915710196))
                Line((4, 0.9915710196), (5, 0.9915710196))
                CenterArc((-0.0019057073, -0.8797741929), 5.3405049957, 20.5121524015, 69.4674021561)
                Line((0, 4.4607304628), (0, 3))
                CenterArc((0, 0), 3, -90, 180)
                Line((0, -3), (0, -9.5))
                CenterArc((0, -12.5), 3, -90, 180)
                Line((0, -15.5), (0, -19))
                Line((0, -19), (4, -19))
            make_face()
            # Profile area: 64.3032524126, perimeter: 61.7799917736
            with BuildLine():
                Line((0, -15.5), (0, -19))
                CenterArc((0, -12.5), 3, 90, 180)
                Line((0, -3), (0, -9.5))
                CenterArc((0, 0), 3, 90, 180)
                Line((0, 4.4607304628), (0, 3))
                CenterArc((-0.0019057073, -0.8797741929), 5.3405049957, 89.9795545576, 69.3919131699)
                Line((-4, 1.0017270828), (-5, 1.0017270828))
                Line((-4, 1.0017270828), (-4, -19))
                Line((-4, -19), (0, -19))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical tank or pressure vessel with a flat circular base and curved top surface, featuring a mesh or grid pattern overlay on its body and what appears to be internal structural ribbing or reinforcement details.
def model_82012_c533307b_0004():
    """Model: rod v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a cylindrical container or vessel with a curved, tapered body and an open top featuring an inward-angled elliptical rim or flange.
def model_82375_657b4b9f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8912221556, perimeter: 9.3057859202
            with Locations((5.5880001783, -1.2700000405)):
                Circle(1.4810618286)
        # OneSide extrude, distance=2.032
        extrude(amount=2.032)
    return part.part


# Description: This is a cylindrical rod or pin with a slightly tapered design, featuring rounded ends and a uniform diameter along its length, appearing to be a simple mechanical component such as a dowel pin, shaft, or connector rod.
def model_82485_d6d73980_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.8912217157, perimeter: 27.1307941564
            with BuildLine():
                CenterArc((20.32, 0), 2.413, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((20.32, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-91.44
        extrude(amount=-91.44)
    return part.part


# Description: This is a cylindrical sleeve or tube with a uniform diameter and height, featuring a curved or slightly tapered sidewall and an open top with a flat or slightly beveled rim.
def model_82491_79dd5db3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.1041014668, perimeter: 23.8074537752
            Circle(3.7890739508)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical shaft or rod with rounded end caps, featuring longitudinal grooves or flutes running along its length and threaded or hexagonal socket holes at both ends.
def model_82512_252da752_0000():
    """Model: lefthook"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0001767146, perimeter: 0.0471238898
            with Locations((-0.3499999922, 0.1999999955)):
                Circle(0.0075)
        # OneSide extrude, distance=0.1635
        extrude(amount=0.1635)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a trapezoidal profile, featuring internal diagonal reinforcement ribs or webs running across its surface.
def model_82512_252da752_0004():
    """Model: glass"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1311766841, perimeter: 5.1696046823
            with BuildLine():
                Line((0.1136542146, -0.1000000015), (-0.4590152029, -0.1000000015))
                Line((0.1136542146, -0.1000000015), (-0.1000000015, 0.6973683882))
                Line((-0.6726694189, 0.6973683882), (-0.1000000015, 0.6973683882))
                Line((-0.4590152029, -0.1000000015), (-0.6726694189, 0.6973683882))
            make_face()
            with BuildLine():
                Line((-0.1353851445, 0.6418667802), (0.0500000007, -0.0500000007))
                Line((0.0500000007, -0.0500000007), (-0.420525817, -0.0500000007))
                Line((-0.420525817, -0.0500000007), (-0.6056526011, 0.6418667802))
                Line((-0.6056526011, 0.6418667802), (-0.1353851445, 0.6418667802))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3254518071, perimeter: 2.3732728457
            with BuildLine():
                Line((-0.6056526011, 0.6418667802), (-0.1353851445, 0.6418667802))
                Line((-0.420525817, -0.0500000007), (-0.6056526011, 0.6418667802))
                Line((0.0500000007, -0.0500000007), (-0.420525817, -0.0500000007))
                Line((-0.1353851445, 0.6418667802), (0.0500000007, -0.0500000007))
            make_face()
        # OneSide extrude, distance=0.012
        extrude(amount=0.012)
    return part.part


# Description: This is a mounting bracket or support structure featuring a flat, elongated top plate with a large spherical or hemispherical dome protruding downward, designed to provide structural support or housing for a spherical component while maintaining a low-profile footprint.
def model_83108_0e20d25b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 71.5136535162, perimeter: 89.7468774724
            with BuildLine():
                Line((0, 0), (0, -0.6))
                Line((0, -0.6), (8.7148733879, -0.6))
                CenterArc((8.7148733879, -1.6), 1, 0, 90)
                Line((9.7148733879, -4.3), (9.7148733879, -1.6))
                CenterArc((14.75, -4.3), 5.0351266121, 180, 180)
                Line((19.7851266121, -4.3), (19.7851266121, -1.6))
                CenterArc((20.7851266121, -1.6), 1, 90, 90)
                Line((20.7851266121, -0.6), (29.5, -0.6))
                Line((29.5, 0), (29.5, -0.6))
                Line((0, 0), (29.5, 0))
            make_face()
            with BuildLine():
                CenterArc((14.75, -4.3), 2.7465720689, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a hexagonal or octagonal ring-shaped connector or spacer with a large central hole, featuring curved inner and outer surfaces with ribbed or textured detailing on the interior surfaces.
def model_83109_0311c05e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.5095467448, perimeter: 62.6124344442
            with BuildLine():
                Line((5.8867513459, 3.2679491924), (0.1132486541, 6.7320508076))
                Line((0.1132486541, 6.7320508076), (-5.7735026919, 3.4641016151))
                Line((-5.7735026919, 3.4641016151), (-5.8867513459, -3.2679491924))
                Line((-5.8867513459, -3.2679491924), (-0.1132486541, -6.7320508076))
                Line((-0.1132486541, -6.7320508076), (5.7735026919, -3.4641016151))
                Line((5.7735026919, -3.4641016151), (5.8867513459, 3.2679491924))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5355339059, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered, curved top edge that flares outward, featuring a hollow interior and smooth curved sidewalls.
def model_83110_487f8396_0003():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.0446616728, perimeter: 11.780972451
            Circle(1.875)
        # OneSide extrude, distance=3.25
        extrude(amount=3.25)
    return part.part


# Description: This is a hinged blue and dark gray composite part with a symmetrical butterfly or bow-tie shape, featuring two angled wing-like sections connected by a central articulated joint that allows the wings to fold inward.
def model_83112_fbb40a06_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 427.8, perimeter: 279.1822971503
            with BuildLine():
                Line((95, 0), (68.25, 0))
                CenterArc((68.25, -2), 2, 90, 90)
                Line((66.25, -2), (66.25, -21.8))
                CenterArc((64.25, -21.8), 2, -90, 90)
                Line((30.75, -23.8), (64.25, -23.8))
                CenterArc((30.75, -21.8), 2, 180, 90)
                Line((28.75, -2), (28.75, -21.8))
                CenterArc((26.75, -2), 2, 0, 90)
                Line((0, 0), (26.75, 0))
                Line((0, 0), (0, -3))
                Line((0, -3), (20.75, -3))
                CenterArc((20.75, -8), 5, 0, 90)
                Line((25.75, -8), (25.75, -21.8))
                CenterArc((30.75, -21.8), 5, 180, 90)
                Line((64.25, -26.8), (30.75, -26.8))
                CenterArc((64.25, -21.8), 5, -90, 90)
                Line((69.25, -8), (69.25, -21.8))
                CenterArc((74.25, -8), 5, 90, 90)
                Line((95, -3), (74.25, -3))
                Line((95, 0), (95, -3))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a hexagonal ring or bushing with a hollow center bore, featuring a geometric hexagonal outer profile and a large circular opening through its middle, commonly used as a structural connector or spacer component.
def model_83219_f6c9d6bc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 67.8184768998, perimeter: 76.4492475327
            with BuildLine():
                Line((6.5, -3.7527767497), (6.5, 3.7527767497))
                Line((6.5, 3.7527767497), (0, 7.5055534995))
                Line((0, 7.5055534995), (-6.5, 3.7527767497))
                Line((-6.5, 3.7527767497), (-6.5, -3.7527767497))
                Line((-6.5, -3.7527767497), (0, -7.5055534995))
                Line((0, -7.5055534995), (6.5, -3.7527767497))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5)
    return part.part


# Description: This is a whistle or air-flow device featuring a spherical/bulbous resonance chamber (dark gray) connected to a flat rectangular platform or flange (light blue) with an angled nozzle or outlet spout on one end.
def model_83230_50d5eae5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 411.0200885142, perimeter: 215.6247719319
            with BuildLine():
                Line((0, 0), (0, -3))
                Line((0, -3), (21.9, -3))
                Line((21.9, -13.2), (21.9, -3))
                CenterArc((32.5, -13.2), 10.6, 180, 180)
                Line((43.1, -13.2), (43.1, -3))
                Line((43.1, -3), (65, -3))
                Line((65, 0), (65, -3))
                Line((0, 0), (65, 0))
            make_face()
            with BuildLine():
                CenterArc((32.5, -13.2), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a hexagonal ring or bushing with a large central hole and a cylindrical bore, featuring faceted external surfaces and internal radial webbing or fins that provide structural support while minimizing material weight.
def model_83232_0c29683a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 53.3395581649, perimeter: 58.7791305347
            with BuildLine():
                Line((-1.2141016151, -5.897114317), (4.5, -4))
                Line((4.5, -4), (5.7141016151, 1.897114317))
                Line((5.7141016151, 1.897114317), (1.2141016151, 5.897114317))
                Line((1.2141016151, 5.897114317), (-4.5, 4))
                Line((-4.5, 4), (-5.7141016151, -1.897114317))
                Line((-5.7141016151, -1.897114317), (-1.2141016151, -5.897114317))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.6055512755, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a flat parallelogram or slanted rectangular plate with a beveled or chamfered edge on the left side and an internal diagonal line, rendered in a 3D perspective view.
def model_83259_487d379e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 160, perimeter: 56
            with BuildLine():
                Line((-10, 4), (-10, -4))
                Line((-10, -4), (10, -4))
                Line((10, -4), (10, 4))
                Line((10, 4), (-10, 4))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a flat rectangular panel or cover plate with a slightly curved or beveled top edge and mounting flanges on the sides, appearing to be a protective enclosure or duct component with a streamlined aerodynamic design.
def model_83259_487d379e_0004():
    """Model: Zijschotten"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24, perimeter: 22
            with BuildLine():
                Line((6.7740829037, 3.7132491458), (6.7740829037, 0.7132491458))
                Line((6.7740829037, 0.7132491458), (14.7740829037, 0.7132491458))
                Line((14.7740829037, 0.7132491458), (14.7740829037, 3.7132491458))
                Line((14.7740829037, 3.7132491458), (6.7740829037, 3.7132491458))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a tapered cylindrical rod or shaft with a slightly conical shape that narrows along its length, featuring a smooth, featureless surface with no holes, slots, or flanges.
def model_83337_74fe9172_0000():
    """Model: Layens Frame End Bars"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 112.0965499999, perimeter: 86.132411335
            with BuildLine():
                CenterArc((3.4925, 30.63875), 0.3175, -90, 90)
                Line((3.81, 30.63875), (3.81, 39.52875))
                Line((3.81, 39.52875), (0, 39.52875))
                Line((0, 39.52875), (0, 30.63875))
                CenterArc((0.3175, 30.63875), 0.3175, 180, 90)
                CenterArc((0.3175, 30.00375), 0.3175, 0, 90)
                Line((0.635, 30.00375), (0.635, 0))
                Line((0.635, 0), (3.175, 0))
                Line((3.175, 30.00375), (3.175, 0))
                CenterArc((3.4925, 30.00375), 0.3175, 90, 90)
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


# Description: This is a parallelogram-shaped flat plate or bar with a slanted rectangular form, featuring clean edges and a uniform thickness throughout, with no holes, slots, or other features—appearing to be a simple structural component or spacer element.
def model_83337_74fe9172_0001():
    """Model: Board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 362.7121778, perimeter: 99.38004
            with BuildLine():
                Line((12.6999998093, 40.80002), (12.6999998093, 0))
                Line((12.6999998093, 0), (21.5899998093, 0))
                Line((21.5899998093, 0), (21.5899998093, 40.80002))
                Line((21.5899998093, 40.80002), (12.6999998093, 40.80002))
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


# Description: This is a long, narrow sheet metal channel or trim strip with a curved/formed profile, featuring flanged edges along its length and tapered end sections.
def model_83338_b9bb889f_0000():
    """Model: Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 58.7935169019, perimeter: 68.7148670025
            with BuildLine():
                Line((2.69875, -2.54), (2.69875, -4.445))
                Line((2.69875, -4.445), (33.655, -4.445))
                Line((33.655, -4.445), (33.655, -2.54))
                Line((33.655, -2.54), (2.69875, -2.54))
            make_face()
            with BuildLine():
                CenterArc((5.23875, -3.4925), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((13.890625, -3.4925), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((31.115, -3.4925), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.463125, -3.4925), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a circular disc or wheel with a flat front face and a ribbed or finned cylindrical rim on the back, commonly used as a pulley, fan blade, or similar rotational component.
def model_83367_f3132ff3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is an elliptical or oval-shaped structural panel or cover with a shallow dome profile, featuring a reinforced perimeter flange and internal ribbing or support structures running across its surface.
def model_83378_2dc861a1_0001():
    """Model: seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 993.1466590311, perimeter: 111.7150347617
            Circle(17.78)
        # OneSide extrude, distance=1.8288
        extrude(amount=1.8288)
    return part.part


# Description: This is a cylindrical or capsule-shaped structural component featuring a hollow central core with internal ribbing/bracing, rounded ends, and what appears to be a mounting flange or opening at the top.
def model_83384_bb9418ee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 41 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 155.562760969, perimeter: 66.0516037338
            with BuildLine():
                CenterArc((37.5, 17.5), 2.5, 90, 90)
                Line((35, 6.0470939801), (35, 17.5))
                CenterArc((37.5, 6.0470939801), 2.5, 180, 90)
                Line((42.5, 3.5470939801), (37.5, 3.5470939801))
                CenterArc((42.5, 6.0470939801), 2.5, -90, 90)
                Line((45, 17.5), (45, 6.0470939801))
                CenterArc((42.5, 17.5), 2.5, 0, 90)
                Line((37.5, 20), (42.5, 20))
            make_face()
            with BuildLine():
                Line((43.3000006452, 16.3000002429), (43.3000006452, 16.4000002444))
                Line((42.0000006258, 16.3000002429), (43.3000006452, 16.3000002429))
                Line((42.0000006258, 16.4000002444), (42.0000006258, 16.3000002429))
                Line((43.3000006452, 16.4000002444), (42.0000006258, 16.4000002444))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((43.3000006452, 16.7000002488), (42.0000006258, 16.7000002488))
                Line((42.0000006258, 16.7000002488), (42.0000006258, 16.8000002503))
                Line((42.0000006258, 16.8000002503), (43.3000006452, 16.8000002503))
                Line((43.3000006452, 16.8000002503), (43.3000006452, 16.7000002488))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((43.3000006452, 16.5000002459), (43.3000006452, 16.6000002474))
                Line((42.0000006258, 16.5000002459), (43.3000006452, 16.5000002459))
                Line((42.0000006258, 16.6000002474), (42.0000006258, 16.5000002459))
                Line((43.3000006452, 16.6000002474), (42.0000006258, 16.6000002474))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((37.2268484269, 16), (37.2268484269, 16.787832123))
                Line((37.2268484269, 16.787832123), (38.1759619923, 16.787832123))
                Line((38.1759619923, 16.787832123), (38.1759619923, 16))
                Line((38.1759619923, 16), (37.2268484269, 16))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((40, 16.5643565288), 0.8855280645, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a structural enclosure or housing component with an elongated rectangular body featuring curved surfaces, a cylindrical opening or port on the left side, and aerodynamic tapering, commonly used in aerospace or industrial equipment applications.
def model_83432_a7f85698_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4463495408, perimeter: 6.5707963268
            with BuildLine():
                CenterArc((7.25, 0.25), 0.25, -180, 90)
                Line((7.25, 0), (9.25, 0))
                CenterArc((9.25, 0.25), 0.25, -90, 90)
                Line((9.5, 0.25), (9.5, 0.75))
                CenterArc((9.25, 0.75), 0.25, 0, 90)
                Line((9.25, 1), (7.25, 1))
                CenterArc((7.25, 0.75), 0.25, 90, 90)
                Line((7, 0.75), (7, 0.25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat rectangular enclosure or mounting plate with a large central rectangular opening/window and multiple circular mounting holes positioned around the perimeter, featuring a parallelogram-like perspective shape in the 3D view.
def model_84025_ec3401ea_0000():
    """Model: Fillplate1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 88.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 23.6690266447, perimeter: 27.9398223686
            with BuildLine():
                Line((-46.9042121114, -42.7566838488), (-46.9042121114, -38.7566838488))
                Line((-46.9042121114, -38.7566838488), (-53.1042121114, -38.7566838488))
                Line((-53.1042121114, -38.7566838488), (-53.1042121114, -42.7566838488))
                Line((-53.1042121114, -42.7566838488), (-46.9042121114, -42.7566838488))
            make_face()
            with BuildLine():
                CenterArc((-47.6042121114, -39.5566838488), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-47.6042121114, -41.9566838488), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52.4042121114, -41.9566838488), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52.4042121114, -39.5566838488), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a trapezoidal appearance, featuring a simple planar design with no holes, slots, or additional features.
def model_84025_ec3401ea_0003():
    """Model: WoodPlate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 91.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4141.381425427, perimeter: 284.7481641637
            with BuildLine():
                Line((-8.0025540358, -60.8741252318), (-8.0025540358, -10.8741252318))
                Line((-8.0025540358, -10.8741252318), (-92.0025540358, -10.8741252318))
                Line((-92.0025540358, -10.8741252318), (-92.0025540358, -60.8741252318))
                Line((-92.0025540358, -60.8741252318), (-74.5024931617, -60.8741252318))
                Line((-74.5024931617, -60.8741252318), (-74.5025015358, -52.50004665))
                Line((-74.5025015358, -52.50004665), (-67.5025015358, -52.50003965))
                Line((-67.5025015358, -52.50003965), (-67.5024931617, -60.8741252318))
                Line((-67.5024931617, -60.8741252318), (-8.0025540358, -60.8741252318))
            make_face()
            # Profile area: 58.6185745731, perimeter: 30.7481641637
            with BuildLine():
                Line((-67.5025015358, -52.50003965), (-67.5024931617, -60.8741252318))
                Line((-74.5025015358, -52.50004665), (-67.5025015358, -52.50003965))
                Line((-74.5024931617, -60.8741252318), (-74.5025015358, -52.50004665))
                Line((-74.5024931617, -60.8741252318), (-67.5024931617, -60.8741252318))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a rectangular panel or enclosure cover with a parallelogram shape, featuring a recessed central area, rounded corners, mounting holes at the corners, and a dark blue finish typical of industrial or electronic equipment housings.
def model_84025_ec3401ea_0005():
    """Model: Mountingplate1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 124.6438055098, perimeter: 59.7079632679
            with BuildLine():
                CenterArc((0.5, 0.5), 0.5, 180, 90)
                Line((0.5, 0), (15.5, 0))
                CenterArc((15.5, 0.5), 0.5, -90, 90)
                Line((16, 0.5), (16, 7.5))
                CenterArc((15.5, 7.5), 0.5, 0, 90)
                Line((15.5, 8), (0.5, 8))
                CenterArc((0.5, 7.5), 0.5, 90, 90)
                Line((0, 7.5), (0, 0.5))
            make_face()
            with BuildLine():
                CenterArc((1.5, 1.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 6.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.5, 6.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.5, 1.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a suppressor or silencer — a cylindrical tube with a tapered front end, designed to be mounted on a firearm barrel to reduce noise and muzzle flash.
def model_84025_ec3401ea_0009():
    """Model: M16*120"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((3.4709874554, -8.6453298657)):
                Circle(0.8)
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a tapered cylindrical rod or stylus with a long, slender body that gradually narrows from a thicker upper section to a fine pointed tip at the lower end.
def model_84025_ec3401ea_0017():
    """Model: rail1000"""
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
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 86), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.0991919555, perimeter: 10.033908589
            with BuildLine():
                Line((2.3, -0.4279768942), (2.3, 0))
                Line((2.3, 0), (0, 0))
                Line((0, 0), (0, -0.4279768942))
                _nurbs_edge([(0, -0.4279768942), (0.0190644027, -0.4292694854), (0.0560597826, -0.4321504926), (0.1081525951, -0.4373594831), (0.170796685, -0.4460829281), (0.2377524042, -0.4600030682), (0.2934978367, -0.4770625885), (0.3384130343, -0.4974858429), (0.3732112067, -0.5216214696), (0.399077907, -0.5499806374), (0.4176773344, -0.58322999), (0.4308343099, -0.6220812043), (0.4403017677, -0.6672005374), (0.4474564927, -0.7191098321), (0.4531641958, -0.7780858625), (0.4578504731, -0.844047649), (0.4615202428, -0.9164480263), (0.4637919164, -0.9941487587), (0.4639296492, -1.0753199582), (0.4608550053, -1.1572626287), (0.4533147914, -1.2367293275), (0.4400903445, -1.3103672777), (0.4201872718, -1.3751075398), (0.3930493493, -1.4286034323), (0.3587348578, -1.4695975286), (0.3181950243, -1.4984731335), (0.2730925226, -1.5169796238), (0.2253926261, -1.5275529788), (0.1770452639, -1.5327956183), (0.1295957419, -1.5348411844), (0.0839305755, -1.5349303638), (0.0491787536, -1.5339461124), (0.0241769491, -1.5327090613), (0.0079804312, -1.5316633153), (0, -1.5310851653)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((0, -1.5310851653), (0, -1.9))
                CenterArc((0.3, -1.9), 0.3, 180, 90)
                Line((0.3, -2.2), (2, -2.2))
                CenterArc((2, -1.9), 0.3, -90, 90)
                Line((2.3, -1.9), (2.3, -1.5310851653))
                _nurbs_edge([(2.3, -0.4279768942), (2.2809355973, -0.4292694854), (2.2439402174, -0.4321504926), (2.1918474049, -0.4373594831), (2.129203315, -0.4460829281), (2.0622475958, -0.4600030682), (2.0065021633, -0.4770625885), (1.9615869657, -0.4974858429), (1.9267887933, -0.5216214696), (1.900922093, -0.5499806374), (1.8823226656, -0.58322999), (1.8691656901, -0.6220812043), (1.8596982323, -0.6672005374), (1.8525435073, -0.7191098321), (1.8468358042, -0.7780858625), (1.8421495269, -0.844047649), (1.8384797572, -0.9164480263), (1.8362080836, -0.9941487587), (1.8360703508, -1.0753199582), (1.8391449947, -1.1572626287), (1.8466852086, -1.2367293275), (1.8599096555, -1.3103672777), (1.8798127282, -1.3751075398), (1.9069506507, -1.4286034323), (1.9412651422, -1.4695975286), (1.9818049757, -1.4984731335), (2.0269074774, -1.5169796238), (2.0746073739, -1.5275529788), (2.1229547361, -1.5327956183), (2.1704042581, -1.5348411844), (2.2160694245, -1.5349303638), (2.2508212464, -1.5339461124), (2.2758230509, -1.5327090613), (2.2920195688, -1.5316633153), (2.3, -1.5310851653)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)
    return part.part


# Description: This is a flat sheet metal bracket or mounting plate with a parallelogram shape, featuring a rectangular notch cut out from the upper right corner and bent edges for structural rigidity.
def model_84025_ec3401ea_0019():
    """Model: freesplaat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 89.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4141.3814254267, perimeter: 284.7481641637
            with BuildLine():
                Line((-74.5025015358, -52.50004665), (-74.5024931617, -60.8741252318))
                Line((-67.5025015358, -52.50003965), (-74.5025015358, -52.50004665))
                Line((-67.5024931617, -60.8741252318), (-67.5025015358, -52.50003965))
                Line((-67.5024931617, -60.8741252318), (-8.0025540358, -60.8741252318))
                Line((-8.0025540358, -60.8741252318), (-8.0025540358, -10.8741252318))
                Line((-8.0025540358, -10.8741252318), (-92.0025540358, -10.8741252318))
                Line((-92.0025540358, -60.8741252318), (-92.0025540358, -10.8741252318))
                Line((-92.0025540358, -60.8741252318), (-74.5024931617, -60.8741252318))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical reinforced belt or loop with an elliptical cross-section, featuring a solid dark core material reinforced with a blue mesh or woven fabric outer layer for structural integrity and durability.
def model_84129_211748cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 191.3289595936, perimeter: 152.476220724
            with BuildLine():
                CenterArc((0, 0), 13.388483907, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 10.8788603252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.2
        extrude(amount=2.2, both=True)
    return part.part


# Description: This is a long, rectangular steel bar or channel with a uniform prismatic shape, featuring a slightly angled or beveled end on the left side and a flat right end, designed for structural or assembly applications.
def model_84608_204c01e6_0000():
    """Model: Stootlat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 20.8
            with BuildLine():
                Line((4.4176003203, -1.8077924464), (4.4176003203, -2.2077924464))
                Line((4.4176003203, -2.2077924464), (14.4176003203, -2.2077924464))
                Line((14.4176003203, -2.2077924464), (14.4176003203, -1.8077924464))
                Line((14.4176003203, -1.8077924464), (4.4176003203, -1.8077924464))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a flat, dark blue parallelogram-shaped plate with a simple geometric form and no additional features such as holes, slots, or curves.
def model_84608_204c01e6_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((5, -5), (-5, -5))
                Line((5, 5), (5, -5))
                Line((-5, 5), (5, 5))
                Line((-5, -5), (-5, 5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a parallelogram-shaped flat plate or sheet metal component with a skewed rectangular form and a diagonal line or ridge feature running across its surface.
def model_84608_204c01e6_0005():
    """Model: Basisplaat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1508.8783025048, perimeter: 156.5654703086
            with BuildLine():
                Line((59.1353138536, -9.9132717987), (15.1805947097, -9.9132717987))
                Line((59.1353138536, 24.4147442117), (59.1353138536, -9.9132717987))
                Line((15.1805947097, 24.4147442117), (59.1353138536, 24.4147442117))
                Line((15.1805947097, -9.9132717987), (15.1805947097, 24.4147442117))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a long tubular body, featuring a rounded end cap and surface texturing/markings along its length, designed to attach to a firearm barrel.
def model_85195_c6ef0067_0005():
    """Model: stud v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


# Description: This is a torus (donut-shaped ring) with a smooth, curved geometry featuring a central hole and a textured or meshed surface finish across its outer diameter.
def model_85195_c6ef0067_0007():
    """Model: washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5292030703, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a wheel or steering wheel rim with an elliptical/oval shape, featuring three large oval holes for weight reduction, a dark gray/black rim structure, and blue triangular reinforcement sections or spokes integrated into the design.
def model_85200_70e166c4_0006():
    """Model: Cylinder piping tube glanse packing v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.1119888046, perimeter: 17.2824767844
            with BuildLine():
                CenterArc((-1.6, 0), 0.6, 104.4775121859, 151.0449756281)
                Line((-1.75, -0.5809475019), (-0.25, -0.9682458366))
                CenterArc((0, 0), 1, -104.4775121859, 28.9550243719)
                Line((0.25, -0.9682458366), (1.75, -0.5809475019))
                CenterArc((1.6, 0), 0.6, -75.5224878141, 151.0449756281)
                Line((0.25, 0.9682458366), (1.75, 0.5809475019))
                CenterArc((0, 0), 1, 75.5224878141, 28.9550243719)
                Line((-1.75, 0.5809475019), (-0.25, 0.9682458366))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6, 0), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6, 0), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a hollow tubular body, featuring longitudinal grooves or ridges running along its length and a rounded/domed end cap on one side.
def model_85631_f44b2bdc_0000():
    """Model: pipe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.9344556752, perimeter: 43.8880493706
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


# Description: This is a flat, thin parallelogram-shaped plate with a uniformly sloped geometry and no additional features such as holes or slots.
def model_85637_45bb38ad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.49, perimeter: 17.2
            with BuildLine():
                Line((4.3, -4.3), (0, -4.3))
                Line((4.3, 0), (4.3, -4.3))
                Line((0, 0), (4.3, 0))
                Line((0, -4.3), (0, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender hexagonal or angular cross-section, featuring a tapered or pointed end at the top and a slight base or collar at the bottom.
def model_85638_2ab1040c_0001():
    """Model: MontantArr"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 296.5045706706, perimeter: 156.3756982304
            with BuildLine():
                Line((15.6550109867, -5.3886710578), (28.5268805785, 67.6113289422))
                Line((28.5268805785, 67.6113289422), (24.4651741309, 67.6113289422))
                Line((24.4651741309, 67.6113289422), (11.5933045392, -5.3886710578))
                Line((11.5933045392, -5.3886710578), (15.6550109867, -5.3886710578))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a beveled edge on one side and a slightly raised or stepped rim around its perimeter, appearing to be a shallow tray or mounting base component.
def model_85638_2ab1040c_0002():
    """Model: MarcheSup"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 960, perimeter: 128
            with BuildLine():
                Line((-17.4445802829, -12.1303976114), (-57.4445802829, -12.1303976114))
                Line((-17.4445802829, 11.8696023886), (-17.4445802829, -12.1303976114))
                Line((-57.4445802829, 11.8696023886), (-17.4445802829, 11.8696023886))
                Line((-57.4445802829, -12.1303976114), (-57.4445802829, 11.8696023886))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a long, slender rectangular prism or beam with a slightly tapered top end and vertical slot or channel running along its length, appearing to be a structural support or mounting rail component.
def model_85638_2ab1040c_0003():
    """Model: Montant1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 93.4192482935, perimeter: 54.8330370418
            with BuildLine():
                Line((4.0555205563, 23), (0, 0))
                Line((0, 0), (4.0617064475, 0))
                Line((4.0617064475, 0), (8.1172270038, 23))
                Line((8.1172270038, 23), (4.0555205563, 23))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat, rectangular parallelogram-shaped plate or platform with a trapezoidal profile, featuring a beveled or angled edge on one end and internal diagonal reinforcement ribs or webbing across its top surface.
def model_85638_2ab1040c_0004():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 560, perimeter: 108
            with BuildLine():
                Line((40, -14), (0, -14))
                Line((40, 0), (40, -14))
                Line((0, 0), (40, 0))
                Line((0, -14), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or band with a smooth outer surface and a hollow elliptical center, featuring a textured or mesh-patterned outer rim and a dark inner surface.
def model_86099_c101852f_0000():
    """Model: washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a tapered cylindrical shaft or pin with a pointed conical tip at one end, featuring a gradually reducing diameter along its length.
def model_86296_8a6ed4d3_0001():
    """Model: PIN"""
    with BuildPart() as part:
        # Sketch4 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0763, perimeter: 3.1808318916
            with BuildLine():
                Line((-0.015, 1.05), (-0.025, 0.93))
                Line((-0.025, 0.93), (-0.025, -0.5))
                Line((-0.025, -0.5), (0.025, -0.5))
                Line((0.025, -0.5), (0.025, 0.93))
                Line((0.015, 1.05), (0.025, 0.93))
                Line((0.015, 1.05), (-0.015, 1.05))
            make_face()
        # Symmetric extrude, full_length=True, total=0.02
        extrude(amount=0.01, both=True)
    return part.part


# Description: This is a geometric polyhedron or faceted block with an elongated hexagonal profile, featuring a twisted or saddle-shaped geometry with alternating dark and light blue faceted surfaces that create a complex, asymmetrical three-dimensional form.
def model_86296_8a6ed4d3_0002():
    """Model: BODY"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.12075, perimeter: 1.4954069196
            with BuildLine():
                Line((-0.23, 0.5), (0, 0.53))
                Line((-0.23, 0), (-0.23, 0.5))
                Line((-0.12, -0.02), (-0.23, 0))
                Line((0, 0), (-0.12, -0.02))
                Line((0, 0.53), (0, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=0.65
        extrude(amount=0.325, both=True)
    return part.part


# Description: Three identical elongated hexagonal prisms with angled top surfaces and a central longitudinal slot or groove running along their length.
def model_86296_8a6ed4d3_0003():
    """Model: TERMINAL"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.046, perimeter: 1.03
            with BuildLine():
                Line((-0.0575, 0.4), (-0.0575, 0))
                Line((-0.0575, 0), (0.0575, 0))
                Line((0.0575, 0), (0.0575, 0.4))
                Line((0.0575, 0.4), (-0.0575, 0.4))
            make_face()
            # Profile area: 0.032, perimeter: 0.96
            with BuildLine():
                Line((-0.269, 0.4), (-0.269, 0))
                Line((-0.269, 0), (-0.189, 0))
                Line((-0.189, 0), (-0.189, 0.4))
                Line((-0.189, 0.4), (-0.269, 0.4))
            make_face()
            # Profile area: 0.032, perimeter: 0.96
            with BuildLine():
                Line((0.189, 0.4), (0.189, 0))
                Line((0.189, 0), (0.269, 0))
                Line((0.269, 0), (0.269, 0.4))
                Line((0.269, 0.4), (0.189, 0.4))
            make_face()
        # TwoSides offset extrude, full=-0.175, trim=-0.12
        extrude(amount=-0.175)
        extrude(sk.sketch, amount=-0.12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal bracket or channel with an elongated, arrow-like profile featuring a pointed left end, a flat top surface (shown in light blue), a deeper dark body section, and what appears to be a slot or opening on the lower left side.
def model_86296_8a6ed4d3_0014():
    """Model: TERMINAL (2)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0474323152, perimeter: 3.785627967
            with BuildLine():
                Line((-0.3707249094, -0.0127), (0.3707249094, -0.0127))
                Line((0.3707249094, -0.0127), (0.4247273272, -0.55))
                Line((0.4247273272, -0.55), (0.45, -0.5474599192))
                Line((0.45, -0.5474599192), (0.3937, 0.0127))
                Line((0.3937, 0.0127), (-0.3937, 0.0127))
                Line((-0.45, -0.5474599192), (-0.3937, 0.0127))
                Line((-0.4247273272, -0.55), (-0.45, -0.5474599192))
                Line((-0.3707249094, -0.0127), (-0.4247273272, -0.55))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a long, slender hexagonal bar or shaft with a tapered or angled cutting edge at one end, resembling a turning tool or lathe insert holder with a prismatic geometric profile.
def model_86296_8a6ed4d3_0015():
    """Model: pin"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0252, perimeter: 0.96
            with BuildLine():
                Line((-0.13, 0.42), (-0.13, 0))
                Line((-0.13, 0), (-0.07, 0))
                Line((-0.07, 0), (-0.07, 0.42))
                Line((-0.07, 0.42), (-0.13, 0.42))
            make_face()
        # TwoSides offset extrude, full=1.3125, trim=1.2875
        extrude(amount=1.3125)
        extrude(sk.sketch, amount=1.2875, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends featuring two symmetrical spherical end caps or flanges with radial grooves or ribs, and a smooth central body with a horizontal slot or keyway running along its length.
def model_86296_8a6ed4d3_0019():
    """Model: REGIN (1)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0028274334, perimeter: 0.5654866776
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.04, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.66
        extrude(amount=0.33, both=True)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a long, slender body that gradually narrows from a thicker end to a pointed or sharpened end, featuring a smooth conical taper along its length.
def model_86704_3f8f3bfe_0004():
    """Model: Vertical 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 552.2698632, perimeter: 227.58908
            with BuildLine():
                Line((45.2145409537, -33.0199995804), (-63.4999990463, -33.0199995804))
                Line((45.2145409537, -27.9399995804), (45.2145409537, -33.0199995804))
                Line((-63.4999990463, -27.9399995804), (45.2145409537, -27.9399995804))
                Line((-63.4999990463, -33.0199995804), (-63.4999990463, -27.9399995804))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a tapered metal pin or punch with a pointed cone-shaped tip, featuring a cylindrical shaft that gradually narrows toward the end.
def model_86704_3f8f3bfe_0008():
    """Model: Horizontal 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 619.3536, perimeter: 254
            with BuildLine():
                Line((-24.5969506451, 117.2841611132), (-24.5969506451, -4.6358388868))
                Line((-24.5969506451, -4.6358388868), (-19.5169506451, -4.6358388868))
                Line((-19.5169506451, -4.6358388868), (-19.5169506451, 117.2841611132))
                Line((-19.5169506451, 117.2841611132), (-24.5969506451, 117.2841611132))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a double-pyramid or bi-pyramid geometric solid consisting of two triangular pyramids joined at their bases, creating a diamond-shaped form when viewed from the side with four triangular faces and a defined ridge line running horizontally through its center.
def model_87757_eb92dadf_0005():
    """Model: sikakupart"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.681658155, 0, 0.8567486903), x_dir=(0.2266513074, 0, -0.9739759673), z_dir=(0.9739759673, 0, 0.2266513074))):
            # Profile area: 0.5376, perimeter: 3.04
            with BuildLine():
                Line((-3.041613437, -0.1001336082), (-4.001613437, -0.1001336082))
                Line((-3.041613437, 0.4598663918), (-3.041613437, -0.1001336082))
                Line((-4.001613437, 0.4598663918), (-3.041613437, 0.4598663918))
                Line((-4.001613437, -0.1001336082), (-4.001613437, 0.4598663918))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)
    return part.part


# Description: This is a parallelogram-shaped frame or border with a hollow rectangular opening in the center, featuring uniform dark blue walls and a three-dimensional depth, commonly used as a window frame, mounting bracket, or structural surround component.
def model_88300_ac762961_0003():
    """Model: Boom Arm Collar"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 229.4054341257), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 280.5567543478, perimeter: 265.191969218
            with BuildLine():
                Line((-31.2430091761, 89.9281941098), (-31.2430091761, 54.7573342814))
                Line((-31.2430091761, 54.7573342814), (4.1158767, 54.7573342814))
                Line((4.1158767, 54.7573342814), (4.1158767, 89.9281941098))
                Line((4.1158767, 89.9281941098), (-31.2430091761, 89.9281941098))
            make_face()
            with BuildLine():
                Line((-29.1271324761, 87.8123174098), (-29.1271324761, 56.8732109814))
                Line((2, 87.8123174098), (-29.1271324761, 87.8123174098))
                Line((2, 56.8732109814), (2, 87.8123174098))
                Line((-29.1271324761, 56.8732109814), (2, 56.8732109814))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a complex molded plastic or composite bracket/housing component with an irregular angular shape, featuring multiple internal ribs and reinforcement structures, a slotted upper section, and curved surfaces designed for structural support and assembly integration.
def model_88300_ac762961_0008():
    """Model: Rear Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 9246.7701996979, perimeter: 546.4036808544
            with BuildLine():
                Line((0, 0), (14.9193670782, -0.3618805009))
                CenterArc((14.4453124855, -19.9058859548), 19.5497538844, 47.2789165155, 41.3316035925)
                Line((27.7084530894, -5.5433660415), (35.815018319, 0.7053284807))
                Line((35.815018319, 0.7053284807), (44.2435755862, 9.725627115))
                CenterArc((-19.3614890817, 69.1581306018), 87.0507135072, -43.0576781394, 16.7229867402)
                Line((58.6549269027, 30.541222918), (66.5435444361, 46.4783267397))
                Line((66.5435444361, 46.4783267397), (76.2096931811, 79.0374841811))
                Line((76.2096931811, 79.0374841811), (79.039272448, 93.506272736))
                Line((79.039272448, 93.506272736), (85.1936286975, 92.3027000403))
                Line((85.1936286975, 92.3027000403), (85.1936286975, 143.2379094983))
                Line((85.1936286975, 143.2379094983), (85.1798956848, 157.4959428001))
                CenterArc((67.7369789421, 157.4791421804), 17.4429248337, 0.0551859715, 90.5786622631)
                Line((67.5440163593, 174.9209996559), (18.9938570943, 174.3838800206))
                Line((18.9938570943, 174.3838800206), (15.8504249532, 172.1417743115))
                Line((15.8504249532, 172.1417743115), (-5.2716876643, 172.1417743115))
                Line((-5.2716876643, 172.1417743115), (-5.2716876643, 159.7420439996))
                CenterArc((-0.066315435, 112.4842473518), 47.5436141249, -88.0205724875, 184.3062737286)
                Line((1.5758721639, 64.9690028092), (0, 0))
            make_face()
        # Symmetric extrude, each_side=56.1079
        extrude(amount=56.1079, both=True)
    return part.part


# Description: This is a curved deflector or shroud component with an elongated, streamlined shape featuring a ribbed or textured upper surface and a smooth underside, designed to direct airflow or protect internal components.
def model_88495_2fdd1d11_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.2037966865, perimeter: 69.0436735187
            with BuildLine():
                CenterArc((8.5090002716, -71.3740022779), 71.3750191746, 89.6941535482, 7.15266875)
                CenterArc((6.0023837815, 0.2540000081), 2.8987661285, -5.0269029325, 36.2585795107)
                CenterArc((8.3597036141, 99.9256945769), 98.1687598349, -94.2901290666, 4.3609548095)
                CenterArc((-0.2540000081, 3.1115000993), 1.6667994562, -139.6354634269, 99.2709268538)
                CenterArc((-2.0320000648, -21.3614006817), 23.3989158404, 88.7559874951, 20.2493433108)
                Line((-10.1600003242, 0), (-9.652000308, 0.7620000243))
                CenterArc((-7.112000227, -40.8940013051), 41.0074340496, 80.012578425, 14.2500326978)
            make_face()
            with BuildLine():
                CenterArc((8.1280002594, 1.2700000405), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.3660002351, 1.2700000405), (1.7780000567, 1.2700000405))
                CenterArc((7.3660002351, 1.0160000324), 0.2540000081, -90, 180)
                Line((1.7780000567, 0.7620000243), (7.3660002351, 0.7620000243))
                CenterArc((1.7780000567, 1.0160000324), 0.2540000081, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((6.8785323022, 0.6657981372), (0.7825321077, 0.6657981372))
                CenterArc((6.8785323022, 0.4117981291), 0.2540000081, -90, 180)
                Line((0.7825321077, 0.157798121), (6.8785323022, 0.157798121))
                CenterArc((0.7825321077, 0.4117981291), 0.2540000081, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)
    return part.part


# Description: This is a trapezoidal duct or channel component with a tapered rectangular profile, featuring a slotted or louvered left side panel and a smooth right side, designed for fluid flow or air handling applications.
def model_88670_b2a44f24_0001():
    """Model: STATIONARY JAW"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 34.6595664312, perimeter: 26.5028097596
            with BuildLine():
                Line((7.6682379358, 8.89), (7.6682379358, 0))
                Line((7.6682379358, 0), (13.0657379358, 0))
                Line((13.0657379358, 0), (13.0657379358, 4.445))
                CenterArc((13.9883196383, 9.4405222952), 5.08, -173.7786076914, 73.3150225895)
                Line((7.6682379358, 8.89), (8.9382379358, 8.89))
            make_face()
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


# Description: This is a rectangular block or base component with an L-shaped or stepped profile, featuring a main horizontal body with a vertical raised section or flange on one end, and triangulated surface geometry indicating a complex or organic form.
def model_88680_0fb9b042_0000():
    """Model: Moving Jaw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.6685, perimeter: 18.17
            with BuildLine():
                Line((-3.05, -3.75), (3.05, -3.75))
                Line((3.05, -1.765), (3.05, -3.75))
                Line((0.78, -1.765), (3.05, -1.765))
                Line((0.78, -1.765), (0.78, -0.765))
                Line((-0.78, -0.765), (0.78, -0.765))
                Line((-0.78, -1.765), (-0.78, -0.765))
                Line((-3.05, -1.765), (-0.78, -1.765))
                Line((-3.05, -3.75), (-3.05, -1.765))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


# Description: This is a rounded rectangular or pill-shaped capsule with a symmetrical, smooth ovoid form featuring vertical ribbed or fluted surface patterns across all sides, creating a textured cylindrical body with rounded ends.
def model_88941_aa581346_0004():
    """Model: tyre (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a 3D parallelogram-shaped plate or flat component with a slanted, trapezoidal profile and a diagonal line feature running across its surface, commonly used as a structural bracket or mounting plate in assemblies.
def model_88941_aa581346_0008():
    """Model: Back"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33353.6544, perimeter: 730.52
            with BuildLine():
                Line((182.38, -182.88), (0, -182.88))
                Line((182.38, 0), (182.38, -182.88))
                Line((0, 0), (182.38, 0))
                Line((0, -182.88), (0, 0))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a simple straight rod or shaft with a cylindrical form and slight diagonal orientation, featuring no holes, slots, or other distinguishing features.
def model_88941_aa581346_0014():
    """Model: Hinge rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0415475628, perimeter: 0.7225663103
            Circle(0.115)
        # OneSide extrude, distance=-182.88
        extrude(amount=-182.88)
    return part.part


# Description: This is a curved structural bracket or support component featuring a wavy, undulating top surface with multiple triangular facets and a hollow underside, designed to distribute loads across a bent geometry.
def model_89255_3c610b95_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.3731381107, perimeter: 16.1303240726
            with BuildLine():
                Line((0, 0), (0.5, 0))
                CenterArc((0.4101494288, 0.9959552575), 1, -84.8449893765, 56.434339157)
                CenterArc((2.5210937839, -0.1459352493), 1.4, 75, 76.5893497804)
                Line((4.4, 0.8), (2.8834404471, 1.2063609075))
                Line((6, 0.8), (4.4, 0.8))
                Line((6, 0.8), (6.5, 1.3))
                Line((6.5, 1.3), (6.5, 1.7))
                Line((6.5, 1.7), (5.2349351573, 1.7))
                CenterArc((5.2349351573, 3.2), 1.5, -133.9455195623, 43.9455195623)
                CenterArc((3.5, 1.4), 1, 46.0544804377, 43.9455195623)
                Line((1, 2.4), (3.5, 2.4))
                Line((0, 1.4), (1, 2.4))
                Line((0, 0), (0, 1.4))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a karambit knife or curved blade tool featuring a distinctive hook-shaped handle at the top and a sharp, downward-curving blade that extends to a pointed tip at the bottom.
def model_89265_decd9971_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 578.2960481824, perimeter: 255.54345644
            with BuildLine():
                CenterArc((-31.9112692499, 14.5534851008), 11.3157988059, -120.3172868557, 32.6186503732)
                CenterArc((-39.033727754, 2.3732959725), 2.794, 59.6827131444, 23.7803617968)
                CenterArc((-23.174661632, 140.7734673256), 136.5118412588, -104.962405737, 8.4254806782)
                CenterArc((-31.8943588223, 32.7578905363), 35.6831304452, -138.0189764895, 53.638590241)
                Line((25.3999996185, 2.5399999619), (-28.4001387723, -2.7537445234))
                CenterArc((25.8745392951, -2.2827300249), 4.8460202672, 26.6794722041, 68.9401415474)
                Line((30.2046149881, -0.1068722808), (30.7340009809, 0))
                CenterArc((33.0690748025, 0.5391711983), 2.3965131615, 101.122922006, 91.8788700711)
                CenterArc((36.8592361206, -18.7386159574), 22.0433551581, 61.7570255584, 39.3658964476)
                CenterArc((50.766628976, -0.2627485386), 3.6019068514, 164.8194797799, 260.0884335837)
                CenterArc((30.8689288227, -42.7550666038), 50.5222176555, 64.9079133636, 31.2883479456)
                CenterArc((-65.1510789394, 841.6616240893), 839.0915888174, -87.6986364825, 3.8948977917)
            make_face()
            with BuildLine():
                CenterArc((50.766628976, -0.2627485386), 2.2380945357, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.381
        extrude(amount=0.381)
    return part.part


# Description: This is a cylindrical foam or rubber tube with a slightly tapered top end and text/branding printed on the upper surface, appearing to be a grip sleeve or protective covering.
def model_89527_b3bf425d_0014():
    """Model: 16.1 v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a curved or tapered wall profile, featuring an open top with a mesh or perforated rim detail and a smooth curved interior surface.
def model_89527_b3bf425d_0017():
    """Model: 12 v0"""
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
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a cylindrical mesh filter or perforated tube with a slightly tapered top end and a fine mesh or perforated surface covering its lateral walls, designed to allow fluid or air passage while filtering particles.
def model_89527_b3bf425d_0022():
    """Model: screw1 v0"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3)
    return part.part


# Description: This is a toroidal ring or torus-shaped component featuring a smooth, curved outer surface with a large central hollow opening and a uniform circular cross-section throughout.
def model_89527_b3bf425d_0026():
    """Model: 15 v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5890486225, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical foam or composite roller with a slightly tapered, rounded top end and a hollow tubular body, designed for use as a tool or component in industrial applications.
def model_89527_b3bf425d_0031():
    """Model: 2*6 v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a flat trapezoidal plate or base with a slight 3D depth, featuring a triangular internal division and a beveled or chamfered edge on one side, giving it a wedge-like appearance.
def model_89527_b3bf425d_0034():
    """Model: base plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48.64, perimeter: 28
            with BuildLine():
                Line((7.6, -6.4), (0, -6.4))
                Line((7.6, 0), (7.6, -6.4))
                Line((0, 0), (7.6, 0))
                Line((0, -6.4), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with hemispherical ends, featuring a smooth continuous surface with no holes, slots, or flanges.
def model_89790_a9620602_0031():
    """Model: Small Piston (1) (2) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube featuring two hemispherical end caps connected by a cylindrical body, with a smooth, continuous surface suitable for applications requiring sealed or streamlined geometry.
def model_89790_a9620602_0032():
    """Model: Large Piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 13.8544236023, perimeter: 13.1946891451
            Circle(2.1)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a curved arch or band component with a hollow center, featuring a ribbed or textured surface pattern on both the inner and outer faces, resembling a structural reinforcement ring or collar.
def model_89907_161bb6f3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0320788791, perimeter: 37.1283155163
            with BuildLine():
                CenterArc((0, 0), 6, 0, 180)
                Line((-5.5, 0), (-6, 0))
                CenterArc((0, 0), 5.5, 0, 180)
                Line((6, 0), (5.5, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat parallelogram-shaped panel or plate with a dark frame border and blue translucent center surface, featuring internal diagonal cross-bracing or reinforcement lines.
def model_89939_2c1be711_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4856, perimeter: 396
            with BuildLine():
                Line((92.5, -47.5), (-7.5, -47.5))
                Line((92.5, 2.5), (92.5, -47.5))
                Line((-7.5, 2.5), (92.5, 2.5))
                Line((-7.5, -47.5), (-7.5, 2.5))
            make_face()
            with BuildLine():
                Line((85.5, -40.5), (91.5, -40.5))
                Line((91.5, -40.5), (91.5, -46.5))
                Line((91.5, -46.5), (85.5, -46.5))
                Line((85.5, -46.5), (85.5, -40.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5, -46.5), (-0.5, -40.5))
                Line((-6.5, -46.5), (-0.5, -46.5))
                Line((-6.5, -40.5), (-6.5, -46.5))
                Line((-0.5, -40.5), (-6.5, -40.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((85.5, -4.5), (91.5, -4.5))
                Line((85.5, 1.5), (85.5, -4.5))
                Line((91.5, 1.5), (85.5, 1.5))
                Line((91.5, -4.5), (91.5, 1.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6.5, -4.5), (-6.5, 1.5))
                Line((-6.5, 1.5), (-0.5, 1.5))
                Line((-0.5, 1.5), (-0.5, -4.5))
                Line((-0.5, -4.5), (-6.5, -4.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with a hollow central bore and two hemispherical end caps, featuring a smooth, seamless design suitable for mechanical applications like hydraulic cylinders or pressure vessels.
def model_90106_aaea5474_0000():
    """Model: PIPE JUNCTION"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0215984495, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a square frame or border with a hollow rectangular opening in the center, featuring uniform dark blue material and a tilted 3D perspective that emphasizes its raised edges and depth.
def model_90116_d24f5dc4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.3414396958, perimeter: 40.7226324236
            with BuildLine():
                Line((-1.5, -2.5), (-7.5, -2.5))
                Line((-1.5, 2.5), (-1.5, -2.5))
                Line((-7.5, 2.5), (-1.5, 2.5))
                Line((-7.5, -2.5), (-7.5, 2.5))
            make_face()
            with BuildLine():
                Line((-7.0903290529, 2.0903290529), (-1.9096709471, 2.0903290529))
                Line((-1.9096709471, 2.0903290529), (-1.9096709471, -2.0903290529))
                Line((-1.9096709471, -2.0903290529), (-7.0903290529, -2.0903290529))
                Line((-7.0903290529, -2.0903290529), (-7.0903290529, 2.0903290529))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


MODELS = {
    "model_73091_ce795f51_0000": {"func": model_73091_ce795f51_0000, "volume": 262.5, "area": 260},
    "model_73388_10a40b49_0000": {"func": model_73388_10a40b49_0000, "volume": 0.0013917758, "area": 0.1930887791},
    "model_73388_10a40b49_0006": {"func": model_73388_10a40b49_0006, "volume": 0.2121988758, "area": 3.1767784913},
    "model_73388_10a40b49_0007": {"func": model_73388_10a40b49_0007, "volume": 0.5026548246, "area": 6.0318578949},
    "model_73388_10a40b49_0009": {"func": model_73388_10a40b49_0009, "volume": 0.1131727338, "area": 2.1343980488},
    "model_73388_10a40b49_0010": {"func": model_73388_10a40b49_0010, "volume": 0.0701666027, "area": 1.7600470343},
    "model_73388_10a40b49_0012": {"func": model_73388_10a40b49_0012, "volume": 0.2852895997, "area": 3.9461545322},
    "model_73388_10a40b49_0020": {"func": model_73388_10a40b49_0020, "volume": 0.3017939567, "area": 4.1198846059},
    "model_73388_10a40b49_0021": {"func": model_73388_10a40b49_0021, "volume": 0.0085215701, "area": 0.9495463795},
    "model_73388_10a40b49_0022": {"func": model_73388_10a40b49_0022, "volume": 0.0426078504, "area": 1.3391038686},
    "model_73388_10a40b49_0024": {"func": model_73388_10a40b49_0024, "volume": 0.2357765287, "area": 3.4249643109},
    "model_73388_10a40b49_0028": {"func": model_73388_10a40b49_0028, "volume": 0.1603280395, "area": 2.6307696881},
    "model_74148_8ce0be94_0000": {"func": model_74148_8ce0be94_0000, "volume": 0.4272566009, "area": 8.5451320178},
    "model_74667_3504f3e1_0000": {"func": model_74667_3504f3e1_0000, "volume": 2064.512, "area": 1677.2128},
    "model_74722_43175bd2_0000": {"func": model_74722_43175bd2_0000, "volume": 6.7561287914, "area": 182.7905280882},
    "model_74811_83a8fddf_0000": {"func": model_74811_83a8fddf_0000, "volume": 522.7610175573, "area": 532.8141140488},
    "model_75032_945d0803_0001": {"func": model_75032_945d0803_0001, "volume": 0.4965483539, "area": 7.8067707936},
    "model_75646_4baf69b2_0010": {"func": model_75646_4baf69b2_0010, "volume": 180.9557368468, "area": 186.9875947417},
    "model_75646_4baf69b2_0011": {"func": model_75646_4baf69b2_0011, "volume": 48.7577449968, "area": 115.3124979831},
    "model_75646_4baf69b2_0012": {"func": model_75646_4baf69b2_0012, "volume": 125.6637061436, "area": 276.4601535159},
    "model_75990_213a7354_0000": {"func": model_75990_213a7354_0000, "volume": 8115.3079364416, "area": 8325.231023737},
    "model_76278_13dd168d_0006": {"func": model_76278_13dd168d_0006, "volume": 0.00002, "area": 0.0048},
    "model_76278_13dd168d_0007": {"func": model_76278_13dd168d_0007, "volume": 0.3255, "area": 5.225},
    "model_76278_13dd168d_0008": {"func": model_76278_13dd168d_0008, "volume": 4.8347502656, "area": 100.1289875481},
    "model_76298_af8ea172_0018": {"func": model_76298_af8ea172_0018, "volume": 0.2993152401, "area": 5.0357766742},
    "model_76298_af8ea172_0025": {"func": model_76298_af8ea172_0025, "volume": 0.0687389265, "area": 3.0701214766},
    "model_76666_8c3d34c0_0000": {"func": model_76666_8c3d34c0_0000, "volume": 14.8377621932, "area": 71.2896199971},
    "model_76880_9bb28e72_0001": {"func": model_76880_9bb28e72_0001, "volume": 1.4181149238, "area": 36.9859703107},
    "model_77211_d46ae17d_0000": {"func": model_77211_d46ae17d_0000, "volume": 204, "area": 218},
    "model_77211_d46ae17d_0001": {"func": model_77211_d46ae17d_0001, "volume": 46.7657501196, "area": 77.9426646553},
    "model_77211_d46ae17d_0002": {"func": model_77211_d46ae17d_0002, "volume": 54, "area": 90},
    "model_77211_d46ae17d_0003": {"func": model_77211_d46ae17d_0003, "volume": 432, "area": 360},
    "model_77211_d46ae17d_0005": {"func": model_77211_d46ae17d_0005, "volume": 306, "area": 342},
    "model_77211_d46ae17d_0007": {"func": model_77211_d46ae17d_0007, "volume": 2490.84, "area": 1321.08},
    "model_77211_d46ae17d_0008": {"func": model_77211_d46ae17d_0008, "volume": 792, "area": 600},
    "model_77211_d46ae17d_0011": {"func": model_77211_d46ae17d_0011, "volume": 14.4, "area": 151.2},
    "model_77211_d46ae17d_0012": {"func": model_77211_d46ae17d_0012, "volume": 324, "area": 342},
    "model_77211_d46ae17d_0014": {"func": model_77211_d46ae17d_0014, "volume": 408, "area": 422},
    "model_77306_fe3133f0_0000": {"func": model_77306_fe3133f0_0000, "volume": 34.9719483939, "area": 216.112830472},
    "model_77397_df713db5_0004": {"func": model_77397_df713db5_0004, "volume": 353.4123540812, "area": 366.3923395555},
    "model_77686_b1e8a0fa_0002": {"func": model_77686_b1e8a0fa_0002, "volume": 484530.9649148735, "area": 36339.8223686155},
    "model_78288_d264181d_0001": {"func": model_78288_d264181d_0001, "volume": 0.0654685689, "area": 1.3784262295},
    "model_78422_3d6c0e4e_0003": {"func": model_78422_3d6c0e4e_0003, "volume": 9.0343655337, "area": 68.1281928841},
    "model_78422_3d6c0e4e_0004": {"func": model_78422_3d6c0e4e_0004, "volume": 2219702.2546760403, "area": 182314.7812134497},
    "model_78513_7ad0bd6a_0000": {"func": model_78513_7ad0bd6a_0000, "volume": 190.3428156957, "area": 326.8512996795},
    "model_78513_7ad0bd6a_0005": {"func": model_78513_7ad0bd6a_0005, "volume": 9.8960168588, "area": 69.9318524689},
    "model_78600_3f295e84_0001": {"func": model_78600_3f295e84_0001, "volume": 9.8174770425, "area": 47.1238898038},
    "model_78603_4720dcb8_0006": {"func": model_78603_4720dcb8_0006, "volume": 1.82, "area": 9.82},
    "model_78687_39a896db_0023": {"func": model_78687_39a896db_0023, "volume": 0.106088112, "area": 1.4549226784},
    "model_78773_06275eba_0009": {"func": model_78773_06275eba_0009, "volume": 0.0018853184, "area": 0.4587832707},
    "model_78863_d59be42e_0000": {"func": model_78863_d59be42e_0000, "volume": 30.5415280696, "area": 129.0822468156},
    "model_78880_ed3c684d_0000": {"func": model_78880_ed3c684d_0000, "volume": 18.2957220693, "area": 373.2130154098},
    "model_78880_ed3c684d_0001": {"func": model_78880_ed3c684d_0001, "volume": 70.6858347058, "area": 372.2787294504},
    "model_78970_755e6a93_0000": {"func": model_78970_755e6a93_0000, "volume": 164.8541466521, "area": 448.6211734408},
    "model_79010_bf913e12_0000": {"func": model_79010_bf913e12_0000, "volume": 2.707305, "area": 24.3949},
    "model_79093_054c6005_0000": {"func": model_79093_054c6005_0000, "volume": 10494.5022128562, "area": 6230.179475326},
    "model_79116_8392be69_0001": {"func": model_79116_8392be69_0001, "volume": 71680, "area": 36352},
    "model_79116_8392be69_0002": {"func": model_79116_8392be69_0002, "volume": 8800, "area": 9760},
    "model_79116_8392be69_0004": {"func": model_79116_8392be69_0004, "volume": 10496, "area": 5376},
    "model_79120_688e7f03_0001": {"func": model_79120_688e7f03_0001, "volume": 1.6075198376, "area": 33.8099033354},
    "model_79120_688e7f03_0004": {"func": model_79120_688e7f03_0004, "volume": 1.206466494, "area": 25.7128681698},
    "model_79211_141cf274_0000": {"func": model_79211_141cf274_0000, "volume": 162.8785638196, "area": 261.3623521375},
    "model_79325_5f4654e1_0001": {"func": model_79325_5f4654e1_0001, "volume": 375.8699537242, "area": 1263.1401146926},
    "model_79338_5e0d79fe_0000": {"func": model_79338_5e0d79fe_0000, "volume": 1.3513553785, "area": 14.339521727},
    "model_79423_62db5fc6_0020": {"func": model_79423_62db5fc6_0020, "volume": 0.7575630438, "area": 6.6195351495},
    "model_79424_5ac55435_0000": {"func": model_79424_5ac55435_0000, "volume": 23.5612657306, "area": 189.5872812414},
    "model_79510_f27c9c97_0000": {"func": model_79510_f27c9c97_0000, "volume": 115.5164034696, "area": 405.4235254217},
    "model_79510_f27c9c97_0001": {"func": model_79510_f27c9c97_0001, "volume": 385.5792252879, "area": 1294.3705994497},
    "model_79625_8be98a9f_0000": {"func": model_79625_8be98a9f_0000, "volume": 7.853981634, "area": 21.9911485751},
    "model_79678_786d163b_0000": {"func": model_79678_786d163b_0000, "volume": 274.8893571891, "area": 463.3849164045},
    "model_79693_9396219b_0000": {"func": model_79693_9396219b_0000, "volume": 9.3871388363, "area": 51.0722330226},
    "model_79693_9396219b_0002": {"func": model_79693_9396219b_0002, "volume": 0.1443540989, "area": 2.6613256163},
    "model_79906_052c7eb4_0000": {"func": model_79906_052c7eb4_0000, "volume": 0.204480048, "area": 3.7660516227},
    "model_79906_052c7eb4_0001": {"func": model_79906_052c7eb4_0001, "volume": 0.0826364532, "area": 2.4102298838},
    "model_79986_27ba3aa9_0000": {"func": model_79986_27ba3aa9_0000, "volume": 1050.6308243656, "area": 582.2031314258},
    "model_80178_284e8e7a_0000": {"func": model_80178_284e8e7a_0000, "volume": 8, "area": 24},
    "model_80470_fca39d24_0000": {"func": model_80470_fca39d24_0000, "volume": 191.3991513259, "area": 283.3979113222},
    "model_80473_92aeb455_0000": {"func": model_80473_92aeb455_0000, "volume": 201.047483649, "area": 293.0953941962},
    "model_80490_5d5ba15f_0000": {"func": model_80490_5d5ba15f_0000, "volume": 0.010463898, "area": 0.6741638523},
    "model_80490_5d5ba15f_0001": {"func": model_80490_5d5ba15f_0001, "volume": 3.4636059006, "area": 20.5617239177},
    "model_80491_e73dabd5_0000": {"func": model_80491_e73dabd5_0000, "volume": 18.77216876, "area": 104.0288710667},
    "model_80493_74f06ac0_0000": {"func": model_80493_74f06ac0_0000, "volume": 500, "area": 441.4213562373},
    "model_80494_8a92342c_0000": {"func": model_80494_8a92342c_0000, "volume": 9.5076472623, "area": 43.8001258089},
    "model_80758_5dd10206_0000": {"func": model_80758_5dd10206_0000, "volume": 315.5025530651, "area": 482.3975447579},
    "model_80761_62bb3981_0002": {"func": model_80761_62bb3981_0002, "volume": 1861.5873852123, "area": 900.8572933822},
    "model_80766_9206dfb0_0000": {"func": model_80766_9206dfb0_0000, "volume": 3.5451327412, "area": 32.1307963268},
    "model_80768_93483df3_0002": {"func": model_80768_93483df3_0002, "volume": 2330, "area": 1132},
    "model_80769_6632d585_0000": {"func": model_80769_6632d585_0000, "volume": 19.6137166941, "area": 203.6221225333},
    "model_80911_b01bc2a7_0000": {"func": model_80911_b01bc2a7_0000, "volume": 179.2274333882, "area": 450.7380520836},
    "model_81123_41bb9143_0000": {"func": model_81123_41bb9143_0000, "volume": 2.1299998191, "area": 49.6999957798},
    "model_81123_41bb9143_0001": {"func": model_81123_41bb9143_0001, "volume": 1.5428853074, "area": 14.7134430518},
    "model_81123_41bb9143_0009": {"func": model_81123_41bb9143_0009, "volume": 22.9022104447, "area": 62.7690212187},
    "model_81145_bdb0ac6a_0016": {"func": model_81145_bdb0ac6a_0016, "volume": 7.1336895274, "area": 81.6393580965},
    "model_81145_bdb0ac6a_0017": {"func": model_81145_bdb0ac6a_0017, "volume": 6.16, "area": 26.28},
    "model_81145_bdb0ac6a_0023": {"func": model_81145_bdb0ac6a_0023, "volume": 0.1880243203, "area": 10.8069216487},
    "model_81145_bdb0ac6a_0024": {"func": model_81145_bdb0ac6a_0024, "volume": 0.219361707, "area": 12.5976294613},
    "model_81145_bdb0ac6a_0041": {"func": model_81145_bdb0ac6a_0041, "volume": 4.4814374404, "area": 55.5650868951},
    "model_81145_bdb0ac6a_0043": {"func": model_81145_bdb0ac6a_0043, "volume": 3.5697699978, "area": 44.0109742423},
    "model_81145_bdb0ac6a_0049": {"func": model_81145_bdb0ac6a_0049, "volume": 1.0807035615, "area": 6.5654867622},
    "model_81146_08caa784_0000": {"func": model_81146_08caa784_0000, "volume": 0.5446730056, "area": 7.0979449033},
    "model_81549_8d959744_0000": {"func": model_81549_8d959744_0000, "volume": 8.468612906, "area": 33.0769941209},
    "model_81549_b0ace035_0000": {"func": model_81549_b0ace035_0000, "volume": 64.5486800771, "area": 133.7743879839},
    "model_81969_8bc864bd_0000": {"func": model_81969_8bc864bd_0000, "volume": 0.1108353888, "area": 3.39543334},
    "model_81969_8bc864bd_0003": {"func": model_81969_8bc864bd_0003, "volume": 0.0960116546, "area": 3.2254898635},
    "model_81972_a6710ac4_0002": {"func": model_81972_a6710ac4_0002, "volume": 0.5002486732, "area": 12.1305067431},
    "model_81980_55748cd2_0000": {"func": model_81980_55748cd2_0000, "volume": 0.0250377926, "area": 0.9745793746},
    "model_81997_a224b06d_0000": {"func": model_81997_a224b06d_0000, "volume": 35.3178853174, "area": 85.7610735075},
    "model_82012_c533307b_0000": {"func": model_82012_c533307b_0000, "volume": 192.9051867854, "area": 408.1600199759},
    "model_82012_c533307b_0004": {"func": model_82012_c533307b_0004, "volume": 169.6460032938, "area": 169.6460032938},
    "model_82375_657b4b9f_0000": {"func": model_82375_657b4b9f_0000, "volume": 14.0029634201, "area": 32.6918013011},
    "model_82485_d6d73980_0002": {"func": model_82485_d6d73980_0002, "volume": 630.133313686, "area": 2494.6222610928},
    "model_82491_79dd5db3_0000": {"func": model_82491_79dd5db3_0000, "volume": 225.5205073342, "area": 209.2454718099},
    "model_82512_252da752_0000": {"func": model_82512_252da752_0000, "volume": 0.0000288928, "area": 0.0080581852},
    "model_82512_252da752_0004": {"func": model_82512_252da752_0004, "volume": 0.0054795419, "area": 0.9468129645},
    "model_83108_0e20d25b_0000": {"func": model_83108_0e20d25b_0000, "volume": 500.5955746133, "area": 771.2554493394},
    "model_83109_0311c05e_0000": {"func": model_83109_0311c05e_0000, "volume": 314.0381869792, "area": 407.4688312666},
    "model_83110_487f8396_0003": {"func": model_83110_487f8396_0003, "volume": 35.8951504365, "area": 60.3774838112},
    "model_83112_fbb40a06_0000": {"func": model_83112_fbb40a06_0000, "volume": 12834, "area": 9231.0689145077},
    "model_83219_f6c9d6bc_0000": {"func": model_83219_f6c9d6bc_0000, "volume": 373.001622949, "area": 556.1078152294},
    "model_83230_50d5eae5_0000": {"func": model_83230_50d5eae5_0000, "volume": 8220.401770285, "area": 5134.5356156665},
    "model_83232_0c29683a_0000": {"func": model_83232_0c29683a_0000, "volume": 266.6977908245, "area": 400.5747690031},
    "model_83259_487d379e_0000": {"func": model_83259_487d379e_0000, "volume": 64, "area": 342.4},
    "model_83259_487d379e_0004": {"func": model_83259_487d379e_0004, "volume": 9.6, "area": 56.8},
    "model_83337_74fe9172_0000": {"func": model_83337_74fe9172_0000, "volume": 106.7719638749, "area": 306.2342217964},
    "model_83337_74fe9172_0001": {"func": model_83337_74fe9172_0001, "volume": 345.4833493545, "area": 820.0838437},
    "model_83338_b9bb889f_0000": {"func": model_83338_b9bb889f_0000, "volume": 112.0016496981, "area": 248.4888554436},
    "model_83367_f3132ff3_0000": {"func": model_83367_f3132ff3_0000, "volume": 441.7864669111, "area": 471.2388980385},
    "model_83378_2dc861a1_0001": {"func": model_83378_2dc861a1_0001, "volume": 1816.2666100361, "area": 2190.5977736343},
    "model_83384_bb9418ee_0000": {"func": model_83384_bb9418ee_0000, "volume": 155.562760969, "area": 377.1771256718},
    "model_83432_a7f85698_0001": {"func": model_83432_a7f85698_0001, "volume": 1.2231747704, "area": 8.1780972451},
    "model_84025_ec3401ea_0000": {"func": model_84025_ec3401ea_0000, "volume": 23.6690266447, "area": 75.277875658},
    "model_84025_ec3401ea_0003": {"func": model_84025_ec3401ea_0003, "volume": 6300.0000000001, "area": 8802.0000000001},
    "model_84025_ec3401ea_0005": {"func": model_84025_ec3401ea_0005, "volume": 124.6438055098, "area": 308.9955742876},
    "model_84025_ec3401ea_0009": {"func": model_84025_ec3401ea_0009, "volume": 24.1274315796, "area": 64.3398175455},
    "model_84025_ec3401ea_0017": {"func": model_84025_ec3401ea_0017, "volume": 409.9167335793, "area": 1011.5890778585},
    "model_84025_ec3401ea_0019": {"func": model_84025_ec3401ea_0019, "volume": 8282.7628508535, "area": 8852.2591791808},
    "model_84129_211748cd_0000": {"func": model_84129_211748cd_0000, "volume": 841.847422212, "area": 1053.5532903729},
    "model_84608_204c01e6_0000": {"func": model_84608_204c01e6_0000, "volume": 3.2, "area": 24.64},
    "model_84608_204c01e6_0002": {"func": model_84608_204c01e6_0002, "volume": 30, "area": 212},
    "model_84608_204c01e6_0005": {"func": model_84608_204c01e6_0005, "volume": 603.5513210019, "area": 3080.3827931331},
    "model_85195_c6ef0067_0005": {"func": model_85195_c6ef0067_0005, "volume": 6.7858401318, "area": 24.8814138164},
    "model_85195_c6ef0067_0007": {"func": model_85195_c6ef0067_0007, "volume": 1.6587609211, "area": 15.2053084434},
    "model_85200_70e166c4_0006": {"func": model_85200_70e166c4_0006, "volume": 0.5111988805, "area": 11.9522252876},
    "model_85631_f44b2bdc_0000": {"func": model_85631_f44b2bdc_0000, "volume": 212.3611044898, "area": 696.7227837591},
    "model_85637_45bb38ad_0000": {"func": model_85637_45bb38ad_0000, "volume": 1.849, "area": 38.7},
    "model_85638_2ab1040c_0001": {"func": model_85638_2ab1040c_0001, "volume": 593.0091413413, "area": 905.7605378021},
    "model_85638_2ab1040c_0002": {"func": model_85638_2ab1040c_0002, "volume": 1920, "area": 2176},
    "model_85638_2ab1040c_0003": {"func": model_85638_2ab1040c_0003, "volume": 186.838496587, "area": 296.5045706706},
    "model_85638_2ab1040c_0004": {"func": model_85638_2ab1040c_0004, "volume": 1120, "area": 1336},
    "model_86099_c101852f_0000": {"func": model_86099_c101852f_0000, "volume": 4.9480084294, "area": 33.9292006588},
    "model_86296_8a6ed4d3_0001": {"func": model_86296_8a6ed4d3_0001, "volume": 0.001526, "area": 0.2162166378},
    "model_86296_8a6ed4d3_0002": {"func": model_86296_8a6ed4d3_0002, "volume": 0.0784875, "area": 1.2135144977},
    "model_86296_8a6ed4d3_0003": {"func": model_86296_8a6ed4d3_0003, "volume": 0.00605, "area": 0.38225},
    "model_86296_8a6ed4d3_0014": {"func": model_86296_8a6ed4d3_0014, "volume": 0.1660131031, "area": 13.3445625147},
    "model_86296_8a6ed4d3_0015": {"func": model_86296_8a6ed4d3_0015, "volume": 0.00063, "area": 0.0744},
    "model_86296_8a6ed4d3_0019": {"func": model_86296_8a6ed4d3_0019, "volume": 0.001866106, "area": 0.378876074},
    "model_86704_3f8f3bfe_0004": {"func": model_86704_3f8f3bfe_0004, "volume": 350.691363132, "area": 1249.0587922},
    "model_86704_3f8f3bfe_0008": {"func": model_86704_3f8f3bfe_0008, "volume": 393.289536, "area": 1399.9972},
    "model_87757_eb92dadf_0005": {"func": model_87757_eb92dadf_0005, "volume": 0.016128, "area": 1.1664},
    "model_88300_ac762961_0003": {"func": model_88300_ac762961_0003, "volume": 701.3918858694, "area": 1224.0934317406},
    "model_88300_ac762961_0008": {"func": model_88300_ac762961_0008, "volume": 1037633.7153752584, "area": 79808.6665694127},
    "model_88495_2fdd1d11_0000": {"func": model_88495_2fdd1d11_0000, "volume": 12.9212593502, "area": 87.2019574209},
    "model_88670_b2a44f24_0001": {"func": model_88670_b2a44f24_0001, "volume": 528.2117924119, "area": 473.2219535993},
    "model_88680_0fb9b042_0000": {"func": model_88680_0fb9b042_0000, "volume": 25.97015, "area": 61.86},
    "model_88941_aa581346_0004": {"func": model_88941_aa581346_0004, "volume": 1.5268140296, "area": 8.4823001647},
    "model_88941_aa581346_0008": {"func": model_88941_aa581346_0008, "volume": 8338.4136, "area": 66889.9388},
    "model_88941_aa581346_0014": {"func": model_88941_aa581346_0014, "volume": 7.5982182929, "area": 132.226021958},
    "model_89255_3c610b95_0000": {"func": model_89255_3c610b95_0000, "volume": 8.3731381107, "area": 32.876600294},
    "model_89265_decd9971_0000": {"func": model_89265_decd9971_0000, "volume": 220.3307943575, "area": 1253.9541532685},
    "model_89527_b3bf425d_0014": {"func": model_89527_b3bf425d_0014, "volume": 0.0282743339, "area": 0.6283185307},
    "model_89527_b3bf425d_0017": {"func": model_89527_b3bf425d_0017, "volume": 0.1225221135, "area": 2.8274333882},
    "model_89527_b3bf425d_0022": {"func": model_89527_b3bf425d_0022, "volume": 0.2552544031, "area": 2.4347343065},
    "model_89527_b3bf425d_0026": {"func": model_89527_b3bf425d_0026, "volume": 0.2945243113, "area": 5.1050880621},
    "model_89527_b3bf425d_0031": {"func": model_89527_b3bf425d_0031, "volume": 0.0188495559, "area": 0.4398229715},
    "model_89527_b3bf425d_0034": {"func": model_89527_b3bf425d_0034, "volume": 24.32, "area": 111.28},
    "model_89790_a9620602_0031": {"func": model_89790_a9620602_0031, "volume": 28.1486701762, "area": 51.2707921066},
    "model_89790_a9620602_0032": {"func": model_89790_a9620602_0032, "volume": 48.4904826082, "area": 73.8902592124},
    "model_89907_161bb6f3_0000": {"func": model_89907_161bb6f3_0000, "volume": 18.0641577581, "area": 92.3207887907},
    "model_89939_2c1be711_0001": {"func": model_89939_2c1be711_0001, "volume": 12625.6, "area": 10741.6},
    "model_90106_aaea5474_0000": {"func": model_90106_aaea5474_0000, "volume": 0.0129590697, "area": 1.0799224747},
    "model_90116_d24f5dc4_0000": {"func": model_90116_d24f5dc4_0000, "volume": 2.0853599239, "area": 26.8635374975},
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
