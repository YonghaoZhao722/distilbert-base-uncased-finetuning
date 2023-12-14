from datasets import load_dataset

# 加载 IMDb 电影评论数据集
dataset = load_dataset("imdb.py")

# 获取训练集、测试集和无监督数据集
train_data = dataset['train']
test_data = dataset['test']
unsupervised_data = dataset['unsupervised']

# 查看数据集示例
print(train_data[0])  # 查看第一个训练集样本
print(test_data[0])   # 查看第一个测试集样本
print(unsupervised_data[0])  # 查看第一个无监督样本
