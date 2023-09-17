# 定义一个计算阶乘的函数
def factorial(n):
  # n 是一个正整数
  # 返回 n 的阶乘
  if n == 0 or n == 1:
    # 0 和 1 的阶乘都是 1
    return 1
  else:
    # n 的阶乘等于 n 乘以 n-1 的阶乘
    return n * factorial(n-1)

# 导入计算阶乘的函数

# 向用户询问一个正整数
n = int(input("请输入一个正整数: "))
# 检查输入是否有效
if n >= 0:
  # 计算并打印阶乘结果
  result = factorial(n)
  print(f"{n} 的阶乘是 {result}.")
else:
  # 打印一个错误信息
  print("输入无效，请输入一个正整数.")
