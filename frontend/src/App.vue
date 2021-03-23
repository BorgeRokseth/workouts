<template>
  <v-app>
    <NavBar :drawer="drawer" />
    <v-app-bar app dark>
      <v-app-bar-nav-icon @click.stop="drawer.open = !drawer.open" />
      <v-toolbar-title>Workout Flows</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn href="/accounts/logout/" small plain>Logout {{ user }}</v-btn>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavBar from "@/components/NavBar";
import { apiService } from "@/common/api.service";

export default {
  name: "App",
  components: {
    NavBar
  },
  data() {
    return {
      drawer: { open: false },
      user: " "
    };
  },

  methods: {
    getUserDetails() {
      const endpoint = "/api/user/";
      apiService(endpoint).then(data => {
        this.user = data.username;
      });
    }
  },
  created() {
    this.getUserDetails();
  }
};
</script>
