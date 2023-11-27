    turtle.hideturtle()
    turtle.speed('fastest')
    marbles = []
    for i in range(rows):
        row = []
        for j in range(columns):
            x = x_offset + j * 3 * marble_radius
            y = y_offset - i * 3 * marble_radius
            marble = Marble(Point(x, y), 'white', marble_radius)
            marble.draw()
            row.append(marble)
        marbles.append(row)
    return marbles