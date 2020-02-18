from elems3d import *

def draw3d(*objects, origin=True, axes=True, width=6, save_as=None):
    fig = plt.gcf()
    ax = fig.add_subplot(111, projection='3d')

    all_vectors = list(extract_vectors_3D(objects))
    
    if origin:
        all_vectors.append((0,0,0))
    xs, ys, zs = zip(*all_vectors)

    max_x, min_x = max(0,*xs), min(0,*xs)
    max_y, min_y = max(0,*ys), min(0,*ys)
    max_z, min_z = max(0,*zs), min(0,*zs)

    x_size = max_x - min_x
    y_size = max_y - min_y
    z_size = max_z - min_z

    padding_x = 0.05 * x_size if x_size else 1
    padding_y = 0.05 * y_size if y_size else 1
    padding_z = 0.05 * z_size if z_size else 1

    plot_x_range = (min(min_x - padding_x,-2), max(max_x + padding_x,2))
    plot_y_range = (min(min_y - padding_y,-2), max(max_y + padding_y,2))
    plot_z_range = (min(min_z - padding_z,-2), max(max_z + padding_z,2))
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    def draw_segment(start, end, color=black, linestyle='solid'):
        xs, ys, zs = [[start[i], end[i]] for i in range(0,3)]
        
        ax.plot(xs, ys, zs, color=color, linestyle=linestyle)

    if axes:
        draw_segment( (plot_x_range[0], 0, 0), (plot_x_range[1], 0, 0) )
        draw_segment( (0, plot_y_range[0], 0), (0, plot_y_range[1], 0) )
        draw_segment( (0, 0, plot_z_range[0]), (0, 0, plot_z_range[1]) )

    if origin:
        ax.scatter([0],[0],[0], color='k', marker='x')

    # use key-value pattern
    for object in objects:
        if type(object) == Points3D:
            xs, ys, zs = zip(*object.vectors)
            ax.scatter(xs, ys, zs, color = object.color)

        elif type(object) == Polygon3D:
            for i in range(0, len(object.vertices)):
                draw_segment(
                    object.vertices[i],
                    object.vertices[(i+1) % len(object.vertices)],
                    color = object.color)

        elif type(object) == Arrow3D:
            xs, ys, zs = zip(object.tail, object.tip)
            a = FancyArrow3D(xs, ys, zs, mutation_scale = 20, arrowstyle='-|>', color=object.color)
            ax.add_artist(a)

        elif type(object) == Segment3D:
            draw_segment(object.start_point, object.end_point, color=object.color)

        elif type(object) == Box3D:
            x,y,z = object.vector
            kwargs = {'linestyle':'dashed', 'color':'gray'}
            
            draw_segment((0,y,0), (x,y,0), **kwargs)
            draw_segment((0,0,z), (0,y,z), **kwargs)
            draw_segment((0,0,z), (x,0,z), **kwargs)
            draw_segment((0,y,0), (0,y,z), **kwargs)
            draw_segment((x,0,0), (x,y,0), **kwargs)
            draw_segment((x,0,0), (x,0,z), **kwargs)
            draw_segment((0,y,z), (x,y,z), **kwargs)
            draw_segment((x,0,z), (x,y,z), **kwargs)
            draw_segment((x,y,0), (x,y,z), **kwargs)
        
        elif type(object) == Octohedron:
            x,y,z = object.vector
            kwargs = {'linestyle':'dashed', 'color':'green'}
            
            # draw in loop be good
            draw_segment((0,y,0), (x,y,0), **kwargs)
            draw_segment((0,0,z), (0,y,z), **kwargs)
            draw_segment((0,0,z), (x,0,z), **kwargs)
            draw_segment((0,y,0), (0,y,z), **kwargs)
            draw_segment((x,0,0), (x,y,0), **kwargs)
            draw_segment((x,0,0), (x,0,z), **kwargs)
            draw_segment((0,y,z), (x,y,z), **kwargs)
            draw_segment((x,0,z), (x,y,z), **kwargs)
            draw_segment((x,y,0), (x,y,z), **kwargs)
        else:
            raise TypeError("Unrecognized object: {}".format(object))

    if save_as:
        plt.savefig("images/"+save_as)

    plt.show()
