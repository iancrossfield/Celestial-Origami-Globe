from PIL import Image, ImageDraw
# 2024-04-18 19:46 IJMC: Added sortxyxy() to ensure correct ordering
#                        for draw.rectangle.

def sortxyxy(fourlist):
    """Sort [x0,y0,x1,y1] to ensure that
        x0 < x1 and y0 < y1.
    """
    # 2024-04-18 19:29 IJMC: Created 
    x0,y0,x1,y1 = fourlist
    xvals = [x0,x1]
    yvals = [y0,y1]
    xvals.sort()
    yvals.sort()
    x0,x1 = xvals
    y0,y1 = yvals
    return([x0,y0,x1,y1])

def draw_triangles(img, top, right, bottom, left):
    width = img.width
    height = img.height
    draw = ImageDraw.Draw(img)

    if (top):
        draw.polygon([(0, 0), (width / 2, height / 2), (width, 0)], fill = 'white')

    if (right):
        draw.polygon([(width, 0), (width / 2, height / 2), (width, height)], fill = 'white')

    if (bottom):
        draw.polygon([(0, height), (width / 2, height / 2), (width, height)], fill = 'white')

    if (left):
        draw.polygon([(0, 0), (width / 2, height / 2), (0, height)], fill = 'white')

    return img

def draw_white_lines(img):
    width = img.width
    height = img.height
    draw = ImageDraw.Draw(img)

    draw.line((width * (1/8), height * (1/8), width * (1/8), height * (3/8)), fill = 'white', width = 5)
    draw.line((width * (3/8), height * (1/8), width * (3/8), height * (3/8)), fill = 'white', width = 5)
    draw.line((width * (5/8), height * (1/8), width * (5/8), height * (3/8)), fill = 'white', width = 5)
    draw.line((width * (7/8), height * (1/8), width * (7/8), height * (3/8)), fill = 'white', width = 5)

    draw.line((width * (1/8), height * (5/8), width * (1/8), height * (7/8)), fill = 'white', width = 5)
    draw.line((width * (3/8), height * (5/8), width * (3/8), height * (7/8)), fill = 'white', width = 5)
    draw.line((width * (5/8), height * (5/8), width * (5/8), height * (7/8)), fill = 'white', width = 5)
    draw.line((width * (7/8), height * (5/8), width * (7/8), height * (7/8)), fill = 'white', width = 5)

    return img

def draw_black_lines(img):
    width = img.width
    height = img.height
    draw = ImageDraw.Draw(img)


    #black box around whole image
    draw.line((0, 0, width, 0), fill = 'black', width = 2)
    draw.line((0, 0, 0, height), fill = 'black', width = 2)
    draw.line((0, height - 2, width, height - 2), fill = 'black', width = 2)
    draw.line((width - 2, 0, width - 2, height), fill = 'black', width = 2)

    #the two horizotnal lines
    draw.line((0, height * (3/8), width, height * (3/8)), fill = 'black', width = 3)
    draw.line((0, height * (5/8), width, height * (5/8)), fill = 'black', width = 3)

    #zig-zag lines in top row - from left to right
    draw.line((0, height * (1/4), width * (1/8), height * (3/8)), fill = 'black', width = 3)
    draw.line((width * (1/8), height * (3/8), width * (1/4), height * (1/4)), fill = 'black', width = 3)
    draw.line((width * (1/4), height * (1/4), width * (3/8), height * (3/8)), fill = 'black', width = 3)
    draw.line((width * (3/8), height * (3/8), width * (1/2), height * (1/4)), fill = 'black', width = 3)
    draw.line((width * (1/2), height * (1/4), width * (5/8), height * (3/8)), fill = 'black', width = 3)
    draw.line((width * (5/8), height * (3/8), width * (3/4), height * (1/4)), fill = 'black', width = 3)
    draw.line((width * (3/4), height * (1/4), width * (7/8) - 2, height * (3/8)), fill = 'black', width = 3)
    draw.line((width * (7/8), height * (3/8), width, height * (1/4)), fill = 'black', width = 3)

    #zig zag lines in bottom row - left to right
    draw.line((0, height * (3/4), width * (1/8), height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (1/8), height * (5/8), width * (1/4), height * (3/4)), fill = 'black', width = 3)
    draw.line((width * (1/4), height * (3/4), width * (3/8) - 3, height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (3/8), height * (5/8), width * (1/2), height * (3/4)), fill = 'black', width = 3)
    draw.line((width * (1/2), height * (3/4), width * (5/8), height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (5/8) + 3, height * (5/8), width * (3/4), height * (3/4)), fill = 'black', width = 3)
    draw.line((width * (3/4), height * (3/4), width * (7/8) - 3, height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (7/8), height * (5/8), width, height * (3/4)), fill = 'black', width = 3)

    #vertical borders
    draw.line((width * (1/8), height * (3/8), width * (1/8), height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (3/8), height * (3/8), width * (3/8), height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (5/8), height * (3/8), width * (5/8), height * (5/8)), fill = 'black', width = 3)
    draw.line((width * (7/8), height * (3/8), width * (7/8), height * (5/8)), fill = 'black', width = 3)

    return img

def draw_shapes(img, color):
    # 2024-04-18 19:35 IJMC: Added sortxyxy calls to ensure correct coordinate ordering.

    width = img.width
    height = img.height
    draw = ImageDraw.Draw(img)

    #draw vertical lines down center of image
    draw.line((width / 2, 2, width / 2, height / 4), fill = color, width = 40)    
    draw.line((width / 2, height * (3/4), width / 2, height - 4), fill = color, width = 40)

    #draw the 4 boxes around the image
    draw.rectangle((width / 8, 2, width / 4, height * (1/8)), fill = color)
    draw.rectangle((width / 8, height * (7/8), width / 4, height - 4), fill = color)
    ###draw.rectangle((width * (7/8), 2, width * (3/4), height * (1/8)), fill = color)
    xy = sortxyxy((width * (7/8), 2, width * (3/4), height * (1/8)))
    draw.rectangle(xy, fill=color)
    ###draw.rectangle((width * (7/8), height * (7/8), width * (3/4), height - 4), fill = color)
    xy = sortxyxy((width * (7/8), height * (7/8), width * (3/4), height - 4))
    draw.rectangle(xy, fill=color)

    #draw diagonal lines towards center
    draw.line((2, 2 , width / 4, height / 4), fill = color, width = 3)
    draw.line((2, height - 2, width * (1/4), height * (3/4)), fill = color, width = 3)
    draw.line((width - 2, height - 4, width * (3/4), height * (3/4)), fill = color, width = 3)
    draw.line((width - 2, 2, width * (3/4), height * (1/4)), fill = color, width = 3)

    #dashed lines towards center
    cur_height = height / 4
    cur_width = width / 4

    while (cur_width < (width / 2) - 20):
        draw.line((cur_width, cur_height, cur_width + 10, cur_height - 10), fill = color, width = 3)
        cur_width += 20
        cur_height -= 20

    cur_width = width * (3/4)
    cur_height = height / 4

    while (cur_width > (width / 2) + 20):
        draw.line((cur_width, cur_height, cur_width - 10, cur_height - 10), fill = color, width = 3)
        cur_width -= 20
        cur_height -= 20

    cur_width = width / 4
    cur_height = height * (3/4)

    while (cur_width < (width / 2) - 20):
        draw.line((cur_width, cur_height, cur_width + 10, cur_height + 10), fill = color, width = 3)
        cur_width += 20
        cur_height += 20

    cur_width = width * (3/4)
    cur_height = height * (3/4)

    while (cur_width > (width / 2) + 20):
        draw.line((cur_width, cur_height, cur_width - 10, cur_height + 10), fill = color, width = 3)
        cur_width -= 20
        cur_height += 20

    #dotted lines
    cur_width = 2
    cur_height = height * (7/8)

    while (cur_width < (width / 8)):
        draw.line((cur_width, cur_height, cur_width + 3, cur_height), fill = color, width = 4)
        cur_width += 9

    cur_width = width - 4
    
    while (cur_width > (width * (7/8))):
        draw.line((cur_width, cur_height, cur_width - 3, cur_height), fill = color, width = 4)
        cur_width -= 9

    cur_width = 2
    cur_height = height / 8

    while (cur_width < (width / 8)):
        draw.line((cur_width, cur_height, cur_width + 3, cur_height), fill = color, width = 4)
        cur_width += 9

    cur_width = width - 4
    
    while (cur_width > (width * (7/8))):
        draw.line((cur_width, cur_height, cur_width - 3, cur_height), fill = color, width = 4)
        cur_width -= 9

    #dot-dash lines
    cur_width = width / 8
    cur_height = height / 8
    dot = False

    while (cur_height < height * (3/8) - 2):
        if (dot):
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 10
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 15
            dot = False
        else:
            draw.line((cur_width, cur_height, cur_width, cur_height + 10), fill = color, width = 3)
            cur_height += 20
            dot = True

    cur_width = width * (7/8)
    cur_height = height / 8
    dot = False

    while (cur_height < height * (3/8) - 2):
        if (dot):
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 10
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 15
            dot = False
        else:
            draw.line((cur_width, cur_height, cur_width, cur_height + 10), fill = color, width = 3)
            cur_height += 20
            dot = True

    cur_width = width / 8
    cur_height = height * (5/8) + 2

    dot = False

    while (cur_height < height * (7/8)):
        if (dot):
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 10
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 15
            dot = False
        else:
            draw.line((cur_width, cur_height, cur_width, cur_height + 10), fill = color, width = 3)
            cur_height += 20
            dot = True

    cur_width = width * (7/8)
    cur_height = height * (5/8) + 2

    dot = False

    while (cur_height < height * (7/8)):
        if (dot):
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 10
            draw.line((cur_width, cur_height, cur_width, cur_height + 3), fill = color, width = 3)
            cur_height += 15
            dot = False
        else:
            draw.line((cur_width, cur_height, cur_width, cur_height + 10), fill = color, width = 3)
            cur_height += 20
            dot = True

    return img
