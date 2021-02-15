<template>
  <v-navigation-drawer v-model="drawer.open" app>
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
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: `NavBar`,
  props: [`drawer`],
  data() {
    return {
      selectedItem: 1,
      menuItems: [
        { text: `Exercise`, icon: `mdi-border-color` },
        { text: `Flow`, icon: `mdi-airplane` },
        { text: `Workout`, icon: `mdi-clock` }
      ]
    };
  }
});
</script>
