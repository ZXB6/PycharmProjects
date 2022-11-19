class bird:
 """
 speed:速度
 position:位置
 fit:适应度
 lBestPosition:经历的最佳位置
 lBestFit:经历的最佳的适应度值
 """
 def __init__(self, speed, position, fit, lBestPosition, lBestFit):
  self.speed = speed
  self.position = position
  self.fit = fit
  self.lBestFit = lBestPosition
  self.lBestPosition = lBestFit