#!/bin/bash
# 统计 _output 目录下包含 "python" 的行数

# 设置初始计数
count=0

# 遍历 _output 目录下的所有 CSV 文件
for file in _output/*.csv; do
    echo "Processing $file..."
    file_count=$(grep -i "python" "$file" | wc -l)
    count=$((count + file_count))
done

# 输出结果
echo "Total lines containing 'python': $count"

# 将结果保存到 _output/python_count.txt
echo "Total lines containing 'python': $count" > _output/python_count.txt

