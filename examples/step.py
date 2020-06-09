from taichi_glsl import *

image = vec_array(3, float, 512, 512)


@ti.kernel
def paint():
    for i, j in image:
        # TODO: for coor in view(image):
        coor = view(image, i, j)
        image[i,
              j] = smoothstep(distance(coor, vec(0.5, 0.5)), 0.5, 0.44) * vec(
                  coor.x, coor.y, 0.0)


paint()
ti.imshow(image)