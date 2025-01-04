<div class="relative">
  <!-- Mobile menu button -->
  <button
    on:click={() => isOpen = !isOpen}
    class={`fixed top-4 z-50 p-2 rounded-md bg-gray-800 text-white ease-in-out duration-300 transition-all
    ${isOpen ? "left-64" : "left-0"}`}
  >
    {#if isOpen}
      <Icon icon="mdi:close" className="h-6 w-6" />
    {:else}
      <Icon icon="mdi:hamburger-menu" className="h-6 w-6" />
    {/if}
  </button>
<!-- class="h-full w-64 bg-white dark:bg-slate-800 duration-300 shadow-md z-40 transition-colors" -->
  <!-- Sidebar -->
  <div
    class="fixed top-0 left-0 h-full bg-white text-white dark:bg-slate-800 transition-all shadow-md duration-300 ease-in-out"
    class:w-64={isOpen}
    class:w-0={!isOpen}
  >
    <div class="p-4 {!isOpen ? 'hidden' : ''}">
      <h2 class="text-xl font-bold mb-4">Sidebar</h2>
      <nav>
        <ul class="space-y-2">
          <li>
            <a href="/" class="block py-2 px-4 hover:bg-gray-700 rounded">Home</a>
          </li>
          <li>
            <a href="/" class="block py-2 px-4 hover:bg-gray-700 rounded">About</a>
          </li>
          <li>
            <a href="/" class="block py-2 px-4 hover:bg-gray-700 rounded">Contact</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</div>

<script lang="ts">
  import { onMount } from "svelte";
  import Icon from "$lib/components/icons/Icon.svelte"

  let isOpen = true;
  let isMobileWidth = false;
  function checkWidth(){
    isMobileWidth = window.innerWidth < 768;
    isOpen = isMobileWidth ? false : true;
  }

  onMount(() => {
    checkWidth();
    window.addEventListener("resize", checkWidth);
    return () => window.removeEventListener("resize", checkWidth);
  });
</script>