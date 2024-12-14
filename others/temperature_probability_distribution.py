import matplotlib.pyplot as plt
import numpy as np

# ロジット値
logits = [2.0, 1.5, 1.0, 0.5, 0.0]
tokens = ['A', 'B', 'C', 'D', 'E']

# 温度1の確率分布
def softmax(logits, temperature=1):
    exp_logits = np.exp(np.array(logits) / temperature)
    return exp_logits / np.sum(exp_logits)

probs_temp1 = softmax(logits)

# 温度0の確率分布 (近似)
probs_temp0 = [1.0, 0.0, 0.0, 0.0, 0.0]

# グラフの作成
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# 温度1のグラフ
ax[0].bar(tokens, probs_temp1)
ax[0].set_title('Temperature = 1')
ax[0].set_ylabel('Probability')
ax[0].set_ylim([0, 1])

# 温度0のグラフ
ax[1].bar(tokens, probs_temp0)
ax[1].set_title('Temperature ≈ 0')
ax[1].set_ylabel('Probability')
ax[1].set_ylim([0, 1])

plt.tight_layout()
plt.show()
