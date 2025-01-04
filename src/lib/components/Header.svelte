<script lang="ts">
  import Icon from "@iconify/svelte";
  import ThemeToggleButton from "$lib/components/buttons/ThemeToggleButton.svelte";
  import SidebarToggleButton from "$lib/components/buttons/SidebarToggleButton.svelte";
</script>

<header class="fixed top-0 left-0 right-0 h-16 bg-white dark:bg-slate-800 duration-300 shadow-md z-50 px-4">
  <div class="h-full flex items-center justify-between">
    <div class="flex items-center gap-2 scale-110 pl-2">
      <SidebarToggleButton />
      <Icon icon="mdi:music-note" class="text-xl text-gray-900 dark:text-gray-300 duration-300 transition-colors"/>
      <span class="text-xl font-semibold text-gray-900 dark:text-gray-300 duration-300 transition-colors">Humerize</span>
    </div>
    <div>
      <ThemeToggleButton />
    </div>
  </div>
</header>