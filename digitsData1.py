# scikit-learn(sklearn)に存在するデータをインポート
import sklearn.datasets
# Matplotlibとpyplotインターフェイスのインポート(グラフを作成できる)
import matplotlib.pyplot as plt

# sklearn.datasets内の数値のデータ
digits = sklearn.datasets.load_digits()

'''
# 画像データを数値で表示している
# データの個数を表示
print("データの個数=", len(digits.images))
# １つ目の画像データの表示
print("画像データ=", digits.images[0])
# １つ目の数字の表示
print("何の数字か=", digits.target[0])
'''

# 数値データをグレーの濃淡画像にする
plt.imshow(digits.images[0], cmap = "Greys")
# 作成した画像を表示
plt.show()

