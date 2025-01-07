<div class="relative">
  <div
    class="fixed top-0 left-0 h-full bg-white dark:bg-slate-800 transition-all duration-300 ease-in-out {$sidebarStore.isOpen ? 'w-64' : 'w-0'}"
  >
    <!-- SidebarContent -->
    <div class="p-4 transition-all duration-300 w-64 {$sidebarStore.isOpen ? 'translate-x-0' : '-translate-x-full'}">
      <h2 class="text-xl font-bold mb-4">Sidebar</h2>
      <nav>
        <ul class="space-y-2">
          <li>
            <a href="/" class="block py-2 px-4 hover:bg-gray-700 rounded">Home</a>
          </li>
          <li>
            <a href="/about" class="block py-2 px-4 hover:bg-gray-700 rounded">About</a>
          </li>
          <li>
            <a href="/contact" class="block py-2 px-4 hover:bg-gray-700 rounded">Contact</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</div>

<script lang="ts">
  import { onMount } from "svelte";
  import { sidebarStore } from "$lib/stores/sidebar";

  onMount(() => {
    const checkWidth = () => {
      const isMobile = window.innerWidth < 768;
      sidebarStore.update(state => ({
        ...state,
        isMobileWidth: isMobile,
        isOpen: isMobile ? false : true
      }));
    };

    checkWidth();
    window.addEventListener("resize", checkWidth);
    return () => window.removeEventListener("resize", checkWidth);
  });
</script>