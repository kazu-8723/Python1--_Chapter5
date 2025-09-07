# Tkinterを読み込み、短くtkという名前で使えるようにする
import tkinter as tk
# Tkinterの中のファイル選択ダイアログ専用モジュールをfdという短い名前で使う。
import tkinter.filedialog as fd
# 画像の読み込み・変換・リサイズ
import PIL.Image
# Pillowの画像をTkinterで表示できる形式(PhotoImage)に変換
import PIL.ImageTk
# scikit-learn(sklearn)に存在するデータをインポート
import sklearn.datasets
# sklearnのSVM(データを分類して境界線を引くためのアルゴリズム)をインポート
import sklearn.svm
# Numpy(Pythonで数値計算を行うためのライブラリ)をインポート
import numpy

# 画像ファイルのパスを受け取る関数を定義。
def imageToData(filename):
    # 画像ファイルを開き、グレースケール("L")に変換
    grayImage = PIL.Image.open(filename).convert("L")
    # 画像を8×8ピクセルに縮小
    grayImage = grayImage.resize((8 ,8), PIL.Image.Resampling.LANCZOS)
    # 縮小した画像を300×300に拡大し、Tkinterで表示できる画像オブジェクト(PhotoImage)に変換(resample=0は最近傍補間)
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300), resample = 0))
    # 画面上のラベル(imageLabel)に、この画像を表示するよう設定
    imageLabel.configure(image = dispImage)
    # 画像オブジェクトをラベルの属性として保持(Tkinterは、PhotoImageへの参照が無くなると画像が消えてしまう(ガベージコレクションされる)ので、どこかに保持しておく必要がある)
    imageLabel.image = dispImage
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


# ボタンから呼ばれる関数を定義
def openFile():
    # ファイルを選ぶダイアログを表示して、選ばれたファイルのパス(文字列)を受け取る
    fpath = fd.askopenfilename()
    # 何かしら選ばれていれば(=空でなければ)、先ほどのimageToDataを呼び出して表示
    if fpath:
        data = imageToData(fpath)

# アプリのメインウィンドウを作成
root = tk.Tk()
# ウィンドウの初期サイズを幅400×高さ400に指定
root.geometry("400x400")

# 置く場所はroot、ボタンの表示文字は"ファイルを開く"、クリックされたらopenFile関数が呼ばれるボタンの作成
btn = tk.Button(root, text = "ファイルを開く", command = openFile)
#
imageLabel = tk.Label()

# packという配置マネージャで、ウィジェットを順に縦へ並べる(記述した順に配置される)
btn.pack()
imageLabel.pack()

# イベントループの開始
tk.mainloop()
