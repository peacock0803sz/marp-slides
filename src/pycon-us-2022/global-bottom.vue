<template>
  <footer
    v-if="$slidev.nav.currentLayout !== 'intro'"
    class="absolute bottom-0 text-right left-0 right-0 p-2"
  >
    {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
  </footer>
</template>