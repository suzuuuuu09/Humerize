<script lang="ts">
  import IconifyIcon from '@iconify/svelte'

  export let icon: string
  export let className = ""
</script>

<IconifyIcon icon={icon} class={className}/>