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
  class="p-2 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-800 duration-300 transition-colors"
>
  {#if isDarkMode}
  <Icon icon="mdi:weather-sunny" class="text-slate-100 duration-300 transition-colors"/>
  {:else}
  <Icon icon="mdi:weather-night" class="text-slate-700 duration-300 transition-colors"/>
  {/if}
</button>