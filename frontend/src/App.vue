<template>
  <v-app>
    <nav-bar :drawer="drawer" />
    <v-app-bar app dark>
      <v-app-bar-nav-icon @click.stop="drawer.open = !drawer.open" />
      <v-toolbar-title>Workout Flows</v-toolbar-title>
      <v-spacer></v-spacer>
      <a class="btn" href="/accounts/logout/">Logout</a>
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
