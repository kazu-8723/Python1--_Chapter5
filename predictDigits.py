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
    # 画像を 8×8 ピクセルに縮小。LANCZOS は高品質な縮小用フィルタ。
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    # Pillowの画像をNumPy配列(浮動小数)に変換。
    numImage = numpy.asarray(grayImage, dtype = float)
    '''
    画素値（0〜255）を 0〜16 の整数 にスケーリングし、さらに黒ほど値が大きくなるよう反転。
    17 * 値 / 256 → 0〜16.9… を floor で 0〜16 に。
    16 - (...) によって、黒(0)→16, 白(255)→0。
    これは scikit-learn の digits データセット（8×8, 画素値 0〜16, 濃いほど大）と同じ表現に合わせるため。
    '''
    numImage = 16 - numpy.floor(17 * numImage / 256)
    # (8, 8)を1次元(長さ64)のベクトルに平坦化。SVMに渡せる形にする。
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
