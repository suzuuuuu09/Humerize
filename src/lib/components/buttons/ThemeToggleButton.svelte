<script lang="ts">
  import Icon from "$lib/components/icons/Icon.svelte";

  let Theme = [
    "light",
    "dark",
    "system"
  ];

  let isDarkMode = false;
  function toggleDarkTheme() {
    isDarkMode = !isDarkMode;
    document.documentElement.classList.toggle("dark");
  }
</script>

<button
  on:click={toggleDarkTheme}
  class="p-3 rounded-lg hover:bg-slate-300 dark:hover:bg-slate-700 duration-300"
>
  <Icon icon="{isDarkMode ? 'mdi:weather-sunny' : 'mdi:weather-night'}" className="text-2xl duration-300
    {isDarkMode ? 'text-slate-100' : 'text-slate-700'}"
  />
</button>