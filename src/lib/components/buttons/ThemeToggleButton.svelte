<script lang="ts">
  import Icon from "@iconify/svelte";

  let isDarkMode = false
  function toggleDarkTheme() {
    isDarkMode = !isDarkMode
    document.documentElement.classList.toggle("dark")
  }
</script>

<button
  on:click={toggleDarkTheme}
  class="p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors"
>
  {#if isDarkMode}
  <Icon icon="mdi:weather-sunny" />
  {:else}
  <Icon icon="mdi:weather-night" />
  {/if}
</button>