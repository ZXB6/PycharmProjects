import math
import random
import numpy
import matplotlib.pyplot as plt

Max_iter = 1000  #迭代次数
lb = -100  #下界
ub = 100  #上届
dim = 30  #狼的寻值范围
SearchAgents_no = 5  #寻值的狼的数量

def GWO(objf, lb, ub, dim, SearchAgents_no, Max_iter):
    shuchu = []
    # 初始化 alpha, beta, and delta_pos
    Alpha_pos   = numpy.zeros(dim)  # 位置.形成30的列表
    Alpha_score = float("inf")  # 这个是表示“正负无穷”,所有数都比 +inf 小；正无穷：float("inf"); 负无穷：float("-inf")
    Beta_pos    = numpy.zeros(dim)
    Beta_score  = float("inf")
    Delta_pos   = numpy.zeros(dim)
    Delta_score = float("inf")  # float() 函数用于将整数和字符串转换成浮点数。


    if not isinstance(lb, list):  # 作用：来判断一个对象是否是一个已知的类型。 一为对象，二为类型名，若对象的类型与参数类型相同返回True
        lb = [lb] * dim  # 生成[-100，-100，.....-100]30个
    if not isinstance(ub, list):
        ub = [ub] * dim


    # 初始化所有狼的位置
    Positions = numpy.zeros((SearchAgents_no, dim))  # 5行30列 0
    # print(Positions.dtype)
    x1 = []
    y1 = []

    for i in range(dim):  # 形成5*30个数[-100，100)以内
        Positions[:, i] = numpy.random.uniform(0, 1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]  # 形成[5个0-1的数]*200-100
                            # 从一个均匀分布[low,high)中随机采样                 * 200      -100
                            # low: 采样下界，float类型，默认值为0；
                            # high: 采样上界，float类型，默认值为1；
                            # size: 输出样本数目，为int或元组，size = (m, n, k), 则输出m * n * k个样本，缺省时输出1个值。
                            # 返回值：和参数一致。


    Convergence_curve = numpy.zeros(Max_iter)   # 100个0 的数组


    for l in range(0, Max_iter):  #  循环1000次以迭代寻优 左闭右开
        a = 2 - l * ( 2 / Max_iter)  # a从2线性减少到0  每次少0.02
        #更新 A B D 的scores 和pos的赋值
        for i in range(0, SearchAgents_no): # 5
            # 返回超出搜索空间边界的搜索代理
            for j in range(dim): # 30
                Positions[i, j] = numpy.clip(Positions[i, j], lb[j], ub[j])  # clip这个函数将将数组中的元素限制在a_min(-100), a_max(100)之间，大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min。
                                                  # 数组     最小值-100 最大值100
            # 计算每个搜索代理的目标函数
            fitness = objf(Positions[i, :])              # 把某行数据带入函数计算
            if fitness < Alpha_score:                    # Alpha_score +无穷
                Alpha_score = fitness                    # Update alpha
                Alpha_pos = Positions[i, :].copy()
            if (fitness > Alpha_score and fitness < Beta_score):
                Beta_score = fitness  # Update beta
                Beta_pos = Positions[i, :].copy()
            if (fitness > Alpha_score and fitness > Beta_score and fitness < Delta_score):
                Delta_score = fitness  # Update delta
                Delta_pos = Positions[i, :].copy()

        # 以上的循环里，Alpha《Beta《Delta
        # fitness最小 Positions给 Alpha 最大给Delta

        # 在此循环中更新 灰狼的Positions
        for i in range(0, SearchAgents_no):
            for j in range(0, dim):
                r1 = random.random()  # r1  [0,1]主要生成一个0-1的随机浮点数。
                r2 = random.random()
                A1 = 2 * a * r1 - a  # Equation (3.3)  =a(2*r1-1) 即为[-a，a)  无穷大趋于0
                C1 = 2 * r2          # Equation (3.4)  [0,2)  表示狼所在的位置对猎物影响的随机权重
                # D_alpha表示候选狼与Alpha狼的距离
                D_alpha = abs(C1 * Alpha_pos[j] - Positions[i, j])  # abs() 函数返回数字的绝对值。Alpha_pos[j]表示Alpha位置，Positions[i,j])候选灰狼所在位置
                X1 = Alpha_pos[j] - A1 * D_alpha  # X1表示根据alpha得出的下一代灰狼位置向量

                r1 = random.random()            #
                r2 = random.random()            #
                A2 = 2 * a * r1 - a             #  同上算出到Beta的距离
                C2 = 2 * r2                     #
                D_beta = abs(C2 * Beta_pos[j] - Positions[i, j])
                X2 = Beta_pos[j] - A2 * D_beta

                r1 = random.random()            #
                r2 = random.random()            #
                A3 = 2 * a * r1 - a             #  同上算出到Delta的距离
                C3 = 2 * r2                     #
                D_delta = abs(C3 * Delta_pos[j] - Positions[i, j])
                X3 = Delta_pos[j] - A3 * D_delta

                Positions[i, j] = (X1 + X2 + X3) / 3  # 候选狼的位置更新为根据Alpha、Beta、Delta得出的下一代灰狼地址。

        Convergence_curve[l] = Alpha_score # 收敛曲线值 即1000次迭代每次的最小值
        if (l % 1 == 0):
            y = str(Alpha_score)
            print(['迭代次数为' + str(l) + ' 的迭代结果' + str(Alpha_score)])  # 每一次的迭代结果
        shuchu.append(str(Alpha_score))
    return shuchu

def F1(x):
    #s = numpy.sum(abs(x))            # TODO 此处可以进行优化
    #s = numpy.sum(x**2)
    s = numpy.sum(abs(x**3))
    # 400 x    265迭代 收敛0
    # 400 x**2 180迭代 收敛0
    # 1   x**3 135迭代 收敛0
    # 1   x    160
    return s

x = GWO(F1, lb, ub, dim, SearchAgents_no, Max_iter)
# print(x)
# Position为狼距离猎物的位置