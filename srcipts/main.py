import sys
sys.path.append('..')
print   ('sys.path:',sys.path)      
from pointtools import GenerateData,k_means
from pyconcorde.concorde.tsp import TSPSolver
from tsp_solver.greedy import solve_tsp
from MST.mst_solver import mst_path
from solution import Solution
import numpy as np
import matplotlib.pyplot as plt
import time


def tspsolver(points,mode="concorde",norm="EUC_2D"):
    '''
    使用concorde求解TSP问题
    input:
        points: 待求解的点
        norm: 距离的计算方式
    output:
        solution: 求解结果
    '''
    if mode=="concorde":
        solver = TSPSolver.from_data(xs=points[:, 0], ys=points[:, 1], norm=norm)
        solution = solver.solve()
        if solution.found_tour:
            print('Successfully found tour')
            print(solution.optimal_value)
            print(solution.tour)
            print('-----------------')
        else:
            print('Failed to find tour')
    elif mode=="MST":
        path = mst_path(points)
        solution = Solution(path, points)
    elif mode=="greedy":
        dist_matrix = GenerateData.calculate_distance_matrix(points)
        # 获取下三角矩阵并转换为列表
        dist_matrix = np.tril(dist_matrix).tolist()
        path = solve_tsp(dist_matrix)
        solution = Solution(path, points)
    else:
        raise ValueError("mode should be one of 'concorde','MST','greedy'")
    return solution
def visualize_solution(sample_points, solutions, start_point,first_target,mode):
    '''
    可视化解决方案
    input:
        solutions: 求解结果
        first_target: 配送人员第一个目标点的索引
        sample_points: 分组后的点
        start_point: 配送员的起点
    '''
    # 创建一个新的图像
    plt.figure()
    # 设置标题
    plt.title(f"TSP Solution Visualization(mode={mode})")
    # 为每个分组的路径选择一个颜色
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for i, solution in enumerate(solutions):
        # 获取当前分组的路径和目标点
        tour = solution.tour
        path = sample_points[i][tour]
        target = sample_points[i][first_target[i]]

        # 绘制从起点到first_target的路径
        plt.plot([start_point[0], target[0]], [start_point[1], target[1]], color=colors[i % len(colors)])

        # 绘制TSP的解决方案
        plt.plot(*zip(*path), color=colors[i % len(colors)])

        # 连接路径的首尾
        plt.plot([path[0][0], path[-1][0]], [path[0][1], path[-1][1]], color=colors[i % len(colors)])

    # 显示图像
    plt.show()
    

def main(start_point,n_persons, n_points=500,axis_range=(-150,150,-150,150),mode="concorde"):
    '''
    主函数
    input: 
        start_point: 配送员的起点
        n_persons: 配送人员数量
        n_points: 生成的点的数量
        axis_range: 生成的点的范围
        mode : 求解TSP问题的方式
    output:
        solutions: 求解结果
        indexs: 配送人员第一个目标点的索引
        sample_points: 分组后的点
        end_time-start_time: 求解时间
    '''
    if mode == "concorde":
        # 生成500个点，代表配送的目标点，x坐标在-150-150之间，y坐标在-150-150之间
        target_points = GenerateData.generate_points(n_points, axis_range[0], axis_range[1],axis_range[2], axis_range[3])
        # 保存随机数据
        GenerateData.save_as_npy(target_points, '../data/random_points.npy')
    else:
        target_points = np.load('../data/random_points.npy')
    # 对配送区域进行采样分组
    sample_points = k_means.sample_points(target_points, n_persons)

    # 并用TSPSolver求解
    solutions = []
    indexs = []
    start_time = time.time()
    for points in sample_points:
        # 使用concorde求解TSP问题
        solution = tspsolver(points,mode=mode)
        # 找到从起点第一个点的路径
        distance = np.sum((start_point - points)**2, axis=-1)
        index = np.argmin(distance)
        indexs.append(index)
        solutions.append(solution)
    end_time = time.time()
    return solutions, indexs,sample_points, end_time-start_time

if __name__=="__main__":
    start_point = np.array([0, 0])
    n_persons = 5
    mode = "concorde"
    solutions,first_target,sample_points,time_cost = main(start_point,n_persons,2000,axis_range=(-1500,1500,-1500,1500),mode=mode)
    visualize_solution(sample_points,solutions, start_point,first_target,mode)