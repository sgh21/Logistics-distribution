import numpy as np

def generate_points(n_points, x_min=0, x_max=100, y_min=0, y_max=100):
    '''
    生成n_points个点,x坐标在x_min和x_max之间,y坐标在y_min和y_max之间
    input:
        n_points: 点的数量
        x_min: x坐标的最小值
        x_max: x坐标的最大值
        y_min: y坐标的最小值
        y_max: y坐标的最大值
    output:
        points: 生成的点
    '''
    x_coords = np.random.randint(x_min, x_max, n_points)
    y_coords = np.random.randint(y_min, y_max, n_points)
    points = np.column_stack((x_coords, y_coords))
    return points

def save_as_npy(points, filename='points.npy'):
    np.save(filename, points)
    print(f"Points saved as {filename}")

def calculate_distance_matrix(points,round=True):
    '''
    计算点之间的距离矩阵
    input:
        points: 点的坐标
        round: 是否四舍五入
    ouput:
        distances: 点之间的距离矩阵
    '''
    
    expanded_points = points[:, np.newaxis, :]
    distances = np.sqrt(np.sum((expanded_points - points)**2, axis=-1))
    if round:
        distances = np.round(distances).astype(int)
    return distances


if __name__=="__main__":
    # 生成100个点，x坐标在0-50之间，y坐标在0-100之间
    points = generate_points(4, 0, 10, 0, 10)
    print(points)
    # 使用生成的点计算距离矩阵
    dist_matrix = calculate_distance_matrix(points)
    print(dist_matrix)
    # 保存为numpy格式
    save_as_npy(points)