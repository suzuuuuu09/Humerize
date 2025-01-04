import { writable } from "svelte/store";

interface SidebarStore {
  isOpen: boolean;
  isMobileWidth: boolean;
}

export const sidebarStore = writable<SidebarStore>({
  isOpen: false,
  isMobileWidth: false
})