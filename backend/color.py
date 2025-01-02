from time import sleep

class Text_color:
    def __init__(self):
        pass

    def gaming_color(self, text: str, interval: float = 0.02):
        def hsv_to_rgb(h, s, v):
            h = float(h)
            s = float(s)
            v = float(v)

            hi = int(h / 60) % 6
            f = h / 60 - hi
            p = v * (1 - s)
            q = v * (1 - f * s)
            t = v * (1 - (1 - f) * s)

            if hi == 0:
                r, g, b = v, t, p
            elif hi == 1:
                r, g, b = q, v, p
            elif hi == 2:
                r, g, b = p, v, t
            elif hi == 3:
                r, g, b = p, q, v
            elif hi == 4:
                r, g, b = t, p, v
            elif hi == 5:
                r, g, b = v, p, q

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            return [r, g, b]

        h, s, v = 0, 0.8, 1
        # 画面をクリアして、カーソルを非表示
        print("\033[2J\033[?25l", end="")
        # テキストを一度だけ出力し、カーソルを先頭に戻す
        print(text)
        print(f"\033[{text.count(chr(10)) + 1}A", end="")
        
        try:
            while True:
                h += 1
                rgb = hsv_to_rgb(h, s, v)
                r, g, b = rgb
                # 色だけを変更して同じ位置に出力
                print(f"\033[38;2;{r};{g};{b}m{text}", flush=True, end="")
                # カーソルを元の位置に戻す
                print(f"\033[{text.count(chr(10)) + 1}A", end="")
                sleep(interval)
                if h >= 360:
                    h = 0
        except KeyboardInterrupt:
            # プログラム終了時にカーソルを再表示
            print("\033[?25h")
            return

if __name__ == "__main__":
    color = Text_color()
    word = """\
                  ■■       ■■       ■■    ■■■■■■   
                 ■  ■     ■  ■     ■  ■   ■        
                ■    ■    ■  ■    ■    ■  ■        
                ■■   ■   ■    ■   ■■   ■  ■        
                     ■   ■    ■        ■  ■ ■■■    
                    ■    ■    ■       ■   ■■   ■   
                   ■     ■    ■      ■    ■     ■  
                   ■     ■    ■      ■          ■  
                  ■      ■    ■     ■           ■  
                 ■       ■    ■    ■      ■■    ■  
                 ■   ■   ■    ■    ■   ■  ■     ■  
                ■    ■    ■  ■    ■    ■   ■   ■   
                ■■■■■■    ■  ■    ■■■■■■    ■■■    
      ■                     ■          ■                            
      ■            ■        ■          ■                    ■       
  ■■■■■■■■■■■      ■        ■          ■      ■■     ■      ■       
     ■            ■■        ■          ■■■■■   ■■    ■      ■       
     ■   ■        ■   ■■■■■■■■■■■  ■■■■■        ■    ■■ ■■■■■■■     
     ■■■■■■■      ■         ■          ■              ■■■  ■  ■■■   
   ■■■   ■ ■■■    ■         ■          ■              ■    ■    ■   
  ■■ ■   ■   ■    ■         ■          ■ ■■■■■■      ■■■   ■    ■■  
  ■  ■   ■   ■■   ■         ■          ■■■    ■■     ■ ■■ ■■     ■  
 ■■  ■  ■     ■   ■         ■        ■■■       ■■   ■■  ■ ■      ■  
 ■   ■  ■     ■   ■ ■       ■       ■■ ■        ■   ■   ■■■      ■  
 ■   ■ ■     ■■   ■■       ■■      ■■  ■        ■   ■    ■      ■■  
 ■   ■■      ■     ■       ■       ■   ■       ■■   ■  ■■■■     ■   
  ■■■      ■■■            ■■       ■  ■■      ■■     ■■■  ■   ■■■   
         ■■■             ■■         ■■■     ■■■             ■■■     
"""
    color.gaming_color(word)