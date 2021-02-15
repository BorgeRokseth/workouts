<template>
  <v-app-bar color="deep-purple accent-4" dense dark>
    <v-app-bar-nav-icon
      @click.stop="drawer.open = !drawer.open"
    ></v-app-bar-nav-icon>
    <v-toolbar-title>Workout Flows</v-toolbar-title>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {}
})
export default class App extends Vue {
  drawer = { open: false };
}
</script>
