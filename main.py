from isometriesRn.isometries import Glide
from isometriesRn.isometries import NoneZeroTranslation
from isometriesRn.isometries import NoneZeroRotation
from isometriesRn.isometries import Rotation
from isometriesRn.isometries import Reflection
from isometriesRn.isometries import ReflectionComposition


scenes = [
    Glide, 
    NoneZeroTranslation, 
    NoneZeroRotation, 
    Rotation, 
    Reflection, 
    ReflectionComposition
]

if __name__ == "__main__":
    for SceneClass in scenes:
        print(f"--- Rendering: {SceneClass.__name__} ---")
        scene = SceneClass()
        scene.render()
