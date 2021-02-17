<template>
  <v-navigation-drawer v-model="drawer.open" app>
    <v-list>
      <v-list-item-group>
        <v-list-item v-for="(item, i) in menuItems" :key="i">
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <router-link :to="item.link">
            <v-list-item-title v-text="item.text">
            </v-list-item-title>
              </router-link>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script lang="ts">
import Vue from 'vue';


export default Vue.extend({
  name: 'NavBar',
  props: ['drawer'],
  data() {
    return {
      menuItems: [{ text: "Exercise", icon: `mdi-alpha-e-circle`, link: "/exercises" },
        { text: "Flow", icon: `mdi-alpha-f-circle`, link: "/flows" },
        { text: "Workout", icon: `mdi-alpha-w-circle`, link: "/workouts" }]
    };
  }
})

</script>
<style scoped>
</style>