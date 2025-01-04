<script lang="ts">
  import Icon from "$lib/components/icons/Icon.svelte";

  let isDarkMode = false
  function toggleDarkTheme() {
    isDarkMode = !isDarkMode
    document.documentElement.classList.toggle("dark")
  }
</script>

<button
  on:click={toggleDarkTheme}
  class="p-3 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-700 duration-300"
>
  {#if isDarkMode}
    <Icon icon="mdi:weather-sunny" className="text-2xl text-slate-100 duration-300"/>
  {:else}
    <Icon icon="mdi:weather-night" className="text-2xl text-slate-700 duration-300"/>
  {/if}
</button>