from turtle import Turtle
from typing import List
from food import Food
from settings import left_border, right_border, top_border, bottom_border
from segment import Segment


class Snake:
    def __init__(self):
        self.segments: List[Segment] = [Segment(0, 0), Segment(-20, 0), Segment(-40, 0)]
        self.head = self.segments[0]
        self.base_speed = 10
        self.easy_speed = 11
        self.inter_speed = 12
        self.hard_speed = 15
        self.extreme_speed = 20
        self.speed = self.base_speed
        self.score = 0

    def __get_segment_position(self, index: int):
        return self.segments[index].position()

    def __get_heading(self, index: int):
        return self.segments[index].heading()

    def __set_heading(self, direction):
        current_heading = self.__get_heading(0)
        match direction:
            case "up":
                if current_heading == 0:
                    self.head.setheading(current_heading - 90 % 360)
                elif current_heading == 180:
                    self.head.setheading(current_heading + 90 % 360)
            case "right":
                if current_heading == 270:
                    self.head.setheading(current_heading + 90 % 360)
                elif current_heading == 90:
                    self.head.setheading(current_heading - 90 % 360)
            case "down":
                if current_heading == 0:
                    self.head.setheading(current_heading + 90 % 360)
                elif current_heading == 180:
                    self.head.setheading(current_heading - 90 % 360)
            case "left":
                if current_heading == 270:
                    self.head.setheading(current_heading - 90 % 360)
                elif current_heading == 90:
                    self.head.setheading(current_heading + 90 % 360)

    def __segments_follow(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_position = self.__get_segment_position(i - 1)
            self.segments[i].setposition(next_position)

    def __add_segment(self):
        x, y = self.__get_segment_position(-1)
        segment = Segment(x, y)
        self.segments.append(segment)

    def __has_collided_with(self, items: [Turtle], distance: int):
        collided = False
        for item in items:
            if self.head.distance(item) < distance:
                collided = True
        return collided

    def __has_collided_with_wall(self):
        head_position_x = self.__get_segment_position(0)[0]
        head_position_y = self.__get_segment_position(0)[1]

        if (head_position_x <= left_border or
                head_position_x >= right_border or
                head_position_y >= top_border or
                head_position_y <= bottom_border):
            return True
        else:
            return False

    def __update_speed(self):
        match self.score:
            case self.score if self.score == 5 and self.speed == self.base_speed:
                self.speed = self.easy_speed
            case self.score if self.score == 15 and self.speed == self.easy_speed:
                self.speed = self.inter_speed
            case self.score if self.score == 25 and self.speed == self.inter_speed:
                self.speed = self.hard_speed
            case self.score if self.score == 35 and self.speed == self.hard_speed:
                self.speed = self.extreme_speed

    def check_game_over(self):
        return self.__has_collided_with_wall() or self.__has_collided_with(self.segments[1:], 5)

    def move_forward(self):
        if not self.check_game_over():
            previous_heading = self.__get_heading(0)
            previous_position = self.__get_segment_position(0)
            self.__segments_follow()
            match previous_heading:
                case previous_heading if previous_heading == 0:
                    self.head.setposition((previous_position[0] + self.speed, previous_position[1]))
                case previous_heading if previous_heading == 90:
                    self.head.setposition((previous_position[0], previous_position[1] - self.speed))
                case previous_heading if previous_heading == 180:
                    self.head.setposition((previous_position[0] - self.speed, previous_position[1]))
                case previous_heading if previous_heading == 270:
                    self.head.setposition((previous_position[0], previous_position[1] + self.speed))
            self.__update_speed()

    def move_right(self):
        self.__set_heading("right")

    def move_left(self):
        self.__set_heading("left")

    def move_up(self):
        self.__set_heading("up")

    def move_down(self):
        self.__set_heading("down")

    def eat(self, food: Food):
        if self.__has_collided_with([food], 17):
            self.__add_segment()
            self.score += 1
            return True
        return False
