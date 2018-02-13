def draw_grid(line):

    def draw_line(line):
        print('+', '–', '–', '–', '–','+', '–', '–', '–', '–','+')

    def draw_column():
        print('|', ' ', ' ', ' ', ' ','|', ' ', ' ', ' ', ' ','|')

    for item in range(0, line, 4):
        draw_line(line)
        draw_column()
        draw_column()
        draw_column()
        draw_column()
    draw_line(line)

draw_grid(8)
