from manim import *
import numpy as np



class Eigenvalues(Scene):
    def construct(self):
        title = Text("تجزيه جردن و بررسي يک مثال",font="IRAN Kharazmi", font_size=25).scale(1.5)[::-1]
        self.play(Write(title))
        self.play(Unwrite(title))
        A = IntegerMatrix([[11, -3, 3], [-3, 11, 3], [3, 3, 11]]).scale(0.5)
        eq = Text("A = ").shift(2*LEFT)
        gr = VGroup(eq,A.next_to(eq))
        self.play(Write(gr))
        self.play(Transform(gr,gr.copy().to_corner(UL)))
        Acp = A.copy()
        self.add(Acp)
        self.play(Transform(Acp,Acp.copy().move_to([0,0,0])))
        Alam = Matrix([[r"11-\lambda", -3, 3], [-3, r"11-\lambda", 3], [3, 3, r"11-\lambda"]],h_buff=1.6,element_alignment_corner=UP)
        self.play(ReplacementTransform(Acp,Alam))
        det = get_det_text(Alam,0)
        self.play(Write(det))
        simp_det = MathTex(r"(11-\lambda)((11-\lambda)^2-9)-(-3)(-3(11-\lambda)-9)+3(-9-3(11-\lambda))=0").scale(0.5)
        self.play(ReplacementTransform(VGroup(det,Alam),simp_det))
        simp_det2 = MathTex(r"-\lambda^3+33\lambda^2-336\lambda+980=0").scale(0.5)
        self.play(ReplacementTransform(simp_det,simp_det2))
        simp_det = MathTex(r"-(\lambda-5)(\lambda-14)^2=0").scale(0.5)
        self.play(ReplacementTransform(simp_det2,simp_det))
        simp_det2 = MathTex(r"\lambda_1=5 , \lambda_2=\lambda_3=14").scale(0.5)
        self.play(ReplacementTransform(simp_det,simp_det2))
        self.wait(2)

class Eigenvector5(Scene):
    def construct(self):
        title = Text("بردارهاي ويژه",font="IRAN Kharazmi", font_size=25).scale(1.5)[::-1]
        self.play(Write(title))
        self.play(Unwrite(title))
        eq5 = MathTex(r"\lambda_1=5")
        self.play(Write(eq5))
        self.play(eq5.animate.to_edge(UL))
        
        eq = MathTex("A",r"\overrightarrow{x}=\lambda_1\overrightarrow{x}")
        self.play(Write(eq))
        eq2 = MathTex(r"(A-\lambda_1I)",r"\overrightarrow{x}=\overrightarrow{0}")
        self.play(TransformMatchingTex(eq,eq2))
        Alam = Matrix([[r"11-\lambda_1", -3, 3], [-3, r"11-\lambda_1", 3], [3, 3, r"11-\lambda_1"]],h_buff=1.6,element_alignment_corner=UP)
        eq = VGroup(Alam,MathTex(r"\overrightarrow{x}"),MathTex(r"=\overrightarrow{0}")).arrange(RIGHT)
        self.play(ReplacementTransform(eq2,eq))
        x = Matrix([["x_1"], ["x_2"], ["x_3"]])
        zero = Matrix([[0], [0], [0]])
        eq2 = VGroup(Alam,x,MathTex("="),zero).arrange(RIGHT)
        self.play(ReplacementTransform(eq,eq2))
        Am5 = IntegerMatrix([[6, -3, 3], [-3, 6, 3], [3, 3, 6]]).next_to(x,LEFT)
        self.play(ReplacementTransform(Alam,Am5))
        Am5r = IntegerMatrix([[1, 0, 1], [0, 1, 1], [0,0,0]]).next_to(x,LEFT)
        self.play(ReplacementTransform(Am5,Am5r))
        eigen5 = Matrix([["x_1"], ["x_1"], ["-x_1"]])
        self.play(ReplacementTransform(eq2,eigen5))
        

class Eigenvector14(Scene):
    def construct(self):
        eq14 = MathTex(r"\lambda_2=\lambda_3=14")
        self.play(Write(eq14))
        self.play(eq14.animate.to_edge(UL))
        
        eq = MathTex("A",r"\overrightarrow{x}=\lambda_2\overrightarrow{x}")
        self.play(Write(eq))
        eq2 = MathTex(r"(A-\lambda_2I)",r"\overrightarrow{x}=\overrightarrow{0}")
        self.play(TransformMatchingTex(eq,eq2))
        Alam = Matrix([[r"11-\lambda_2", -3, 3], [-3, r"11-\lambda_2", 3], [3, 3, r"11-\lambda_2"]],h_buff=1.6,element_alignment_corner=UP)
        eq = VGroup(Alam,MathTex(r"\overrightarrow{x}"),MathTex(r"=\overrightarrow{0}")).arrange(RIGHT)
        self.play(ReplacementTransform(eq2,eq))
        x = Matrix([["x_1"], ["x_2"], ["x_3"]])
        zero = Matrix([[0], [0], [0]])
        eq2 = VGroup(Alam,x,MathTex("="),zero).arrange(RIGHT)
        self.play(ReplacementTransform(eq,eq2))
        Am14 = IntegerMatrix([[-3, -3, 3], [-3, -3, 3], [3, 3, -3]]).next_to(x,LEFT)
        self.play(ReplacementTransform(Alam,Am14))
        Am14r = IntegerMatrix([[1, 1, -1], [0, 0, 0], [0,0,0]]).next_to(x,LEFT)
        self.play(ReplacementTransform(Am14,Am14r))
        eigen14 = Matrix([["x_1"], ["x_2"], ["x_1+x_2"]],element_alignment_corner=UP).add_background_rectangle()
        self.play(ReplacementTransform(eq2,eigen14))
        #self.play(ReplacementTransform(eigen14,eigen14.copy().next_to(eq14,DOWN)))

        
        

class Eigenvector14_3d(ThreeDScene):
    def construct(self):
        eq14 = MathTex(r"\lambda_2=\lambda_3=14").to_edge(UL).add_background_rectangle()
        eigen14 = (Matrix([["x_1"], ["x_2"], ["x_1+x_2"]],element_alignment_corner=UP)
            .scale(0.5).next_to(eq14,DOWN).add_background_rectangle())
        self.add_fixed_in_frame_mobjects(eigen14,eq14)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        self.play(Create(axes))
        def plotvec(x1,x2):
            v = Vector(direction=[x1,x2,x1+x2],color=BLUE)
            eqt = MathTex("x_1=",x1,",x_2=",x2).to_corner(DL)
            self.add_fixed_in_frame_mobjects(eqt)
            self.play(Create(v))
            self.remove(eqt)
            return v
        self.begin_ambient_camera_rotation(rate=0.5)
        vs = []
        for i in range(-1,2):
            for j in range(-1,2):
                vs.append(plotvec(i,j))
        n = np.cross(np.array([1,1,2]),np.array([-1,1,0]))
        s1 = Surface(lambda x, y : axes.c2p(x,y,-(n[0]*x + n[1]*y)/n[2]),u_range=[-3,3],v_range=[-3,3],resolution=1)
        self.play(FadeIn(s1))
        self.play(Uncreate(VGroup(*vs)))
        
        v = VGroup(Vector([-1,1,0],color=RED),Vector([-1,0.5,-0.5],color=RED))
        self.play(Unwrite(eigen14))
        eigen14 = (VGroup(Matrix([[-1], [1], [0]],element_alignment_corner=UP),Text(","),
                          Matrix([[-1], [0.5], [-0.5]],element_alignment_corner=UP))
            .scale(0.5).arrange(RIGHT).next_to(eq14,DOWN).add_background_rectangle())
        self.add_fixed_in_frame_mobjects(eigen14)
        self.play(Create(v))
        self.wait(1)
        self.play(Uncreate(v))

        v = VGroup(Vector([-1,1,0],color=GREEN),Vector([0.5,0.5,1],color=GREEN))
        self.play(Unwrite(eigen14))
        eigen14 = (VGroup(Matrix([[-1], [1], [0]],element_alignment_corner=UP),Text(","),
                          Matrix([[0.5], [0.5], [1]],element_alignment_corner=UP))
            .scale(0.5).arrange(RIGHT).next_to(eq14,DOWN).add_background_rectangle())
        self.add_fixed_in_frame_mobjects(eigen14)
        self.play(Create(v))
        
        self.play(Unwrite(VGroup(eigen14,eq14)))
        eigen5 = (VGroup(MathTex("\lambda_1=5"),
                          Matrix([[-0.5], [-0.5], [0.5]],element_alignment_corner=UP))
            .scale(0.5).arrange(DOWN).add_background_rectangle().to_corner(UL))
        self.add_fixed_in_frame_mobjects(eigen5)
        v = Vector([-0.5,-0.5,0.5],color=GREEN)
        self.play(Create(v))
        self.play(Create(Line3D([-3,-3,3],[3,3,-3])))
        self.wait(2)




        

        
            
        
        
def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    scene.play(*animations)


class CombinedScene(ThreeDScene):
    def construct(self):
        scenes = [Eigenvalues,Eigenvector5,Eigenvector14,Eigenvector14_3d] 
        for scene in scenes:
            scene.construct(self)
            fade_out(self)

