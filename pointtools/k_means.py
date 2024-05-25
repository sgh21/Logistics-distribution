import cv2
import numpy as np

def sample_points(points, num_clusters):
    '''
    对点进行采样分组
    input:
        points: 点的坐标 [n,2]
        num_clusters: 聚类的数量
    output:
        sampled_points: 聚类后的点 list[num_clusters, ndarray[m, 2]]
    '''
    # 将数据转换为float32类型
    points = np.float32(points)

    # 定义停止条件，迭代10次或者精度达到1.0
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # 应用k-means聚类
    _, labels, centers = cv2.kmeans(points, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # 初始化一个列表来存储采样的点
    sampled_points = []

    for i in range(num_clusters):
        # 获取当前聚类的点
        cluster_points = points[labels.flatten() == i]
        sampled_points.append(cluster_points)

    # 将列表转换为numpy数组
    sampled_points = [np.array(cluster,dtype=np.int32) for cluster in sampled_points]

    return sampled_points

if __name__=="__main__":
    import sys
    sys.path.append('..')
    from pointtools import GenerateData
    # 生成500个点，代表配送的目标点，x坐标在-150-150之间，y坐标在-150-150之间
    target_points = GenerateData.generate_points(50, -150, 150, -150, 150)
    # 对配送区域进行采样分组
    sample_point = sample_points(target_points, 5)
    print(sample_point)
    print(len(sample_point[0]))
    print(len(sample_point[1]))
    print(len(sample_point[2]))
    print(len(sample_point[3]))
    print(len(sample_point[4]))
    print(sample_point[0][0])
    print(sample_point[1][0])
    print(sample_point[2][0])
    print(sample_point[3][0])
    print(sample_point[4][0])