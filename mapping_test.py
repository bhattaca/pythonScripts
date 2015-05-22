"""
Conformal animations with MoviePy and Scikit Image, after user u/spel3o on Reddit.
Links:

Reddit discussion:
http://www.reddit.com/r/math/comments/2o9wge/conformal_image_map_animation_of_1z_to/

Original gif:
https://i.imgur.com/2W5dCvF.gif

Gif produced by this script:
http://i.imgur.com/rHlyfJz.gif
"""
 
import numpy as np # for numerical computations
from skimage import transform # for the transformation
import moviepy.editor as mpy # for the animation (Video/GIF)
from urllib import urlretrieve # to download the image
 
def apply_transformation_to_image(image, complex_fun, t):
    """ Applies the conformal tranformation complex_fun(z,t)
        to the given image (z=0 at the center of the image)."""
    def map_coordinates(xy):
        center = np.mean(xy, axis=0)
        xc, yc = (xy - center).T
        new_z = complex_fun(xc+yc*1j, t)
        return np.column_stack([new_z.real, new_z.imag]) + center
    
    new_image = transform.warp(image, map_coordinates, mode='reflect')
    return (255*new_image).astype("uint8")
 
def make_clip(clip, complex_fun):
    """ Makes a MoviePy clip which can be written to a GIF""" 
    def transfo(gf, t):
        return apply_transformation_to_image(gf(t),complex_fun,t)
    return clip.fl( transfo )
 
# Downlad the picture
urlretrieve("http://7thgearonline.files.wordpress.com/2009/05/falling_man.jpg",
                   "falling_man.jpg")
 
# Create the animated clip
 
# The next two lines could be written like this to use an animated clip as a basis
#~ clip = mpy.VideoFileClip("my_video_clip.mp4").resize(width=400)
#~ D = clip.duration # duration in seconds
clip = mpy.ImageClip("falling_man.jpg").resize(width=400)
D = 3 # duration in seconds
 
complex_fun = lambda z,t : clip.w*(300/z - 2*t/D) # our complex transfo.
final_clip = make_clip(clip, complex_fun).set_duration(D)
 
# Write a GIF
final_clip.write_gif("falling_conformal.gif", fps=20)
