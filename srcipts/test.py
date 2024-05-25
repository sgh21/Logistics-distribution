from main import main
import numpy as np
def test_tspsolver():
    start_point = np.array([0, 0])
    n_persons = 5
    axis_range = (-500,500,-500,500)
    modes = ["concorde","greedy","MST"]
    n_points = [50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000]
    
    with open('output.txt', 'w') as f:
        for n in n_points:
            for mode in modes:
                values=0
                solutions, indexs, sample_points, time = main(start_point, n_persons, n, axis_range, mode)
                for i in range(n_persons):
                    values += solutions[i].optimal_value
                f.write(f"n_points: {n}, mode: {mode}, time: {time:0.4f},optimal_value:{values:0.4f}\n")

if __name__=="__main__":
    test_tspsolver()