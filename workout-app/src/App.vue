<template>
  <v-app>
    <nav-bar :drawer="drawer" />
    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="drawer.open = !drawer.open" />
      <v-toolbar-title>Workout Flows</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import NavBar from "@/components/NavBar.vue";

@Component({
  components: { NavBar }
})
export default class App extends Vue {
  drawer = { open: false };
}
</script>
