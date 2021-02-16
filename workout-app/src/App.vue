<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
      <v-list>
        <v-subheader>MENU</v-subheader>
        <v-list-item-group v-model="selectedItem">
          <v-list-item v-for="(item, i) in menuItems" :key="i">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app dark>
      <v-app-bar-nav-icon @click="drawerControl" />
      <v-toolbar-title>Workout Flows </v-toolbar-title>
    </v-app-bar>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {}
})
export default class App extends Vue {
  drawer = false;
  selectedItem = 1;
  menuItems = [
    { text: `Exercise`, icon: `mdi-alpha-e-circle` },
    { text: `Flow`, icon: `mdi-alpha-f-circle` },
    { text: `Workout`, icon: `mdi-alpha-w-circle` }
  ];

  drawerControl() {
    if (this.drawer === false) {
      this.drawer = true;
    } else {
      this.drawer = false;
    }
    console.log(this.drawer);
  }
}
</script>
