<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
      <v-list>
        <v-list-item-group v-model="selectedItem">
          <v-list-item v-for="(item, i) in menuItems" :key="i">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text" @click="clicked(item.link)" link :to="item.link">
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <h1>Hello</h1>
    <v-app-bar app dark>
      <v-app-bar-nav-icon @click="drawerControl" />
      <v-toolbar-title>Workout Flows </v-toolbar-title>
    </v-app-bar>
    <div>
      <router-view />
    </div>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import ExerciseListView from "@/views/ExerciseListView.vue";

@Component({
  components: { ExerciseListView }
})
export default class App extends Vue {
  drawer = false;
  selectedItem = 1;
  menuItems = [
    { text: "Exercise", icon: `mdi-alpha-e-circle`, link: "/exercises" },
    { text: "Flow", icon: `mdi-alpha-f-circle`, link: "/flows" },
    { text: "Workout", icon: `mdi-alpha-w-circle`, link: "/workouts" }
  ];
  text = "Click me!";

  drawerControl() {
    if (this.drawer === false) {
      this.drawer = true;
    } else {
      this.drawer = false;
    }
    console.log(this.drawer);
  }

  clicked(link: string) {
    console.log("You clicked on: ", link);
  }
}
</script>
