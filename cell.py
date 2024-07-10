from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line, 'white')
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            line = Line(Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2),
                        Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2))
            self._win.draw_line(line,"red")
        else:
            line = Line(Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2),
                        Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2))
            self._win.draw_line(line,"gray")
