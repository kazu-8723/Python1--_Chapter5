# scikit-learn(sklearn)に存在するデータをインポート
import sklearn.datasets
# Matplotlibとpyplotインターフェイスのインポート(グラフを作成できる)
import matplotlib.pyplot as plt

# sklearn.datasets内の数値のデータ
digits = sklearn.datasets.load_digits()

# データを50個表示させる
for i in range(50):
    # 5x10に順番に表示
    plt.subplot(5, 10, i + 1)
    # 枠線を非表示
    plt.axis("off")
    # その数字は何か表示
    plt.title(digits.target[i])
    # 数値データをグレーの濃淡画像にする
    plt.imshow(digits.images[i], cmap = "Greys")
# 作成した画像を表示
plt.show()
