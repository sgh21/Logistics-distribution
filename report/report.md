## 任务介绍
### 问题描述
### 思路分析
### 问题关键和难点
## 任务实现
### 算法思路
### TSP算法实现
+ concorde算法
    + 算法原理
    + 复杂度分析
    + 最优解or局部最优
+ Greedy 算法
    + 算法原理
    + 复杂度分析
    + 最优解or局部最优 
+ MST 算法
    + 算法原理
    + 复杂度分析
    + 最优解or局部最优
### 结果对比
+ 效率
```
n_points: 50, mode: concorde, time: 0.0083,optimal_value:4711.0000
n_points: 50, mode: greedy, time: 0.0008,optimal_value:5347.2927
n_points: 50, mode: MST, time: 0.0014,optimal_value:5843.0064
n_points: 60, mode: concorde, time: 0.0102,optimal_value:5688.0000
n_points: 60, mode: greedy, time: 0.0005,optimal_value:6728.7854
n_points: 60, mode: MST, time: 0.0018,optimal_value:6287.6182
n_points: 70, mode: concorde, time: 0.0128,optimal_value:5254.0000
n_points: 70, mode: greedy, time: 0.0005,optimal_value:6359.0584
n_points: 70, mode: MST, time: 0.0028,optimal_value:6230.4541
n_points: 80, mode: concorde, time: 0.0157,optimal_value:5752.0000
n_points: 80, mode: greedy, time: 0.0006,optimal_value:6903.9438
n_points: 80, mode: MST, time: 0.0028,optimal_value:6861.9444
n_points: 90, mode: concorde, time: 0.0173,optimal_value:6960.0000
n_points: 90, mode: greedy, time: 0.0008,optimal_value:7945.1175
n_points: 90, mode: MST, time: 0.0050,optimal_value:8191.7237
n_points: 100, mode: concorde, time: 0.0226,optimal_value:7702.0000
n_points: 100, mode: greedy, time: 0.0008,optimal_value:8217.5793
n_points: 100, mode: MST, time: 0.0053,optimal_value:8793.9968
n_points: 200, mode: concorde, time: 0.1028,optimal_value:10823.0000
n_points: 200, mode: greedy, time: 0.0030,optimal_value:11441.5268
n_points: 200, mode: MST, time: 0.0296,optimal_value:13767.9203
n_points: 300, mode: concorde, time: 0.7027,optimal_value:13514.0000
n_points: 300, mode: greedy, time: 0.0086,optimal_value:13713.6186
n_points: 300, mode: MST, time: 0.0864,optimal_value:17278.6560
n_points: 400, mode: concorde, time: 0.5600,optimal_value:15656.0000
n_points: 400, mode: greedy, time: 0.0156,optimal_value:16231.9682
n_points: 400, mode: MST, time: 0.2016,optimal_value:19767.7882
n_points: 500, mode: concorde, time: 0.4175,optimal_value:17234.0000
n_points: 500, mode: greedy, time: 0.0230,optimal_value:17317.7859
n_points: 500, mode: MST, time: 0.3438,optimal_value:22627.6107
n_points: 600, mode: concorde, time: 0.8148,optimal_value:18889.0000
n_points: 600, mode: greedy, time: 0.0359,optimal_value:19430.8973
n_points: 600, mode: MST, time: 0.6173,optimal_value:25193.8965
n_points: 700, mode: concorde, time: 2.5528,optimal_value:20078.0000
n_points: 700, mode: greedy, time: 0.0452,optimal_value:20595.2621
n_points: 700, mode: MST, time: 1.0424,optimal_value:26432.4345
n_points: 800, mode: concorde, time: 2.1579,optimal_value:21454.0000
n_points: 800, mode: greedy, time: 0.0608,optimal_value:22038.3997
n_points: 800, mode: MST, time: 1.2478,optimal_value:28368.4690
n_points: 900, mode: concorde, time: 5.0416,optimal_value:22661.0000
n_points: 900, mode: greedy, time: 0.0791,optimal_value:23408.7368
n_points: 900, mode: MST, time: 1.8246,optimal_value:30315.3464
n_points: 1000, mode: concorde, time: 2.9223,optimal_value:23726.0000
n_points: 1000, mode: greedy, time: 0.1014,optimal_value:24961.7360
n_points: 1000, mode: MST, time: 2.8502,optimal_value:31442.3629
n_points: 1200, mode: concorde, time: 3.5851,optimal_value:25964.0000
n_points: 1200, mode: greedy, time: 0.1460,optimal_value:27166.6678
n_points: 1200, mode: MST, time: 4.0077,optimal_value:35394.8762
n_points: 1400, mode: concorde, time: 5.9574,optimal_value:27903.0000
n_points: 1400, mode: greedy, time: 0.1990,optimal_value:29456.7417
n_points: 1400, mode: MST, time: 6.7171,optimal_value:37053.1129
n_points: 1600, mode: concorde, time: 23.7644,optimal_value:30046.0000
n_points: 1600, mode: greedy, time: 0.2687,optimal_value:31725.7083
n_points: 1600, mode: MST, time: 9.6363,optimal_value:40800.0600
n_points: 1800, mode: concorde, time: 44.5968,optimal_value:31524.0000
n_points: 1800, mode: greedy, time: 0.3397,optimal_value:33311.0576
n_points: 1800, mode: MST, time: 14.2308,optimal_value:42255.0887
n_points: 2000, mode: concorde, time: 90.4802,optimal_value:33003.0000
n_points: 2000, mode: greedy, time: 0.4127,optimal_value:34986.8254
n_points: 2000, mode: MST, time: 20.4292,optimal_value:44374.7902


```
+ optimal_value
## 总结和分析
## 小组分工
+ 共同
    + 方案设计和思路讨论
    + 算法调研
+ 申广辉
    + 主要代码撰写
    + concorde、greedy、MST算法实现和整合
    + 算法可视化以及测试
    + 数据整理，项目整合和上传
    + 报告修改补充
+ 胡宸源
    + 主要报告撰写
    + MST算法实现
    + (你再想两条补充点)