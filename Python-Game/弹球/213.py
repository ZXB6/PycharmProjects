# -*- coding: utf-8 -*-

import tkinter as tk

# 游戏对象的一些通用方法
class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    # 删除对象
    def delete(self):
        self.canvas.delete(self.item)

    # 得到对象的坐标
    def get_coords(self):
        return self.canvas.coords(self.item)

    # 对象移动
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

class Racket(GameObject):
    def __init__(self, canvas, x, y):
        item = canvas.create_rectangle(x, y, x + 90, y + 10, fill='green')
        super().__init__(canvas, item)

    # 绘制弹板
    def draw(self, offset):
        pos = self.get_coords()
        width = self.canvas.winfo_width()
        # 当弹板在画布内时，按给定偏移量移动
        if pos[0] + offset >= 0 and pos[2] + offset <= width:
            super().move(offset, 0)

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(x, y, x + 20, y + 20, fill='blue')
        super().__init__(canvas, item)

    # 绘制弹球
    def draw(self):
        pos = self.get_coords()
        self.canvas_width = self.canvas.winfo_width()
        # 方向判断
        if pos[1] <= 0:
            self.direction[1] *= -1
        if game.hit_racket():
            self.direction[1] *= -1
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.direction[0] *= -1
        # 偏移量
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

# 游戏类，定义了游戏的完整流程
class Game(tk.Frame):
    def __init__(self, master):
        #调用父类 ( tk.Frame ) 并返回该类实例的__init__方法。
        super().__init__(master)

        self.lives = 3
        self.scores = 0
        self.width = 800
        self.height = 600

        # 设置画板并放置
        self.canvas = tk.Canvas(self, bg='#f8c26c', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()

        self.ball = None
        self.lives_text = None
        self.scores_text = None

        # 初始化弹板
        self.racket = Racket(self.canvas, self.width/2-45, 480)

        self.setup_game()
        # 将键盘焦点转移到画布组件上
        self.canvas.focus_set()

        # 将键盘左右键与弹板左右移动绑定在一起
        self.canvas.bind('<KeyPress-Left>', lambda turn_left: self.racket.draw(-15))
        self.canvas.bind('<KeyPress-Right>', lambda turn_right: self.racket.draw(15))

    # 加载游戏，或预置游戏
    def setup_game(self):
        # 将球设置在弹板中间位置的上方
        self.reset_ball()
        # 预置生命、得分和游戏提示的文本
        self.update_lives_text()
        self.update_scores_text()
        self.text = self.canvas.create_text(400, 200, text='单击鼠标左键开始游戏', font=('Helvetica', 36))
        # 将鼠标左键单击与开始游戏绑定在一起
        self.canvas.bind('<Button-1>', lambda start_game: self.start_game())

    # 在游戏预置时添加弹球，弹球在弹板中间位置的上方
    def reset_ball(self):
        if self.ball != None:
            self.ball.delete()
        racket_pos = self.racket.get_coords()
        x = (racket_pos[0] + racket_pos[2]) * 0.5-10
        self.ball = Ball(self.canvas, x, 350)

    # 更新生命的数字
    def update_lives_text(self):
        text = '生命: %s' % self.lives
        if self.lives_text is None:
            self.lives_text = self.canvas.create_text(60, 30, text=text, font=('Helvetica', 16), fill='green')
        else:
            self.canvas.itemconfig(self.lives_text, text=text)

    # 更新得分的数字
    def update_scores_text(self):
        text = '得分: %s' % self.scores
        if self.scores_text is None:
            self.scores_text = self.canvas.create_text(60, 60, text=text, font=('Helvetica', 16), fill='green')
        else:
            self.scores = self.scores + 1
            text = '得分: %s' % self.scores
            self.canvas.itemconfig(self.scores_text, text=text)

    # 开始游戏
    def start_game(self):
        # 依次解除绑定、重设得分、删除提示文本、开始游戏循环
        self.canvas.unbind('<Button-1>')
        self.reset_score()
        self.canvas.delete(self.text)
        self.game_loop()

    # 重置得分的数字为“ 0 ”
    def reset_score(self):
        self.scores = 0
        text = '得分: %s' % self.scores
        self.canvas.itemconfig(self.scores_text, text=text)

    # 游戏循环
    def game_loop(self):
        # 如果弹球超过底部，则将弹球的速度变为 0，lives 减 1，否则绘制弹球，再次进行游戏循环
        if self.ball.get_coords()[3] >= self.height:
            self.ball.speed = 0
            self.lives -= 1
            # 如果 lives 小于 0，游戏结束，否则调整 scores，重新预置游戏
            if self.lives < 0:
                self.canvas.create_text(400, 200, text='游戏结束', font=('Helvetica', 36), fill='red')
            else:
                self.scores = self.scores - 1
                self.after(1000, self.setup_game)
        else:
            self.ball.draw()
            self.after(50, self.game_loop)

    # 弹球与弹板的碰撞条件，当碰撞一次就更新一次得分
    def hit_racket(self):
        ball_pos = self.ball.get_coords()
        racket_pos = self.racket.get_coords()
        if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
            if ball_pos[3] >= racket_pos[1] and ball_pos[3] <= racket_pos[3]:
                self.update_scores_text()
                return True
        return False

if __name__ == '__main__':
    root = tk.Tk()
    root.title('弹球游戏')
    # 设定窗口大小不可改变
    root.resizable(0, 0)
    # 设定窗口总是显示在最前面
    root.wm_attributes("-topmost", 1)
    game = Game(root)
    game.mainloop()

