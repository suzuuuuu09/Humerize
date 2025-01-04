<div class="min-h-screen">
	<Header />
	<main class="pt-16 flex bg-white dark:bg-slate-800 transition-colors duration-300 h-screen">
		<Sidebar />
		<h1 class="text-4xl text-blue-500 dark:text-indigo-200 duration-300">Hello world!</h1>
		<div class=""></div>
	</main>
</div>

<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
</script>
