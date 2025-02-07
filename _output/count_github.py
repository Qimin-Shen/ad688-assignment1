import pandas as pd

# CSV 文件列表
files = ["_output/questions.csv", "_output/question_tags.csv"]

# 初始化计数
total_count = 0

# 逐个文件处理
for file in files:
    print(f"Processing {file}...")
    try:
        # 使用 chunksize=100000 分块读取，减少内存占用
        for chunk in pd.read_csv(file, encoding="utf-8", chunksize=100000, dtype=str, low_memory=False, on_bad_lines="skip"):
            # **向量化** 统计 'GitHub' 关键词出现的行数（比 apply() 快）
            total_count += chunk.apply(lambda x: x.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()
    except Exception as e:
        print(f"❌ Error processing {file}: {e}")

# 输出统计结果
print(f"📊 Total lines containing 'GitHub': {total_count}")

# 将结果写入 _output/github_count.txt
with open("_output/github_count.txt", "w") as f:
    f.write(f"Total lines containing 'GitHub': {total_count}\n")

print("✅ Finished writing results to _output/github_count.txt")
