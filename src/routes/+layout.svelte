<script lang="ts">
	import '$lib/app.css';
	import Header from '$lib/components/Header.svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
</script>

<div class="min-h-screen">
	<Header />
	<main class="pt-16 flex bg-white dark:bg-slate-800 transition-colors duration-300 h-screen">
		<Sidebar />
		<slot />
	</main>
</div>
