# little cropper for miniARATA (和訳；ミニ新ちゃん用の小さなクロッパー；台譯；小新用小切割器)
It is not easy to obtain 200 × 200 pixel^2 images one by one. So we wrote a simple script for doing it.

200×200ピクセルの画像を1枚ずつ取得するのは簡単ではありません。そのため、簡単なスクリプトを作成しました。

一張一張獲得200×200像素的影像並不容易。因此，我們編寫了一個簡單的code來執行此操作。(方便我們在短時間內切割上萬張圖片)


Background of image collection 背景

We installed three scanners, each with dimensions of 216 × 296 mm^2 (5,100 × 7,020 pixel^2) in Chamaecyparis obtusa (C. obtusa) forest at Kiryu Experimental Watershed (KEW) and Larix kaempferi (K. kaempferi) and Cryptomeria japonica (C. japonica) forests at Shinshu University, totalling 9 individuals. 桐生実験流域（KEW）のヒノキ林と信州大学のカラマツ林とスギ林に、それぞれ216×296mm2（5,100×7,020ピクセル2）のスキャナを3台設置し、合計9個体を撮影しました。

The experiment commenced in August 2020 in the Kiryu forest, with the scanning of root images occurring every hour (31,904 images from 3 scanners at C. obtusa). 実験は2020年8月に桐生林で開始され、1時間ごとに根の画像のスキャンが行われました（C. obtusaでは3台のスキャナから31,904枚の画像）。

Following internal discussions, image data (42 images from 3 scanners at L. kaempferi and 33 images from 3 scanners at C. japonica) were collected at Shinshu University at approximately monthly intervals starting in April 2022. 内部協議の結果、2022年4月から約1ヶ月間隔で信州大学で画像データ（L. kaempferiの3台のスキャナーから42枚の画像、C. japonicaの3台のスキャナーから33枚の画像）が収集されました。

All data collection finished in November 2022. After collecting the data, the first step involved data clearing, followed by the creation of 16.9 × 16.9 mm^2 (400 × 400 pixel^2) bicolour-labelled images for training the ARATA model. すべてのデータ収集は2022年11月に終了しました。データ収集後、最初のステップとしてデータのクリアを行い、続いてARATAモデルのトレーニング用に16.9 × 16.9 mm^2（400 × 400ピクセル^2）の2色ラベル付き画像を作成しました。

Further, we used KEW's image to further crop root tips 200 × 200 pixel^2 images by the little cropper for mini ARATA. さらに、KEWの画像を使用して、小さなクロッパーで根の先端の200 × 200ピクセル^2画像をさらに切り取り、ミニARATAを作成しました。
