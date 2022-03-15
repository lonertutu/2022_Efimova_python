import pygame
import pygame.draw as dr
pygame.init()


# константа pi
pi = 3.14

# константа для таймера
FPS = 30

# сделаем заготовку окна на экране, в котором будем рисовать
screen = pygame.display.set_mode((900, 700))

# пропишим цвета согласно калькулятору RGB
CORAL = (245, 155, 141)
PINKY = (245, 204, 190)
BAMBOO = (54, 117, 50)
WHITE = (255, 238, 249)
REALWHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACKY = (30, 20, 44)
GREY = (42, 31, 47)
BEIGE = (250, 235, 215)
OLIVE = (107, 142, 35)
BAMBOO2 = (60, 155, 50)
DARKOLIVE = (69, 97, 47)
LIGHTGREEN = (74, 185, 75)


def writer_smoothly_flowing_surface(r, g, b, bias, x0, y0, x1, y1,
                                    color_r_constant, color_g_constant, color_b_constant):
    """
    :param r: начальный параметр цвета по красному цвету
    :param g: начальный параметр цвета по зеленому цвету
    :param b: начальный параметр цвета по синиму цвету
    :param bias: константа, показывающая, куда смещаемся при рисовании линии
    :param x0: начальная координата точки по х
    :param y0: начальная координата точки по y
    :param x1: конечнаая координата точки по х
    :param y1: конечная координата точки по y
    :param color_r_constant: константа га которую умножается константа перехода цвета к новому оттенку r
    :param color_g_constant: константа га которую умножается константа перехода цвета к новому оттенку g
    :param color_b_constant: константа га которую умножается константа перехода цвета к новому оттенку b
    функция рисует переходы неба и земли
    """

    color_change_constant = 1

    # будем плавно изменять нужный нам цвет и прорисовывать его на экране с помощью линий

    for i in range(80):
        red = r + color_change_constant * color_r_constant
        green = g + color_change_constant * color_g_constant
        blue = b + color_change_constant * color_b_constant
        name_of_color = (red, green, blue)
        if bias == -1:
            i *= -1
        dr.aaline(screen, name_of_color, [x0, y0 + i], [x1, y1 + i])
        if bias == -1:
            i *= -1
        color_change_constant += 1


def make_trunk(color_of_trunk, x1, y1, x2, y2, x3, y3, x4, y4):

    """
    :param color_of_trunk: цвет ствола дерева
    :param x1: 1-ая координата многоугльника по x
    :param y1: 1-ая координата многоугльника по y
    :param x2: 2-ая координата многоугльника по x
    :param y2: 2-ая координата многоугльника по y
    :param x3: 3-ая координата многоугльника по x
    :param y3: 3-ая координата многоугльника по y
    :param x4: 4-ая координата многоугльника по x
    :param y4: 4-ая координата многоугльника по y
    функция создает ствол дерева
    """

    dr.polygon(screen, color_of_trunk, [[x1, y1], [x2, y2], [x3, y3], [x4, y4]])


def make_bamboo_tree(color_of_1_trunk, x1, y1, x2, y2, x3, y3, x4, y4, color_of_2_trunk, color_of_3_trunk,):

    """
    :param color_of_1_trunk: цвет основного ствола дерева
    :param x1: 1-ая координата многоугльника по x основного ствола дерева
    :param y1: 1-ая координата многоугльника по y основного ствола дерева
    :param x2: 2-ая координата многоугльника по x основного ствола дерева
    :param y2: 2-ая координата многоугльника по y основного ствола дерева
    :param x3: 3-ая координата многоугльника по x основного ствола дерева
    :param y3: 3-ая координата многоугльника по y основного ствола дерева
    :param x4: 4-ая координата многоугльника по x основного ствола дерева
    :param y4: 4-ая координата многоугльника по y основного ствола дерева
    :param color_of_2_trunk: цвет темнойчасти ствола дерева
    :param color_of_3_trunk: цвет светлой части ствола дерева
    """

    # константные множители - коэфициенты проопорциональности
    make_trunk(color_of_1_trunk, x1, y1, x2, y2, x3, y3, x4, y4)
    make_trunk(color_of_2_trunk, x1 * 1.05, y1, x2 * 0.99, y2, x3 * 0.97, y3, x4 * 1.067, y4)
    make_trunk(color_of_3_trunk, x1 * 1.01, y1, x2 * 0.97, y2, x3 * 0.94, y3, x4 * 1.03, y4)

def make_leaf(color_of_leaf, x1, y1, x2, y2, width):
    """
    :param color_of_leaf: цвет листа
    :param x1: координата начала листа по x
    :param y1: координата начала листа по y
    :param x2: координата конца листа по x
    :param y2: координата конца листа по y
    :param width: ширина листа
    функция создает лист дерева
    """
    dr.line(screen, color_of_leaf, (x1, y1), (x2, y2), width)


def body_of_left_panda(x_position, y_position, length, width, size):
    """
    :param size: коэфициент размера тела относительно панды
    :param x_position: координата по x верхнего угла прямоугольника, в который вписана голова панды
    :param y_position: координата по x верхнего угла прямоугольника, в который вписана голова панды
    :param length: длина прямоугольника, в который вписана голова панды
    :param width: ширина прямоугольника, в который вписана голова панды
    """

    dr.ellipse(screen, WHITE, (x_position, y_position, length * size, width * size))

    bias_coord_x1 = 30 * size
    bias_coord_y1 = 10 * size
    stretching1 = 220 / 150 * size
    extension1 = 160 / 160 * size
    dr.ellipse(screen, WHITE, (x_position + bias_coord_x1, y_position + bias_coord_y1,
                               length * stretching1, width * extension1))


def make_left_leg_of_left_panda(x_position, y_position, length, width, size):
    """
    :param x_position: координата по х эллиппса верхней части ноги
    :param y_position: координта по у эллипса верхней части ноги
    :param length: длина эллиппса верхней части ноги
    :param width: ширина эллиппса верхней части ноги
    :param size: коэфициент размера ноги относительно панды
    """
    dr.ellipse(screen, BLACK, [x_position, y_position, length * size, width * size])
    bias_coord_y1 = 65 * size
    bias_coord_x1 = 45 * size
    bias_coord_x2 = 25 * size
    bias_coord_y2 = 155 * size
    bias_coord_y3 = 165 * size
    bias_coord_x3 = 45 * size
    bias_coord_y4 = 120 * size
    dr.polygon(screen, BLACK, [[x_position, y_position + bias_coord_y1],
                               [x_position - bias_coord_x1, y_position + bias_coord_y2],
                               [x_position + bias_coord_x2, y_position + bias_coord_y3],
                               [x_position + bias_coord_x3, y_position + bias_coord_y4]])
    bias_coord_x1 = 50 * size
    bias_coord_y1 = 130 * size
    stretching1 = 80 / 60 * size
    extension1 = 50 / 130 * size

    dr.ellipse(screen, BLACK, [x_position - bias_coord_x1, y_position + bias_coord_y1,
                               length * stretching1, width * extension1])


def make_front_right_leg_of_left_panda(x_coordinate, y_coordinate, length, width, size):
    """
    :param size: коэфициент размера ноги относительно панды
    :param x_coordinate: координата по х эллиппса верхней части ноги
    :param y_coordinate: координата по y эллиппса верхней части ноги
    :param length: длина эллиппса верхней части ноги
    :param width: ширина эллиппса верхней части ноги
    """
    dr.ellipse(screen, BLACKY, [x_coordinate, y_coordinate, length * size, width * size])
    bias_coord_y1 = 110 * size
    bias_coord_x1 = 25 * size
    bias_coord_x2 = 55 * size
    bias_coord_x3 = 70 * size
    bias_coord_x4 = 40 * size

    dr.polygon(screen, BLACKY, [[x_coordinate + bias_coord_x1, y_coordinate],
                                [x_coordinate + bias_coord_x2, y_coordinate],
                                [x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y1],
                                [x_coordinate + bias_coord_x4, y_coordinate + bias_coord_y1]])
    bias_coord_y2 = 10 * size
    bias_coord_x5 = 25 * size
    bias_coord_x6 = 70 * size
    bias_coord_y3 = 110 * size
    bias_coord_x8 = 40 * size
    bias_coord_y4 = 149 * size
    bias_coord_x9 = 15 * size
    bias_coord_y5 = 140 * size
    dr.polygon(screen, BLACKY, [[x_coordinate + bias_coord_x5, y_coordinate + bias_coord_y2],
                                [x_coordinate + bias_coord_x6, y_coordinate + bias_coord_y3],
                                [x_coordinate + bias_coord_x8, y_coordinate + bias_coord_y4],
                                [x_coordinate - bias_coord_x9, y_coordinate + bias_coord_y5]])

    bias_coord_y6 = 120 * size
    bias_coord_x10 = 23 * size
    length_proport_fact = 65 / 40 * size
    width_proport_fact = 45 / 130 * size

    dr.ellipse(screen, BLACKY, [x_coordinate - bias_coord_x10, y_coordinate + bias_coord_y6,
                                length * length_proport_fact, width * width_proport_fact])


def make_ear(x_coordinate, y_coordinate, length, width, size):
    """

    :param x_coordinate: координата верхнего угла уха по х
    :param y_coordinate: координата верхнего угла уха по у
    :param length: длина уха
    :param width: ширина уха
    :param size: коэфициент размера уха относительно панды
    """

    dr.rect(screen, BLACK, (x_coordinate, y_coordinate, length * size, width * size), border_top_right_radius=50,
            border_bottom_left_radius=40, border_bottom_right_radius=40, border_top_left_radius=80)


def make_head(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: координата левого эллипса по х
    :param y_coordinate: координата левого эллипса по у
    :param length: длина левого эллипса уха
    :param width: ширина левого эллипса уха
    :param size: коэфициент головы относительно панды
    """

    dr.ellipse(screen, REALWHITE, (x_coordinate, y_coordinate, length * size, width * size))  # head

    bias_coord_x1 = 20 * size
    bias_coord_y1 = 10 * size
    stretching1 = 99 / 120
    extension1 = 90 / 100
    bias_coord_x2 = 10 * size
    bias_coord_y2 = 5 * size
    stretching2 = 100 / 120 * size
    extension2 = 125 / 100 * size
    dr.ellipse(screen, REALWHITE, [x_coordinate + bias_coord_x1, y_coordinate + bias_coord_y1,
                                   length * stretching1, width * extension1])
    dr.ellipse(screen, REALWHITE, [x_coordinate - bias_coord_x2, y_coordinate - bias_coord_y2,
                                   length * stretching2, width * extension2])


def make_face(x_coordinate, y_coordinate, length, width, size):

    """
    :param x_coordinate: координата эллипса морды панды по х
    :param y_coordinate: координата эллипса морды панды по у
    :param length: длина эллипса морды панды по у
    :param width: ширина эллипса морды панды по у
    :param size: размер морды панды относительно панды
    """

    dr.ellipse(screen, BEIGE, [x_coordinate, y_coordinate, length * size, width * size])

    bias_coord_y1 = 10 * size
    bias_coord_x1 = 20 * size
    bias_coord_x2 = 50 * size
    bias_coord_y2 = 30 * size
    bias_coord_y3 = 25 * size
    dr.polygon(screen, BEIGE, [[x_coordinate + bias_coord_x1, y_coordinate - bias_coord_y1],
                               [x_coordinate + bias_coord_x2, y_coordinate],
                               [x_coordinate + bias_coord_x2, y_coordinate + bias_coord_y2],
                               [x_coordinate, y_coordinate + bias_coord_y3]])
    bias_coord_x4 = 40 * size
    bias_coord_y4 = 15 * size
    stretching1 = 30 / 70 * size
    extension1 = 30 / 50 * size
    dr.rect(screen, BLACK, (x_coordinate + bias_coord_x4, y_coordinate - bias_coord_y4,
                            length * stretching1, width * extension1),
            border_top_right_radius=20, border_bottom_left_radius=20,
            border_bottom_right_radius=7, border_top_left_radius=10)

    bias_coord_x5 = 10 * size
    bias_coord_y5 = 15 * size
    stretching2 = 10 / 70 * size
    extension2 = 20 / 50 * size
    dr.rect(screen, BLACK, (x_coordinate + bias_coord_x5, y_coordinate - bias_coord_y5,
                            length * stretching2, width * extension2),
            border_top_right_radius=5, border_bottom_left_radius=5,
            border_bottom_right_radius=5, border_top_left_radius=5)

    bias_coord_y6 = 25 * size
    stretching3 = 20 / 70 * size
    extension3 = 15 / 50 * size
    dr.rect(screen, BLACK, (x_coordinate, y_coordinate + bias_coord_y6, length * stretching3, width * extension3),
            border_top_right_radius=5, border_bottom_left_radius=10,
            border_bottom_right_radius=10, border_top_left_radius=5)

    bias_coord_y7 = 35 * size
    bias_coord_x7 = 10 * size
    stretching3 = 25 / 70 * size
    extension3 = 15 / 50 * size
    dr.rect(screen, BLACK, (x_coordinate + bias_coord_x7, y_coordinate + bias_coord_y7,
                            length * stretching3, width * extension3),
            border_top_right_radius=5, border_bottom_left_radius=20,
            border_bottom_right_radius=25, border_top_left_radius=7)


def make_left_panda(x_coordinate, y_coordinate, length, width):
    """

    :param x_coordinate: координата головы по x
    :param y_coordinate: координата головы по x
    :param length: длина координата головы по x
    :param width: ширина координата головы по x
    """

    size = 1
    bias_coord_x1 = 5 * size
    bias_coord_y1 = 95 * size
    stretching1 = 40 / 120 * size
    extension1 = 130 / 100 * size
    make_front_right_leg_of_left_panda(x_coordinate - bias_coord_x1, y_coordinate + bias_coord_y1,
                                       length * stretching1, width * extension1, size * 0.9)

    bias_coord_x2 = 45 * size
    bias_coord_y2 = 35 * size
    stretching2 = 150 / 120 * size
    extension2 = 160 / 100 * size
    body_of_left_panda(x_coordinate + bias_coord_x2, y_coordinate + bias_coord_y2,
                       length * stretching2, width * extension2, size)

    bias_coord_x3 = 95 * size
    bias_coord_y3 = 65 * size
    stretching3 = 60 / 120 * size
    extension3 = 130 / 100 * size
    make_left_leg_of_left_panda(x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y3,
                                length * stretching3, width * extension3, size * 1.2)

    bias_coord_x3 = 225 * size
    bias_coord_y3 = 105 * size
    stretching3 = 60 / 120 * size
    extension3 = 130 / 100 * size
    make_left_leg_of_left_panda(x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y3,
                                length * stretching3, width * extension3, size)

    # правое ухо панды
    bias_coord_x4 = 10 * size
    bias_coord_y4 = 30 * size
    stretching4 = 23 / 120 * size
    extension4 = 45 / 100 * size
    make_ear(x_coordinate + bias_coord_x4, y_coordinate - bias_coord_y4,
             length * stretching4, width * extension4, size)

    make_head(x_coordinate, y_coordinate, length, width, size)

    # левое ухо панды
    bias_coord_x5 = 65 * size
    bias_coord_y5 = 15 * size
    stretching5 = 25 / 120 * size
    extension5 = 35 / 100 * size
    make_ear(x_coordinate + bias_coord_x5, y_coordinate - bias_coord_y5,
             length * stretching5, width * extension5, size)

    bias_coord_x6 = 15 * size
    bias_coord_y6 = 65 * size
    stretching6 = 70 / 120 * size
    extension6 = 50 / 100 * size
    make_face(x_coordinate - bias_coord_x6, y_coordinate + bias_coord_y6,
              length * stretching6, width * extension6, size)


def make_body_of_right_panda(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: координаты эллипса, входящего в туловеще, по х
    :param y_coordinate: координаты эллипса, входящего в туловеще, по у
    :param length: длина эллипса, входящего в туловеще
    :param width: длина эллипса, входящего в туловеще
    :param size: размер туловища относительно панды
    """

    dr.ellipse(screen, REALWHITE, (x_coordinate, y_coordinate, length * size, width * size))

    bias_coord_x1 = 20 * size
    bias_coord_y1 = 50 * size
    bias_coord_x2 = 150 * size
    bias_coord_y2 = 100 * size
    bias_coord_x3 = 215 * size
    bias_coord_y3 = 50 * size
    bias_coord_y4 = 80 * size
    dr.polygon(screen, REALWHITE, [[x_coordinate + bias_coord_x1, y_coordinate - bias_coord_y1],
                                   [x_coordinate + bias_coord_x2, y_coordinate - bias_coord_y2],
                                   [x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y3],
                                   [x_coordinate, y_coordinate + bias_coord_y4]])

    bias_coord_x5 = 55 * size
    bias_coord_y5 = 140 * size
    bias_coord_x6 = 115 * size
    bias_coord_y6 = 130 * size
    bias_coord_x7 = 150 * size
    bias_coord_y7 = 100 * size
    bias_coord_y8 = 50 * size
    bias_coord_x8 = 20 * size
    dr.polygon(screen, REALWHITE, [[x_coordinate + bias_coord_x5, y_coordinate - bias_coord_y5],
                                   [x_coordinate + bias_coord_x6, y_coordinate - bias_coord_y6],
                                   [x_coordinate + bias_coord_x7, y_coordinate - bias_coord_y7],
                                   [x_coordinate + bias_coord_x8, y_coordinate - bias_coord_y8]])


def make_back_left_leg_of_right_panda(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: координаты эллипса, входящего в ногу, по х
    :param y_coordinate: координаты эллипса, входящего в ногу, по у
    :param length: длина эллипса, входящего в ногу
    :param width: длина эллипса, входящего в ногу
    :param size: размер ноги относительно панды
    """

    dr.ellipse(screen, BLACK, (x_coordinate, y_coordinate, length * size, width * size))

    bias_coord_x1 = 40 * size
    bias_coord_y1 = 10 * size
    stretching1 = 60 / 80 * size
    extension1 = 50 / 55 * size
    dr.rect(screen, BLACK, (x_coordinate + bias_coord_x1, y_coordinate + bias_coord_y1,
                            length * stretching1, width * extension1),
            border_top_right_radius=40, border_bottom_left_radius=20,
            border_bottom_right_radius=25, border_top_left_radius=5)


def make_front_left_leg(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: координаты эллипса, входящего в лапу, по х
    :param y_coordinate: координаты эллипса, входящего в лапу, по у
    :param length: длина эллипса, входящего в лапу
    :param width: длина эллипса, входящего в лапу
    :param size: размер лапы относительно панды
    """
    dr.ellipse(screen, BLACKY, (x_coordinate, y_coordinate, length * size, width * size))

    bias_coord_x1 = 5 * size
    bias_coord_y1 = 140 * size
    bias_coord_x2 = 65 * size
    bias_coord_y2 = 30 * size
    bias_coord_x3 = 10 * size
    bias_coord_y3 = 30 * size
    bias_coord_y4 = 130 * size
    bias_coord_x4 = 25 * size
    dr.polygon(screen, BLACKY, [[x_coordinate - bias_coord_x1, y_coordinate - bias_coord_y1],
                                [x_coordinate + bias_coord_x2, y_coordinate + bias_coord_y2],
                                [x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y3],
                                [x_coordinate - bias_coord_x4, y_coordinate - bias_coord_y4]])


def make_hed_of_right_panda(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: положение головы панды по x
    :param y_coordinate: положение головы панды по y
    :param length: длина головы панды
    :param width: щирина головы панды
    :param size: размер головы относительно панды
    """
    dr.ellipse(screen, WHITE, (x_coordinate, y_coordinate, length * size, width * size))


def make_face_of_left_panda(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: положение левого глаза по х
    :param y_coordinate: положение левого глаза по у
    :param length: длина левого глаза
    :param width: ширина левого глаза
    :param size: размер лица относительно панды
    """
    # левый глаз
    dr.rect(screen, BLACK, (x_coordinate, y_coordinate, length * size, width * size),
            border_top_right_radius=55, border_bottom_left_radius=40,
            border_bottom_right_radius=25, border_top_left_radius=15)

    # морда
    bias_coord_x1 = 40 * size
    stretching1 = 45 / 10 * size
    extension1 = 50 / 25 * size
    dr.rect(screen, REALWHITE, (x_coordinate - bias_coord_x1, y_coordinate, length * stretching1, width * extension1),
            border_top_right_radius=55, border_bottom_left_radius=40,
            border_bottom_right_radius=25, border_top_left_radius=15)
    # нос
    bias_coord_x2 = 20 * size
    bias_coord_y2 = 30 * size
    stretching2 = 24 / 10 * size
    extension2 = 15 / 25 * size
    dr.rect(screen, BLACK, (x_coordinate - bias_coord_x2, y_coordinate + bias_coord_y2, length * stretching2, width * extension2),
            border_top_right_radius=55, border_bottom_left_radius=40,
            border_bottom_right_radius=25, border_top_left_radius=15)

    # улыбка
    bias_coord_x3 = 40 * size
    stretching3 = 45 / 10 * size
    extension3 = 50 / 25 * size
    dr.arc(screen, BLACK, (x_coordinate - bias_coord_x3, y_coordinate,
                           length * stretching3, width * extension3), (5 / 4) * pi, (5 / 3) * pi, 4)

    # правый глаз
    bias_coord_x4 = 45 * size
    stretching4 = 20 / 10 * size
    extension4 = 30 / 25 * size
    dr.rect(screen, BLACK, (x_coordinate - bias_coord_x4, y_coordinate, length * stretching4, width * extension4),
            border_top_right_radius=15, border_bottom_left_radius=10,
            border_bottom_right_radius=25, border_top_left_radius=15)


def make_front_right_leg_of_right_panda(x_coordinate, y_coordinate, length, width, size):
    """
    :param x_coordinate: положение по х эллипса из верхней части руки
    :param y_coordinate: положение по у эллипса из верхней части руки
    :param length: длина эллипса из верхней части руки
    :param width: ширина эллипса из верхней части руки
    :param size: размерруки относительноо панды
    """
    dr.ellipse(screen, BLACK, (x_coordinate, y_coordinate, length * size, width * size))

    bias_coord_x1 = 70 * size
    bias_coord_y1 = 65 * size
    stretching1 = 80 / 110 * size
    extension1 = 60 / 110 * size
    dr.ellipse(screen, BLACK, (x_coordinate + bias_coord_x1, y_coordinate + bias_coord_y1,
                               length * stretching1, width * extension1))

    bias_coord_x2 = 40 * size
    bias_coord_y2 = 105 * size
    bias_coord_x3 = 95 * size
    bias_coord_y3 = 20 * size
    bias_coord_x4 = 145 * size
    bias_coord_y4 = 80 * size
    bias_coord_x5 = 100 * size
    bias_coord_y5 = 125 * size
    dr.polygon(screen, BLACK, [[x_coordinate + bias_coord_x2, y_coordinate + bias_coord_y2],
                               [x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y3],
                               [x_coordinate + bias_coord_x4, y_coordinate + bias_coord_y4],
                               [x_coordinate + bias_coord_x5, y_coordinate + bias_coord_y5]])

    bias_coord_x6 = 115 * size
    bias_coord_y6 = 45 * size
    bias_coord_x7 = 175 * size
    bias_coord_y7 = 25 * size
    bias_coord_x8 = 185 * size
    bias_coord_y8 = 75 * size
    bias_coord_x9 = 125 * size
    bias_coord_y9 = 120 * size
    dr.polygon(screen, BLACK, [[x_coordinate + bias_coord_x6, y_coordinate + bias_coord_y6],
                               [x_coordinate + bias_coord_x7, y_coordinate + bias_coord_y7],
                               [x_coordinate + bias_coord_x8, y_coordinate + bias_coord_y8],
                               [x_coordinate + bias_coord_x9, y_coordinate + bias_coord_y9]])
    bias_coord_x10 = 145 * size
    bias_coord_y10 = 25 * size
    stretching10 = 50 / 110 * size
    extension10 = 60 / 110 * size
    dr.ellipse(screen, BLACK, (x_coordinate + bias_coord_x10, y_coordinate + bias_coord_y10,
                               length * stretching10, width * extension10))


def make_right_panda(x_coordinate, y_coordinate, length, width):
    """
    :param x_coordinate: положение тела по х
    :param y_coordinate: положение тела по у
    :param length: длина тела
    :param width: ширина тела
    """
    size = 1
    make_body_of_right_panda(x_coordinate, y_coordinate, length, width, size)
    bias_coord_x1 = 130 * size
    bias_coord_y1 = 210 * size
    stretching1 = 30 / 220 * size
    extension1 = 50 / 150 * size
    make_ear(x_coordinate + bias_coord_x1, y_coordinate - bias_coord_y1,
             length * stretching1, width * extension1, size * 1.5)

    bias_coord_x2 = 165 * size
    bias_coord_y2 = 50 * size
    stretching2 = 80 / 220 * size
    extension2 = 55 / 150 * size
    make_back_left_leg_of_right_panda(x_coordinate + bias_coord_x2, y_coordinate + bias_coord_y2,
                                      length * stretching2, width * extension2, size)

    bias_coord_x3 = 165 * size
    bias_coord_y3 = 50 * size
    stretching3 = 65 / 220 * size
    extension3 = 60 / 150 * size
    make_front_left_leg(x_coordinate + bias_coord_x3, y_coordinate + bias_coord_y3,
                        length * stretching3, width * extension3, size)

    bias_coord_x4 = 55 * size
    bias_coord_y4 = 200 * size
    stretching4 = 130 / 220 * size
    extension4 = 130 / 150 * size
    make_hed_of_right_panda(x_coordinate + bias_coord_x4, y_coordinate - bias_coord_y4,
                            length * stretching4, width * extension4, size)

    bias_coord_x5 = 75 * size
    bias_coord_y5 = 98 * size
    stretching5 = 80 / 220 * size
    extension5 = 55 / 150 * size
    make_back_left_leg_of_right_panda(x_coordinate + bias_coord_x5, y_coordinate + bias_coord_y5,
                                      length * stretching5, width * extension5, size * 1.65)
    bias_coord_x10 = 140 * size
    bias_coord_y10 = 90 * size
    bias_coord_x11 = 200 * size
    bias_coord_y11 = 30 * size
    make_leaf(BAMBOO2, x_coordinate + bias_coord_x10, y_coordinate - bias_coord_y10,
              x_coordinate + bias_coord_x11, y_coordinate + bias_coord_y11, size * 15)

    bias_coord_x6 = 150 * size
    bias_coord_y6 = 150 * size
    stretching6 = 10 / 220 * size
    extension6 = 25 / 150 * size
    make_face_of_left_panda(x_coordinate + bias_coord_x6, y_coordinate - bias_coord_y6,
                            length * stretching6, width * extension6, size)

    bias_coord_x7 = 65 * size
    bias_coord_y7 = 210 * size
    stretching7 = 40 / 220 * size
    extension7 = 50 / 150 * size
    make_ear(x_coordinate + bias_coord_x7, y_coordinate - bias_coord_y7,
             length * stretching7, width * extension7, size)

    bias_coord_x8 = 10 * size
    bias_coord_y8 = 80 * size
    stretching8 = 110 / 220 * size
    extension8 = 110 / 150 * size
    make_front_right_leg_of_right_panda(x_coordinate + bias_coord_x8, y_coordinate - bias_coord_y8,
             length * stretching8, width * extension8, size)


# работаем с верхним окном на экране (устанавливаем цвета и прозрачность)
surf = pygame.Surface((900, 350))
surf.fill((245, 165, 151))
surf.set_alpha(100)

# создадим окно на экране, в котором будем рисовать. Подберем нужные цвета для фона
dr.rect(screen, CORAL, (0, 0, 900, 700))
dr.rect(screen, OLIVE, (0, 350, 900, 700))

# сделаем тени оот мишек на земле
dr.ellipse(screen, DARKOLIVE, (200, 455, 250, 70))
dr.ellipse(screen, DARKOLIVE, (570, 485, 250, 70))
dr.ellipse(screen, DARKOLIVE, (470, 485, 150, 70))

# рисуем нижний переход неба
writer_smoothly_flowing_surface(165, 75, 71, -1, 0, 350, 900, 350, 1, 1, 1)

# рисуем верхний переход неба
writer_smoothly_flowing_surface(165, 75, 91, 1, 0, 0, 900, 0, 1, 1, 1)

# рисуем верхний переход земли
writer_smoothly_flowing_surface(187, 222, 125, 1, 0, 350, 900, 350, -1, -1, -1)

# рисуем нижнюю часть земли
writer_smoothly_flowing_surface(10, 20, 10, -1, 0, 700, 900, 700, 1.2, 1.525, 0.3)

# нарисуем деревья
make_bamboo_tree(BAMBOO2, 300, 0, 340, 0, 350, 300, 295, 300, BAMBOO, LIGHTGREEN)

make_bamboo_tree(BAMBOO2, 540, 0, 560, 0, 570, 300, 530, 300, BAMBOO, LIGHTGREEN)
# сделаем так, чтобы некоторые деревья были вдлаи
screen.blit(surf, (0, 0))

make_bamboo_tree(BAMBOO, 600, 0, 640, 0, 655, 350, 595, 350, DARKOLIVE, BAMBOO2)

# нарисуем деревья из листьев
make_leaf(BAMBOO2, 200, 370, 200, 250, 10)
make_leaf(BAMBOO2, 200, 170, 220, 100, 10)
make_leaf(BAMBOO2, 220, 90, 250, 60, 10)
make_leaf(BAMBOO2, 200, 235, 200, 180, 10)

make_leaf(BAMBOO2, 700, 370, 700, 250, 10)
make_leaf(BAMBOO2, 700, 170, 720, 100, 10)
make_leaf(BAMBOO2, 720, 90, 750, 60, 10)
make_leaf(BAMBOO2, 700, 235, 700, 180, 10)


make_leaf(BAMBOO, 180, 410, 180, 250, 15)
make_leaf(BAMBOO, 180, 235, 170, 180, 14)
make_leaf(BAMBOO, 170, 170, 140, 130, 12)

# нарисуем панду слева от нас
make_left_panda(205, 245, 120, 100)

# нарисуем дерево посередине холста
make_bamboo_tree(BAMBOO, 455, 0, 510, 0, 510, 555, 455, 555, DARKOLIVE, BAMBOO2)

# нарисуем панду справа от нас
make_right_panda(475, 400, 220, 150)

# офигеем от жизни и порадуемся рисунку
pygame.display.update()
clock = pygame.time.Clock()  # object clock, wait some time
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
