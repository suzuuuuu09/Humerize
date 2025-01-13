import librosa
import numpy as np
from midiutil import MIDIFile
import math

def audio_to_midi(audio_path, output_midi_path, min_duration=0.1):
    """
    音声ファイルを読み込み、ピッチを抽出してMIDIファイルに変換する
    
    Parameters:
        audio_path (str): 入力音声ファイルのパス
        output_midi_path (str): 出力MIDIファイルのパス
        min_duration (float): 最小ノート長（秒）
    """
    # 音声ファイルの読み込み
    y, sr = librosa.load(audio_path)
    
    # ピッチ抽出
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    
    # 各フレームで最も強い周波数を抽出
    pitches_with_magnitude = []
    for i in range(len(pitches[0])):
        index = magnitudes[:,i].argmax()
        pitch = pitches[index,i]
        if pitch > 0:  # 無音部分を除外
            pitches_with_magnitude.append(pitch)
        else:
            pitches_with_magnitude.append(0)
    
    # MIDIファイルの作成
    midi = MIDIFile(1)  # 1トラック
    track = 0
    time = 0
    midi.addTempo(track, time, 120)  # テンポ設定
    
    # ピッチをMIDIノートに変換
    current_note = None
    note_start_time = 0
    frame_time = librosa.frames_to_time(1, sr=sr)
    
    for i, pitch in enumerate(pitches_with_magnitude):
        if pitch > 0:
            midi_note = int(round(librosa.hz_to_midi(pitch)))
            
            if current_note != midi_note:
                # 前のノートを終了
                if current_note is not None:
                    duration = i * frame_time - note_start_time
                    if duration >= min_duration:
                        midi.addNote(track, 0, current_note, note_start_time, duration, 100)
                
                # 新しいノートの開始
                current_note = midi_note
                note_start_time = i * frame_time
        else:
            # 無音部分の処理
            if current_note is not None:
                duration = i * frame_time - note_start_time
                if duration >= min_duration:
                    midi.addNote(track, 0, current_note, note_start_time, duration, 100)
                current_note = None
    
    # 最後のノートの処理
    if current_note is not None:
        duration = len(pitches_with_magnitude) * frame_time - note_start_time
        if duration >= min_duration:
            midi.addNote(track, 0, current_note, note_start_time, duration, 100)
    
    # MIDIファイルの保存
    with open(output_midi_path, "wb") as f:
        midi.writeFile(f)

# 使用例
if __name__ == "__main__":
    audio_to_midi("sample.wav", "output.mid")