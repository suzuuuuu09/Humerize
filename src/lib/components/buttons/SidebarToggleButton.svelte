<button
  on:click={toggleSidebar}
  class="m-100 p-2 rounded-md text-slate-800 dark:text-white ease-in-out duration-300 transition-all bg-opacity-90 relative
  {$sidebarStore.isMobileWidth ? "right-0" : "right-32 w-0"}"
>
  <Icon icon="{$sidebarStore.isOpen ? "mdi:close" : "mdi:hamburger-menu"}" className="h-6 w-6" />
</button>

<script lang="ts">
  import { sidebarStore } from "$lib/stores/sidebar";
  import Icon from "$lib/components/icons/Icon.svelte";

  function toggleSidebar() {
    sidebarStore.update(state => ({
      ...state,
      isOpen: !state.isOpen
    }));
  }
</script>