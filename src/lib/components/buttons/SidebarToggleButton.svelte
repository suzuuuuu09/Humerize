<button
  on:click={toggleSidebar}
  class="fixed p-2 rounded-md bg-gray-800 text-white ease-in-out duration-300 transition-all bg-opacity-90
  {$sidebarStore.isMobileWidth ? "left-4" : "-left-32"}"
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