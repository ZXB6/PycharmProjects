import random
import sd


class PSO:
      """
      fitFunc:适应度函数
      birdNum:种群规模
      w:惯性权重
      c1,c2:个体学习因子，社会学习因子
      solutionSpace:解空间，列表类型：[最小值，最大值]
      """
      def __init__(self, fitFunc, birdNum, w, c1, c2, solutionSpace):
          self.fitFunc = fitFunc
          self.w = w
          self.c1 = c1
          self.c2 = c2
          self.birds, self.best = self.initBirds(birdNum, solutionSpace)

      def initBirds(self, size, solutionSpace):
          birds = []
          for i in range(size):
              position = random.uniform(solutionSpace[0], solutionSpace[1])
              speed = 0
              fit = self.fitFunc(position)
              birds.append(birds(speed, position, fit, position, fit))
          best = birds[0]
          for bird in birds:
              if bird.fit > best.fit:
                  best = bird
          return birds, best

      def updateBirds(self):
          for bird in self.birds:
              # 更新速度
              bird.speed = self.w * bird.speed + self.c1 * random.random() * (
                          bird.lBestPosition - bird.position) + self.c2 * random.random() * (
                                       self.best.position - bird.position)
              # 更新位置
              bird.position = bird.position + bird.speed
              # 跟新适应度
              bird.fit = self.fitFunc(bird.position)
              # 查看是否需要更新经验最优
              if bird.fit > bird.lBestFit:
                  bird.lBestFit = bird.fit
                  bird.lBestPosition = bird.position

      def solve(self, maxIter):
          # 只考虑了最大迭代次数，如需考虑阈值，添加判断语句就好
          for i in range(maxIter):
              # 更新粒子
              self.updateBirds()
              for bird in self.birds:
                  # 查看是否需要更新全局最优
                  if bird.fit > self.best.fit:
                     self.best = bird
