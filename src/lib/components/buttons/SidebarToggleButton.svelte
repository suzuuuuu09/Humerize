<script lang="ts">
	import { sidebarStore } from '$lib/stores/sidebar';
	import Icon from '$lib/components/icons/Icon.svelte';

	function toggleSidebar() {
		sidebarStore.update((state) => ({
			...state,
			isOpen: !state.isOpen
		}));
	}
</script>

<button
	on:click={toggleSidebar}
	class="md:right-60 md:w-0 md:pl-0 right-0 pl-2 m-100 text-slate-800 dark:text-white ease-in-out duration-300 transition-all relative"
>
	<Icon icon={$sidebarStore.isOpen ? 'mdi:close' : 'mdi:hamburger-menu'} className="h-6 w-6" />
</button>
