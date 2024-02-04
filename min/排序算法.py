# 排序算法内容
p = [7, 8, 9, 10, 13, 15, 8, 97, 45]  # 随便输入，只要不是字符串
# 正叙
for i in range(len(p)):
    for j in range(len(p)):
        if p[i] < p[j]:
            p[i], p[j] = p[j], p[i]
print(f"正叙{p}")
# 倒叙
for i in range(len(p)):
    for j in range(len(p)):
        if p[i] > p[j]:
            p[i], p[j] = p[j], p[i]
print(f"倒叙{p}")
# 正叙原理：因为p[i] < p[j]，所以p[i],p[j] = p[j],p[i]，这是因为倒叙是从最小数开始的
# 倒叙原理：因为p[i] > p[j]，所以p[i],p[j] = p[j],p[i]，这是因为正叙是从最大数开始的
