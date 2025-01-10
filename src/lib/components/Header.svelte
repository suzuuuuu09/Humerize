<script lang="ts">
  import Icon from "$lib/components/icons/Icon.svelte";
  import ThemeToggleButton from "$lib/components/buttons/ThemeToggleButton.svelte";
  import SidebarToggleButton from "$lib/components/buttons/SidebarToggleButton.svelte";
</script>

<header class="fixed top-0 left-0 right-0 h-16 duration-300 shadow-md z-50">
  <div class="h-full flex items-center justify-between">
    <!-- SidebarContent -->
    <div class="flex items-center gap-2 scale-110 pl-2">
      <!-- RightContent -->
      <SidebarToggleButton />
      <Icon icon="mdi:music-note" className="text-xl text-gray-900 dark:text-gray-300 duration-300 transition-colors"/>
      <span class="text-xl font-semibold text-gray-900 dark:text-gray-300 duration-300 transition-colors">Humerize</span>
    </div>
    <div>
      <!-- LeftContent -->
      <ThemeToggleButton />
    </div>
  </div>
</header>