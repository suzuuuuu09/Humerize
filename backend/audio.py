import librosa
import numpy as np
import matplotlib.pyplot as plt

def extract_pitch(file_path, sr=None, hop_length=512):
    """
    音声ファイルからピッチを抽出する関数
    
    Parameters:
    -----------
    file_path : str
        音声ファイルのパス
    sr : int or None
        サンプリングレート（Noneの場合、ファイルのデフォルト値を使用）
    hop_length : int
        フレーム間のサンプル数
        
    Returns:
    --------
    times : ndarray
        各フレームの時間（秒）
    pitches : ndarray
        各フレームのピッチ周波数（Hz）
    """
    # 音声ファイルの読み込み
    y, sr = librosa.load(file_path, sr=sr)
    
    # ピッチ抽出
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr, hop_length=hop_length)
    
    # 各フレームで最も強い周波数成分を抽出
    pitches_max = np.zeros(pitches.shape[1])
    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        pitches_max[i] = pitches[index, i]
    
    # 時間軸の生成
    times = librosa.times_like(pitches_max, sr=sr, hop_length=hop_length)
    
    return times, pitches_max

# 使用例
file_path = '440hz.mp3'

try:
    # ピッチ抽出の実行
    times, pitches = extract_pitch(file_path)
    
    # 結果のプロット
    plt.figure(figsize=(12, 6))
    plt.plot(times, pitches)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Pitch Contour')
    plt.grid(True)
    plt.show()
    
    # 基本統計量の表示
    print(f"平均ピッチ: {np.mean(pitches):.2f} Hz")
    print(f"最大ピッチ: {np.max(pitches):.2f} Hz")
    print(f"最小ピッチ: {np.min(pitches):.2f} Hz")

except Exception as e:
    print(f"エラーが発生しました: {str(e)}")