import pandas as pd
import os

# 设置数据文件目录
data_dir = "./_output"
files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".csv")]

count = 0  # 统计包含 "GitHub" 的行数

# 逐个读取文件
for file in files:
    try:
        df = pd.read_csv(file, encoding="utf-8", on_bad_lines="skip")
        count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
    except Exception as e:
        print(f"处理文件 {file} 时出错: {e}")

# 输出总数
print(f"Total lines containing 'GitHub': {count}")

# 保存结果到文件
output_file = os.path.join(data_dir, "github_count.txt")
with open(output_file, "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")

print(f"结果已保存到 {output_file}")

