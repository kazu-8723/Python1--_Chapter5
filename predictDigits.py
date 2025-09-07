# scikit-learn(sklearn)に存在するデータをインポート
import sklearn.datasets
# sklearnのSVM(データを分類して境界線を引くためのアルゴリズム)をインポート
import sklearn.svm
# Pillow(画像処理を行うにあたって用いられるライブラリ(PIL; Python Imaging Library))をインポート
import PIL.Image
# Numpy(Pythonで数値計算を行うためのライブラリ)をインポート
import numpy

# 画像ファイルを数値リストに変換
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    # 数値リストに変換
    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    numImage = numImage.flatten()
    # 戻り値として返す
    return numImage

# 数字を予測
def predictDigits(data):
    # 学習用データを読み込む
    digits = sklearn.datasets.load_digits()
    # 機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    # 予測結果の表示
    n = clf.predict([data])
    print("予測 = ", n)

# 画像ファイルを数値リストに変換
data = imageToData("2.png")
# 数字を予測
predictDigits(data)
