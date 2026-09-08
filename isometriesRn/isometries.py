from manim import *
import numpy as np

class BaseTransformationScene(MovingCameraScene):    
    def setup(self):
        """Sets up background for every scene"""
        super().setup()
        
        self.axes = Axes(
            x_range=[-10, 80, 1],
            y_range=[-10, 10, 1],
            x_length=110,
            y_length=25,
            tips=True
        ).center()
        
        self.trapezoid_points = [[-1, 2, 0], [-5, 2, 0], [-4, 5, 0], [-2, 5, 0]]
        self.walker = self.create_polygon(self.trapezoid_points, BLUE)


    def create_polygon(self, points, color=WHITE):
        if not points:
            return VGroup()
        # c2p maps math coordinates to the screen coordinates of the axes
        screen_points = [self.axes.c2p(p[0], p[1], p[2]) for p in points]
        return Polygon(*screen_points, color=color)


    def add_text(self, text_string, font_size=72, text_type='LaTeX'):
    
        """
        Frames latex text in white box in upper right corner of the screen.
        Returns: mathematical object (mobject) containing latex text to be displayed.
        """
        if text_type != 'LaTeX':
            text=Text(text_string,color=WHITE,font_size=font_size)
        else:
            text = MathTex(text_string, color=WHITE, font_size=font_size)
        box = SurroundingRectangle(text, color=WHITE, buff=MED_LARGE_BUFF)
        mobjects = VGroup(box, text)
    
        frame_right_edge = self.camera.frame.get_right()[0]
        frame_top_edge = self.camera.frame.get_top()[1]
        mobjects.move_to(np.array([frame_right_edge, frame_top_edge, 0]))
        
        mobjects.shift(RIGHT * 5 + DOWN * 2) # Adjust padding (larger because we zoomed out)
        self.camera.frame.add(mobjects)
        return mobjects


    def setup_tracking_camera(self, target_mobject, scale=2, height=None):
        """
        Camera tracks polygon as it moves across the X-axis. Sets up camera in the beginning frame.
        """
        if height is not None:
            self.camera.frame.set_height(height)
        else:
            self.camera.frame.scale(scale)
        self.camera.frame.save_state()
        start_x = target_mobject.get_center()[0]
        self.camera.frame.move_to(np.array([start_x, 0, 0]))



    @staticmethod
    def reflect(matrix, points):
        return [np.dot(matrix, p[:-1]).tolist() + [0] for p in points]

    @staticmethod
    def translate(vector, points):
        return [(np.array(p[:2]) + vector).tolist() + [0] for p in points]


class Glide(BaseTransformationScene):
    def construct(self):
        reflection_matrix = np.array([[1, 0], [0, -1]])
        translation_vector = np.array([0, 6])
        
        #setup scene
        self.setup_tracking_camera(self.walker)    
        self.add(self.axes, self.walker,self.add_text(r"\det A = -1, \quad w \ne 0"))
        self.wait(1)

        current_points = self.trapezoid_points

        for _ in range(4):
            footprint = self.walker.copy().set_color(WHITE)
            self.add(footprint)
            self.bring_to_back(footprint)

            # calculate isometry action points
            reflected_data = self.reflect(reflection_matrix, current_points)
            glided_data = self.translate(translation_vector, reflected_data)

            reflected_polygon = self.create_polygon(reflected_data, BLUE)
            glided_polygon = self.create_polygon(glided_data, WHITE)

            # reflection
            self.play(
                Transform(self.walker, reflected_polygon),
                run_time=1.0
            )

            # translation and camera tracking
            target_camera_point = np.array([glided_polygon.get_center()[0], 0, 0])
            self.play(
                Transform(self.walker, glided_polygon),
                self.camera.frame.animate.move_to(target_camera_point),
                run_time=1.5,
                rate_functions=linear
            )
            
            current_points = glided_data


class NoneZeroTranslation(BaseTransformationScene):
    def construct(self):
        reflection_matrix = np.array([[1,  0],[0, 1] ])
        translation_vector = np.array([6,0])

        self.setup_tracking_camera(self.walker)    
        self.add(self.axes, self.walker,self.add_text(r"A = I_2, \quad w \ne 0"))
        self.wait(1)

        current_points = self.trapezoid_points

        for _ in range(4):
            footprint = self.walker.copy().set_color(WHITE)
            self.add(footprint)
            self.bring_to_back(footprint)

            # calculate isometry action points
            reflected_data = self.reflect(reflection_matrix, current_points)
            glided_data = self.translate(translation_vector, reflected_data)

            reflected_polygon = self.create_polygon(reflected_data, BLUE)
            glided_polygon = self.create_polygon(glided_data, WHITE)

            # reflection
            self.play(
                Transform(self.walker, reflected_polygon),
                run_time=1.0
            )
            # translation and camera tracking
            target_camera_point = np.array([glided_polygon.get_center()[0], 0, 0])
            self.play(
                Transform(self.walker, glided_polygon),
                self.camera.frame.animate.move_to(target_camera_point),
                run_time=1.5,
                rate_functions=linear
            )
            
            current_points = glided_data
        

class NoneZeroRotation(BaseTransformationScene):
    def construct(self):
        rotation_matrix = np.array([[0,  -1],[1, 0] ])
        translation_vector = np.array([3,0])
        self.setup_tracking_camera(self.walker, height=28)    
        self.add(self.axes, self.walker,self.add_text(r" \det A = 1, A \ne I_2, w\ne 0"))
        self.wait(1)

        current_points = self.trapezoid_points

        for _ in range(4):
            footprint = self.walker.copy().set_color(WHITE)
            self.add(footprint)
            self.bring_to_back(footprint)

            # calculate isometry action points
            reflected_data = self.reflect(rotation_matrix, current_points)
            glided_data = self.translate(translation_vector, reflected_data)

            reflected_polygon = self.create_polygon(reflected_data, BLUE)
            glided_polygon = self.create_polygon(glided_data, WHITE)

            # reflection
            self.play(
                Transform(self.walker, reflected_polygon),
                run_time=1.0
            )
            # translation and camera tracking
            self.play(
                Transform(self.walker, glided_polygon),
                run_time=1.5,
                rate_functions=linear
            )
            
            current_points = glided_data


class Rotation(BaseTransformationScene):
    def construct(self):
        rotation_matrix = np.array([[0,  -1],[1, 0] ])
        self.setup_tracking_camera(self.walker, height=28)    
        self.add(self.axes, self.walker,self.add_text(r" \det A = 1, A \ne I_2, w= 0"))
        self.wait(1)

        current_points = self.trapezoid_points

        for _ in range(4):
            footprint = self.walker.copy().set_color(WHITE)
            self.add(footprint)
            self.bring_to_back(footprint)

            # calculate isometry action points
            rotation_data = self.reflect(rotation_matrix, current_points)
            rotation_polygon = self.create_polygon(rotation_data, BLUE)

            # rotation
            self.play(
                Transform(self.walker, rotation_polygon),
                run_time=1.0
            )
            self.wait(1.5)

            current_points = rotation_data


class Reflection(BaseTransformationScene):
    def construct(self):
        reflection_matrix = np.array([[1,  0],[0, -1] ])
        #setup scene
        self.setup_tracking_camera(self.walker)    
        self.add(self.axes, self.walker,self.add_text(r"\det A = -1, w=0"))
        self.wait(1)

        current_points = self.trapezoid_points
        for _ in range(4):
            footprint = self.walker.copy().set_color(WHITE)
            self.add(footprint)
            self.bring_to_back(footprint)

            # calculate isometry action points
            reflected_data = self.reflect(reflection_matrix, current_points)
            reflected_polygon = self.create_polygon(reflected_data, BLUE)

            # reflection
            self.play(
                Transform(self.walker, reflected_polygon),
                run_time=1.0
            )
            self.wait(1.5)
            
            current_points = reflected_data


class ReflectionComposition(BaseTransformationScene):
    def construct(self):
        matrix1 = np.array([[-1,0],[0,1]])
        matrix2 = np.array([[1,0],[0,-1]])
        translation_vector = np.array([8,0])
        #setup scene
        self.setup_tracking_camera(self.walker)    
        self.add(self.axes, self.walker,self.add_text("Composition of three reflections",font_size=48, text_type='Text'))
        self.wait(1)

        current_points = self.trapezoid_points

        for _ in range(3):
            footprint = self.walker.copy().set_color(WHITE)
            self.add(footprint)
            self.bring_to_back(footprint)

            # calculate isometry action points
            reflection1_data = self.reflect(matrix1, current_points)
            reflection2_data = self.translate(translation_vector, self.reflect(matrix1, reflection1_data))
            reflection3_data = self.reflect(matrix2, reflection2_data)

            polygon1 = self.create_polygon(reflection1_data, WHITE).set_stroke(width=2)
            polygon2 = self.create_polygon(reflection2_data, RED).set_stroke(width=2)
            polygon3 = self.create_polygon(reflection3_data, BLUE).set_stroke(width=2)


            self.play(
                Transform(self.walker, polygon1),
                run_time=1.5
            )
            self.play(
                Transform(self.walker, polygon2),
                run_time=1.5
            )

            cam_target = np.array([polygon3.get_center()[0], 0, 0])
            self.play(
                Transform(self.walker, polygon3),
                self.camera.frame.animate.move_to(cam_target),
                run_time=1.5
            )

            current_points = reflection3_data

        self.play(
            self.camera.frame.animate.scale(1.5).shift(LEFT * 14),
            run_time=1.5
        )
        self.wait(1)


