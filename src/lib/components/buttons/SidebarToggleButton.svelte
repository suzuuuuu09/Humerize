<button
  on:click={toggleSidebar}
  class="fixed top-4 z-50 p-2 rounded-md bg-gray-800 text-white ease-in-out duration-300 transition-all
  {$sidebarStore.isOpen ? ($sidebarStore.isMobileWidth ? "left-64" : "-left-32") : "left-4"}"
>
  {#if $sidebarStore.isOpen}
    <Icon icon="mdi:close" className="h-6 w-6" />
  {:else}
    <Icon icon="mdi:hamburger-menu" className="h-6 w-6" />
  {/if}
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