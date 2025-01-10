<script lang="ts">
  import anime from 'animejs'

  let box: HTMLElement;

  // アニメーションを開始する関数
  const animateBox = () => {
    anime({
      targets: box,
      translateX: 250, // X方向に250px移動
      duration: 1000,  // アニメーションの時間（ミリ秒）
      easing: 'easeInOutQuad',
    });
  };
</script>

<!-- TailwindCSSでスタイル管理 -->
<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
  <!-- ボタン -->
  <button
    class="px-4 py-2 bg-blue-500 text-white rounded shadow hover:bg-blue-600"
    on:click={animateBox}
  >
    アニメーション開始
  </button>

  <!-- アニメーション対象のボックス -->
  <div
    bind:this={box}
    class="mt-6 w-24 h-24 bg-blue-400 rounded"
  ></div>
</div>
