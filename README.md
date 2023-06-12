# OpenMV-Spike-Prime-Converter
超音波センサのハウジングに取り付けることでOpenMVをSpike Primeで使用可能にする基板とその付属品及びサンプルプログラムです。

オープンソースハードウェアとして公開します。ライセンスはCC BY-NC-SA 4.0です。
+ オープンソースハードウェアとは:https://www.oshwa.org/definition/japanese/
+ CC BY-NC-SA 4.0とは:https://creativecommons.jp/licenses/
## それぞれのファイルについて
ハードウェア
+ board.brd:Eagle互換のボードファイル
+ schematic.sch:Eagle互換の回路図ファイル
+ spacer_FRONT.stl:基板のFRONT側にインサートナットと共に使用する。spacer_BACKと基板本体を固定するパーツ。
+ spacer_BACK.stl:基板のBACK側に使用する。基板とハウジングの隙間を適切な距離にするパーツ。

サンプルプログラム
+ OpenMV_sample.py:OpenMVから回SPIKE Primeに1秒に１回数字の100を送信する。
+ SPIKE_sample.llsp:SPIKE Primeが受信したデータをコンソールに表示する。
## 実装方法
実装例はmount_example.stepを参照
## その他
質問、問題等があった場合はissuesにお願いします。
